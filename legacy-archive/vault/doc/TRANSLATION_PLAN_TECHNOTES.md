# technotes 分类翻译计划

> 前置说明见 `/agent.md`（翻译规范、铁律：标题与正文必须同批次翻译）与 `technotes/memory.md`（模块进度概览）。

## Context

`technotes/` 分类由 PR #10（"补入抓取器漏掉的 950 份归档文档"）新引入，此前仓库不存在这个分类，因此从未被纳入过任何翻译批次，**索引标题和正文都还是纯英文**，不存在"标题已译正文未译"的技术债问题——这是一份"从零开始"的计划，不是补技术债。

内容是 Apple Technical Note（tn 前缀，如 tn2058），绝大多数是独立单页短文（798 份文档对应 799 页，几乎 1:1），少量有配图子页面。

## 范围口径

- 覆盖 `technotes/` 目录下全部 798 份文档、799 页。
- 排除标准：无（体量都不大，未发现类似 documentation 分类里 WebObjects/GCC 那种超大型遗留文档，不需要排除）。
- 表格按 frontmatter `topic` 字段分组；604 份（约 76%）`topic` 字段为空，归入"未分类"，组内按标题字母序排列。

## 翻译流程

与 `doc/TRANSLATION_PLAN.md`、`doc/TRANSLATION_PLAN_DOCUMENTATION_PHASE2.md` 完全一致的约定（frontmatter 只译 title、代码块零改动、链接锚点不动、NBSP 守恒等），完整规范见 `/agent.md`。

**与 documentation 分类的区别**：本分类标题正文都未译，翻译时必须同一个 commit 里把该文档的 frontmatter title、正文、以及 `_indexes/technotes.md`（含子索引 `_indexes/technotes/*.md`、`_indexes/by-type/technical-note.md`）里对应的链接显示文字**一起改完**，不允许像 PR #9 那样只批量改索引不改正文。

## 执行建议

单篇体量小、彼此独立，不需要像 Cocoa 那样严格按顺序推进，可以按"未分类"之外的具体分类（音视频、数据管理、图形动画等）挑感兴趣的小批量认领，每批 20~30 篇为宜。

## 完整清单（798 份 / 799 页，按 topic 分组，组内页数从大到小排列）


### 未分类（603 份，603 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 1 | '"New" cdev Messages' | 1 | `technotes/tb/-New- cdev Messages` | 已译 |
| 2 | '''CDEF'' Parameters and Bugs' | 1 | `technotes/tb/'CDEF' Parameters and Bugs` | 已译 |
| 3 | '''LDEF'' Madness' | 1 | `technotes/tb/'LDEF' Madness` | 未开始 |
| 4 | '''SICN'' Tired of Large Icons in Menus?' | 1 | `technotes/tb/'SICN' Tired of Large Icons in Menus` | 未开始 |
| 5 | '''pdat'' specification' | 1 | `technotes/tn/'pdat' specification` | 未开始 |
| 6 | '''pslt'' resource - What Is It?' | 1 | `technotes/hw/'pslt' resource - What Is It` | 未开始 |
| 7 | '32-Bit QuickDraw: Version 1.2 Features' | 1 | `technotes/qd/32-Bit QuickDraw- Version 1.2 Features` | 未开始 |
| 8 | 'ADB - The Untold Story: Space Aliens Ate My Mouse' | 1 | `technotes/hw/ADB - The Untold Story- Space Aliens Ate My Mouse` | 未开始 |
| 9 | 'ADBReInit on the SE with System 4.1: Don''t Call It' | 1 | `technotes/hw/ADBReInit on the SE with System 4.1- Don't Call It` | 未开始 |
| 10 | 'AppleTalk: The Rest of the Story' | 1 | `technotes/nw/AppleTalk- The Rest of the Story` | 未开始 |
| 11 | 'BitMapToRegion: So Many Bitmaps, So Little Time' | 1 | `technotes/qd/BitMapToRegion- So Many Bitmaps, So Little Time` | 未开始 |
| 12 | 'Blessed Folder : A How-To Guide' | 1 | `technotes/fl/Blessed Folder - A How-To Guide` | 未开始 |
| 13 | 'Color Cursing: Two Major Causes' | 1 | `technotes/tn/Color Cursing- Two Major Causes` | 未开始 |
| 14 | 'Color Cursor Cursing: A Leading Cause' | 1 | `technotes/qd/Color Cursor Cursing- A Leading Cause` | 未开始 |
| 15 | 'Compatibility: Why & How' | 1 | `technotes/ov/Compatibility- Why & How` | 未开始 |
| 16 | 'Data in Resource Fork: Don''t Do It' | 1 | `technotes/fl/Data in Resource Fork- Don't Do It` | 未开始 |
| 17 | 'Deconstructing A Keynote 1.x Document: Part One - Slides' | 1 | `technotes/tn2002/Deconstructing A Keynote 1.x Document- Part One - Slides` | 未开始 |
| 18 | 'Driver Loader Library Call GetDriverInformation: A Bug & Workaround' | 1 | `technotes/tn/Driver Loader Library Call GetDriverInformation- A Bug & Workaround` | 未开始 |
| 19 | 'E.T.O: The Right Tools for the Right Job' | 1 | `technotes/tn/E.T.O- The Right Tools for the Right Job` | 未开始 |
| 20 | 'Finder Notes: "Get Info" Default & Icon Masks' | 1 | `technotes/ov/Finder Notes- -Get Info- Default & Icon Masks` | 未开始 |
| 21 | 'FireWire for Mac OS 9: An Overview' | 1 | `technotes/tn2004/FireWire for Mac OS 9- An Overview` | 未开始 |
| 22 | 'Fundamentals of Open Firmware, Part I: The User Interface' | 1 | `technotes/tn/Fundamentals of Open Firmware, Part I- The User Interface` | 未开始 |
| 23 | 'Fundamentals of Open Firmware, Part II: The Device Tree' | 1 | `technotes/tn/Fundamentals of Open Firmware, Part II- The Device Tree` | 未开始 |
| 24 | 'Fundamentals of Open Firmware, Part III: Understanding PCI Expansion ROM Choices | 1 | `technotes/tn/Fundamentals of Open Firmware, Part III- Understanding PCI Expansion ROM Choices` | 未开始 |
| 25 | 'Getting Up to Speed with QuickTime VR: Notes from the Field' | 1 | `technotes/tn/Getting Up to Speed with QuickTime VR- Notes from the Field` | 未开始 |
| 26 | 'Glue Code: It Gets You Out of Sticky Situations' | 1 | `technotes/pt/Glue Code- It Gets You Out of Sticky Situations` | 未开始 |
| 27 | 'High-Level Control and Status Calls: When a Good Call Goes Bad' | 1 | `technotes/dv/High-Level Control and Status Calls- When a Good Call Goes Bad` | 未开始 |
| 28 | 'History & Peregrinations: The Dogcow Goes QuickTime VR' | 1 | `technotes/tn/History & Peregrinations- The Dogcow Goes QuickTime VR` | 未开始 |
| 29 | 'HyperCard And You: Economy Edition' | 1 | `technotes/pt/HyperCard And You- Economy Edition` | 未开始 |
| 30 | 'Inside Macintosh: Devices, Power Manager Addenda' | 1 | `technotes/tn/Inside Macintosh- Devices, Power Manager Addenda` | 未开始 |
| 31 | 'Inside Macintosh: Files Errata' | 1 | `technotes/tn/Inside Macintosh- Files Errata` | 未开始 |
| 32 | 'Inside Macintosh: Memory Errata' | 1 | `technotes/im errata/Inside Macintosh- Memory Errata` | 未开始 |
| 33 | 'Inside Macintosh: Networking Errata' | 1 | `technotes/im errata/Inside Macintosh- Networking Errata` | 未开始 |
| 34 | 'Inside Macintosh: Operating System Utilities: Addendum to Chapter 4 - Determining | 1 | `technotes/tn/Inside Macintosh- Operating System Utilities- Addendum to Chapter 4 - Determinin` | 未开始 |
| 35 | 'Inside Macintosh: Overview Errata' | 1 | `technotes/im errata/Inside Macintosh- Overview Errata` | 未开始 |
| 36 | 'Inside Macintosh: PowerPC System Software Errata' | 1 | `technotes/im errata/Inside Macintosh- PowerPC System Software Errata` | 未开始 |
| 37 | 'Inside Macintosh: Processes Errata' | 1 | `technotes/im errata/Inside Macintosh- Processes Errata` | 未开始 |
| 38 | 'Inside Macintosh: Processes: Time Manager Addenda' | 1 | `technotes/tn/Inside Macintosh- Processes- Time Manager Addenda` | 未开始 |
| 39 | 'JNI Tips: Building Your Native-Method Libraries For MacOS' | 1 | `technotes/tn/JNI Tips- Building Your Native-Method Libraries For MacOS` | 未开始 |
| 40 | 'LW 8.5.1 CopyBits Support: Transparent and Clipped Images' | 1 | `technotes/tn/LW 8.5.1 CopyBits Support- Transparent and Clipped Images` | 未开始 |
| 41 | 'LaserWriter 8.5.1: The Extended ''PAPA'' Resource' | 1 | `technotes/tn/LaserWriter 8.5.1- The Extended 'PAPA' Resource` | 未开始 |
| 42 | 'LaserWriter 8.5.1: The Settings Library' | 1 | `technotes/tn/LaserWriter 8.5.1- The Settings Library` | 未开始 |
| 43 | 'LaserWriter 8.6: How to Write a Converter Plug-in for the Download Manager' | 1 | `technotes/tn/LaserWriter 8.6- How to Write a Converter Plug-in for the Download Manager` | 未开始 |
| 44 | 'MPW C Functions: To declare or not to declare, that is the question.' | 1 | `technotes/pt/MPW C Functions- To declare or not to declare, that is the question` | 未开始 |
| 45 | 'MPW: {$LOAD}; _DataInit;%_MethTables' | 1 | `technotes/pt/MPW- {$LOAD}; DataInit;%MethTables` | 未开始 |
| 46 | 'Mac OS X: v10.1.1 - v10.1.3' | 1 | `technotes/tn/Mac OS X- v10.1.1 - v10.1.3` | 未开始 |
| 47 | 'Macintosh IIfx:  The Inside Story' | 1 | `technotes/hw/Macintosh IIfx- The Inside Story` | 未开始 |
| 48 | 'Maximizing Your Media: A Brief Guide To the Latest and Greatest QuickTime | 1 | `technotes/tn/Maximizing Your Media- A Brief Guide To the Latest and Greatest QuickTime Media` | 未开始 |
| 49 | 'MicroBug: The ROM Debugger' | 1 | `technotes/tn/MicroBug- The ROM Debugger` | 未开始 |
| 50 | 'Mixing QuickDraw & Post-Script Printing from Your App: Some Gotchas' | 1 | `technotes/tn/Mixing QuickDraw & Post-Script Printing from Your App- Some Gotchas` | 未开始 |
| 51 | 'Monitor Depth : Gimmie Depth Or Gimmie Death' | 1 | `technotes/dv/Monitor Depth - Gimmie Depth Or Gimmie Death` | 未开始 |
| 52 | 'MultiFinder Revisited:  The 6.0 System' | 1 | `technotes/ov/MultiFinder Revisited- The 6.0 System` | 未开始 |
| 53 | 'On Changes to QuickTime Conferencing Components: New Error Codes, Behavior | 1 | `technotes/tn/On Changes to QuickTime Conferencing Components- New Error Codes, Behavior & Met` | 未开始 |
| 54 | 'On the Importance of Print Testing: A Brief Checklist' | 1 | `technotes/tn/On the Importance of Print Testing- A Brief Checklist` | 未开始 |
| 55 | 'OpenRFPerm: What your mother never told you' | 1 | `technotes/tb/OpenRFPerm- What your mother never told you` | 未开始 |
| 56 | 'Parameters for MDEF Message #3' | 1 | `technotes/tb/Parameters for MDEF Message 3` | 未开始 |
| 57 | 'Pascal to C:  PROCEDURE Parameters' | 1 | `technotes/pt/Pascal to C- PROCEDURE Parameters` | 未开始 |
| 58 | 'Plotting Small Icons: The ''SICN'' Resource' | 1 | `technotes/tn/Plotting Small Icons- The 'SICN' Resource` | 未开始 |
| 59 | 'Power Management & Servers: Auto Restart From Power Failure' | 1 | `technotes/tn/Power Management & Servers- Auto Restart From Power Failure` | 未开始 |
| 60 | 'Print Dialogs: Adding Items' | 1 | `technotes/pr/Print Dialogs- Adding Items` | 未开始 |
| 61 | 'QuickDraw GX ''ptyp'' Resource: Calculations, Uses & Limitations' | 1 | `technotes/tn/QuickDraw GX 'ptyp' Resource- Calculations, Uses & Limitations` | 未开始 |
| 62 | 'QuickDraw GX ''rdip'' Resources: The Number of the Beast' | 1 | `technotes/tn/QuickDraw GX 'rdip' Resources- The Number of the Beast` | 未开始 |
| 63 | 'QuickDraw GX ConicLibrary.c in Detail: Description and Derivations' | 1 | `technotes/tn/QuickDraw GX ConicLibrary.c in Detail- Description and Derivations` | 未开始 |
| 64 | 'QuickDraw GX MappingLibrary.c: Its Uses and Limitations' | 1 | `technotes/tn/QuickDraw GX MappingLibrary.c- Its Uses and Limitations` | 未开始 |
| 65 | 'QuickDraw GX OffscreenLibrary.c in Detail: Description, Uses & Limitations' | 1 | `technotes/tn/QuickDraw GX OffscreenLibrary.c in Detail- Description, Uses & Limitations` | 未开始 |
| 66 | 'Running CFM-68K Code at Interrupt Time: Is Your Code at Risk?' | 1 | `technotes/tn/Running CFM-68K Code at Interrupt Time- Is Your Code at Risk` | 未开始 |
| 67 | 'SIMMs to DIMMs: Making Sense Out of Memory Expansion for the Power Macintosh' | 1 | `technotes/tn/SIMMs to DIMMs- Making Sense Out of Memory Expansion for the Power Macintosh` | 未开始 |
| 68 | 'SendToSelf: Getting in Touch With Yourself Via the Apple Event Manager' | 1 | `technotes/ic/SendToSelf- Getting in Touch With Yourself Via the Apple Event Manager` | 未开始 |
| 69 | 'SimpleCocoaApp: An Overview' | 1 | `technotes/tn/SimpleCocoaApp- An Overview` | 未开始 |
| 70 | 'Some Sound Advice: Getting the Most Out of the Sound Manager' | 1 | `technotes/tn/Some Sound Advice- Getting the Most Out of the Sound Manager` | 未开始 |
| 71 | 'Sony Driver: What Your Sony Drives For You' | 1 | `technotes/dv/Sony Driver- What Your Sony Drives For You` | 未开始 |
| 72 | 'TextEdit: Advice & Descent' | 1 | `technotes/te/TextEdit- Advice & Descent` | 未开始 |
| 73 | 'The Notification Manager: Problems & Fixes' | 1 | `technotes/tn/The Notification Manager- Problems & Fixes` | 未开始 |
| 74 | 'Traditional Device Drivers: Sync or Swim' | 1 | `technotes/tn/Traditional Device Drivers- Sync or Swim` | 未开始 |
| 75 | 'Tuning for G5: A Practical Guide' | 1 | `technotes/tn/Tuning for G5- A Practical Guide` | 未开始 |
| 76 | 'Update: Borrowed AFP Sessions' | 1 | `technotes/tn/Update- Borrowed AFP Sessions` | 未开始 |
| 77 | 'VCBs and Drive Numbers : The Real Story' | 1 | `technotes/fl/VCBs and Drive Numbers - The Real Story` | 未开始 |
| 78 | 'Write Cache Flushing: Techniques for Properly Handling System Shutdown' | 1 | `technotes/tn/Write Cache Flushing- Techniques for Properly Handling System Shutdown` | 未开始 |
| 79 | '_StripAddress:  The Untold Story' | 1 | `technotes/me/StripAddress- The Untold Story` | 未开始 |
| 80 | +5 Volt Trickle | 1 | `technotes/hw/+5 Volt Trickle` | 未开始 |
| 81 | 10+ Commandments | 1 | `technotes/ov/10+ Commandments` | 未开始 |
| 82 | 8*24 GC QuickDraw and Deaccelerated CopyBits | 1 | `technotes/qd/824 GC QuickDraw and Deaccelerated CopyBits` | 未开始 |
| 83 | A Printing Loop That Cares - The Sequel | 1 | `technotes/tn/A Printing Loop That Cares - The Sequel` | 未开始 |
| 84 | A Printing Loop That Cares... | 1 | `technotes/pr/A Printing Loop That Cares` | 未开始 |
| 85 | A Technique for Estimating the Total RAM You Need for a QuickTime VR Project | 1 | `technotes/tn/A Technique for Estimating the Total RAM You Need for a QuickTime VR Project` | 未开始 |
| 86 | A Technique for Figuring Out a Resource's Base Value | 1 | `technotes/tn/A Technique for Figuring Out a Resource's Base Value` | 未开始 |
| 87 | A/ROSE & MCP Card Q&As | 1 | `technotes/pt/A-ROSE & MCP Card Q&As` | 未开始 |
| 88 | A/UX 2.0 Compatibility Guidelines | 1 | `technotes/pt/A-UX 2.0 Compatibility Guidelines` | 未开始 |
| 89 | A/UX Q&As | 1 | `technotes/pt/A-UX Q&As` | 未开始 |
| 90 | A/UX System Calls From Macintosh Software | 1 | `technotes/pt/A-UX System Calls From Macintosh Software` | 未开始 |
| 91 | A5 Within Trap Patches - Don't Depend on It | 1 | `technotes/ov/A5 Within Trap Patches - Don't Depend on It` | 未开始 |
| 92 | AOCE SMPReadContent Function | 1 | `technotes/nw/AOCE SMPReadContent Function` | 未开始 |
| 93 | ARA GetUserPortGlobalsPtr Call | 1 | `technotes/nw/ARA GetUserPortGlobalsPtr Call` | 未开始 |
| 94 | ASP and AFP Description Discrepancies | 1 | `technotes/nw/ASP and AFP Description Discrepancies` | 未开始 |
| 95 | ATA Device Software Guide Additions and Corrections | 1 | `technotes/tn/ATA Device Software Guide Additions and Corrections` | 未开始 |
| 96 | ATA Interface Modules | 1 | `technotes/tn/ATA Interface Modules` | 未开始 |
| 97 | About the Keynote 1.x XML File Format (APXL Schema) | 1 | `technotes/tn2002/About the Keynote 1.x XML File Format (APXL Schema)` | 未开始 |
| 98 | Absolute Pointing Device Memory Structure | 1 | `technotes/dv/Absolute Pointing Device Memory Structure` | 未开始 |
| 99 | Access & the Power Manager:Headaches & Cures | 1 | `technotes/tn/Access & the Power Manager-Headaches & Cures` | 未开始 |
| 100 | Adding In-App Purchase to Your Applications | 1 | `technotes/Adding In-App Purchase to Your Applications` | 未开始 |
| 101 | Adding Items to the Printing Manager's Dialogs | 1 | `technotes/tn/Adding Items to the Printing Manager's Dialogs` | 未开始 |
| 102 | Alias Manager Q&As | 1 | `technotes/fl/Alias Manager Q&As` | 未开始 |
| 103 | Apple Desktop Bus Q&As | 1 | `technotes/hw/Apple Desktop Bus Q&As` | 未开始 |
| 104 | Apple Event Manager Q&As | 1 | `technotes/ic/Apple Event Manager Q&As` | 未开始 |
| 105 | Apple Extensions to ISO 9660 | 1 | `technotes/fl/Apple Extensions to ISO 9660` | 未开始 |
| 106 | Apple File Exchange Q&As | 1 | `technotes/pt/Apple File Exchange Q&As` | 未开始 |
| 107 | Apple Media Tool's Memory Error Explained | 1 | `technotes/tn/Apple Media Tool's Memory Error Explained` | 未开始 |
| 108 | Apple's Multidisk Installer | 1 | `technotes/pt/Apple's Multidisk Installer` | 未开始 |
| 109 | AppleShare Foreground Applications | 1 | `technotes/nw/AppleShare Foreground Applications` | 未开始 |
| 110 | AppleShare Q&As | 1 | `technotes/nw/AppleShare Q&As` | 未开始 |
| 111 | AppleShare and File-Sharing Limits | 1 | `technotes/nw/AppleShare and File-Sharing Limits` | 未开始 |
| 112 | AppleShare and Old Finders | 1 | `technotes/nw/AppleShare and Old Finders` | 未开始 |
| 113 | AppleShare-able Applications and the Resource Manager | 1 | `technotes/nw/AppleShare-able Applications and the Resource Manager` | 未开始 |
| 114 | AppleTalk Data Stream Protocol Q&As | 1 | `technotes/nw/AppleTalk Data Stream Protocol Q&As` | 未开始 |
| 115 | AppleTalk Ethernet Driver Q&As | 1 | `technotes/nw/AppleTalk Ethernet Driver Q&As` | 未开始 |
| 116 | AppleTalk Filing Protocol Q&As | 1 | `technotes/nw/AppleTalk Filing Protocol Q&As` | 未开始 |
| 117 | AppleTalk Interface Update | 1 | `technotes/nw/AppleTalk Interface Update` | 未开始 |
| 118 | AppleTalk Overview Q&As | 1 | `technotes/nw/AppleTalk Overview Q&As` | 未开始 |
| 119 | AppleTalk Phase 2 on the Macintosh | 1 | `technotes/nw/AppleTalk Phase 2 on the Macintosh` | 未开始 |
| 120 | AppleTalk Remote Access Protocol Q&As | 1 | `technotes/nw/AppleTalk Remote Access Protocol Q&As` | 未开始 |
| 121 | AppleTalk Timers Explained | 1 | `technotes/nw/AppleTalk Timers Explained` | 未开始 |
| 122 | AppleTalk Transaction Protocol Q&As | 1 | `technotes/nw/AppleTalk Transaction Protocol Q&As` | 未开始 |
| 123 | AppleVision Technote | 1 | `technotes/tn/AppleVision Technote` | 未开始 |
| 124 | Applet Signing with MRJ and Javakey | 1 | `technotes/tn/Applet Signing with MRJ and Javakey` | 未开始 |
| 125 | Arbitrating the Use of afpMiscUserCommand and afpMiscUserWrite | 1 | `technotes/nw/Arbitrating the Use of afpMiscUserCommand and afpMiscUserWrite` | 未开始 |
| 126 | Available Volumes | 1 | `technotes/fl/Available Volumes` | 未开始 |
| 127 | Avoid Use of Network Events | 1 | `technotes/nw/Avoid Use of Network Events` | 未开始 |
| 128 | Basic QuickDraw Q&As | 1 | `technotes/qd/Basic QuickDraw Q&As` | 未开始 |
| 129 | Boot Blocks | 1 | `technotes/dv/Boot Blocks` | 未开始 |
| 130 | Borrowed AFP Sessions | 1 | `technotes/nw/Borrowed AFP Sessions` | 未开始 |
| 131 | Break/CTS Device Driver Event Structure | 1 | `technotes/hw/Break-CTS Device Driver Event Structure` | 未开始 |
| 132 | Building Universal QuickTime Components for Mac OS X | 1 | `technotes/Building Universal QuickTime Components for Mac OS X` | 未开始 |
| 133 | Building a 3D application that calls RAVE | 1 | `technotes/tn/Building a 3D application that calls RAVE` | 未开始 |
| 134 | Bundles | 1 | `technotes/tb/Bundles` | 未开始 |
| 135 | Bus Error Handlers | 1 | `technotes/dv/Bus Error Handlers` | 未开始 |
| 136 | Byte Smear(ing) Tactics | 1 | `technotes/hw/Byte Smear(ing) Tactics` | 未开始 |
| 137 | C++ Pitfalls in MPW | 1 | `technotes/pt/C++ Pitfalls in MPW` | 未开始 |
| 138 | CD Remote Database Format | 1 | `technotes/dv/CD Remote Database Format` | 未开始 |
| 139 | CD-ROM Driver Calls | 1 | `technotes/dv/CD-ROM Driver Calls` | 未开始 |
| 140 | CD-ROM Notes (Most Excellent) | 1 | `technotes/dv/CD-ROM Notes (Most Excellent)` | 未开始 |
| 141 | CD-ROM Q&As | 1 | `technotes/dv/CD-ROM Q&As` | 未开始 |
| 142 | CMOS On Macintosh LC PDS | 1 | `technotes/hw/CMOS On Macintosh LC PDS` | 未开始 |
| 143 | Cache As Cache Can | 1 | `technotes/hw/Cache As Cache Can` | 未开始 |
| 144 | Calling CFM Code From Classic 68K Code | 1 | `technotes/tn/Calling CFM Code From Classic 68K Code` | 未开始 |
| 145 | Changes in International Utilities and Resources | 1 | `technotes/te/Changes in International Utilities and Resources` | 未开始 |
| 146 | Checking for Specific Functionality | 1 | `technotes/ov/Checking for Specific Functionality` | 未开始 |
| 147 | Checklist for Building Applications and Extensions | 1 | `technotes/tn/Checklist for Building Applications and Extensions` | 未开始 |
| 148 | ChooseMovieClock and Video Output Components | 1 | `technotes/tn/ChooseMovieClock and Video Output Components` | 未开始 |
| 149 | Chooser Enhancements | 1 | `technotes/ov/Chooser Enhancements` | 未开始 |
| 150 | Clearing ioCompletion | 1 | `technotes/fl/Clearing ioCompletion` | 未开始 |
| 151 | Collaborative Computing Q&As | 1 | `technotes/ic/Collaborative Computing Q&As` | 未开始 |
| 152 | Color Management in Safari | 1 | `technotes/Color Management in Safari.md` | 未开始 |
| 153 | Color Manager Q&As | 1 | `technotes/qd/Color Manager Q&As` | 未开始 |
| 154 | Color Monitor Connections | 1 | `technotes/hw/Color Monitor Connections` | 未开始 |
| 155 | Color Picker 2.1 | 1 | `technotes/tn/Color Picker 2.1` | 未开始 |
| 156 | Color Printing | 1 | `technotes/pr/Color Printing` | 未开始 |
| 157 | Color QuickDraw Q&As | 1 | `technotes/qd/Color QuickDraw Q&As` | 未开始 |
| 158 | Color, Windows and 7.0 | 1 | `technotes/tb/Color, Windows and 7.0` | 未开始 |
| 159 | Colorizing With CopyBits | 1 | `technotes/qd/Colorizing With CopyBits` | 未开始 |
| 160 | Command-Shift-Number Keys | 1 | `technotes/os/Command-Shift-Number Keys` | 未开始 |
| 161 | Communications Toolbox Overview Q&As | 1 | `technotes/cm/Communications Toolbox Overview Q&As` | 未开始 |
| 162 | Compatibility Guidelines | 1 | `technotes/ov/Compatibility Guidelines` | 未开始 |
| 163 | Compatibility Q&As | 1 | `technotes/ov/Compatibility Q&As` | 未开始 |
| 164 | Compatibility between JDirect 2 and JDirect 3 | 1 | `technotes/tn/Compatibility between JDirect 2 and JDirect 3` | 未开始 |
| 165 | Component Manager Q&As | 1 | `technotes/tb/Component Manager Q&As` | 未开始 |
| 166 | Component Manager version 3.0 | 1 | `technotes/qt/Component Manager version 3.0` | 未开始 |
| 167 | Composite SIMMs Not Supported | 1 | `technotes/hw/Composite SIMMs Not Supported` | 未开始 |
| 168 | Compressing QuickTime Movies for the Web | 1 | `technotes/Compressing QuickTime Movies for the Web` | 未开始 |
| 169 | Connection Manager Q&As | 1 | `technotes/cm/Connection Manager Q&As` | 未开始 |
| 170 | Constructing a Business Card DSSpec | 1 | `technotes/nw/Constructing a Business Card DSSpec` | 未开始 |
| 171 | Control Panel Q&As | 1 | `technotes/tb/Control Panel Q&As` | 未开始 |
| 172 | Control Strip Modules | 1 | `technotes/os/Control Strip Modules` | 未开始 |
| 173 | Cooperating with the Coprocessor | 1 | `technotes/hw/Cooperating with the Coprocessor` | 未开始 |
| 174 | Coping With VM and Memory Mappings | 1 | `technotes/me/Coping With VM and Memory Mappings` | 未开始 |
| 175 | CreateResFile and the Poor Man's Search Path | 1 | `technotes/fl/CreateResFile and the Poor Man's Search Path` | 未开始 |
| 176 | Creating Desktop Printers on the Fly | 1 | `technotes/tn/Creating Desktop Printers on the Fly` | 未开始 |
| 177 | Creating Files Inside an AppleShare Drop Folder | 1 | `technotes/fl/Creating Files Inside an AppleShare Drop Folder` | 未开始 |
| 178 | Creating Off-Screen Bitmaps When Speed is Critical | 1 | `technotes/tn/Creating Off-Screen Bitmaps When Speed is Critical` | 未开始 |
| 179 | Cursor Components | 1 | `technotes/tn/Cursor Components` | 未开始 |
| 180 | Custom Menu Flashing Bug | 1 | `technotes/tb/Custom Menu Flashing Bug` | 未开始 |
| 181 | Custom WDEF and wDraw | 1 | `technotes/tb/Custom WDEF and wDraw` | 未开始 |
| 182 | Customizing Apple Media Tool 2.0 & 2.1 Scroll Bars and Movie Controllers | 1 | `technotes/tn/Customizing Apple Media Tool 2.0 & 2.1 Scroll Bars and Movie Controllers` | 未开始 |
| 183 | Customizing Desktop Printer Utility | 1 | `technotes/tn/Customizing Desktop Printer Utility` | 未开始 |
| 184 | Data Access Extensions | 1 | `technotes/nw/Data Access Extensions` | 未开始 |
| 185 | Data Servers on AppleTalk | 1 | `technotes/nw/Data Servers on AppleTalk` | 未开始 |
| 186 | Datagram Delivery Protocol Q&As | 1 | `technotes/nw/Datagram Delivery Protocol Q&As` | 未开始 |
| 187 | Debugging FairPlay Streaming | 1 | `technotes/Debugging FairPlay Streaming` | 未开始 |
| 188 | Debugging Java Code With MacsBug | 1 | `technotes/tn/Debugging Java Code With MacsBug` | 未开始 |
| 189 | Debugging Tips | 1 | `technotes/ov/Debugging Tips` | 未开始 |
| 190 | Debugging With PurgeMem and CompactMem | 1 | `technotes/ov/Debugging With PurgeMem and CompactMem` | 未开始 |
| 191 | Decomposing a QuickDraw GX Mapping | 1 | `technotes/tn/Decomposing a QuickDraw GX Mapping` | 未开始 |
| 192 | Decompressing DV frames and accessing the pixels | 1 | `technotes/tn/Decompressing DV frames and accessing the pixels` | 未开始 |
| 193 | Desktop Manager Q&As | 1 | `technotes/tb/Desktop Manager Q&As` | 未开始 |
| 194 | Desktop Printing Revealed | 1 | `technotes/tn/Desktop Printing Revealed` | 未开始 |
| 195 | Determining Which File System Is Active | 1 | `technotes/fl/Determining Which File System Is Active` | 未开始 |
| 196 | Device Management Overview Q&As | 1 | `technotes/dv/Device Management Overview Q&As` | 未开始 |
| 197 | Device Manager Q&As | 1 | `technotes/dv/Device Manager Q&As` | 未开始 |
| 198 | Device-Independent Printing | 1 | `technotes/pr/Device-Independent Printing` | 未开始 |
| 199 | Dialog Manager Helper Functions | 1 | `technotes/tn/Dialog Manager Helper Functions` | 未开始 |
| 200 | Dictionary Downloading | 1 | `technotes/pr/Dictionary Downloading` | 未开始 |
| 201 | Disabling Interrupts on the Traditional Mac OS | 1 | `technotes/tn/Disabling Interrupts on the Traditional Mac OS` | 未开始 |
| 202 | Displaying Large PICT Files | 1 | `technotes/qd/Displaying Large PICT Files` | 未开始 |
| 203 | Docking Manager Q&As | 1 | `technotes/dv/Docking Manager Q&As` | 未开始 |
| 204 | Document Names and the Printing Manager | 1 | `technotes/pr/Document Names and the Printing Manager` | 未开始 |
| 205 | Don't Look at ioPosOffset for Devices | 1 | `technotes/fl/Don't Look at ioPosOffset for Devices` | 未开始 |
| 206 | Don't println to a Socket | 1 | `technotes/tn/Don't println to a Socket` | 未开始 |
| 207 | Drawing Characters into a Narrow GrafPort | 1 | `technotes/te/Drawing Characters into a Narrow GrafPort` | 未开始 |
| 208 | Drawing Icons | 1 | `technotes/qd/Drawing Icons` | 未开始 |
| 209 | Drawing Icons the System 7 Way | 1 | `technotes/qd/Drawing Icons the System 7 Way` | 未开始 |
| 210 | Drive Queue Elements | 1 | `technotes/dv/Drive Queue Elements` | 未开始 |
| 211 | Driver Education | 1 | `technotes/dv/Driver Education` | 未开始 |
| 212 | Driver Tuning on Panther or G5 | 1 | `technotes/tn/Driver Tuning on Panther or G5` | 未开始 |
| 213 | Drivers & DAs in Need of (a Good) Time | 1 | `technotes/dv/Drivers & DAs in Need of (a Good) Time` | 未开始 |
| 214 | Edition Manager Q&As | 1 | `technotes/ic/Edition Manager Q&As` | 未开始 |
| 215 | Error in FCBPBRec | 1 | `technotes/fl/Error in FCBPBRec` | 未开始 |
| 216 | Event Manager Q&As | 1 | `technotes/tb/Event Manager Q&As` | 未开始 |
| 217 | Every Picture [Comment] Tells Its Story, Don't It? | 1 | `technotes/qd/Every Picture -Comment- Tells Its Story, Don't It` | 未开始 |
| 218 | Exporting Movies for iPod, Apple TV, iPad and iPhone | 1 | `technotes/Exporting Movies for iPod, Apple TV, iPad and iPhone` | 未开始 |
| 219 | Extending and Controlling Sherlock | 1 | `technotes/tn/Extending and Controlling Sherlock` | 未开始 |
| 220 | Extending the Print Record for LaserWriter 8 | 1 | `technotes/tn/Extending the Print Record for LaserWriter 8` | 未开始 |
| 221 | Extension Manager 4.0 | 1 | `technotes/tn/Extension Manager 4.0` | 未开始 |
| 222 | FCBs, Now and Forever | 1 | `technotes/tn/FCBs, Now and Forever` | 未开始 |
| 223 | FPU Operations on Macintosh Quadra Computers | 1 | `technotes/hw/FPU Operations on Macintosh Quadra Computers` | 未开始 |
| 224 | Fear No SCSI | 1 | `technotes/dv/Fear No SCSI` | 未开始 |
| 225 | Feeder Fodder | 1 | `technotes/pr/Feeder Fodder` | 未开始 |
| 226 | File Manager Directory Handling Q&As | 1 | `technotes/fl/File Manager Directory Handling Q&As` | 未开始 |
| 227 | File Manager Overview Q&As | 1 | `technotes/fl/File Manager Overview Q&As` | 未开始 |
| 228 | File Manager Volume Handling Q&As | 1 | `technotes/fl/File Manager Volume Handling Q&As` | 未开始 |
| 229 | File Mapping in Mac OS 9.1 | 1 | `technotes/tn/File Mapping in Mac OS 9.1` | 未开始 |
| 230 | File Sharing Extension 7.6.1 | 1 | `technotes/nw/File Sharing Extension 7.6.1` | 未开始 |
| 231 | File Sharing and Shared Folders | 1 | `technotes/fl/File Sharing and Shared Folders` | 未开始 |
| 232 | Fill in the size field before calling ICMGetPixelFormatInfo | 1 | `technotes/Fill in the size field before calling ICMGetPixelFormatInfo.md` | 未开始 |
| 233 | FindDItem | 1 | `technotes/tb/FindDItem` | 未开始 |
| 234 | Finder Flags | 1 | `technotes/tb/Finder Flags` | 未开始 |
| 235 | Finder Icon Positioning and File Initialization | 1 | `technotes/tb/Finder Icon Positioning and File Initialization` | 未开始 |
| 236 | Finder Q&As | 1 | `technotes/tb/Finder Q&As` | 未开始 |
| 237 | Finding Drivers in the Unit Table | 1 | `technotes/dv/Finding Drivers in the Unit Table` | 未开始 |
| 238 | Fixed CLUT Devices and the Single Techno Nerd | 1 | `technotes/qd/Fixed CLUT Devices and the Single Techno Nerd` | 未开始 |
| 239 | Floppy Disk Interface Q&As | 1 | `technotes/hw/Floppy Disk Interface Q&As` | 未开始 |
| 240 | Fond of FONDs | 1 | `technotes/te/Fond of FONDs` | 未开始 |
| 241 | Font Family Numbers | 1 | `technotes/te/Font Family Numbers` | 未开始 |
| 242 | Font Height Tables | 1 | `technotes/te/Font Height Tables` | 未开始 |
| 243 | Font Manager Q&As | 1 | `technotes/te/Font Manager Q&As` | 未开始 |
| 244 | Font Names | 1 | `technotes/te/Font Names` | 未开始 |
| 245 | Fonts and the Script Manager | 1 | `technotes/te/Fonts and the Script Manager` | 未开始 |
| 246 | Forcing Floppy Disk Size to be Either 400K or 800K | 1 | `technotes/dv/Forcing Floppy Disk Size to be Either 400K or 800K` | 未开始 |
| 247 | Frequently Asked Text Services Manager (TSM) Questions | 1 | `technotes/tn2005/Frequently Asked Text Services Manager (TSM) Questions` | 未开始 |
| 248 | Full Screen changes in QuickTime 6.1 and 6.3 | 1 | `technotes/tn2002/Full Screen changes in QuickTime 6.1 and 6.3` | 未开始 |
| 249 | Gestalt & _SysEnvirons - A Never-Ending Story | 1 | `technotes/ov/Gestalt & SysEnvirons - A Never-Ending Story` | 未开始 |
| 250 | Gestalt Manager Q&As | 1 | `technotes/os/Gestalt Manager Q&As` | 未开始 |
| 251 | GetNextEvent; Blinking Apple Menu | 1 | `technotes/tb/GetNextEvent; Blinking Apple Menu` | 未开始 |
| 252 | Getting a Full Pathname | 1 | `technotes/fl/Getting a Full Pathname` | 未开始 |
| 253 | Giving the (Desk)Hook to INITs | 1 | `technotes/os/Giving the (Desk)Hook to INITs` | 未开始 |
| 254 | Graphics Devices Manager Q&As | 1 | `technotes/dv/Graphics Devices Manager Q&As` | 未开始 |
| 255 | HFS Compatibility Guidelines | 1 | `technotes/fl/HFS Compatibility Guidelines` | 未开始 |
| 256 | HFS Elucidations Revisited | 1 | `technotes/tn/HFS Elucidations Revisited` | 未开始 |
| 257 | HFS Ruminations | 1 | `technotes/fl/HFS Ruminations` | 未开始 |
| 258 | HFS Tidbits | 1 | `technotes/fl/HFS Tidbits` | 未开始 |
| 259 | HIView APIs vs. Control Manager APIs | 1 | `technotes/tn2002/HIView APIs vs. Control Manager APIs` | 未开始 |
| 260 | Handles VS Pointers - Identity Crisis | 1 | `technotes/me/Handles VS Pointers - Identity Crisis` | 未开始 |
| 261 | Hard Disk Hacking | 1 | `technotes/dv/Hard Disk Hacking` | 未开始 |
| 262 | Help Manager Q&As | 1 | `technotes/tb/Help Manager Q&As` | 未开始 |
| 263 | Hey Buddy, Can You Spare A Block? | 1 | `technotes/fl/Hey Buddy, Can You Spare A Block` | 未开始 |
| 264 | High-Level AppleTalk Routines | 1 | `technotes/nw/High-Level AppleTalk Routines` | 未开始 |
| 265 | High-Speed SDRAM Design Considerations | 1 | `technotes/tn/High-Speed SDRAM Design Considerations` | 未开始 |
| 266 | How To Be a Good Multiple Users Citizen | 1 | `technotes/tn/How To Be a Good Multiple Users Citizen` | 未开始 |
| 267 | How To Produce Continuous Sound Without Clicking | 1 | `technotes/tb/How To Produce Continuous Sound Without Clicking` | 未开始 |
| 268 | How the Simple Network Management Protocol (SNMP) Manager Finds Network Cards | 1 | `technotes/nw/How the Simple Network Management Protocol (SNMP) Manager Finds Network Cards` | 未开始 |
| 269 | How to Construct Word-Break Tables | 1 | `technotes/te/How to Construct Word-Break Tables` | 未开始 |
| 270 | How to structure your handleCheckUpdate callback | 1 | `technotes/tn/How to structure your handleCheckUpdate callback` | 未开始 |
| 271 | How to use the ATSUI Low Level APIs to get glyph outlines | 1 | `technotes/tn/How to use the ATSUI Low Level APIs to get glyph outlines` | 未开始 |
| 272 | How to write a JDBC Plugin (With Example) | 1 | `technotes/tn/How to write a JDBC Plugin (With Example)` | 未开始 |
| 273 | ICM Drawing non-scheduled frames with QuickTime 6 | 1 | `technotes/ICM Drawing non-scheduled frames with QuickTime 6.md` | 未开始 |
| 274 | ISO 9660 (& High Sierra) CD-ROM Format | 1 | `technotes/fl/ISO 9660 (& High Sierra) CD-ROM Format` | 未开始 |
| 275 | Idling Movie Importers | 1 | `technotes/Idling Movie Importers.md` | 未开始 |
| 276 | ImageWriter II Paper Motion | 1 | `technotes/pr/ImageWriter II Paper Motion` | 未开始 |
| 277 | Importing animated GIFs | 1 | `technotes/tn/Importing animated GIFs` | 未开始 |
| 278 | Improving Windows Screen Updating with QuickTime for Windows Double-Buffering | 1 | `technotes/Improving Windows Screen Updating with QuickTime for Windows Double-Buffering Fe.md` | 未开始 |
| 279 | In Search of Missing Links | 1 | `technotes/tn/In Search of Missing Links` | 未开始 |
| 280 | In-App Purchase FAQ | 1 | `technotes/In-App Purchase FAQ.md` | 未开始 |
| 281 | InitGraf with MPW Assembly | 1 | `technotes/pt/InitGraf with MPW Assembly` | 未开始 |
| 282 | Inline Input for TextEdit with TSMTE | 1 | `technotes/te/Inline Input for TextEdit with TSMTE` | 未开始 |
| 283 | Inside Macintosh Text and Life Before 7.1 | 1 | `technotes/te/Inside Macintosh Text and Life Before 7.1` | 未开始 |
| 284 | Inside Object Pascal | 1 | `technotes/pt/Inside Object Pascal` | 未开始 |
| 285 | Insights on OpenGL | 1 | `technotes/tn/Insights on OpenGL` | 未开始 |
| 286 | Installer Q&As | 1 | `technotes/pt/Installer Q&As` | 未开始 |
| 287 | International Canceling | 1 | `technotes/te/International Canceling` | 未开始 |
| 288 | Internationalization Checklist | 1 | `technotes/ov/Internationalization Checklist` | 未开始 |
| 289 | Interrupt-Safe Routines | 1 | `technotes/tn/Interrupt-Safe Routines` | 未开始 |
| 290 | Interrupts in Need of (a Good) Time | 1 | `technotes/tn/Interrupts in Need of (a Good) Time` | 未开始 |
| 291 | Introducing the LaserWriter 8 Driver Version 8.6 | 1 | `technotes/tn/Introducing the LaserWriter 8 Driver Version 8.6` | 未开始 |
| 292 | Introducing the LaserWriter 8 Driver version 8.6.5 | 1 | `technotes/tn/Introducing the LaserWriter 8 Driver version 8.6.5` | 未开始 |
| 293 | Introducing the LaserWriter 8 Driver version 8.7 | 1 | `technotes/tn/Introducing the LaserWriter 8 Driver version 8.7` | 未开始 |
| 294 | Introducing the LaserWriter Driver Version 8.5.1 | 1 | `technotes/tn/Introducing the LaserWriter Driver Version 8.5.1` | 未开始 |
| 295 | Introduction to MRJ Scripting with AppleScript for Java | 1 | `technotes/tn/Introduction to MRJ Scripting with AppleScript for Java` | 未开始 |
| 296 | JIS Keyboard Support in Mac OS 8 | 1 | `technotes/tn/JIS Keyboard Support in Mac OS 8` | 未开始 |
| 297 | Keyboard Resource Q&As | 1 | `technotes/te/Keyboard Resource Q&As` | 未开始 |
| 298 | KillNBP Clarification | 1 | `technotes/nw/KillNBP Clarification` | 未开始 |
| 299 | Large-Screen Display Compatibility | 1 | `technotes/ov/Large-Screen Display Compatibility` | 未开始 |
| 300 | LaserWriter 8.6 and Fonts | 1 | `technotes/tn/LaserWriter 8.6 and Fonts` | 未开始 |
| 301 | LaserWriter 8.6.5 Job Log Format | 1 | `technotes/tn/LaserWriter 8.6.5 Job Log Format` | 未开始 |
| 302 | LaserWriter Driver Surprises in 5.0 and Newer | 1 | `technotes/pr/LaserWriter Driver Surprises in 5.0 and Newer` | 未开始 |
| 303 | LaserWriter Optimization Techniques | 1 | `technotes/pr/LaserWriter Optimization Techniques` | 未开始 |
| 304 | LaserWriter ROMs Bugs | 1 | `technotes/pr/LaserWriter ROMs Bugs` | 未开始 |
| 305 | LaserWriter Utility Q&As | 1 | `technotes/qd/LaserWriter Utility Q&As` | 未开始 |
| 306 | Life With Font/DA Mover--Desk Accessories | 1 | `technotes/pt/Life With Font-DA Mover--Desk Accessories` | 未开始 |
| 307 | Link Access Protocol Q&As | 1 | `technotes/nw/Link Access Protocol Q&As` | 未开始 |
| 308 | List Manager Q&As | 1 | `technotes/tb/List Manager Q&As` | 未开始 |
| 309 | Little PowerBook in Slumberland | 1 | `technotes/hw/Little PowerBook in Slumberland` | 未开始 |
| 310 | Loading Components Bug | 1 | `technotes/qt/Loading Components Bug` | 未开始 |
| 311 | Lock, Unlock the Range | 1 | `technotes/fl/Lock, Unlock the Range` | 未开始 |
| 312 | Locking and Unlocking Handles | 1 | `technotes/tn/Locking and Unlocking Handles` | 未开始 |
| 313 | MP-Safe Routines | 1 | `technotes/tn/MP-Safe Routines` | 未开始 |
| 314 | MPW 2.0.2 Bugs | 1 | `technotes/pt/MPW 2.0.2 Bugs` | 未开始 |
| 315 | MPW Assembler Q&As | 1 | `technotes/pt/MPW Assembler Q&As` | 未开始 |
| 316 | MPW C++ Q&As | 1 | `technotes/pt/MPW C++ Q&As` | 未开始 |
| 317 | MPW Library Q&As | 1 | `technotes/pt/MPW Library Q&As` | 未开始 |
| 318 | MPW Object Pascal Without MacApp | 1 | `technotes/pt/MPW Object Pascal Without MacApp` | 未开始 |
| 319 | MPW Pascal Q&As | 1 | `technotes/pt/MPW Pascal Q&As` | 未开始 |
| 320 | MPW Q&As | 1 | `technotes/pt/MPW Q&As` | 未开始 |
| 321 | MPW's -mc68881 Option | 1 | `technotes/pt/MPW's -mc68881 Option` | 未开始 |
| 322 | Mac OS 7.6 | 1 | `technotes/tn/Mac OS 7.6` | 未开始 |
| 323 | Mac OS 7.6.1 | 1 | `technotes/tn/Mac OS 7.6.1` | 未开始 |
| 324 | Mac OS 8 | 1 | `technotes/tn/Mac OS 8` | 未开始 |
| 325 | Mac OS 8.1 | 1 | `technotes/tn/Mac OS 8.1` | 未开始 |
| 326 | Mac OS 8.5 | 1 | `technotes/tn/Mac OS 8.5` | 未开始 |
| 327 | Mac OS 8.6 | 1 | `technotes/tn/Mac OS 8.6` | 未开始 |
| 328 | Mac OS 9 | 1 | `technotes/tn/Mac OS 9` | 未开始 |
| 329 | Mac OS 9.0.4 | 1 | `technotes/tn/Mac OS 9.0.4` | 未开始 |
| 330 | Mac OS 9.1 | 1 | `technotes/tn/Mac OS 9.1` | 未开始 |
| 331 | Mac OS X 10.2 | 1 | `technotes/tn2002/Mac OS X 10.2` | 未开始 |
| 332 | Mac OS X 10.3 Navigation Services Changes | 1 | `technotes/Mac OS X 10.3 Navigation Services Changes.md` | 未开始 |
| 333 | Mac OS X QuickDraw Performance | 1 | `technotes/tn/Mac OS X QuickDraw Performance` | 未开始 |
| 334 | Mac OS X v10.1 | 1 | `technotes/tn/Mac OS X v10.1` | 未开始 |
| 335 | MacApp 'View' Adventure Game | 1 | `technotes/pt/MacApp 'View' Adventure Game` | 未开始 |
| 336 | MacApp Q&As | 1 | `technotes/pt/MacApp Q&As` | 未开始 |
| 337 | MacApp Segmentation Illuminations | 1 | `technotes/pt/MacApp Segmentation Illuminations` | 未开始 |
| 338 | MacPaint Document Format | 1 | `technotes/pt/MacPaint Document Format` | 未开始 |
| 339 | MacTCP Q&As | 1 | `technotes/nw/MacTCP Q&As` | 未开始 |
| 340 | MacinTalk - The Final Chapter | 1 | `technotes/pt/MacinTalk - The Final Chapter` | 未开始 |
| 341 | Macintosh 21" Color Display Technical Specifications | 1 | `technotes/hw/Macintosh 21- Color Display Technical Specifications` | 未开始 |
| 342 | Macintosh Memory Configurations | 1 | `technotes/hw/Macintosh Memory Configurations` | 未开始 |
| 343 | Macintosh Plus Pinouts | 1 | `technotes/hw/Macintosh Plus Pinouts` | 未开始 |
| 344 | Macintosh Plus ROM Versions | 1 | `technotes/hw/Macintosh Plus ROM Versions` | 未开始 |
| 345 | Macintosh Portable PDS Development | 1 | `technotes/hw/Macintosh Portable PDS Development` | 未开始 |
| 346 | Macintosh Portable ROM Expansion | 1 | `technotes/hw/Macintosh Portable ROM Expansion` | 未开始 |
| 347 | Macintosh Protocol Package Q&As | 1 | `technotes/nw/Macintosh Protocol Package Q&As` | 未开始 |
| 348 | Macintosh Quadra Built-In Video | 1 | `technotes/hw/Macintosh Quadra Built-In Video` | 未开始 |
| 349 | Macintosh SE/30 Info | 1 | `technotes/hw/Macintosh SE-30 Info` | 未开始 |
| 350 | MacsBug Q&As | 1 | `technotes/pt/MacsBug Q&As` | 未开始 |
| 351 | Managerial Abuse | 1 | `technotes/ov/Managerial Abuse` | 未开始 |
| 352 | Managing QTCompressionOptions - An overview of the QTCompressionOptionsWindow | 1 | `technotes/Managing QTCompressionOptions - An overview of the QTCompressionOptionsWindow sa` | 未开始 |
| 353 | Math Function Q&As | 1 | `technotes/os/Math Function Q&As` | 未开始 |
| 354 | MaxApplZone and MoveHHi from Assembly Language | 1 | `technotes/me/MaxApplZone and MoveHHi from Assembly Language` | 未开始 |
| 355 | Maximum Number of Resources in a File | 1 | `technotes/tb/Maximum Number of Resources in a File` | 未开始 |
| 356 | Memory Allocation Recommendations on Mac OS X | 1 | `technotes/Memory Allocation Recommendations on Mac OS X.md` | 未开始 |
| 357 | Memory Hardware Q&As | 1 | `technotes/hw/Memory Hardware Q&As` | 未开始 |
| 358 | Memory Management Overview Q&As | 1 | `technotes/me/Memory Management Overview Q&As` | 未开始 |
| 359 | Memory Manager Compatibility | 1 | `technotes/me/Memory Manager Compatibility` | 未开始 |
| 360 | Memory Manager Q&As | 1 | `technotes/me/Memory Manager Q&As` | 未开始 |
| 361 | Migrating to FSRefs & long Unicode names from FSSpecs | 1 | `technotes/Migrating to FSRefs & long Unicode names from FSSpecs.md` | 未开始 |
| 362 | Miscellaneous Tool Q&As | 1 | `technotes/pt/Miscellaneous Tool Q&As` | 未开始 |
| 363 | Mixing HFS and C File I/O | 1 | `technotes/fl/Mixing HFS and C File I-O` | 未开始 |
| 364 | Modifying the Standard String Comparison | 1 | `technotes/te/Modifying the Standard String Comparison` | 未开始 |
| 365 | Movable Modal Dialogs | 1 | `technotes/tb/Movable Modal Dialogs` | 未开始 |
| 366 | MoveHHi and SetResPurge | 1 | `technotes/me/MoveHHi and SetResPurge` | 未开始 |
| 367 | Movie Data Security | 1 | `technotes/tn/Movie Data Security` | 未开始 |
| 368 | Movie Toolbox Q&As | 1 | `technotes/qt/Movie Toolbox Q&As` | 未开始 |
| 369 | Movies `LOOP' Atom and Friends | 1 | `technotes/qt/Movies `LOOP' Atom and Friends` | 未开始 |
| 370 | Moving Your Code to Mac OS X | 1 | `technotes/tn/Moving Your Code to Mac OS X` | 未开始 |
| 371 | Multi-Buffer Aware Image Decompressors | 1 | `technotes/Multi-Buffer Aware Image Decompressors.md` | 未开始 |
| 372 | MultiFinder Frequently Asked Questions | 1 | `technotes/tb/MultiFinder Frequently Asked Questions` | 未开始 |
| 373 | MultiFinder Miscellanea | 1 | `technotes/tb/MultiFinder Miscellanea` | 未开始 |
| 374 | MultiFinder and _SetGrowZone | 1 | `technotes/me/MultiFinder and SetGrowZone` | 未开始 |
| 375 | Multilingual Text Engine Frequently Asked Questions | 1 | `technotes/Multilingual Text Engine Frequently Asked Questions.md` | 未开始 |
| 376 | Name Binding Protocol Q&As | 1 | `technotes/nw/Name Binding Protocol Q&As` | 未开始 |
| 377 | Networking and Multitasking | 1 | `technotes/Networking and Multitasking.md` | 未开始 |
| 378 | New Resource Manager Calls | 1 | `technotes/tb/New Resource Manager Calls` | 未开始 |
| 379 | New Sound Input Driver Features | 1 | `technotes/tn/New Sound Input Driver Features` | 未开始 |
| 380 | NewGWorlds in VRAM and AGP Memory | 1 | `technotes/tn/NewGWorlds in VRAM and AGP Memory` | 未开始 |
| 381 | Notification Manager Q&As | 1 | `technotes/ps/Notification Manager Q&As` | 未开始 |
| 382 | NuBus Block Transfer Mode sResource Entries | 1 | `technotes/hw/NuBus Block Transfer Mode sResource Entries` | 未开始 |
| 383 | NuBus Expansion Interface Q&As | 1 | `technotes/hw/NuBus Expansion Interface Q&As` | 未开始 |
| 384 | NuBus Interrupt Latency (I Was a Teenage DMA Junkie) | 1 | `technotes/hw/NuBus Interrupt Latency (I Was a Teenage DMA Junkie)` | 未开始 |
| 385 | NuBus Physical Designs - Beware | 1 | `technotes/hw/NuBus Physical Designs - Beware` | 未开始 |
| 386 | NuBus Power Allocation | 1 | `technotes/hw/NuBus Power Allocation` | 未开始 |
| 387 | Nulls in Filenames | 1 | `technotes/fl/Nulls in Filenames` | 未开始 |
| 388 | Object Support Library Version History | 1 | `technotes/tn/Object Support Library Version History` | 未开始 |
| 389 | Of Time and Space and _CopyBits | 1 | `technotes/qd/Of Time and Space and CopyBits` | 未开始 |
| 390 | Old-Style Colors | 1 | `technotes/qd/Old-Style Colors` | 未开始 |
| 391 | OmegaSANE | 1 | `technotes/os/OmegaSANE` | 未开始 |
| 392 | On Drag Manager Additions (Release 1.1) | 1 | `technotes/tn/On Drag Manager Additions (Release 1.1)` | 未开始 |
| 393 | On Improving Open Transport Network Server Performance | 1 | `technotes/tn/On Improving Open Transport Network Server Performance` | 未开始 |
| 394 | On Multiple Inheritance & HandleObjects | 1 | `technotes/tn/On Multiple Inheritance & HandleObjects` | 未开始 |
| 395 | On Power Macintosh Interrupt Management | 1 | `technotes/tn/On Power Macintosh Interrupt Management` | 未开始 |
| 396 | On QuickTime Component Manager 3.0 & PowerPC Native Components | 1 | `technotes/tn/On QuickTime Component Manager 3.0 & PowerPC Native Components` | 未开始 |
| 397 | On the Deferred Task Manager | 1 | `technotes/tn/On the Deferred Task Manager` | 未开始 |
| 398 | Open Transport STREAMS FAQ | 1 | `technotes/tn/Open Transport STREAMS FAQ` | 未开始 |
| 399 | OpenGL Release Highlights - Mac OS X 10.3 Panther | 1 | `technotes/OpenGL Release Highlights - Mac OS X 10.3 Panther.md` | 未开始 |
| 400 | Opening AppleTalk | 1 | `technotes/nw/Opening AppleTalk` | 未开始 |
| 401 | Opening Resource Files Twice Considered Hard? | 1 | `technotes/tn/Opening Resource Files Twice Considered Hard` | 未开始 |
| 402 | Opening the Serial Driver | 1 | `technotes/dv/Opening the Serial Driver` | 未开始 |
| 403 | Optimization Strategies for Mac OS X | 1 | `technotes/tn/Optimization Strategies for Mac OS X` | 未开始 |
| 404 | Optimizing QD3D 1.5.3 Apps For Maximum Performance | 1 | `technotes/tn/Optimizing QD3D 1.5.3 Apps For Maximum Performance` | 未开始 |
| 405 | Our Checksum Bounced | 1 | `technotes/dv/Our Checksum Bounced` | 未开始 |
| 406 | Owned Resource Shortcuts | 1 | `technotes/tb/Owned Resource Shortcuts` | 未开始 |
| 407 | PAP Status Buffer | 1 | `technotes/nw/PAP Status Buffer` | 未开始 |
| 408 | PBHSetVol is Dangerous | 1 | `technotes/fl/PBHSetVol is Dangerous` | 未开始 |
| 409 | PBShare, PBUnshare, and PBGetUGEntry | 1 | `technotes/fl/PBShare, PBUnshare, and PBGetUGEntry` | 未开始 |
| 410 | PDS Expansion Interface Q&As | 1 | `technotes/hw/PDS Expansion Interface Q&As` | 未开始 |
| 411 | PPC Toolbox Q&As | 1 | `technotes/ic/PPC Toolbox Q&As` | 未开始 |
| 412 | Packages in Mac OS 9 | 1 | `technotes/tn/Packages in Mac OS 9` | 未开始 |
| 413 | Palette Manager Q&As | 1 | `technotes/qd/Palette Manager Q&As` | 未开始 |
| 414 | Palette Manager Tidbits | 1 | `technotes/tn/Palette Manager Tidbits` | 未开始 |
| 415 | Partial Resource Myths and Legends | 1 | `technotes/tb/Partial Resource Myths and Legends` | 未开始 |
| 416 | Pascal Routines Passed by Pointer | 1 | `technotes/pt/Pascal Routines Passed by Pointer` | 未开始 |
| 417 | Passbook FAQ | 1 | `technotes/Passbook FAQ.md` | 未开始 |
| 418 | Pending Update Perils | 1 | `technotes/tn/Pending Update Perils` | 未开始 |
| 419 | Performance Tuning with Development Tools | 1 | `technotes/pt/Performance Tuning with Development Tools` | 未开始 |
| 420 | Picture Utility Q&As | 1 | `technotes/qd/Picture Utility Q&As` | 未开始 |
| 421 | Pictures and Clip Regions | 1 | `technotes/qd/Pictures and Clip Regions` | 未开始 |
| 422 | Pinouts | 1 | `technotes/hw/Pinouts` | 未开始 |
| 423 | Position-Independent PostScript | 1 | `technotes/pr/Position-Independent PostScript` | 未开始 |
| 424 | PostScript Output Filters for LaserWriter 8.7 | 1 | `technotes/tn/PostScript Output Filters for LaserWriter 8.7` | 未开始 |
| 425 | PostScript Q&As | 1 | `technotes/pr/PostScript Q&As` | 未开始 |
| 426 | Power Management & PC Card Manager 3.0 | 1 | `technotes/tn/Power Management & PC Card Manager 3.0` | 未开始 |
| 427 | Power Management & The Energy Saver API | 1 | `technotes/tn/Power Management & The Energy Saver API` | 未开始 |
| 428 | Power Manager 2.0 | 1 | `technotes/tn/Power Manager 2.0` | 未开始 |
| 429 | Power Manager Q&As | 1 | `technotes/dv/Power Manager Q&As` | 未开始 |
| 430 | Power Supply Q&As | 1 | `technotes/hw/Power Supply Q&As` | 未开始 |
| 431 | PowerBook Miscellanea (Cold Serial in the Morning) | 1 | `technotes/hw/PowerBook Miscellanea (Cold Serial in the Morning)` | 未开始 |
| 432 | PowerPC Compatibility and Performance Issues | 1 | `technotes/pt/PowerPC Compatibility and Performance Issues` | 未开始 |
| 433 | PowerPC G5 Performance Primer | 1 | `technotes/tn/PowerPC G5 Performance Primer` | 未开始 |
| 434 | PrGeneral | 1 | `technotes/pr/PrGeneral` | 未开始 |
| 435 | PrGeneral Bug | 1 | `technotes/pr/PrGeneral Bug` | 未开始 |
| 436 | Principia Off-Screen Graphics Environments | 1 | `technotes/qd/Principia Off-Screen Graphics Environments` | 未开始 |
| 437 | PrintMonitor Q&As | 1 | `technotes/pr/PrintMonitor Q&As` | 未开始 |
| 438 | Printer Access Protocol Q&As | 1 | `technotes/nw/Printer Access Protocol Q&As` | 未开始 |
| 439 | Printer Direct Mode APIs for Macintosh Printer Drivers | 1 | `technotes/tn/Printer Direct Mode APIs for Macintosh Printer Drivers` | 未开始 |
| 440 | Printer Driver Q&As | 1 | `technotes/pr/Printer Driver Q&As` | 未开始 |
| 441 | Printing Manager Q&As | 1 | `technotes/pr/Printing Manager Q&As` | 未开始 |
| 442 | Problem with GetVInfo | 1 | `technotes/fl/Problem with GetVInfo` | 未开始 |
| 443 | Problem with WaitNextEvent in MultiFinder 1.0 | 1 | `technotes/tb/Problem with WaitNextEvent in MultiFinder 1.0` | 未开始 |
| 444 | Process Manager Q&As | 1 | `technotes/ps/Process Manager Q&As` | 未开始 |
| 445 | Processors & General Logic Q&As | 1 | `technotes/hw/Processors & General Logic Q&As` | 未开始 |
| 446 | Projector Q&As | 1 | `technotes/pt/Projector Q&As` | 未开始 |
| 447 | Querying PostScript Printers at dtp Creation Time the QuickDraw GX Way | 1 | `technotes/tn/Querying PostScript Printers at dtp Creation Time the QuickDraw GX Way` | 未开始 |
| 448 | QuickDraw GX Printing Q&As | 1 | `technotes/pr/QuickDraw GX Printing Q&As` | 未开始 |
| 449 | QuickDraw GX Q&As | 1 | `technotes/qd/QuickDraw GX Q&As` | 未开始 |
| 450 | QuickDraw's Internal Picture Definition | 1 | `technotes/qd/QuickDraw's Internal Picture Definition` | 未开始 |
| 451 | QuickTime 1.6.1 Features | 1 | `technotes/qt/QuickTime 1.6.1 Features` | 未开始 |
| 452 | QuickTime 3.0.2 | 1 | `technotes/tn/QuickTime 3.0.2` | 未开始 |
| 453 | QuickTime 4.0.3 | 1 | `technotes/tn/QuickTime 4.0.3` | 未开始 |
| 454 | QuickTime 4.1.1/4.1.2 | 1 | `technotes/tn/QuickTime 4.1.1-4.1.2` | 未开始 |
| 455 | QuickTime Overview Q&As | 1 | `technotes/qt/QuickTime Overview Q&As` | 未开始 |
| 456 | QuickTime TV Tuner APIs | 1 | `technotes/tn/QuickTime TV Tuner APIs` | 未开始 |
| 457 | QuickTime Teletext Component APIs | 1 | `technotes/tn/QuickTime Teletext Component APIs` | 未开始 |
| 458 | QuickTime VR 1.0 Object Movie File Format | 1 | `technotes/tn/QuickTime VR 1.0 Object Movie File Format` | 未开始 |
| 459 | QuickTime VR 1.0 Panorama Movie File Format | 1 | `technotes/tn/QuickTime VR 1.0 Panorama Movie File Format` | 未开始 |
| 460 | QuickTime for Windows ActiveX/COM Frequently Asked Questions | 1 | `technotes/QuickTime for Windows ActiveX-COM Frequently Asked Questions.md` | 未开始 |
| 461 | QuickTime for Windows Q&As | 1 | `technotes/qt/QuickTime for Windows Q&As` | 未开始 |
| 462 | Register A5 Within GrowZone Functions | 1 | `technotes/me/Register A5 Within GrowZone Functions` | 未开始 |
| 463 | RegisterName | 1 | `technotes/nw/RegisterName` | 未开始 |
| 464 | ResEdit Q&As | 1 | `technotes/pt/ResEdit Q&As` | 未开始 |
| 465 | Reserved Resource Types | 1 | `technotes/tb/Reserved Resource Types` | 未开始 |
| 466 | Resource Manager Q&As | 1 | `technotes/tb/Resource Manager Q&As` | 未开始 |
| 467 | Resource Manager Tips | 1 | `technotes/tb/Resource Manager Tips` | 未开始 |
| 468 | Resource in CDEV? | 1 | `technotes/ov/Resource in CDEV` | 未开始 |
| 469 | Resources Contained in the Desktop File | 1 | `technotes/tb/Resources Contained in the Desktop File` | 未开始 |
| 470 | Routes From the Source | 1 | `technotes/nw/Routes From the Source` | 未开始 |
| 471 | Routing Table Maintenance Protocol Q&As | 1 | `technotes/nw/Routing Table Maintenance Protocol Q&As` | 未开始 |
| 472 | Running files from a hard drive in Open Firmware | 1 | `technotes/tn/Running files from a hard drive in Open Firmware` | 未开始 |
| 473 | SADE Q&As | 1 | `technotes/pt/SADE Q&As` | 未开始 |
| 474 | SCSI Bugs | 1 | `technotes/dv/SCSI Bugs` | 未开始 |
| 475 | SCSI Manager Q&As | 1 | `technotes/dv/SCSI Manager Q&As` | 未开始 |
| 476 | SCSI Port Q&As | 1 | `technotes/hw/SCSI Port Q&As` | 未开始 |
| 477 | SCSI Termination | 1 | `technotes/dv/SCSI Termination` | 未开始 |
| 478 | SNMP Transports | 1 | `technotes/nw/SNMP Transports` | 未开始 |
| 479 | Safe cdevs | 1 | `technotes/te/Safe cdevs` | 未开始 |
| 480 | Scrap Manager Q&As | 1 | `technotes/tb/Scrap Manager Q&As` | 未开始 |
| 481 | Scrapbook File Format | 1 | `technotes/tb/Scrapbook File Format` | 未开始 |
| 482 | Scribbling Into AWT Components | 1 | `technotes/tn/Scribbling Into AWT Components` | 未开始 |
| 483 | Script Manager 2.0 Date & Time Problems | 1 | `technotes/te/Script Manager 2.0 Date & Time Problems` | 未开始 |
| 484 | Script Manager Print Action Routine | 1 | `technotes/te/Script Manager Print Action Routine` | 未开始 |
| 485 | Script Manager Q&As | 1 | `technotes/te/Script Manager Q&As` | 未开始 |
| 486 | Script Manager Q&As | 1 | `technotes/ic/Script Manager Q&As` | 未开始 |
| 487 | Script Manager's Pixel2Char Routine | 1 | `technotes/te/Script Manager's Pixel2Char Routine` | 未开始 |
| 488 | Searching Volumes - Solutions and Problems | 1 | `technotes/fl/Searching Volumes - Solutions and Problems` | 未开始 |
| 489 | Sense Lines | 1 | `technotes/hw/Sense Lines` | 未开始 |
| 490 | Separate Resource Files | 1 | `technotes/tb/Separate Resource Files` | 未开始 |
| 491 | Serial GPi (General-Purpose Input) | 1 | `technotes/dv/Serial GPi (General-Purpose Input)` | 未开始 |
| 492 | Serial I/O Port Q&As | 1 | `technotes/hw/Serial I-O Port Q&As` | 未开始 |
| 493 | Serial PollProc | 1 | `technotes/dv/Serial PollProc` | 未开始 |
| 494 | Serial Port Apocrypha | 1 | `technotes/tn/Serial Port Apocrypha` | 未开始 |
| 495 | SetLineWidth Revealed | 1 | `technotes/pr/SetLineWidth Revealed` | 未开始 |
| 496 | Setting and Restoring A5 | 1 | `technotes/ov/Setting and Restoring A5` | 未开始 |
| 497 | Setting ioFDirIndex in PBGetCatInfo Calls | 1 | `technotes/fl/Setting ioFDirIndex in PBGetCatInfo Calls` | 未开始 |
| 498 | Sherlock's Find By Content Library | 1 | `technotes/tn/Sherlock's Find By Content Library` | 未开始 |
| 499 | Sherlock's Find by Content Text Extractor Plug-ins | 1 | `technotes/tn/Sherlock's Find by Content Text Extractor Plug-ins` | 未开始 |
| 500 | Sleep Queue Tasks | 1 | `technotes/hw/Sleep Queue Tasks` | 未开始 |
| 501 | Slot Interrupt Prio-Technics | 1 | `technotes/hw/Slot Interrupt Prio-Technics` | 未开始 |
| 502 | Slot Manager Q&As | 1 | `technotes/dv/Slot Manager Q&As` | 未开始 |
| 503 | Smoothing Fonts | 1 | `technotes/tn/Smoothing Fonts` | 未开始 |
| 504 | SndPlayDoubleBuffer and Carbon | 1 | `technotes/tn/SndPlayDoubleBuffer and Carbon` | 未开始 |
| 505 | Sound Input Q&As | 1 | `technotes/tb/Sound Input Q&As` | 未开始 |
| 506 | Sound Manager Q&As | 1 | `technotes/tb/Sound Manager Q&As` | 未开始 |
| 507 | Speedy the Math Coprocessor | 1 | `technotes/hw/Speedy the Math Coprocessor` | 未开始 |
| 508 | Spooler Queries? | 1 | `technotes/pr/Spooler Queries` | 未开始 |
| 509 | Stand-Alone Code, ad nauseam | 1 | `technotes/pt/Stand-Alone Code, ad nauseam` | 未开始 |
| 510 | Standard File Customization | 1 | `technotes/fl/Standard File Customization` | 未开始 |
| 511 | Standard File Package Q&As | 1 | `technotes/fl/Standard File Package Q&As` | 未开始 |
| 512 | Standard File Tips | 1 | `technotes/fl/Standard File Tips` | 未开始 |
| 513 | Start Manager Extension Table Mechanism | 1 | `technotes/tn/Start Manager Extension Table Mechanism` | 未开始 |
| 514 | Stationery Pads | 1 | `technotes/ov/Stationery Pads` | 未开始 |
| 515 | Strategies for Dealing with Low-Memory Conditions | 1 | `technotes/tn/Strategies for Dealing with Low-Memory Conditions` | 未开始 |
| 516 | Strip With _OpenResFile and _OpenRFPerm | 1 | `technotes/tb/Strip With OpenResFile and OpenRFPerm` | 未开始 |
| 517 | Styled TextEdit Changes in System 6.0 | 1 | `technotes/te/Styled TextEdit Changes in System 6.0` | 未开始 |
| 518 | Suppliers for Macintosh II Board Developers | 1 | `technotes/hw/Suppliers for Macintosh II Board Developers` | 未开始 |
| 519 | Supplying codec-specific options within the Standard Compression Dialog | 1 | `technotes/Supplying codec-specific options within the Standard Compression Dialog` | 未开始 |
| 520 | Supported Countries for CLGeocoder | 1 | `technotes/Supported Countries for CLGeocoder.md` | 未开始 |
| 521 | Supporting Plug-in Rendereds in QD3D 1.5.3 Applications | 1 | `technotes/tn/Supporting Plug-in Rendereds in QD3D 1.5.3 Applications` | 未开始 |
| 522 | System 7.5 Update 2.0; System 7.5.3 | 1 | `technotes/tn/System 7.5 Update 2.0; System 7.5.3` | 未开始 |
| 523 | System 7.5.3 Revision 2 | 1 | `technotes/tn/System 7.5.3 Revision 2` | 未开始 |
| 524 | System 7.5.5 | 1 | `technotes/tn/System 7.5.5` | 未开始 |
| 525 | System Error 33, "zcbFree has gone negative" | 1 | `technotes/me/System Error 33, -zcbFree has gone negative` | 未开始 |
| 526 | System Software Utility Q&As | 1 | `technotes/pt/System Software Utility Q&As` | 未开始 |
| 527 | TEScroll Bug | 1 | `technotes/te/TEScroll Bug` | 未开始 |
| 528 | Tagging Handle and Pointer Data References in QuickTime | 1 | `technotes/Tagging Handle and Pointer Data References in QuickTime` | 未开始 |
| 529 | Tailoring Java 1.3.1 Applications for Mac OS X | 1 | `technotes/tn/Tailoring Java 1.3.1 Applications for Mac OS X` | 未开始 |
| 530 | Text Services Manager Q&As | 1 | `technotes/te/Text Services Manager Q&As` | 未开始 |
| 531 | TextEdit EOL Ambiguity | 1 | `technotes/te/TextEdit EOL Ambiguity` | 未开始 |
| 532 | TextEdit Q&As | 1 | `technotes/te/TextEdit Q&As` | 未开始 |
| 533 | TextEdit Record Size Limitations Revisited | 1 | `technotes/te/TextEdit Record Size Limitations Revisited` | 未开始 |
| 534 | TextEdit Technicalities | 1 | `technotes/te/TextEdit Technicalities` | 未开始 |
| 535 | The 'plst' Resource | 1 | `technotes/The 'plst' Resource.md` | 未开始 |
| 536 | The Appearance of Text | 1 | `technotes/te/The Appearance of Text` | 未开始 |
| 537 | The Browser Control (aka That ListView Thing) | 1 | `technotes/tn/The Browser Control (aka That ListView Thing)` | 未开始 |
| 538 | The CGDirectDisplay API | 1 | `technotes/tn/The CGDirectDisplay API` | 未开始 |
| 539 | The Care And Feeding Of Runtime.exec | 1 | `technotes/tn/The Care And Feeding Of Runtime.exec` | 未开始 |
| 540 | The Compleat Guide To SimpleText | 1 | `technotes/tn/The Compleat Guide To SimpleText` | 未开始 |
| 541 | The Compleat Guide to TeachText | 1 | `technotes/pt/The Compleat Guide to TeachText` | 未开始 |
| 542 | The Desktop File's Outer Limits | 1 | `technotes/ov/The Desktop File's Outer Limits` | 未开始 |
| 543 | The Download Manager | 1 | `technotes/tn/The Download Manager` | 未开始 |
| 544 | The Effect of Spool-a-page/Print-a-page on Shared Printers | 1 | `technotes/pr/The Effect of Spool-a-page-Print-a-page on Shared Printers` | 未开始 |
| 545 | The Font Panel for Carbon API | 1 | `technotes/The Font Panel for Carbon API.md` | 未开始 |
| 546 | The Joy Of Being 32-Bit Clean | 1 | `technotes/ov/The Joy Of Being 32-Bit Clean` | 未开始 |
| 547 | The Mac OS X Font Manager | 1 | `technotes/tn/The Mac OS X Font Manager` | 未开始 |
| 548 | The Monster Disk Driver Technote | 1 | `technotes/tn/The Monster Disk Driver Technote` | 未开始 |
| 549 | The New Memory Manager and You | 1 | `technotes/me/The New Memory Manager and You` | 未开始 |
| 550 | The New PrGeneral Version Opcode | 1 | `technotes/tn/The New PrGeneral Version Opcode` | 未开始 |
| 551 | The Preferences Problem | 1 | `technotes/tn/The Preferences Problem` | 未开始 |
| 552 | The Printing Plug-ins Manager | 1 | `technotes/tn/The Printing Plug-ins Manager` | 未开始 |
| 553 | The Problem with & (Simple) Fix to Purgeable WDEFs | 1 | `technotes/tn/The Problem with & (Simple) Fix to Purgeable WDEFs` | 未开始 |
| 554 | Thread-Safe Toolbox Access From MRJ | 1 | `technotes/tn/Thread-Safe Toolbox Access From MRJ` | 未开始 |
| 555 | Threading Architectures | 1 | `technotes/tn/Threading Architectures` | 未开始 |
| 556 | Time Manager Q&As | 1 | `technotes/ps/Time Manager Q&As` | 未开始 |
| 557 | Token Ring Q&As | 1 | `technotes/nw/Token Ring Q&As` | 未开始 |
| 558 | TokenTalk Programmer's Guide Update | 1 | `technotes/nw/TokenTalk Programmer's Guide Update` | 未开始 |
| 559 | Toolbox Karma | 1 | `technotes/tb/Toolbox Karma` | 未开始 |
| 560 | Translation Manager 1.1 | 1 | `technotes/tb/Translation Manager 1.1` | 未开始 |
| 561 | TrueType Q&As | 1 | `technotes/te/TrueType Q&As` | 未开始 |
| 562 | USB Printer Sharing Compatibility | 1 | `technotes/tn/USB Printer Sharing Compatibility` | 未开始 |
| 563 | USB Software Locator | 1 | `technotes/tn/USB Software Locator` | 未开始 |
| 564 | Understanding Conic Splines | 1 | `technotes/tn/Understanding Conic Splines` | 未开始 |
| 565 | Understanding Open Transport Asset Tracking | 1 | `technotes/tn/Understanding Open Transport Asset Tracking` | 未开始 |
| 566 | Understanding Open Transport Memory Management | 1 | `technotes/tn/Understanding Open Transport Memory Management` | 未开始 |
| 567 | Understanding PCI Bus Performance | 1 | `technotes/tn/Understanding PCI Bus Performance` | 未开始 |
| 568 | Understanding PackBits | 1 | `technotes/tn/Understanding PackBits` | 未开始 |
| 569 | Understanding Type 11 & No FPU Installed Errors on the Power Macintosh | 1 | `technotes/tn/Understanding Type 11 & No FPU Installed Errors on the Power Macintosh` | 未开始 |
| 570 | Understanding the SerialDMA Driver | 1 | `technotes/tn/Understanding the SerialDMA Driver` | 未开始 |
| 571 | Unknown Sound Features | 1 | `technotes/tn/Unknown Sound Features` | 未开始 |
| 572 | Unlocking GDHandles Considered Harmful | 1 | `technotes/tn/Unlocking GDHandles Considered Harmful` | 未开始 |
| 573 | Updating Applications for QuickTime 6 | 1 | `technotes/Updating Applications for QuickTime 6` | 未开始 |
| 574 | Using Laser Prep Routines | 1 | `technotes/pr/Using Laser Prep Routines` | 未开始 |
| 575 | Using Low-Level Printing Calls With AppleTalk ImageWriters | 1 | `technotes/pr/Using Low-Level Printing Calls With AppleTalk ImageWriters` | 未开始 |
| 576 | Using MPW for Non-Macintosh 68000 Systems | 1 | `technotes/pt/Using MPW for Non-Macintosh 68000 Systems` | 未开始 |
| 577 | Using QuickDraw GX Functionality from Pascal or Modula-2 - Without Writing | 1 | `technotes/tn/Using QuickDraw GX Functionality from Pascal or Modula-2 - Without Writing Any C` | 未开始 |
| 578 | Using The GXGraphics Extension | 1 | `technotes/tn/Using The GXGraphics Extension` | 未开始 |
| 579 | Using a PurgeProc | 1 | `technotes/me/Using a PurgeProc` | 未开始 |
| 580 | Using the Drag Manager to Interact with and Manipulate File System Entities | 1 | `technotes/tn/Using the Drag Manager to Interact with and Manipulate File System Entities` | 未开始 |
| 581 | Using the QuickTime 64-bit Timecode Media Handler | 1 | `technotes/Using the QuickTime 64-bit Timecode Media Handler.md` | 未开始 |
| 582 | VIA IC Q&As | 1 | `technotes/hw/VIA IC Q&As` | 未开始 |
| 583 | Version Territory | 1 | `technotes/ov/Version Territory` | 未开始 |
| 584 | Video Hardware Q&As | 1 | `technotes/hw/Video Hardware Q&As` | 未开始 |
| 585 | Virtual Memory Application Compatibility | 1 | `technotes/tn/Virtual Memory Application Compatibility` | 未开始 |
| 586 | Virtual Memory Q&As | 1 | `technotes/me/Virtual Memory Q&As` | 未开始 |
| 587 | WMgrPortability | 1 | `technotes/tb/WMgrPortability` | 未开始 |
| 588 | Weak-Linking to a Code Fragment Manager-based Shared Library | 1 | `technotes/tn/Weak-Linking to a Code Fragment Manager-based Shared Library` | 未开始 |
| 589 | Where Have My Font Icons Gone? | 1 | `technotes/te/Where Have My Font Icons Gone` | 未开始 |
| 590 | Will Your AppleTalk Application Support Internets? | 1 | `technotes/nw/Will Your AppleTalk Application Support Internets` | 未开始 |
| 591 | Working with Multiprocessing Services | 1 | `technotes/tn/Working with Multiprocessing Services` | 未开始 |
| 592 | WorldScript Q&As | 1 | `technotes/te/WorldScript Q&As` | 未开始 |
| 593 | Worldwide Overview Q&As | 1 | `technotes/ov/Worldwide Overview Q&As` | 未开始 |
| 594 | Writing Custom Hoses for LaserWriter 8.6 | 1 | `technotes/tn/Writing Custom Hoses for LaserWriter 8.6` | 未开始 |
| 595 | Writing PPD Files for Use With LaserWriter 8, version 8.4.1 | 1 | `technotes/tn/Writing PPD Files for Use With LaserWriter 8, version 8.4.1` | 未开始 |
| 596 | Writing Plug-ins for Desktop Printer Utility | 1 | `technotes/tn/Writing Plug-ins for Desktop Printer Utility` | 未开始 |
| 597 | X.25 and X.400 Q&As | 1 | `technotes/nw/X.25 and X.400 Q&As` | 未开始 |
| 598 | _AddDrive, _DrvrInstall, and _DrvrRemove | 1 | `technotes/dv/AddDrive, DrvrInstall, and DrvrRemove` | 未开始 |
| 599 | _PBClose the Barn Door | 1 | `technotes/dv/PBClose the Barn Door` | 未开始 |
| 600 | _ZoomWindow | 1 | `technotes/tb/ZoomWindow` | 未开始 |
| 601 | iAd Implementation Best Practices | 1 | `technotes/iAd Implementation Best Practices.md` | 未开始 |
| 602 | ioNamePtr in File Manager Calls | 1 | `technotes/fl/ioNamePtr in File Manager Calls` | 未开始 |
| 603 | pIdle Proc (or how to let users know what's going on during print time...) | 1 | `technotes/pr/pIdle Proc (or how to let users know what's going on during print time...)` | 未开始 |

### 音视频与特效（46 份，46 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 604 | 'Audio Units: Embedding a Carbon View in a Cocoa Window' | 1 | `technotes/Audio Units- Embedding a Carbon View in a Cocoa Window` | 未开始 |
| 605 | AAC Audio - Encoder Delay and Synchronization | 1 | `technotes/AAC Audio - Encoder Delay and Synchronization` | 未开始 |
| 606 | AUInstrumentBase changes for Mac OS X Lion | 1 | `technotes/AUInstrumentBase changes for Mac OS X Lion.md` | 未开始 |
| 607 | AUSampler - Controlling the Settings of the AUSampler in Real Time | 1 | `technotes/AUSampler - Controlling the Settings of the AUSampler in Real Time` | 未开始 |
| 608 | AUSampler - Loading Instruments | 1 | `technotes/AUSampler - Loading Instruments.md` | 未开始 |
| 609 | AV Foundation iOS Machine Readable Code Detection FAQ | 1 | `technotes/AV Foundation iOS Machine Readable Code Detection FAQ.md` | 未开始 |
| 610 | AVFoundation - Timecode Support with AVAssetWriter and AVAssetReader | 1 | `technotes/AVFoundation - Timecode Support with AVAssetWriter and AVAssetReader` | 未开始 |
| 611 | Audio Components and the Application Sandbox | 1 | `technotes/Audio Components and the Application Sandbox.md` | 未开始 |
| 612 | Audio Export - Encoding AAC Audio For MPEG-4 Export | 1 | `technotes/Audio Export - Encoding AAC Audio For MPEG-4 Export` | 未开始 |
| 613 | Audio Unit AUPlugIn - Updating an existing Audio Unit for OS X Lion and later | 1 | `technotes/Audio Unit AUPlugIn - Updating an existing Audio Unit for OS X Lion and later` | 未开始 |
| 614 | Audio Unit Development - Handling Audio Unit Events | 1 | `technotes/Audio Unit Development - Handling Audio Unit Events` | 未开始 |
| 615 | Audio Unit Host Sandboxing Guide | 1 | `technotes/Audio Unit Host Sandboxing Guide` | 未开始 |
| 616 | Audio Unit Validation Using the auval Tool | 1 | `technotes/Audio Unit Validation Using the auval Tool.md` | 未开始 |
| 617 | Audio Units - How to correctly save and restore Audio Unit presets. | 1 | `technotes/Audio Units - How to correctly save and restore Audio Unit presets.md` | 未开始 |
| 618 | Audio Units - The AudioUnit_IOKitUserClients info.plist key | 1 | `technotes/Audio Units - The AudioUnitIOKitUserClients info.plist key.md` | 未开始 |
| 619 | Bit Rate Control Modes for AAC Encoding | 1 | `technotes/Bit Rate Control Modes for AAC Encoding` | 未开始 |
| 620 | Creating Reference Movies - MakeRefMovie | 1 | `technotes/Creating Reference Movies - MakeRefMovie` | 未开始 |
| 621 | Creating media files for Apple TV that contain a Dolby Digital (AC-3) and/or | 1 | `technotes/Creating media files for Apple TV that contain a Dolby Digital (AC-3) and-or Dol.md` | 未开始 |
| 622 | Debugging AVFoundation Compositions, Video Compositions, and Audio Mixes | 1 | `technotes/Debugging AVFoundation Compositions, Video Compositions, and Audio Mixes` | 未开始 |
| 623 | Debugging HTTP Live Streaming | 1 | `technotes/Debugging HTTP Live Streaming.md` | 未开始 |
| 624 | Device input using the HAL Output Audio Unit | 1 | `technotes/Device input using the HAL Output Audio Unit` | 未开始 |
| 625 | Digital CD Audio | 1 | `technotes/tn/Digital CD Audio` | 未开始 |
| 626 | Evaluating an Application's Video Color | 1 | `technotes/Evaluating an Application's Video Color` | 未开始 |
| 627 | Handling Frame Drops with AVCaptureVideoDataOutput | 1 | `technotes/Handling Frame Drops with AVCaptureVideoDataOutput.md` | 未开始 |
| 628 | High-Efficiency Advanced Audio Coding (HE-AAC) | 1 | `technotes/High-Efficiency Advanced Audio Coding (HE-AAC).md` | 未开始 |
| 629 | Logic Pro X - Core Audio Device Properties Supported by Logic Pro X 10.1 | 1 | `technotes/Logic Pro X - Core Audio Device Properties Supported by Logic Pro X 10.1` | 未开始 |
| 630 | Media Stream Validator Tool Results Explained | 1 | `technotes/Media Stream Validator Tool Results Explained.md` | 未开始 |
| 631 | Moving Off Deprecated HAL APIs | 1 | `technotes/Moving Off Deprecated HAL APIs.md` | 未开始 |
| 632 | New AV Foundation APIs in OS X Yosemite for Professional Video Workflows | 1 | `technotes/New AV Foundation APIs in OS X Yosemite for Professional Video Workflows.md` | 未开始 |
| 633 | New AV Foundation Camera Features for the iPhone 6 and iPhone 6 Plus | 1 | `technotes/New AV Foundation Camera Features for the iPhone 6 and iPhone 6 Plus` | 未开始 |
| 634 | OpenAL FAQ for iPhone OS | 1 | `technotes/OpenAL FAQ for iPhone OS.md` | 未开始 |
| 635 | Optimizing Audio Unit User Experience in Logic Studio | 1 | `technotes/Optimizing Audio Unit User Experience in Logic Studio.md` | 未开始 |
| 636 | Playing a sound file using the Default Output Audio Unit | 1 | `technotes/Playing a sound file using the Default Output Audio Unit.md` | 未开始 |
| 637 | QTKit Frequently Asked Questions | 1 | `technotes/QTKit Frequently Asked Questions.md` | 未开始 |
| 638 | QuickTime - Rendering in Y'CbCr | 1 | `technotes/QuickTime - Rendering in Y'CbCr.md` | 未开始 |
| 639 | QuickTime Pixel Format Four Character Codes (FourCCs) | 1 | `technotes/QuickTime Pixel Format Four Character Codes (FourCCs).md` | 未开始 |
| 640 | Saving Power During Audio I/O - The kAudioHardwarePropertyPowerHint Property | 1 | `technotes/Saving Power During Audio I-O - The kAudioHardwarePropertyPowerHint Property.md` | 未开始 |
| 641 | The Sonogram View Demo Audio Unit | 1 | `technotes/The Sonogram View Demo Audio Unit` | 未开始 |
| 642 | The System Sound APIs for Mac OS X v10.2 through v10.4 | 1 | `technotes/The System Sound APIs for Mac OS X v10.2 through v10.4` | 未开始 |
| 643 | Thread-safe programming in QuickTime | 1 | `technotes/Thread-safe programming in QuickTime` | 未开始 |
| 644 | Transitioning QTKit Code to AV Foundation | 1 | `technotes/Transitioning QTKit Code to AV Foundation` | 未开始 |
| 645 | Uncompressed Y´CbCr Video in QuickTime Files | 1 | `technotes/Uncompressed Y´CbCr Video in QuickTime Files` | 未开始 |
| 646 | Using AudioDeviceRead in Mac OS 10.4 | 1 | `technotes/Using AudioDeviceRead in Mac OS 10.4.md` | 未开始 |
| 647 | Using the 3DMixer Audio Unit | 1 | `technotes/Using the 3DMixer Audio Unit` | 未开始 |
| 648 | Video Color Management in AV Foundation and QTKit | 1 | `technotes/Video Color Management in AV Foundation and QTKit` | 未开始 |
| 649 | Video Decode Acceleration Framework Reference | 1 | `technotes/Video Decode Acceleration Framework Reference.md` | 未开始 |

### 数据管理（25 份，25 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 650 | 'The Death of typeFSSpec: Moving Along to typeFileURL' | 1 | `technotes/The Death of typeFSSpec- Moving Along to typeFileURL` | 未开始 |
| 651 | Accessing Shared Data from an App Extension and its Containing App | 1 | `technotes/Accessing Shared Data from an App Extension and its Containing App.md` | 未开始 |
| 652 | Changes To App Containers In iOS 8 | 1 | `technotes/Changes To App Containers In iOS 8.md` | 未开始 |
| 653 | Daemons and Agents | 1 | `technotes/Daemons and Agents` | 未开始 |
| 654 | Data Management and Synchronization for Shared iPad | 1 | `technotes/Data Management and Synchronization for Shared iPad.md` | 未开始 |
| 655 | Debugging Case-Sensitivity Bugs in Applications | 1 | `technotes/Debugging Case-Sensitivity Bugs in Applications.md` | 未开始 |
| 656 | Exclusive File Access in Mac OS X | 1 | `technotes/tn/Exclusive File Access in Mac OS X` | 未开始 |
| 657 | File Manager File Handling Q&As | 1 | `technotes/fl/File Manager File Handling Q&As` | 未开始 |
| 658 | File Manager Performance and Caching | 1 | `technotes/fl/File Manager Performance and Caching` | 未开始 |
| 659 | Glyph Access Protocol | 1 | `technotes/Glyph Access Protocol` | 未开始 |
| 660 | HFS Plus Volume Format | 1 | `technotes/tn/HFS Plus Volume Format` | 未开始 |
| 661 | Handling version conflicts in the iCloud environment | 1 | `technotes/Handling version conflicts in the iCloud environment` | 未开始 |
| 662 | Locating Application Support Files under Mac OS X | 1 | `technotes/tn/Locating Application Support Files under Mac OS X` | 未开始 |
| 663 | Migrating to CloudKit | 1 | `technotes/Migrating to CloudKit.md` | 未开始 |
| 664 | Observing Process Lifetimes Without Polling | 1 | `technotes/Observing Process Lifetimes Without Polling.md` | 未开始 |
| 665 | Programmatic Mounting of AppleShare Volumes | 1 | `technotes/tn/Programmatic Mounting of AppleShare Volumes` | 未开始 |
| 666 | Remapping Keys in macOS 10.12 Sierra | 1 | `technotes/Remapping Keys in macOS 10.12 Sierra.md` | 未开始 |
| 667 | Resolving Alias Files Quietly | 1 | `technotes/fl/Resolving Alias Files Quietly` | 未开始 |
| 668 | Resolving Automatic Assessment Configuration (AAC) conflicts with Guided Access | 1 | `technotes/Resolving Automatic Assessment Configuration (AAC) conflicts with Guided Access.md` | 未开始 |
| 669 | Simple and Reliable Threading with NSOperation | 1 | `technotes/Simple and Reliable Threading with NSOperation` | 未开始 |
| 670 | Using Launch Services for discovering document binding and launching applications | 1 | `technotes/tn/Using Launch Services for discovering document binding and launching application` | 未开始 |
| 671 | Working with Default Data in Core Data Apps | 1 | `technotes/Working with Default Data in Core Data Apps.md` | 未开始 |
| 672 | You Want Permission to do What?!! | 1 | `technotes/fl/You Want Permission to do What-!!` | 未开始 |
| 673 | iCloud Drive Migration | 1 | `technotes/iCloud Drive Migration.md` | 未开始 |
| 674 | iOS Search API Best Practices and FAQs | 1 | `technotes/iOS Search API Best Practices and FAQs.md` | 未开始 |

### 图形与动画（22 份，22 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 675 | 'OpenGL Performance Optimization : The Basics' | 1 | `technotes/OpenGL Performance Optimization - The Basics` | 未开始 |
| 676 | 'Working Around Incorrect -needsToDrawRect: Behavior in Custom View Classes' | 1 | `technotes/tn2002/Working Around Incorrect -needsToDrawRect- Behavior in Custom View Classes` | 未开始 |
| 677 | Apple Image Capture Camera Module changes for Mac OS X Update 10.1.3 | 1 | `technotes/tn/Apple Image Capture Camera Module changes for Mac OS X Update 10.1.3` | 未开始 |
| 678 | Best Practices for Color Management in OS X and iOS | 1 | `technotes/Best Practices for Color Management in OS X and iOS` | 未开始 |
| 679 | ColorSync on Mac OS X | 1 | `technotes/ColorSync on Mac OS X` | 未开始 |
| 680 | Detecting low printer ink levels | 1 | `technotes/Detecting low printer ink levels.md` | 未开始 |
| 681 | Efficiently using Quartz Composer compositions with QuickTime | 1 | `technotes/Efficiently using Quartz Composer compositions with QuickTime` | 未开始 |
| 682 | Enabling multi-threaded execution of the OpenGL framework | 1 | `technotes/Enabling multi-threaded execution of the OpenGL framework` | 未开始 |
| 683 | Getting images in and out of Quartz Composer compositions | 1 | `technotes/Getting images in and out of Quartz Composer compositions.md` | 未开始 |
| 684 | Image Color Management | 1 | `technotes/Image Color Management` | 未开始 |
| 685 | Making the most of Cocoa bindings in Quartz Composer | 1 | `technotes/tn2005/Making the most of Cocoa bindings in Quartz Composer` | 未开始 |
| 686 | New ColorSync 3.0 APIs | 1 | `technotes/tn/New ColorSync 3.0 APIs` | 未开始 |
| 687 | Obtaining 16 Bits-Per-Color Data with CUPS Raster Printing | 1 | `technotes/Obtaining 16 Bits-Per-Color Data with CUPS Raster Printing.md` | 未开始 |
| 688 | Real world profiling with the OpenGL Profiler | 1 | `technotes/Real world profiling with the OpenGL Profiler` | 未开始 |
| 689 | Sandboxing a Print Dialog Extension | 1 | `technotes/Sandboxing a Print Dialog Extension.md` | 未开始 |
| 690 | Saving Printer Settings for Automatic Printing | 1 | `technotes/Saving Printer Settings for Automatic Printing.md` | 未开始 |
| 691 | TWAIN Data Sources for Mac OS X | 1 | `technotes/tn2002/TWAIN Data Sources for Mac OS X` | 未开始 |
| 692 | The CGDirectPalette API | 1 | `technotes/tn/The CGDirectPalette API` | 未开始 |
| 693 | The Enhanced Print Apple Event | 1 | `technotes/tn2002/The Enhanced Print Apple Event` | 未开始 |
| 694 | Understanding and Detecting OpenGL Functionality | 1 | `technotes/Understanding and Detecting OpenGL Functionality.md` | 未开始 |
| 695 | Using Cocoa and Core Printing Together | 1 | `technotes/Using Cocoa and Core Printing Together.md` | 未开始 |
| 696 | What's New With ColorSync 2.6 | 1 | `technotes/tn/What's New With ColorSync 2.6` | 未开始 |

### Xcode（15 份，15 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 697 | Basic debugging using logging for Swift and Objective-C apps. | 1 | `technotes/Basic debugging using logging for Swift and Objective-C apps` | 未开始 |
| 698 | Building from the Command Line with Xcode FAQ | 1 | `technotes/Building from the Command Line with Xcode FAQ` | 未开始 |
| 699 | C++ Tips and Tricks for Mac OS X | 1 | `technotes/C++ Tips and Tricks for Mac OS X.md` | 未开始 |
| 700 | Debugging An Authorization Plug-In With Xcode | 1 | `technotes/Debugging An Authorization Plug-In With Xcode` | 未开始 |
| 701 | Debugging Dashboard Widgets | 1 | `technotes/Debugging Dashboard Widgets` | 未开始 |
| 702 | Embedding Frameworks In An App | 1 | `technotes/Embedding Frameworks In An App` | 未开始 |
| 703 | Ensuring Backwards Binary Compatibility - Weak Linking and Availability Macros | 1 | `technotes/Ensuring Backwards Binary Compatibility - Weak Linking and Availability Macros o` | 未开始 |
| 704 | GDB for MacsBug Veterans | 1 | `technotes/tn/GDB for MacsBug Veterans` | 未开始 |
| 705 | Getting Started with GDB | 1 | `technotes/tn/Getting Started with GDB` | 未开始 |
| 706 | Nested Functions in Xcode | 1 | `technotes/Nested Functions in Xcode.md` | 未开始 |
| 707 | Resolving "0xE800003A", applications not launching and "missing entitlement" | 1 | `technotes/Resolving -0xE800003A-, applications not launching and -missing entitlement.md` | 未开始 |
| 708 | Speeding up your Xcode Builds | 1 | `technotes/Speeding up your Xcode Builds.md` | 未开始 |
| 709 | Troubleshooting App Thinning and Bitcode Build Failures | 1 | `technotes/Troubleshooting App Thinning and Bitcode Build Failures` | 未开始 |
| 710 | Troubleshooting Failed Signature Verification | 1 | `technotes/Troubleshooting Failed Signature Verification` | 未开始 |
| 711 | Using the iCloud App ID Service Settings with Xcode 5 and Xcode 6 | 1 | `technotes/Using the iCloud App ID Service Settings with Xcode 5 and Xcode 6` | 未开始 |

### 驱动、内核与硬件（13 份，13 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 712 | 'FireWire: DCL Programs Under Mac OS X' | 1 | `technotes/tn2002/FireWire- DCL Programs Under Mac OS X` | 未开始 |
| 713 | Building Universal IOKit Drivers | 1 | `technotes/Building Universal IOKit Drivers` | 未开始 |
| 714 | Introducing the Apple AppleUSBFTDI kernel driver | 1 | `technotes/Introducing the Apple AppleUSBFTDI kernel driver.md` | 未开始 |
| 715 | Kernel Authorization | 1 | `technotes/Kernel Authorization.md` | 未开始 |
| 716 | Kernel Core Dumps | 1 | `technotes/tn2004/Kernel Core Dumps` | 未开始 |
| 717 | Multipathing with FibreChannel on Mac OS X | 1 | `technotes/Multipathing with FibreChannel on Mac OS X` | 未开始 |
| 718 | New HID Manager APIs for Mac OS X version 10.5 | 1 | `technotes/New HID Manager APIs for Mac OS X version 10.5.md` | 未开始 |
| 719 | Power Management for Macintosh; getting started | 1 | `technotes/Power Management for Macintosh; getting started` | 未开始 |
| 720 | Secrets of the GPT | 1 | `technotes/Secrets of the GPT.md` | 未开始 |
| 721 | Selecting a GPU for OpenCL on the Mac Pro (Late 2013) | 1 | `technotes/Selecting a GPU for OpenCL on the Mac Pro (Late 2013).md` | 未开始 |
| 722 | Thermal considerations for Mac Pro FB-DIMMs | 1 | `technotes/tn2006/Thermal considerations for Mac Pro FB-DIMMs` | 未开始 |
| 723 | Understanding and Debugging Kernel Panics | 1 | `technotes/Understanding and Debugging Kernel Panics` | 未开始 |
| 724 | User-Approved Kernel Extension Loading | 1 | `technotes/User-Approved Kernel Extension Loading` | 未开始 |

### 用户体验（11 份，12 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 725 | Kiosk Mode Programming Topic | 2 | `technotes/Kiosk Mode Programming Topic` | 未开始 |
| 726 | Automatic Table Sorting with NSArrayController | 1 | `technotes/Automatic Table Sorting with NSArrayController` | 未开始 |
| 727 | Creating Kiosks | 1 | `technotes/Creating Kiosks.md` | 未开始 |
| 728 | Creating an About Panel in Your Cocoa Application | 1 | `technotes/Creating an About Panel in Your Cocoa Application` | 未开始 |
| 729 | Implementing a Shared iAd Banner | 1 | `technotes/Implementing a Shared iAd Banner.md` | 未开始 |
| 730 | Installable Keyboard Layouts | 1 | `technotes/Installable Keyboard Layouts.md` | 未开始 |
| 731 | Launching your iPhone Application in Landscape | 1 | `technotes/Launching your iPhone Application in Landscape` | 未开始 |
| 732 | Preparing Your Web Content for iPad | 1 | `technotes/Preparing Your Web Content for iPad` | 未开始 |
| 733 | The Euro Currency Symbol | 1 | `technotes/tn/The Euro Currency Symbol` | 未开始 |
| 734 | UIScrollView And Autolayout | 1 | `technotes/UIScrollView And Autolayout.md` | 未开始 |
| 735 | Using Unwind Segues | 1 | `technotes/Using Unwind Segues` | 未开始 |

### 语言与工具（11 份，11 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 736 | Changes To Embedding Python Using Xcode 5.0 | 1 | `technotes/Changes To Embedding Python Using Xcode 5.0.md` | 未开始 |
| 737 | Entitlements Troubleshooting | 1 | `technotes/Entitlements Troubleshooting` | 未开始 |
| 738 | Managing Multiple App ID Prefixes | 1 | `technotes/Managing Multiple App ID Prefixes.md` | 未开始 |
| 739 | New Control Styles available within J2SE 5.0 on Mac OS X 10.5 | 1 | `technotes/tn2007/New Control Styles available within J2SE 5.0 on Mac OS X 10.5` | 未开始 |
| 740 | Preprocessing Info.plist files in Xcode Using the C Preprocessor | 1 | `technotes/Preprocessing Info.plist files in Xcode Using the C Preprocessor.md` | 未开始 |
| 741 | Scripting Additions for Mac OS X | 1 | `technotes/Scripting Additions for Mac OS X.md` | 未开始 |
| 742 | Testing Core Bluetooth Applications in the iOS Simulator | 1 | `technotes/Testing Core Bluetooth Applications in the iOS Simulator` | 未开始 |
| 743 | Version Numbers and Build Numbers | 1 | `technotes/Version Numbers and Build Numbers` | 未开始 |
| 744 | Xcode Validation and Submission Issues for iOS | 1 | `technotes/Xcode Validation and Submission Issues for iOS.md` | 未开始 |
| 745 | iOS Code Signing Troubleshooting | 1 | `technotes/iOS Code Signing Troubleshooting` | 未开始 |
| 746 | iOS Code Signing Troubleshooting Index | 1 | `technotes/iOS Code Signing Troubleshooting Index.md` | 未开始 |

### 通用（10 份，10 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 747 | 'Game Center: Life without a Sandbox' | 1 | `technotes/Game Center- Life without a Sandbox.md` | 未开始 |
| 748 | 'Mac OS X: versions 10.0.1 through 10.0.4' | 1 | `technotes/tn/Mac OS X- versions 10.0.1 through 10.0.4` | 未开始 |
| 749 | Language Identifiers in iOS, macOS, watchOS, and tvOS | 1 | `technotes/Language Identifiers in iOS, macOS, watchOS, and tvOS.md` | 未开始 |
| 750 | Mac OS X Debugging Magic | 1 | `technotes/Mac OS X Debugging Magic` | 未开始 |
| 751 | Newsstand FAQ | 1 | `technotes/Newsstand FAQ.md` | 未开始 |
| 752 | Resolving Compatibility Problems on New OS Releases | 1 | `technotes/Resolving Compatibility Problems on New OS Releases.md` | 未开始 |
| 753 | SpriteKit Debugging Guide | 1 | `technotes/SpriteKit Debugging Guide` | 未开始 |
| 754 | Testing iOS App Updates | 1 | `technotes/Testing iOS App Updates.md` | 未开始 |
| 755 | Uniquely Identifying a Macintosh Computer | 1 | `technotes/Uniquely Identifying a Macintosh Computer.md` | 未开始 |
| 756 | iOS Debugging Magic | 1 | `technotes/iOS Debugging Magic` | 未开始 |

### 网络与互联网（9 份，9 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 757 | Browser Plugins in Mac OS X | 1 | `technotes/tn/Browser Plugins in Mac OS X` | 未开始 |
| 758 | Creating Certificates for TLS Testing | 1 | `technotes/Creating Certificates for TLS Testing` | 未开始 |
| 759 | Creating NetBoot Server-Friendly Applications | 1 | `technotes/tn/Creating NetBoot Server-Friendly Applications` | 未开始 |
| 760 | Document Transfer Strategies | 1 | `technotes/Document Transfer Strategies.md` | 未开始 |
| 761 | Embedding Bonjour in Windows Applications | 1 | `technotes/tn2007/Embedding Bonjour in Windows Applications` | 未开始 |
| 762 | Example Playlist Files for use with HTTP Live Streaming | 1 | `technotes/Example Playlist Files for use with HTTP Live Streaming.md` | 未开始 |
| 763 | HTTPS Server Trust Evaluation | 1 | `technotes/HTTPS Server Trust Evaluation.md` | 未开始 |
| 764 | Living in a Dynamic TCP/IP Environment | 1 | `technotes/Living in a Dynamic TCP-IP Environment` | 未开始 |
| 765 | Troubleshooting Push Notifications | 1 | `technotes/Troubleshooting Push Notifications.md` | 未开始 |

### 跨平台（9 份，9 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 766 | 'QuickTime For Windows: Resolving Common Installation Issues' | 1 | `technotes/tn/QuickTime For Windows- Resolving Common Installation Issues` | 未开始 |
| 767 | Building Universal Binaries from "configure"-based Open Source Projects | 1 | `technotes/tn2005/Building Universal Binaries from -configure--based Open Source Projects` | 未开始 |
| 768 | Frequently Asked Questions about the X Window System (X11) for Mac OS X | 1 | `technotes/tn2006/Frequently Asked Questions about the X Window System (X11) for Mac OS X` | 未开始 |
| 769 | Identifying Java on OS X | 1 | `technotes/tn2002/Identifying Java on OS X` | 未开始 |
| 770 | JNI Development on Mac OS X | 1 | `technotes/JNI Development on Mac OS X.md` | 未开始 |
| 771 | Java Runtime Properties for Mac OS X | 1 | `technotes/tn/Java Runtime Properties for Mac OS X` | 未开始 |
| 772 | OpenSSH updates in macOS 10.12.2 | 1 | `technotes/OpenSSH updates in macOS 10.12.2.md` | 未开始 |
| 773 | Porting Command Line Unix Tools to Mac OS X | 1 | `technotes/tn2002/Porting Command Line Unix Tools to Mac OS X` | 未开始 |
| 774 | Understanding the Differences Between Apple and Windows IMA-ADPCM Compressed | 1 | `technotes/tn/Understanding the Differences Between Apple and Windows IMA-ADPCM Compressed Sou` | 未开始 |

### 安全（7 份，7 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 775 | Accessing CrashWrangler to analyze crashes for security implications | 1 | `technotes/Accessing CrashWrangler to analyze crashes for security implications.md` | 未开始 |
| 776 | Authorization for Everyone | 1 | `technotes/Authorization for Everyone.md` | 未开始 |
| 777 | Installation Failure Troubleshooting for iOS | 1 | `technotes/Installation Failure Troubleshooting for iOS` | 未开始 |
| 778 | Running At Login | 1 | `technotes/Running At Login.md` | 未开始 |
| 779 | Using Secure Event Input Fairly | 1 | `technotes/Using Secure Event Input Fairly.md` | 未开始 |
| 780 | iOS 5 and TLS 1.2 Interoperability Issues | 1 | `technotes/iOS 5 and TLS 1.2 Interoperability Issues.md` | 未开始 |
| 781 | macOS Code Signing In Depth | 1 | `technotes/macOS Code Signing In Depth.md` | 未开始 |

### 应用间通信（7 份，7 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 782 | AEBuild*, AEPrint* and Friends | 1 | `technotes/tn/AEBuild, AEPrint and Friends` | 未开始 |
| 783 | AEStream and Friends | 1 | `technotes/tn/AEStream and Friends` | 未开始 |
| 784 | Building a Cocoa-AppleScript (AppleScriptObjC) Automator Action | 1 | `technotes/Building a Cocoa-AppleScript (AppleScriptObjC) Automator Action` | 未开始 |
| 785 | On Launching an App with a Document | 1 | `technotes/tn/On Launching an App with a Document` | 未开始 |
| 786 | Scripting Interface Guidelines | 1 | `technotes/tn2002/Scripting Interface Guidelines` | 未开始 |
| 787 | Using AppleScript Scripts in Cocoa Applications | 1 | `technotes/Using AppleScript Scripts in Cocoa Applications` | 未开始 |
| 788 | do shell script in AppleScript | 1 | `technotes/do shell script in AppleScript.md` | 未开始 |

### 性能（5 份，5 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 789 | 'High Precision Timers in iOS / OS X ' | 1 | `technotes/High Precision Timers in iOS - OS X.md` | 未开始 |
| 790 | Coalesced Updates | 1 | `technotes/Coalesced Updates.md` | 未开始 |
| 791 | Minimizing your app's Memory Footprint | 1 | `technotes/Minimizing your app's Memory Footprint` | 未开始 |
| 792 | Supporting Multiple GPUs on Mac OS X | 1 | `technotes/Supporting Multiple GPUs on Mac OS X.md` | 未开始 |
| 793 | Using collection classes safely with multithreaded applications | 1 | `technotes/tn2002/Using collection classes safely with multithreaded applications` | 未开始 |

### Apple 应用程序（4 份，4 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 794 | Building 64-bit and Universal 32/64-bit FxPlugs | 1 | `technotes/Building 64-bit and Universal 32-64-bit FxPlugs` | 未开始 |
| 795 | Final Cut Pro - The 'r4fl' Pixel Format | 1 | `technotes/Final Cut Pro - The 'r4fl' Pixel Format` | 未开始 |
| 796 | Final Cut Pro X - Metadata in MP4 | 1 | `technotes/Final Cut Pro X - Metadata in MP4.md` | 未开始 |
| 797 | Final Cut Server XML Format | 1 | `technotes/Final Cut Server XML Format.md` | 未开始 |

### 数学计算（1 份，1 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 798 | Support for Denormal Numbers | 1 | `technotes/Support for Denormal Numbers.md` | 未开始 |