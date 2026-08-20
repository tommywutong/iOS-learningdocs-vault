# documentation 分类正文翻译计划（阶段二：标题已译 → 正文待译）

> 前置计划：`doc/TRANSLATION_PLAN.md`（iOS Cocoa 40 份）与 `doc/TRANSLATION_PLAN_WINDOWS_VIEWS.md`（Windows Views 8 份）已全部完成（344/344、51/51 页，已核实与实际文件一致）。本计划是它们的后续，范围、流程、约定基本沿用，只是目标文档集合不同。

## Context

PR #9（`索引层中文化：documentation 分类 11252 处标题`）把 `_indexes/` 下 `documentation` 分类的索引条目标题批量译成了中文，但**只改了索引文件里的链接显示文字，完全没有触碰实际文档文件**。这导致 vault 出现"目录看着是中文、点进去正文还是英文"的落差：全仓共 1765 处中文索引链接文字，其中 1618 处指向的文档，其自身 frontmatter `title` 及正文仍是纯英文。

按物理文档去重、排除同一文档下的多个子页面重复计数后，实际对应 **540 份独立文档**。本计划覆盖其中排除掉体量过大或非叙述性内容后的 **533 份、3988 页**，作为下一阶段翻译的执行清单。

## 范围口径

- 覆盖对象：`_indexes/` 下已译成中文标题、但对应实际文档 `documentation/**/*.md`（含 1 份 `samplecode/`）frontmatter `title` 仍是英文的文档。
- **不包含** `doc/TRANSLATION_PLAN.md` 与 `doc/TRANSLATION_PLAN_WINDOWS_VIEWS.md` 已覆盖的 Cocoa 40 份 + Windows Views 8 份（那些早已译完，且标题也已是中文，不在本次统计范围内）。
- **已排除 7 份体量过大或非叙述性的参考文档**（共 4815 页，超过原始候选总页数的一半），见文末「排除清单」。如需翻译需用户另行确认后再单独立项，不建议与其余正文一起批量推进。
- 表格里的"物理路径"：多页文档给的是文档目录（该目录下所有 `.md` 都属于同一份文档，含 `Document Revision History.md`）；单页文档（目录下无同名子目录、文件直接躺在分类根目录）给的是文件本体路径。

## 与前两份计划的差异

- **规模级差**：前两份计划合计 395 页，本计划 3988 页，约 10 倍体量，不适合再要求"一次性产出完整对照表"式的重度人工校对，建议按文档为单位分批推进，允许并行。

## 翻译流程（沿用前两份计划的约定）

**每份文档的处理流程**：
1. 定位该文档目录下的全部页面文件（入口页 + 子章节页 + `Document Revision History.md`）。
2. 逐页把正文英文替换为中文翻译，原地写回（不新建双语版本、不新建镜像目录）。
3. frontmatter 只翻译 `title` 字段，其余字段（`apple_id`、`resource_type`、`platform`、`topic`、`technology`、`source_url`、`archived_at` 等）一字不改。
4. API / 类 / 方法 / 常量 / 框架名保留英文；`[Next]`/`[Previous]` → `[下一页]`/`[上一页]`；面包屑 `[documentation]` → `[文档]`；`__Figure N__`/`__Table N__`/`__Listing N__` → `__图 N__`/`__表 N__`/`__清单 N__`（正文里的引用如"see Figure 2-3"也要同步译成"见 图 2-3"）。
5. 代码块本身（代码、GDB 会话、命令输出等）内容零改动，只译代码注释；代码块内 NBSP（U+00A0）缩进不能被替换成普通空格；代码块数量、行数、文件末尾换行数需保持一致。
6. 链接路径与 `#apple-...` 锚点一字不动。
7. 翻译完成后，把本计划对应文档那一行的「状态」从「未开始」改成「已译」，作为一次 git 提交提交到 `main`（提交信息注明文档标题，方便按提交追溯）。

**质量把关**（沿用前几批 PR 的三道关）：翻译 → 机械校验（链接/锚点零变化、frontmatter 非 title 字段零改动、代码块行数与数量守恒、NBSP 守恒、翻页链接与面包屑无残留英文）→ 人工/独立校对（对照英文原文逐段复核，重点检查术语一致性）。

## 执行建议

- **按分类分批**：下表已按 `topic` 分组并按页数从大到小排列，可以一次认领一个分类下的若干份文档作为一批 PR，与之前 Cocoa/Windows Views 的批次节奏一致（每批 40~60 页左右为宜）。
- **优先级建议**：数据管理、用户体验、Xcode、通用、网络与互联网 这几类是日常开发高频查阅的内容，建议优先；「未分类」里体量普遍较小（多数 <10 页），适合作为补空档的零散批次。
- **同名文档提醒**：部分英文标题相近但不是同一份文档（如 "Aperture SDK Overview" 与 "Aperture 2.1 SDK Overview"、"Pasteboard Programming Topics for Cocoa" 与 "Pasteboard Programming Guide"），翻译时注意区分，不要合并处理。
- **特殊情况**：`samplecode/Calculator`（表中 #21）经抽查代码文件里已有相当比例的中文注释翻译，只是 frontmatter `title` 和导航栏未同步，怀疑是早期一次未被计划记录在案的翻译。建议先核实实际完成度，而不是当作全新文档从头译。

## 排除清单（默认不纳入本计划，如需翻译请另行确认）

| 英文标题 | 页数 | 排除理由 |
| --- | --- | --- |
| WebObjects 4.5 Developer Documentation | 1473 | 体量过大且技术已停止维护多年（WebObjects/旧版 GCC），投入产出比低 |
| WebObjects 4.0 Developer Documentation | 1104 | 体量过大且技术已停止维护多年（WebObjects/旧版 GCC），投入产出比低 |
| WebObjects 5.0 Developer Documentation | 1053 | 体量过大且技术已停止维护多年（WebObjects/旧版 GCC），投入产出比低 |
| Miscellaneous User Space API Reference | 470 | 自动生成的 API 差异/清单类参考文档，非叙述性正文，翻译价值低 |
| GNU Compiler Collection (GCC) 4.2 Internals | 265 | 体量过大且技术已停止维护多年（WebObjects/旧版 GCC），投入产出比低 |
| GNU Compiler Collection (GCC) Internals | 242 | 体量过大且技术已停止维护多年（WebObjects/旧版 GCC），投入产出比低 |
| OS X v10.10 API Diffs | 208 | 自动生成的 API 差异/清单类参考文档，非叙述性正文，翻译价值低 |
## 完整清单（533 份 / 3988 页，按分类分组，页数从大到小排列）


### 未分类（159 份文档，862 页）

| # | 中文标题（索引已译） | 英文标题（正文待译） | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 1 | Cocoa Bindings 参考 | Cocoa Bindings Reference | 61 | `documentation/Cocoa/Cocoa Bindings Reference` | 未开始 |
| 2 | Xcode 2.0 用户指南 | Xcode 2.0 User Guide | 52 | `documentation/Developer Tools/Xcode 2.0 User Guide` | 未开始 |
| 3 | 使用 Appearance Manager 编程 | Programming with the Appearance Manager | 33 | `documentation/Carbon/Programming with the Appearance Manager` | 未开始 |
| 4 | WebObjects Java Client 编程指南 | WebObjects Java Client Programming Guide | 28 | `documentation/Web Objects/WebObjects Java Client Programming Guide` | 未开始 |
| 5 | 开发 SMIL 演示文稿 | Developing SMIL Presentations | 27 | `documentation/Web Objects/Developing SMIL Presentations` | 未开始 |
| 6 | Safari HTML5 Canvas 指南 | Safari HTML5 Canvas Guide | 18 | `documentation/Audio Video/Safari HTML5 Canvas Guide` | 未开始 |
| 7 | AppleScript Studio 编程指南 | AppleScript Studio Programming Guide | 16 | `documentation/Apple Script/AppleScript Studio Programming Guide` | 未开始 |
| 8 | 软件交付旧版指南 | Software Delivery Legacy Guide | 14 | `documentation/Developer Tools/Software Delivery Legacy Guide` | 未开始 |
| 9 | Apple Events 编程指南 | Apple Events Programming Guide | 13 | `documentation/Apple Script/Apple Events Programming Guide` | 未开始 |
| 10 | Carbon-Cocoa 集成指南 | Carbon-Cocoa Integration Guide | 13 | `documentation/Cocoa/Carbon-Cocoa Integration Guide` | 未开始 |
| 11 | Cocoa 事件处理指南 | Cocoa Event Handling Guide | 13 | `documentation/Cocoa/Cocoa Event Handling Guide` | 未开始 |
| 12 | 面向 QuickDraw 开发者的 Quartz 编程指南 | Quartz Programming Guide for QuickDraw Developers | 13 | `documentation/Carbon/Quartz Programming Guide for QuickDraw Developers` | 未开始 |
| 13 | 使用 JavaMonitor 的 WebObjects 部署指南 | WebObjects Deployment Guide Using JavaMonitor | 12 | `documentation/Web Objects/WebObjects Deployment Guide Using JavaMonitor` | 未开始 |
| 14 | ATSUI 编程指南 | ATSUI Programming Guide | 11 | `documentation/Carbon/ATSUI Programming Guide` | 未开始 |
| 15 | 扩展打印对话框 | Extending Printing Dialogs | 11 | `documentation/Printing/Extending Printing Dialogs` | 未开始 |
| 16 | Sherlock 频道 | Sherlock Channels | 11 | `documentation/Apple Applications/Sherlock Channels` | 未开始 |
| 17 | 通用二进制编程规范（第二版） | Universal Binary Programming Guidelines, Second Edition | 11 | `documentation/Mac OSX/Universal Binary Programming Guidelines, Second Edition` | 未开始 |
| 18 | WebKit DOM 编程主题 | WebKit DOM Programming Topics | 11 | `documentation/Apple Applications/WebKit DOM Programming Topics` | 未开始 |
| 19 | 在 Mac OS 9 中使用 ColorSync 管理颜色 | Managing Colors With ColorSync in Mac OS 9 | 10 | `documentation/Graphics Imaging/Managing Colors With ColorSync in Mac OS 9` | 未开始 |
| 20 | Mac OS X v10.4 版 NSPersistentDocument Core Data 教程 | NSPersistentDocument Core Data Tutorial for Mac OS X v10.4. | 10 | `documentation/Cocoa/NSPersistentDocument Core Data Tutorial for Mac OS X v10.4` | 未开始 |
| 21 | 计算器 | Calculator | 9 | `samplecode/Calculator` | 疑似已译¹ |
| 22 | Carbon 移植指南 | Carbon Porting Guide | 9 | `documentation/Carbon/Carbon Porting Guide` | 未开始 |
| 23 | 网络服务定位管理器（旧版） | Network Services Location Manager (Legacy) | 9 | `documentation/Networking/Network Services Location Manager (Legacy)` | 未开始 |
| 24 | 使用 Apple Help 提供用户帮助 | Providing User Assistance With Apple Help | 9 | `documentation/User Experience/Providing User Assistance With Apple Help` | 未开始 |
| 25 | AVFoundation 编程指南 | AVFoundation Programming Guide | 8 | `documentation/Audio Video/AVFoundation Programming Guide` | 未开始 |
| 26 | 多处理服务编程指南 | Multiprocessing Services Programming Guide | 8 | `documentation/Carbon/Multiprocessing Services Programming Guide` | 未开始 |
| 27 | 面向对象编程与 Objective-C 编程语言 1.0 | Object Oriented Programming and the Objective-C Programming Language 1.0 | 8 | `documentation/Cocoa/Object Oriented Programming and the Objective-C Programming Language 1.0` | 未开始 |
| 28 | 将 CodeWarrior 项目移植到 Xcode | Porting CodeWarrior Projects to Xcode | 8 | `documentation/Developer Tools/Porting CodeWarrior Projects to Xcode` | 未开始 |
| 29 | 文本输入管理 | Text Input Management | 8 | `documentation/Cocoa/Text Input Management` | 未开始 |
| 30 | WebObjects Web 应用程序编程指南 | WebObjects Web Applications Programming Guide | 8 | `documentation/Web Objects/WebObjects Web Applications Programming Guide` | 未开始 |
| 31 | Carbon Event Manager 编程指南 | Carbon Event Manager Programming Guide | 7 | `documentation/Carbon/Carbon Event Manager Programming Guide` | 未开始 |
| 32 | 发布订阅编程指南 | Publication Subscription Programming Guide | 7 | `documentation/Internet Web/Publication Subscription Programming Guide` | 未开始 |
| 33 | 运行循环 | Run Loops | 7 | `documentation/Cocoa/Run Loops` | 未开始 |
| 34 | Safari HTML5 音频和视频指南 | Safari HTML5 Audio and Video Guide | 7 | `documentation/Audio Video/Safari HTML5 Audio and Video Guide` | 未开始 |
| 35 | iAd Creative Management 手册 | iAd Creative Management Manual | 7 | `documentation/Miscellaneous/iAd Creative Management Manual` | 未开始 |
| 36 | 管理字体：QuickDraw | 'Managing Fonts: QuickDraw' | 6 | `documentation/Carbon/Managing Fonts- QuickDraw` | 未开始 |
| 37 | Carbon 辅助功能编程指南 | Accessibility Programming Guidelines for Carbon | 6 | `documentation/Carbon/Accessibility Programming Guidelines for Carbon` | 未开始 |
| 38 | DNSServiceDiscovery 基于 Mach 的 API | DNSServiceDiscovery Mach-Based API | 6 | `documentation/Networking/DNSServiceDiscovery Mach-Based API` | 未开始 |
| 39 | 处理 Carbon 窗口和控件 | Handling Carbon Windows and Controls | 6 | `documentation/Carbon/Handling Carbon Windows and Controls` | 未开始 |
| 40 | 运行循环 | Run Loops | 6 | `documentation/Core Foundation/Run Loops` | 未开始 |
| 41 | 在 Carbon 应用程序中支持打印 | Supporting Printing in Your Carbon Application | 6 | `documentation/Carbon/Supporting Printing in Your Carbon Application` | 未开始 |
| 42 | WebObjects 概述 | WebObjects Overview | 6 | `documentation/Web Objects/WebObjects Overview` | 未开始 |
| 43 | AltiVec/SSE 迁移指南 | AltiVec/SSE Migration Guide | 5 | `documentation/Performance/AltiVec-SSE Migration Guide` | 未开始 |
| 44 | Carbon 概述 | Carbon Overview | 5 | `documentation/Carbon/Carbon Overview` | 未开始 |
| 45 | Cocoa-Java 集成指南 | Cocoa-Java Integration Guide | 5 | `documentation/Cocoa/Cocoa-Java Integration Guide` | 未开始 |
| 46 | 使用 MLTE 处理 Unicode 文本编辑 | Handling Unicode Text Editing With MLTE | 5 | `documentation/Carbon/Handling Unicode Text Editing With MLTE` | 未开始 |
| 47 | 网络内核扩展（旧版） | Network Kernel Extensions (legacy) | 5 | `documentation/Darwin/Network Kernel Extensions (legacy)` | 未开始 |
| 48 | 空中配置文件传送与配置 | Over-the-Air Profile Delivery and Configuration | 5 | `documentation/Networking Internet/Over-the-Air Profile Delivery and Configuration` | 未开始 |
| 49 | Safari 图像传送最佳实践 | Safari Image Delivery Best Practices | 5 | `documentation/Networking Internet/Safari Image Delivery Best Practices` | 未开始 |
| 50 | 设置 Carbon 应用程序以使用服务菜单 | Setting Up Your Carbon Application to Use the Services Menu | 5 | `documentation/Carbon/Setting Up Your Carbon Application to Use the Services Menu` | 未开始 |
| 51 | 升级到 Mac OS X HIToolbox | Upgrading to the Mac OS X HIToolbox | 5 | `documentation/Carbon/Upgrading to the Mac OS X HIToolbox` | 未开始 |
| 52 | WebObjects 应用程序属性参考 | WebObjects Application Properties Reference | 5 | `documentation/Web Objects/WebObjects Application Properties Reference` | 未开始 |
| 53 | WebObjects Direct to Web 指南 | WebObjects Direct to Web Guide | 5 | `documentation/Web Objects/WebObjects Direct to Web Guide` | 未开始 |
| 54 | WebObjects 教程 | WebObjects Tutorial | 5 | `documentation/Developer Tools/WebObjects Tutorial` | 未开始 |
| 55 | AirPort 开发者说明 | AirPort Developer Note | 4 | `documentation/Hardware Drivers/AirPort Developer Note` | 未开始 |
| 56 | Apple Type Services for Fonts 编程指南 | Apple Type Services for Fonts Programming Guide | 4 | `documentation/Carbon/Apple Type Services for Fonts Programming Guide` | 未开始 |
| 57 | 音频开发者说明 | Audio Developer Note | 4 | `documentation/Hardware/Audio Developer Note` | 未开始 |
| 58 | 蓝牙开发者说明 | Bluetooth Developer Note | 4 | `documentation/Hardware Drivers/Bluetooth Developer Note` | 未开始 |
| 59 | 创建 Carbon 菜单 | Creating Carbon Menus | 4 | `documentation/Carbon/Creating Carbon Menus` | 未开始 |
| 60 | 以太网开发者说明 | Ethernet Developer Note | 4 | `documentation/Hardware Drivers/Ethernet Developer Note` | 未开始 |
| 61 | FireWire 开发者说明 | FireWire Developer Note | 4 | `documentation/Hardware Drivers/FireWire Developer Note` | 未开始 |
| 62 | HIArchive 编程指南 | HIArchive Programming Guide | 4 | `documentation/Carbon/HIArchive Programming Guide` | 未开始 |
| 63 | HIView 编程指南 | HIView Programming Guide | 4 | `documentation/Carbon/HIView Programming Guide` | 未开始 |
| 64 | Navigation Services 编程指南 | Navigation Services Programming Guide | 4 | `documentation/Carbon/Navigation Services Programming Guide` | 未开始 |
| 65 | 使用 Icon Services 获取和使用图标 | Obtaining and Using Icons With Icon Services | 4 | `documentation/Carbon/Obtaining and Using Icons With Icon Services` | 未开始 |
| 66 | iOS 版 OpenGL ES 硬件平台指南 | OpenGL ES Hardware Platform Guide for iOS | 4 | `documentation/OpenGL ES Hardware Platform Guide for iOS` | 未开始 |
| 67 | 使用 Display Manager 优化显示模式和窗口排列 | Optimizing Display Modes and Window Arrangement With the Display Manager | 4 | `documentation/Carbon/Optimizing Display Modes and Window Arrangement With the Display Manager` | 未开始 |
| 68 | PCI 开发者说明 | PCI Developer Note | 4 | `documentation/Hardware/PCI Developer Note` | 未开始 |
| 69 | 在 Mac OS 9 中使用 Navigation Services 编程 | Programming With Navigation Services in Mac OS 9 | 4 | `documentation/Carbon/Programming With Navigation Services in Mac OS 9` | 未开始 |
| 70 | 在 Carbon 中提供帮助标签 | Providing Help Tags in Carbon | 4 | `documentation/Carbon/Providing Help Tags in Carbon` | 未开始 |
| 71 | QuickTime 7 更新指南 | QuickTime 7 Update Guide | 4 | `documentation/Quick Time/QuickTime 7 Update Guide` | 未开始 |
| 72 | 面向 Windows 的 QuickTime 7 更新指南 | QuickTime 7 for Windows Update Guide | 4 | `documentation/Quick Time/QuickTime 7 for Windows Update Guide` | 未开始 |
| 73 | RAM 扩展开发者说明 | RAM Expansion Developer Note | 4 | `documentation/Hardware Drivers/RAM Expansion Developer Note` | 未开始 |
| 74 | 支持 Unicode 输入 | Supporting Unicode Input | 4 | `documentation/Carbon/Supporting Unicode Input` | 未开始 |
| 75 | 使用 Interface Builder Services 取消归档界面对象 | Unarchiving Interface Objects With Interface Builder Services | 4 | `documentation/Carbon/Unarchiving Interface Objects With Interface Builder Services` | 未开始 |
| 76 | 通用串行总线开发者说明 | Universal Serial Bus Developer Note | 4 | `documentation/Hardware Drivers/Universal Serial Bus Developer Note` | 未开始 |
| 77 | 视频开发者说明 | Video Developer Note | 4 | `documentation/Hardware/Video Developer Note` | 未开始 |
| 78 | 15 英寸 MacBook Pro 开发者说明 | 15-Inch MacBook Pro Developer Note | 3 | `documentation/Hardware Drivers/15-Inch MacBook Pro Developer Note (2007)-2` | 未开始 |
| 79 | 15 英寸 MacBook Pro 开发者说明 | 15-Inch MacBook Pro Developer Note | 3 | `documentation/Hardware Drivers/15-Inch MacBook Pro Developer Note (2008)` | 未开始 |
| 80 | 15 英寸 MacBook Pro 开发者说明 | 15-inch MacBook Pro Developer Note | 3 | `documentation/Hardware Drivers/15-inch MacBook Pro Developer Note` | 未开始 |
| 81 | 15 英寸 MacBook Pro 开发者说明 | 15-inch MacBook Pro Developer Note | 3 | `documentation/Hardware Drivers/15-inch MacBook Pro Developer Note (2007)` | 未开始 |
| 82 | 15 英寸 MacBook Pro 开发者说明 | 15-inch MacBook Pro Developer Note | 3 | `documentation/Hardware Drivers/15-inch MacBook Pro Developer Note (2007)-3` | 未开始 |
| 83 | 17 英寸 MacBook Pro 开发者说明 | 17-Inch MacBook Pro Developer Note | 3 | `documentation/Hardware Drivers/17-Inch MacBook Pro Developer Note (2008)` | 未开始 |
| 84 | 17 英寸 MacBook Pro 开发者说明 | 17-inch MacBook Pro Developer Note | 3 | `documentation/Hardware Drivers/17-inch MacBook Pro Developer Note` | 未开始 |
| 85 | 17 英寸 MacBook Pro 开发者说明 | 17-inch MacBook Pro Developer Note | 3 | `documentation/Hardware Drivers/17-inch MacBook Pro Developer Note (2007)` | 未开始 |
| 86 | 17 英寸 MacBook Pro 开发者说明 | 17-inch MacBook Pro Developer Note | 3 | `documentation/Hardware Drivers/17-inch MacBook Pro Developer Note (2007)-2` | 未开始 |
| 87 | 17 英寸 MacBook Pro 开发者说明 | 17-inch MacBook Pro Developer Note | 3 | `documentation/Hardware Drivers/17-inch MacBook Pro Developer Note (2007)-3` | 未开始 |
| 88 | 面向教育行业的 17 英寸 iMac 开发者说明 | 17-inch iMac for Education Developer Note | 3 | `documentation/Hardware Drivers/17-inch iMac for Education Developer Note` | 未开始 |
| 89 | QuickTime 的 Component Manager | Component Manager for QuickTime | 3 | `documentation/Quick Time/Component Manager for QuickTime` | 未开始 |
| 90 | HIToolbar 编程指南 | HIToolbar Programming Guide | 3 | `documentation/Carbon/HIToolbar Programming Guide` | 未开始 |
| 91 | 硬件开发者说明术语与缩写 | Hardware Developer Note Terms and Abbreviations | 3 | `documentation/Hardware Drivers/Hardware Developer Note Terms and Abbreviations` | 未开始 |
| 92 | Mac Pro 开发者说明 | Mac Pro Developer Note | 3 | `documentation/Hardware Drivers/Mac Pro Developer Note` | 未开始 |
| 93 | Mac Pro 开发者说明 | Mac Pro Developer Note | 3 | `documentation/Hardware Drivers/Mac Pro Developer Note (2007)` | 未开始 |
| 94 | Mac Pro 开发者说明 | Mac Pro Developer Note | 3 | `documentation/Hardware Drivers/Mac Pro Developer Note (2008)` | 未开始 |
| 95 | Mac mini 开发者说明 | Mac mini Developer Note | 3 | `documentation/Hardware Drivers/Mac mini Developer Note` | 未开始 |
| 96 | MacBook Air 开发者说明 | MacBook Air Developer Note | 3 | `documentation/Hardware Drivers/MacBook Air Developer Note` | 未开始 |
| 97 | MacBook 开发者说明 | MacBook Developer Note | 3 | `documentation/Hardware Drivers/MacBook Developer Note` | 未开始 |
| 98 | MacBook 开发者说明 | MacBook Developer Note | 3 | `documentation/Hardware Drivers/MacBook Developer Note (2007)` | 未开始 |
| 99 | MacBook 开发者说明 | MacBook Developer Note | 3 | `documentation/Hardware Drivers/MacBook Developer Note (2007)-2` | 未开始 |
| 100 | MacBook 开发者说明 | MacBook Developer Note | 3 | `documentation/Hardware Drivers/MacBook Developer Note (2007)-3` | 未开始 |
| 101 | MacBook 开发者说明 | MacBook Developer Note | 3 | `documentation/Hardware Drivers/MacBook Developer Note (2008)` | 未开始 |
| 102 | Power Mac G5 开发者说明 | Power Mac G5 Developer Note | 3 | `documentation/Hardware/Power Mac G5 Developer Note` | 未开始 |
| 103 | 使用 Language Analysis Manager 编程 | Programming With the Language Analysis Manager | 3 | `documentation/Carbon/Programming With the Language Analysis Manager` | 未开始 |
| 104 | QuickTime 7.2.1 更新指南 | QuickTime 7.2.1 Update Guide | 3 | `documentation/Quick Time/QuickTime 7.2.1 Update Guide` | 未开始 |
| 105 | QuickTime 初始化指南 | QuickTime Initialization Guide | 3 | `documentation/Quick Time/QuickTime Initialization Guide` | 未开始 |
| 106 | 面向 QuickTime 的 SMIL 脚本编写指南 | SMIL Scripting Guide for QuickTime | 3 | `documentation/Quick Time/SMIL Scripting Guide for QuickTime` | 未开始 |
| 107 | 理解 Carbon 中的文本输入和 Text Services Manager | Understanding Text Input and the Text Services Manager in Carbon | 3 | `documentation/Carbon/Understanding Text Input and the Text Services Manager in Carbon` | 未开始 |
| 108 | Xserve 开发者说明 | Xserve Developer Note | 3 | `documentation/Hardware Drivers/Xserve Developer Note` | 未开始 |
| 109 | Xserve 开发者说明 | Xserve Developer Note | 3 | `documentation/Hardware Drivers/Xserve Developer Note (2008)` | 未开始 |
| 110 | iMac 开发者说明 | iMac Developer Note | 3 | `documentation/Hardware Drivers/iMac Developer Note` | 未开始 |
| 111 | iMac 开发者说明 | iMac Developer Note | 3 | `documentation/Hardware Drivers/iMac Developer Note (2006)` | 未开始 |
| 112 | iMac 开发者说明 | iMac Developer Note | 3 | `documentation/Hardware Drivers/iMac Developer Note (2007)` | 未开始 |
| 113 | iMac 开发者说明 | iMac Developer Note | 3 | `documentation/Hardware Drivers/iMac Developer Note (2007)-2` | 未开始 |
| 114 | iMac 开发者说明 | iMac Developer Note | 3 | `documentation/Hardware Drivers/iMac Developer Note (2007)-3` | 未开始 |
| 115 | iMac G5 开发者说明 | iMac G5 Developer Note | 3 | `documentation/Hardware/iMac G5 Developer Note` | 未开始 |
| 116 | Carbon 版 Navigation Services 概述 | 'Navigation Services for Carbon: An Overview' | 2 | `documentation/Carbon/Navigation Services for Carbon- An Overview` | 未开始 |
| 117 | QuickTime 7.1 更新指南 | QuickTime 7.1 Update Guide | 2 | `documentation/Quick Time/QuickTime 7.1 Update Guide` | 未开始 |
| 118 | 使用 URL Access Manager 传输数据 | Transferring Data With URL Access Manager | 2 | `documentation/Carbon/Transferring Data With URL Access Manager` | 未开始 |
| 119 | 12 英寸 PowerBook G4 开发者说明 | 12-inch PowerBook G4 Developer Note | 1 | `documentation/Hardware/12-inch PowerBook G4 Developer Note.md` | 未开始 |
| 120 | 15 英寸 PowerBook G4 开发者说明 | 15-inch PowerBook G4 Developer Note | 1 | `documentation/Hardware/15-inch PowerBook G4 Developer Note.md` | 未开始 |
| 121 | 17 英寸 PowerBook G4 开发者说明 | 17-inch PowerBook G4 Developer Note | 1 | `documentation/Hardware/17-inch PowerBook G4 Developer Note.md` | 未开始 |
| 122 | Mac OS X 安装指南 | Installation Guide for Mac OS X | 1 | `documentation/Web Objects/Installation Guide for Mac OS X.md` | 未开始 |
| 123 | Windows 和 Solaris 安装指南 | Installation Guide for Windows and Solaris | 1 | `documentation/Web Objects/Installation Guide for Windows and Solaris.md` | 未开始 |
| 124 | 交互式影片 | Interactive Movies | 1 | `documentation/Quick Time/Interactive Movies.md` | 未开始 |
| 125 | Mac mini 开发者说明 | Mac mini Developer Note | 1 | `documentation/Hardware/Mac mini Developer Note.md` | 未开始 |
| 126 | Power Mac G5——单处理器开发者说明 | Power Mac G5 -- Single Processor Developer Note | 1 | `documentation/Hardware/Power Mac G5 -- Single Processor Developer Note.md` | 未开始 |
| 127 | Power Mac G5 开发者说明 | Power Mac G5 Developer Note | 1 | `documentation/Hardware/Power Mac G5 Developer Note (2005).md` | 未开始 |
| 128 | 面向 WebObjects 开发者的 Project Builder | Project Builder for WebObjects Developers | 1 | `documentation/Web Objects/Project Builder for WebObjects Developers.md` | 未开始 |
| 129 | QuickTime 组件创建指南 | QuickTime Component Creation Guide | 1 | `documentation/Quick Time/QuickTime Component Creation Guide.md` | 未开始 |
| 130 | QuickTime 压缩与解压缩指南 | QuickTime Compression and Decompression Guide | 1 | `documentation/Quick Time/QuickTime Compression and Decompression Guide.md` | 未开始 |
| 131 | QuickTime 导入与导出指南 | QuickTime Import and Export Guide | 1 | `documentation/Quick Time/QuickTime Import and Export Guide.md` | 未开始 |
| 132 | QuickTime 媒体类型与媒体处理程序指南 | QuickTime Media Types and Media Handlers Guide | 1 | `documentation/Quick Time/QuickTime Media Types and Media Handlers Guide.md` | 未开始 |
| 133 | QuickTime 影片基础 | QuickTime Movie Basics | 1 | `documentation/Quick Time/QuickTime Movie Basics.md` | 未开始 |
| 134 | QuickTime 影片创建指南 | QuickTime Movie Creation Guide | 1 | `documentation/Quick Time/QuickTime Movie Creation Guide.md` | 未开始 |
| 135 | QuickTime 影片内部原理指南 | QuickTime Movie Internals Guide | 1 | `documentation/Quick Time/QuickTime Movie Internals Guide.md` | 未开始 |
| 136 | QuickTime 影片播放编程指南 | QuickTime Movie Playback Programming Guide | 1 | `documentation/Quick Time/QuickTime Movie Playback Programming Guide.md` | 未开始 |
| 137 | QuickTime 音乐架构指南 | QuickTime Music Architecture Guide | 1 | `documentation/Quick Time/QuickTime Music Architecture Guide.md` | 未开始 |
| 138 | QuickTime 概述 | QuickTime Overview | 1 | `documentation/Quick Time/QuickTime Overview.md` | 未开始 |
| 139 | QuickTime 流媒体指南 | QuickTime Streaming Guide | 1 | `documentation/Quick Time/QuickTime Streaming Guide.md` | 未开始 |
| 140 | QuickTime 流媒体服务器模块编程指南 | QuickTime Streaming Server Modules Programming Guide | 1 | `documentation/Quick Time/QuickTime Streaming Server Modules Programming Guide.md` | 未开始 |
| 141 | QuickTime 传输与传送指南 | QuickTime Transport and Delivery Guide | 1 | `documentation/Quick Time/QuickTime Transport and Delivery Guide.md` | 未开始 |
| 142 | QuickTime 矢量图形 | QuickTime Vector Graphics | 1 | `documentation/Quick Time/QuickTime Vector Graphics.md` | 未开始 |
| 143 | QuickTime 视频效果与转场指南 | QuickTime Video Effects and Transitions Guide | 1 | `documentation/Quick Time/QuickTime Video Effects and Transitions Guide.md` | 未开始 |
| 144 | 标准声音对话框组件 | Standard Sound Dialog Component | 1 | `documentation/Quick Time/Standard Sound Dialog Component.md` | 未开始 |
| 145 | WebObjects 5.2 发行说明 | WebObjects 5.2 Release Notes | 1 | `documentation/Web Objects/WebObjects 5.2 Release Notes.md` | 未开始 |
| 146 | WebObjects 企业对象编程指南 | WebObjects Enterprise Objects Programming Guide | 1 | `documentation/Web Objects/WebObjects Enterprise Objects Programming Guide.md` | 未开始 |
| 147 | WebObjects J2EE 编程指南 | WebObjects J2EE Programming Guide | 1 | `documentation/Web Objects/WebObjects J2EE Programming Guide.md` | 未开始 |
| 148 | WebObjects Web 服务编程指南 | WebObjects Web Services Programming Guide | 1 | `documentation/Web Objects/WebObjects Web Services Programming Guide.md` | 未开始 |
| 149 | WebObjects XML 序列化指南 | WebObjects XML Serialization Guide | 1 | `documentation/Web Objects/WebObjects XML Serialization Guide.md` | 未开始 |
| 150 | 面向 Windows 开发者的 WebObjects | WebObjects for Windows Developers | 1 | `documentation/Web Objects/WebObjects for Windows Developers.md` | 未开始 |
| 151 | Mac OS X 版 QuickTime 6.4 的新增内容 | What's New in QuickTime 6.4 For Mac OS X | 1 | `documentation/Quick Time/What's New in QuickTime 6.4 For Mac OS X.md` | 未开始 |
| 152 | QuickTime 6.5 的新增内容 | What's New in QuickTime 6.5 | 1 | `documentation/Quick Time/What's New in QuickTime 6.5.md` | 未开始 |
| 153 | WebObjects 5.2 的新增内容 | What's New in WebObjects 5.2 | 1 | `documentation/Web Objects/What's New in WebObjects 5.2.md` | 未开始 |
| 154 | WebObjects 5.2.2 的新增内容 | What's New in WebObjects 5.2.2 | 1 | `documentation/Web Objects/What's New in WebObjects 5.2.2.md` | 未开始 |
| 155 | Xserve G5 开发者说明 | Xserve G5 Developer Note | 1 | `documentation/Hardware/Xserve G5 Developer Note.md` | 未开始 |
| 156 | eMac 开发者说明 | eMac Developer Note | 1 | `documentation/Hardware/eMac Developer Note.md` | 未开始 |
| 157 | iBook 开发者说明 | iBook Developer Note | 1 | `documentation/Hardware/iBook Developer Note.md` | 未开始 |
| 158 | iMac G5 开发者说明 | iMac G5 Developer Note | 1 | `documentation/Hardware/iMac G5 Developer Note (2005).md` | 未开始 |
| 159 | iSight 编程指南 | iSight Programming Guide | 1 | `documentation/Hardware/iSight Programming Guide.md` | 未开始 |

### 数据管理（65 份文档，543 页）

| # | 中文标题（索引已译） | 英文标题（正文待译） | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 160 | CloudKit Web 服务参考 | CloudKit Web Services Reference | 32 | `documentation/Data Management/CloudKit Web Services Reference` | 未开始 |
| 161 | Apple Filing Protocol 编程指南 | Apple Filing Protocol Programming Guide | 17 | `documentation/Networking/Apple Filing Protocol Programming Guide` | 未开始 |
| 162 | 字体处理 | Font Handling | 16 | `documentation/Cocoa/Font Handling` | 未开始 |
| 163 | Sync Services 编程指南 | Sync Services Programming Guide | 16 | `documentation/Cocoa/Sync Services Programming Guide` | 未开始 |
| 164 | 基于树的 XML 编程指南 | Tree-Based XML Programming Guide | 16 | `documentation/Cocoa/Tree-Based XML Programming Guide` | 未开始 |
| 165 | 文件系统概述 | File System Overview | 15 | `documentation/Mac OSX/File System Overview` | 未开始 |
| 166 | Core Foundation 字符串编程指南 | String Programming Guide for Core Foundation | 14 | `documentation/Core Foundation/String Programming Guide for Core Foundation` | 未开始 |
| 167 | 文件系统编程指南 | File System Programming Guide | 13 | `documentation/File Management/File System Programming Guide` | 未开始 |
| 168 | 按需资源指南 | On-Demand Resources Guide | 13 | `documentation/File Management/On-Demand Resources Guide` | 未开始 |
| 169 | 文本编辑编程指南 | Text Editing Programming Guide | 13 | `documentation/Cocoa/Text Editing Programming Guide` | 未开始 |
| 170 | Mac 通讯录编程指南 | Address Book Programming Guide for Mac | 12 | `documentation/User Experience/Address Book Programming Guide for Mac` | 未开始 |
| 171 | 应用程序文件管理 | Application File Management | 12 | `documentation/Cocoa/Application File Management` | 未开始 |
| 172 | 插件编程主题 | Plug-in Programming Topics | 12 | `documentation/Core Foundation/Plug-in Programming Topics` | 未开始 |
| 173 | 快速查看编程指南 | Quick Look Programming Guide | 12 | `documentation/User Experience/Quick Look Programming Guide` | 未开始 |
| 174 | 标尺与段落样式编程主题 | Ruler and Paragraph Style Programming Topics | 12 | `documentation/Cocoa/Ruler and Paragraph Style Programming Topics` | 未开始 |
| 175 | Core Foundation 集合编程主题 | Collections Programming Topics for Core Foundation | 11 | `documentation/Core Foundation/Collections Programming Topics for Core Foundation` | 未开始 |
| 176 | Settings 应用程序模式参考 | Settings Application Schema Reference | 11 | `documentation/Settings Application Schema Reference` | 未开始 |
| 177 | iSync 手动测试套件指南 | iSync Manual Test Suite Guide | 11 | `documentation/Apple Applications/iSync Manual Test Suite Guide` | 未开始 |
| 178 | iOS 文本编程指南 | Text Programming Guide for iOS | 10 | `documentation/Strings Text Fonts/Text Programming Guide for iOS` | 未开始 |
| 179 | Cocoa 文本架构指南 | Cocoa Text Architecture Guide | 9 | `documentation/Cocoa Text Architecture Guide` | 未开始 |
| 180 | 文件系统性能指南 | File-System Performance Guidelines | 9 | `documentation/Performance/File-System Performance Guidelines` | 未开始 |
| 181 | Syncrospector 用户指南 | Syncrospector User Guide | 9 | `documentation/Syncing/Syncrospector User Guide` | 未开始 |
| 182 | 文本属性编程主题 | Text Attribute Programming Topics | 9 | `documentation/Cocoa/Text Attribute Programming Topics` | 未开始 |
| 183 | Workspace Services 编程主题 | Workspace Services Programming Topics | 9 | `documentation/Cocoa/Workspace Services Programming Topics` | 未开始 |
| 184 | Calendar Store 编程指南 | Calendar Store Programming Guide | 8 | `documentation/Apple Applications/Calendar Store Programming Guide` | 未开始 |
| 185 | Mac 版基于文档的应用程序编程指南 | Document-Based App Programming Guide for Mac | 8 | `documentation/Data Management/Document-Based App Programming Guide for Mac` | 未开始 |
| 186 | iOS 版基于文档的应用程序编程指南 | Document-Based App Programming Guide for iOS | 8 | `documentation/Data Management/Document-Based App Programming Guide for iOS` | 未开始 |
| 187 | Spotlight 导入器编程指南 | Spotlight Importer Programming Guide | 8 | `documentation/Carbon/Spotlight Importer Programming Guide` | 未开始 |
| 188 | 包编程指南 | Bundle Programming Guide | 7 | `documentation/Core Foundation/Bundle Programming Guide` | 未开始 |
| 189 | Core Foundation 偏好设置编程主题 | Preferences Programming Topics for Core Foundation | 7 | `documentation/Core Foundation/Preferences Programming Topics for Core Foundation` | 未开始 |
| 190 | 使用 Text Encoding Conversion Manager 编程 | Programming With the Text Encoding Conversion Manager | 7 | `documentation/Carbon/Programming With the Text Encoding Conversion Manager` | 未开始 |
| 191 | Core Foundation 属性列表编程主题 | Property List Programming Topics for Core Foundation | 7 | `documentation/Core Foundation/Property List Programming Topics for Core Foundation` | 未开始 |
| 192 | Safari 客户端存储与离线应用程序编程指南 | Safari Client-Side Storage and Offline Applications Programming Guide | 7 | `documentation/iPhone/Safari Client-Side Storage and Offline Applications Programming Guide` | 未开始 |
| 193 | Services 实现指南 | Services Implementation Guide | 7 | `documentation/Cocoa/Services Implementation Guide` | 未开始 |
| 194 | Spotlight 概述 | Spotlight Overview | 7 | `documentation/Carbon/Spotlight Overview` | 未开始 |
| 195 | 面向 Core Data 的 iCloud 编程指南 | iCloud Programming Guide for Core Data | 7 | `documentation/Data Management/iCloud Programming Guide for Core Data` | 未开始 |
| 196 | iOS 版 Address Book 编程指南 | Address Book Programming Guide for iOS | 6 | `documentation/Address Book Programming Guide for iOS` | 未开始 |
| 197 | Apple File System 指南 | Apple File System Guide | 6 | `documentation/File Management/Apple File System Guide` | 未开始 |
| 198 | Core Data 代码片段 | Core Data Snippets | 6 | `documentation/Data Management/Core Data Snippets` | 未开始 |
| 199 | iOS 文档交互编程主题 | Document Interaction Programming Topics for iOS | 6 | `documentation/File Management/Document Interaction Programming Topics for iOS` | 未开始 |
| 200 | 文件元数据搜索编程指南 | File Metadata Search Programming Guide | 6 | `documentation/Carbon/File Metadata Search Programming Guide` | 未开始 |
| 201 | 文件系统事件编程指南 | File System Events Programming Guide | 6 | `documentation/Darwin/File System Events Programming Guide` | 未开始 |
| 202 | 运行时配置规范 | Runtime Configuration Guidelines | 6 | `documentation/Mac OSX/Runtime Configuration Guidelines` | 未开始 |
| 203 | 拼写检查编程主题 | Spell Checking Programming Topics | 6 | `documentation/Cocoa/Spell Checking Programming Topics` | 未开始 |
| 204 | Value Transformer 编程指南 | Value Transformer Programming Guide | 6 | `documentation/Cocoa/Value Transformer Programming Guide` | 未开始 |
| 205 | iOS 设备兼容性参考 | iOS Device Compatibility Reference | 6 | `documentation/iOS Device Compatibility Reference` | 未开始 |
| 206 | Core Foundation 二进制数据编程指南 | Binary Data Programming Guide for Core Foundation | 5 | `documentation/Core Foundation/Binary Data Programming Guide for Core Foundation` | 未开始 |
| 207 | Core Text 编程指南 | Core Text Programming Guide | 5 | `documentation/Strings Text Fonts/Core Text Programming Guide` | 未开始 |
| 208 | Core Foundation 日期和时间编程指南 | Date and Time Programming Guide for Core Foundation | 5 | `documentation/Core Foundation/Date and Time Programming Guide for Core Foundation` | 未开始 |
| 209 | 文件元数据属性参考 | File Metadata Attributes Reference | 5 | `documentation/File Metadata Attributes Reference` | 未开始 |
| 210 | Incremental Store 编程指南 | Incremental Store Programming Guide | 5 | `documentation/Data Management/Incremental Store Programming Guide` | 未开始 |
| 211 | Launch Services 编程指南 | Launch Services Programming Guide | 5 | `documentation/Carbon/Launch Services Programming Guide` | 未开始 |
| 212 | 文本附件编程主题 | Text Attachment Programming Topics | 5 | `documentation/Cocoa/Text Attachment Programming Topics` | 未开始 |
| 213 | 统一类型标识符概述 | Uniform Type Identifiers Overview | 5 | `documentation/File Management/Uniform Type Identifiers Overview` | 未开始 |
| 214 | 在应用程序中使用 Ink Services | Using Ink Services in Your Application | 5 | `documentation/Carbon/Using Ink Services in Your Application` | 未开始 |
| 215 | Core Foundation XML 编程主题 | XML Programming Topics for Core Foundation | 5 | `documentation/Core Foundation/XML Programming Topics for Core Foundation` | 未开始 |
| 216 | Apple Notification Center Service (ANCS) 规范 | Apple Notification Center Service (ANCS) Specification | 4 | `documentation/Core Bluetooth/Apple Notification Center Service (ANCS) Specification` | 未开始 |
| 217 | Core Data Spotlight 集成编程指南 | Core Data Spotlight Integration Programming Guide | 4 | `documentation/Cocoa/Core Data Spotlight Integration Programming Guide` | 未开始 |
| 218 | Core Foundation 数据格式化指南 | Data Formatting Guide for Core Foundation | 4 | `documentation/Core Foundation/Data Formatting Guide for Core Foundation` | 未开始 |
| 219 | 文稿选取器编程指南 | Document Picker Programming Guide | 4 | `documentation/File Management/Document Picker Programming Guide` | 未开始 |
| 220 | Locale 编程指南 | Locales Programming Guide | 4 | `documentation/Core Foundation/Locales Programming Guide` | 未开始 |
| 221 | CloudKit 快速入门 | CloudKit Quick Start | 3 | `documentation/Data Management/CloudKit Quick Start` | 未开始 |
| 222 | 文件系统高级编程主题 | File System Advanced Programming Topics | 3 | `documentation/File Management/File System Advanced Programming Topics` | 未开始 |
| 223 | Mail 编程主题 | Mail Programming Topics | 3 | `documentation/Apple Applications/Mail Programming Topics` | 未开始 |
| 224 | 统一类型标识符参考 | Uniform Type Identifiers Reference | 3 | `documentation/Miscellaneous/Uniform Type Identifiers Reference` | 未开始 |

### Xcode（47 份文档，468 页）

| # | 中文标题（索引已译） | 英文标题（正文待译） | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 225 | 标记格式参考 | Markup Formatting Reference | 51 | `documentation/Xcode/Markup Formatting Reference` | 未开始 |
| 226 | 使用 GDB 调试 | Debugging with GDB | 38 | `documentation/Developer Tools/Debugging with GDB` | 未开始 |
| 227 | 资源目录格式参考 | Asset Catalog Format Reference | 36 | `documentation/Xcode/Asset Catalog Format Reference` | 未开始 |
| 228 | GDB 内部原理 | GDB Internals | 22 | `documentation/Developer Tools/GDB Internals` | 未开始 |
| 229 | Shark 用户指南 | Shark User Guide | 22 | `documentation/Developer Tools/Shark User Guide` | 未开始 |
| 230 | Xcode 项目管理指南 | Xcode Project Management Guide | 16 | `documentation/Developer Tools/Xcode Project Management Guide` | 未开始 |
| 231 | Interface Builder 用户指南 | Interface Builder User Guide | 15 | `documentation/Developer Tools/Interface Builder User Guide` | 未开始 |
| 232 | Xcode 调试指南 | Xcode Debugging Guide | 15 | `documentation/Developer Tools/Xcode Debugging Guide` | 未开始 |
| 233 | 文档集指南 | Documentation Set Guide | 14 | `documentation/Developer Tools/Documentation Set Guide` | 未开始 |
| 234 | 框架编程指南 | Framework Programming Guide | 13 | `documentation/Mac OSX/Framework Programming Guide` | 未开始 |
| 235 | Dashcode 用户指南 | Dashcode User Guide | 12 | `documentation/Apple Applications/Dashcode User Guide` | 未开始 |
| 236 | HeaderDoc 用户指南 | HeaderDoc User Guide | 12 | `documentation/Developer Tools/HeaderDoc User Guide` | 未开始 |
| 237 | Xcode 工作区指南 | Xcode Workspace Guide | 12 | `documentation/Developer Tools/Xcode Workspace Guide` | 未开始 |
| 238 | 使用 Xcode 测试 | Testing with Xcode | 11 | `documentation/Developer Tools/Testing with Xcode` | 未开始 |
| 239 | 面向 Core Data 的 Xcode 工具 | Xcode Tools for Core Data | 11 | `documentation/Developer Tools/Xcode Tools for Core Data` | 未开始 |
| 240 | GNU C 4.2 预处理器内部原理 | GNU C 4.2 Preprocessor Internals | 10 | `documentation/Developer Tools/GNU C 4.2 Preprocessor Internals` | 未开始 |
| 241 | Xcode 单元测试指南 | Xcode Unit Testing Guide | 10 | `documentation/Developer Tools/Xcode Unit Testing Guide` | 未开始 |
| 242 | Xcode 4 过渡指南 | Xcode 4 Transition Guide | 9 | `documentation/IDEs/Xcode 4 Transition Guide` | 未开始 |
| 243 | Xcode 构建系统指南 | Xcode Build System Guide | 9 | `documentation/Developer Tools/Xcode Build System Guide` | 未开始 |
| 244 | Interface Builder 插件编程指南 | Interface Builder Plug-In Programming Guide | 8 | `documentation/Developer Tools/Interface Builder Plug-In Programming Guide` | 未开始 |
| 245 | Simulator 用户指南 | Simulator User Guide | 8 | `documentation/IDEs/Simulator User Guide` | 未开始 |
| 246 | 用于类建模的 Xcode 设计工具 | Xcode Design Tools for Class Modeling | 8 | `documentation/Developer Tools/Xcode Design Tools for Class Modeling` | 未开始 |
| 247 | Xcode Server API 参考 | Xcode Server API Reference | 8 | `documentation/Xcode/Xcode Server API Reference` | 未开始 |
| 248 | Xcode Server 与持续集成指南 | Xcode Server and Continuous Integration Guide | 8 | `documentation/IDEs/Xcode Server and Continuous Integration Guide` | 未开始 |
| 249 | Xcode 导览 | A Tour of Xcode | 7 | `documentation/Developer Tools/A Tour of Xcode` | 未开始 |
| 250 | Xcode 的新增内容 | What’s New in Xcode | 7 | `documentation/Developer Tools/What’s New in Xcode` | 未开始 |
| 251 | Xcode 源码管理指南 | Xcode Source Management Guide | 7 | `documentation/Developer Tools/Xcode Source Management Guide` | 未开始 |
| 252 | C++ 运行时环境编程指南 | C++ Runtime Environment Programming Guide | 6 | `documentation/Developer Tools/C++ Runtime Environment Programming Guide` | 未开始 |
| 253 | Xcode 新增内容存档 | What's New in Xcode — Archive | 6 | `documentation/Xcode/What's New in Xcode — Archive` | 未开始 |
| 254 | iSync Plug-in Maker 用户指南 | iSync Plug-in Maker User Guide | 6 | `documentation/Syncing/iSync Plug-in Maker User Guide` | 未开始 |
| 255 | Instruments 新增功能用户指南 | Instruments New Features User Guide | 5 | `documentation/Analysis Tools/Instruments New Features User Guide` | 未开始 |
| 256 | LLDB 快速入门指南 | LLDB Quick Start Guide | 5 | `documentation/IDEs/LLDB Quick Start Guide` | 未开始 |
| 257 | Xcode 键盘快捷键与手势 | Xcode Keyboard Shortcuts and Gestures | 5 | `documentation/IDEs/Xcode Keyboard Shortcuts and Gestures` | 未开始 |
| 258 | 面向 Core Data 的 Xcode 映射工具 | Xcode Mapping Tool for Core Data | 5 | `documentation/Developer Tools/Xcode Mapping Tool for Core Data` | 未开始 |
| 259 | Big Top 用户指南 | Big Top User Guide | 4 | `documentation/Developer Tools/Big Top User Guide` | 未开始 |
| 260 | 粒子发射器编辑器指南 | Particle Emitter Editor Guide | 4 | `documentation/IDEs/Particle Emitter Editor Guide` | 未开始 |
| 261 | Xcode 调试器中自定义类型的 Quick Look | Quick Look for Custom Types in the Xcode Debugger | 4 | `documentation/IDEs/Quick Look for Custom Types in the Xcode Debugger` | 未开始 |
| 262 | Saturn 4.5 用户指南 | Saturn 4.5 User Guide | 4 | `documentation/Developer Tools/Saturn 4.5 User Guide` | 未开始 |
| 263 | Xcode 安装指南 | Xcode Installation Guide | 4 | `documentation/Xcode/Xcode Installation Guide` | 未开始 |
| 264 | Xcode 配置文件引导优化 | Xcode Profile Guided Optimization | 4 | `documentation/Developer Tools/Xcode Profile Guided Optimization` | 未开始 |
| 265 | Instruments 帮助主题 | Instruments Help Topics | 1 | `documentation/Analysis Tools` | 未开始 |
| 266 | LLVM 编译器概述 | LLVM Compiler Overview | 1 | `documentation/LLVM Compiler Overview.md` | 未开始 |
| 267 | OS X 汇编器参考 | OS X Assembler Reference | 1 | `documentation/Developer Tools/OS X Assembler Reference.md` | 未开始 |
| 268 | Simulator 帮助主题 | Simulator Help Topics | 1 | `documentation/IDEs/Simulator Help Topics.md` | 未开始 |
| 269 | gperf 3.0.1 用户指南 | User's Guide to gperf 3.0.1 | 1 | `documentation/Developer Tools/User's Guide to gperf 3.0.1.md` | 未开始 |
| 270 | Xcode 构建系统指南 | Xcode Build System Guide | 1 | `documentation/Developer Tools/Xcode Build System Guide (2016).md` | 未开始 |
| 271 | Xcode 帮助主题 | Xcode Help Topics | 1 | `documentation/IDEs/Xcode Help Topics.md` | 未开始 |

### 用户体验（57 份文档，435 页）

| # | 中文标题（索引已译） | 英文标题（正文待译） | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 272 | 窗口编程指南 | Window Programming Guide | 25 | `documentation/Cocoa/Window Programming Guide` | 未开始 |
| 273 | 自动布局指南 | Auto Layout Guide | 19 | `documentation/User Experience/Auto Layout Guide` | 未开始 |
| 274 | 偏好设置面板编程指南 | Preference Pane Programming Guide | 16 | `documentation/User Experience/Preference Pane Programming Guide` | 未开始 |
| 275 | Button 编程主题 | Button Programming Topics | 15 | `documentation/Cocoa/Button Programming Topics` | 未开始 |
| 276 | Safari Web 内容指南 | Safari Web Content Guide | 15 | `documentation/Apple Applications/Safari Web Content Guide` | 未开始 |
| 277 | Control 与 Cell 编程主题 | Control and Cell Programming Topics | 14 | `documentation/Cocoa/Control and Cell Programming Topics` | 未开始 |
| 278 | Cocoa 版 Toolbar 编程主题 | Toolbar Programming Topics for Cocoa | 12 | `documentation/Cocoa/Toolbar Programming Topics for Cocoa` | 未开始 |
| 279 | Sheet 编程主题 | Sheet Programming Topics | 11 | `documentation/Cocoa/Sheet Programming Topics` | 未开始 |
| 280 | 文本布局编程指南 | Text Layout Programming Guide | 11 | `documentation/Cocoa/Text Layout Programming Guide` | 未开始 |
| 281 | 文本系统存储层概述 | Text System Storage Layer Overview | 11 | `documentation/Cocoa/Text System Storage Layer Overview` | 未开始 |
| 282 | 文本系统用户界面层编程指南 | Text System User Interface Layer Programming Guide | 11 | `documentation/Cocoa/Text System User Interface Layer Programming Guide` | 未开始 |
| 283 | 应用程序菜单与弹出列表编程主题 | Application Menu and Pop-up List Programming Topics | 10 | `documentation/Cocoa/Application Menu and Pop-up List Programming Topics` | 未开始 |
| 284 | 国际化与本地化指南 | Internationalization and Localization Guide | 10 | `documentation/Mac OSX/Internationalization and Localization Guide` | 未开始 |
| 285 | 定位与地图编程指南 | Location and Maps Programming Guide | 10 | `documentation/User Experience/Location and Maps Programming Guide` | 未开始 |
| 286 | Mac 版 Table View 编程指南 | Table View Programming Guide for Mac | 10 | `documentation/Cocoa/Table View Programming Guide for Mac` | 未开始 |
| 287 | Mac 版辅助功能编程规范 | Accessibility Programming Guidelines for Mac | 9 | `documentation/Cocoa/Accessibility Programming Guidelines for Mac` | 未开始 |
| 288 | Token Field 编程指南 | Token Field Programming Guide | 9 | `documentation/Cocoa/Token Field Programming Guide` | 未开始 |
| 289 | 钱包开发者指南 | Wallet Developer Guide | 9 | `documentation/User Experience/Wallet Developer Guide` | 未开始 |
| 290 | iOS 7 UI 过渡指南 | iOS 7 UI Transition Guide | 9 | `documentation/User Experience/iOS 7 UI Transition Guide` | 未开始 |
| 291 | OS X 辅助功能编程指南 | Accessibility Programming Guide for OS X | 8 | `documentation/Accessibility Programming Guide for OS X` | 未开始 |
| 292 | Apple Help 编程指南 | Apple Help Programming Guide | 8 | `documentation/Carbon/Apple Help Programming Guide` | 未开始 |
| 293 | Safari HTML 参考 | Safari HTML Reference | 8 | `documentation/Apple Applications/Safari HTML Reference` | 未开始 |
| 294 | 语音合成编程指南 | Speech Synthesis Programming Guide | 8 | `documentation/User Experience/Speech Synthesis Programming Guide` | 未开始 |
| 295 | 视图编程指南 | View Programming Guide | 8 | `documentation/Cocoa/View Programming Guide` | 未开始 |
| 296 | Combo Box 编程主题 | Combo Box Programming Topics | 7 | `documentation/Cocoa/Combo Box Programming Topics` | 未开始 |
| 297 | Box 编程主题 | Box Programming Topics | 6 | `documentation/Cocoa/Box Programming Topics` | 未开始 |
| 298 | 对话框与特殊面板 | Dialogs and Special Panels | 6 | `documentation/Cocoa/Dialogs and Special Panels` | 未开始 |
| 299 | Font Panel 编程主题 | Font Panel Programming Topics | 6 | `documentation/Cocoa/Font Panel Programming Topics` | 未开始 |
| 300 | 设计扩展广告单元指南 | Guide to Designing Expanded Ad Units | 6 | `documentation/User Experience/Guide to Designing Expanded Ad Units` | 未开始 |
| 301 | Matrix 编程指南 | Matrix Programming Guide | 6 | `documentation/Cocoa/Matrix Programming Guide` | 未开始 |
| 302 | Safari CSS 参考 | Safari CSS Reference | 6 | `documentation/Apple Applications/Safari CSS Reference` | 未开始 |
| 303 | Mac 版 Scroll View 编程指南 | Scroll View Programming Guide for Mac | 6 | `documentation/Cocoa/Scroll View Programming Guide for Mac` | 未开始 |
| 304 | SearchKit 编程指南 | SearchKit Programming Guide | 6 | `documentation/User Experience/SearchKit Programming Guide` | 未开始 |
| 305 | Tab View 编程主题 | Tab View Programming Topics | 6 | `documentation/Cocoa/Tab View Programming Topics` | 未开始 |
| 306 | Browser 编程主题 | Browser Programming Topics | 5 | `documentation/Cocoa/Browser Programming Topics` | 未开始 |
| 307 | 词典服务编程指南 | Dictionary Services Programming Guide | 5 | `documentation/User Experience/Dictionary Services Programming Guide` | 未开始 |
| 308 | Form 编程主题 | Form Programming Topics | 5 | `documentation/Cocoa/Form Programming Topics` | 未开始 |
| 309 | 多用户环境编程主题 | Multiple User Environment Programming Topics | 5 | `documentation/Mac OSX/Multiple User Environment Programming Topics` | 未开始 |
| 310 | 在线帮助 | Online Help | 5 | `documentation/Cocoa/Online Help` | 未开始 |
| 311 | Outline View 编程主题 | Outline View Programming Topics | 5 | `documentation/Cocoa/Outline View Programming Topics` | 未开始 |
| 312 | Progress Indicator 编程主题 | Progress Indicator Programming Topics | 5 | `documentation/Cocoa/Progress Indicator Programming Topics` | 未开始 |
| 313 | Slider 编程主题 | Slider Programming Topics | 5 | `documentation/Cocoa/Slider Programming Topics` | 未开始 |
| 314 | iAd JS HTML 和 CSS 声明式参考 | iAd JS HTML and CSS Declarative Reference | 5 | `documentation/User Experience/iAd JS HTML and CSS Declarative Reference` | 未开始 |
| 315 | iOS 辅助功能编程指南 | Accessibility Programming Guide for iOS | 4 | `documentation/User Experience/Accessibility Programming Guide for iOS` | 未开始 |
| 316 | 光标管理 | Cursor Management | 4 | `documentation/Cocoa/Cursor Management` | 未开始 |
| 317 | Data Browser 编程指南 | Data Browser Programming Guide | 4 | `documentation/Carbon/Data Browser Programming Guide` | 未开始 |
| 318 | Drawer 编程主题 | Drawer Programming Topics | 4 | `documentation/Cocoa/Drawer Programming Topics` | 未开始 |
| 319 | Image View 编程主题 | Image View Programming Topics | 4 | `documentation/Cocoa/Image View Programming Topics` | 未开始 |
| 320 | 面向受管客户端的偏好设置清单文件概述 | Preference Manifest Files for Managed Clients Overview | 4 | `documentation/Mac OSX Server/Preference Manifest Files for Managed Clients Overview` | 未开始 |
| 321 | Segmented Control 编程指南 | Segmented Control Programming Guide | 4 | `documentation/Cocoa/Segmented Control Programming Guide` | 未开始 |
| 322 | 语音编程主题 | Speech Programming Topics | 4 | `documentation/Cocoa/Speech Programming Topics` | 未开始 |
| 323 | Status Bar 编程主题 | Status Bar Programming Topics | 4 | `documentation/Cocoa/Status Bar Programming Topics` | 未开始 |
| 324 | iOS 系统消息编程主题 | System Messaging Programming Topics for iOS | 4 | `documentation/User Experience/System Messaging Programming Topics for iOS` | 未开始 |
| 325 | 用户界面验证 | User Interface Validation | 4 | `documentation/Cocoa/User Interface Validation` | 未开始 |
| 326 | 在 iPhone 上采用 3D Touch | Adopting 3D Touch on iPhone | 3 | `documentation/User Experience/Adopting 3D Touch on iPhone` | 未开始 |
| 327 | 接力编程指南 | Handoff Programming Guide | 3 | `documentation/User Experience/Handoff Programming Guide` | 未开始 |
| 328 | Stepper 编程主题 | Stepper Programming Topics | 3 | `documentation/Cocoa/Stepper Programming Topics` | 未开始 |

### 通用（34 份文档，285 页）

| # | 中文标题（索引已译） | 英文标题（正文待译） | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 329 | Objective-C 编程中的概念 | Concepts in Objective-C Programming | 15 | `documentation/General/Concepts in Objective-C Programming` | 未开始 |
| 330 | App 扩展编程指南 | App Extension Programming Guide | 14 | `documentation/General/App Extension Programming Guide` | 未开始 |
| 331 | Cocoa Bindings 编程主题 | Cocoa Bindings Programming Topics | 14 | `documentation/Cocoa/Cocoa Bindings Programming Topics` | 未开始 |
| 332 | 代码加载编程主题 | Code Loading Programming Topics | 13 | `documentation/Cocoa/Code Loading Programming Topics` | 未开始 |
| 333 | Core Foundation 设计理念 | Core Foundation Design Concepts | 11 | `documentation/Core Foundation/Core Foundation Design Concepts` | 未开始 |
| 334 | 你的第二个 iOS App：Storyboards | 'Your Second iOS App: Storyboards' | 10 | `documentation/iPhone/Your Second iOS App- Storyboards` | 未开始 |
| 335 | 你的第三个 iOS App：iCloud | 'Your Third iOS App: iCloud' | 10 | `documentation/General/Your Third iOS App- iCloud` | 未开始 |
| 336 | 64 位过渡指南 | 64-Bit Transition Guide | 10 | `documentation/Darwin/64-Bit Transition Guide` | 未开始 |
| 337 | tvOS App 编程指南 | App Programming Guide for tvOS | 10 | `documentation/General/App Programming Guide for tvOS` | 未开始 |
| 338 | App 搜索编程指南 | App Search Programming Guide | 10 | `documentation/General/App Search Programming Guide` | 未开始 |
| 339 | 守护进程与服务编程指南 | Daemons and Services Programming Guide | 10 | `documentation/Mac OSX/Daemons and Services Programming Guide` | 未开始 |
| 340 | 垃圾回收编程指南 | Garbage Collection Programming Guide | 10 | `documentation/Cocoa/Garbage Collection Programming Guide` | 未开始 |
| 341 | 信息属性列表键参考 | Information Property List Key Reference | 10 | `documentation/General/Information Property List Key Reference` | 未开始 |
| 342 | 动态库编程主题 | Dynamic Library Programming Topics | 9 | `documentation/Developer Tools/Dynamic Library Programming Topics` | 未开始 |
| 343 | GameplayKit 编程指南 | GameplayKit Programming Guide | 9 | `documentation/General/GameplayKit Programming Guide` | 未开始 |
| 344 | 与操作系统交互 | Interacting with the Operating System | 9 | `documentation/Cocoa/Interacting with the Operating System` | 未开始 |
| 345 | Mach-O 编程主题 | Mach-O Programming Topics | 9 | `documentation/Developer Tools/Mach-O Programming Topics` | 未开始 |
| 346 | watchOS 2 过渡指南 | watchOS 2 Transition Guide | 9 | `documentation/General/watchOS 2 Transition Guide` | 未开始 |
| 347 | 为 App Store 开发 | Developing for the App Store | 8 | `documentation/General/Developing for the App Store` | 未开始 |
| 348 | LLDB 调试指南 | LLDB Debugging Guide | 8 | `documentation/General/LLDB Debugging Guide` | 未开始 |
| 349 | Mac App 编程指南 | Mac App Programming Guide | 8 | `documentation/General/Mac App Programming Guide` | 未开始 |
| 350 | Mac 技术概述 | Mac Technology Overview | 8 | `documentation/Mac OSX/Mac Technology Overview` | 未开始 |
| 351 | 应用程序架构概述 | Application Architecture Overview | 7 | `documentation/Cocoa/Application Architecture Overview` | 未开始 |
| 352 | iCloud 设计指南 | iCloud Design Guide | 7 | `documentation/General/iCloud Design Guide` | 未开始 |
| 353 | 面向 Carbon 开发者的 64 位指南 | 64-Bit Guide for Carbon Developers | 6 | `documentation/Carbon/64-Bit Guide for Carbon Developers` | 未开始 |
| 354 | Cocoa 64 位过渡指南 | 64-Bit Transition Guide for Cocoa | 6 | `documentation/Cocoa/64-Bit Transition Guide for Cocoa` | 未开始 |
| 355 | Core Foundation 调试编程主题 | Debugging Programming Topics for Core Foundation | 6 | `documentation/Core Foundation/Debugging Programming Topics for Core Foundation` | 未开始 |
| 356 | Entitlement Key 参考 | Entitlement Key Reference | 6 | `documentation/Miscellaneous/Entitlement Key Reference` | 未开始 |
| 357 | OS X ABI 函数调用指南 | OS X ABI Function Call Guide | 6 | `documentation/Developer Tools/OS X ABI Function Call Guide` | 未开始 |
| 358 | 面向新闻发布商的营收报告 API | Revenue Reporting API for News Publishers | 5 | `documentation/General/Revenue Reporting API for News Publishers` | 未开始 |
| 359 | SDK 兼容性指南 | SDK Compatibility Guide | 5 | `documentation/Developer Tools/SDK Compatibility Guide` | 未开始 |
| 360 | OS X 术语表 | OS X Glossary | 3 | `documentation/General/OS X Glossary` | 未开始 |
| 361 | iAd 发布商报告参考 | iAd Publisher Reporting Reference | 2 | `documentation/General/iAd Publisher Reporting Reference` | 未开始 |
| 362 | iAd Tester 安装指南 | iAd Tester Installation Guide | 2 | `documentation/Miscellaneous/iAd Tester Installation Guide` | 未开始 |

### 图形与动画（29 份文档，247 页）

| # | 中文标题（索引已译） | 英文标题（正文待译） | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 363 | Mac 版 OpenGL 编程指南 | OpenGL Programming Guide for Mac | 21 | `documentation/Graphics Imaging/OpenGL Programming Guide for Mac` | 未开始 |
| 364 | Quartz 2D 编程指南 | Quartz 2D Programming Guide | 19 | `documentation/Graphics Imaging/Quartz 2D Programming Guide` | 未开始 |
| 365 | OpenGL ES 编程指南 | OpenGL ES Programming Guide | 18 | `documentation/3D Drawing/OpenGL ES Programming Guide` | 未开始 |
| 366 | Metal 最佳实践指南 | Metal Best Practices Guide | 15 | `documentation/3D Drawing/Metal Best Practices Guide` | 未开始 |
| 367 | Metal 编程指南 | Metal Programming Guide | 15 | `documentation/Miscellaneous/Metal Programming Guide` | 未开始 |
| 368 | 颜色编程主题 | Color Programming Topics | 13 | `documentation/Cocoa/Color Programming Topics` | 未开始 |
| 369 | Core Image 编程指南 | Core Image Programming Guide | 12 | `documentation/Graphics Imaging/Core Image Programming Guide` | 未开始 |
| 370 | Cocoa 绘制指南 | Cocoa Drawing Guide | 11 | `documentation/Cocoa/Cocoa Drawing Guide` | 未开始 |
| 371 | Quartz Display Services 编程主题 | Quartz Display Services Programming Topics | 11 | `documentation/Graphics Imaging/Quartz Display Services Programming Topics` | 未开始 |
| 372 | iOS 版绘制与打印指南 | Drawing and Printing Guide for iOS | 10 | `documentation/Drawing and Printing Guide for iOS` | 未开始 |
| 373 | ImageKit 编程指南 | ImageKit Programming Guide | 9 | `documentation/Graphics Imaging/ImageKit Programming Guide` | 未开始 |
| 374 | Mac 版打印编程指南 | Printing Programming Guide for Mac | 9 | `documentation/Cocoa/Printing Programming Guide for Mac` | 未开始 |
| 375 | SpriteKit 编程指南 | SpriteKit Programming Guide | 9 | `documentation/Graphics Animation/SpriteKit Programming Guide` | 未开始 |
| 376 | OS X 高分辨率指南 | High Resolution Guidelines for OS X | 8 | `documentation/Graphics Animation/High Resolution Guidelines for OS X` | 未开始 |
| 377 | 动画概述 | Animation Overview | 7 | `documentation/Graphics Imaging/Animation Overview` | 未开始 |
| 378 | Quartz Composer 自定义 Patch 编程指南 | Quartz Composer Custom Patch Programming Guide | 7 | `documentation/Graphics Imaging/Quartz Composer Custom Patch Programming Guide` | 未开始 |
| 379 | Image Unit 教程 | Image Unit Tutorial | 6 | `documentation/Graphics Imaging/Image Unit Tutorial` | 未开始 |
| 380 | Quartz Composer 编程指南 | Quartz Composer Programming Guide | 6 | `documentation/Graphics Imaging/Quartz Composer Programming Guide` | 未开始 |
| 381 | 颜色管理概述 | Color Management Overview | 5 | `documentation/Graphics Imaging/Color Management Overview` | 未开始 |
| 382 | Image Capture 应用程序编程指南 | Image Capture Applications Programming Guide | 5 | `documentation/Carbon/Image Capture Applications Programming Guide` | 未开始 |
| 383 | Image I/O 编程指南 | Image I/O Programming Guide | 5 | `documentation/Graphics Imaging/Image I-O Programming Guide` | 未开始 |
| 384 | Cocoa 版动画编程指南 | Animation Programming Guide for Cocoa | 4 | `documentation/Cocoa/Animation Programming Guide for Cocoa` | 未开始 |
| 385 | Core Animation 秘笈 | Core Animation Cookbook | 4 | `documentation/Graphics Imaging/Core Animation Cookbook` | 未开始 |
| 386 | PDFKit 编程指南 | PDFKit Programming Guide | 4 | `documentation/Graphics Imaging/PDFKit Programming Guide` | 未开始 |
| 387 | 使用 PostScript 打印机描述文件 | Using PostScript Printer Description Files | 4 | `documentation/Printing/Using PostScript Printer Description Files` | 未开始 |
| 388 | Core Image Kernel Language 参考 | Core Image Kernel Language Reference | 3 | `documentation/Graphics Imaging/Core Image Kernel Language Reference` | 未开始 |
| 389 | 在打印对话框中提供 PDF 工作流选项 | Providing PDF Workflow Options in the Print Dialog | 3 | `documentation/Printing/Providing PDF Workflow Options in the Print Dialog` | 未开始 |
| 390 | Core Image Filter 参考 | Core Image Filter Reference | 2 | `documentation/Graphics Imaging/Core Image Filter Reference` | 未开始 |
| 391 | SceneKit 编程指南 | SceneKit Programming Guide | 2 | `documentation/3D Drawing/SceneKit Programming Guide` | 未开始 |

### 网络与互联网（30 份文档，244 页）

| # | 中文标题（索引已译） | 英文标题（正文待译） | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 392 | Dashboard 编程主题 | Dashboard Programming Topics | 24 | `documentation/Apple Applications/Dashboard Programming Topics` | 未开始 |
| 393 | WebKit Objective-C 编程指南 | WebKit Objective-C Programming Guide | 22 | `documentation/Cocoa/WebKit Objective-C Programming Guide` | 未开始 |
| 394 | 网络概述 | Networking Overview | 13 | `documentation/Networking Internet Web/Networking Overview` | 未开始 |
| 395 | Game Center 编程指南 | Game Center Programming Guide | 11 | `documentation/Networking Internet/Game Center Programming Guide` | 未开始 |
| 396 | 本地和远程通知编程指南 | Local and Remote Notification Programming Guide | 11 | `documentation/Networking Internet/Local and Remote Notification Programming Guide` | 未开始 |
| 397 | EOModeler 用户指南 | EOModeler User Guide | 10 | `documentation/Web Objects/EOModeler User Guide` | 未开始 |
| 398 | Safari CSS 视觉效果指南 | Safari CSS Visual Effects Guide | 10 | `documentation/Internet Web/Safari CSS Visual Effects Guide` | 未开始 |
| 399 | WebObjects Builder 用户指南 | WebObjects Builder User Guide | 10 | `documentation/Web Objects/WebObjects Builder User Guide` | 未开始 |
| 400 | Core Services Identity 参考 | Core Services Identity Reference | 9 | `documentation/Networking/Core Services Identity Reference` | 未开始 |
| 401 | 网络概念 | Networking Concepts | 9 | `documentation/Networking Internet/Networking Concepts` | 未开始 |
| 402 | Safari Web Inspector 指南 | Safari Web Inspector Guide | 9 | `documentation/Apple Applications/Safari Web Inspector Guide` | 未开始 |
| 403 | CFNetwork 编程指南 | CFNetwork Programming Guide | 8 | `documentation/Networking/CFNetwork Programming Guide` | 未开始 |
| 404 | Core Bluetooth 编程指南 | Core Bluetooth Programming Guide | 8 | `documentation/Networking Internet Web/Core Bluetooth Programming Guide` | 未开始 |
| 405 | Java 应用程序服务器指南 | Java Application Server Guide | 8 | `documentation/Web Objects/Java Application Server Guide` | 未开始 |
| 406 | NSNetServices 与 CFNetServices 编程指南 | NSNetServices and CFNetServices Programming Guide | 8 | `documentation/Networking/NSNetServices and CFNetServices Programming Guide` | 未开始 |
| 407 | DNS 服务发现编程指南 | DNS Service Discovery Programming Guide | 7 | `documentation/Networking/DNS Service Discovery Programming Guide` | 未开始 |
| 408 | Game Controller 编程指南 | Game Controller Programming Guide | 7 | `documentation/Game Controller Programming Guide` | 未开始 |
| 409 | HTTP Live Streaming 概述 | HTTP Live Streaming Overview | 6 | `documentation/Networking Internet/HTTP Live Streaming Overview` | 未开始 |
| 410 | 热点网络子系统编程指南 | Hotspot Network Subsystem Programming Guide | 6 | `documentation/Networking Internet/Hotspot Network Subsystem Programming Guide` | 未开始 |
| 411 | Identity Services 编程指南 | Identity Services Programming Guide | 6 | `documentation/Networking/Identity Services Programming Guide` | 未开始 |
| 412 | System Configuration 编程规范 | System Configuration Programming Guidelines | 6 | `documentation/Networking/System Configuration Programming Guidelines` | 未开始 |
| 413 | Web Inspector 教程 | Web Inspector Tutorial | 6 | `documentation/Networking Internet Web/Web Inspector Tutorial` | 未开始 |
| 414 | 网络编程主题 | Networking Programming Topics | 5 | `documentation/Networking Internet/Networking Programming Topics` | 未开始 |
| 415 | 面向网站的通知编程指南 | Notification Programming Guide for Websites | 5 | `documentation/Networking Internet/Notification Programming Guide for Websites` | 未开始 |
| 416 | WebKit 插件编程主题 | WebKit Plug-In Programming Topics | 5 | `documentation/Internet Web/WebKit Plug-In Programming Topics` | 未开始 |
| 417 | HTTP Live Streaming 的定时元数据 | Timed Metadata for HTTP Live Streaming | 4 | `documentation/Audio Video/Timed Metadata for HTTP Live Streaming` | 未开始 |
| 418 | Web Services Core 编程指南 | Web Services Core Programming Guide | 4 | `documentation/Networking/Web Services Core Programming Guide` | 未开始 |
| 419 | Quartz Composer WebKit 插件 JavaScript 参考 | Quartz Composer WebKit Plug-in JavaScript Reference | 3 | `documentation/Internet Web/Quartz Composer WebKit Plug-in JavaScript Reference` | 未开始 |
| 420 | Time Machine 网络接口规范 (TMNIS) | Time Machine Network Interface Specification (TMNIS) | 3 | `documentation/Networking Internet Web/Time Machine Network Interface Specification (TMNIS)` | 未开始 |
| 421 | Dashboard 参考 | Dashboard Reference | 1 | `documentation/Apple Applications/Dashboard Reference.md` | 未开始 |

### 语言与工具（18 份文档，185 页）

| # | 中文标题（索引已译） | 英文标题（正文待译） | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 422 | Mac 自动化脚本编写指南 | Mac Automation Scripting Guide | 44 | `documentation/Mac Automation Scripting Guide` | 未开始 |
| 423 | AppleScript 语言指南 | AppleScript Language Guide | 22 | `documentation/Apple Script/AppleScript Language Guide` | 未开始 |
| 424 | Shell 脚本编写入门 | Shell Scripting Primer | 22 | `documentation/Shell Scripting Primer` | 未开始 |
| 425 | iOS 团队管理指南 | iOS Team Administration Guide | 11 | `documentation/Tools Languages/iOS Team Administration Guide` | 未开始 |
| 426 | App Store 提交教程 | App Store Submission Tutorial | 9 | `documentation/Tools Languages/App Store Submission Tutorial` | 未开始 |
| 427 | AppleScript 概述 | AppleScript Overview | 9 | `documentation/Apple Script/AppleScript Overview` | 未开始 |
| 428 | Automator AppleScript 操作教程 | Automator AppleScript Actions Tutorial | 9 | `documentation/Apple Applications/Automator AppleScript Actions Tutorial` | 未开始 |
| 429 | Mac Java 开发指南 | Java Development Guide for Mac | 8 | `documentation/Java/Java Development Guide for Mac` | 未开始 |
| 430 | Quartz Composer 用户指南 | Quartz Composer User Guide | 7 | `documentation/Graphics Imaging/Quartz Composer User Guide` | 未开始 |
| 431 | Mac 版 Ruby 与 Python 编程主题 | Ruby and Python Programming Topics for Mac | 7 | `documentation/Cocoa/Ruby and Python Programming Topics for Mac` | 未开始 |
| 432 | OpenGL Profiler 用户指南 | OpenGL Profiler User Guide | 6 | `documentation/Graphics Imaging/OpenGL Profiler User Guide` | 未开始 |
| 433 | Apple JavaScript 编码规范 | Apple JavaScript Coding Guidelines | 5 | `documentation/Apple JavaScript Coding Guidelines` | 未开始 |
| 434 | OpenGL Driver Monitor 用户指南 | OpenGL Driver Monitor User Guide | 5 | `documentation/Graphics Imaging/OpenGL Driver Monitor User Guide` | 未开始 |
| 435 | PackageMaker 用户指南 | PackageMaker User Guide | 5 | `documentation/Developer Tools/PackageMaker User Guide` | 未开始 |
| 436 | XML-RPC 和 SOAP 编程指南 | XML-RPC and SOAP Programming Guide | 5 | `documentation/Apple Script/XML-RPC and SOAP Programming Guide` | 未开始 |
| 437 | Jar Bundler 用户指南 | Jar Bundler User Guide | 4 | `documentation/Java/Jar Bundler User Guide` | 未开始 |
| 438 | OpenGL Shader Builder 用户指南 | OpenGL Shader Builder User Guide | 4 | `documentation/Graphics Imaging/OpenGL Shader Builder User Guide` | 未开始 |
| 439 | 分发定义 XML 架构参考 | Distribution Definition XML Schema Reference | 3 | `documentation/Developer Tools/Distribution Definition XML Schema Reference` | 未开始 |

### 驱动、内核与硬件（22 份文档，173 页）

| # | 中文标题（索引已译） | 英文标题（正文待译） | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 440 | 内核编程指南 | Kernel Programming Guide | 23 | `documentation/Darwin/Kernel Programming Guide` | 未开始 |
| 441 | IOKit 基础 | IOKit Fundamentals | 17 | `documentation/Device Drivers/IOKit Fundamentals` | 未开始 |
| 442 | IOKit 设备驱动程序设计指南 | IOKit Device Driver Design Guidelines | 13 | `documentation/Device Drivers/IOKit Device Driver Design Guidelines` | 未开始 |
| 443 | 网络内核扩展编程指南 | Network Kernel Extensions Programming Guide | 11 | `documentation/Darwin/Network Kernel Extensions Programming Guide` | 未开始 |
| 444 | 从应用程序访问硬件 | Accessing Hardware From Applications | 10 | `documentation/Device Drivers/Accessing Hardware From Applications` | 未开始 |
| 445 | 内核扩展编程主题 | Kernel Extension Programming Topics | 10 | `documentation/Darwin/Kernel Extension Programming Topics` | 未开始 |
| 446 | 大容量存储设备驱动程序编程指南 | Mass Storage Device Driver Programming Guide | 10 | `documentation/Device Drivers/Mass Storage Device Driver Programming Guide` | 未开始 |
| 447 | CCL 调制解调器脚本编写指南 | CCL Modem Scripting Guide | 8 | `documentation/Hardware Drivers/CCL Modem Scripting Guide` | 未开始 |
| 448 | 编写 PCI 驱动程序 | Writing PCI Drivers | 8 | `documentation/Device Drivers/Writing PCI Drivers` | 未开始 |
| 449 | HID 类设备接口指南 | HID Class Device Interface Guide | 7 | `documentation/Device Drivers/HID Class Device Interface Guide` | 未开始 |
| 450 | 音频设备驱动程序编程指南 | Audio Device Driver Programming Guide | 6 | `documentation/Device Drivers/Audio Device Driver Programming Guide` | 未开始 |
| 451 | FireWire 设备接口指南 | FireWire Device Interface Guide | 6 | `documentation/Device Drivers/FireWire Device Interface Guide` | 未开始 |
| 452 | Thunderbolt 设备驱动程序编程指南 | Thunderbolt Device Driver Programming Guide | 6 | `documentation/Hardware Drivers/Thunderbolt Device Driver Programming Guide` | 未开始 |
| 453 | 蓝牙设备访问指南 | Bluetooth Device Access Guide | 5 | `documentation/Device Drivers/Bluetooth Device Access Guide` | 未开始 |
| 454 | HBA 设备驱动程序编程指南 | HBA Device Driver Programming Guide | 5 | `documentation/Hardware Drivers/HBA Device Driver Programming Guide` | 未开始 |
| 455 | 网络设备驱动程序编程指南 | Network Device Driver Programming Guide | 5 | `documentation/Device Drivers/Network Device Driver Programming Guide` | 未开始 |
| 456 | 将驱动程序移植到 OS X | Porting Drivers to OS X | 5 | `documentation/Porting/Porting Drivers to OS X` | 未开始 |
| 457 | Disk Arbitration 编程指南 | Disk Arbitration Programming Guide | 4 | `documentation/Disk Arbitration Programming Guide` | 未开始 |
| 458 | SCSI 架构模型设备接口指南 | SCSI Architecture Model Device Interface Guide | 4 | `documentation/Device Drivers/SCSI Architecture Model Device Interface Guide` | 未开始 |
| 459 | USB 设备接口指南 | USB Device Interface Guide | 4 | `documentation/Device Drivers/USB Device Interface Guide` | 未开始 |
| 460 | 串行设备文件访问指南 | Device File Access Guide for Serial Devices | 3 | `documentation/Device Drivers/Device File Access Guide for Serial Devices` | 未开始 |
| 461 | 存储设备文件访问指南 | Device File Access Guide for Storage Devices | 3 | `documentation/Device Drivers/Device File Access Guide for Storage Devices` | 未开始 |

### 性能（14 份文档，159 页）

| # | 中文标题（索引已译） | 英文标题（正文待译） | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 462 | iOS App 能效指南 | Energy Efficiency Guide for iOS Apps | 25 | `documentation/Performance/Energy Efficiency Guide for iOS Apps` | 未开始 |
| 463 | Mac App 能效指南 | Energy Efficiency Guide for Mac Apps | 23 | `documentation/Performance/Energy Efficiency Guide for Mac Apps` | 未开始 |
| 464 | Mac OpenCL 编程指南 | OpenCL Programming Guide for Mac | 18 | `documentation/Performance/OpenCL Programming Guide for Mac` | 未开始 |
| 465 | 代码速度性能指南 | Code Speed Performance Guidelines | 12 | `documentation/Performance/Code Speed Performance Guidelines` | 未开始 |
| 466 | Core Foundation 内存管理编程指南 | Memory Management Programming Guide for Core Foundation | 11 | `documentation/Core Foundation/Memory Management Programming Guide for Core Foundation` | 未开始 |
| 467 | Cocoa 性能规范 | Cocoa Performance Guidelines | 10 | `documentation/Cocoa/Cocoa Performance Guidelines` | 未开始 |
| 468 | 内存使用性能指南 | Memory Usage Performance Guidelines | 10 | `documentation/Performance/Memory Usage Performance Guidelines` | 未开始 |
| 469 | 代码大小性能指南 | Code Size Performance Guidelines | 8 | `documentation/Performance/Code Size Performance Guidelines` | 未开始 |
| 470 | 并发编程指南 | Concurrency Programming Guide | 8 | `documentation/General/Concurrency Programming Guide` | 未开始 |
| 471 | 绘制性能指南 | Drawing Performance Guidelines | 8 | `documentation/Performance/Drawing Performance Guidelines` | 未开始 |
| 472 | Xgrid 编程指南 | Xgrid Programming Guide | 8 | `documentation/Mac OSX Server/Xgrid Programming Guide` | 未开始 |
| 473 | 启动时间性能指南 | Launch Time Performance Guidelines | 7 | `documentation/Performance/Launch Time Performance Guidelines` | 未开始 |
| 474 | 性能概述 | Performance Overview | 6 | `documentation/Performance/Performance Overview` | 未开始 |
| 475 | 蜂窝网络最佳实践指南 | Cellular Best Practices Guide | 5 | `documentation/Performance/Cellular Best Practices Guide` | 未开始 |

### 音视频与特效（22 份文档，121 页）

| # | 中文标题（索引已译） | 英文标题（正文待译） | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 476 | 音频会话编程指南 | Audio Session Programming Guide | 10 | `documentation/Audio/Audio Session Programming Guide` | 未开始 |
| 477 | Core Audio 概述 | Core Audio Overview | 9 | `documentation/Music Audio/Core Audio Overview` | 未开始 |
| 478 | Audio Unit 编程指南 | Audio Unit Programming Guide | 8 | `documentation/Music Audio/Audio Unit Programming Guide` | 未开始 |
| 479 | 媒体播放编程指南 | Media Playback Programming Guide | 8 | `documentation/Audio Video/Media Playback Programming Guide` | 未开始 |
| 480 | QTKit 应用程序教程 | QTKit Application Tutorial | 8 | `documentation/Cocoa/QTKit Application Tutorial` | 未开始 |
| 481 | QuickTime Kit 编程指南 | QuickTime Kit Programming Guide | 8 | `documentation/Quick Time/QuickTime Kit Programming Guide` | 未开始 |
| 482 | iPod 资料库访问编程指南 | iPod Library Access Programming Guide | 7 | `documentation/Audio/iPod Library Access Programming Guide` | 未开始 |
| 483 | AirPlay 概述 | AirPlay Overview | 6 | `documentation/Audio Video/AirPlay Overview` | 未开始 |
| 484 | DVD Playback Services 编程指南 | DVD Playback Services Programming Guide | 6 | `documentation/Graphics Imaging/DVD Playback Services Programming Guide` | 未开始 |
| 485 | Audio Queue Services 编程指南 | Audio Queue Services Programming Guide | 5 | `documentation/Music Audio/Audio Queue Services Programming Guide` | 未开始 |
| 486 | iOS 版 Audio Unit 宿主指南 | Audio Unit Hosting Guide for iOS | 5 | `documentation/Music Audio/Audio Unit Hosting Guide for iOS` | 未开始 |
| 487 | Core Video 编程指南 | Core Video Programming Guide | 5 | `documentation/Graphics Imaging/Core Video Programming Guide` | 未开始 |
| 488 | 用于 HTTP Live Streaming 的 MPEG-2 流加密格式 | MPEG-2 Stream Encryption Format for HTTP Live Streaming | 5 | `documentation/Audio Video/MPEG-2 Stream Encryption Format for HTTP Live Streaming` | 未开始 |
| 489 | QTKit 应用程序编程指南 | QTKit Application Programming Guide | 5 | `documentation/Cocoa/QTKit Application Programming Guide` | 未开始 |
| 490 | Cocoa 版声音编程主题 | Sound Programming Topics for Cocoa | 5 | `documentation/Cocoa/Sound Programming Topics for Cocoa` | 未开始 |
| 491 | Apple Media Service 参考 | Apple Media Service Reference | 4 | `documentation/Core Bluetooth/Apple Media Service Reference` | 未开始 |
| 492 | iOS 相机编程主题 | Camera Programming Topics for iOS | 4 | `documentation/Audio Video/Camera Programming Topics for iOS` | 未开始 |
| 493 | 多媒体编程指南 | Multimedia Programming Guide | 4 | `documentation/Audio Video/Multimedia Programming Guide` | 未开始 |
| 494 | Core Audio 术语表 | Core Audio Glossary | 3 | `documentation/Music Audio/Core Audio Glossary` | 未开始 |
| 495 | 面向 QuickTime 的 HTML 脚本编写指南 | HTML Scripting Guide for QuickTime | 3 | `documentation/Quick Time/HTML Scripting Guide for QuickTime` | 未开始 |
| 496 | MIDI 网络驱动程序协议 | MIDI Network Driver Protocol | 2 | `documentation/Audio/MIDI Network Driver Protocol` | 未开始 |
| 497 | Apple Core Audio Format 规范 1.0 | Apple Core Audio Format Specification 1.0 | 1 | `documentation/Music Audio` | 未开始 |

### 应用间通信（9 份文档，83 页）

| # | 中文标题（索引已译） | 英文标题（正文待译） | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 498 | Cocoa 脚本编写指南 | Cocoa Scripting Guide | 15 | `documentation/Cocoa/Cocoa Scripting Guide` | 未开始 |
| 499 | Distributed Objects 编程主题 | Distributed Objects Programming Topics | 14 | `documentation/Cocoa/Distributed Objects Programming Topics` | 未开始 |
| 500 | Automator 编程指南 | Automator Programming Guide | 13 | `documentation/Apple Applications/Automator Programming Guide` | 未开始 |
| 501 | Cocoa 版 Pasteboard 编程主题 | Pasteboard Programming Topics for Cocoa | 10 | `documentation/Cocoa/Pasteboard Programming Topics for Cocoa` | 未开始 |
| 502 | Pasteboard 编程指南 | Pasteboard Programming Guide | 8 | `documentation/Cocoa/Pasteboard Programming Guide` | 未开始 |
| 503 | 拖放编程主题 | Drag and Drop Programming Topics | 7 | `documentation/Cocoa/Drag and Drop Programming Topics` | 未开始 |
| 504 | Mac 通知概述 | Mac Notification Overview | 6 | `documentation/Darwin/Mac Notification Overview` | 未开始 |
| 505 | Pasteboard Manager 编程指南 | Pasteboard Manager Programming Guide | 5 | `documentation/Carbon/Pasteboard Manager Programming Guide` | 未开始 |
| 506 | Scripting Bridge 编程指南 | Scripting Bridge Programming Guide | 5 | `documentation/Cocoa/Scripting Bridge Programming Guide` | 未开始 |

### Apple 应用程序（12 份文档，70 页）

| # | 中文标题（索引已译） | 英文标题（正文待译） | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 507 | 日历脚本编写指南 | Calendar Scripting Guide | 13 | `documentation/Apple Applications/Calendar Scripting Guide` | 未开始 |
| 508 | FxPlug SDK 概述 | FxPlug SDK Overview | 12 | `documentation/Apple Applications/FxPlug SDK Overview` | 未开始 |
| 509 | Final Cut Pro X XML 的旧版 DTD | Legacy DTDs for Final Cut Pro X XML | 10 | `documentation/Miscellaneous/Legacy DTDs for Final Cut Pro X XML` | 未开始 |
| 510 | Final Cut Pro X 工作流程开发者指南 | Final Cut Pro X Workflows Developer Guide | 9 | `documentation/Final Cut Pro X/Final Cut Pro X Workflows Developer Guide` | 未开始 |
| 511 | Motion XML 文件格式 | Motion XML File Format | 9 | `documentation/Apple Applications/Motion XML File Format` | 未开始 |
| 512 | FxPlug 人机界面指南 | FxPlug Human Interface Guidelines | 7 | `documentation/Final Cut Pro X/FxPlug Human Interface Guidelines` | 未开始 |
| 513 | Aperture 2.1 SDK 概述 | Aperture 2.1 SDK Overview | 2 | `documentation/Apple Applications/Aperture 2.1 SDK Overview` | 未开始 |
| 514 | Aperture SDK 概述 | Aperture SDK Overview | 2 | `documentation/Aperture SDK Overview` | 未开始 |
| 515 | 为 iPhoto 创建打印预设 | Creating Printing Presets for iPhoto | 2 | `documentation/Printing/Creating Printing Presets for iPhoto` | 未开始 |
| 516 | 在 Final Cut 中渲染 FxPlug 效果 | Rendering FxPlug Effects in Final Cut | 2 | `documentation/Apple Applications/Rendering FxPlug Effects in Final Cut` | 未开始 |
| 517 | Final Cut Pro 7 XML 交换格式 | Final Cut Pro 7 XML Interchange Format | 1 | `documentation/Apple Applications/Final Cut Pro 7 XML Interchange Format.md` | 未开始 |
| 518 | 面向 Apple Loops 开发者的说明 | Notes for Apple Loops Developers | 1 | `documentation/Apple Applications/Notes for Apple Loops Developers.md` | 未开始 |

### 安全（8 份文档，61 页）

| # | 中文标题（索引已译） | 英文标题（正文待译） | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 519 | 安全编码指南 | Secure Coding Guide | 14 | `documentation/Security/Secure Coding Guide` | 未开始 |
| 520 | 加密服务指南 | Cryptographic Services Guide | 9 | `documentation/Security/Cryptographic Services Guide` | 未开始 |
| 521 | 安全性概述 | Security Overview | 9 | `documentation/Security/Security Overview` | 未开始 |
| 522 | Security Transforms 编程指南 | Security Transforms Programming Guide | 7 | `documentation/Security/Security Transforms Programming Guide` | 未开始 |
| 523 | 身份验证、授权与权限指南 | Authentication, Authorization, and Permissions Guide | 6 | `documentation/Security/Authentication, Authorization, and Permissions Guide` | 未开始 |
| 524 | 系统完整性保护指南 | System Integrity Protection Guide | 6 | `documentation/Security/System Integrity Protection Guide` | 未开始 |
| 525 | Authorization Services 编程指南 | Authorization Services Programming Guide | 5 | `documentation/Security/Authorization Services Programming Guide` | 未开始 |
| 526 | 代码签名指南 | Code Signing Guide | 5 | `documentation/Security/Code Signing Guide` | 未开始 |

### 跨平台（4 份文档，40 页）

| # | 中文标题（索引已译） | 英文标题（正文待译） | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 527 | 将 UNIX/Linux 应用程序移植到 OS X | Porting UNIX/Linux Applications to OS X | 13 | `documentation/Porting/Porting UNIX-Linux Applications to OS X` | 未开始 |
| 528 | 面向 Mac OS X 的 Java 1.3.1 开发 | Java 1.3.1 Development for Mac OS X | 11 | `documentation/Java/Java 1.3.1 Development for Mac OS X` | 未开始 |
| 529 | 从 Windows Win32 API 移植到 Mac OS X | Porting to Mac OS X from Windows Win32 API | 10 | `documentation/Porting/Porting to Mac OS X from Windows Win32 API` | 未开始 |
| 530 | 使用 Java Bridge | Using the Java Bridge | 6 | `documentation/Cocoa/Using the Java Bridge` | 未开始 |

### 数学计算（1 份文档，6 页）

| # | 中文标题（索引已译） | 英文标题（正文待译） | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 531 | vDSP 编程指南 | vDSP Programming Guide | 6 | `documentation/Performance/vDSP Programming Guide` | 未开始 |

### 系统管理（2 份文档，6 页）

| # | 中文标题（索引已译） | 英文标题（正文待译） | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 532 | OS X Server 故障转移消息传递架构指南 | OS X Server Failover Messaging Architecture Guide | 3 | `documentation/Mac OSX Server/OS X Server Failover Messaging Architecture Guide` | 未开始 |
| 533 | 服务器通知中心编程指南 | Server Notification Center Programming Guide | 3 | `documentation/Networking/Server Notification Center Programming Guide` | 未开始 |