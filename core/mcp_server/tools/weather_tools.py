from typing import Any, Dict, Optional
import os
import httpx
import csv
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
import json
import asyncio
load_dotenv('/mnt/e/project/langgraph_mcp_agent/.env')

mcp = FastMCP("weather")

AMAP_API_BASE_URL = "https://restapi.amap.com/v3/weather/weatherInfo?parameters"
AMAP_API_KEY = os.getenv('AMAP_API_KEY')

def get_city_adcode(city_name:str) -> Optional[str]:
    """
    根据城市名称获取城市编码
    """
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file_path = os.path.join(current_dir, "AMap_adcode_citycode.csv")
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            next(reader)
            for row in reader:
                if city_name in row["city"].strip():
                    city_adcode = row["adcode"].strip()

                    return city_adcode
    except FileNotFoundError:
        print("城市编码文件未找到")
    return None

async def send_amap_request(params: Dict[str, Any]) -> Dict[str, Any]:
    """
    发送请求到高德API
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(AMAP_API_BASE_URL, params=params, timeout=10.0)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"请求高德API失败: {e}")
        return None
    
def parse_current_weather(weather_data: Dict[str, Any]) -> str:
    """解析高德地图API返回的天气数据并格式化为字符串
    
    Args:
        weather_data: 高德地图API返回的天气数据
        
    Returns:
        格式化后的天气信息字符串
    """
    if not weather_data or "lives" not in weather_data or not weather_data["lives"]:
        return "无法获取天气信息或数据格式错误"
    
    live = weather_data["lives"][0]
    
    return f"""
城市: {live.get('city', '未知')}
天气: {live.get('weather', '未知')}
温度: {live.get('temperature', '未知')}°C
风向: {live.get('winddirection', '未知')}
风力: {live.get('windpower', '未知')}级
湿度: {live.get('humidity', '未知')}%
发布时间: {live.get('reporttime', '未知')}
"""

def parse_forecast_weather(weather_data: Dict[str, Any]) -> str:
    """解析高德地图API返回的天气预报数据并格式化为字符串
    
    Args:
        weather_data: 高德地图API返回的天气预报数据
        
    Returns:
        格式化后的天气预报信息字符串
    """
    if not weather_data or "forecasts" not in weather_data or not weather_data["forecasts"]:
        return "无法获取天气预报信息或数据格式错误"
    
    forecast = weather_data["forecasts"][0]
    casts = forecast.get("casts", [])
    city = forecast.get('city', '未知')
    
    if not casts:
        return "没有可用的天气预报数据"
    
    forecasts = []
    for cast in casts:
        day_forecast = f"""
日期: {cast.get('date', '未知')}
白天天气: {cast.get('dayweather', '未知')}
白天温度: {cast.get('daytemp', '未知')}°C
白天风向: {cast.get('daywind', '未知')}
白天风力: {cast.get('daypower', '未知')}级
夜间天气: {cast.get('nightweather', '未知')}
夜间温度: {cast.get('nighttemp', '未知')}°C
夜间风向: {cast.get('nightwind', '未知')}
夜间风力: {cast.get('nightpower', '未知')}级
"""
        forecasts.append(day_forecast)
    
    return f"城市: {city}\n\n" + "\n---\n".join(forecasts)

@mcp.tool()
async def get_current_weather(city: str) -> str:
    """
    获取当前天气信息
    :param city: 城市名称
    :return: 当前天气信息字符串
    """
    city_adcode = get_city_adcode(city)
    if not city_adcode:
        return f"无法找到城市 '{city}' 的编码"
    
    params = {
        "key": AMAP_API_KEY,
        "city": city_adcode,
        "extensions": "base"
    }
    
    weather_data = await send_amap_request(params)
    
    if not weather_data:
        return "获取天气信息失败，请稍后再试"
    
    return parse_current_weather(weather_data)

@mcp.tool()
async def get_forecast_weather(city: str) -> str:
    """
    获取天气预报信息
    :param city: 城市名称
    :return: 天气预报信息字符串
    """
    city_adcode = get_city_adcode(city)
    if not city_adcode:
        return f"无法找到城市 '{city}' 的编码"
    
    params = {
        "key": AMAP_API_KEY,
        "city": city_adcode,
        "extensions": "all"
    }
    
    weather_data = await send_amap_request(params)
    
    if not weather_data:
        return "获取天气预报信息失败，请稍后再试"
    
    return parse_forecast_weather(weather_data)


if __name__ == "__main__":

    mcp.run(transport="stdio")
    