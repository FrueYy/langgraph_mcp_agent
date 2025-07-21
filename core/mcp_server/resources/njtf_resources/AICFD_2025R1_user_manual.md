# AICFD 2025R1用户手册

![](media/image1.png)

---

## 前言
本手册所提及的概念、方法和实例仅为说明及培训之目的，并不意欲应用于实际工程分析和设计。材料参数仅供参考。南京天洑软件有限公司不对因使用本手册信息造成的直接或间接损失承担责任。

**联系我们：**  
邮箱：info@njtf.cn  
官网：www.njtf.cn  
微信客服：Tianfu_Software  
微信公众号：天洑CAE技术源  

![](media/image2.png) ![](media/image3.png)

Copyright © 2025 南京天洑软件有限公司  
江宁开发区苏源大道19号九龙湖国际企业总部园B1栋11层/5层  

---

# 目录

- [AICFD 2025R1用户手册](#aicfd-2025r1用户手册)
  - [前言](#前言)
- [目录](#目录)
  - [1. 系统概述 ](#1-系统概述-)
    - [1.1 产品概要 ](#11-产品概要-)
    - [1.2 功能简介 ](#12-功能简介-)
      - [1.2.1 模型读入 ](#121-模型读入-)
      - [1.2.2 网格划分 ](#122-网格划分-)
      - [1.2.3 网格生成 ](#123-网格生成-)
      - [1.2.4 前前处理 ](#124-前前处理-)
      - [1.2.5 求解器 ](#125-求解器-)
      - [1.2.6 后处理 ](#126-后处理-)
    - [1.3 操作流程 ](#13-操作流程-)
  - [2. 界面功能介绍 ](#2-界面功能介绍-)
    - [2.1 菜单栏 ](#21-菜单栏-)
    - [2.2 视口界面 ](#22-视口界面-)
    - [2.3 视口工具栏 ](#23-视口工具栏-)
    - [2.4 日志输出窗口 ](#24-日志输出窗口-)
  - [3. 前前处理（Pre-pre processing） ](#3-前前处理pre-pre-processing-)
    - [3.1 界面布局与功能 ](#31-界面布局与功能-)
      - [3.1.1 顶端导航栏 ](#311-顶端导航栏-)
      - [3.1.2 问答主页面 ](#312-问答主页面-)
      - [3.1.3 结果缩略图 ](#313-结果缩略图-)
      - [3.1.4 功能按键 ](#314-功能按键-)
      - [3.1.5 保存与退出 ](#315-保存与退出-)
    - [3.2 应用案例 ](#32-应用案例-)
      - [3.2.1物理现象](#321物理现象)
      - [3.2.2湍流模型](#322湍流模型)
      - [3.2.3边界条件](#323边界条件)
      - [3.2.4总结页面](#324总结页面)
  - [4. 文件（File） ](#4-文件file-)
    - [4.1 文件格式说明 ](#41-文件格式说明-)
    - [4.2 新建（New） ](#42-新建new-)
    - [4.3 打开（Open） ](#43-打开open-)
    - [4.4 恢复（Recover） ](#44-恢复recover-)
    - [4.5 打开最近工程（Open Recent） ](#45-打开最近工程open-recent-)
    - [4.6 保存（Save） ](#46-保存save-)
    - [4.7 另存（Save As） ](#47-另存save-as-)
    - [4.8 关闭（Close） ](#48-关闭close-)
    - [4.9 退出（Exit） ](#49-退出exit-)
  - [5. 几何（Geometry） ](#5-几何geometry-)
    - [5.1 导入几何（Import Geometry） ](#51-导入几何import-geometry-)
    - [5.2 压印（Imprint） ](#52-压印imprint-)
    - [5.3 内流抽体（Internal Flow Extration） ](#53-内流抽体internal-flow-extration-)
    - [5.4 外流场创建（Outflow Field Creation） ](#54-外流场创建outflow-field-creation-)
    - [5.5 几何检查（Geometry Inspection） ](#55-几何检查geometry-inspection-)
    - [5.6 几何剖切（Geometry Clip） ](#56-几何剖切geometry-clip-)
  - [6. 网格（Mesh） ](#6-网格mesh-)
    - [6.1 导入面网格（Read Surface Mesh） ](#61-导入面网格read-surface-mesh-)
    - [6.2 水密性检查（Tightness Inspection） ](#62-水密性检查tightness-inspection-)
    - [6.3 导入体网格（Import Volume Mesh） ](#63-导入体网格import-volume-mesh-)
    - [6.4 导出体网格（Export Volume Mesh） ](#64-导出体网格export-volume-mesh-)
    - [6.5 网格参数（Mesh Parameters） ](#65-网格参数mesh-parameters-)
      - [6.5.1 全局尺寸（Global Size） ](#651-全局尺寸global-size-)
      - [6.5.2 体网格（Volume Mesh） ](#652-体网格volume-mesh-)
      - [6.5.3 面网格（Surface Mesh） ](#653-面网格surface-mesh-)
      - [6.5.4 边界层（Boundary Layers） ](#654-边界层boundary-layers-)
    - [6.6 网格加密（Mesh Density） ](#66-网格加密mesh-density-)
      - [6.6.1创建](#661创建)
      - [6.6.2生成](#662生成)
      - [6.6.3修改尺寸](#663修改尺寸)
      - [6.6.4加密设置](#664加密设置)
    - [6.7 创建面网格（Create Surface Mesh） ](#67-创建面网格create-surface-mesh-)
    - [6.8 配置（Config） ](#68-配置config-)
    - [6.9 创建网格（Create Volume Mesh） ](#69-创建网格create-volume-mesh-)
    - [6.10 转化多面体（Transform Polyhedra） ](#610-转化多面体transform-polyhedra-)
    - [6.11 停止创建网格（Stop） ](#611-停止创建网格stop-)
    - [6.12 信息统计（Mesh Info） ](#612-信息统计mesh-info-)
    - [6.13 网格质量（Mesh Quality） ](#613-网格质量mesh-quality-)
      - [6.13.1快速面网格质量报告（Quick Mesh Quality）](#6131快速面网格质量报告quick-mesh-quality)
      - [6.13.2快速体网格质量报告（Quick Mesh Quality）](#6132快速体网格质量报告quick-mesh-quality)
      - [6.13.3网格质量检查（Mesh Mesh Quality）](#6133网格质量检查mesh-mesh-quality)
    - [6.14 删除网格（Delete Mesh） ](#614-删除网格delete-mesh-)
    - [6.15 网格切面（Mesh Clip） ](#615-网格切面mesh-clip-)
    - [6.16 AI 网格（AI Mesh） ](#616-ai-网格ai-mesh-)
    - [6.17 恢复原始网格（Restore original mesh） ](#617-恢复原始网格restore-original-mesh-)
  - [7. 求解（Solution） ](#7-求解solution-)
    - [7.1 材料设置 （Material） ](#71-材料设置-material-)
    - [7.2 计算域设置 （Domain） ](#72-计算域设置-domain-)
    - [7.3 边界条件设置（Boundary Condition） ](#73-边界条件设置boundary-condition-)
      - [7.3.1固壁边界（Wall）](#731固壁边界wall)
      - [7.3.2速度入口边界（Velocity Inlet）](#732速度入口边界velocity-inlet)
      - [7.3.3质量流量入口边界（Mass flow Inlet）](#733质量流量入口边界mass-flow-inlet)
      - [7.3.4静压入口边界（Static Pressure Inlet）](#734静压入口边界static-pressure-inlet)
      - [7.3.5总压入口边界（Total Pressure Inlet）](#735总压入口边界total-pressure-inlet)
      - [7.3.6压力出口边界（Pressure Outlet）](#736压力出口边界pressure-outlet)
      - [7.3.7质量流量出口边界（Mass flow Outlet）](#737质量流量出口边界mass-flow-outlet)
      - [7.3.8对称面（Symmetry）](#738对称面symmetry)
      - [7.3.9 动态边界条件 ](#739-动态边界条件-)
    - [7.4 交界面设置（Interface） ](#74-交界面设置interface-)
    - [7.5 边界条件导入、导出（Import、Export Boundary） ](#75-边界条件导入导出importexport-boundary-)
    - [7.6用户点设置 （User Point）](#76用户点设置-user-point)
    - [7.7热源（Heat Source）](#77热源heat-source)
    - [7.8平面热源（Planar Heat Source）](#78平面热源planar-heat-source)
    - [7.9风扇（Fans）](#79风扇fans)
    - [7.10边界热阻（Heat Resistant）](#710边界热阻heat-resistant)
    - [7.11热管元件（Heat Pipe）](#711热管元件heat-pipe)
    - [7.12印制电路板（PCB）](#712印制电路板pcb)
    - [7.13 双热阻（Dual Thermal Resistance）](#713-双热阻dual-thermal-resistance)
    - [7.14计算域初始化 （Initialize）](#714计算域初始化-initialize)
    - [7.15启动求解 （Run Solver）](#715启动求解-run-solver)
    - [7.16停止求解 （Stop Run）](#716停止求解-stop-run)
    - [7.17均方根残差 （RMS Residuals ）](#717均方根残差-rms-residuals-)
    - [7.18可视化求解结果 （Post Process Results）](#718可视化求解结果-post-process-results)
  - [8. 后处理（Post） ](#8-后处理post-)
    - [8.1 导入结果文件（Load Result） ](#81-导入结果文件load-result-)
    - [8.2 时序文件选择器（TimeStep Selector） ](#82-时序文件选择器timestep-selector-)
    - [8.3 用户自定义位置（Location） ](#83-用户自定义位置location-)
    - [8.4 矢量图（Vector） ](#84-矢量图vector-)
    - [8.5 云图 （Contour） ](#85-云图-contour-)
    - [8.6 流线图 （Streamline） ](#86-流线图-streamline-)
    - [8.7 绘图 （Chart） ](#87-绘图-chart-)
    - [8.8 动画演示 （Animation） ](#88-动画演示-animation-)
    - [8.9 对比（Compare） ](#89-对比compare-)
    - [8.10 探针（Probe） ](#810-探针probe-)
    - [8.11 变换 （Transform） ](#811-变换-transform-)
    - [8.12 旋转机械后处理模块（TurboPost） ](#812-旋转机械后处理模块turbopost-)
    - [8.13 模型显示状态窗口 （View） ](#813-模型显示状态窗口-view-)
    - [8.14 导出求解结果 （Export Data） ](#814-导出求解结果-export-data-)
  - [9. 树节点 ](#9-树节点-)
    - [9.1 几何（Geometry） ](#91-几何geometry-)
    - [9.2 网格（Mesh） ](#92-网格mesh-)
      - [9.2.1加密区域（Mesh Density）](#921加密区域mesh-density)
      - [9.2.2网格域（Mesh Domains）](#922网格域mesh-domains)
    - [9.3 仿真模拟（Simulation） ](#93-仿真模拟simulation-)
      - [9.3.1求解模型（Solution Modeling）](#931求解模型solution-modeling)
      - [9.3.2材料（Material）](#932材料material)
      - [9.3.3流体域分析（Flow Analysis）](#933流体域分析flow-analysis)
        - [9.3.3.1计算域（Domains）](#9331计算域domains)
        - [9.3.3.2交界面（Interfaces）](#9332交界面interfaces)
        - [9.3.3.3热模型（Thermal Models）](#9333热模型thermal-models)
      - [9.3.4求解设置（Solver Setting）](#934求解设置solver-setting)
      - [9.3.5求解控制（Solver Controls）](#935求解控制solver-controls)
      - [9.3.6计算域初始化（Field Initialization）](#936计算域初始化field-initialization)
      - [9.3.7监控（Monitoring）](#937监控monitoring)
    - [9.4 后处理（Post） ](#94-后处理post-)
      - [9.4.1结果（Result）](#941结果result)
      - [9.4.2报告（Report）](#942报告report)
      - [9.4.3场景（Scene）](#943场景scene)
      - [9.4.4旋转机械后处理（Turbo Post）](#944旋转机械后处理turbo-post)
  - [10. 工具 （Tools） ](#10-工具-tools-)
    - [10.1 单位设置 ](#101-单位设置-)
    - [10.2 语言 ](#102-语言-)
    - [10.3 高级设置 ](#103-高级设置-)
    - [10.4 自定义函数 ](#104-自定义函数-)
    - [10.5 自定义标量](#105-自定义标量)
    - [10.5 自定义标量 ](#105-自定义标量-)
    - [10.6 界面显示功能 ](#106-界面显示功能-)
    - [10.7 宏录制 ](#107-宏录制-)
    - [11. 帮助（Help） ](#11-帮助help-)
    - [11.1 用户手册 ](#111-用户手册-)
    - [11.2 案例手册 ](#112-案例手册-)
    - [11.3 用户许可 ](#113-用户许可-)
    - [11.4 关于 ](#114-关于-)
    - [12. 操作简介 ](#12-操作简介-)
    - [12.1 新建工程 ](#121-新建工程-)
    - [12.2 导入模型 ](#122-导入模型-)
    - [12.3 可视化已导入几何模型 ](#123-可视化已导入几何模型-)
      - [12.3.1 平移、缩放和旋转视图 ](#1231-平移缩放和旋转视图-)
      - [12.3.2 高亮 ](#1232-高亮-)
    - [12.4 网格划分 ](#124-网格划分-)
      - [12.4.1 网格尺寸 ](#1241-网格尺寸-)
      - [12.4.2 定义边界表面 ](#1242-定义边界表面-)
      - [12.4.3 体网格/面网格/边界层 ](#1243-体网格面网格边界层-)
      - [12.4.4 局部加密 ](#1244-局部加密-)
    - [12.5 创建网格 ](#125-创建网格-)
    - [12.6 求解分析 ](#126-求解分析-)
      - [12.6.1 设置求解模型 ](#1261-设置求解模型-)
      - [12.6.2 材料设置 ](#1262-材料设置-)
      - [12.6.3 建立流体域分析模型 ](#1263-建立流体域分析模型-)
        - [12.6.3.1 设置计算域 ](#12631-设置计算域-)
        - [12.6.3.2 设置边界条件 ](#12632-设置边界条件-)
      - [12.6.4 求解设置 ](#1264-求解设置-)
      - [12.6.5 求解控制 ](#1265-求解控制-)
      - [12.6.6 计算域初始化 ](#1266-计算域初始化-)
    - [12.7 运行求解 ](#127-运行求解-)
    - [12.8 后处理 ](#128-后处理-)
      - [12.8.1 云图 ](#1281-云图-)
      - [12.8.2 矢量图 ](#1282-矢量图-)
      - [12.8.3 流线图 ](#1283-流线图-)
    - [13. 旋转机械模块（Turbomachinery） ](#13-旋转机械模块turbomachinery-)
      - [13.1 新建工程（New Project） ](#131-新建工程new-project-)
      - [13.2 基础设置（Basic Settings） ](#132-基础设置basic-settings-)
      - [13.3 计算域定义（Component Definition） ](#133-计算域定义component-definition-)
      - [13.4 物理参数定义（Physics Definition） ](#134-物理参数定义physics-definition-)
      - [13.5 交界面定义（Interface Definition） ](#135-交界面定义interface-definition-)
      - [13.6 边界定义（Boundaries Definition） ](#136-边界定义boundaries-definition-)
      - [13.7 进入常规模式（Enter General Mode） ](#137-进入常规模式enter-general-mode-)
    - [14. 旋转机械后处理（Turbo Post） ](#14-旋转机械后处理turbo-post-)
      - [14.1 模型初始化（Turbo Initialization） ](#141-模型初始化turbo-initialization-)
      - [14.2 三维视图（3D View） ](#142-三维视图3d-view-)
      - [14.3 叶间平面（Blade-to-Blade） ](#143-叶间平面blade-to-blade-)
      - [14.4 子午面（Meridional） ](#144-子午面meridional-)
      - [14.5 自定义位置（Location） ](#145-自定义位置location-)
        - [14.5.1 曲面位置信息展示（Turbo Surface） ](#1451-曲面位置信息展示turbo-surface-)
        - [14.5.2 曲线位置信息展示（Turbo Line） ](#1452-曲线位置信息展示turbo-line-)
          - [14.5.2.1 入口至出口（Inlet to Outlet） ](#14521-入口至出口inlet-to-outlet-)
          - [14.5.2.2 径向曲线（Hub to Shroud） ](#14522-径向曲线hub-to-shroud-)
          - [14.5.2.3 圆周方向（Circumferential） ](#14523-圆周方向circumferential-)
      - [14.6 图表（Turbo Chart） ](#146-图表turbo-chart-)
        - [14.6.1 叶片载荷（Blade Loading） ](#1461-叶片载荷blade-loading-)
        - [14.6.2 圆周面（Circumferential） ](#1462-圆周面circumferential-)
        - [14.6.3 径向曲线（Hub to Shroud ） ](#1463-径向曲线hub-to-shroud--)
        - [14.6.4 入口至出口（Inlet to Outlet） ](#1464-入口至出口inlet-to-outlet-)

---

## 1. 系统概述 <a name="1-系统概述"></a>

### 1.1 产品概要 <a name="11-产品概要"></a>  
AICFD是一款通用的智能热流体仿真软件，实现对流动及传热的快速智能仿真。其功能包括模型导入、网格自动生成、快速仿真、结果可视化和智能加速，支持Windows、Linux跨平台操作。  

### 1.2 功能简介 <a name="12-功能简介"></a>  

#### 1.2.1 模型读入 <a name="121-模型读入"></a>  
软件前处理支持导入STEP和IGES等格式几何文件，支持导入STL格式面网格文件。  

#### 1.2.2 网格划分 <a name="122-网格划分"></a>  
软件支持对几何文件和面网格文件进行网格划分。用户通过网格基本尺寸设置，以及对面网格、体网格、自定义区进行加密设置和边界层设置后，可一键生成网格文件。 

#### 1.2.3 网格生成 <a name="123-网格生成"></a>  
软件支持生成四面体，六面体，多面体，三棱柱，四棱锥形式网格。完成网格设置后可进行一键快速生成网格。 

#### 1.2.4 前前处理 <a name="124-前前处理"></a>  
通过智能引导问答的形式，从应用场景的语言出发，配合图文结合的帮助示例，自动为用户推荐最合适的湍流、多相流、传热、边界条件等配置，帮助用户合理、快速地使用CFD软件。 

#### 1.2.5 求解器 <a name="125-求解器"></a>  
软件求解器采用有限体积法，数值求解不可压缩的Navier-Stokes 方程组。压力-速度耦合算法包括SIMPLE、PISO 等，同时具备对应的动网格算法，包括滑移网格法等，支持如下问题的求解：
a.稳态及非稳态问题；
b.共轭传热及自然散热问题；
c.可压缩及不可压缩问题；
d.层流和湍流问题，其中，支持的湍流模型包括：RANS 模型，如S-A、k-ε、k-ω等；
e.DES、LES等脱体涡模型；
f.多相流、空化，相变问题；
g.噪声问题；
h.考虑重力加速度的流动问题。
针对上述问题，软件提供了丰富的常用介质材料数据库，以及用户自定义材料属性功能；提供了各种常用边界类型供用户选择及定义。
软件支持基于Microsoft MPI 协议的并行计算，具有优异的大规模并行计算能力。  

#### 1.2.6 后处理 <a name="126-后处理"></a>  
针对计算结果，软件支持丰富的流场可视化功能，包括：
a.云图；
b.矢量图；
c.流线图
d.等值面；
e.动画；
f.结果对比
g.探针
h.曲线图；
i.创建点，线，面，体查看对应后处理结果；
j.视图半透明化展现物体内部结构；
k.图片保存；
l.残差曲线；
m.用户自定义变量监控曲线；
n.数据自动保存。 

### 1.3 操作流程 <a name="13-操作流程"></a>  
1. 新建工程  
2. 导入几何文件  
3. 创建网格  
4. 设置边界条件  
5. 定义流动参数  
6. 运行求解  
7. 后处理分析  

---

## 2. 界面功能介绍 <a name="2-界面功能介绍"></a>  
AICFD 界面主要由上方菜单栏，左侧树节点，视口界面和日志输出窗口四部分组成。
a. 菜单栏（红框）：菜单栏采用Ribbon菜单格式，包含“文件（File）”，“几何（Geometry）”，“网格（Mesh）”，“求解（Solver）”，“后处理（Post）”，“工具（Tools）”，“帮助（Help）”八个菜单项；
b. 工具栏（紫框）：每一个菜单项都有对应的操作按钮或图标，用户点击按钮或图标，可在弹出对话框设置相关参数，或是直接执行某个运行命令；
c. 左侧（橙框）：“树”结构形式展示了当前工程的所有信息，包含已输入的几何，生成的网格或导入的网格、计算域设置、求解器及物理模型、多域参数设置，边界条件、初始化、监控、可视化等相关设置；
d. 树节点右侧“视图”区（绿框）：可进行几何，计算域网格及流场数据的可视化交互操作，仿真计算残差、数据可视化（曲线）。“视图”窗口右侧为可视化快捷操作按钮；
e. 右下方“日志（Output Message）”区（黄框）：仿真过程中输出相关统计数据，或操作日志信息。
![](media/image4.png)
图 2-1软件界面

### 2.1 菜单栏 <a name="21-菜单栏"></a>  
菜单栏主要是对当前工程的新建，打开，恢复，保存，另存，关闭功能。
![](media/image5.png)
图 2-2 菜单栏

### 2.2 视口界面 <a name="22-视口界面"></a>  
视口界面共分为6个显示窗口：前前处理、几何、前处理（网格）、监控、后处理、图表。
a.前前处理：导入网格后，可进入向导式前前处理；
b.几何窗口：导入几何文件后可通过几何窗口查看，新建的辅助几何也在该窗口显示；
c.前处理（网格窗口）： 网格创建完成后会在此窗口显示带网格的几何信息，从外界导入的网格模型也会在此窗口中显示；
d.监控窗口：显示残差曲线和用户自定义点变量曲线；
e.后处理窗口：显示所有后处理结果云图，矢量图，流线图等；
f.图表窗口：显示创建的Chart图表，与其他几个窗口不同，图表窗口只有在用户创建图表时弹出。
![](media/image6.png)
图 2-3 视口界面图 

### 2.3 视口工具栏 <a name="23-视口工具栏"></a>  
为了更好地显示当前几何模型，视口区工具栏提供了丰富地显示工具，从上到下依次为：自适应，刷新，+X，-X，+Y，-Y，+Z，-Z轴方向显示，区域放大，标尺功能。
a.自适应：视口中模型可适应视口大小居中显示；
  ![](media/image7.png)![](media/image8.png)
图 2-4 视口区域放大/自适应效果

b.刷新：调整模型进行全局显示；
![](media/image9.png)
图 2-5 视口刷新效果

c.+X，-X，+Y，-Y，+Z，-Z轴方向显示；
  
  
  ![](media/image10.png)![](media/image11.png)![](media/image12.png)![](media/image13.png)![](media/image14.png)![](media/image15.png)
图 2-6 视图效果

d.区域放大：用户可通过鼠标拉选区域，实现局部放大；

![](media/image16.png)![](media/image17.png)
图 2-7 局部放大

e.标尺：用户可以点击标尺来查看当前模型尺寸，便于划分网格及设置参数；
![](media/image18.png)
图 2-8 标尺工具

f.背景颜色设置：点击后弹出背景设置窗口，渐变（Use Gradient）选项可设置视口区域由上到下渐变。  


### 2.4 日志输出窗口 <a name="24-日志输出窗口"></a>  
日志输出窗口用于输出进程信息。
![](media/image19.png)
图 2-9 日志输出窗口  

---

## 3. 前前处理（Pre-pre processing） <a name="3-前前处理pre-pre-processing"></a>  
前前处理 功能入口位于视口区上方页签处，点击 开始 进入前前处理模块。注意：需要保证AICFD中已有网格导入，否则 开始 按键无法选择。
![](media/image20.png)
图 3-1 前前处理模块入口

### 3.1 界面布局与功能 <a name="31-界面布局与功能"></a>  
点击 开始 后，系统弹出 前前处理设置 面板，其界面布局如下：
![](media/image21.png)
图 3-2 前前处理设置界面布局

#### 3.1.1 顶端导航栏 <a name="311-顶端导航栏"></a>  
其作用为显示当前智能问答的进度，包括 物理现象 、湍流模型 、边界条件 、总结 四个部分，正在进行和已完成的环节会用蓝色表示，未进行的部分会用灰色表示；  

#### 3.1.2 问答主页面 <a name="312-问答主页面"></a>  
其作用为交互式问答
a.大部分问题的下方有按键，展开可查看帮助信息，以图文形式为主；双击图片，可查看大图；
![](media/image23.png)
图 3-3 前前处理帮助系统

b.答案输入分为5种类形式：单选、多选、输入框、弹窗、复杂综合情况；
![](media/image24.png)
图 3-4 前前处理 – 单选输入示例
![](media/image25.png)
图 3-5前前处理 – 多选输入示例
![](media/image26.png)
图 3-6 前前处理 – 输入框示例
![](media/image27.png)
图 3-7 前前处理 – 弹窗输入示例
![](media/image28.png)
图 3-8 前前处理 – 复杂综合情况

c.该功能为动态问答，即上一问题的答案会决定下一问题的内容，以首个问题为例：当问题 1.1仿真场景中流体的数量 答案为1时，系统判断用户希望仿真单相流单组分场景，则问题 1.2 变为选择 流体类型，只能选择 气体 或者 液体；当问题 1.1仿真场景中流体的数量 答案为2时，系统判断用户希望仿真多相流或者多组分场景，则问题 1.2 变为选择 多种流体之间的相对分布情况。
![](media/image29.png)
图 3-9 前前处理 – 仿真场景中流体的数量为1
![](media/image30.png)
图 3-10 前前处理 – 仿真场景中流体的数量为2

#### 3.1.3 结果缩略图 <a name="313-结果缩略图"></a>  
位于左侧边栏，实时反映截至目前用户所有的答案记录，便于用户回溯。
注意：与计算域相关的问题答案由于内容过多，不会记录在左侧缩略图中。
![](media/image31.png)
图 3-11 前前处理 – 计算域相关信息不计入缩略图 

#### 3.1.4 功能按键 <a name="314-功能按键"></a>  
位于右下角，各子功能详情如下：
a.下一页：在本页问答进行完毕后，主页面下方会提示 已完成本页，点击「下一页」继续配置，下一页 按键激活，可切换至 顶端导航栏 的下一个部分；
![](media/image32.png)
图 3-12 前前处理 – 「下一页」功能按键示意图
b.重置：点击 重置 后，主界面出现弹窗，点击 重置当前页 或 重置所有页，即可清空当前页所选内容或所有页所选内容；
![](media/image33.png)
图 3-13 前前处理 – 「重置」功能按键示意图
c.返回：点击后可 返回 上一页。注意，点击后本页内容会被清空；
![](media/image34.png)
图 3-14 前前处理 – 「返回」功能按键示意图
d.确定：确定 分为两种情况。当顶部导航栏状态为 物理现象 、湍流模型、边界条件 时，点击 确定 可直接到达 总结 页面；当顶部导航栏状态为 总结 时，点击 确定 代表用户已完成前前处理，回到AICFD主窗口；用户可点击左侧树节点区校验，前前处理的选择已被写入求解模型中。
![](media/image35.png)
图 3-15 前前处理 – 「确定」功能按键示意图

#### 3.1.5 保存与退出 <a name="315-保存与退出"></a>  
a.保存：前前处理无保存按键，其过程数据会自动保存；
b.退出：点击右上角，可关闭窗口，返回AICFD仿真主界面；
c.下图为AICFD前前处理窗口与仿真主界面的交互示意图：
 ![](media/image37.png)

图 3-16前前处理窗口与仿真主界面的交互示意图

### 3.2 应用案例 <a name="32-应用案例"></a>  
#### 3.2.1物理现象

本页引导用户对所仿真的物理场景进行初步定义，可覆盖下列内容：
a.流体：单/多相流及对应多相流模型、流体介质；
b.时间：瞬态/稳态；
c.空间：内流/外流、物体形状与特征尺寸；
d.传热：热对流/热传导/热辐射、流/固/多孔介质域；
e.运动：旋转/直线运动；
下面为应用案例：
a.汽车外气动场景：
1) 此场景中，只涉及一种类型（常温空气）的流体，且流体在汽车外表面运动；
2) 用户只关注最终的整车阻力统计值而并非流场发展的动态过程；
3) 传热等其它物理现象可忽略。
按照需求，推荐的页面问答选项如下图：
![](media/image38.png)
图 3-17 前前处理 物理现象 页面：汽车外气动场景
b.船舶静水阻力场景：
1) 此场景中，涉及到两种流体（空气与水），关注波形图（清晰分界面）； 
2) 两种流体均在整船外部流动；
3) 用户只关注最终的整船阻力统计值而并非流场发展的动态过程；
4) 传热等其它物理现象可忽略。
![](media/image39.png)
图 3-18 前前处理 物理现象 页面：船舶静水阻力场景
c.圆柱绕流场景：
1) 此场景中，涉及到一种流体（水），且沿圆柱外表面流动； 
2) 用户关注流场发展的动态过程（例如卡门涡街）；
3) 传热等其它物理现象可忽略。
![](media/image40.png)
图 3-19 前前处理 物理现象 页面：圆柱绕流场景
d.电子机箱散热场景：
1) 此场景中，涉及到一种流体（水），且在机箱内部流动； 
2) 用户只关注最终的温度分布情况而并非流场发展的动态过程；
3) 需要考虑电子元件的发热与流体的对流散热。
![](media/image41.png)
图 3-20 前前处理 物理现象 页面：电子机箱散热场景
※注意事项：
在“流体材料”一问中，当前版本只支持有限种材料类型，后续会得到完善。 
#### 3.2.2湍流模型
本页引导用户对近壁面流体模型进行定义，可覆盖下列内容：
a. 根据流体雷诺数定义层流/转捩/湍流；
b. 根据流体的声速及流速判断可压缩性；
c. 根据关注的近壁面流体现象，结合计算资源与网格质量等现实条件，推荐具体的湍流模型；
d. 在通用推荐之外，如遇特定行业应用（如汽车或航空外气动场景），则按行业惯例进行推荐；
下面为应用案例：
a. 圆柱绕流场景：
1) 圆柱直径0.001m，介质为空气；
2) 对三种工况进行仿真：
流速 = 0.1 m/s；雷诺数 = 100（层流）
流速 = 10 m/s；雷诺数 = 1*10^4（转捩）
流速 = 5000 m/s；雷诺数 = 5*10^6（湍流）
3) 网格为3D，关注涡脱落的过程（卡门涡街）。 
按照需求，对三种工况分别进行设置，推荐的页面问答选项如下图：

![](media/image42.png)
![](media/image43.png)
图 3-21 前前处理 湍流模型 及 总结 页面：层流圆柱绕流 

![](media/image44.png)![](media/image45.png)
图 3-22 前前处理 湍流模型 及 总结 页面：转捩圆柱绕流 

![](media/image46.png)![](media/image47.png)
图 3-23 前前处理 湍流模型 及 总结 页面：湍流圆柱绕流 

b.NACA0012翼型外气动场景：
1) 翼型长度为1m，介质为空气；
2) 近壁面网格质量良好，希望研究不同攻角下的流动分离情况；
3) 流体速度为272m/s（0.8Ma，跨声速）；雷诺数 = 9*10^6（湍流）； 
4) 属于航空领域，行业内有特定的湍流模型使用惯例；
按照需求，推荐的页面问答选项如下图：

![](media/image48.png)![](media/image49.png)
图 3-24 前前处理 湍流模型及总结页面：NACA012翼型外气动仿真场景

#### 3.2.3边界条件
本页引导用户对计算域各面的边界条件进行定义，可覆盖下列内容：
a.各面所适用的边界条件：入口、出口、对称面、壁面；
b.入口/出口属性的定义：速度/总压/静压、湍流、热量；
c.壁面属性的定义：摩擦、运动、热量。
下面为应用案例：
汽车外气动：
1) 几何网格：全车模型，单域案例，地面移动；wall为地面、inlet为入口、outlet为出口、symm_top/ symm1/ symm2分别为计算域上表面与两个侧面、wall_car为车身、zhizhu为简化的圆柱形车轮；
2) 物理：关注所有壁面的边界层摩擦力；
3) 环境：模拟风洞实验（低湍流强度），入口速度40m/s。
![](media/image50.png)
图 3-25 前前处理 边界条件：汽车外气动的网格模型示意
按照需求，推荐的页面问答选项如下图：
![](media/image51.png)
图 3-26 前前处理 边界条件 页面：汽车外气动仿真

#### 3.2.4总结页面
本页将用户所有的选择转换为CFD软件可识别的设置信息，页面布局包括两部分：
a.信息展示区：包含 求解模型、计算域设置、边界条件 的总结，点击 确定 后，在所有设置会传递到AICFD主页面树节点中；
b.提示区：对于无法传递到AICFD主页面树节点的信息，给予逐行提示。
![](media/image52.png)
图 3-27 前前处理 总结 页面：汽车外气动仿真

---

## 4. 文件（File） <a name="4-文件file"></a>  
文件菜单栏主要是对当前工程的新建、打开、恢复、保存、另存、关闭、退出功能。
![](media/image53.png)
图 4-1 文件菜单栏

### 4.1 文件格式说明 <a name="41-文件格式说明"></a>  
在AICFD软件中，执行一个完整的算例数值模拟可能会涉及如下文件：
a.几何文件：AICFD软件支持导入STEP和IGES等格式的几何文件；
b.网格文件：AICFD软件支持导入STL格式的面网格文件。AICFD 软件支持CGNS， msh，tf格式的非结构化网格；
c.*.aicfd 算例文件：AICFD软件将用户定义的仿真算例，保存为.aicfd 后缀的文件，以便用户下次打开、修改设置或提交仿真计算；
d.*.vtk 数据文件：AICFD 软件将仿真计算结果保存为.vtk 文件，以便用户在可视化窗口中绘制仿真流场数据；
动画文件：用户使用AICFD软件生成的动画可保存为*.avi文件。

### 4.2 新建（New） <a name="42-新建new"></a>  
“新建”功能为新建一个仿真算例，新建工程文件之前软件树节点及菜单栏按钮均为未激活状态，新建工程文件后，才会被激活。若在已有工程的条件下新建，当前的工程文件会被新建的工程文件覆盖，用户可根据弹出对话框提示保存当前工程后再新建。
操作步骤：点击新建菜单按钮（New），弹出新建工程对话框（New Project），设置工程名称和路径。弹框下方默认路径勾选，可记忆当前路径为工程文件默认路径。
![](media/image54.png)
图 4-2 新建工程文件 

### 4.3 打开（Open） <a name="43-打开open"></a>  
AICFD 支持打开已有工程文件（.aicfd格式）。
操作步骤：点击打开（Open）菜单可打开AICFD工程文件继续编辑或查看。
![](media/image55.png)
图 4-3打开已有工程文件

### 4.4 恢复（Recover） <a name="44-恢复recover"></a>  
工程文件未保存时，AICFD支持恢复工程，点击打开恢复（Recover）菜单栏按钮可展开最近已使用的工程文件名称列表及其所在位置，选中文件夹下的GUIInfoBack文件，可恢复工程。
![](media/image56.png)
图 4-4恢复工程文件 

### 4.5 打开最近工程（Open Recent） <a name="45-打开最近工程open-recent"></a>  
AICFD支持打开最近使用的工程文件，点击打开最近工程（Open Recent）菜单栏按钮可展开最近已使用的工程文件名称列表及其所在位置，可任意选择列表中文件单击打开工程文件。
![](media/image57.png)
图 4-5 打开最近工程文件

### 4.6 保存（Save） <a name="46-保存save"></a>  
工程文件中所有的文件和设置参数需要保存在.aicfd文件中，以便下次打开继续分析和使用。
操作步骤：点击菜单栏文件（File）中的保存（Save）按钮，软件将自动保存当前工程文件，路径为新建工程文件的默认路径。 

### 4.7 另存（Save As） <a name="47-另存save-as"></a>  
AICFD软件支持将当前工程文件另存为其他路径，并重命名。
操作步骤：选择“另存（Save As）”按钮，打开图42对话框，选择要另存的路径，文件保存类型设置为默认“.aicfd”类型，点击对话框界面“保存”按钮，即可完成当前工程文件的另存功能。
![](media/image58.png)
图 4-6 另存当前工程文件 

### 4.8 关闭（Close） <a name="48-关闭close"></a>  
关闭当前工程，自动保存修改，返回软件初始界面。  

### 4.9 退出（Exit） <a name="49-退出exit"></a>  
退出软件，自动保存所有打开的工程文件，结束进程。  

---

## 5. 几何（Geometry） <a name="5-几何geometry"></a>  
几何菜单栏包括导入几何（Import Geometry），压印（Imprint），内流抽体（Internal Flow Extration）,外流场创建（Outflow Field Creation），几何检查（Geometry Inspection），几何剖切（Geometry Clip）功能。
![](media/image59.png)
图 5-1 几何菜单栏

### 5.1 导入几何（Import Geometry） <a name="51-导入几何import-geometry"></a>  
AICFD支持导入外部STP、IGES几何文件。
操作步骤：点击几何＞导入几何（Import Geometry）按钮，打开如图45所示对话框，指定文件路径，几何文件类型，选择文件，点击确认（OK）按钮。
![](media/image60.png)
图 5-2 导入几何文件 

### 5.2 压印（Imprint） <a name="52-压印imprint"></a>  
AICFD支持压印功能，压印工具可用于将一组面和边压印在一起。
操作步骤：点击“几何＞压印”按钮，可以实现多域几何模型一键压印。
![](media/image61.png)
图 5-3 压印  

### 5.3 内流抽体（Internal Flow Extration） <a name="53-内流抽体internal-flow-extration"></a>  
AICFD支持内流抽体功能，在选定零部件中的封闭体积并生成零部件来填充该体积。
操作步骤：点击“几何＞内流抽体”按钮，选择封闭端面和任意内部面，实现內部流体域抽取创建。
![](media/image62.png)
图 5-4 内流抽体 

### 5.4 外流场创建（Outflow Field Creation） <a name="54-外流场创建outflow-field-creation"></a>  
点击菜单栏“创建外流场（Outflow Field Creation）”，可以通过立方体等类型创建外流场几何。立方体几何输入体对角线两点坐标，创建外流场时可以勾选保留原有几何域。
![](media/image63.png)
图 5-5 创建外流场  

### 5.5 几何检查（Geometry Inspection） <a name="55-几何检查geometry-inspection"></a>  
AICFD支持一键自动几何检查功能，依次检查模型全部域的水密性。
![](media/image64.png)
图 5-6 几何检查  

### 5.6 几何剖切（Geometry Clip） <a name="56-几何剖切geometry-clip"></a>  
可作用于切分几何视口，提供 X-Y，Y-Z，Z-X 平面三平面剖切；
![](media/image65.png)
图 5-7 压印

---

## 6. 网格（Mesh） <a name="6-网格mesh"></a>  
网格菜单栏包含 “导入网格（Import Mesh）”，“导出网格（Export）”；“网格参数（Mesh Parameters）”；“网格加密（Mesh Refinement）”；“创建网格（Create Mesh）”；“停止创建网格（Stop）”；“网格质量（Mesh Quality）”；“删除网格（Delete Mesh）”功能。
![](media/image66.png)
图 6-1 网格菜单栏

### 6.1 导入面网格（Read Surface Mesh） <a name="61-导入面网格read-surface-mesh"></a>  
AICFD支持导入外部STL面网格文件。
操作步骤：点击“导入面网格（Read Surface Mesh）”按钮，打开如图48所示对话框，指定文件路径，面网格文件类型，选择文件，点击确认（OK）按钮。
![](media/image67.png)
图 6-2  导入面网格文件 

### 6.2 水密性检查（Tightness Inspection） <a name="62-水密性检查tightness-inspection"></a>  
AICFD支持一键自动面网格水密检查功能，依次按域检查面网格的水密性。
![](media/image68.png)
图 6-3  面网格水密性检查  

### 6.3 导入体网格（Import Volume Mesh） <a name="63-导入体网格import-volume-mesh"></a>  
AICFD支持导入多种格式网格，包括msh，cgns，tf等网格格式。
操作步骤：通过点击导入网格菜单按钮，弹出导入框，选择导入路径及网格形式。点击确认，即可在视口窗中显示网格文件。
![](media/image69.png)
图 6-4  导入体网格文件

网格文件导入后，左侧树节点会挂载网格详细信息，包括体网格和面网格及对应面信息。
![](media/image70.png)
图 6-5 树节点网格信息显示

### 6.4 导出体网格（Export Volume Mesh） <a name="64-导出体网格export-volume-mesh"></a>  
AICFD支持导出cgns、msh及Openfoam格式网格文件。
选中网格文件名称，点击“导出体网格（Export Volume Mesh）”菜单按钮，弹出弹框，选择文件保存名称和路径，即可完成网格导出功能。
![](media/image71.png)
图 6-6 导出体网格文件 

### 6.5 网格参数（Mesh Parameters） <a name="65-网格参数mesh-parameters"></a>  
AICFD支持全局尺寸，体网格，面网格，边界层网格参数设置；用户可根据需求设置适合网格参数。

#### 6.5.1 全局尺寸（Global Size） <a name="651-全局尺寸global-size"></a>  
全局尺寸主要用于全局网格的尺寸控制。具体设置如下：
a.全局受限尺寸：包括最小网格尺寸、最大网格尺寸、网格尺寸增长率。最小网格尺寸、最大网格尺寸可根据模型的尺寸范围给与推荐尺寸设置；
b.曲率控制：用于控制几何局部曲率加密，范围0-180，软件给出默认值为8；
c.间隙控制：用于控制几何局部薄壁、间隙位置加密，范围0-5层，软件给出默认值为2；
d.保留原始网格：stl面网格导入后，可以保留该网格模型，默认不保留。
![](media/image72.png)
图 6-7 全局尺寸设置 

#### 6.5.2 体网格（Volume Mesh） <a name="652-体网格volume-mesh"></a>  
主要用于体网格的尺寸控制。具体设置如下：
a.选择对象：选择需要局部体网格加密的对象，默认不进行局部体网格加密；
b.网格类型：体网格生成类型，默认为四面体网格；
c.分组名称：进行局部体网格加密的组名称；
d.尺寸控制：包括最大体网格尺寸和体网格尺寸变化率；
e.分组列表：可以点击查看已设置好的体网格尺寸。
![](media/image73.png)
图 6-8 体网格参数设置  

#### 6.5.3 面网格（Surface Mesh） <a name="653-面网格surface-mesh"></a>  
主要用于面网格的尺寸控制。具体设置如下：
a.选择对象：选择需要局部面网格加密的对象，默认不进行局部面网格加密；
b.网格类型：面网格生成类型，默认为三角形网格；
c.分组名称：进行局部面网格加密的组名称；
d.尺寸控制：包括最大体网格尺寸和体网格尺寸变化率；
e.分组列表：可以点击查看已设置好的面网格尺寸。
![](media/image74.png)
图 6-9 面网格参数设置  

#### 6.5.4 边界层（Boundary Layers） <a name="654-边界层boundary-layers"></a>  
主要用于边界层的控制。具体设置如下：
a.边界层网格开启：控制是否生成棱柱层网格，默认不开启；
b.选择对象：选择需要进行划分边界层的边界，默认全局，当设置选择局部边界时，退出全局选择；
c.分组名称：进行划分边界层的组名称；
d.参数：包括首层、厚度比、总层数，总厚度自动算出；
e.激活：控制是否开启本组边界层划分；
f.分组列表：可以点击查看已设置好的边界层参数。
![](media/image75.png)
图 6-10 边界层参数设置

### 6.6 网格加密（Mesh Density） <a name="66-网格加密mesh-density"></a>  
软件支持创建方体，球体，圆柱体形状的辅助几何，用于网格局部加密；用户可根据需求创建适合的几何，辅助几何与模型重合区域即为加密区域。具体操作步骤如下：

#### 6.6.1创建
点击菜单栏选择网格加密中的“立方体（Box）”， “球体（Sphere）”， “圆柱体（Cylinder）”或者右击树节点“网格（Mesh）＞“加密区域（Mesh Density）”。
![](media/image76.png) ![](media/image77.png)
图 6-11 添加网格加密

#### 6.6.2生成
打开对话框，输入辅助几何名称，此时左侧树节点会挂载相应辅助几何节点（下图为Sphere1），视口区域显示默认尺寸的球体。
  ![](media/image78.png)![](media/image79.png)
图 6-12 添加加密区域

#### 6.6.3修改尺寸
双击加密区域中的几何，可设置加密区域详细信息，包括位置，尺寸和加密设置。
方法一：立方体几何输入体对角线两点坐标，球体几何输入球体中心位置坐标，半径大小。圆柱体几何输入中心轴两点坐标位置；
  ![](media/image80.png)![](media/image81.png)![](media/image82.png)
图 6-13 设置加密区域尺寸

方法二：点击设置面在视口区长按鼠标左键拖住该加密几何，可对其进行移动，配合视口区缩放、旋转等操作，也可完成几何的位置设置。

#### 6.6.4加密设置
加密设置界面输入加密等级，可根据需要设置加密区域最大网格尺寸和体网格尺寸增长率。

### 6.7 创建面网格（Create Surface Mesh） <a name="67-创建面网格create-surface-mesh"></a>  
AICFD支持生成或重构三角形面网格。
![](media/image83.png)
图 6-14  创建面网格  

### 6.8 配置（Config） <a name="68-配置config"></a>  
AICFD一键生成网格前可以选择生成网格的区域，以及是否直接生成多面体。
![](media/image84.png)
图 6-15  配置

### 6.9 创建网格（Create Volume Mesh） <a name="69-创建网格create-volume-mesh"></a>  
AICFD支持导入外部网格，也支持自动创建网格。目前AICFD支持网格形式包括四面体，金字塔，棱柱等。
a.点击“创建网格（Create Mesh）”按钮，即可一键生成网格文件，视口端自动跳转至“Pre-Processing”窗口；
b.日志栏将显示网格划分细节，页面右下角将显示网格划分进程。
![](media/image85.png)
图 6-16 网格生成过长
![](media/image86.png)
图 6-17 网格生成后视口显示

### 6.10 转化多面体（Transform Polyhedra） <a name="610-转化多面体transform-polyhedra"></a>  
![](media/image87.png)
图 6-18  转化多面体 

### 6.11 停止创建网格（Stop） <a name="611-停止创建网格stop"></a>  
用户在创建网格完成后，可根据需要停止创建网格，点击“停止创建网格”按钮即可。 

### 6.12 信息统计（Mesh Info） <a name="612-信息统计mesh-info"></a>  
用户在创建网格完成后，查看网格基本信息，点击“信息统计”按钮即可。
![](media/image88.png)
图 6-19 网格信息展示  

### 6.13 网格质量（Mesh Quality） <a name="613-网格质量mesh-quality"></a>  
自动生成网格或导入网格文件成功后，点击“网格质量（Mesh Quality）”菜单按钮，可查看当前网格详细信息。包括网格名称，网格文件保存路径，网格点数量，网格单元数量，网格面数量，网格边界数量，网格点区域数量，网格单元区域数量，网格面区域数量，各形状网格数量，XYZ方向网格分布区域范围信息。通过上述网格信息展示，可帮助用户进一步确认当前网格质量。

#### 6.13.1快速面网格质量报告（Quick Mesh Quality）

![](media/image89.png)
图 6-20 快速网格质量报告

#### 6.13.2快速体网格质量报告（Quick Mesh Quality）
![](media/image90.png)
图 6-21 快速网格质量报告
#### 6.13.3网格质量检查（Mesh Mesh Quality）
![](media/image91.png)
图 6-22 2D网格质量检查
![](media/image92.png)
图 6-23 3D网格质量检查
![](media/image93.png)
图 6-24 3D网格质量检查视口显示

### 6.14 删除网格（Delete Mesh） <a name="614-删除网格delete-mesh"></a>  
用户可根据需要删除工程中任一网格文件，通过选中树节点网格名称，点击菜单栏删除网格按钮，或通过右击树节点网格名称>删除完成。

### 6.15 网格切面（Mesh Clip） <a name="615-网格切面mesh-clip"></a>
可作用于切分网格视口，提供 X-Y，Y-Z，Z-X 平面三平面剖切；
![](media/image94.png)
图 6-25 网格切面查看

### 6.16 AI 网格（AI Mesh） <a name="616-ai网格ai-mesh"></a>

AICFD具备AI网格功能，实现网格自适应加密。
勾选启动AI网格功能：
a.网格优化次数：网格优化过程中调整网格的最大次数。
b.最大加密等级：网格优化过程中，原始网格中的单元被调整的最大次数。
c.加密比例：每轮网格优化过程中，待调整单元在网格单元中所占比例。
d.预计最终网格量：根据网格单元总数、加密比例以及网格优化次数预估的最终的网格的网格量。
e.壁面y*期望值：如果待优化的壁面单元的y+已经低于用户所设置的y+期望值，则该单元不会发生变化。
f.几何保形：如果网格初始时较为粗糙，相较于原始表面存在明显失真。在网格优化过程中，将会回复到最初的几何形态。
![](media/image95.png)
图 6-26 AI网格设置
 
### 6.17 恢复原始网格（Restore original mesh） <a name="617-恢复原始网格restore-original-mesh"></a>  
撤销AI网格优化或手动修改，恢复至初始网格状态，支持版本回溯。  

---

## 7. 求解（Solution） <a name="7-求解solution"></a>  
求解菜单栏包含：
a.新建对象部分：材料（Material）、域（Domain）、边界条件（Boundary）、交界面（Interface）、自定义点（User Points）；
b.热模型部分：热源（Heat Source）、平面热源（Planar Heat Source)、风扇（Fan）、印制电路版PCB，热管(Heat Pipe)，双热阻（Dual Thermal Resistance）；
c.求解部分：计算域初始化（Initialize）、启动求解（Run Solver）、停止求解（Stop Run）；
d.监控部分：均方根残差（RMS Residual）、最大残差（Max Residual）；
e.结果部分：导出求解结果（Export）、可视化求解结果（Post Process Results）。
![](media/image96.png)
图 7-1 求解菜单栏

### 7.1 材料设置 （Material） <a name="71-材料设置-material"></a>  
AICFD 提供了模型材料库，并将常用的材料放到材料树节点下，双击某一材料模型，可查看该材料的详细信息。
  ![](media/image97.png)![](media/image98.png)
图 7-2 查看材料信息

单击另存为新材料（Save As New Material）按钮，程序可以把已有材料存为新材料，允许用户进行编辑和后续使用。
右击树节点Materials，弹出导入材料库数据（Import Library Data）菜单，点击此菜单进入材料库窗口，AICFD材料库提供了各种材料模型，从中选择某一材料后，直接点击下方OK按钮，可将该材料添加到材料列表。在材料列表中的材料，可以赋值给当前模型。
![](media/image99.png)
图 7-3 从材料库导入材料

AICFD还支持自建材料功能，右击树节点Materials，弹出自建材料（Add Library）菜单，允许用户自建新材料，输入材料物性参数赋值于当前模型，支持材料物性分段线性和多项式。
 ![](media/image100.png)![](media/image101.png)
图 7-4 自建材料

### 7.2 计算域设置 （Domain） <a name="72-计算域设置-domain"></a>  
通常情况下，AICFD会自动识别计算域，不需要用户新建计算域。如有必要，用户需要根据流体仿真问题的特点，设置计算域以及各个计算域的仿真类型和相关属性。
操作步骤：右击左侧树节点“计算域（Domains）”>“插入域（Insert Domain）”，打开“计算域设置（Domain Basic Setting）”面板。
用户可自定义计算域名称，选择对应网格区域，定义计算域流动属性（固体域、流体域或多孔介质），材料属性（若为多相流，根据选择的相数，软件会显示对应数量的流体材料名称及对应材料设置框，主相通常默认为水），旋转特征（旋转机械仿真需要定义计算域为旋转域（Option>Rotating）），完成设置后点击下一步，进入计算域流动模型（Fluid Models）设置或多孔介质模型（Porosity Setting）设置。
![](media/image102.png)
图 7-5 计算域参数设置
![](media/image103.png)
图 7-6 多相流计算域基础参数设置

若计算域为多孔介质模型，则启动多孔介质模型设置界面，包括各向同性和各向异性。
![](media/image104.png)
图 7-7 多孔介质模型参数设置

若计算域不是多孔介质模型，则启动计算域流动模型设置界面，包括多相流、传热、燃烧、热辐射四部分内容，用户可以根据不同的场景进行设置，具体详细说明请参考后续应用案例。
![](media/image105.png)
图 7-8 计算域流动模型设置

设置完成后，点击OK按钮完成计算域设置。

### 7.3 边界条件设置（Boundary Condition） <a name="73-边界条件设置boundary-condition"></a>  
边界条件模块，用于定义当前计算域的所有边界面的边界类型及边界参数值。AICFD提供了丰富的边界条件类型，包括：
a.固壁边界（Wall）；
b.速度入口边界（Velocity Inlet）；
c.质量流量入口边界（Mass flow Inlet）；
d.压力入口边界（Pressure Inlet）；
e.驻点压力入口边界（Stagnation Inlet）；
f.压力出口边界（Pressure Outlet）；
g.质量流量出口边界（Mass flow Outlet）；
h.对称面（Symmetry）。
![](media/image106.png)
图 7-9 边界条件类型设置

主要操作步骤：
点击菜单栏“新建边界条件（Boundary）”或者右击计算域树节点边界条件（Boundaries）>添加边界条件（Insert Boundary）。
设置步骤：
a.输入边界名称（Boundary Name）：系统会给默认名称，用户亦可修改重命名；
b.选择计算域（Domain Belong）：选择边界条件所属计算域；
c.选择计算域边界（Patch List）：选择对应网格面；
d.定义边界类型（Boundary Type）：可选择上面介绍的八种边界类型；
e.对应不同边界类型，需要设置动量（Momentum），湍流变量（Turbulence），热量（Thermal）三部分参数。
边界条件定义完成后，AICFD新增显示已定义边界的方向和区域功能，默认以绿色箭头显示。
![](media/image107.png)
图 7-10 边界条件显示  

#### 7.3.1固壁边界（Wall）
输入边界名称，命名为“流体壁面”，选择当前计算域，如下图所示：
![](media/image109.png)
图 7-11 固壁边界名称修改
a.选择对应的网格面，AICFD采用多选框设计，方便用户一次性选择多个网格面定义边界条件，为了避免用户重复设置或者遗漏设置，已设置过的边界面将不会出现在多选框中。
![](media/image109.png)
图 7-12 边界面多选框
b.在“边界条件类型（Boundary Type）”中选择“固壁边界（Wall）”，之后我们依次设置动量（Momentum），热量（Thermal）参数。
c.动量（Momentum）设置：可以设置壁面运动与壁面粗糙度。壁面运动（Wall Motion），有静止壁面（Stationary Wall）和运动壁面（Moving Wall）两种形式。
1) 若为运动壁面，在运动方式中选择平动（Translational）或转动（Rotational），平动则输入速度大小和速度方向，速度方向通过三点坐标分量实现。若为转动，输入转动速度大小和转动方向，转动轴通过两点坐标实现，转动速度值为正，则表示顺时针转动，速度为负，则表示逆时针方向转动；
2) 壁面剪切条件（Shear Condition），有无滑移（No Slip），自由滑移（Free Slip）和壁面剪切力（Specified Shear）三种方式。
3) 若选择壁面剪切力（Specified Shear）方式，需要输入X，Y，Z三方向的剪切应力大小。
4) 勾选壁面粗糙度可设置粗糙高度和粗糙常数。
  ![](media/image110.png)![](media/image111.png)
图 7-13 固壁边界参数设置（动量标签页）
d.热量（Thermal）：若用户在求解模型（Solution Modeling）中激活了能量方程，需要在热量标签页输入热传递参数，AICFD提供了热通量（Heat Flux），流体温度（Temperature），绝热（Adiabatic）和热对流（Convection）。
若选择热通量（Heat Flux），需要填入对应热通量数值，若选择温度（Temperature），输入流体总温，选择绝热，无需输入任何参数，热对流（Convection）形式需要用户输入热传递系数（Heat Transfer Coefficient）和自由流体温度（Free Stream Temperature），对应设置界面如下。
  
![](media/image112.png)![](media/image113.png)![](media/image114.png)![](media/image115.png)
图 7-14 固壁边界参数设置（热量）

#### 7.3.2速度入口边界（Velocity Inlet）
在“边界条件类型（Boundary Type）”中选择速度入口边界，进入动量，湍流变量及热量的标签页设置界面。
a.动量（Momentum）设置：AICFD进口速度可采用局部坐标系（Reference Frame）定义，也可采用全局坐标系设置进口速度。本版本目前只开放了全局坐标系。在此坐标系中，用户需要输入速度大小（Speed Value）和速度方向（Direction Specification Method），速度进入方向可选择入口面法向方向（Normal to Boundary）或者在笛卡尔坐标系中，输入X，Y，Z三分量的值。
![](media/image116.png)
图 7-15 速度入口边界参数设置（动量标签页）
b.湍流变量（Turbulence）设置：AICFD提供了壁面函数用于处理不同类型的湍流模型（参见流动类型（Solution Modeling）中关于湍流变量的介绍）。
若用户选择了K-Epsilon 湍流模型，壁面处理（Near-Wall Treatment）选项中，默认选择标准壁面函数（Standard Wall Function）。若用户选择k-Omega湍流模型，可自由选择打开或关闭标准壁面函数（Standard Wall Function）。若用户选择Spalart-Allmaras湍流模型，目前暂未开放标准壁面函数功能。
湍流模型求解方法（Specification Method）中提供了三种方法：
1) 方法一：k-epsilon或k-Omega系数数值方法，需要用户输入k和epsilon （对应k-epsilon湍流模型）或k和Omega数值（对应k-Omega湍流模型）；
2) 方法二：强度和长度数值方法（Intensity and Length Scale），用户需要输入湍流强度（Turbulent Intensity）和湍流长度数值（Turbulent Length Scale）；
3) 方法三：强度和粘性系数方法（Intensity and Viscosity Ratio），用户输入对应的湍流强度（Turbulent Intensity）和粘性系数数值（Viscosity Ratio）。

 
 ![](media/image117.png)![](media/image118.png)![](media/image119.png)
图 7-16 速度入口边界参数设置（湍流标签页）
c.热量（Thermal）：若用户在求解模型（Solution Modeling）中激活了能量方程，则可以在热量标签页输入流体总温（Total Temperature）。
点击OK按钮完成边界条件设置，点击“关闭（Close）”按钮即可回到树节点。
![](media/image120.png)
图 7-17 速度入口边界设置（热量标签页）

#### 7.3.3质量流量入口边界（Mass flow Inlet）
在“边界条件类型（Boundary Type）”中选择质量流量入口边界，进入动量，湍流变量及热量的标签页设置界面。
a.动量（Momentum）设置：在全局坐标系中，输入质量流量数值大小（Mass Flux）和进入方向（Direction Specification Method），质量流量流入方向可选择进口面法向方向（Normal to Boundary）或者在笛卡尔坐标系中，输入X，Y，Z三分量的值。   
![](media/image121.png)
图 7-18 质量流量入口边界参数设置（含动量标签页）
b.湍流变量（Turbulence）设置：与速度入口边界设置步骤相同。 
c.热量（Thermal）：若用户在求解模型（Solution Modeling）中激活了能量方程，则可以在热量标签页输入流体总温（Total Temperature）。
点击OK按钮完成边界条件设置，点击“关闭（Close）”按钮即可回到树节点。

#### 7.3.4静压入口边界（Static Pressure Inlet）
在“边界条件类型（Boundary Type）”中选择压力入口边界，进入动量，湍流变量及热量的标签页设置界面。
a.动量（Momentum）设置：在全局坐标系中，输入相对静压数值大小（Relative Static Pressure）和进入方向（Direction Specification Method），压强方向可选择进口面法向方向（Normal to Boundary）或者在笛卡尔坐标系中，输入X，Y，Z三分量的值确认进口压强方向。
b.湍流变量（Turbulence）设置：与速度入口边界设置步骤相同。
c.热量（Thermal）：若用户在求解模型（Solution Modeling）中激活了能量方程，则可以在热量标签页输入流体静温（Static Temperature）。

#### 7.3.5总压入口边界（Total Pressure Inlet）
在“边界条件类型（Boundary Type）”中选择压力入口边界，进入动量，湍流变量及热量的标签页设置界面。
a.动量（Momentum）设置：在全局坐标系中，输入相对总压数值大小（Relative Static Pressure）和进入方向（Direction Specification Method），压强方向可选择进口面法向方向（Normal to Boundary）或者在笛卡尔坐标系中，输入X，Y，Z三分量的值确认进口压强方向。
![](media/image122.png)
图 7-19 入口边界参数设置（动量标签页）
b.湍流变量（Turbulence）设置：与速度入口边界设置步骤相同。 
c.热量（Thermal）：若用户在求解模型（Solution Modeling）中激活了能量方程，则可以在热量标签页输入流体总温（Total Temperature）。
![](media/image123.png)
图 7-20 入口边界参数设置（热量标签页）
#### 7.3.6压力出口边界（Pressure Outlet）
在“边界条件类型（Boundary Type）”中选择压力出口边界，进入动量，湍流变量及热量的标签页设置界面
a.动量（Momentum）设置：在全局坐标系中，输入出口相对静压数值大小（Relative Static Pressure）；下方 抑制回流 代表在计算过程中不计入与出口方向相反的流体通量值，此选项默认开启，可增强计算稳定性。
![](media/image124.png)
图 7-21 压力出口边界参数设置（动量标签页）
b.湍流变量（Turbulence）设置：与速度入口边界设置步骤相同。 
c.热量（Thermal）：若用户在求解模型（Solution Modeling）中激活了能量方程，则需要在热量标签页输入回流总温（Total Temperature）。
![](media/image125.png)
图 7-22 压力出口边界参数设置（热量标签页）

#### 7.3.7质量流量出口边界（Mass flow Outlet）
在“边界条件类型（Boundary Type）”中选择质量流量出口边界，进入动量，湍流变量及热量的标签页设置界面。
a.动量（Momentum）设置：在全局坐标系中，输入出口质量流量数值大小（Mass Flux）和流出方向（Direction Specification Method），回流方向可选择出口面法向方向（Normal to Boundary）或者在笛卡尔坐标系中，输入X，Y，Z三分量的值。
b.湍流变量（Turbulence）设置：与速度入口边界设置步骤相同。 
c.热量（Thermal）：若用户在求解模型（Solution Modeling）中激活了能量方程，则可以在热量标签页输入回流总温（Total Temperature）。
点击OK按钮完成边界条件设置，点击“关闭（Close）”按钮即可回到树节点。

#### 7.3.8对称面（Symmetry）
在“边界条件类型（Boundary Type）”中选择对称面边界，如下图所示，点击OK按钮即可，点击“关闭（Close）”按钮即可回到树节点。
![](media/image126.png)
图 7-23 对称面边界参数设置

#### 7.3.9 动态边界条件 <a name="739-动态边界条件"></a>  
动态边界条件包括：
a.动态静压入口：在选择静压入口边界条件时，给定动态压力可选择项，并导入对应的时间序列曲线；
b.动态速度入口：在选择速度入口边界条件时，给定动态速度可选择项，并导入对应的时间序列曲线；
c.动态质量流量入口：在选择质量流量入口边界条件时，给定动态质量流量可选择项，并导入对应的时间序列曲线；
d.动态温度入口：能量方程开启时，在入口边界条件时，给定动态质量流量可选择项，并导入对应的时间序列曲线；
e.动态温度壁面：在选择壁面边界条件时，给定动态温度可选择项，并导入对应的时间序列曲线。
文件中的数据格式如下，推荐txt格式，默认如下图所示：
![](media/image127.png)
图 7-24 动态温度时间序列txt表单示例
对于速度而言有两种情况：
a.速度为normal to boundary
![](media/image128.png)
图 7-25 动态速度（模量形式）时间序列txt表单示例
b.速度为分量形式
![](media/image129.png)
图 7-26 动态速度（分量形式）时间序列txt表单示例
![](media/image130.png)
图 7-27 动态边界设置

### 7.4 交界面设置（Interface） <a name="74-交界面设置interface"></a>  
AICFD通常会自动识别不同域之间的交界面。大部分情况不需要用户手动新建，只需要检查即可。少数情况没有自动识别，或者识别有误的，才需要用户新建交界面。
若用户设置多个计算域，需要设置交界面参数，确定多域之间的连接关系和连接方式。
操作步骤：点击菜单栏“新建交界面（Interface）按钮”或右击树节点“交界面（Interface）”>插入新的交界面（Insert Interface），打开设置面板，依次设置参数，交界面命名（Interface Name）>选择连接域类型（Type）（流固连接或流体（fluid-solid）-流体连接（fluid-fluid），固体-固体连接（solid-solid））>选择第一个计算域（Interface Side1>Domain List）>第一个连接面（Interface Side1>Region List）>第二个计算域（Interface Side2>Domain List）>第二个连接面（Interface Side2>Region List）。
对于周期性交界面，可在交界面模型（Interface Model）选项中选择平动周期性交界面（Translational Periodicity）或者旋转周期性交界面（Rotational Periodicity）。若选择旋转周期性交界面，需要定义旋转机械叶轮数量或周期面到旋转中心的角度，以及旋转轴轴位置。完成设置点击确认按钮（OK）退出设置界面。
![](media/image131.png)
图 7-28 交界面设置

### 7.5 边界条件导入、导出（Import、Export Boundary） <a name="75-边界条件导入导出import-export-boundary"></a>  
AICFD提供设置边界条件导入及导出功能，便于工程边界条件的复用。
操作步骤：右击树节点“边界（Boundaries）”，选择导入或导出边界条件，实现边界条件的保存和复用。
![](media/image132.png)
图 7-29 边界条件导出
![](media/image133.png)
图 7-30 边界条件导入

### 7.6用户点设置 （User Point）
AICFD提供新建用户点功能，用于监控该点的变量信息或提取当前时刻该点上变量值。
操作步骤：点击菜单栏“新建用户点（User Point）”，选择监控变量，输入三坐标即可生成新的用户点，后续可在监控窗口查看用户点上变量随时间变化的曲线。
![](media/image134.png)
图 7-31 新建用户点

### 7.7热源（Heat Source）
AICFD支持自定义热源，目前可以定义点体热源，模拟固定位置热源。
注意：模拟传热相关问题时，需要在Solution Modeling界面打开能量（Energy）开关。
操作步骤：点击菜单栏热源（Heat Source）按钮，输入热源名称，选择热源类型，当前版本支持点（Point）类型，输入点热源在笛卡尔坐标系中的三坐标，完成后可点击右侧OK按钮在视口区确认设置的热源位置是否合理（已设置的点热源显示为红色圆点），最后输入热源热量，单位为瓦特（W）。点击下方确认按钮完成点热源设置。
![](media/image135.png)
图 7-32 热源设置界面

### 7.8平面热源（Planar Heat Source）
AICFD增加了自定义平面热源和外部导入热源，模拟某一平面位置热源。
![](media/image136.png)
图 7-33 平面热源设置界面
### 7.9风扇（Fans）
AICFD增加了风扇模型，用于模拟边界风扇和域内风扇。
a.边界风扇分为吸出式风扇（Exhaust）和吹入式风扇（Intake）两种类型，吸出式风扇（Exhaust）主要通过创建出口压降达到吸出效果，吹入式风扇（Intake）通过在入口增加压强达到模拟风扇的目的。
  ![](media/image137.png)![](media/image138.png)
图 7-34 风扇设置界面
边界风扇基本选项：
1) 命名（Name）：用户自定义；
2) 风扇类型（Type）：Intake/Exhaust；
3) 位置（Location）：指定边界及其所属计算域；
4) 环境压力（Environment Pressure）：默认值为大气压；
5) 环境温度（Environment Temperature）：默认值为300K；
6) 降额系数（Derating Factor）：默认值为 1.0；
7) 风扇描述（Fan Description）：Fan Performance Curve（P-Q曲线）、Consant Volume Flow （固定体积流量）；
8) 风扇流动类型（Flow Type）：Normal/Angled，当类型为Angled时需要格外指定流动方向： Flow Direction；
9) 湍流部分：与入口/出口边界条件类似，需要设置湍流变量相关参数。
b.域内风扇用于模拟计算域内风扇模型，可选择某计算域作为整个风扇模型，用户也可以自定义风扇模型及其位置。
域内风扇基本选项：
1) 命名（Name）：用户自定义；
2) 风扇类型（Fan Type）：类型选择Internal则为域内风扇；
3) 指定区域（Location）：包含已知计算域（DefaultDomain）和用户自定义圆柱区域（User Define Cylinder）；
4)  风扇定义（Fan Description）：这里默认为固定体积流量曲线（Constant Volume Curve）；
5) 风扇风速（Velocity Value）：设置风扇工作风速；
6) 风速方向（Velocity Direction）：设置风扇风速方向；
7) 对于用户自定义圆柱区域（User Define Cylinder）类型，需要指定圆柱上下表面中心点坐标（Point1，Point2及半径值（Radius）。
![](media/image139.png)
图 7-35 域内风扇设置-1
![](media/image140.png)
图 7-36 域内风扇设置-2
P-Q曲线（Fan Performance Curve）的定义
P-Q曲线为风扇在额定功率下的P-Q关系曲线，当用户选择风扇描述（Fan Description）为Fan Performance Curve（P-Q曲线）时，点击设置界面Edit按钮，进入P-Q曲线设置界面。
操作步骤：参考实际风扇P-Q曲线在界面输入一系列流量Q与压力P的对应列表，点击“Draw”按钮，左边作图区会根据采集到的P-Q样本计算出函数关系曲线图（蓝色曲线）。
绿色曲线为通过降额系数得到的实际功率下的P-Q关系曲线图。
当样本数量较多时，用户亦可通过点击“Import”导入已有的CSV文件直接输入P-Q数据样本，CSV文件格式要求第一列为流量Q值，第二列为压力P值，且单位与界面一致。
![](media/image141.png)
图 7-37 P-Q曲线绘制界面

### 7.10边界热阻（Heat Resistant）
AICFD提供了边界热阻元件用于模拟散热问题，当Solution Modeling界面上打开了能量（Energy）开关后，边界条件热量（Thermal）标签页可勾选薄壳传导（Shell Conduction）来设置边界热阻。具体界面如下：
 ![](media/image142.png)![](media/image143.png)
图 7-38 热阻界面
基本选项：
a.热阻类型（Thermal Resistant）：平面热阻（Plane）/圆柱热阻（Cylinder）；
b.层数（Layers）：热阻层数。
1)若为圆柱热阻（Cylinder），需设置：
圆柱内直径（Inner Diameter）；
圆柱外直径（Outer Diameter）；
热传导系数（Heat Conductivity Coefficient）。
2)若为平面热阻（Plane），需设置：
平面厚度（Thickness）；
热传导系数（Heat Conductivity Coefficient）。

### 7.11热管元件（Heat Pipe）
热管元件为AICFD软件提供的散热元件之一，具有高效的传热属性，通过利用相变传热原理，达到快速传热的目的，一般可作为电子散热领域重要的散热元件，此版本提供了双热阻模型，将热管两端分别假定为蒸发段和冷凝端，具体设置界面如下：
![](media/image144.png)
图 7-39 热管设置界面
基本选项：
a.名称（Name）：用户自定义；
b.模型类型（Model）： 默认为双热阻模型；
c.指定区域（Source Location）：选择元件对应的网格区域；
d.蒸发端（Evaporation Side）：指定蒸发端边界；
e.冷凝端（Condensation Side）：指定冷凝端边界；
f.热阻（Thermal Resistant）：设定热管热阻值；
g.最大热流量（Maximum Heat Flux）：设定通过热管的最大热流量。

### 7.12印制电路板（PCB）
PCB元件主要用于模拟电子散热问题而设计，软件通过计算PCB各层导热率的方式简化工业领域真实的印制电路板，达到模拟电路板传热的效果。设置界面如下：
![](media/image145.png)
图 7-40 百分比模型                    
![](media/image146.png)
图 7-41 层定义模型
![](media/image147.png)
图 7-42 层定义设置界面
基本选项：
a.名称（Name）：用户自定义；
b.建模级别（Modeling Level）：默认为精简级别；
c.指定区域（Source Location）：选择PCB元件对应的网格区域；
d.材料分析类型（Material Composition）：软件提供两种类型，1-百分比模型（% Conductor By Volume）；2-层定义模型（Layer Definition）。
1) 若选择百分比模型（% Conductor By Volume），所需设置如下：
PCB板导电部分所占体积百分比（% Conductor By Volume）
导电层材料（Conductor Material）
绝热层材料（Dielectric Material）
2) 若选择2-层定义模型（Layer Definition），需要设置以下选项：
点击层定义（Layer Definition）按钮打开层定义设置弹框：
导电层层数（Number of Conducting Layers）：设置完导电层数后，界面默认生成PCB导电层（Conductor1，Conductor2…）和绝缘层（Dielectri1， Dielectric2…）层级结构及其设置选项，如图108所示。
导电层/绝缘层厚度（Layer Thickness）
导电面积覆盖率（% Layer Coverage）
绝缘层材料（Dielectric Material）
导电层材料（Conductor Material）
其他高级选项设置（Advanced Option）
工作温度（Temperature）
平均过孔直径（Average Via Diameter）
平均电镀厚度（Average Via Plating Thickness）

### 7.13 双热阻（Dual Thermal Resistance）
AICFD支持双热阻模型。
在采取双热阻模型时，需要指定计算域为双热阻模型，并给与板边界结板热阻和壳边界结壳热阻。
![](media/image148.png)
图 7-43 双热阻模型

### 7.14计算域初始化 （Initialize）
完成所有的求解设置步骤之后，需要点击“计算域初始化（Initialize）”菜单按钮，此时软件会执行对整个域的初始化工作，为求解做好准备。

### 7.15启动求解 （Run Solver）	
计算域初始化完成后，可点击启动求解（Run Solver）菜单按钮下的直接求解（Run Directly），开始求解。AICFD提供了串行和并行两种求解方式，若求解模型网格规模较大，可选择并行求解加快求解速度，根据具体问题及计算机配置不同，用户可选择相应的并行核数。
![](media/image149.png)

图 7-44 运行求解
AICFD提供AI预测功能，在启动求解时候，用户可以设定预测参数，采样空间，采样方法等，单击应用（Apply）进入下一步，具体的步骤参考后续的实际案例操作。
![](media/image150.png)
图 7-45  AI预测样本设置

续算（restart）即在中断的数值模拟计算中，从先前保存的计算状态继续计算的过程，通常用于计算过程中调整求解参数或初始条件的场合。
下述情况下，AICFD不支持续算：
求解模型中不同湍流类型间的切换（例如层流切换至湍流，或者SST k-ω切换至S-A)
求解模型中多相流模式的切换（例如模式由关闭切换至开启，或者相数由2切换至3）
流体模型中燃烧类型的切换（例如由无切换至组分输运）
计算域设置中的任何修改（例如某计算域类型由流体域切换至多孔介质域）
边界类型的修改（例如某个面由入口改为出口）
监控 – 报告表已有监控量定义的修改（例如力报告中改变方向、切换域、改变已选区域面等操作，如下图所示）
![](media/image151.png)
图 7-46不支持续算的操作（以监控-报告表-力报告为例）

在至少满足一个上述情况的前提下，在原有工程文件基础上点击求解 – 直接求解，系统会给与不支持续算的提示，响应软件界面见下图：
![](media/image152.png)
图 7-47 AICFD界面不支持续算的提示

下述情况下（包括但不限于），AICFD支持续算：
求解模型中相同湍流类型间的切换（例如由标准k-epsilon模型切换至RNG k-epsilon模型）
边界条件中标量值的改动（例如入口速度由1m/s改为10m/s）
求解设置与求解控制中算法相关参数的改动（例如动量对流格式由二阶迎风格式改为一阶迎风格式，松弛因子的改动等）
监控 – 报告表已有监控量名称、数据显示状态的修改，此类操作不会影响既有数据的结果（例如将名称由Force1修改为Force2，勾选合并数据、显示分力等，如下图所示）
![](media/image153.png)
图 7-48支持续算的操作（以监控-报告表-力报告为例）

### 7.16停止求解 （Stop Run）
AICFD支持求解过程中暂停求解功能，用户可根据需求暂停当前求解任务。

### 7.17均方根残差 （RMS Residuals ）
AICFD支持生成均方根残差曲线。用户可根据需要选择查看。
![](media/image154.png)
图 7-49 残差曲线

### 7.18可视化求解结果 （Post Process Results）
求解完成后，用户可以选择直接查看后处理结果，点击“可视化求解结果（Post Process Results）”，即可在后处理视口窗查看可视化结果。

---

## 8. 后处理（Post） <a name="8-后处理post"></a>  
后处理菜单栏包含导入结果文件，动画演示，用户自定义位置（点，线，面，体，等值面），矢量图，云图，流线图，图表，变换及模型显示状态窗口。
![](media/image155.png)
图 8-1后处理菜单界面

### 8.1 导入结果文件（Load Result） <a name="81-导入结果文件load-result"></a>  
用户可直接导入结果文件，做可视化结果分析。在后处理菜单栏点击导入结果文件（Load Result）按钮，选择文件位置和文件类型，目前AICFD主要支持VTK类型文件的结果查看。
![](media/image156.png)
图 8-2 导入结果文件 

### 8.2 时序文件选择器（TimeStep Selector） <a name="82-时序文件选择器timestep-selector"></a>  
用户导入多个时序文件可通过时序文件选择器查看，可以对时序结果进行重新排序或删除操作，可通过时序文件选择器直接进入动画查看设置界面。  

### 8.3 用户自定义位置（Location） <a name="83-用户自定义位置location"></a>  
AICFD 提供了用户自定义位置菜单工具，生成的位置标记主要用于显示该位置的后处理结果信息。用户可根据需要创建各种形式的位置标记。
a.点位置：点击后处理菜单栏“创建点（Point）”工具，在弹出设置框中选择后处理结果对象，输入点位置名称和点坐标信息，AICFD提供两种方法生成自定义点位置。方法一：输入点位置三坐标，点击OK按钮，即可完成点位置创建；方法二：勾选显示点位置（Show Point）选项，通过移动交互平面工具，得到实时点位置信息，确认后点击OK按钮。
![](media/image157.png)
图 8-3  创建点位置

b.线位置：点击后处理菜单栏“创建线（Line）”工具，在弹出设置框中选择后处理结果对象，AICFD提供两种方法生成自定义线位置。方法一：分别输入两点位置坐标，点击OK按钮，即可完成线位置创建；方法二：勾选显示线位置（Show Line）选项，通过移动交互线工具，得到实时线位置信息，确认后点击OK按钮。
![](media/image158.png)
图 8-4  创建线位置
c.平面位置：点击后处理菜单栏“创建面（Plane）”工具，在弹出设置框中选择后处理结果对象，输入面位置名称，AICFD提供两种方法生成自定义平面位置，方法一：选择三点坐标或点和法线任意一种方式，输入坐标参数，即可生成一个用户自定义的面；方法二：通过拖动视口界面的辅助移动工具，确定最终位置信息，点击确认，将挂载到树节点上。
![](media/image159.png)
图 8-5 创建平面位置
d.体位置：目前支持创建正方体，球，圆柱体三种。点击后处理菜单栏“创建体（Volume）”工具，在弹出设置框中选择后处理结果对象，输入体位置名称，选择要创建的体形状，输入坐标参数，即可生成一个用户自定义的体，用户亦可通过拖动视口界面的辅助移动工具，确定最终位置信息，点击确认，将挂载到树节点上。
![](media/image160.png)
图 8-6 创建体位置
e.等值面：用户可通过“创建等值面（Isosurface）”菜单查看结果模型上特定变量（压力，温度，速度等）一些特定值的分布情况。点击菜单栏创建等值面工具，在弹出设置框中选择后处理结果对象，输入等值面名称，选择要显示的变量，根据需要输入等值面数值（可输入多个值），点击确认，视口端会显示对应数值的等值面，树节点上挂载等值面名称。
![](media/image161.png)
图 8-7 创建等值面  

### 8.4 矢量图（Vector） <a name="84-矢量图vector"></a>  
矢量图是用来显示模型每个网格点上的矢量信息。可以显示整个模型上的矢量场信息，也可以选择显示局部位置矢量信息。
操作步骤：
点击菜单栏矢量图按钮，弹出设置面板，设置面板从上到下设置顺序如下：
a.矢量图位置（Location）：下拉框中包含了结果模型本身以及所有的用户自定义位置（点，线，面，体，等值面），根据需求选择相应位置；
b.设置矢量图名称（Name）；
c.设置矢量点形状类型（Glyph Type）：目前只支持箭头类型；
d.设置矢量图方向（Orientation）：可选择“无方向”，此时系统默认统一方向；也可选择当前点速度方向；
e.设置矢量大小控制变量（Scale>Array）：下拉框选择矢量大小控制变量，可选择“均一大小”，或者其他控制变量。例如，选择温度，则每个点的矢量大小表示当前温度值大小；
f.设置矢量大小比例因子（Scale>Factor）：通过比例因子可调节矢量箭头的大小；
g.设置矢量点数量（Glyph）：可选择显示所有网格点矢量，或每隔N个网格点显示一个点矢量参数；
h.设置上色变量（Coloring）：可选择不同的变量给矢量图上色以查看该变量在矢量图位置上的大小分布。
![](media/image162.png)
图 8-8 创建矢量图
设置完成点击确认，后处理窗口中显示矢量图信息，左侧树节点上挂载矢量图名称。点击关闭按钮可关闭设置窗口。  

### 8.5 云图 （Contour） <a name="85-云图-contour"></a>  
通过对结果模型着色来显示各区域变量值大小。不同颜色对应不同的数值。可以显示整个模型云图，也可以选择显示局部位置云图。实际操作可点击菜单栏矢量图按钮，弹出设置面板，设置面板从上到下设置顺序为：
a.云图位置（Location）：下拉框中包含了结果模型本身以及所有的用户自定义位置（面、体、等值面），根据需求选择相应位置；
b.设置云图名称（Name）；
c.选择云图展示的信息变量（Variable）；
d.基于系统给出的变量数值范围（Range），设置当前云图显示数值范围；若不设置，默认显示范围即为从变量最小值到最大值；
e.设置云图层级（Level），用户给出云图的区间级数。例：层级设为6，变量数值区间将被均匀划分为6等份，每一等份用一种颜色来表示；
f.参数设置完成之后，点击OK查看视口端效果图，确认后，可点击关闭按钮关闭当前设置框，回到树节点界面，此时树节点上会挂载新建的云图名称。
![](media/image163.png)
图 8-9  创建云图 

### 8.6 流线图 （Streamline） <a name="86-流线图-streamline"></a>  
流线图用来表征一些质量为零的粒子通过流场域的路径。默认流线图针对的是稳态流动模拟。通过龙格-库塔方法，在控制时间步长条件下对矢量变量积分得到。具体设置操作如下：
a.首先从位置列表中选择粒子数据源（Location），可以选择从结果模型本身，用户自定义的体或自定义的面上散发出粒子；
b.输入流线名称（Name）；
c.选择矢量变量（Vector）：目前默认为速度；
d.选择积分方向（Integration Direction）：可以选择粒子往两侧发散轨迹，也可以选择往前、后某一方向发散；
e.选择积分方法（Integrator Type）：目前有龙格库塔2阶，龙格库塔4阶，龙格库塔4-5阶三种方法可选；
f.选择流线宽度（Streamline Length）：决定了流向的粗细程度；
g.设置流线种子类型和位置（Seed Type）：根据用户选择的数据源信息，输入相关的位置参数。比如用户选择了从自定义的体上散发流线，则需要设置体位置信息，包括中心位置和半径大小；
h.输入流线点数量（Number of Points）：输入流线点布置数量。例如用户设置了100个点，选择了从自定义的体表面散发流线，表示将在这个体表面均匀布置100个质量为零的点，每个点将会生成一条通过流场区域的轨迹线，所有点的轨迹线加在一起便是所要生成的流线图；
i.设置着色变量（Color By）：可通过选择不同的变量给流线着色。不同的颜色代表该处变量值的大小；
j.设置完成后点击确认按钮，视口端将会显示流线图。确认后可关闭设置面板回到树节点界面，此时树节点上会挂载流线图名称。
![](media/image164.png)
图 8-10 创建流线图
![](media/image165.png)
图 8-11 创建表面流线图

### 8.7 绘图 （Chart） <a name="87-绘图-chart"></a>  
图表功能主要用于做后处理曲线图。用户可自定义变量查看数据变化曲线，也可保存图表用于报告分析。具体操作步骤如下：
a.输入图表名称（Chart Name）；
b.选择图表类型（Chart Type）：目前默认为X-Y曲线图；
c.设置图表系列及对应源（Series&Location）：图表系列设置框中包含系列名称设置和系列数据源设置，点击右侧＋－号添加或删除系列；
d.设置坐标轴参数（X，Y Axis Variable）：点击某一系列名，设置对应的X，Y轴变量；
e.设置坐标轴节点数（X，Y Axis Tick）：分别设置X轴，Y轴坐标节点数；
f.设置曲线尺寸（Line>Size）：可通过调节曲线尺寸来改变每一个系列曲线的粗细程度；
g.设置系列颜色（Line>Color）：用户可对每一个系列设置不同的颜色，便于查看；
h.设置完成后点击确认按钮，视口会新增一个图标窗口，并显示创建的曲线图。确认后可关闭设置面板回到树节点界面，此时树节点上会挂载图表名称。
![](media/image166.png)
图 8-12 创建图表

### 8.8 动画演示 （Animation） <a name="88-动画演示-animation"></a>  
AICFD支持动画演示后处理结果。用户可选择演示两种形式动画。
第一种动画演示形式：查看时序结果文件动画效果。具体操作步骤如下：
a.导入时序结果文件（Load Results）；
b.筛选时序结果文件或重新排序（Timestep Selector）；
c.点击动画按钮（Animation）；
d.选择瞬态动画选项（Transient）；
e.选择动画对象（Post Objects）：可以任意选择已创建的云图，矢量图或流线图；
f.选择查看方式（Control By）：目前默认为按时间顺序播放；
g.选择开始步数（Start Step）；
h.选择结束步数（End Step）。
![](media/image167.png)
图 8-13 时序结果动画
第二种动画演示形式：查看稳态流动示踪粒子轨迹动画。具体操作步骤如下：
a.点击动画按钮（Animation）；
b.选择稳态动画选项（Steady）；
c.选择后处理结果文件（Results）：选择需要查看粒子轨迹的结果文件名称，若未导入，可通过导入后处理结果菜单导入后再重新点击动画界面选择； 
d.选择矢量变量（Vector）；
e.设置透明度（Alpha）；
f.设置轨迹宽度（Step Length）；
g.设置粒子数量（Number of Particles）；
h.设置粒子最大存活时间（Max Time to Live）：粒子最大存活时间决定了动画的频率周期。
![](media/image168.png)
图 8-14 示踪粒子轨迹动画

### 8.9 对比（Compare） <a name="89-对比compare"></a>  
对比功能对多个结果进行对比操作。比如对同一个网格的不同工况进行仿真时，可以通过对比功能同时查看不同结果。
![](media/image169.png)
图 8-15 结果对比 

### 8.10 探针（Probe） <a name="810-探针probe"></a>  
探针功能可实现域内任意点的变量值报告，同时可以获取该域内变量最值的报告及位置标注。
![](media/image170.png)
图 8-16 探针设置面板
![](media/image171.png)
图 8-17 探针温度场标注  

### 8.11 变换 （Transform） <a name="811-变换-transform"></a>  
变换功能主要用于对一个对象进行多次复制绘制。比如对一个叶轮机械模型进行仿真时，我们可以只对其中八分之一部分进行求解。在后处理中通过旋转平移等方式绘制出另外八分之七的模型，以便查看完整模型后处理结果。具体操作如下：
a.选择变换源；
b.创建变换名称；
c.旋转变换：设置三坐标旋转角度；
d.平移变换：设置三坐标平移数值大小；
e.缩放变换：若需要对模型进行缩放，可设置三坐标缩放比例（默认比例为1）；
以上三种变换形式可任选一种或选择几种方式叠加进行变换。
![](media/image172.png)
图 8-18 变换设置

### 8.12 旋转机械后处理模块（TurboPost） <a name="812-旋转机械后处理模块turbopost"></a>  
详见第13节。  

### 8.13 模型显示状态窗口 （View） <a name="813-模型显示状态窗口-view"></a>  
模型显示状态窗口主要用于切换模型显示方式，用户可根据需要选择以下几种形式显示：
![](media/image173.png)
图 8-19 模型显示方式
a.表面显示：显示不透明模型几何表面；
![](media/image174.png)
图 8-20 显示模型表面
b.表面+网格节点显示：显示带网格的模型不透明表面；
![](media/image175.png)
图 8-21 显示模型表面加网格节点
c.框架显示：透明化几何模型，显示模型网格；
![](media/image176.png)
图 8-22 显示模型结构框架
d.点显示：只显示模型上网格点。
![](media/image177.png)
图 8-23 显示模型点集  

### 8.14 导出求解结果 （Export Data） <a name="814-导出求解结果-export-data"></a>  
求解完成后，可导出后处理.csv格式数据文件，用户可自定义文件名称和保存路径。

---

## 9. 树节点 <a name="9-树节点"></a>  
树节点包含了整个仿真过程所有的操作步骤，主要包含几何网格、求解、后处理三大部分。
![](media/image178.png)
图 9-1 树节点
### 9.1 几何（Geometry） <a name="91-几何geometry"></a>  
几何节点下包含了几何模型，导入几何后可以展示几何模型的域，边界列表，通过右健进入重命名，边界合并，边界拆分，删除等操作。

### 9.2 网格（Mesh） <a name="92-网格mesh"></a>  
网格节点下包含了加密区域，网格区域两部分内容。
#### 9.2.1加密区域（Mesh Density）
右击树节点“网格（Mesh）＞“加密区域（Mesh Density）”，可以创建“立方体（Box）”， “球体（Sphere）”， “圆柱体（Cylinder）”辅助几何。
![](media/image179.png)
图 9-2 添加加密区域
右击树节点已经添加的辅助几何，进入编辑面板，可设置加密区域详细信息，包括位置，尺寸和加密设置。
![](media/image180.png)
图 9-3 边界加密区域
#### 9.2.2网格域（Mesh Domains）
右键树节点网格域，可以将进行读取面网格、读取体网格、添加体网格、替换体网格等操作。
![](media/image181.png)
图 9-4 右键树节点网格域
导入网格后可以展示网格模型的域、边界列表、通过右键树节点网格>网格域>模型进入展开所有，全部收起，删除等操作。
![](media/image182.png)
图 9-5 右键树节点网格模型
右键树节点网格>网格域>边界列表进入按角度划分、合并、重命名、删除操作。
![](media/image183.png)
图 9-6 右键树节点网格边界
右健树节点网格>网格域>域，插入域，创建自定义位置。
若求解模型为多相流，需要用户新建自定义区域，作为第N种材料对应区域。具体操作如下：
a.右击网格区域节点（Mesh Domains）；
b.添加自定义区域（Insert Zones）；
c.输入区域名称（Name）；
d.选择区域归属计算域名称（Location）；
e.选择区域形状（Zone Type）；
f.设置区域位置参数；
g.指定区域与计算域的布尔运算方式，通过点击区域外或区域内按钮实现；
h.设置完成后点击确认，树节点网格区域（Mesh Domains）>区域（Zone）下方会挂载新建区域名称。
![](media/image184.png)
图 9-7 自定义域设置

### 9.3 仿真模拟（Simulation） <a name="93-仿真模拟simulation"></a>  
仿真模拟包含了求解模型、材料、流体域分析、求解设置、求解控制、计算域初始化、监控几个部分。
#### 9.3.1求解模型（Solution Modeling）
求解模型包括AI预测和基本模型设置部分。
![](media/image185.png)
图 9-8 AI预测设置界面
AI预测设置界面
a.预测模式启动选项（AI Predict Mode）：样本计算完成后，需要对样本进行训练，样本训练可以在样本计算后一键完成，或者在本页面点击Train按钮完成，训练完成后，预测模式可启动（On选项可用）；
b.预测变量输入表格：预测模式启动后界面会生成预测变量列表和对应预测值，用户完成输入后点击Apply可一键进行结果预测。完成预测后用户可点击Post-process查看结果文件。
![](media/image186.png)
图 9-9 求解基本模型设置

基本模型设置界面
a.设置流动模型（Time）：稳态流动或瞬态流动；
b.设置流体性质（Flow）：可压缩流体或不可压缩流体；
c.设置马赫数类型（Mach）：若用户设置为瞬态流动，且流体为可压缩流体，可设置亚音速或超音速；
d.设置湍流模型（Turbulence）：可选择层流或湍流（Reynolds Averaged Navier-Stokes Models(缩写为RANS）、Detached Eddy Simulation（缩写为DES)和Large Eddy Simulation（缩写为LES）。选择湍流后，需要确认具体的湍流模型，RANS有Zero Equation、Spalart-Allmaras、k-epsilon（包含Standard k-epsilon、RNG k-epsilon和 Realizable k-epsilon），k-omega（包含Standard k-omega和SST k-omega）三种类型可选，LES有Standard Smagorinsky、Dynamic Smagorinsky和WALE三种模型可选，DES有Detached Eddy Simulation（S-A）、Detached Eddy Simulation（SST k-omega）、Delayed DES（S-A）、Delayed DES（SST k-omega）、Improved DDES（S-A）和Improved DDES（SST k-omega）模型可选；
e.设置多相流参数（Multi phase）：若选择了瞬态不可压流动，需设置多相流选项，可设置单项流（多相流关闭）、自由表面、混合表面和欧拉欧拉四种模式，目前只支持前三种。若为多相流，需要设置项数量，目前默认为两相流；
f.设置噪声（Sound）：提供 FWH 和Curle噪声模型；
g.设置传热参数（Thermal）：对于可压缩流体，默认勾选能量传递选项，用户可根据实际情况选择勾选浮力项。若为不可压流体，用户可根据需要选择是否勾选能量和浮力选项；
h.设置重力加速度（Gravity）：需要用户设置重力加速度三个分量值。

#### 9.3.2材料（Material）
右击树节点可从材料库中添加材料，点击确认后添加的材料会挂载到材料树节点下面，便于设置计算域时选择。请注意：计算域的材料只能从树节点材料下挂载的列表中选择。
![](media/image187.png)
图 9-10  材料树节点

#### 9.3.3流体域分析（Flow Analysis）
流体域分析树节点包含了计算域列表，交界面列表和用户新建区域列表。
![](media/image188.png)
图 9-11  树节点：流动分析
##### 9.3.3.1计算域（Domains）
建立计算域是建立仿真过程的基本步骤之一，右击流体与分析节点，或点击菜单栏新建计算域按钮，设置完成后，计算域节点上会挂载新建的域名称。AICFD支持求解多域流动模型。
![](media/image189.png)
图 9-12 树节点：计算域 

##### 9.3.3.2交界面（Interfaces）
用户可右击流动分析>交界面或点击菜单栏新建交界面，并设置相应的参数，新建的交界面列表会挂载到交界面树节点上。
![](media/image190.png)
图 9-13 树节点：交界面 

##### 9.3.3.3热模型（Thermal Models）
用户可右击流动分析>热模型或点击菜单栏新建热模型，并设置相应的参数，新建的热模型列表会挂载到交界面树节点上。
![](media/image191.png)
图 9-14 树节点：热模型 

#### 9.3.4求解设置（Solver Setting）
计算域，边界及自定义区域设置完成之后，需要设置求解设置相关参数，包括对流项格式，限制器和时间控制方法。
a.设置对流项格式：目前有多种格式可选（1st Upwind， 2nd Upwind， 3rd Upwind， Central Difference，Central Difference/1st Upwind，Central Difference/3rd Upwind，Bounded Central Difference）；
b.空间离散方法：目前提供两种方法（Green-Gauss和Least Squares）；
c.压力插值方法：目前提供两种方法（Linear和Mixed）；
d.限制器：2nd Upwind， 3rd Upwind两种数值格式，用户可设置限制器Slope，Venkat，Minmod和None四种方式，目前求解器推荐使用2nd Upwind+Venkat限制器；
e.时间控制方法：目前提供两种方法（Euler Implicit和Crank Nicolson）；
f.Rhie-Chow插值：目前提供三种格式：弱、中、强；
g.交叉扩散：默认不勾选。
![](media/image192.png)
图 9-15 树节点：求解基本参数设置 

#### 9.3.5求解控制（Solver Controls）
求解控制主要用于设置求解过程控制相关参数。具体设置如下：
a.迭代步数：包括开始迭代步数和最大迭代步数；
b.收敛值：判定求解结果是否收敛依据，主要用于稳态流动；
c.设置时间项：提供Auto、Constant和none三种时间项方法。Auto：设置库朗数，平衡求解准确性和效率的参数。随着库朗数的增大，收敛速度会加快，稳定性会降低，用户可根据实际情况设置参数；Constant：设置固定时间步长；
d.松弛因子：松弛因子的值在0～1之间，越小表示两次迭代值之间变化越小，也就越稳定，但达到收敛所用的迭代次数也就越多，需要的计算时间也就越久；
e.交界面误差值：范围0-1，软件给出默认值为1e-7；
f.SIMPLE迭代算法：设置迭代最大步数和误差值（0-1）；
g.SIMPLE迭代算法的压力方程/速度方程：迭代次数：软件给出默认值为40/20，用户可根据经验调节数值大小；绝对收敛值：软件给出默认值为1e-8/1e-10，用户可根据经验调节数值大小；
h.矩阵求解器：提供CG和AMG（代数多重网格）、BiCG STAB和Gauss Seidel四种求解器，共轭梯度迭代（主要用于对称矩阵）和双共轭梯度迭代（主要用于非对称矩阵）建议使用推荐值。
![](media/image193.png)
图 9-16 树节点：求解控制参数设置

AICFD提供AMG（代数多重网格）高级设置，通过点击设置图标按钮进入参数面板。用户可以自由地设置这部分从而获得更高效的求解器。
a.迭代求解器：AICFD支持的迭代求解器有共轭梯度法（Conjugate Gradient，CG）、稳定双共轭梯度法（Biconjugate gradient stabilized method, BiCGStab）、广义最小残量法（Generalized Minimal ResidualMethod、 GMRES)方法；
b.压力绝对收敛准则：界面默认0.01；
c.最大粗化层数：整数，界面默认10。最大代数多重网格层数，当层数超过它时，将停止产生更稀疏网格；
d.前松弛（npre）：界面默认1；
e.后松弛（npost）：界面默认1；
f.周期类型：提供多种类型，包括V-cycle、 W-cycle、F-cycle；
g.AMG次数（pre_cycles）：1；
h.最粗网格数（coarse_enough）：1000；
i.最粗网格求解（direct_coarse）：false；
j.粗化方法（type）：提供多种方法，包括smoothed_aggregation、aggregation、smoothed_aggr_emin、ruge_stuben；
k.粗化因子（eps_strong)：界面默认0.2；
l.光顺方法（type）：提供多中方法，包括gauss_seidel、jacobi_damped、ilu0、spai0。
![](media/image194.png)
图 9-17 代数多重网格设置 

#### 9.3.6计算域初始化（Field Initialization）
求解设置完成之后需要对流场环境进行初始化，包括速度、压强和动量设置；若为多相流还需设置主相相关信息。
![](media/image195.png)
图 9-18 树节点：计算域初始化设置

#### 9.3.7监控（Monitoring）
监控树节点包含残差曲线（Residuals）和报告图表（Report charts）两部分内容；
残差曲线（Residuals）：目前包含方均根残差和最大残差，监控变量包含连续性、速度的三方向分量值、湍流变量值和温度。
报告图表（Report charts）：包含流量/能量报告（Flow/Energy Report），受力报告（Force Report），表面积分报告（Surface Integrals Report），体积积分报告（Volume Integrals Report），用户自定义点报告（User Point）。
![](media/image196.png)
图 9-19 报告图表

a.流量/能量报告（Flow/Energy Report）：用于输出单位时间内通过有效截面的质量流量（Mass Flow Rate）和单位时间内通过有效截面的热通量（Heat Flux）；
 ![](media/image197.png)![](media/image198.png)
图 9-20 流量/能量报告设置界面

b.受力报告（Force Report）：用于查看壁面所受压力&摩擦力，阻力系数以及力矩；
![](media/image199.png)![](media/image200.png)![](media/image201.png)
图 9-21 力/力系数/力矩报告设置界面
c.面积分报告（Surface Integrals Report）：包括平均温度、平均压力、平均速度、平均总温、平均总压、压降、最大温度、最小温度、最大压力、最小压力、最大速度、最小速度；
![](media/image202.png)
图 9-22 树节点：面积分报告
![](media/image203.png)
 图 9-23 面积分报告设置界面-平均压力
d.体积积分报告（Volume Integrals Report）：包括平均温度，平均压力，平均速度，平均总温，平均总压，压降，最大温度，最小温度，最大压力，最小压力，最大速度，最小速度；
     ![](media/image204.png)
图 9-24树节点：面积分报告             
![](media/image205.png)
图 9-25 体积分报告设置界面-最大温度
e.用户自定义点（User Point）：用户可根据自定义点坐标来观察该点的变量值。支持点的压力，温度，速度监控。
![](media/image206.png)
图 9-26 自定义点监控  

### 9.4 后处理（Post） <a name="94-后处理post"></a>  
后处理树节点分为四部分：结果、场景、报告和旋转机械后处理。   

#### 9.4.1结果（Result）
其中结果文件为当前读入的后处理VTK文件名，其他导入结果都会按创建顺序挂载到结果树节点下。
![](media/image207.png)
图 9-27 后处理结果树节点

#### 9.4.2报告（Report）
报告功能目前支持在日志窗口输出后处理相关数据，包括包含流量/能量报告（Flow/Energy Report），受力报告（Force Report）、表面积报告（Areas）、表面积分报告（Surface Integrals Report），体积积分报告（Volume Integrals Report）、噪声后处理（Sound Post）、投影面积（Projected Surface Areas）、自定义变量（User Defined Variable）。
![](media/image208.png)
图 9-28 后处理报告树节点
流量/能量报告（Flow/Energy Report）、受力报告（Force Report）、表面积报告（Areas）、表面积分报告（Surface Integrals Report）和体积积分报告（Volume Integrals Report）具体输出内容参考10.3.7监控（Monitoring）部分的详细解释。
噪声后处理模块（Sound Post）：若用户进行了噪声仿真，在完成计算后，可在噪声后处理（Sound Post）进行压力脉动和声压级的计算。
![](media/image209.png)
图 9-29 噪声后处理
用户可在树节点投影面积（Projected Surface Areas）中计算网格不同方向投影面积。
![](media/image210.png)
图 9-30 投影面积报告
用户可在树节点自定义变量（User Defined Variable）中设置自定义变量。
![](media/image211.png)
图 9-31 自定义变量

#### 9.4.3场景（Scene）
后处理查看结果都会按创建顺序挂载到场景树节点下，包括用户新建位置、云图、矢量图和流线图。
![](media/image212.png)
图 9-32 后处理场景树节点
#### 9.4.4旋转机械后处理（Turbo Post）
此模块只有在界面计算旋转机械类型案例加载结果并且点击TurboPost进行模型初始化后才为激活状态。
![](media/image213.png)
图 9-33 后处理旋转机械后处理树节点

---

## 10. 工具 （Tools） <a name="10-工具-tools"></a>  
工具菜单栏包含了录制脚本：播放脚本文件、新建脚本文件、开始录制脚本、停止录制脚本；单位设置、用户许可；界面显示、隐藏等功能。
![](media/image214.png)
图 10-1 工具菜单栏

### 10.1 单位设置 <a name="101-单位设置"></a>  
设置当前模型的单位，该单位为全局变量，适用于前处理和后处理。当前版本暂未支持此功能。
![](media/image215.png)
图 10-2 单位制 

### 10.2 语言 <a name="102-语言"></a>  
用户点击可选择当前界面语言。AICFD支持简体中文和英文语言。
![](media/image216.png)
图 10-3 语言选择

### 10.3 高级设置 <a name="103-高级设置"></a>  
用户点击可进行高级设置，可以设置开关预处理、开关自动加载求解结果、开关载荷质量和选择投影方法。
![](media/image217.png)
图 10-4 高级设置  

### 10.4 自定义函数 <a name="104-自定义函数"></a>  
用户点击可进行高级设置，可以设置开关预处理、开关自动加载求解结果、开关载荷质量和选择投影方法。
![](media/image218.png)
图 10-5 自定义函数  

### 10.5 自定义标量


### 10.5 自定义标量 <a name="105-自定义标量"></a>  
用户点击可进行高级设置，可以设置开关预处理、开关自动加载求解结果、开关载荷质量和选择投影方法。

![图 10-6 自定义标量](media/image219.png)  

### 10.6 界面显示功能 <a name="106-界面显示功能"></a>  
勾选项目数据可显示左侧树节点，关闭可使视口界面放大。输出日志窗口和工具栏也可根据需要选择显示或不显。

### 10.7 宏录制 <a name="107-宏录制"></a>  
AICFD支持宏录制功能，可实现自动化前处理和仿真求解。

---

### 11. 帮助（Help） <a name="11-帮助help"></a>  
帮助菜单栏包含帮助、许可证、版本信息等。
![](media/image220.png)
图 11-1 帮助菜单栏

### 11.1 用户手册 <a name="111-用户手册"></a>  
点击帮助菜单，可查看软件详细用户手册。  

### 11.2 案例手册 <a name="112-案例手册"></a>  
点击帮助菜单，可查看软件详细用户手册。

### 11.3 用户许可 <a name="113-用户许可"></a>  
用户点击可查看或编辑当前服务器IP地址。
![](media/image221.png)
图 11-2 用户许可
 

### 11.4 关于 <a name="114-关于"></a>  
点击关于菜单，可查看软件版本信息、公司信息、版权保护信息等。  

---

### 12. 操作简介 <a name="12-操作简介"></a>  

### 12.1 新建工程 <a name="121-新建工程"></a>  
软件启动后，此时界面树节点默认为灰色，需要新建工程或打开已有工程文件，点击菜单栏新建按钮，界面弹出弹框，定义工程名称及路径。
![](media/image222.png)
图 12-1 新建工程窗口

新建完成后点击OK按钮，激活左侧树节点。此时，左侧树节点上方新建工程名称，该工程默认包含当前树节点上所有内容，随着操作继续，其他节点会添加到对象树中。
除了新建工程文件，用户可以通过Open菜单打开已有工程文件，同时菜单还提供了保存（Save），另存（Save as）及关闭工程文件（Close）的功能。

### 12.2 导入模型 <a name="122-导入模型"></a>  
AICFD支持导入多种几何类型。点击“几何（Geometry）”菜单栏，选择“导入文件（Import Geometry）”，或者右击“几何（Geometry）”打开弹框，选择需要导入的文件类型及路径，单击OK完成几何导入。
输出窗口Output Message提供导入进程反馈。视口端显示导入的几何模型。在树节点上，展开几何（Geometry）节点，查看导入的几何模型。新导入的几何模型“Tube”下方会显示对应的几何面名称。
![](media/image223.png)
图 12-2 导入几何文件

### 12.3 可视化已导入几何模型 <a name="123-可视化已导入几何模型"></a>  
几何场景已在“几何”窗口（Geometry）中显示，原几何随机着色，不透明表面表示。

#### 12.3.1 平移、缩放和旋转视图 <a name="1231-平移缩放和旋转视图"></a>  
借助视口工具栏工具，可对几何模型进行平移，缩放，旋转和显示方向设置。通过“标尺”工具测量几何模型实际大小。
![](media/image224.png)
图 12-3 标尺功能

#### 12.3.2 高亮 <a name="1232-高亮"></a>  
点击树节点任意几何面视口端“几何”窗口中会对该面进行高亮。
![](media/image225.png)
图 12-4 高亮显示 

### 12.4 网格划分 <a name="124-网格划分"></a>  

#### 12.4.1 网格尺寸 <a name="1241-网格尺寸"></a>  
从主菜单单击持全局尺寸，体网格，面网格，边界层网格参数设置；用户可根据需求设置适合网格参数。
![](media/image226.png)
图 12-5 全局网格尺寸图

#### 12.4.2 定义边界表面 <a name="1242-定义边界表面"></a>  
分别定义几何模型的进口，出口，壁面位置（这里沿用重命名设置的表面名称）。
![](media/image227.png)
图 12-6 重命名后的几何面信息图

#### 12.4.3 体网格/面网格/边界层 <a name="1243-体网格面网格边界层"></a>  
双击几何面，按需要对已经的域或面进行相应的网格精度加密和加边界层。这里对单个域进行精度加密。点击对象选择选项，可同时选择几个域一次性设置加密参数。
![](media/image228.png)![](media/image229.png)![](media/image230.png)
图 12-7 体网格/面网格/边界层设置 

#### 12.4.4 局部加密 <a name="1244-局部加密"></a>  
可根据需要创建自定义加密区域，对特殊部位进行局部加密操作，这里对弯管弯曲部分进行局部加密。
点击菜单栏选择网格加密中的“立方体（Box）”、 “球体（Sphere）”、 “圆柱体（Cylinder）”或者右击树节点“网格（Mesh）＞“网格加密（Mesh Density）”。
 ![](media/image231.png)![](media/image232.png)
图 12-8 添加加密区域
设置加密区域尺寸，或过鼠标拖动来调加密区边界位置。
![](media/image233.png)![](media/image234.png)
图 12-9立方体加密区域
### 12.5 创建网格 <a name="125-创建网格"></a>  
点击“创建网格（Create Mesh）”按钮，即可一键生成网格文件，视口端自动跳转至“Pre-Processing”窗口。
![](media/image235.png)
图 12-10 生成的网格视口，网格信息查看界面

### 12.6 求解分析 <a name="126-求解分析"></a>  

#### 12.6.1 设置求解模型 <a name="1261-设置求解模型"></a>  
网格生成之后，需要进行求解模型设置。功能选项包括流动状态：稳态流动还是瞬态流动；可压缩性，马赫数，湍流模型，是否为多相流，是否涉及噪声，是否涉及传热和浮力，及重力加速度。本例中为稳态，不可压缩，层流，无传热模型。点击树节点求解模型设置界面-选择-稳态-层流，此时AI预测、马赫数、多相流选项、噪声、传热、浮力及重力设置选项将为置灰状态。
![](media/image236.png)
图 12-11 求解模型设置界面

#### 12.6.2 材料设置 <a name="1262-材料设置"></a>  
“材料（Materials）”列出了常用的材料模型，双击某一材料可查看相关参数。除了树节点显示的材料，AICFD同时提供了更为丰富的材料库，右击Materials，可打开材料库，选择材料后，可将材料库中的模型导入到树节点，方便用户查看和使用。
![](media/image237.png)
图 12-12  AICFD的材料库

#### 12.6.3 建立流体域分析模型 <a name="1263-建立流体域分析模型"></a>  

##### 12.6.3.1 设置计算域 <a name="12631-设置计算域"></a>  
本软件支持求解多域模型，生成网格之后，程序会自动创建默认计算域Default Domain，用户可直接在该计算域设置边界条件；或右击树节点Domains添加新的计算域；
a.自定义计算域名称；
b.选择计算域对应网格域位置，此案例为单域，选择当前网格域即为计算域；
c.定义计算域类型，此案例为流体域；
d.选择计算域材料，此处可自定义材料名；单击材料框可从材料树节点下方的材料中选择，本案例中的材料选择“水”；
e.此案例不涉及旋转功能，旋转设置中选择“静止”选项；
f.点击确认按钮，新的计算域会挂载到流体域分析下计算域下方。
![](media/image238.png)
图 12-13 计算域设置界面

##### 12.6.3.2 设置边界条件 <a name="12632-设置边界条件"></a>  
设置进口边界条件
右击树节点边界设置（Boundaries），点击添加边界条件（Insert Boundary），进入设置界面。
a.自定义进口边界名称；
b.选择对应计算域，这里默认为当前计算域；
c.点击边界面右边多选选项，选择进口面；
d.选择边界类型为速度进口；
e.设置进口速度，这里选择笛卡尔三坐标确定进口速度矢量；
f.点击确认按钮回到树节点。
![](media/image239.png)
图 12-14 进口边界条件设置界面

设置出口边界条件
再次右击树节点边界设置（Boundaries），点击添加边界条件（Insert Boundary），进入设置界面。
a.自定义出口边界名称；
b.选择对应计算域，这里默认为当前计算域；
c.点击边界面右边多选选项，选择出口面；
d.选择边界类型为静压出口；
e.设置出口静压，这里设为大气压；
f.点击确认按钮回到树节点；
![](media/image240.png)
图 12-15 出口边界条件设置界面

设置壁面边界条件
右击树节点边界设置（Boundaries），点击添加边界条件（Insert Boundary），进入设置界面。
a.自定义出口边界名称 ；
b.选择对应计算域，这里默认为当前计算域；
c.点击边界面右边多选选项，全部选中为壁面（已设置过的面将不在多选框中出现）；
d.选择边界类型为流体壁面；
e.设置静止壁面，无滑移模式；
f.点击确认按钮回到树节点。
![](media/image241.png)
图 12-16 壁面边界条件设置界面

#### 12.6.4 求解设置 <a name="1264-求解设置"></a>  
点击树节点“求解设置（Solver Setting）”按钮，进入求解设置界面。
a.设置对流项格式为二阶迎风格式（2st Upwind）；
b.设置空间离散方法，这里设置为Green-Gauss；
c.设置压力插值方法，这里设置为Linear；
d.设置限制器，这里设置为Venkat；
e.设置时间计算方法，这里设置为Implicit；
f. 点击确定按钮返回树节点。
![](media/image242.png)
图 12-17求解基本设置界面

#### 12.6.5 求解控制 <a name="1265-求解控制"></a>  
点击树节点“求解控制（Solver Control）”按钮，进入求解控制界面。
a.设置开始迭代和结束迭代步数，开始迭代默认为模型当前求解步数；
b.此案例为稳态流动，故需设置收敛值，默认值0.0001；
c.时间步长类型设为自动，设置库朗数30；
d.松弛因子设为默认值，压力0.3，温度0.7，湍流0.7，温度0.7，共轭传热0.9；
e.交界面误差：设置默认值为1e-5；
f.迭代算法，设为默认值最大迭代步数为1，误差为0.2；
g.设置矩阵求解器，默认推荐Conjugate Method，设置压力方程迭代步数40，绝对收敛值1e-8；速度方程迭代步数20，绝对收敛值1e-10；
h.设置求解限制，最小绝对压力和最大绝对压力，最大绝对速度默认为100m/s；
i.输出步频，设置瞬态模型时开启，默认步频为5；
j.点击确认按钮，回到树节点。
![](media/image243.png)
图 12-18求解控制设置界面

#### 12.6.6 计算域初始化 <a name="1266-计算域初始化"></a>  
点击树节点“计算域初始化（Field Initialization）”按钮，进入计算域初始化界面。
a.设置初场流动速度，这里设为进口速度；
b.设置初场压强，这里设为大气压；
c.点击确认按钮，回到树节点；
d.点击菜单栏计算域初始化按钮，可以在日志输出框中查看初始化状态。
![](media/image244.png)
图 12-19 初始化设置界面  

### 12.7 运行求解 <a name="127-运行求解"></a>  
初始化成功后点击菜单栏“运行求解（Run Solver）”按钮，选择Run Directly，弹出求解器控制（Run Solver）窗口。用户可选择串行（Serial）或并行（Parallel）计算方式，其中对于大模型，并行计算可充分利用电脑资源，根据计算机的核数进行设置。本案例模型较小，直接采用串行方式。
![](media/image245.png)
图 12-20 求解器控制窗口

点击运行（Start），可看到监控窗口中已开始生成残差曲线。
求解完成后，点击保存按钮保存当前工程文件。

### 12.8 后处理 <a name="128-后处理"></a>  
点击求解（Solution）菜单栏中“生成后处理结果（Post-Process Result）”按钮，可在后处理窗口查看结果。

#### 12.8.1 云图 <a name="1281-云图"></a>  
后处理云图有两种查看方式：
a.查看计算模型整体云图。
点击后处理菜单栏云图（Contour）菜单，云图对象（Location）选择结果模型，查看压力云图，或其他参数云图。
b.查看特殊位置云图（这里以平面云图举例，其他位置类似）。
点击菜单栏位置>平面（Location>Plane）菜单，创建平面1（Plane1）。点击云图（Contour）菜单，云图对象（Location）选择平面1（Plane1），查看压力云图或其他参数云图。
![](media/image246.png)
图 12-21 结果云图
![](media/image247.png)
图 12-22 创建平面
![](media/image248.png)
图 12-23 平面云图 

#### 12.8.2 矢量图 <a name="1282-矢量图"></a>  
与云图一样，后处理矢量图有两种查看方式：
a.查看计算模型整体矢量图。
点击后处理菜单栏矢量图（Vectors）菜单，矢量对象（Location）选择结果模型，查看速度矢量图，或其他参数对应矢量图。
b.查看特殊位置矢量图（这里以平面矢量图举例，其他位置类似）。
点击菜单栏位置>平面（Location>Plane）菜单，创建平面1（Plane1）。点击矢量图（Velocity）菜单，矢量图对象（Location）选择平面1（Plane1），查看速度矢量图或其他参数矢量图。
![](media/image249.png)
图 12-24 矢量图设置
![](media/image250.png)
图 12-25 矢量图

#### 12.8.3 流线图 <a name="1283-流线图"></a>  
点击流线图（Streamline），流线对象选择模型（Location>RES），矢量选择速度（Vector>Velocity），根据模型大小输入适当大小的流线长度（Streamline Length），此处模型最大长度为0.35m，流线散发源为半径为0.05的球。可选择显示或隐藏球面源。流线图颜色显示压力场大小。
![](media/image251.png)
图 12-26流线图
![](media/image252.png)
图 12-27 流线图设置界面&辅助球体  

---

### 13. 旋转机械模块（Turbomachinery） <a name="13-旋转机械模块turbomachinery"></a>  
#### 13.1 新建工程（New Project） <a name="131-新建工程new-project"></a>  
新建工程：选择Turbomachinery模式进入。
操作步骤：点击新建菜单按钮（New），弹出新建工程对话框（New Project），点击Turbomachinery进入旋转机械向导模式，设置工程名称和路径。弹框下方默认路径勾选，可记忆当前路径为工程文件默认路径。
![](media/image253.png)
图 13-1 新建工程文件  

#### 13.2 基础设置（Basic Settings） <a name="132-基础设置basic-settings"></a>  
操作步骤：
a.设置叶轮机械类型（Machine Type）：Pump或Fan；
b.设置流动模型（Analysis Type）：稳态流动或瞬态流动；默认为稳态（Steady）。
![](media/image254.png)
图 13-2 基础模型设置  

#### 13.3 计算域定义（Component Definition） <a name="133-计算域定义component-definition"></a>  
操作步骤：
a.点击“Add Component”，弹出二级设置界面；
b.定义计算域名称，设置计算域类型（旋转域/静子域），设置完成，点击OK按钮，将计算域增加至树节点。
![](media/image255.png)
图 13-3 添加计算域

例如：添加转子域（Rotating Component）
![](media/image256.png)
图 13-4 添加转子域

a.计算域类型：根据上一页弹框设置信息，显示计算域类型：Rotating；
b.角速度：设置旋转域转轴角速度；
c.网格：选择计算域对应网格文件；
d.定义轴：
e.默认名称Coordiante Axis
f.旋转轴：X，Y，Z
g.旋转轴显示，勾选后视口显示旋转轴；
h.网格域：识别所选的网格文件中的网格域，视口区可同步显示被选中的网格域；
i.边界信息：根据边界名称自动识别， 例如Component “R1”中包含“Hub”字样边界读入 Hub选项框中。
![](media/image257.png)
图 13-5 创建转子域

例如：添加静子域（Stationary Component）
![](media/image258.png)
图 13-6 添加静子域

a.计算域类型：根据上一页弹框设置信息，显示计算域类型：Stationary；
b.网格：选择计算域对应网格文件；
c.网格域：识别所选的网格文件中的网格域，视口区可同步显示被选中的网格域；
d.边界信息：根据边界名称自动识别，例如Component “R1”中包含“Hub”字样边界读入 Hub选项框中。
![](media/image259.png)
图 13-7 添加静子域 

#### 13.4 物理参数定义（Physics Definition） <a name="134-物理参数定义physics-definition"></a>  
列出了常用的流体材料模型，双击某一材料可查看相关参数除了树节点显示的材料，AICFD同时提供了更为丰富的材料库，右击Materials，可打开材料库，选择材料后，可将材料库中的模型导入到树节点，方便用户查看和使用；
a.参考压力：计算域参考压力，单位包含Pa和atm；
b.传热方式：None/Total Energy；
c.湍流模型：Laminar/Standard k-Epsilon；
d.进出口边界条件组合：列出了进出口边界条件组合
e.None：不指定类型
f.总压入口，静压出口
g.总压入口，质量流量出口
h.质量流量入口，静压出口；
i.交界面处理方式：
j.若为稳态计算（Time=Steady），默认为Frozen Rotor
k.若为瞬态计算（Time=Transient），默认为Sliding Mesh；
l.求解参数设置（Solver Paramenters）：对流项格式（Advection Scheme）、最大迭代步数（Max Iteration）、时间步长控制方式(Time Step Control)、库朗数（Courant Number）。
![](media/image260.png)
图 13-8 物理参数定义

#### 13.5 交界面定义（Interface Definition） <a name="135-交界面定义interface-definition"></a>  
a.右击Interface可添加交界面；
b.Type类型包括：None、Frozen Rotor（瞬态为Sliding Mesh）、Periodic；
c.交界面自动识别：
1) 界面设置中已识别的Periodic1，Periodic2 自动创建为Periodic类型交界面，命名规则为：“边界名1”to “边界名2”。
2) 自动识别相邻Component之间的交界面，若为转子-静子域，则设置为Frozen Rotor（稳态）或Sliding Mesh（瞬态）类型交界面，命名规则同上。
3) 若存在Tip面，自动创建转子与Tip面之间交界面，类型为None，命名规则同上。
![](media/image261.png)
图 13-9 交界面定义

#### 13.6 边界定义（Boundaries Definition） <a name="136-边界定义boundaries-definition"></a>  
包含质量流量入口、总压入口、静压入口、速度入口、静压出口、质量流量出口、壁面及对称边界8种边界条件，向导模式中边界条件说明如下:
对于转子域壁面边界条件，提供了无滑移（No slip）和自由滑移(Free slip)两大类壁面边界条件，其中无滑移边界条件类型包括相对旋转壁面（Rotating）和绝对静止壁面(Counter Rotating)两种，静子域壁面边界条件与常规模式相同。
本模块中，基于Region Information识别信息和进出口边界类型提供自动创建边界条件功能，自动创建规则如下：
a.右击选项：Add Boundary；
b.树节点一级节点应为Component，二级节点为边界名称；
c.根据前面设置信息，自动创建进出口边界条件，若前面进出口边界类型选择为None，则默认设置为总压入口、静压出口边界条件；
d.根据Region Information识别信息，对已识别边界创建对应的边界条件，包括：Hub、Shroud、Blade设置为Wall 边界类型、转子壁面默认类型为No Slip Wall、静子壁面默认为Counter Rotating Wall；
e.Symmetry边界设置为Symmetry类型；
f.进入Next前，判断是否所有边界均已设置完成，所有边界条件设置完成后进入下一步；
g.用户可根据实际问题修改边界条件，设置方法与常规模式类似，参考“6.2”。
![](media/image262.png)
图 13-10 边界定义

#### 13.7 进入常规模式（Enter General Mode） <a name="137-进入常规模式enter-general-mode"></a>  
完成前处理设置后，可选择进入常规模式（Enter General Mode）进行更多设置，或直接开始求解（Start Solver），求解之前可通过勾选（Save Project）保存工程文件。
![](media/image263.png)
图 13-11 进入常规模式  

---

### 14. 旋转机械后处理（Turbo Post） <a name="14-旋转机械后处理turbo-post"></a>  
旋转机械后处理模块主要包含模型初始化（Turbo Initialization）、三维视图（3D View）、叶间平面（Blade-to-Blade）、子午面（Meridional）、自定义位置（Location）和图表（Turbo Chart）。

#### 14.1 模型初始化（Turbo Initialization） <a name="141-模型初始化turbo-initialization"></a>  
加载结果后，点击TurboPost进行模型初始化，激活TurboPost模式。分别选择需要初始化的结果及其计算域。
![](media/image264.png)
图 14-1 模型初始化
![](media/image265.png)
图 14-2 选择初始化VTK
点击自动初始化（Auto-Initialize），软件会根据前处理信息，自动进行模型始化，并将结果文件和计算域加载到树节点，显示如下：    
![](media/image266.png)
图 14-3 自动初始化树节点加载计算域
若计算域前面出现红色感叹号，如下，表明自动初始化失败，需要进行手动初始化。
![](media/image267.png)
图 14-4 自动初始化失败
手动初始化步骤如下：
在树节点中双击或右击编辑目标计算域；
在设置界面手动指定每个边界对应类型；
![](media/image268.png)
图 14-5 手动初始化

初始化成功后会显示对应的背景网格，如下图所示：
![](media/image269.png)
图 14-6 手动初始化成功

a.Component视口区显示数量；
b.Component旋转轴设置，包括三种方式：
c.从计算结果自动获取
d.用户自定义，包括X，Y，Z轴
e.用户自定义，两点确定坐标轴；
f. 旋转周期定义：
g.自动识别（From Results File）
h.用户自定义（Custom）。

#### 14.2 三维视图（3D View） <a name="142-三维视图3d-view"></a>  
用于模型可视化，可展示计算域边界，Blade to Blade对象位置，Turbo Charts位置，界面设置说明如下：
i.Components：选择需要展示的计算域，所有计算域或单个计算域。
j.Parts to Draw: 选择需要展示的边界，Blade to Blade，Turbo Charts对象。
k.Part显示方式：展示面信息（Show Faces）或网格信息（Show Mesh Line）。
l.显示对象颜色设置。
m.选择不同Component或者All components进行拷贝显示。
![](media/image270.png)
图 14-7 创建三维视图 

#### 14.3 叶间平面（Blade-to-Blade） <a name="143-叶间平面blade-to-blade"></a>  
用于显示不同叶高处转静子流面上物理量分布，可查看云图、矢量图、流线图。
基本设置选项：
a.计算域（Domains）：可选择查看单个计算域或当前所有计算域Blade-to-Blade平面；
b.叶高位置设置（Span）：提供手动输入或滑动条两种方式调节叶高位置；
c.结果查看形式：云图，矢量图和流线图三种形式；
d.结果查看详细设置参数：与云图，矢量图和流线图设置类似。
e.复制选项（Graphical Instancing): 可选择特定计算域进行复制显示。
![](media/image271.png)
图 14-8 创建叶间平面云图
![](media/image272.png)
图 14-9创建叶间平面矢量图
![](media/image273.png)
图 14-10 创建叶间平面流线图

#### 14.4 子午面（Meridional） <a name="144-子午面meridional"></a>  
子午面功能，用于展示流场沿周向平均的物理量信息。
基本设置选项：
a.计算域（Domains）：可选择查看任意计算域或当前所有计算域子午面信息；
b.流向样本数量（Stream Sample）：设置沿流向样本数量；
c.叶高样本数量（Span Sample）：设置叶高方向样本数量；结果查看形式：云图（Contour），矢量图（Vector）两种形式；结果查看详细设置参数：与云图，矢量图设置类似。
d.平均算法选择（Circ Average):提供面积平均（Area），质量平均（Mass）两种算法。
样本网格线展示（Show Sample Mesh)：勾选展示效果如图223所示。
![](media/image274.png)
图 14-11 创建子午面云图
![](media/image275.png)
图 14-12 创建子午面矢量图
![](media/image276.png)
图 14-13子午面云图展示（样本网格线）  

#### 14.5 自定义位置（Location） <a name="145-自定义位置location"></a>  
AICFD 提供了旋转机械模块专用的自定义位置菜单工具Turbo Surface和Turbo Line功能，用于显示叶轮机械特殊位置曲面及曲面流场信息。

##### 14.5.1 曲面位置信息展示（Turbo Surface） <a name="1451-曲面位置信息展示turbo-surface"></a>  
基本设置选项：
a.提供多种创建Turbo surface 的方式。
b.生成方式1：Constant Span（Hub到Shroud方向位置）；
c.生成方式2：Constant Streamwise Location（Inlet到Outlet方向位置）；
d.生成方式4：Constant Theta（Theta方向角位置）；
e.Bounds：确定平面旋转面生成范围；
f. None：表示当前结果模型所包含空间范围；
g.Rectangular（暂未开放）：用户自定义三角区，通过定义流向和Theta向最大最小值确定曲面生成区域。
![](media/image277.png)
图 14-14 创建Turbo Surface 

##### 14.5.2 曲线位置信息展示（Turbo Line） <a name="1452-曲线位置信息展示turbo-line"></a>  
Turbo Line提供三种创建曲线的方式如下：
###### 14.5.2.1 入口至出口（Inlet to Outlet） <a name="14521-入口至出口inlet-to-outlet"></a>  
基本设置选项：
a.Method：下拉选择Inlet to Outlet选项。
b.周向角度（Theta）区间：[theta1，theta2]
c.叶高位置（Span）区间：[0，1]
d.样本数量（Samples）：默认值为100，区间：[2，10000]；
e.Type：默认为None，表示覆盖Inlet到Outline完整区间；
f. Stream Min:曲线沿流向起始位置，区间为[0,1]*级数；
g.Stream Max:曲线沿流向结束位置，区间为[0,1]*级数；
h.平均算法选择（Circ Average):提供（None），面积平均（Area），质量平均（Mass）两种算法，None表示不采用平均算法，展示变量值为当点的实际数值。
![](media/image278.png)
图 14-15 创建Turbo Line-Inlet to Outlet 

###### 14.5.2.2 径向曲线（Hub to Shroud） <a name="14522-径向曲线hub-to-shroud"></a>  
a.Method：下拉选择Hub to Shroud选项。
b.Mode：默认Streamwise Location一个选项
c.Streamwise：流向区间：[0，1]*级数
d.Theta区间：[theta1，theta2]
e.Distribution：默认Equal Distance一个选项
f.Samples：默认值为100，区间：[2，10000]；
g.Circ Average：含None、Area、Mass三个选项。
![](media/image279.png)
图 14-16 创建Turbo Line-Line-Hub to Shroud  

###### 14.5.2.3 圆周方向（Circumferential） <a name="14523-圆周方向circumferential"></a>  
a.Method：下拉选择Circumferential选项。
b.Streamwise：流向区间：[0，1]*级数
c.Samples：默认值为100，区间：[2，10000]
d.Span：叶高位置，区间[0,1]；
e.Type：默认为None，表示覆盖theta1到theta2完整区间。
f. Theta Min：起始点Theta角
g.Theta Max：结束点Theta角；
h.Circ Average：含None、Area、Mass三个选项
i. Max Samples: 最大样本数量，默认20。
![](media/image280.png)
图 14-17 创建Turbo Line-Circumferential

#### 14.6 图表（Turbo Chart） <a name="146-图表turbo-chart"></a>  
AICFD提供4种叶轮机械快速图表创建功能，具体操作如下：
##### 14.6.1 叶片载荷（Blade Loading） <a name="1461-叶片载荷blade-loading"></a>  
用于展示不同叶高处叶片表面物理量分布。
a.Components：选择计算域；
b.Span区间：[0，1]；
c.X Axis Variable：X轴默认为Streamwise，流向归一化参数，区间为[0,1]；
d.Y Axis Variable：Y周展示物理量数值。
![](media/image281.png)
图 14-18 创建Blade Loading表 

##### 14.6.2 圆周面（Circumferential） <a name="1462-圆周面circumferential"></a>  
用于展示沿周向特定位置曲线上物理量分布。
a.Span区间：[0，1]；
b.Streamwise区间：[0，1]*级数；
c.Samples：默认值50，区间：[2，10000]；
d.X Axis Variable：唯一选项Theta；
e.Y Axis Variable：选择图表展示的信息变量。
![](media/image282.png)
图 14-19 创建Circumferential表

##### 14.6.3 径向曲线（Hub to Shroud ） <a name="1463-径向曲线hub-to-shroud-"></a>  
展示沿径向的特定位置曲线上物理量分布。
Mode：唯一选项-Streamwise Location，流向归一化参数；
Distribution：唯一选项-Equal Distance；
Samples：默认值50，区间： [2，10000]；
Streamwise区间：[0，1]*级数；
X Axis Variable：曲线变量列表；
Circ Average：平均方法，选项列表：Area、Mass；
Y Axis Variable：唯一选项-Span Normalized，叶高位置归一化，区间 [0,1]；
Circ Average：平均方法，选项列表：Area、Mass；
![](media/image283.png)
图 14-20 创建Hub to Shroud表
##### 14.6.4 入口至出口（Inlet to Outlet） <a name="1464-入口至出口inlet-to-outlet"></a>  
用于展示沿流向平均的物理量分布。
Components：选项包括All Domains， Domain1，Domain2…；
Samples/Comp：每个计算域样本数量，默认值50，区间： [2，10000]；
X Axis Variable： 唯一选项-Streamwise Location；
Y Axis Variable：曲线变量列表；
Circ Average： 平均方法，选项列表：Area、Mass。
![](media/image284.png)
图 14-21创建Inlet to Outlet表


