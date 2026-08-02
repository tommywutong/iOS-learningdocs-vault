# qa 分类翻译计划

> 前置说明见 `/agent.md`（翻译规范、铁律：标题与正文必须同批次翻译）与 `qa/memory.md`（模块进度概览）。

## Context

`qa/` 是 Apple Technical Q&A（问答式短文），索引标题和正文均为纯英文，从未被任何一批 PR 覆盖过——同样是"从零开始"的计划，不涉及技术债清理。

内容几乎全是单页文档（1502 份对应 1503 页），比 technotes 体量更大，但单篇更短、结构更统一（一问一答）。

## 范围口径

- 覆盖 `qa/` 目录下全部 1502 份文档、1503 页。
- 排除标准：无。
- 表格按 frontmatter `topic` 字段分组（qa 分类的 topic 字段填写率高于 technotes，多数文档有明确分类）。

## 翻译流程

与 `/agent.md` 规定的规范一致。翻译时必须同一个 commit 里把该文档的 frontmatter title、正文、以及 `_indexes/qa.md`（含相关分类子索引）里对应的链接显示文字一起改完。

## 执行建议

单篇体量小（多数 1 页）、问答体裁重复度高，适合批量小规模并行认领，每批 30~50 篇为宜；建议优先处理有明确 topic 分类（尤其数据管理、用户体验）的部分，这些是日常开发高频检索内容。

## 完整清单（1502 份 / 1503 页，按 topic 分组，组内页数从大到小排列）


### 未分类（969 份，970 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 1 | Shift Booting under System 7 | 2 | `qa/ops/What Does Extension Manager Turn Off` | 未开始 |
| 2 | '"Payment requests are restricted to products returned as valid via Store Kit''s | 1 | `qa/-Payment requests are restricted to products returned as valid via Store Kit's d` | 未开始 |
| 3 | '''aete'' in Java' | 1 | `qa/java/'aete' in Java` | 未开始 |
| 4 | '''ptyp'' Resource Documentation' | 1 | `qa/gxpd/'ptyp' Resource Documentation.md` | 未开始 |
| 5 | 'Bizarre Extension Loading Order: BackQuote Sorts Between "A" and "B".' | 1 | `qa/ops/Bizarre Extension Loading Order- BackQuote Sorts Between -A- and -B` | 未开始 |
| 6 | 'Closing the Connection: OpenTransport' | 1 | `qa/nw/Closing the Connection- OpenTransport` | 未开始 |
| 7 | 'Decompressing to Partial window: Bug & Workaround' | 1 | `qa/qticm/Decompressing to Partial window- Bug & Workaround.md` | 未开始 |
| 8 | 'Developing with ZeroLink: small applications and launching on other computers' | 1 | `qa/qa2001/Developing with ZeroLink- small applications and launching on other computers` | 未开始 |
| 9 | 'Error Loading: DriverServicesLib (-2804) Error Explained' | 1 | `qa/qd3d/Error Loading- DriverServicesLib (-2804) Error Explained.md` | 未开始 |
| 10 | 'LaserWriter 8.3 %%?BeginQuery: RBIAppleDevice Query' | 1 | `qa/qd/LaserWriter 8.3 %%-BeginQuery- RBIAppleDevice Query.md` | 未开始 |
| 11 | 'Open Transport Error -3208:  kEBADFErr' | 1 | `qa/nw/Open Transport Error -3208- kEBADFErr` | 未开始 |
| 12 | 'PCI Drivers: I/O Queue & KillIO' | 1 | `qa/hw/PCI Drivers- I-O Queue & KillIO` | 未开始 |
| 13 | 'Spaces in project names: solving "Missing file or directory" errors in Project | 1 | `qa/qa2001/Spaces in project names- solving -Missing file or directory- errors in Project B` | 未开始 |
| 14 | -27835 Error at GXFinishPage | 1 | `qa/gx/-27835 Error at GXFinishPage` | 未开始 |
| 15 | -28482 Errors When Selecting Markers | 1 | `qa/qd3d/-28482 Errors When Selecting Markers.md` | 未开始 |
| 16 | -51 or -39 Error Code with GX Printing | 1 | `qa/gxpd/-51 or -39 Error Code with GX Printing.md` | 未开始 |
| 17 | 128Mb SDRAM ICs limitation on original "Bronze Keyboard" Powerbook G3 | 1 | `qa/qa2001/128Mb SDRAM ICs limitation on original -Bronze Keyboard- Powerbook G3` | 未开始 |
| 18 | 3D Acceleration | 1 | `qa/qd3d/3D Acceleration.md` | 未开始 |
| 19 | 48 bit & 64 bit Pixel Format support in QuickTime | 1 | `qa/qa2001/48 bit & 64 bit Pixel Format support in QuickTime` | 未开始 |
| 20 | 68K Open Transport Code on Power Macintoshes | 1 | `qa/nw/68K Open Transport Code on Power Macintoshes/Not Recommended Documentclose button.md` | 未开始 |
| 21 | A Method for AMT to "remember" Changes Made on Screen | 1 | `qa/amt pe/A Method for AMT to -remember- Changes Made on Screen.md` | 未开始 |
| 22 | A SCSI little secret | 1 | `qa/hw/A SCSI little secret` | 未开始 |
| 23 | A5 World | 1 | `qa/ppcsys/A5 World.md` | 未开始 |
| 24 | AFPCommand() variation | 1 | `qa/nw/AFPCommand() variation` | 未开始 |
| 25 | AMT_PE and QuickTime for Windows Compatibility under Windows 95 | 1 | `qa/amt pe/AMTPE and QuickTime for Windows Compatibility under Windows 95.md` | 未开始 |
| 26 | API for Non-GX Printing? | 1 | `qa/qd/API for Non-GX Printing.md` | 未开始 |
| 27 | ATA Manager Events Clarified | 1 | `qa/dv/ATA Manager Events Clarified.md` | 未开始 |
| 28 | ATSUI and MLTE Printing | 1 | `qa/qd/ATSUI and MLTE Printing.md` | 未开始 |
| 29 | Aborting a OTConnect in Progress | 1 | `qa/nw/Aborting a OTConnect in Progress` | 未开始 |
| 30 | Accessing DHCP Options | 1 | `qa/nw/Accessing DHCP Options` | 未开始 |
| 31 | Accessing Decompressed Images | 1 | `qa/qtmtb/Accessing Decompressed Images.md` | 未开始 |
| 32 | Accessing Image Metadata in iOS | 1 | `qa/Accessing Image Metadata in iOS.md` | 未开始 |
| 33 | Accessing the ARA/PPP password | 1 | `qa/nw/Accessing the ARA-PPP password` | 未开始 |
| 34 | Accessing the DialAssist data | 1 | `qa/nw/Accessing the DialAssist data` | 未开始 |
| 35 | Accessing the Geographical Database in Apple's Map Control Panel | 1 | `qa/ops/Accessing the Geographical Database in Apple's Map Control Panel` | 未开始 |
| 36 | Activating CrashReporter in OS X | 1 | `qa/qa2001/Activating CrashReporter in OS X` | 未开始 |
| 37 | Adding Color Icons to Menu Items | 1 | `qa/tb/Adding Color Icons to Menu Items` | 未开始 |
| 38 | Adding File and Clipboard Support to a QuickDraw 3D Application | 1 | `qa/qd3d/Adding File and Clipboard Support to a QuickDraw 3D Application.md` | 未开始 |
| 39 | Adding Print Items to a Dialog | 1 | `qa/gxpd/Adding Print Items to a Dialog.md` | 未开始 |
| 40 | Adding QuickDraw GX Printing Panels | 1 | `qa/gxpd/Adding QuickDraw GX Printing Panels.md` | 未开始 |
| 41 | Adding QuickTime Movie Data to Non-QuickTime Files | 1 | `qa/qtmtb/Adding QuickTime Movie Data to Non-QuickTime Files.md` | 未开始 |
| 42 | Adding Special Folders | 1 | `qa/tb/Adding Special Folders` | 未开始 |
| 43 | Adding Unicode characters to Text Media in a Text Track | 1 | `qa/Adding Unicode characters to Text Media in a Text Track.md` | 未开始 |
| 44 | Adding a Text Track to a QuickTime Video | 1 | `qa/qtmtb/Adding a Text Track to a QuickTime Video.md` | 未开始 |
| 45 | Adding a movie reference to a movie | 1 | `qa/Adding a movie reference to a movie.md` | 未开始 |
| 46 | Adding an automated Window menu to your application | 1 | `qa/qa2001/Adding an automated Window menu to your application` | 未开始 |
| 47 | Adding dependencies with kmodload | 1 | `qa/qa2001/Adding dependencies with kmodload` | 未开始 |
| 48 | Adding menu separator items to controls in a Sherlock channel | 1 | `qa/qa2001/Adding menu separator items to controls in a Sherlock channel` | 未开始 |
| 49 | Adding metadata to a QuickTime movie using the QuickTime MetaData APIs | 1 | `qa/Adding metadata to a QuickTime movie using the QuickTime MetaData APIs.md` | 未开始 |
| 50 | Adding metadata to an iTunes file using the QuickTime Metadata APIs | 1 | `qa/Adding metadata to an iTunes file using the QuickTime Metadata APIs.md` | 未开始 |
| 51 | Additional URL Access Error Codes | 1 | `qa/nw/Additional URL Access Error Codes` | 未开始 |
| 52 | AddrToName | 1 | `qa/nw/AddrToName` | 未开始 |
| 53 | Adjusting the movie brightness | 1 | `qa/Adjusting the movie brightness.md` | 未开始 |
| 54 | All Geometry Vertices Need UV Parameterization | 1 | `qa/qd3d/All Geometry Vertices Need UV Parameterization.md` | 未开始 |
| 55 | Allocating Memory to MPW | 1 | `qa/qtvr/Allocating Memory to MPW.md` | 未开始 |
| 56 | Altering the GX General Print Panel | 1 | `qa/gxpd/Altering the GX General Print Panel.md` | 未开始 |
| 57 | Ambient Coefficient | 1 | `qa/qd3d/Ambient Coefficient.md` | 未开始 |
| 58 | Animation Techniques | 1 | `qa/qtvr/Animation Techniques.md` | 未开始 |
| 59 | Apple Accelerator Card & Textures | 1 | `qa/qd3d/Apple Accelerator Card & Textures.md` | 未开始 |
| 60 | Apple Mass Storage Class Driver always matches to my device at startup | 1 | `qa/qa2001/Apple Mass Storage Class Driver always matches to my device at startup` | 未开始 |
| 61 | AppleGuide 1.2.7 Fixes PowerPC Context & Coach Handler Crashes | 1 | `qa/hs/AppleGuide 1.2.7 Fixes PowerPC Context & Coach Handler Crashes.md` | 未开始 |
| 62 | AppleGuideGlueLib.xcoff Name Change | 1 | `qa/hs/AppleGuideGlueLib.xcoff Name Change.md` | 未开始 |
| 63 | AppleScript for Java | 1 | `qa/java/AppleScript for Java` | 未开始 |
| 64 | AppleTalk Limitations | 1 | `qa/nw/AppleTalk Limitations` | 未开始 |
| 65 | Application Freezes on Startup with WorldScript I v7.1 | 1 | `qa/qd/Application Freezes on Startup with WorldScript I v7.1.md` | 未开始 |
| 66 | Application-Defined Functions,SetSequenceProgressProc | 1 | `qa/qticm/Application-Defined Functions,SetSequenceProgressProc.md` | 未开始 |
| 67 | Are the Name Registry device tree nodes unique? | 1 | `qa/hw/Are the Name Registry device tree nodes unique` | 未开始 |
| 68 | Are the root control, the root view, and the content view the same entity? | 1 | `qa/qa2001/Are the root control, the root view, and the content view the same entity` | 未开始 |
| 69 | Are there any OSStatus values I can use in my programs? | 1 | `qa/ov/Are there any OSStatus values I can use in my programs.md` | 未开始 |
| 70 | Asserting fast-back-to-back transfers in the PCI Power Mac | 1 | `qa/hw/Asserting fast-back-to-back transfers in the PCI Power Mac` | 未开始 |
| 71 | Assigning Keystroke Combinations | 1 | `qa/qtvr/Assigning Keystroke Combinations.md` | 未开始 |
| 72 | Audio Queue - Handling Playback Interruptions | 1 | `qa/qa2008/Audio Queue - Handling Playback Interruptions` | 未开始 |
| 73 | AudioChannelLayout - What's the Audio Channel Order when the Layout has a Channel | 1 | `qa/AudioChannelLayout - What's the Audio Channel Order when the Layout has a Channe.md` | 未开始 |
| 74 | Auto-dependency Checker | 1 | `qa/plat/Auto-dependency Checker` | 未开始 |
| 75 | Automatically starting and stopping application instances without using Monitor | 1 | `qa/qa2001/Automatically starting and stopping application instances without using Monitor` | 未开始 |
| 76 | Avoiding DragDrawingProc Pixel Trails | 1 | `qa/tb/Avoiding DragDrawingProc Pixel Trails` | 未开始 |
| 77 | Avoiding Pauses When Looping Audio files with QuickTime | 1 | `qa/Avoiding Pauses When Looping Audio files with QuickTime.md` | 未开始 |
| 78 | Background Printing On, Print Monitor Dialog Missing | 1 | `qa/qd/Background Printing On, Print Monitor Dialog Missing.md` | 未开始 |
| 79 | Base-Derived async image codecs must implement ImageCodecQueueStarting and | 1 | `qa/qa2001/Base-Derived async image codecs must implement ImageCodecQueueStarting and Image` | 未开始 |
| 80 | Batch Exporting movie sound tracks with ConvertMovieToFile() | 1 | `qa/qtmtb/Batch Exporting movie sound tracks with ConvertMovieToFile().md` | 未开始 |
| 81 | BeginMediaEdits -2050 badDataRefIndex error after calling NewMovie | 1 | `qa/qtmtb/BeginMediaEdits -2050 badDataRefIndex error after calling NewMovie.md` | 未开始 |
| 82 | Bonjour over Bluetooth on iOS 5 and Later | 1 | `qa/Bonjour over Bluetooth on iOS 5 and Later.md` | 未开始 |
| 83 | Booting after invoking the Open Firmware user interface | 1 | `qa/hw/Booting after invoking the Open Firmware user interface` | 未开始 |
| 84 | BowelsOfTheMemoryManager (aka YourHeapIsProbablyCorrupt) | 1 | `qa/me/BowelsOfTheMemoryManager (aka YourHeapIsProbablyCorrupt).md` | 未开始 |
| 85 | Building an Application for Windows in Apple Media Tool | 1 | `qa/amt pe/Building an Application for Windows in Apple Media Tool.md` | 未开始 |
| 86 | C Open File Limit | 1 | `qa/plat/C Open File Limit` | 未开始 |
| 87 | C++ Precedence Bug | 1 | `qa/plat/C++ Precedence Bug` | 未开始 |
| 88 | CTB & the AppleTalk ADSP Tool | 1 | `qa/nw/CTB & the AppleTalk ADSP Tool` | 未开始 |
| 89 | CalcCMask and SeedCFill in Carbon | 1 | `qa/qd/CalcCMask and SeedCFill in Carbon.md` | 未开始 |
| 90 | Calculating the static video frame rate of a QuickTime movie. | 1 | `qa/Calculating the static video frame rate of a QuickTime movie.md` | 未开始 |
| 91 | Call Q3View_GetWorldToFrustumMatrixState Only In A Rendering Loop | 1 | `qa/qd3d/Call Q3ViewGetWorldToFrustumMatrixState Only In A Rendering Loop.md` | 未开始 |
| 92 | Calling CloseOpenTransport When Writing an App | 1 | `qa/nw/Calling CloseOpenTransport When Writing an App` | 未开始 |
| 93 | Calling Control Strip Routines from PowerPC Code | 1 | `qa/ops/Calling Control Strip Routines from PowerPC Code` | 未开始 |
| 94 | Calling GetMenu Redundantly | 1 | `qa/tb/Calling GetMenu Redundantly` | 未开始 |
| 95 | Calling TrackDrag with the Event Record's 'where' Field Expressed in Local | 1 | `qa/tb/Calling TrackDrag with the Event Record's 'where' Field Expressed in Local Coord` | 未开始 |
| 96 | Calling ataManager on a Power Macintosh | 1 | `qa/dv/Calling ataManager on a Power Macintosh.md` | 未开始 |
| 97 | Calling the Resource Manager from a Patch | 1 | `qa/tb/Calling the Resource Manager from a Patch` | 未开始 |
| 98 | Camera Hither Distance Must Be > 0 | 1 | `qa/qd3d/Camera Hither Distance Must Be - 0.md` | 未开始 |
| 99 | Can I have parameters of type typeHIRect instead of type typeQDRectangle in | 1 | `qa/qa2001/Can I have parameters of type typeHIRect instead of type typeQDRectangle in my k` | 未开始 |
| 100 | Can you explain the words "begin" and "again"? | 1 | `qa/hw/Can you explain the words -begin- and -again` | 未开始 |
| 101 | Can't Print Hairlines | 1 | `qa/gxpd/Can't Print Hairlines.md` | 未开始 |
| 102 | Can't Turn Off DrawContext's clearImageMethod | 1 | `qa/qd3d/Can't Turn Off DrawContext's clearImageMethod.md` | 未开始 |
| 103 | Can't attach during two-machine debugging with GDB | 1 | `qa/qa2001/Can't attach during two-machine debugging with GDB` | 未开始 |
| 104 | Cannot load underlying module for XCTest | 1 | `qa/Cannot load underlying module for XCTest` | 未开始 |
| 105 | Capturing Speech Manager Output | 1 | `qa/snd/Capturing Speech Manager Output.md` | 未开始 |
| 106 | Capturing a real-time movie stream | 1 | `qa/Capturing a real-time movie stream.md` | 未开始 |
| 107 | Carbon Drawer problem in Mac OS X v10.4 and v10.4.1 | 1 | `qa/Carbon Drawer problem in Mac OS X v10.4 and v10.4.1.md` | 未开始 |
| 108 | Carbon Full Screen Conundrums | 1 | `qa/qa2001/Carbon Full Screen Conundrums` | 未开始 |
| 109 | Changing IP Numbers under Open Transport | 1 | `qa/nw/Changing IP Numbers under Open Transport` | 未开始 |
| 110 | Changing Scaling, Flipping, and Resolution | 1 | `qa/gxpd/Changing Scaling, Flipping, and Resolution.md` | 未开始 |
| 111 | Changing the Default Directory for StandardFile Calls | 1 | `qa/tb/Changing the Default Directory for StandardFile Calls` | 未开始 |
| 112 | Changing the configuration variable in Open Firmware | 1 | `qa/hw/Changing the configuration variable in Open Firmware` | 未开始 |
| 113 | Checking For QD3D Windows DLL's | 1 | `qa/qd3d/Checking For QD3D Windows DLL's.md` | 未开始 |
| 114 | Checking Whether QD3D Is Available | 1 | `qa/qd3d/Checking Whether QD3D Is Available.md` | 未开始 |
| 115 | Checking for the Availability of Acceleration Hardware | 1 | `qa/c/Checking for the Availability of Acceleration Hardware` | 未开始 |
| 116 | Checking for the Printer Driver | 1 | `qa/dv/Checking for the Printer Driver.md` | 未开始 |
| 117 | Checking for the presence of a native library from Java | 1 | `qa/java/Checking for the presence of a native library from Java` | 未开始 |
| 118 | Checking if Open Transport IP Stack is Loaded | 1 | `qa/nw/Checking if Open Transport IP Stack is Loaded` | 未开始 |
| 119 | Choosing an inviter when using Multipeer Connectivity | 1 | `qa/Choosing an inviter when using Multipeer Connectivity.md` | 未开始 |
| 120 | Choosing the Position Where a Movie is Pasted | 1 | `qa/qtmtb/Choosing the Position Where a Movie is Pasted.md` | 未开始 |
| 121 | Clarification of TQ3HitData's 'distance' Field | 1 | `qa/qd3d/Clarification of TQ3HitData's 'distance' Field.md` | 未开始 |
| 122 | Clearing the Z-buffer in RAVE | 1 | `qa/qd3d/Clearing the Z-buffer in RAVE.md` | 未开始 |
| 123 | Clickable Static Text Item | 1 | `qa/Clickable Static Text Item.md` | 未开始 |
| 124 | CloseDialog and 'ictb's | 1 | `qa/tb/CloseDialog and 'ictb's` | 未开始 |
| 125 | Closing PPC ports | 1 | `qa/ic/Closing PPC ports.md` | 未开始 |
| 126 | Cocoa-Java quit/cancel-quit header bug in Mac OS X 10.0 | 1 | `qa/qa2001/Cocoa-Java quit-cancel-quit header bug in Mac OS X 10.0` | 未开始 |
| 127 | Code Resources Larger Than 32K | 1 | `qa/plat/Code Resources Larger Than 32K` | 未开始 |
| 128 | Collision Detection | 1 | `qa/qd3d/Collision Detection.md` | 未开始 |
| 129 | Color Animated Cursors | 1 | `qa/tb/Color Animated Cursors` | 未开始 |
| 130 | Color-Separating Arbitrary Shapes | 1 | `qa/gx/Color-Separating Arbitrary Shapes` | 未开始 |
| 131 | ColorPicker.h and ColorSync 2.0 | 1 | `qa/c/ColorPicker.h and ColorSync 2.0` | 未开始 |
| 132 | ColorSync 2.0 | 1 | `qa/c/ColorSync 2.0` | 未开始 |
| 133 | ColorSync 2.0 Gamut Checking | 1 | `qa/c/ColorSync 2.0 Gamut Checking` | 未开始 |
| 134 | Common Problems when Installing QuickTime VR | 1 | `qa/qtvr/Common Problems when Installing QuickTime VR.md` | 未开始 |
| 135 | Comparing selectors in Cocoa-Java code | 1 | `qa/qa2001/Comparing selectors in Cocoa-Java code` | 未开始 |
| 136 | Component Definitions | 1 | `qa/qtmcc/Component Definitions.md` | 未开始 |
| 137 | Composite Class Driver loads via both Driver/InterfaceInitialize entry point | 1 | `qa/usb/Composite Class Driver loads via both Driver-InterfaceInitialize entry point.md` | 未开始 |
| 138 | CompressSequenceBegin & Ethernet in QuickTime | 1 | `qa/qticm/CompressSequenceBegin & Ethernet in QuickTime.md` | 未开始 |
| 139 | Compressed and Uncompressed Samples in the Same Track | 1 | `qa/qtmtb/Compressed and Uncompressed Samples in the Same Track.md` | 未开始 |
| 140 | Compression Sequence APIs - codecErr returned when compressing with H.264 | 1 | `qa/Compression Sequence APIs - codecErr returned when compressing with H.264.md` | 未开始 |
| 141 | Compression Sessions - Configuring codec quality settings | 1 | `qa/Compression Sessions - Configuring codec quality settings.md` | 未开始 |
| 142 | Compression Sessions - Configuring options using the Standard Compression dialog | 1 | `qa/Compression Sessions - Configuring options using the Standard Compression dialog` | 未开始 |
| 143 | Compression Sessions - Enabling multi-pass encoding | 1 | `qa/Compression Sessions - Enabling multi-pass encoding.md` | 未开始 |
| 144 | Compression Sessions - Multipass encoding and the pass mode flags | 1 | `qa/Compression Sessions - Multipass encoding and the pass mode flags.md` | 未开始 |
| 145 | Compression Sessions - Temporal compression options | 1 | `qa/Compression Sessions - Temporal compression options.md` | 未开始 |
| 146 | Concurrent NSOperations Failing On iOS 4 | 1 | `qa/Concurrent NSOperations Failing On iOS 4.md` | 未开始 |
| 147 | Conditions Under Which Bluetooth State Restoration Will Relaunch An App | 1 | `qa/Conditions Under Which Bluetooth State Restoration Will Relaunch An App.md` | 未开始 |
| 148 | Connecting to a Sleeping or Dozing Macintosh | 1 | `qa/nw/Connecting to a Sleeping or Dozing Macintosh` | 未开始 |
| 149 | Control Panel Problems with Popup Menu's Click Area | 1 | `qa/tb/Control Panel Problems with Popup Menu's Click Area` | 未开始 |
| 150 | Controlling The Location Services Status Bar (Blue Bar) From Your App | 1 | `qa/Controlling The Location Services Status Bar (Blue Bar) From Your App.md` | 未开始 |
| 151 | ConvertMovieToFile unexpected results | 1 | `qa/qtmtb/ConvertMovieToFile unexpected results.md` | 未开始 |
| 152 | Converting RGB Colors to a Palette Index | 1 | `qa/qd/Converting RGB Colors to a Palette Index.md` | 未开始 |
| 153 | Coordinating Deferred Tasks and Secondary Interrupts | 1 | `qa/dv/Coordinating Deferred Tasks and Secondary Interrupts/Legacy Documentclose button.md` | 未开始 |
| 154 | CopyBits and Background Printing | 1 | `qa/qd/CopyBits and Background Printing.md` | 未开始 |
| 155 | Copybits Bus Error with Offscreen GWorld | 1 | `qa/qd/Copybits Bus Error with Offscreen GWorld.md` | 未开始 |
| 156 | Correct Setup of an AGLDrawable | 1 | `qa/ogl/Correct Setup of an AGLDrawable.md` | 未开始 |
| 157 | Correct Time Values | 1 | `qa/qtmtb/Correct Time Values.md` | 未开始 |
| 158 | Correction to SetMediaDataRef, short, not pointer | 1 | `qa/qtmtb/Correction to SetMediaDataRef, short, not pointer.md` | 未开始 |
| 159 | Crash When Sending Messages in an Override | 1 | `qa/gxpd/Crash When Sending Messages in an Override.md` | 未开始 |
| 160 | Crashes on Quit in MPW 3.4a7 | 1 | `qa/plat/Crashes on Quit in MPW 3.4a7` | 未开始 |
| 161 | Creating Apple TV Media Files Containing Dolby Digital Professional AC-3 Audio | 1 | `qa/Creating Apple TV Media Files Containing Dolby Digital Professional AC-3 Audio` | 未开始 |
| 162 | Creating Custom Icons for Documents Generated by a Plug-In | 1 | `qa/ops/Creating Custom Icons for Documents Generated by a Plug-In` | 未开始 |
| 163 | Creating Gray Scaled Images > 8 bits | 1 | `qa/qd/Creating Gray Scaled Images - 8 bits.md` | 未开始 |
| 164 | Creating Native MPW Tools | 1 | `qa/plat/Creating Native MPW Tools` | 未开始 |
| 165 | Creating QuickDrawGX Fonts | 1 | `qa/gxty/Creating QuickDrawGX Fonts.md` | 未开始 |
| 166 | Creating Sample Descriptor Atoms for a Non-Mac Device | 1 | `qa/qtpc/Creating Sample Descriptor Atoms for a Non-Mac Device.md` | 未开始 |
| 167 | Creating Screen Savers | 1 | `qa/tb/Creating Screen Savers` | 未开始 |
| 168 | Creating Sub GWorlds using QTNewGWorldFromPtr | 1 | `qa/qa2001/Extracting DV Fields using QTNewGWorldFromPtr/qa1014.md` | 未开始 |
| 169 | Creating Thumbnail PICTs | 1 | `qa/qticm/Creating Thumbnail PICTs.md` | 未开始 |
| 170 | Creating a GX Printing Extension to Obtain Print Job Information | 1 | `qa/gxpd/Creating a GX Printing Extension to Obtain Print Job Information.md` | 未开始 |
| 171 | Creating a Linked VR Movie without Hotspots | 1 | `qa/qtvr/Creating a Linked VR Movie without Hotspots.md` | 未开始 |
| 172 | Creating a Menu with an Icon as its Title | 1 | `qa/tb/Creating a Menu with an Icon as its Title` | 未开始 |
| 173 | Creating a Monitors Control Panel Extension | 1 | `qa/hw/Creating a Monitors Control Panel Extension` | 未开始 |
| 174 | Creating a Movie from Movie Data in Memory | 1 | `qa/Creating a Movie from Movie Data in Memory.md` | 未开始 |
| 175 | Creating serialVersionUIDs using MRJ | 1 | `qa/java/Creating serialVersionUIDs using MRJ` | 未开始 |
| 176 | Creating textures in the PVRTC compression format | 1 | `qa/Creating textures in the PVRTC compression format.md` | 未开始 |
| 177 | Creating track references when editing movies | 1 | `qa/qtmtb/Creating track references when editing movies.md` | 未开始 |
| 178 | Current GDevice Dependencies | 1 | `qa/qa2001/Current GDevice Dependencies` | 未开始 |
| 179 | Custom Designing a GX Font | 1 | `qa/gxty/Custom Designing a GX Font.md` | 未开始 |
| 180 | Customizing Font Properties | 1 | `qa/java/Customizing Font Properties` | 未开始 |
| 181 | DDC Information Source | 1 | `qa/hw/DDC Information Source` | 未开始 |
| 182 | DDR SDRAM ICs for PowerBooks and iBooks that use Memory bus slewing | 1 | `qa/qa2001/DDR SDRAM ICs for PowerBooks and iBooks that use Memory bus slewing` | 未开始 |
| 183 | DONT_NEED_DDRAW Preprocessor Explained | 1 | `qa/qd3d/DONTNEEDDDRAW Preprocessor Explained.md` | 未开始 |
| 184 | DR Emulator Caches | 1 | `qa/hw/DR Emulator Caches` | 未开始 |
| 185 | DRAM DIMM power pin connections for Macintosh Computers | 1 | `qa/qa2001/DRAM DIMM power pin connections for Macintosh Computers` | 未开始 |
| 186 | DV Codec settings and performance | 1 | `qa/qa2001/DV Codec settings and performance` | 未开始 |
| 187 | Debugging GX Graphics Code | 1 | `qa/gx/Debugging GX Graphics Code` | 未开始 |
| 188 | Decompressing IMA WAVE files | 1 | `qa/qtmcc/Decompressing IMA WAVE files.md` | 未开始 |
| 189 | Decompressing MP3 | 1 | `qa/qtmcc/Decompressing MP3.md` | 未开始 |
| 190 | Decompression Sessions - Setting codec accuracy and field mode | 1 | `qa/Decompression Sessions - Setting codec accuracy and field mode.md` | 未开始 |
| 191 | Default Number of Surface Planes | 1 | `qa/qd3d/Default Number of Surface Planes.md` | 未开始 |
| 192 | Default Surface/Shader UV Params For Caps of Cones & Cylinders | 1 | `qa/qd3d/Default Surface-Shader UV Params For Caps of Cones & Cylinders.md` | 未开始 |
| 193 | Defining and Using the kTransformFocused IconTransformType | 1 | `qa/Defining and Using the kTransformFocused IconTransformType` | 未开始 |
| 194 | Defining user properties with MRJAppBuilder | 1 | `qa/java/Defining user properties with MRJAppBuilder` | 未开始 |
| 195 | Deleting a Resource Fork | 1 | `qa/ops/Deleting a Resource Fork` | 未开始 |
| 196 | Derived Media Handler Components Update | 1 | `qa/qtmcc/Derived Media Handler Components Update.md` | 未开始 |
| 197 | Deselecting Icons in the Finder | 1 | `qa/ic/Deselecting Icons in the Finder.md` | 未开始 |
| 198 | Desk Accessory Menus | 1 | `qa/tb/Desk Accessory Menus` | 未开始 |
| 199 | Desktop Using Icons from Old Versions of Applications | 1 | `qa/ops/Desktop Using Icons from Old Versions of Applications` | 未开始 |
| 200 | Detecting CD/DVD media types | 1 | `qa/qa2001/Detecting CD-DVD media types` | 未开始 |
| 201 | Detecting Classic and Carbon X Environments | 1 | `qa/ov/Detecting Classic and Carbon X Environments.md` | 未开始 |
| 202 | Detecting Control Strip at Startup | 1 | `qa/ops/Detecting Control Strip at Startup` | 未开始 |
| 203 | Detecting a CD-ROM | 1 | `qa/dv/Detecting a CD-ROM.md` | 未开始 |
| 204 | Detecting specific ROM-in-RAM Mac | 1 | `qa/hw/Detecting specific ROM-in-RAM Mac` | 未开始 |
| 205 | Detecting the Microseconds Trap | 1 | `qa/tb/Detecting the Microseconds Trap` | 未开始 |
| 206 | Determining 3DMF Endian-ness | 1 | `qa/qd3d/Determining 3DMF Endian-ness.md` | 未开始 |
| 207 | Determining MRJ's Version | 1 | `qa/java/Determining MRJ's Version` | 未开始 |
| 208 | Determining Open Firmware version | 1 | `qa/hw/Determining Open Firmware version` | 未开始 |
| 209 | Determining Power PC Type 11 Errors | 1 | `qa/plat/Determining Power PC Type 11 Errors` | 未开始 |
| 210 | Determining QuickDrawVideo Media Pixel Depth | 1 | `qa/qtmtb/Determining QuickDrawVideo Media Pixel Depth` | 未开始 |
| 211 | Determining RAM size & location in New World Machines | 1 | `qa/qa2001/Determining RAM size & location in New World Machines` | 未开始 |
| 212 | Determining The Selected Printer's Address | 1 | `qa/qd/Determining The Selected Printer's Address.md` | 未开始 |
| 213 | Determining Whether a Device Supports Asynchronous I/O | 1 | `qa/dv/Determining Whether a Device Supports Asynchronous I-O.md` | 未开始 |
| 214 | Determining Which Features Are Supported by Specific Renderers | 1 | `qa/qd3d/Determining Which Features Are Supported by Specific Renderers.md` | 未开始 |
| 215 | Determining a PostScript Printer's Optimal Resolution | 1 | `qa/qd/Determining a PostScript Printer's Optimal Resolution/Legacy Documentclose button.md` | 未开始 |
| 216 | Determining if a 680x0 program is Running on a PPC | 1 | `qa/ops/Determining if a 680x0 program is Running on a PPC` | 未开始 |
| 217 | Determining if a Drive is a Network Volume | 1 | `qa/fl/Determining if a Drive is a Network Volume.md` | 未开始 |
| 218 | Determining if a PCI Bus Exists | 1 | `qa/hw/Determining if a PCI Bus Exists` | 未开始 |
| 219 | Determining if the Cursor is Hidden Or Not | 1 | `qa/ops/Determining if the Cursor is Hidden Or Not` | 未开始 |
| 220 | Determining required components for QuickTime movies | 1 | `qa/qa2001/Determining required components for QuickTime movies` | 未开始 |
| 221 | Determining the Size of the Disk Cache | 1 | `qa/me/Determining the Size of the Disk Cache.md` | 未开始 |
| 222 | Determining the State of the Modern Memory Manager | 1 | `qa/me/Determining the State of the Modern Memory Manager.md` | 未开始 |
| 223 | Determining the version of Open Firmware on your Mac | 1 | `qa/hw/Determining the version of Open Firmware on your Mac` | 未开始 |
| 224 | Determining volume size | 1 | `qa/fl/Determining volume size/Legacy Documentclose button.md` | 未开始 |
| 225 | Developing a QuickTime Musical Instrument | 1 | `qa/qtma/Developing a QuickTime Musical Instrument.md` | 未开始 |
| 226 | Developing a SCSI SIM for a PCI SCSI Controller | 1 | `qa/hw/Developing a SCSI SIM for a PCI SCSI Controller` | 未开始 |
| 227 | Device Driver Flags | 1 | `qa/dv/Native Drivers ('ndrv's) and dNeedTime/Legacy Documentclose button-2.md` | 未开始 |
| 228 | Device Manager | 1 | `qa/dv/Device Manager.md` | 未开始 |
| 229 | Difference between PCCard SDK2 and SDK3 | 1 | `qa/hw/Difference between PCCard SDK2 and SDK3` | 未开始 |
| 230 | Difference between an Open Firmware word and method | 1 | `qa/hw/Difference between an Open Firmware word and method` | 未开始 |
| 231 | Difference between using Restart or Shut Down in the Finder's Special menu | 1 | `qa/hw/Difference between using Restart or Shut Down in the Finder's Special menu in Op` | 未开始 |
| 232 | Differences between QuickDraw GX 1.1.1 and 1.0.x | 1 | `qa/Differences between QuickDraw GX 1.1.1 and 1.0.x.md` | 未开始 |
| 233 | Differences between iMac models | 1 | `qa/hw/Differences between iMac models` | 未开始 |
| 234 | Direction of Mesh Contours | 1 | `qa/qd3d/Direction of Mesh Contours.md` | 未开始 |
| 235 | Disabling QuickTime Error Dialogs When Opening or Tasking a Movie | 1 | `qa/qa2001/Disabling QuickTime Error Dialogs When Opening or Tasking a Movie` | 未开始 |
| 236 | Discipline startup, Documentation | 1 | `qa/plat/Discipline startup, Documentation` | 未开始 |
| 237 | Disconnect/Retry | 1 | `qa/hw/Disconnect-Retry` | 未开始 |
| 238 | Displaying PCI Configuration Registers contents in Open Firmware | 1 | `qa/qa2001/Displaying PCI Configuration Registers contents in Open Firmware` | 未开始 |
| 239 | Displaying Windows 3DMF Files On A Mac | 1 | `qa/qd3d/Displaying Windows 3DMF Files On A Mac.md` | 未开始 |
| 240 | Distorted Panoramas | 1 | `qa/qtvr/Distorted Panoramas.md` | 未开始 |
| 241 | Do I have to call CreateRootControl after creating my window? | 1 | `qa/qa2001/Do I have to call CreateRootControl after creating my window` | 未开始 |
| 242 | Do PowerBooks have a PCI bus? | 1 | `qa/hw/Do PowerBooks have a PCI bus` | 未开始 |
| 243 | Documentation updater for Project Builder shipping with Mac OS X 10.2 | 1 | `qa/qa2001/Documentation updater for Project Builder shipping with Mac OS X 10.2` | 未开始 |
| 244 | Does This Printer Support PostScript? | 1 | `qa/qd/Does This Printer Support PostScript.md` | 未开始 |
| 245 | Drag Manager & the -600 (procNotFound) Error | 1 | `qa/tb/Drag Manager & the -600 (procNotFound) Error` | 未开始 |
| 246 | Drag Manager and windowKind 20 | 1 | `qa/tb/Drag Manager and windowKind 20` | 未开始 |
| 247 | Dragging to the Trash | 1 | `qa/tb/Dragging to the Trash` | 未开始 |
| 248 | Drawing Text into a RAVE Context | 1 | `qa/qd3d/Drawing Text into a RAVE Context.md` | 未开始 |
| 249 | DriverServicesLib Queue Routines | 1 | `qa/dv/DriverServicesLib Queue Routines.md` | 未开始 |
| 250 | Dynamically registering a bundled component | 1 | `qa/Dynamically registering a bundled component.md` | 未开始 |
| 251 | Embedding a GX Picture into a PICT | 1 | `qa/gx/Embedding a GX Picture into a PICT` | 未开始 |
| 252 | Embedding a framework in an iMessage App | 1 | `qa/Embedding a framework in an iMessage App` | 未开始 |
| 253 | Enabling the Navigation Services default behavior in its dialogs | 1 | `qa/Enabling the Navigation Services default behavior in its dialogs.md` | 未开始 |
| 254 | Enabling the application menu's "Preferences..." menu item on Mac OS X | 1 | `qa/qa2001/Enabling the application menu's -Preferences...- menu item on Mac OS X` | 未开始 |
| 255 | EndFormsPrinting and FormsPrinting PicComments | 1 | `qa/qd/EndFormsPrinting and FormsPrinting PicComments.md` | 未开始 |
| 256 | Enumerating fonts with ATS | 1 | `qa/Enumerating fonts with ATS.md` | 未开始 |
| 257 | Equipment sources for QTVR movies | 1 | `qa/qtvr/Equipment sources for QTVR movies.md` | 未开始 |
| 258 | Error -151 and NewGWorld | 1 | `qa/qd/Error -151 and NewGWorld.md` | 未开始 |
| 259 | Error -3168 (kOTStateChangeErr) and Handoff Endpoints | 1 | `qa/nw/Error -3168 (kOTStateChangeErr) and Handoff Endpoints` | 未开始 |
| 260 | Error -8976 When Displaying JPEG-Compressed PICTS with DrawPicture | 1 | `qa/qd/Error -8976 When Displaying JPEG-Compressed PICTS with DrawPicture.md` | 未开始 |
| 261 | Error on Page 4-163 of QDGX Printing Extensions and Drivers | 1 | `qa/gxpd/Error on Page 4-163 of QDGX Printing Extensions and Drivers.md` | 未开始 |
| 262 | Errors in QADrawContextNew | 1 | `qa/qd3d/Errors in QADrawContextNew.md` | 未开始 |
| 263 | Errors on Symbol Names Longer than 64 Characters | 1 | `qa/tb/Errors on Symbol Names Longer than 64 Characters` | 未开始 |
| 264 | Ethernet Addresses | 1 | `qa/nw/Ethernet Addresses` | 未开始 |
| 265 | Ethernet Driver Interface | 1 | `qa/nw/Ethernet Driver Interface` | 未开始 |
| 266 | Ethernet Driver Message Blocks | 1 | `qa/hw/Ethernet Driver Message Blocks` | 未开始 |
| 267 | Ethernet Error on a PowerMac | 1 | `qa/nw/Ethernet Error on a PowerMac` | 未开始 |
| 268 | Exception in JFileChooser.setAcceptAllFileFilterUsed | 1 | `qa/qa2001/Exception in JFileChooser.setAcceptAllFileFilterUsed` | 未开始 |
| 269 | Excluding UVs When Building a Vertex List | 1 | `qa/qd3d/Excluding UVs When Building a Vertex List.md` | 未开始 |
| 270 | Expanding the System Heap | 1 | `qa/ops/Expanding the System Heap` | 未开始 |
| 271 | Explanation of SDRAM configuration Nomenclature | 1 | `qa/hw/Explanation of SDRAM configuration Nomenclature` | 未开始 |
| 272 | Explicitly Forcing PCI Burst Transfers | 1 | `qa/hw/Explicitly Forcing PCI Burst Transfers` | 未开始 |
| 273 | Exporting Light Groups in QuickDraw 3D | 1 | `qa/qd3d/Exporting Light Groups in QuickDraw 3D.md` | 未开始 |
| 274 | Exporting TIFF files in little-endian format | 1 | `qa/qa2001/Exporting TIFF files in little-endian format` | 未开始 |
| 275 | Extension Off, Macsbug On | 1 | `qa/plat/Extension Off, Macsbug On` | 未开始 |
| 276 | Extensions vs. Libraries | 1 | `qa/qd3d/Extensions vs. Libraries.md` | 未开始 |
| 277 | Extracting DV Fields using QTNewGWorldFromPtr | 1 | `qa/qa2001/Extracting DV Fields using QTNewGWorldFromPtr/qa1017.md` | 未开始 |
| 278 | Extracting InstaCompOne Archive Files | 1 | `qa/plat/Extracting InstaCompOne Archive Files` | 未开始 |
| 279 | FAT Code Resources | 1 | `qa/ppcsys/FAT Code Resources.md` | 未开始 |
| 280 | FCode & OS X | 1 | `qa/qa2001/FCode & OS X` | 未开始 |
| 281 | FDecompressImage, StdPix Bottleneck Calls During Printing | 1 | `qa/qd/FDecompressImage, StdPix Bottleneck Calls During Printing.md` | 未开始 |
| 282 | FWSendSoftwareInterrupt vs. SendSoftwareInterrupt | 1 | `qa/qa2001/FWSendSoftwareInterrupt vs. SendSoftwareInterrupt` | 未开始 |
| 283 | Faster DDR DRAM in the 867MHz Power Mac G4 (Mirrored Drive Doors) | 1 | `qa/qa2001/Faster DDR DRAM in the 867MHz Power Mac G4 (Mirrored Drive Doors)` | 未开始 |
| 284 | FetchTaggedData not Called Often | 1 | `qa/gxpd/FetchTaggedData not Called Often.md` | 未开始 |
| 285 | File Corruption with SCSI Manager 4.3 | 1 | `qa/dv/File Corruption with SCSI Manager 4.3.md` | 未开始 |
| 286 | Filtering QuickTime media types in Navigation Services | 1 | `qa/qa2001/Filtering QuickTime media types in Navigation Services` | 未开始 |
| 287 | Filtering the Effects List returned by QTGetEffectsList | 1 | `qa/qa2001/Filtering the Effects List returned by QTGetEffectsList` | 未开始 |
| 288 | Find Documents Folder | 1 | `qa/ops/Find Documents Folder` | 未开始 |
| 289 | Finder & AOCE | 1 | `qa/fl/Finder & AOCE.md` | 未开始 |
| 290 | Finding Missing OpenGL CFM Entry Points | 1 | `qa/qa2001/Finding Missing OpenGL CFM Entry Points` | 未开始 |
| 291 | Finding The Center Of A Model | 1 | `qa/qd3d/Finding The Center Of A Model.md` | 未开始 |
| 292 | Finding the VM Backing Store | 1 | `qa/me/Finding the VM Backing Store.md` | 未开始 |
| 293 | Finding the bit depth of a Carbon Printing Manager graphics context | 1 | `qa/qd/Finding the bit depth of a Carbon Printing Manager graphics context.md` | 未开始 |
| 294 | Fixed Math Rounding | 1 | `qa/ops/Fixed Math Rounding` | 未开始 |
| 295 | Fixing NSDocumentController to understand HFS file types | 1 | `qa/qa2001/Fixing NSDocumentController to understand HFS file types` | 未开始 |
| 296 | Fixing the Layout Binding of the Tab control User Panes | 1 | `qa/Fixing the Layout Binding of the Tab control User Panes` | 未开始 |
| 297 | Fixing the crash in the Picture Sharing code example | 1 | `qa/qa2001/Fixing the crash in the Picture Sharing code example` | 未开始 |
| 298 | Flattening Objects Separately | 1 | `qa/gxpd/Flattening Objects Separately.md` | 未开始 |
| 299 | Fonts not Appearing in Spool File | 1 | `qa/qd/Fonts not Appearing in Spool File.md` | 未开始 |
| 300 | Forcing TextEdit To Draw Over a Background Image | 1 | `qa/tx/Forcing TextEdit To Draw Over a Background Image.md` | 未开始 |
| 301 | FrontBase and JDBC | 1 | `qa/qa2001/FrontBase and JDBC` | 未开始 |
| 302 | Functions that Modify Movie Properties, QuickTime Track, and Movie Sound Volume | 1 | `qa/qtmtb/Functions that Modify Movie Properties, QuickTime Track, and Movie Sound Volume.md` | 未开始 |
| 303 | GDGetScale | 1 | `qa/qticm/GDGetScale.md` | 未开始 |
| 304 | GDHasScale | 1 | `qa/qticm/GDHasScale.md` | 未开始 |
| 305 | GDSetScale | 1 | `qa/qticm/GDSetScale.md` | 未开始 |
| 306 | GWorld in the 'grafPort' Field of a MacDrawContext Struct | 1 | `qa/qd3d/GWorld in the 'grafPort' Field of a MacDrawContext Struct.md` | 未开始 |
| 307 | GX 'comm' Resource Type | 1 | `qa/gxpd/GX 'comm' Resource Type.md` | 未开始 |
| 308 | GXGetShapeLocalBounds Call | 1 | `qa/gx/GXGetShapeLocalBounds Call` | 未开始 |
| 309 | Gathering all PostScript Printer Descriptions (PPDs) | 1 | `qa/Gathering all PostScript Printer Descriptions (PPDs).md` | 未开始 |
| 310 | Gathering system information under Traditional Mac OS | 1 | `qa/qa2001/Gathering system information under Traditional Mac OS` | 未开始 |
| 311 | Gestalt Selectors for Macintosh Networking | 1 | `qa/nw/Gestalt Selectors for Macintosh Networking` | 未开始 |
| 312 | GetDIBFromPict fails with QuickTime "Minimum" installation | 1 | `qa/GetDIBFromPict fails with QuickTime -Minimum- installation.md` | 未开始 |
| 313 | GetDriverDiskFragment and 'ndrv' Drivers | 1 | `qa/hw/GetDriverDiskFragment and 'ndrv' Drivers` | 未开始 |
| 314 | GetPortBitMapForCopyBits | 1 | `qa/qd/GetPortBitMapForCopyBits.md` | 未开始 |
| 315 | Getting Default Settings for a Given Font | 1 | `qa/gxty/Getting Default Settings for a Given Font.md` | 未开始 |
| 316 | Getting Records From the OCE Catalog Manager | 1 | `qa/nw/Getting Records From the OCE Catalog Manager` | 未开始 |
| 317 | Getting Started with Network Programming | 1 | `qa/nw/Getting Started with Network Programming` | 未开始 |
| 318 | Getting a List of Drivers & LUNs (logical unit numbers) | 1 | `qa/dv/Getting a List of Drivers & LUNs (logical unit numbers).md` | 未开始 |
| 319 | Getting the Processor Type and Speed on a PCI Mac | 1 | `qa/hw/Getting the Processor Type and Speed on a PCI Mac` | 未开始 |
| 320 | Graphics Exporters - Creating 16-bit-per-channel image files | 1 | `qa/Graphics Exporters - Creating 16-bit-per-channel image files.md` | 未开始 |
| 321 | Graphics Importer -8970 errors & TIFF Support | 1 | `qa/qtmcc/Graphics Importer -8970 errors & TIFF Support.md` | 未开始 |
| 322 | Graphics Importers and image files containing multiple layers | 1 | `qa/qa2001/Graphics Importers and image files containing multiple layers` | 未开始 |
| 323 | GraphicsImportSetBoundsRect resets your Matrix | 1 | `qa/qa2001/GraphicsImportSetBoundsRect resets your Matrix` | 未开始 |
| 324 | GrayShare Software Update | 1 | `qa/qd/GrayShare Software Update.md` | 未开始 |
| 325 | Grayscale Printing on a LaserWriter LS | 1 | `qa/qd/Grayscale Printing on a LaserWriter LS.md` | 未开始 |
| 326 | Greenwich Mean Time offsets and the Map control panel | 1 | `qa/ops/Greenwich Mean Time offsets and the Map control panel` | 未开始 |
| 327 | Guide Maker 1.2.7 Fixes PowerTalk Crashes | 1 | `qa/hs/Guide Maker 1.2.7 Fixes PowerTalk Crashes.md` | 未开始 |
| 328 | HIObjectRegisterSubclass returns paramErr | 1 | `qa/qa2001/HIObjectRegisterSubclass returns paramErr` | 未开始 |
| 329 | HMShowBalloon styled TEHandle limit and Workaround | 1 | `qa/tb/HMShowBalloon styled TEHandle limit and Workaround` | 未开始 |
| 330 | Handling of Update Events While a Movie Plays | 1 | `qa/qtmtb/Handling of Update Events While a Movie Plays.md` | 未开始 |
| 331 | Header Conditions | 1 | `qa/qd3d/Header Conditions.md` | 未开始 |
| 332 | Help Book Caching During Software Development | 1 | `qa/Help Book Caching During Software Development.md` | 未开始 |
| 333 | Hey Siri, How Can I Improve the Recognition of My App's Name? | 1 | `qa/Hey Siri, How Can I Improve the Recognition of My App's Name` | 未开始 |
| 334 | Hidden Volumes in HFS | 1 | `qa/fl/Hidden Volumes in HFS.md` | 未开始 |
| 335 | Hiding public methods from AppleScript in Java | 1 | `qa/java/Hiding public methods from AppleScript in Java` | 未开始 |
| 336 | Highlight State | 1 | `qa/qd3d/Highlight State.md` | 未开始 |
| 337 | How PBDTGetAPPL Chooses Which Copy of an App to Launch | 1 | `qa/tb/How PBDTGetAPPL Chooses Which Copy of an App to Launch` | 未开始 |
| 338 | How can I add the ability to read and write Keynote 2 documents to my application? | 1 | `qa/qa2005/How can I add the ability to read and write Keynote 2 documents to my applicatio` | 未开始 |
| 339 | How can I find out what non-RGB pixel formats a codec supports? | 1 | `qa/How can I find out what non-RGB pixel formats a codec supports.md` | 未开始 |
| 340 | How can I handle smooth mouse wheel scrolling? | 1 | `qa/How can I handle smooth mouse wheel scrolling.md` | 未开始 |
| 341 | How can I set the default location with the modern Navigation APIs NavCreatexxx? | 1 | `qa/qa2001/How can I set the default location with the modern Navigation APIs NavCreatexxx` | 未开始 |
| 342 | How can I verify that a Movie can actually draw into a non-RGB GWorld? | 1 | `qa/qa2001/How can I verify that a Movie can actually draw into a non-RGB GWorld` | 未开始 |
| 343 | How can I work with MPEG-2 media using QuickTime? | 1 | `qa/How can I work with MPEG-2 media using QuickTime.md` | 未开始 |
| 344 | How do I access files contained in my AppleScript Studio application's main | 1 | `qa/How do I access files contained in my AppleScript Studio application's main bund` | 未开始 |
| 345 | How do I change the numeric base for the Open Firmware user interface? | 1 | `qa/hw/How do I change the numeric base for the Open Firmware user interface` | 未开始 |
| 346 | How do I count the frames in an MPEG movie? | 1 | `qa/How do I count the frames in an MPEG movie.md` | 未开始 |
| 347 | How do I create a QuickTime movie from PCM audio samples in memory? | 1 | `qa/How do I create a QuickTime movie from PCM audio samples in memory.md` | 未开始 |
| 348 | How do I decompress individual frames into an offscreen? | 1 | `qa/qtmtb/How do I decompress individual frames into an offscreen.md` | 未开始 |
| 349 | How do I determine the top of the Open Firmware dictionary? | 1 | `qa/hw/How do I determine the top of the Open Firmware dictionary` | 未开始 |
| 350 | How do I ring the Doorbell? | 1 | `qa/fw/How do I ring the Doorbell` | 未开始 |
| 351 | How do I use PMSessionGetGraphicsContext to get a CGContextRef? | 1 | `qa/qa2001/How do I use PMSessionGetGraphicsContext to get a CGContextRef` | 未开始 |
| 352 | How do I use QuickDraw with CGDirectDisplay? | 1 | `qa/qa2001/How do I use QuickDraw with CGDirectDisplay` | 未开始 |
| 353 | How does Open Firmware generate the name property? | 1 | `qa/hw/How does Open Firmware generate the name property` | 未开始 |
| 354 | How to Compute Data Rate for QuickTime Movies | 1 | `qa/qtmtb/How to Compute Data Rate for QuickTime Movies.md` | 未开始 |
| 355 | How to Disable the JIT | 1 | `qa/java/Stack Crawl Not Showing Line Numbers/Legacy Documentclose button-2.md` | 未开始 |
| 356 | How to Find the Printer Descriptions folder | 1 | `qa/qd/How to Find the Printer Descriptions folder.md` | 未开始 |
| 357 | How to Get the First Video Frame | 1 | `qa/qtmcc/How to Get the First Video Frame.md` | 未开始 |
| 358 | How to Tell Whether a Picture is QuickTime-Compressed | 1 | `qa/qticm/How to Tell Whether a Picture is QuickTime-Compressed.md` | 未开始 |
| 359 | How to define a plst resource in a .r file | 1 | `qa/qa2001/How to define a plst resource in a .r file` | 未开始 |
| 360 | How to get a native QuickTime movie object from the QuickTime ActiveX/COM control | 1 | `qa/How to get a native QuickTime movie object from the QuickTime ActiveX-COM contro.md` | 未开始 |
| 361 | How to get the Monitor ID as displayed in the Monitors & Sound Control Panel | 1 | `qa/qd/How to get the Monitor ID as displayed in the Monitors & Sound Control Panel.md` | 未开始 |
| 362 | How to solve '_objc_exception_set_functions' ZeroLink errors in Xcode | 1 | `qa/qa2001/How to solve 'objcexceptionsetfunctions' ZeroLink errors in Xcode` | 未开始 |
| 363 | How to use URL Access with proxy servers | 1 | `qa/qa2001/How to use URL Access with proxy servers` | 未开始 |
| 364 | How to use the OT modem script engine | 1 | `qa/nw/How to use the OT modem script engine` | 未开始 |
| 365 | How to work around HIMovieViewCreate failing | 1 | `qa/How to work around HIMovieViewCreate failing` | 未开始 |
| 366 | ICLaunchURL, "file:///" URLs and Mac OS X | 1 | `qa/qa2001/ICLaunchURL, -file----- URLs and Mac OS X` | 未开始 |
| 367 | Icon Families | 1 | `qa/tb/Icon Families` | 未开始 |
| 368 | Identically-Sized Print Files with LW 8.x | 1 | `qa/qd/Identically-Sized Print Files with LW 8.x.md` | 未开始 |
| 369 | Image Compression Dialog Options | 1 | `qa/qticm/Image Compression Dialog Options.md` | 未开始 |
| 370 | Image Decompressor Data-loading Procs | 1 | `qa/qtmcc/Image Decompressor Data-loading Procs.md` | 未开始 |
| 371 | ImageDescription Extension Format | 1 | `qa/qtmcc/ImageDescription Extension Format.md` | 未开始 |
| 372 | Implementing DLLs | 1 | `qa/nw/Implementing DLLs` | 未开始 |
| 373 | Implementing MacsBug-Compatible USB Keyboard and Mouse Drivers | 1 | `qa/usb/Implementing MacsBug-Compatible USB Keyboard and Mouse Drivers.md` | 未开始 |
| 374 | Implementing a CVFillExtendedPixelsCallBack | 1 | `qa/qa2005/Implementing a CVFillExtendedPixelsCallBack` | 未开始 |
| 375 | Implementing read-modify-write on PCI | 1 | `qa/hw/Implementing read-modify-write on PCI` | 未开始 |
| 376 | Importer Components - What is the 'mcfg' resource used for? | 1 | `qa/Importer Components - What is the 'mcfg' resource used for` | 未开始 |
| 377 | Importing Non-PICT Files Into Apple Media Tool | 1 | `qa/amt pe/Importing Non-PICT Files Into Apple Media Tool.md` | 未开始 |
| 378 | Importing Sys 7 Snds | 1 | `qa/qtmcc/Importing Sys 7 Snds.md` | 未开始 |
| 379 | Importing image data from memory | 1 | `qa/qtmtb/Importing image data from memory.md` | 未开始 |
| 380 | Impossibility of Extracting File System Information from the WindowPtr | 1 | `qa/ops/Impossibility of Extracting File System Information from the WindowPtr` | 未开始 |
| 381 | Improper Texture Mapping with Trigrids | 1 | `qa/qd3d/Improper Texture Mapping with Trigrids.md` | 未开始 |
| 382 | Improving ATSUI Text Drawing Performance | 1 | `qa/qa2001/Improving ATSUI Text Drawing Performance` | 未开始 |
| 383 | Including the Cursor in a Screen Capture when using CopyBits | 1 | `qa/qd/Including the Cursor in a Screen Capture when using CopyBits.md` | 未开始 |
| 384 | Inconsistencies, LaserWriter 'xdtl', adding a padByte | 1 | `qa/gxpd/Inconsistencies, LaserWriter 'xdtl', adding a padByte.md` | 未开始 |
| 385 | Incorrect Inside Macintosh Volume V documentation | 1 | `qa/qd/Incorrect Inside Macintosh Volume V documentation.md` | 未开始 |
| 386 | Incorrect Paper Size with QuickDraw GX 1.1.2 | 1 | `qa/gxpd/Incorrect Paper Size with QuickDraw GX 1.1.2.md` | 未开始 |
| 387 | Inputting characters using InputMethod | 1 | `qa/java/Inputting characters using InputMethod` | 未开始 |
| 388 | Integrating the QuickTime for Windows 7.0.3 Installer into your Application | 1 | `qa/Integrating the QuickTime for Windows 7.0.3 Installer into your Application Inst.md` | 未开始 |
| 389 | Interactive Renderer Not Drawing Flat Surfaces | 1 | `qa/qd3d/Interactive Renderer Not Drawing Flat Surfaces.md` | 未开始 |
| 390 | Intercepting QuickTime Wired Actions | 1 | `qa/qa2001/Intercepting QuickTime Wired Actions` | 未开始 |
| 391 | Intercepting movie controller actions | 1 | `qa/qa2001/Intercepting movie controller actions` | 未开始 |
| 392 | InterfaceLib and Native Drivers | 1 | `qa/dv/Coordinating Deferred Tasks and Secondary Interrupts/Legacy Documentclose button-2.md` | 未开始 |
| 393 | Interrupt Management | 1 | `qa/hw/Interrupt Management` | 未开始 |
| 394 | Invisibility of ColorSync Accelerators | 1 | `qa/c/Invisibility of ColorSync Accelerators` | 未开始 |
| 395 | Invoking the Open Firmware user interface | 1 | `qa/hw/Invoking the Open Firmware user interface` | 未开始 |
| 396 | Is QuickTime thread-safe? | 1 | `qa/Is QuickTime thread-safe.md` | 未开始 |
| 397 | Is SCSI Manager 4.3 Emulated? | 1 | `qa/dv/Is SCSI Manager 4.3 Emulated.md` | 未开始 |
| 398 | Is there a relationship between the device tree and the Name Registry? | 1 | `qa/hw/Is there a relationship between the device tree and the Name Registry` | 未开始 |
| 399 | JBound App Results in -35 OSErr | 1 | `qa/java/JBound App Results in -35 OSErr` | 未开始 |
| 400 | Java File Paths are not Unix File Paths | 1 | `qa/java/Java File Paths are not Unix File Paths` | 未开始 |
| 401 | Jumpy Mouse when Transferring Data on PowerMacs | 1 | `qa/dv/Jumpy Mouse when Transferring Data on PowerMacs.md` | 未开始 |
| 402 | Kanji & PostScript Printing | 1 | `qa/qd/Kanji & PostScript Printing.md` | 未开始 |
| 403 | Kanji and Special Text-Processing | 1 | `qa/tx/Kanji and Special Text-Processing.md` | 未开始 |
| 404 | Keyframes and AddMediaSample | 1 | `qa/qtmcc/Keyframes and AddMediaSample.md` | 未开始 |
| 405 | Keywords Dropped from 3DMF Specification | 1 | `qa/qd3d/Keywords Dropped from 3DMF Specification.md` | 未开始 |
| 406 | LMGetTheMenu and LMSetMenuHook | 1 | `qa/tb/LMGetTheMenu and LMSetMenuHook` | 未开始 |
| 407 | LaserWriter 7.5.2 Printing Update 1.1 | 1 | `qa/qd/LaserWriter 7.5.2 Printing Update 1.1.md` | 未开始 |
| 408 | LaserWriter 8 Local Customization File | 1 | `qa/qd/LaserWriter 8 Local Customization File.md` | 未开始 |
| 409 | LaserWriter 8 Support for *JCL/PCL | 1 | `qa/qd/LaserWriter 8 Support for JCL-PCL.md` | 未开始 |
| 410 | LaserWriter 8.4.x - Custom page size support | 1 | `qa/qd/LaserWriter 8.4.x - Custom page size support.md` | 未开始 |
| 411 | LaserWriter Drivers - Which Are ColorSync Aware? | 1 | `qa/qd/LaserWriter Drivers - Which Are ColorSync Aware.md` | 未开始 |
| 412 | LaserWriter GX CustomDialogs Sample | 1 | `qa/gxpd/LaserWriter GX CustomDialogs Sample.md` | 未开始 |
| 413 | Late breaking news for the MacsBug gdb plugin | 1 | `qa/qa2001/Late breaking news for the MacsBug gdb plugin` | 未开始 |
| 414 | Launching a PICT from a Panorama | 1 | `qa/qtvr/Launching a PICT from a Panorama.md` | 未开始 |
| 415 | Launching the Default Internet Browser | 1 | `qa/nw/Launching the Default Internet Browser` | 未开始 |
| 416 | Legacy Devices | 1 | `qa/hw/Legacy Devices` | 未开始 |
| 417 | Light Color | 1 | `qa/qd3d/Light Color.md` | 未开始 |
| 418 | Limitations of ShowDragHilite | 1 | `qa/tb/Limitations of ShowDragHilite` | 未开始 |
| 419 | Limitations of the Apple QuickDraw 3D Acceleration Card | 1 | `qa/qd3d/Limitations of the Apple QuickDraw 3D Acceleration Card.md` | 未开始 |
| 420 | Limitations to Menu Item Size under Menu Manager | 1 | `qa/tb/Limitations to Menu Item Size under Menu Manager` | 未开始 |
| 421 | Limiting the component list in SCRequestImageSettings | 1 | `qa/Limiting the component list in SCRequestImageSettings.md` | 未开始 |
| 422 | Linked Movies with Different Color Palettes | 1 | `qa/qtmrf/Linked Movies with Different Color Palettes.md` | 未开始 |
| 423 | List Manager & LClick | 1 | `qa/tb/List Manager & LClick` | 未开始 |
| 424 | Loading Applications Without QD3D | 1 | `qa/qd3d/Loading Applications Without QD3D.md` | 未开始 |
| 425 | Localization Problems with Apps for Japan | 1 | `qa/tx/Localization Problems with Apps for Japan.md` | 未开始 |
| 426 | Localized Versions of Appearance SDK | 1 | `qa/tb/Localized Versions of Appearance SDK` | 未开始 |
| 427 | Locating a Font's Home File | 1 | `qa/tb/Locating a Font's Home File` | 未开始 |
| 428 | Locating the 1275-1994 Standard Document | 1 | `qa/hw/Locating the 1275-1994 Standard Document` | 未开始 |
| 429 | Locating the Selected Printer | 1 | `qa/gxpd/Locating the Selected Printer.md` | 未开始 |
| 430 | LockPixels and DisposeGWorld with QTNewGWorldFromPtr | 1 | `qa/qa2001/Extracting DV Fields using QTNewGWorldFromPtr/qa1007.md` | 未开始 |
| 431 | Locking an Area Using PBLockRange | 1 | `qa/ops/Locking an Area Using PBLockRange` | 未开始 |
| 432 | Long Timeout When Opening Certain Files - A StyleWriter Quirk | 1 | `qa/qd/Long Timeout When Opening Certain Files - A StyleWriter Quirk.md` | 未开始 |
| 433 | Looping Audio Files with QuickTime for Windows | 1 | `qa/Looping Audio Files with QuickTime for Windows.md` | 未开始 |
| 434 | MACE Restrictions | 1 | `qa/snd/MACE Restrictions.md` | 未开始 |
| 435 | MCSetClip and Clipping with the Movie Controller | 1 | `qa/qtmtb/MCSetClip and Clipping with the Movie Controller.md` | 未开始 |
| 436 | MPEG Compression in QuickTime | 1 | `qa/qticm/MPEG Compression in QuickTime.md` | 未开始 |
| 437 | MPRemoteCall Contexts | 1 | `qa/qa2001/MPRemoteCall Contexts` | 未开始 |
| 438 | MPW Tool Not Found | 1 | `qa/qtvr/MPW Tool Not Found.md` | 未开始 |
| 439 | MacTCP | 1 | `qa/nw/MacTCP` | 未开始 |
| 440 | MacTCP I/O | 1 | `qa/plat/MacTCP I-O` | 未开始 |
| 441 | MacTCP and UDP Performance | 1 | `qa/nw/MacTCP and UDP Performance` | 未开始 |
| 442 | Macintosh Quadra 700 and 900 SCSI Chip Anomaly and Fix | 1 | `qa/dv/Macintosh Quadra 700 and 900 SCSI Chip Anomaly and Fix.md` | 未开始 |
| 443 | Macintosh Quadra SCSI Data Transfer | 1 | `qa/dv/Macintosh Quadra SCSI Data Transfer.md` | 未开始 |
| 444 | Macintosh Quadra and SCSI Termination | 1 | `qa/dv/Macintosh Quadra and SCSI Termination.md` | 未开始 |
| 445 | Make sure your PPD Plugin calls ppdCloseCompiledPPDFromTicket | 1 | `qa/qa2001/Make sure your PPD Plugin calls ppdCloseCompiledPPDFromTicket` | 未开始 |
| 446 | Makefiles Problems | 1 | `qa/plat/Makefiles Problems` | 未开始 |
| 447 | Making Data Executable | 1 | `qa/ops/Making Data Executable` | 未开始 |
| 448 | Making Input Gain Setting Changes | 1 | `qa/snd/Making Input Gain Setting Changes.md` | 未开始 |
| 449 | Making Objects Invisible | 1 | `qa/qd3d/Making Objects Invisible.md` | 未开始 |
| 450 | Making Sure the Object Will Spin without Stopping | 1 | `qa/qtvr/Making Sure the Object Will Spin without Stopping.md` | 未开始 |
| 451 | Making the ADBOp call from CFM-68K | 1 | `qa/hw/Making the ADBOp call from CFM-68K` | 未开始 |
| 452 | Managing custom drawing code in a compositing world | 1 | `qa/Managing custom drawing code in a compositing world.md` | 未开始 |
| 453 | Mapping OT Error Numbers to theirNames | 1 | `qa/nw/Mapping OT Error Numbers to theirNames` | 未开始 |
| 454 | Maximum Memory for the "Firewire" PowerBook | 1 | `qa/hw/Maximum Memory for the -Firewire- PowerBook` | 未开始 |
| 455 | Maximum Number of Menu Items | 1 | `qa/tb/Maximum Number of Menu Items` | 未开始 |
| 456 | Maximum number of fonts | 1 | `qa/tx/Maximum number of fonts.md` | 未开始 |
| 457 | MemAllocatePhysicallyContiguous | 1 | `qa/dv/MemAllocatePhysicallyContiguous/Legacy Documentclose button.md` | 未开始 |
| 458 | MemError | 1 | `qa/me/MemError.md` | 未开始 |
| 459 | Memory Problems, Avoiding Blank Frames | 1 | `qa/qtvr/Memory Problems, Avoiding Blank Frames.md` | 未开始 |
| 460 | Memory Requirements | 1 | `qa/plat/Memory Requirements` | 未开始 |
| 461 | Menu Bar Clock and NVRAM | 1 | `qa/qa2001/Menu Bar Clock and NVRAM` | 未开始 |
| 462 | Menu Definition Drawing Dimmed Items | 1 | `qa/tb/Menu Definition Drawing Dimmed Items` | 未开始 |
| 463 | Menu Issues, Drawing, Removal & Increasing Size | 1 | `qa/tb/Menu Issues, Drawing, Removal & Increasing Size` | 未开始 |
| 464 | Menus & Hardware Accelerated OpenGL under Mac OS 9 Carbon | 1 | `qa/qa2001/Menus & Hardware Accelerated OpenGL under Mac OS 9 Carbon` | 未开始 |
| 465 | Mesh Edge Structure Can Not Have More Than 2 Faces | 1 | `qa/qd3d/Mesh Edge Structure Can Not Have More Than 2 Faces.md` | 未开始 |
| 466 | Metafile Specification Discrepancies | 1 | `qa/qd3d/Metafile Specification Discrepancies.md` | 未开始 |
| 467 | Missing Geometries in QuickDraw 3D 1.0.X | 1 | `qa/qd3d/Missing Geometries in QuickDraw 3D 1.0.X.md` | 未开始 |
| 468 | Missing Low Memory Globals | 1 | `qa/plat/Missing Low Memory Globals` | 未开始 |
| 469 | Modifying Image Metadata Without Recompressing Image | 1 | `qa/Modifying Image Metadata Without Recompressing Image.md` | 未开始 |
| 470 | More Choices and Scroll Bar not Working in Print Dialog | 1 | `qa/gxpd/More Choices and Scroll Bar not Working in Print Dialog.md` | 未开始 |
| 471 | Mounting a Remote File System | 1 | `qa/nw/Mounting a Remote File System` | 未开始 |
| 472 | Movie Drawing Complete Procedure with C++ | 1 | `qa/qa2001/Movie Drawing Complete Procedure with C++` | 未开始 |
| 473 | Movie Export - Always fill in the MovieExportGetDataParams dataSize field | 1 | `qa/Movie Export - Always fill in the MovieExportGetDataParams dataSize field.md` | 未开始 |
| 474 | Movie Export Components - Supporting a MovieProgressProc | 1 | `qa/qa2001/Movie Export Components - Supporting a MovieProgressProc` | 未开始 |
| 475 | Movie Export From Procedures - Providing k2vuyPixelFormat data to MovieExportGetDataProc | 1 | `qa/Movie Export From Procedures - Providing k2vuyPixelFormat data to MovieExportGet` | 未开始 |
| 476 | Movie Import Component Selectors | 1 | `qa/qtmcc/Movie Import Component Selectors.md` | 未开始 |
| 477 | Movie Import Components - MovieImportDataRef Invoked For File Import Operations | 1 | `qa/Movie Import Components - MovieImportDataRef Invoked For File Import Operations.md` | 未开始 |
| 478 | Movie export with AMR audio | 1 | `qa/Movie export with AMR audio.md` | 未开始 |
| 479 | MovieAudioExtraction - Ensure a Movie is fully loaded before starting an extraction | 1 | `qa/MovieAudioExtraction - Ensure a Movie is fully loaded before starting an extract.md` | 未开始 |
| 480 | MovieAudioExtraction - Extracting all available audio samples | 1 | `qa/MovieAudioExtraction - Extracting all available audio samples.md` | 未开始 |
| 481 | Movies - Saving movie playback hints | 1 | `qa/Movies - Saving movie playback hints.md` | 未开始 |
| 482 | Moving Code in DespoolPage to GXSetUpPageImageData | 1 | `qa/gxpd/Moving Code in DespoolPage to GXSetUpPageImageData.md` | 未开始 |
| 483 | Moving Files in Java | 1 | `qa/java/Moving Files in Java` | 未开始 |
| 484 | Moving the Menu Bar | 1 | `qa/tb/Moving the Menu Bar` | 未开始 |
| 485 | Multiple Resources with the Same Type and ID | 1 | `qa/tb/Multiple Resources with the Same Type and ID` | 未开始 |
| 486 | My ListBox control works fine on Mac OS X but I get a crash on Mac OS 9 when | 1 | `qa/qa2001/My ListBox control works fine on Mac OS X but I get a crash on Mac OS 9 when I c` | 未开始 |
| 487 | My custom item dismisses my Navigation Services dialog | 1 | `qa/My custom item dismisses my Navigation Services dialog.md` | 未开始 |
| 488 | NSL and Custom Thread Context-Switching Functions | 1 | `qa/nw/NSL and Custom Thread Context-Switching Functions` | 未开始 |
| 489 | NSL and how it relates to Bonjour | 1 | `qa/NSL and how it relates to Bonjour.md` | 未开始 |
| 490 | Native App Slowdown | 1 | `qa/tb/Native App Slowdown` | 未开始 |
| 491 | Native App Slowdown | 1 | `qa/ppcsys/Native App Slowdown.md` | 未开始 |
| 492 | Native Disk Driver Debugging | 1 | `qa/dv/Native Disk Driver Debugging.md` | 未开始 |
| 493 | Native Drivers ('ndrv's) and dNeedTime | 1 | `qa/dv/Native Drivers ('ndrv's) and dNeedTime/Legacy Documentclose button.md` | 未开始 |
| 494 | Native QuickDraw Hardware Acceleration notSrcCopy Blits | 1 | `qa/qd/Native QuickDraw Hardware Acceleration notSrcCopy Blits.md` | 未开始 |
| 495 | Navigation Services Versions | 1 | `qa/tb/Navigation Services Versions` | 未开始 |
| 496 | Navigation Services and memFullErr | 1 | `qa/tb/Navigation Services and memFullErr` | 未开始 |
| 497 | Necessity of Calling PrJobDialog | 1 | `qa/qd/Necessity of Calling PrJobDialog.md` | 未开始 |
| 498 | New MacApp Release Approach | 1 | `qa/plat/New MacApp Release Approach` | 未开始 |
| 499 | New Monitor Related Playback Calls | 1 | `qa/qticm/New Monitor Related Playback Calls.md` | 未开始 |
| 500 | NewMovieFromScrap, Adding the Media Later | 1 | `qa/qtmtb/NewMovieFromScrap, Adding the Media Later.md` | 未开始 |
| 501 | NewRoutineDescriptor & Porting 68K code to PPC | 1 | `qa/ppcsys/NewRoutineDescriptor & Porting 68K code to PPC.md` | 未开始 |
| 502 | No Limit To The Number Of Vertices In A Polygon | 1 | `qa/qd3d/No Limit To The Number Of Vertices In A Polygon.md` | 未开始 |
| 503 | No Standard UV Parameters For Mesh | 1 | `qa/qd3d/No Standard UV Parameters For Mesh.md` | 未开始 |
| 504 | Non Mac OS X Bundled data-fork based Resources | 1 | `qa/qa2001/Non Mac OS X Bundled data-fork based Resources` | 未开始 |
| 505 | Non-consensual Contextual Menu Manager Plug-ins | 1 | `qa/tb/Non-consensual Contextual Menu Manager Plug-ins` | 未开始 |
| 506 | Normal Line of Object Pick | 1 | `qa/qd3d/Normal Line of Object Pick.md` | 未开始 |
| 507 | Notification Manager Reinitialized During Boot | 1 | `qa/ops/Notification Manager Reinitialized During Boot` | 未开始 |
| 508 | NuBus Declaration ROM | 1 | `qa/hw/NuBus Declaration ROM` | 未开始 |
| 509 | NuBus Timing Problem | 1 | `qa/hw/NuBus Timing Problem` | 未开始 |
| 510 | OT Driver returns EINVAL error for TCP/IP program, but AppleTalk works fine | 1 | `qa/nw/OT Driver returns EINVAL error for TCP-IP program, but AppleTalk works fine` | 未开始 |
| 511 | OT Serial Port I/O Handshaking | 1 | `qa/nw/OT Serial Port I-O Handshaking` | 未开始 |
| 512 | OTScheduleDeferredTask When Task Running | 1 | `qa/nw/OTScheduleDeferredTask When Task Running` | 未开始 |
| 513 | OTScheduleSystemTask Cleanup | 1 | `qa/nw/OTScheduleSystemTask Cleanup` | 未开始 |
| 514 | Obtaining Standard Icons | 1 | `qa/tb/Obtaining Standard Icons` | 未开始 |
| 515 | Obtaining a List of Volumes from a Server Programmatically | 1 | `qa/nw/Obtaining a List of Volumes from a Server Programmatically` | 未开始 |
| 516 | Open Firmware Memory bus speed | 1 | `qa/hw/Open Firmware Memory bus speed` | 未开始 |
| 517 | Open Firmware device tree nodes | 1 | `qa/hw/Open Firmware device tree nodes` | 未开始 |
| 518 | Open Firmware version number | 1 | `qa/hw/Open Firmware version number` | 未开始 |
| 519 | Open Transport Errors -3151/-3160 and Option Management | 1 | `qa/nw/Open Transport Errors -3151--3160 and Option Management` | 未开始 |
| 520 | Open Transport Libraries | 1 | `qa/nw/Open Transport Libraries` | 未开始 |
| 521 | Open Transport T_DATA Event Queuing | 1 | `qa/nw/Open Transport TDATA Event Queuing` | 未开始 |
| 522 | Open Transport Versions | 1 | `qa/nw/Open Transport Versions` | 未开始 |
| 523 | Open Transport's Limited Compatibility with 680x0 | 1 | `qa/nw/68K Open Transport Code on Power Macintoshes/Legacy Documentclose button.md` | 未开始 |
| 524 | OpenGL Texture Sharing Between Contexts | 1 | `qa/qa2001/OpenGL Texture Sharing Between Contexts` | 未开始 |
| 525 | OpenGL and 3D Graphics Changes in Mac OS X v10.2.3 | 1 | `qa/qa2001/OpenGL and 3D Graphics Changes in Mac OS X v10.2.3` | 未开始 |
| 526 | OpenGL and 3D Graphics Changes in Mac OS X v10.2.4 | 1 | `qa/qa2001/OpenGL and 3D Graphics Changes in Mac OS X v10.2.4` | 未开始 |
| 527 | OpenGL and 3D Graphics Changes in Mac OS X v10.2.5 | 1 | `qa/qa2001/OpenGL and 3D Graphics Changes in Mac OS X v10.2.5` | 未开始 |
| 528 | Opening a Web page using an HREF track in QuickTime Player | 1 | `qa/Opening a Web page using an HREF track in QuickTime Player.md` | 未开始 |
| 529 | Order for using the Scene Editor | 1 | `qa/qtvr/Order for using the Scene Editor.md` | 未开始 |
| 530 | PBLockRange with a zero-length range | 1 | `qa/fl/PBLockRange with a zero-length range.md` | 未开始 |
| 531 | PBXGetVolInfo Glue | 1 | `qa/fl/Determining volume size/Legacy Documentclose button-2.md` | 未开始 |
| 532 | PC Card 3.x Custom Actions | 1 | `qa/dv/PC Card 3.x Custom Actions.md` | 未开始 |
| 533 | PC card Voltage Sense line issues with 5-volt only cards | 1 | `qa/hw/PC card Voltage Sense line issues with 5-volt only cards` | 未开始 |
| 534 | PC100 SDRAM DIMMs on the Flat Panel iMac | 1 | `qa/qa2001/PC100 SDRAM DIMMs on the Flat Panel iMac` | 未开始 |
| 535 | PCI Bus Performance with Memory Read and Memory Read Multiple Commands | 1 | `qa/hw/PCI Bus Performance with Memory Read and Memory Read Multiple Commands` | 未开始 |
| 536 | PCI Bus and IEEE Standards | 1 | `qa/hw/PCI Bus and IEEE Standards` | 未开始 |
| 537 | PCI Card's Assigned-Address Properties | 1 | `qa/hw/PCI Card's Assigned-Address Properties` | 未开始 |
| 538 | PCI Device and Driver Matching | 1 | `qa/hw/PCI Device and Driver Matching` | 未开始 |
| 539 | PCI Header types | 1 | `qa/hw/PCI Header types` | 未开始 |
| 540 | PCI Interrupts | 1 | `qa/hw/PCI Interrupts` | 未开始 |
| 541 | PCI Macintoshes and CardBus controllers | 1 | `qa/hw/PCI Macintoshes and CardBus controllers` | 未开始 |
| 542 | PCI Support for the ISA Style Bracket | 1 | `qa/hw/PCI Support for the ISA Style Bracket` | 未开始 |
| 543 | PCI Throughput Issues | 1 | `qa/dv/PCI Throughput Issues.md` | 未开始 |
| 544 | PCI Video Card Bus Error | 1 | `qa/qd/PCI Video Card Bus Error.md` | 未开始 |
| 545 | PCI bus on the iMac | 1 | `qa/hw/PCI bus on the iMac` | 未开始 |
| 546 | PCI/PCI-X slots on the Power Mac G5 | 1 | `qa/qa2001/PCI-PCI-X slots on the Power Mac G5` | 未开始 |
| 547 | PDD File Format API | 1 | `qa/gxpd/PDD File Format API.md` | 未开始 |
| 548 | PICT, QuickTime-Compressed Testing | 1 | `qa/qticm/PICT, QuickTime-Compressed Testing.md` | 未开始 |
| 549 | PPDs | 1 | `qa/qd/Determining a PostScript Printer's Optimal Resolution/Legacy Documentclose button-2.md` | 未开始 |
| 550 | PSetSelfSend in Classic AppleTalk vs. Open Transport AppleTalk | 1 | `qa/nw/PSetSelfSend in Classic AppleTalk vs. Open Transport AppleTalk` | 未开始 |
| 551 | Page Setup/Format Dialog Extensions | 1 | `qa/gxpd/Page Setup-Format Dialog Extensions.md` | 未开始 |
| 552 | Paint Program to Create Hotspot PICT files? | 1 | `qa/qtvr/Paint Program to Create Hotspot PICT files.md` | 未开始 |
| 553 | Paper Type Menu not Updated Often | 1 | `qa/gxpd/Paper Type Menu not Updated Often.md` | 未开始 |
| 554 | ParamErr from PrClosePage | 1 | `qa/qd/ParamErr from PrClosePage.md` | 未开始 |
| 555 | Parsing the PICT File Format | 1 | `qa/qd/Parsing the PICT File Format.md` | 未开始 |
| 556 | Placing Video Over Panorama | 1 | `qa/qtvr/Placing Video Over Panorama.md` | 未开始 |
| 557 | Placing a Foreground Task into the Background | 1 | `qa/ps/Placing a Foreground Task into the Background.md` | 未开始 |
| 558 | Playback of QuickTime movie audio through a multi-channel speaker system | 1 | `qa/Playback of QuickTime movie audio through a multi-channel speaker system.md` | 未开始 |
| 559 | Playing Back VR Movies from CD-ROM Drives | 1 | `qa/qtvr/Playing Back VR Movies from CD-ROM Drives.md` | 未开始 |
| 560 | Playing QuickTime 3 Movie Sound Data | 1 | `qa/qtmtb/Playing QuickTime 3 Movie Sound Data.md` | 未开始 |
| 561 | Playing Uncompressed WAVE files via the Sound Manager | 1 | `qa/snd/Playing Compressed WAVE files via the Sound Manager.md` | 未开始 |
| 562 | Playing Uncompressed WAVE files via the Sound Manager | 1 | `qa/snd/Playing Uncompressed WAVE files via the Sound Manager` | 未开始 |
| 563 | Playing memory-resident WAVE data using QuickTime 4 | 1 | `qa/qtmtb/Playing memory-resident WAVE data using QuickTime 4.md` | 未开始 |
| 564 | PostScript Color Printing Bug | 1 | `qa/gxpd/PostScript Color Printing Bug.md` | 未开始 |
| 565 | Power adapter Sensing for the 17" PowerBook | 1 | `qa/qa2001/Power adapter Sensing for the 17- PowerBook` | 未开始 |
| 566 | PowerBook and Sleep Mode | 1 | `qa/hw/PowerBook and Sleep Mode` | 未开始 |
| 567 | PowerMac 9500 Sound Input | 1 | `qa/dv/PowerMac 9500 Sound Input.md` | 未开始 |
| 568 | PowerPC & Writing Info to the Data Fork | 1 | `qa/ppcsys/PowerPC & Writing Info to the Data Fork.md` | 未开始 |
| 569 | Powered Off Devices Connected to the SCSI Bus | 1 | `qa/dv/Powered Off Devices Connected to the SCSI Bus.md` | 未开始 |
| 570 | PrepareMemoryForIO Options | 1 | `qa/dv/PrepareMemoryForIO Options` | 未开始 |
| 571 | PrepareMemoryForIO and Execution Levels | 1 | `qa/dv/Coordinating Deferred Tasks and Secondary Interrupts/Legacy Documentclose button-3.md` | 未开始 |
| 572 | PrepareMemoryForIO in the NewWorld | 1 | `qa/dv/MemAllocatePhysicallyContiguous/dv33.md` | 未开始 |
| 573 | Preroll Movies | 1 | `qa/qtmtb/Preroll Movies.md` | 未开始 |
| 574 | Preserving embedded ICC profiles when using QuickTime Graphics Importer/Exporters | 1 | `qa/qa2001/Preserving embedded ICC profiles when using QuickTime Graphics Importer-Exporter` | 未开始 |
| 575 | Preventing Memory Leaks | 1 | `qa/me/Preventing Memory Leaks.md` | 未开始 |
| 576 | Preventing crashes when using multiple disabled but editable NSComboBoxes | 1 | `qa/qa2001/Preventing crashes when using multiple disabled but editable NSComboBoxes` | 未开始 |
| 577 | Preview image quality of DV capture | 1 | `qa/qtmcc/Preview image quality of DV capture.md` | 未开始 |
| 578 | Print Job Cancelling | 1 | `qa/gxpd/Print Job Cancelling.md` | 未开始 |
| 579 | Print Scaling | 1 | `qa/qd/Print Scaling.md` | 未开始 |
| 580 | Printer Drivers and KanjiTalk 7.5 | 1 | `qa/qd/Printer Drivers and KanjiTalk 7.5.md` | 未开始 |
| 581 | Printing Finder Icons | 1 | `qa/qd/Printing Finder Icons.md` | 未开始 |
| 582 | Printing, Forward and Reverse Line Feeds | 1 | `qa/qd/Printing, Forward and Reverse Line Feeds.md` | 未开始 |
| 583 | Private HITheme APIs in Mac OS X 10.2 should not be called | 1 | `qa/Private HITheme APIs in Mac OS X 10.2 should not be called.md` | 未开始 |
| 584 | Problem Getting PICTS to Display in Correct Colors | 1 | `qa/qd/Problem Getting PICTS to Display in Correct Colors.md` | 未开始 |
| 585 | Problem with PaintRgn on 256-color Screens | 1 | `qa/qd/Problem with PaintRgn on 256-color Screens.md` | 未开始 |
| 586 | Problems Creating a Mask for a Picture | 1 | `qa/qd/Problems Creating a Mask for a Picture.md` | 未开始 |
| 587 | Problems recording CopyBits into a PICT on Mac OS X 10.2 | 1 | `qa/qa2001/Problems recording CopyBits into a PICT on Mac OS X 10.2` | 未开始 |
| 588 | Problems with CDEV Multiple Dialogs | 1 | `qa/tb/Problems with CDEV Multiple Dialogs` | 未开始 |
| 589 | Problems with Caching Drivers on PowerMac 9500 | 1 | `qa/dv/Problems with Caching Drivers on PowerMac 9500.md` | 未开始 |
| 590 | Problems with DiffRgn | 1 | `qa/qd/Problems with DiffRgn.md` | 未开始 |
| 591 | Problems with MPW and ROM Maps | 1 | `qa/plat/Problems with MPW and ROM Maps` | 未开始 |
| 592 | Problems with Navigable Movies | 1 | `qa/qtvr/Problems with Navigable Movies.md` | 未开始 |
| 593 | Problems with Objects Leaving Trails | 1 | `qa/qtvr/Problems with Objects Leaving Trails.md` | 未开始 |
| 594 | Problems with Panning and Zooming | 1 | `qa/qtvr/Problems with Panning and Zooming.md` | 未开始 |
| 595 | Problems with Stitching | 1 | `qa/qtvr/Problems with Stitching.md` | 未开始 |
| 596 | Process Carbon Events Not Delivered in 10.2 | 1 | `qa/qa2001/Process Carbon Events Not Delivered in 10.2` | 未开始 |
| 597 | Process Manager | 1 | `qa/ps/Process Manager.md` | 未开始 |
| 598 | Programatically retrieving field and frame information | 1 | `qa/Programatically retrieving field and frame information.md` | 未开始 |
| 599 | Programmatic configuration of a Movie Export Component | 1 | `qa/qa2001/Programmatic configuration of a Movie Export Component` | 未开始 |
| 600 | Prompting the user with MRJQuitHandler | 1 | `qa/qa2001/Prompting the user with MRJQuitHandler` | 未开始 |
| 601 | Properties versus methods in automatically generated 'aete' resources | 1 | `qa/java/Properties versus methods in automatically generated 'aete' resources` | 未开始 |
| 602 | Providing QuickDraw with a Known Good Port | 1 | `qa/qa2001/Providing QuickDraw with a Known Good Port` | 未开始 |
| 603 | Putting Client/Server Systems to Sleep | 1 | `qa/nw/Putting Client-Server Systems to Sleep` | 未开始 |
| 604 | Q3Exit Causes Application Crashes and Error Messages | 1 | `qa/qd3d/Q3Exit Causes Application Crashes and Error Messages.md` | 未开始 |
| 605 | Q3View_Sync/Q3View_Flush Differences | 1 | `qa/qd3d/Q3ViewSync-Q3ViewFlush Differences.md` | 未开始 |
| 606 | QD3D Does Not Free Memory Used By Geometries | 1 | `qa/qd3d/QD3D Does Not Free Memory Used By Geometries.md` | 未开始 |
| 607 | QD3D Does Not Provide Z-Buffer Information | 1 | `qa/qd3d/QD3D Does Not Provide Z-Buffer Information.md` | 未开始 |
| 608 | QD3D Functions Not Interrupt Safe | 1 | `qa/qd3d/QD3D Functions Not Interrupt Safe.md` | 未开始 |
| 609 | QD3D Is Not Thread-Safe | 1 | `qa/qd3d/QD3D Is Not Thread-Safe.md` | 未开始 |
| 610 | QD3D Macintosh High Quality Postscript Output | 1 | `qa/qd3d/QD3D Macintosh High Quality Postscript Output.md` | 未开始 |
| 611 | QD3D Plug-In Renderer Handlers | 1 | `qa/qd3d/QD3D Plug-In Renderer Handlers.md` | 未开始 |
| 612 | QD3D Windows High Quality Postscript Output | 1 | `qa/qd3d/QD3D Windows High Quality Postscript Output.md` | 未开始 |
| 613 | QD3D Windows Interactive Renderer | 1 | `qa/qd3d/QD3D Windows Interactive Renderer.md` | 未开始 |
| 614 | QD3D Windows Pixel Format Support | 1 | `qa/qd3d/QD3D Windows Pixel Format Support.md` | 未开始 |
| 615 | QDFlushPortBuffer | 1 | `qa/qd/QDFlushPortBuffer.md` | 未开始 |
| 616 | QDSwapPort | 1 | `qa/qa2001/QDSwapPort` | 未开始 |
| 617 | Quality of QuickTime video effects | 1 | `qa/qa2001/Quality of QuickTime video effects` | 未开始 |
| 618 | Quality of Video Textures | 1 | `qa/qd3d/Quality of Video Textures.md` | 未开始 |
| 619 | QuickDraw 3D -- Meshes or Patches? | 1 | `qa/qd3d/QuickDraw 3D -- Meshes or Patches.md` | 未开始 |
| 620 | QuickDraw 3D Debugging Tools | 1 | `qa/qd3d/QuickDraw 3D Debugging Tools.md` | 未开始 |
| 621 | QuickDraw 3D Documentation | 1 | `qa/qd3d/QuickDraw 3D Documentation.md` | 未开始 |
| 622 | QuickDraw 3D Projection Chain | 1 | `qa/qd3d/QuickDraw 3D Projection Chain.md` | 未开始 |
| 623 | QuickDraw 3D Rendering | 1 | `qa/qd3d/QuickDraw 3D Rendering.md` | 未开始 |
| 624 | QuickDraw 3D and Submit Calls | 1 | `qa/qd3d/QuickDraw 3D and Submit Calls.md` | 未开始 |
| 625 | QuickDraw GX 'ptyp' Page Size Calc | 1 | `qa/gxpd/QuickDraw GX 'ptyp' Page Size Calc.md` | 未开始 |
| 626 | QuickDraw GX 'ptyp' resources | 1 | `qa/gxpd/QuickDraw GX 'ptyp' resources.md` | 未开始 |
| 627 | QuickDraw GX Font Format | 1 | `qa/gxty/QuickDraw GX Font Format.md` | 未开始 |
| 628 | QuickDraw GX Font Problems | 1 | `qa/gxty/QuickDraw GX Font Problems.md` | 未开始 |
| 629 | QuickDraw GX General Print Panel | 1 | `qa/gxpd/QuickDraw GX General Print Panel.md` | 未开始 |
| 630 | QuickDraw GX Layered Drawing | 1 | `qa/gx/QuickDraw GX Layered Drawing` | 未开始 |
| 631 | QuickDraw GX Print Extension | 1 | `qa/gxpd/QuickDraw GX Print Extension.md` | 未开始 |
| 632 | QuickDraw GX Printer Drivers & Configuration | 1 | `qa/gxpd/QuickDraw GX Printer Drivers & Configuration.md` | 未开始 |
| 633 | QuickDraw GX Printing Extensions | 1 | `qa/gxpd/QuickDraw GX Printing Extensions.md` | 未开始 |
| 634 | QuickDraw GX Raster and Blank Lines | 1 | `qa/gxpd/QuickDraw GX Raster and Blank Lines.md` | 未开始 |
| 635 | QuickDraw GX and Adobe Type Reunion | 1 | `qa/gxpd/QuickDraw GX and Adobe Type Reunion.md` | 未开始 |
| 636 | QuickDraw GX and Color Profiles | 1 | `qa/gx/QuickDraw GX and Color Profiles` | 未开始 |
| 637 | QuickDraw GX and DoesPaperFit Message | 1 | `qa/gxpd/QuickDraw GX and DoesPaperFit Message.md` | 未开始 |
| 638 | QuickDraw GX and GXConvertQDFont | 1 | `qa/gxty/QuickDraw GX and GXConvertQDFont.md` | 未开始 |
| 639 | QuickDraw GX and Hypercard | 1 | `qa/gxty/QuickDraw GX and Hypercard.md` | 未开始 |
| 640 | QuickDraw GX and Layout Shapes | 1 | `qa/gxty/QuickDraw GX and Layout Shapes.md` | 未开始 |
| 641 | QuickDraw GX and PDDs | 1 | `qa/gxpd/QuickDraw GX and PDDs.md` | 未开始 |
| 642 | QuickDraw GX and Text Justification | 1 | `qa/gxty/QuickDraw GX and Text Justification.md` | 未开始 |
| 643 | QuickDraw GX's 'xdtl' Implementation | 1 | `qa/gxpd/QuickDraw GX's 'xdtl' Implementation.md` | 未开始 |
| 644 | QuickDraw Printer Drivers and Colorsync | 1 | `qa/qd/QuickDraw Printer Drivers and Colorsync.md` | 未开始 |
| 645 | QuickDraw Text Anti-Aliasing using Quartz 2D | 1 | `qa/qa2001/QuickDraw Text Anti-Aliasing using Quartz 2D` | 未开始 |
| 646 | QuickDrawGX Fonts | 1 | `qa/gxty/QuickDrawGX Fonts.md` | 未开始 |
| 647 | QuickDrawGX Printer Drivers | 1 | `qa/gxpd/QuickDrawGX Printer Drivers.md` | 未开始 |
| 648 | QuickTime & EnterMovies Call | 1 | `qa/qtmtb/QuickTime & EnterMovies Call.md` | 未开始 |
| 649 | QuickTime & MIDI Support | 1 | `qa/qtma/QuickTime & MIDI Support.md` | 未开始 |
| 650 | QuickTime & Memory | 1 | `qa/qtmtb/QuickTime & Memory.md` | 未开始 |
| 651 | QuickTime & Noise Problems | 1 | `qa/qtpc/QuickTime & Noise Problems.md` | 未开始 |
| 652 | QuickTime & PutMovieIntoDataFork, Offsets | 1 | `qa/qtmtb/QuickTime & PutMovieIntoDataFork, Offsets.md` | 未开始 |
| 653 | QuickTime .qtx/.qtr/.qt/.mov files defined | 1 | `qa/qtw/QuickTime .qtx-.qtr-.qt-.mov files defined` | 未开始 |
| 654 | QuickTime 2.0 & MIDI | 1 | `qa/qtma/QuickTime 2.0 & MIDI.md` | 未开始 |
| 655 | QuickTime 2.0 and MIDI Conversions | 1 | `qa/qtma/QuickTime 2.0 and MIDI Conversions.md` | 未开始 |
| 656 | QuickTime 6.4 & AvailabilityMacros.h on Mac OS X 10.2.x | 1 | `qa/qa2001/QuickTime 6.4 & AvailabilityMacros.h on Mac OS X 10.2.x` | 未开始 |
| 657 | QuickTime 7.1.5 Security Enhancements | 1 | `qa/QuickTime 7.1.5 Security Enhancements.md` | 未开始 |
| 658 | QuickTime Audio - Easy Frequency Level Metering with MovieAudio APIs | 1 | `qa/QuickTime Audio - Easy Frequency Level Metering with MovieAudio APIs.md` | 未开始 |
| 659 | QuickTime Audio - Muting and GetMovieAudioFrequencyLevels | 1 | `qa/QuickTime Audio - Muting and GetMovieAudioFrequencyLevels.md` | 未开始 |
| 660 | QuickTime Audio - Rendering QuickTime Movie audio to a specific Audio Device | 1 | `qa/QuickTime Audio - Rendering QuickTime Movie audio to a specific Audio Device.md` | 未开始 |
| 661 | QuickTime Audio - Retrieving the correct audio format bit depth value | 1 | `qa/QuickTime Audio - Retrieving the correct audio format bit depth value.md` | 未开始 |
| 662 | QuickTime CFM Error -2804 | 1 | `qa/qtmtb/QuickTime CFM Error -2804.md` | 未开始 |
| 663 | QuickTime CFM PowerPlug Libraries, Availability, Weak Links | 1 | `qa/qtmtb/QuickTime CFM PowerPlug Libraries, Availability, Weak Links.md` | 未开始 |
| 664 | QuickTime Effects - How to set up parameter description values when using kParameterTypeDataImage | 1 | `qa/qa2001/QuickTime Effects - How to set up parameter description values when using kParam` | 未开始 |
| 665 | QuickTime Error -2127 qtNetworkAlreadyAllocatedErr Explained | 1 | `qa/qa2001/QuickTime Error -2127 qtNetworkAlreadyAllocatedErr Explained` | 未开始 |
| 666 | QuickTime Media Editing | 1 | `qa/qa2001/QuickTime Media Editing` | 未开始 |
| 667 | QuickTime Media Optimization Properties | 1 | `qa/QuickTime Media Optimization Properties.md` | 未开始 |
| 668 | QuickTime Movie Toolbox & Global Variables | 1 | `qa/qtmtb/QuickTime Movie Toolbox & Global Variables.md` | 未开始 |
| 669 | QuickTime Music Architecture | 1 | `qa/qtma/QuickTime Music Architecture.md` | 未开始 |
| 670 | QuickTime Music Architecture Header Update | 1 | `qa/qtma/QuickTime Music Architecture Header Update.md` | 未开始 |
| 671 | QuickTime Supported YUV Pixel Formats | 1 | `qa/qa2001/QuickTime Supported YUV Pixel Formats` | 未开始 |
| 672 | QuickTime Texture Visual Context - kQTVisualContextNotAllowedErr with non-accelerated | 1 | `qa/QuickTime Texture Visual Context - kQTVisualContextNotAllowedErr with non-accele.md` | 未开始 |
| 673 | QuickTime Toolbox GetMovieTime Call | 1 | `qa/qtmtb/QuickTime Toolbox GetMovieTime Call.md` | 未开始 |
| 674 | QuickTime Visual Context - Setting the kQTVisualContextOutputColorSpaceKey | 1 | `qa/QuickTime Visual Context - Setting the kQTVisualContextOutputColorSpaceKey Attri.md` | 未开始 |
| 675 | QuickTime and Carbon Events | 1 | `qa/qa2001/QuickTime and Carbon Events` | 未开始 |
| 676 | QuickTime and Native PowerPC | 1 | `qa/qtmtb/QuickTime and Native PowerPC.md` | 未开始 |
| 677 | QuickTime for Windows resource files | 1 | `qa/qa2001/QuickTime for Windows resource files` | 未开始 |
| 678 | QuickTime for Windows returns bdNamErr (-37) error with long Windows file names | 1 | `qa/QuickTime for Windows returns bdNamErr (-37) error with long Windows file names.md` | 未开始 |
| 679 | QuickTime movies require a valid graphics port | 1 | `qa/qa2001/QuickTime movies require a valid graphics port` | 未开始 |
| 680 | Quickdraw GX Raster Printer Drivers | 1 | `qa/gxpd/Quickdraw GX Raster Printer Drivers.md` | 未开始 |
| 681 | RAVE Multiple GDevice support | 1 | `qa/qd3d/RAVE Multiple GDevice support.md` | 未开始 |
| 682 | RAVE Notifications | 1 | `qa/qd3d/RAVE Notifications.md` | 未开始 |
| 683 | RAVE Support for Apple 3D Accelerator | 1 | `qa/qd3d/RAVE Support for Apple 3D Accelerator.md` | 未开始 |
| 684 | RAVE Z-Buffer Access | 1 | `qa/qd3d/RAVE Z-Buffer Access.md` | 未开始 |
| 685 | RAVE and DrawSprocket Integration | 1 | `qa/qd3d/RAVE and DrawSprocket Integration.md` | 未开始 |
| 686 | Raw IP and Open Transport 2.5.x | 1 | `qa/nw/Raw IP and Open Transport 2.5.x` | 未开始 |
| 687 | Receiving UDP Broadcasts | 1 | `qa/nw/Receiving UDP Broadcasts/Not Recommended Documentclose button.md` | 未开始 |
| 688 | Receiving UDP Broadcasts While Sending from a Secondary Address | 1 | `qa/nw/Receiving UDP Broadcasts While Sending from a Secondary Address` | 未开始 |
| 689 | Recording Compressed Sounds | 1 | `qa/snd/Recording Compressed Sounds.md` | 未开始 |
| 690 | Reducing the size of Physical Memory in Open Firmware | 1 | `qa/qa2001/Reducing the size of Physical Memory in Open Firmware` | 未开始 |
| 691 | Reentrancy in QDGX Printer Drivers | 1 | `qa/gxpd/Reentrancy in QDGX Printer Drivers.md` | 未开始 |
| 692 | Region Structure | 1 | `qa/qd3d/Region Structure.md` | 未开始 |
| 693 | Registered Custom-Attribute Types | 1 | `qa/qd3d/Registered Custom-Attribute Types.md` | 未开始 |
| 694 | Registering custom pixel formats with QuickTime and Core Video | 1 | `qa/Registering custom pixel formats with QuickTime and Core Video.md` | 未开始 |
| 695 | Remotely Retrieving a Macintosh's Network Name using AppleTalk | 1 | `qa/nw/Remotely Retrieving a Macintosh's Network Name using AppleTalk` | 未开始 |
| 696 | Reordering of Vertices in a Mesh | 1 | `qa/qd3d/Reordering of Vertices in a Mesh.md` | 未开始 |
| 697 | Reserved Key Combinations | 1 | `qa/tb/Reserved Key Combinations` | 未开始 |
| 698 | Resetting NVRAM to factory defaults | 1 | `qa/qa2001/Resetting NVRAM to factory defaults` | 未开始 |
| 699 | Resolution Switching | 1 | `qa/qtvr/Resolution Switching.md` | 未开始 |
| 700 | Resolving Aliases Asynchronously | 1 | `qa/fl/Resolving Aliases Asynchronously.md` | 未开始 |
| 701 | Resource chain corruption when using Navigation Services dialogs and Carbon | 1 | `qa/qa2001/Resource chain corruption when using Navigation Services dialogs and Carbon Even` | 未开始 |
| 702 | Resource forks in Mach-O binaries | 1 | `qa/qa2001/Resource forks in Mach-O binaries` | 未开始 |
| 703 | Retrieving Audio from QuickTime Files | 1 | `qa/qtmtb/Retrieving Audio from QuickTime Files.md` | 未开始 |
| 704 | RunApplicationEventLoop and Thread Manager | 1 | `qa/qa2001/RunApplicationEventLoop and Thread Manager` | 未开始 |
| 705 | SCSI Calls Translated for IDE Devices | 1 | `qa/dv/SCSI Calls Translated for IDE Devices.md` | 未开始 |
| 706 | SCSI ID from vRefNum | 1 | `qa/dv/SCSI ID from vRefNum.md` | 未开始 |
| 707 | SCSI Printer Prevents System Boot | 1 | `qa/dv/SCSI Printer Prevents System Boot.md` | 未开始 |
| 708 | SCSIAction and IOSCSIUserClient on Mac OS X 10.2 | 1 | `qa/qa2001/SCSIAction and IOSCSIUserClient on Mac OS X 10.2` | 未开始 |
| 709 | SDRAM Problems With Self-Powered USB Devices | 1 | `qa/hw/SDRAM Problems With Self-Powered USB Devices` | 未开始 |
| 710 | SDRAM, CAS Latency for the | 1 | `qa/qa2001/SDRAM, CAS Latency for the` | 未开始 |
| 711 | SGSetSettings unexpected results | 1 | `qa/qtmtb/SGSetSettings unexpected results.md` | 未开始 |
| 712 | SSL and Applet Caching in MRJ 2.2 | 1 | `qa/java/SSL and Applet Caching in MRJ 2.2` | 未开始 |
| 713 | Sample Description Endianness | 1 | `qa/qa2008/Sample Description Endianness` | 未开始 |
| 714 | Saving Paper Type Information | 1 | `qa/gxpd/Saving Paper Type Information.md` | 未开始 |
| 715 | Saving QuickTime Movie Files | 1 | `qa/qtmtb/Saving QuickTime Movie Files.md` | 未开始 |
| 716 | Saving changes to modified movies | 1 | `qa/qtmtb/Saving changes to modified movies.md` | 未开始 |
| 717 | Saving playback hints in a Movie | 1 | `qa/qa2001/Saving playback hints in a Movie` | 未开始 |
| 718 | Screen Flickering | 1 | `qa/qd3d/Screen Flickering.md` | 未开始 |
| 719 | Scripting Java-based command-line interface applications | 1 | `qa/java/Scripting Java-based command-line interface applications` | 未开始 |
| 720 | Searching Directories with PBCatSearch | 1 | `qa/fl/Searching Directories with PBCatSearch.md` | 未开始 |
| 721 | Secondary Interrupts on the Page Fault Path | 1 | `qa/dv/Secondary Interrupts on the Page Fault Path` | 未开始 |
| 722 | Securely Erasing, Accessing and Dismounting a Macintosh Partition | 1 | `qa/fl/Securely Erasing, Accessing and Dismounting a Macintosh Partition.md` | 未开始 |
| 723 | Selecting a PPD When no Printer is Available | 1 | `qa/qd/Selecting a PPD When no Printer is Available.md` | 未开始 |
| 724 | Selecting a specific sound input source | 1 | `qa/snd/Selecting a specific sound input source.md` | 未开始 |
| 725 | Sending SMS Programmatically | 1 | `qa/Sending SMS Programmatically.md` | 未开始 |
| 726 | Sequence Grabber - Determining the capture resolution of an IIDC device | 1 | `qa/Sequence Grabber - Determining the capture resolution of an IIDC device.md` | 未开始 |
| 727 | Sequence Grabber - Ensuring the SG TimeBase is being driven by the Sound Clock. | 1 | `qa/qa2001/Sequence Grabber - Ensuring the SG TimeBase is being driven by the Sound Clock` | 未开始 |
| 728 | Sequence Grabber - How do I save user settings as CFPreferences? | 1 | `qa/qa2001/Sequence Grabber - How do I save user settings as CFPreferences` | 未开始 |
| 729 | Sequence Grabber - How often should I call SGIdle? | 1 | `qa/qa2001/Sequence Grabber - How often should I call SGIdle` | 未开始 |
| 730 | Sequence Grabber - Setting the sound channel play through state | 1 | `qa/qa2001/Sequence Grabber - Setting the sound channel play through state` | 未开始 |
| 731 | Sequence Grabber - Using the SGDataProc for Sound | 1 | `qa/qa2001/Sequence Grabber - Using the SGDataProc for Sound` | 未开始 |
| 732 | Sequence Grabber Source, Video, and Channel Bounds | 1 | `qa/qa2001/Sequence Grabber Source, Video, and Channel Bounds` | 未开始 |
| 733 | Sequence Grabber preallocates large file when recording | 1 | `qa/Sequence Grabber preallocates large file when recording.md` | 未开始 |
| 734 | Serial (Built-In) | 1 | `qa/dv/Serial (Built-In).md` | 未开始 |
| 735 | Serial API Choice | 1 | `qa/dv/Serial API Choice.md` | 未开始 |
| 736 | Serial Flow Control Bug | 1 | `qa/dv/Serial Flow Control Bug.md` | 未开始 |
| 737 | Server Endpoint 'qlen' Limit | 1 | `qa/nw/Server Endpoint 'qlen' Limit` | 未开始 |
| 738 | SetFontInfoForSelection incorrect prototype | 1 | `qa/SetFontInfoForSelection incorrect prototype.md` | 未开始 |
| 739 | SetSoundMediaBalance balance parameter clarification | 1 | `qa/SetSoundMediaBalance balance parameter clarification.md` | 未开始 |
| 740 | Setting A Default Papertype for GX Printers | 1 | `qa/gxpd/Setting A Default Papertype for GX Printers.md` | 未开始 |
| 741 | Setting Audio Input Gain | 1 | `qa/snd/Setting Audio Input Gain.md` | 未开始 |
| 742 | Setting Data For Q3ViewerUseData | 1 | `qa/qd3d/Setting Data For Q3ViewerUseData.md` | 未开始 |
| 743 | Setting Export Quality | 1 | `qa/qtmcc/Setting Export Quality.md` | 未开始 |
| 744 | Setting GX Paper Types | 1 | `qa/gxpd/Setting GX Paper Types.md` | 未开始 |
| 745 | Setting Landscape Printing from an Application | 1 | `qa/qd/Setting Landscape Printing from an Application.md` | 未开始 |
| 746 | Setting Port Speed on a Modem Port | 1 | `qa/dv/Setting Port Speed on a Modem Port.md` | 未开始 |
| 747 | Setting Sequence Grabber Sound Input Device Driver Parameters | 1 | `qa/qa2001/Setting Sequence Grabber Sound Input Device Driver Parameters` | 未开始 |
| 748 | Setting Up a gxCustomMatrixType | 1 | `qa/gx/Setting Up a gxCustomMatrixType` | 未开始 |
| 749 | Setting a Control's Variant Field | 1 | `qa/tb/Setting a Control's Variant Field` | 未开始 |
| 750 | Setting a Movie's Clipping Region | 1 | `qa/qtmtb/Setting a Movie's Clipping Region.md` | 未开始 |
| 751 | Setting a UserPane's feature | 1 | `qa/tb/Setting a UserPane's feature` | 未开始 |
| 752 | Setting request headers in URL Access | 1 | `qa/qa2001/Setting request headers in URL Access` | 未开始 |
| 753 | Setting the Background Color of a Control | 1 | `qa/tb/Setting the Background Color of a Control` | 未开始 |
| 754 | Setting the Ratio Between Height and Width | 1 | `qa/qtvr/Setting the Ratio Between Height and Width.md` | 未开始 |
| 755 | Setting the movie background color | 1 | `qa/qtmtb/Setting the movie background color.md` | 未开始 |
| 756 | Setting the option button in the ICM dialog | 1 | `qa/qtmcc/Setting the option button in the ICM dialog.md` | 未开始 |
| 757 | Setting the preferred CMM programatically? | 1 | `qa/qa2001/Setting the preferred CMM programatically` | 未开始 |
| 758 | ShaderUV/SurfaceUV Attribute Differences | 1 | `qa/qd3d/ShaderUV-SurfaceUV Attribute Differences.md` | 未开始 |
| 759 | Shading Using Trigrids | 1 | `qa/qd3d/Shading Using Trigrids.md` | 未开始 |
| 760 | Sharing Globals Between Apps & Code Fragment Manager | 1 | `qa/ic/Sharing Globals Between Apps & Code Fragment Manager.md` | 未开始 |
| 761 | Simulated Click on AWT Button | 1 | `qa/java/Simulated Click on AWT Button` | 未开始 |
| 762 | Small Point Size and Hinting | 1 | `qa/gxty/Small Point Size and Hinting.md` | 未开始 |
| 763 | Small System Font Size on a Korean System | 1 | `qa/tx/Small System Font Size on a Korean System.md` | 未开始 |
| 764 | SndPlayDoubleBuffer 16-bit Support | 1 | `qa/snd/SndPlayDoubleBuffer 16-bit Support.md` | 未开始 |
| 765 | Software Debugging - Sources of Information | 1 | `qa/plat/Software Debugging - Sources of Information` | 未开始 |
| 766 | Solving NSTabView drawing problems in Mac OS X 10.1.x | 1 | `qa/qa2001/Solving NSTabView drawing problems in Mac OS X 10.1.x` | 未开始 |
| 767 | Sound Manager Codec support in QuickTime 7 | 1 | `qa/Sound Manager Codec support in QuickTime 7.md` | 未开始 |
| 768 | Sound Ramp-up on Power Macs | 1 | `qa/snd/Sound Ramp-up on Power Macs.md` | 未开始 |
| 769 | Sound Track Hiccups under Windows 95 | 1 | `qa/snd/Sound Track Hiccups under Windows 95.md` | 未开始 |
| 770 | Sources of 3DMF Documentation | 1 | `qa/qd3d/Sources of 3DMF Documentation.md` | 未开始 |
| 771 | Specifying Chunk Sizes | 1 | `qa/qtpc/Specifying Chunk Sizes.md` | 未开始 |
| 772 | Specifying Proxy Settings | 1 | `qa/java/Specifying Proxy Settings` | 未开始 |
| 773 | Specifying a Non-Panorama | 1 | `qa/qtvr/Specifying a Non-Panorama.md` | 未开始 |
| 774 | Specular Control Range in QuickDraw 3D | 1 | `qa/qd3d/Specular Control Range in QuickDraw 3D.md` | 未开始 |
| 775 | Speed of the Printer Port | 1 | `qa/dv/Speed of the Printer Port.md` | 未开始 |
| 776 | Spooling a pixMap into a Window | 1 | `qa/qd/Spooling a pixMap into a Window.md` | 未开始 |
| 777 | Spooling in or out of CompressPicture or CompressImage | 1 | `qa/qd/Spooling in or out of CompressPicture or CompressImage.md` | 未开始 |
| 778 | Spot Light Not Working | 1 | `qa/qd3d/Spot Light Not Working.md` | 未开始 |
| 779 | Stack Crawl Not Showing Line Numbers | 1 | `qa/java/Stack Crawl Not Showing Line Numbers/Legacy Documentclose button.md` | 未开始 |
| 780 | Standalone Networking | 1 | `qa/nw/Standalone Networking` | 未开始 |
| 781 | Standard Audio - Parsing the kQTSCAudioPropertyID_CodecSpecificSettingsArray | 1 | `qa/Standard Audio - Parsing the kQTSCAudioPropertyIDCodecSpecificSettingsArray prop` | 未开始 |
| 782 | Standard Audio - Setting output ASBD returns badFormatErr | 1 | `qa/Standard Audio - Setting output ASBD returns badFormatErr.md` | 未开始 |
| 783 | Standard Audio - The CodecSpecificSettingsArray and MagicCookie properties | 1 | `qa/Standard Audio - The CodecSpecificSettingsArray and MagicCookie properties` | 未开始 |
| 784 | Standard File Package | 1 | `qa/fl/Standard File Package.md` | 未开始 |
| 785 | Static Socket Numbers | 1 | `qa/nw/Static Socket Numbers` | 未开始 |
| 786 | Static Sound on PCI Macs | 1 | `qa/snd/Static Sound on PCI Macs.md` | 未开始 |
| 787 | Stepping Through QuickTime-Movie | 1 | `qa/qtmtb/Stepping Through QuickTime-Movie.md` | 未开始 |
| 788 | Stepping through a PICT Movie | 1 | `qa/qtmcc/Stepping through a PICT Movie.md` | 未开始 |
| 789 | StopAlert and NoteAlert now use the Application icon | 1 | `qa/StopAlert and NoteAlert now use the Application icon` | 未开始 |
| 790 | Stopping Forth command scrolls | 1 | `qa/hw/Stopping Forth command scrolls` | 未开始 |
| 791 | Storing an Array Name in a Field in Another Array | 1 | `qa/amt pe/Storing an Array Name in a Field in Another Array.md` | 未开始 |
| 792 | Stubs.o vs. fgets | 1 | `qa/plat/Stubs.o vs. fgets` | 未开始 |
| 793 | Submenus not Updating With Mac OS Screen MenuBar | 1 | `qa/qa2001/Submenus not Updating With Mac OS Screen MenuBar` | 未开始 |
| 794 | Supporting QuickDraw GX with EPS | 1 | `qa/gx/Supporting QuickDraw GX with EPS` | 未开始 |
| 795 | Suppressing the "unexpectedly quit" alert | 1 | `qa/Suppressing the -unexpectedly quit- alert.md` | 未开始 |
| 796 | Suppressing the LaserWriter 8.3 Manual Feed Alert | 1 | `qa/qd/Suppressing the LaserWriter 8.3 Manual Feed Alert.md` | 未开始 |
| 797 | Switching between one and two machine mode for the Open Firmware user interface | 1 | `qa/hw/Switching between one and two machine mode for the Open Firmware user interface` | 未开始 |
| 798 | Synchronizing Sounds to Video | 1 | `qa/snd/Synchronizing Sounds to Video.md` | 未开始 |
| 799 | Synchronous SCSI Operation | 1 | `qa/dv/Synchronous SCSI Operation.md` | 未开始 |
| 800 | Synchronous SysBeep | 1 | `qa/snd/Synchronous SysBeep.md` | 未开始 |
| 801 | Synchronous TCP OTConnect Client Call Completes Before Server Responds | 1 | `qa/nw/Synchronous TCP OTConnect Client Call Completes Before Server Responds` | 未开始 |
| 802 | System Clock | 1 | `qa/ops/System Clock` | 未开始 |
| 803 | System Error 119 | 1 | `qa/ops/System Error 119` | 未开始 |
| 804 | System Error 29 | 1 | `qa/ops/System Error 29` | 未开始 |
| 805 | System Menu IDs | 1 | `qa/tb/System Menu IDs` | 未开始 |
| 806 | TCP Application Acquires Different Port Address After Relaunch | 1 | `qa/nw/Receiving UDP Broadcasts/Not Recommended Documentclose button-2.md` | 未开始 |
| 807 | TCP Option Sizes | 1 | `qa/nw/TCP Option Sizes` | 未开始 |
| 808 | TQ3Ellipsoid Data Caps Field Explanation | 1 | `qa/qd3d/TQ3Ellipsoid Data Caps Field Explanation.md` | 未开始 |
| 809 | TQ3ViewObject and Bounding Box Calculating Routines | 1 | `qa/qd3d/TQ3ViewObject and Bounding Box Calculating Routines.md` | 未开始 |
| 810 | T_DATA_REQ vs M_DATA TPI Message Blocks | 1 | `qa/nw/TDATAREQ vs MDATA TPI Message Blocks` | 未开始 |
| 811 | Targeting DebuggingCarbonLib asserts | 1 | `qa/qa2001/Targeting DebuggingCarbonLib asserts` | 未开始 |
| 812 | Tear-off Menus | 1 | `qa/tb/Tear-off Menus` | 未开始 |
| 813 | Test What You Ship | 1 | `qa/ov/Test What You Ship.md` | 未开始 |
| 814 | Testing PCI drivers without any device | 1 | `qa/hw/Testing PCI drivers without any device` | 未开始 |
| 815 | Text Mask Mode and QuickDraw | 1 | `qa/qd/Text Mask Mode and QuickDraw.md` | 未开始 |
| 816 | Textures & BitMaps Explained | 1 | `qa/qd3d/Textures & BitMaps Explained.md` | 未开始 |
| 817 | The "/aliases" node in the device tree | 1 | `qa/hw/The --aliases- node in the device tree` | 未开始 |
| 818 | The "chosen" node in the device tree | 1 | `qa/hw/The -chosen- node in the device tree` | 未开始 |
| 819 | The "packages" node in the device tree | 1 | `qa/hw/The -packages- node in the device tree` | 未开始 |
| 820 | The 'vers' Resource and Your Place in the World | 1 | `qa/tx/The 'vers' Resource and Your Place in the World.md` | 未开始 |
| 821 | The AAPL, slot-name property and PCI | 1 | `qa/hw/The AAPL, slot-name property and PCI` | 未开始 |
| 822 | The Backfacing Option | 1 | `qa/qd3d/The Backfacing Option.md` | 未开始 |
| 823 | The Data Browser GetDataBrowserUserState API | 1 | `qa/qa2001/The Data Browser GetDataBrowserUserState API` | 未开始 |
| 824 | The Gamma function in the Mac OS X 10.2 Math Library | 1 | `qa/qa2001/The Gamma function in the Mac OS X 10.2 Math Library` | 未开始 |
| 825 | The Improper use of FSClose | 1 | `qa/tb/The Improper use of FSClose` | 未开始 |
| 826 | The InterfaceLibSys7.additions Stub Library | 1 | `qa/plat/The InterfaceLibSys7.additions Stub Library` | 未开始 |
| 827 | The intermittent behavior of SetDialogItemText | 1 | `qa/qa2001/The intermittent behavior of SetDialogItemText` | 未开始 |
| 828 | The similarity field in ImageCodecBandCompress and Key Frames | 1 | `qa/qa2001/The similarity field in ImageCodecBandCompress and Key Frames` | 未开始 |
| 829 | Tioga PostScript Printing Plugins in Mac OS X 10.2 | 1 | `qa/qa2001/Tioga PostScript Printing Plugins in Mac OS X 10.2` | 未开始 |
| 830 | Tips for searching Headers, APIs and ADC reference material. | 1 | `qa/Tips for searching Headers, APIs and ADC reference material` | 未开始 |
| 831 | Track Editing | 1 | `qa/qtmcc/Track Editing.md` | 未开始 |
| 832 | Transparency Not Working on Some Machines | 1 | `qa/qd3d/Transparency Not Working on Some Machines.md` | 未开始 |
| 833 | Transparency not Working on Laptops | 1 | `qa/amt pe/Transparency not Working on Laptops.md` | 未开始 |
| 834 | Tray Mismatch Dialog in QuickDraw GX 1.1.1b1 | 1 | `qa/gxpd/Tray Mismatch Dialog in QuickDraw GX 1.1.1b1.md` | 未开始 |
| 835 | Triangle Strips | 1 | `qa/qd3d/Triangle Strips.md` | 未开始 |
| 836 | U and V limits in RAVE | 1 | `qa/qd3d/U and V limits in RAVE.md` | 未开始 |
| 837 | URL Access and the Missing Progress Dialog | 1 | `qa/qa2001/URL Access and the Missing Progress Dialog` | 未开始 |
| 838 | URL Access vs. CFNetwork | 1 | `qa/qa2001/URL Access vs. CFNetwork` | 未开始 |
| 839 | USBGetNextDeviceByClass Requires deviceRef | 1 | `qa/usb/USBGetNextDeviceByClass Requires deviceRef.md` | 未开始 |
| 840 | UV Support | 1 | `qa/qd3d/UV Support.md` | 未开始 |
| 841 | UV's in Vertex List | 1 | `qa/qd3d/UV's in Vertex List.md` | 未开始 |
| 842 | Unbinding from a TCP Port | 1 | `qa/nw/Unbinding from a TCP Port` | 未开始 |
| 843 | Undefined Routines in Open TransportLibraries | 1 | `qa/nw/Undefined Routines in Open TransportLibraries` | 未开始 |
| 844 | Undefined Routines with PPCLink? | 1 | `qa/nw/Undefined Routines with PPCLink` | 未开始 |
| 845 | Understanding USB Error -6911 - (kUSBNotResponding) | 1 | `qa/usb/Understanding USB Error -6911 - (kUSBNotResponding).md` | 未开始 |
| 846 | Unified window title and toolbar appearance in Carbon | 1 | `qa/Unified window title and toolbar appearance in Carbon.md` | 未开始 |
| 847 | Universality of ColorSync Accelerators and CMMs | 1 | `qa/c/Universality of ColorSync Accelerators and CMMs` | 未开始 |
| 848 | Unpopped Popup Menus and Mac OS 8.5 | 1 | `qa/tb/Unpopped Popup Menus and Mac OS 8.5` | 未开始 |
| 849 | Unwanted Audio with DV Capture | 1 | `qa/qa2001/Unwanted Audio with DV Capture` | 未开始 |
| 850 | UpTime's values are consistently slow? | 1 | `qa/hw/UpTime's values are consistently slow` | 未开始 |
| 851 | Updating from a wildcard App ID to an explicit App ID | 1 | `qa/Updating from a wildcard App ID to an explicit App ID` | 未开始 |
| 852 | Use Macintosh SCSI Manager for SCSI Chip Compatibility | 1 | `qa/dv/Use Macintosh SCSI Manager for SCSI Chip Compatibility.md` | 未开始 |
| 853 | Use QuickDraw 3D B1C3 Library to Eliminate User Breaks | 1 | `qa/qd3d/Use QuickDraw 3D B1C3 Library to Eliminate User Breaks.md` | 未开始 |
| 854 | Use the Doorbell | 1 | `qa/fw/Use the Doorbell` | 未开始 |
| 855 | User Clicking in a Style Text Document, Human Interface Guidelines | 1 | `qa/tx/User Clicking in a Style Text Document, Human Interface Guidelines.md` | 未开始 |
| 856 | User Interface Tool Demo at WWDC | 1 | `qa/qd3d/User Interface Tool Demo at WWDC.md` | 未开始 |
| 857 | Using "words" in Open Firmware | 1 | `qa/hw/Using -words- in Open Firmware` | 未开始 |
| 858 | Using 'ictb' to Change Edit Fields | 1 | `qa/tb/Using 'ictb' to Change Edit Fields` | 未开始 |
| 859 | Using .zip and .jar Files With Applets | 1 | `qa/java/Using .zip and .jar Files With Applets` | 未开始 |
| 860 | Using AppleScript to send an email with an attachment | 1 | `qa/qa2001/Calling an AppleScript and providing parameters from an Application/Legacy Documentclose button.md` | 未开始 |
| 861 | Using Background Printing When The Finder Isn't Present | 1 | `qa/qd/Using Background Printing When The Finder Isn't Present.md` | 未开始 |
| 862 | Using ConvertMovieToFile or ConvertMovieToDataRef to convert movies without | 1 | `qa/Using ConvertMovieToFile or ConvertMovieToDataRef to convert movies without disp.md` | 未开始 |
| 863 | Using Custom creator codes for USB Class Drivers | 1 | `qa/usb/Using Custom creator codes for USB Class Drivers.md` | 未开始 |
| 864 | Using Deferred Tasks | 1 | `qa/nw/Using Deferred Tasks` | 未开始 |
| 865 | Using Digital Cameras | 1 | `qa/qtvr/Using Digital Cameras.md` | 未开始 |
| 866 | Using GXNewPaperType | 1 | `qa/gxpd/Using GXNewPaperType.md` | 未开始 |
| 867 | Using Hardware Acceleration | 1 | `qa/qd3d/Using Hardware Acceleration.md` | 未开始 |
| 868 | Using JDK Tools Under MRJ 2.2 | 1 | `qa/java/Using JDK Tools Under MRJ 2.2` | 未开始 |
| 869 | Using LaserWriter fonts with StyleWriter | 1 | `qa/qd/Using LaserWriter fonts with StyleWriter.md` | 未开始 |
| 870 | Using Legacy Ethernet Driver Processes on a PowerMac G3 | 1 | `qa/nw/Using Legacy Ethernet Driver Processes on a PowerMac G3` | 未开始 |
| 871 | Using MacsBug to Diagnose Field Problems | 1 | `qa/plat/Using MacsBug to Diagnose Field Problems` | 未开始 |
| 872 | Using MovieExportSetSampleDescription to specify the format of exported data | 1 | `qa/qtmtb/Using MovieExportSetSampleDescription to specify the format of exported data.md` | 未开始 |
| 873 | Using Navigation Services to filter QuickTime files | 1 | `qa/qa2001/Using Navigation Services to filter QuickTime files` | 未开始 |
| 874 | Using OpenTransport With CFM-68K | 1 | `qa/nw/Using OpenTransport With CFM-68K` | 未开始 |
| 875 | Using PICT Comments to Stretch and Rotate Objects | 1 | `qa/gxpd/Using PICT Comments to Stretch and Rotate Objects.md` | 未开始 |
| 876 | Using PixPatHandle to Access the "Set Utilities Pattern" Pattern | 1 | `qa/ops/Using PixPatHandle to Access the -Set Utilities Pattern- Pattern` | 未开始 |
| 877 | Using PrGeneral() to Download Fonts | 1 | `qa/qd/Using PrGeneral() to Download Fonts.md` | 未开始 |
| 878 | Using QTPixelBufferContextCreate with NewMovieFromProperties | 1 | `qa/Using QTPixelBufferContextCreate with NewMovieFromProperties` | 未开始 |
| 879 | Using QTSetAtomData | 1 | `qa/Using QTSetAtomData.md` | 未开始 |
| 880 | Using QuickTime to access MP3 ID3 Tags | 1 | `qa/qa2001/Using QuickTime to access MP3 ID3 Tags` | 未开始 |
| 881 | Using SKCloudServiceController to determine your device's music library capabilities | 1 | `qa/Using SKCloudServiceController to determine your device's music library capabili.md` | 未开始 |
| 882 | Using SetMovieGWorld to draw to the window back buffer | 1 | `qa/qa2001/Using SetMovieGWorld to draw to the window back buffer` | 未开始 |
| 883 | Using SourceSafe without MPW or Toolserver | 1 | `qa/plat/Using SourceSafe without MPW or Toolserver` | 未开始 |
| 884 | Using Standard SCSI Disk Drives on Macs | 1 | `qa/dv/Using Standard SCSI Disk Drives on Macs.md` | 未开始 |
| 885 | Using System.currentTimeMillis( ) | 1 | `qa/java/Using System.currentTimeMillis( )` | 未开始 |
| 886 | Using Temporary Memory with OpenPicture | 1 | `qa/qd/Using Temporary Memory with OpenPicture.md` | 未开始 |
| 887 | Using UIWebView to display select document types | 1 | `qa/Using UIWebView to display select document types.md` | 未开始 |
| 888 | Using a QuickTime time base callback to detect when a movie has stopped | 1 | `qa/qa2001/Using a QuickTime time base callback to detect when a movie has stopped` | 未开始 |
| 889 | Using cmpWantsRegisterMessage not recommended on Mac OS X | 1 | `qa/qa2001/Using cmpWantsRegisterMessage not recommended on Mac OS X` | 未开始 |
| 890 | Using language-tagged QuickTime UserData text APIs with CFStrings | 1 | `qa/Using language-tagged QuickTime UserData text APIs with CFStrings.md` | 未开始 |
| 891 | Using qd and QDGlobals | 1 | `qa/qd/Using qd and QDGlobals.md` | 未开始 |
| 892 | Using stdin on the Macintosh | 1 | `qa/java/Using stdin on the Macintosh` | 未开始 |
| 893 | Using the Color Table Stored in a Movie | 1 | `qa/qtmcc/Using the Color Table Stored in a Movie.md` | 未开始 |
| 894 | Using the Command key when Resizing a Window | 1 | `qa/tb/Using the Command key when Resizing a Window` | 未开始 |
| 895 | Using the Licensed Espy Font | 1 | `qa/tx/Using the Licensed Espy Font.md` | 未开始 |
| 896 | Using the MRJ with IE 5 | 1 | `qa/java/Using the MRJ with IE 5` | 未开始 |
| 897 | Using the QuickTime DVCompressor properties | 1 | `qa/Using the QuickTime DVCompressor properties.md` | 未开始 |
| 898 | Using the kQTPropertyClass_DRM properties with QuickTime | 1 | `qa/Using the kQTPropertyClassDRM properties with QuickTime.md` | 未开始 |
| 899 | VBL Tasking and calling FrontWindow | 1 | `qa/tb/VBL Tasking and calling FrontWindow` | 未开始 |
| 900 | VBL Tasking and calling FrontWindow | 1 | `qa/qd/VBL Tasking and calling FrontWindow.md` | 未开始 |
| 901 | Valid QD3D Metafile Filename Extensions | 1 | `qa/qd3d/Valid QD3D Metafile Filename Extensions.md` | 未开始 |
| 902 | Verifying the PCI Interface | 1 | `qa/hw/Verifying the PCI Interface` | 未开始 |
| 903 | Video Digitizers - Adding Clean Aperture and Pixel Aspect Ratio Information | 1 | `qa/Video Digitizers - Adding Clean Aperture and Pixel Aspect Ratio Information.md` | 未开始 |
| 904 | Video Output Components - Implementing QTVideoOutputGetIndSoundOutput on Mac | 1 | `qa/qa2001/Video Output Components - Implementing QTVideoOutputGetIndSoundOutput on Mac OS` | 未开始 |
| 905 | Video Output Components - QTVideoOutputGetIndImageDecompressor | 1 | `qa/qa2001/Video Output Components - QTVideoOutputGetIndImageDecompressor` | 未开始 |
| 906 | View Hints | 1 | `qa/qd3d/View Hints.md` | 未开始 |
| 907 | Viewer Error "xy values outside of the viewing window" Explained | 1 | `qa/qd3d/Viewer Error -xy values outside of the viewing window- Explained.md` | 未开始 |
| 908 | Viewer Only Supports Perspective Cameras | 1 | `qa/qd3d/Viewer Only Supports Perspective Cameras.md` | 未开始 |
| 909 | Viewing multi-page PDF files | 1 | `qa/qa2001/Viewing multi-page PDF files` | 未开始 |
| 910 | Virtual Memory Management | 1 | `qa/me/Virtual Memory Management.md` | 未开始 |
| 911 | WS PDS Card and SCSI Manager 4.3 | 1 | `qa/dv/WS PDS Card and SCSI Manager 4.3.md` | 未开始 |
| 912 | WaitMouseUp documentation errata | 1 | `qa/qa2001/WaitMouseUp documentation errata` | 未开始 |
| 913 | Was that a path I just saw? | 1 | `qa/hw/Was that a path I just saw` | 未开始 |
| 914 | WebObjects applications crashing on NT using IIS | 1 | `qa/WebObjects applications crashing on NT using IIS.md` | 未开始 |
| 915 | What are NewWorld and Open Firmware version 3? | 1 | `qa/hw/What are NewWorld and Open Firmware version 3` | 未开始 |
| 916 | What are configuration variables in Open Firmware? | 1 | `qa/hw/What are configuration variables in Open Firmware` | 未开始 |
| 917 | What are generic names in Open Firmware? | 1 | `qa/hw/What are generic names in Open Firmware` | 未开始 |
| 918 | What are snag keys in Open Firmware? | 1 | `qa/hw/What are snag keys in Open Firmware` | 未开始 |
| 919 | What depth should I put in an Image Description? | 1 | `qa/What depth should I put in an Image Description.md` | 未开始 |
| 920 | What is JAR caching? | 1 | `qa/java/What is JAR caching` | 未开始 |
| 921 | What is SetMovieDefaultDataRef? | 1 | `qa/qtmtb/What is SetMovieDefaultDataRef.md` | 未开始 |
| 922 | What is a 'scsz' resource in Java? | 1 | `qa/java/What is a 'scsz' resource in Java` | 未开始 |
| 923 | What is a tokenizer? | 1 | `qa/hw/What is a tokenizer` | 未开始 |
| 924 | What is an Open Firmware devalias? | 1 | `qa/hw/What is an Open Firmware devalias` | 未开始 |
| 925 | What is an Open Firmware phandle, and why can't I access it from the Mac OS? | 1 | `qa/hw/What is an Open Firmware phandle, and why can't I access it from the Mac OS` | 未开始 |
| 926 | What is meant by 1 machine mode vs. 2 machine mode with respect to Open Firmware? | 1 | `qa/hw/What is meant by 1 machine mode vs. 2 machine mode with respect to Open Firmware` | 未开始 |
| 927 | What is the minimal set of Carbon Events I need to override in order to implement | 1 | `qa/qa2001/What is the minimal set of Carbon Events I need to override in order to implemen` | 未开始 |
| 928 | What is the return stack in Open Firmware and can I use it? | 1 | `qa/hw/What is the return stack in Open Firmware and can I use it` | 未开始 |
| 929 | What is the word "see" and how do I use it to help me find what a word does? | 1 | `qa/hw/What is the word -see- and how do I use it to help me find what a word does` | 未开始 |
| 930 | When to use PCMCIA, PC Card, and CardBus | 1 | `qa/hw/When to use PCMCIA, PC Card, and CardBus` | 未开始 |
| 931 | Where do QuickTime extension files reside on Windows systems? | 1 | `qa/Where do QuickTime extension files reside on Windows systems.md` | 未开始 |
| 932 | Which Machines Support Driver Services Library and the MP Nanokernel? | 1 | `qa/hw/Which Machines Support Driver Services Library and the MP Nanokernel` | 未开始 |
| 933 | White Backgrounds for Dialog editText Items | 1 | `qa/tb/White Backgrounds for Dialog editText Items` | 未开始 |
| 934 | White Text on Black Background | 1 | `qa/qd/White Text on Black Background.md` | 未开始 |
| 935 | Why am I not receiving kEventControlHit events for some of the parts of my | 1 | `qa/Why am I not receiving kEventControlHit events for some of the parts of my custo.md` | 未开始 |
| 936 | Why does UILocalizedIndexedCollation not give localized results? | 1 | `qa/Why does UILocalizedIndexedCollation not give localized results.md` | 未开始 |
| 937 | Why does logging keep my Printer Module from working? | 1 | `qa/qa2001/Why does logging keep my Printer Module from working` | 未开始 |
| 938 | Why does my identity matrix look strange? | 1 | `qa/qa2001/Why does my identity matrix look strange` | 未开始 |
| 939 | Why doesn't my Scrolling Text Box control work in a compositing window? | 1 | `qa/qa2001/Why doesn't my Scrolling Text Box control work in a compositing window` | 未开始 |
| 940 | Why is my Control/HIView not accepting drops on Mac OS X v10.4 (Tiger)? | 1 | `qa/qa2005/Why is my Control-HIView not accepting drops on Mac OS X v10.4 (Tiger)` | 未开始 |
| 941 | Why is my application crashing in QuickDraw when I'm not using it? | 1 | `qa/Why is my application crashing in QuickDraw when I'm not using it.md` | 未开始 |
| 942 | Why isn't my QuickTime Component recognized by iMovie '08? | 1 | `qa/Why isn't my QuickTime Component recognized by iMovie '08.md` | 未开始 |
| 943 | Why isn't my Static Text Control deactivating when my other controls are? | 1 | `qa/qa2001/Why isn't my Static Text Control deactivating when my other controls are` | 未开始 |
| 944 | Why isn't my edit text box in my Navigation dialog's custom area working on | 1 | `qa/qa2001/Why isn't my edit text box in my Navigation dialog's custom area working on 10.3` | 未开始 |
| 945 | Window Manager and EraseRect | 1 | `qa/qd/Window Manager and EraseRect.md` | 未开始 |
| 946 | WindowShade Problems | 1 | `qa/tb/WindowShade Problems` | 未开始 |
| 947 | Workaround for Asynchronous SCSIAction Crashes | 1 | `qa/qa2001/Workaround for Asynchronous SCSIAction Crashes` | 未开始 |
| 948 | Workaround for Converting Lower to Uppercase Characters while Keeping Diacritical | 1 | `qa/tx/Workaround for Converting Lower to Uppercase Characters while Keeping Diacritica.md` | 未开始 |
| 949 | Workaround for PLookupName Bug | 1 | `qa/nw/Workaround for PLookupName Bug` | 未开始 |
| 950 | Working with Configuration Variables | 1 | `qa/qa2001/Working with Configuration Variables` | 未开始 |
| 951 | Working with groups and folder references in Project Builder | 1 | `qa/qa2001/Working with groups and folder references in Project Builder` | 未开始 |
| 952 | Writing Native SCSI Disk Drivers for PowerMacs | 1 | `qa/dv/Writing Native SCSI Disk Drivers for PowerMacs.md` | 未开始 |
| 953 | aglChoosePixelFormat, The Inside Scoop | 1 | `qa/ogl/aglChoosePixelFormat, The Inside Scoop.md` | 未开始 |
| 954 | couldNotResolveDataRef (-2000) returned from DataHSetDataRef and OpenADataHandler | 1 | `qa/qa2001/couldNotResolveDataRef (-2000) returned from DataHSetDataRef and OpenADataHandle` | 未开始 |
| 955 | dl command in 1 machine mode | 1 | `qa/hw/dl command in 1 machine mode` | 未开始 |
| 956 | fBroadCastAddr Always Zero | 1 | `qa/nw/fBroadCastAddr Always Zero` | 未开始 |
| 957 | gestaltFWVMBackingStore | 1 | `qa/fw/gestaltFWVMBackingStore` | 未开始 |
| 958 | grayishTextOr and Mac OS 8.5 | 1 | `qa/qd/grayishTextOr and Mac OS 8.5.md` | 未开始 |
| 959 | iOS 10 and the Legacy VoIP Architecture | 1 | `qa/iOS 10 and the Legacy VoIP Architecture.md` | 未开始 |
| 960 | iSight - Configuring gain settings for IIDC cameras | 1 | `qa/iSight - Configuring gain settings for IIDC cameras` | 未开始 |
| 961 | noResponseErr from PPC Toolbox | 1 | `qa/ic/noResponseErr from PPC Toolbox.md` | 未开始 |
| 962 | paramErr returned from ConvertMovieToFile when exporting to .wav | 1 | `qa/qa2001/paramErr returned from ConvertMovieToFile when exporting to .wav` | 未开始 |
| 963 | pointOfInterest | 1 | `qa/qd3d/pointOfInterest.md` | 未开始 |
| 964 | siActive Channels Unsupported on Some Power Macs | 1 | `qa/snd/siActive Channels Unsupported on Some Power Macs.md` | 未开始 |
| 965 | siMonitorSource Selector | 1 | `qa/snd/siMonitorSource Selector/Not Recommended Documentclose button.md` | 未开始 |
| 966 | siOSTypeInput Selectors | 1 | `qa/snd/siMonitorSource Selector/Not Recommended Documentclose button-2.md` | 未开始 |
| 967 | siOSTypeInputAvailable Format | 1 | `qa/snd/siOSTypeInputAvailable Format.md` | 未开始 |
| 968 | spatialQuality Values with Lossy Compression | 1 | `qa/qa2001/spatialQuality Values with Lossy Compression` | 未开始 |
| 969 | xSYM files | 1 | `qa/ppcsys/xSYM files.md` | 未开始 |

### 音视频与特效（89 份，89 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 970 | 'AudioConverter: How do I know when I am done?' | 1 | `qa/AudioConverter- How do I know when I am done.md` | 未开始 |
| 971 | AUAudioFilePlayer - Using the Audio File Player Audio Unit | 1 | `qa/AUAudioFilePlayer - Using the Audio File Player Audio Unit.md` | 未开始 |
| 972 | AUGraphs and AudioUnit connections | 1 | `qa/AUGraphs and AudioUnit connections.md` | 未开始 |
| 973 | AUSampler - Adding Instrument Information and Loop Points to Core Audio Files | 1 | `qa/AUSampler - Adding Instrument Information and Loop Points to Core Audio Files.md` | 未开始 |
| 974 | AUSampler - Available Audio Unit Parameters | 1 | `qa/AUSampler - Available Audio Unit Parameters.md` | 未开始 |
| 975 | AVAssetExportSession - Exporting a Trimmed Audio Asset | 1 | `qa/AVAssetExportSession - Exporting a Trimmed Audio Asset.md` | 未开始 |
| 976 | AVAudioPlayer Streaming Support | 1 | `qa/AVAudioPlayer Streaming Support.md` | 未开始 |
| 977 | AVAudioSession -  How setting a category and mode affect the ability to route | 1 | `qa/AVAudioSession - How setting a category and mode affect the ability to route aud.md` | 未开始 |
| 978 | AVAudioSession - AVAudioSessionSilenceSecondaryAudioHintNotification Explained | 1 | `qa/AVAudioSession - AVAudioSessionSilenceSecondaryAudioHintNotification Explained.md` | 未开始 |
| 979 | AVAudioSession - Audio Session APIs & The Remote IO Render Proc. | 1 | `qa/AVAudioSession - Audio Session APIs & The Remote IO Render Proc.md` | 未开始 |
| 980 | AVAudioSession - Differences between AVAudioSessionPortOverrideSpeaker and | 1 | `qa/AVAudioSession - Differences between AVAudioSessionPortOverrideSpeaker and AVAud.md` | 未开始 |
| 981 | AVAudioSession - General recommendations for handling AVAudioSessionMediaServicesWereResetNotification | 1 | `qa/AVAudioSession - General recommendations for handling AVAudioSessionMediaService` | 未开始 |
| 982 | AVAudioSession - Microphone Selection | 1 | `qa/AVAudioSession - Microphone Selection.md` | 未开始 |
| 983 | AVAudioSession - Requesting Audio Session Preferences | 1 | `qa/AVAudioSession - Requesting Audio Session Preferences.md` | 未开始 |
| 984 | Accessing Audio Files in Asset Catalogs | 1 | `qa/Accessing Audio Files in Asset Catalogs` | 未开始 |
| 985 | Adding Bluetooth LE MIDI Support | 1 | `qa/Adding Bluetooth LE MIDI Support` | 未开始 |
| 986 | Always check the result code from AudioUnitGetProperty when used with kAudioUnitProperty_FastDispatch | 1 | `qa/Always check the result code from AudioUnitGetProperty when used with kAudioUnit.md` | 未开始 |
| 987 | Audio Host Time On iOS | 1 | `qa/Audio Host Time On iOS.md` | 未开始 |
| 988 | Audio Interruptions during Movie Playback | 1 | `qa/Audio Interruptions during Movie Playback.md` | 未开始 |
| 989 | Audio Queue - Looping Compressed Audio | 1 | `qa/Audio Queue - Looping Compressed Audio.md` | 未开始 |
| 990 | Audio Queue - Offline Rendering | 1 | `qa/Audio Queue - Offline Rendering.md` | 未开始 |
| 991 | Audio Queue - Playing an Audio File Containing HE-AAC Encoded Audio | 1 | `qa/Audio Queue - Playing an Audio File Containing HE-AAC Encoded Audio.md` | 未开始 |
| 992 | Audio Queue - Recording to a compressed audio format. | 1 | `qa/Audio Queue - Recording to a compressed audio format.md` | 未开始 |
| 993 | Audio Queue playback sample time and buffer sample time explained | 1 | `qa/Audio Queue playback sample time and buffer sample time explained.md` | 未开始 |
| 994 | Audio Server PlugIn - The AudioServerPlugIn_MachServices plist Key | 1 | `qa/Audio Server PlugIn - The AudioServerPlugInMachServices plist Key` | 未开始 |
| 995 | Audio Session - Ensuring audio playback continues when screen is locked | 1 | `qa/Audio Session - Ensuring audio playback continues when screen is locked.md` | 未开始 |
| 996 | Audio Unit - Handling audio unit authorization (copy protection) | 1 | `qa/Audio Unit - Handling audio unit authorization (copy protection)` | 未开始 |
| 997 | Audio Unit - Testing your custom Audio Unit in a sandboxed environment | 1 | `qa/Audio Unit - Testing your custom Audio Unit in a sandboxed environment.md` | 未开始 |
| 998 | Audio Unit Processing Graph - Ensuring audio playback continues when screen | 1 | `qa/Audio Unit Processing Graph - Ensuring audio playback continues when screen is l.md` | 未开始 |
| 999 | Audio Unit Properties and Core Foundation Data Types | 1 | `qa/Audio Unit Properties and Core Foundation Data Types.md` | 未开始 |
| 1000 | Audio Unit Resizing | 1 | `qa/Audio Unit Resizing.md` | 未开始 |
| 1001 | Audio Units - How to determine the version of an Audio Unit | 1 | `qa/Audio Units - How to determine the version of an Audio Unit.md` | 未开始 |
| 1002 | Audio panning with the 3D Mixer audio unit | 1 | `qa/Audio panning with the 3D Mixer audio unit.md` | 未开始 |
| 1003 | AudioDevice Sample Rates | 1 | `qa/AudioDevice Sample Rates.md` | 未开始 |
| 1004 | AudioFileOpenWithCallbacks - Avoiding Permissions Error With MPEG-4 File Types | 1 | `qa/AudioFileOpenWithCallbacks - Avoiding Permissions Error With MPEG-4 File Types.md` | 未开始 |
| 1005 | Avoiding the -42 error with DiscRecording | 1 | `qa/Avoiding the -42 error with DiscRecording.md` | 未开始 |
| 1006 | Capturing a sequence of still images very quickly with AV Foundation on iOS | 1 | `qa/Capturing a sequence of still images very quickly with AV Foundation on iOS.md` | 未开始 |
| 1007 | Changing the volume of audio devices | 1 | `qa/Changing the volume of audio devices.md` | 未开始 |
| 1008 | Core Video - Available Pixel Formats | 1 | `qa/Core Video - Available Pixel Formats.md` | 未开始 |
| 1009 | CoreAudio Overload Warnings | 1 | `qa/CoreAudio Overload Warnings.md` | 未开始 |
| 1010 | CoreAudio PublicUtility - Installing the CARingBuffer Update | 1 | `qa/CoreAudio PublicUtility - Installing the CARingBuffer Update.md` | 未开始 |
| 1011 | Creating Core Audio Format (.caf) Files | 1 | `qa/Creating Core Audio Format (.caf) Files.md` | 未开始 |
| 1012 | Customizing subtitles with AVPlayer | 1 | `qa/Customizing subtitles with AVPlayer.md` | 未开始 |
| 1013 | Determining the availability of the AAC hardware encoder at runtime | 1 | `qa/Determining the availability of the AAC hardware encoder at runtime.md` | 未开始 |
| 1014 | Disabling user interaction in an app while the media is still loading | 1 | `qa/Disabling user interaction in an app while the media is still loading.md` | 未开始 |
| 1015 | ExtAudioFile - ExtAudioFileTell Incorrect Position Work Around | 1 | `qa/ExtAudioFile - ExtAudioFileTell Incorrect Position Work Around.md` | 未开始 |
| 1016 | FairPlay Streaming Server SDK Development Credentials | 1 | `qa/FairPlay Streaming Server SDK Development Credentials.md` | 未开始 |
| 1017 | Finding the latest Audio Tools for Xcode 4.3 or later | 1 | `qa/Finding the latest Audio Tools for Xcode 4.3 or later` | 未开始 |
| 1018 | Getting attachments from a CMSampleBufferRef object | 1 | `qa/Getting attachments from a CMSampleBufferRef object.md` | 未开始 |
| 1019 | How do I achieve smooth video scrubbing with AVPlayer seekToTime:? | 1 | `qa/How do I achieve smooth video scrubbing with AVPlayer seekToTime.md` | 未开始 |
| 1020 | How do I set the volume of audio media for playback with AVPlayer on iOS? | 1 | `qa/How do I set the volume of audio media for playback with AVPlayer on iOS.md` | 未开始 |
| 1021 | How to capture screen activity to a movie file using AV Foundation on OS X | 1 | `qa/How to capture screen activity to a movie file using AV Foundation on OS X 10.7.md` | 未开始 |
| 1022 | How to capture video frames from the camera as images using AV Foundation on | 1 | `qa/How to capture video frames from the camera as images using AV Foundation on iOS.md` | 未开始 |
| 1023 | How to determine whether an AVPlayerItem can be played at rates greater than | 1 | `qa/How to determine whether an AVPlayerItem can be played at rates greater than 1.0.md` | 未开始 |
| 1024 | How to handle audio data with magic cookie information | 1 | `qa/How to handle audio data with magic cookie information.md` | 未开始 |
| 1025 | How to handle kAudioUnitProperty_MaximumFramesPerSlice | 1 | `qa/How to handle kAudioUnitPropertyMaximumFramesPerSlice.md` | 未开始 |
| 1026 | MPMoviePlayerController plays movie audio but not video | 1 | `qa/MPMoviePlayerController plays movie audio but not video.md` | 未开始 |
| 1027 | MTAudioProcessingTap - The Pre and Post effect MTAudioProcessingTapCreationFlags | 1 | `qa/MTAudioProcessingTap - The Pre and Post effect MTAudioProcessingTapCreationFlags` | 未开始 |
| 1028 | Move off AudioUnitRemovePropertyListener and the Component Manager on Mac OS | 1 | `qa/Move off AudioUnitRemovePropertyListener and the Component Manager on Mac OS X 1.md` | 未开始 |
| 1029 | Music Player Sequence Destinations | 1 | `qa/Music Player Sequence Destinations.md` | 未开始 |
| 1030 | Obtaining the name of an external MIDI Device from a MIDI Endpoint | 1 | `qa/Obtaining the name of an external MIDI Device from a MIDI Endpoint.md` | 未开始 |
| 1031 | Preventing HTTP Live Streaming video in an iOS 8 app from being captured during | 1 | `qa/Preventing HTTP Live Streaming video in an iOS 8 app from being captured during.md` | 未开始 |
| 1032 | QTKit Capture - Disabling Audio Or Video When Capturing From a Muxed Device | 1 | `qa/QTKit Capture - Disabling Audio Or Video When Capturing From a Muxed Device.md` | 未开始 |
| 1033 | QTKit Capture - Disabling specific audio channels when recording | 1 | `qa/QTKit Capture - Disabling specific audio channels when recording.md` | 未开始 |
| 1034 | QTKit Capture - Extracting SMPTE Timecode information from a QTSampleBuffer | 1 | `qa/QTKit Capture - Extracting SMPTE Timecode information from a QTSampleBuffer.md` | 未开始 |
| 1035 | QTKit Capture - Setting DecompressedVideoOutput CVPixelBuffer Attributes | 1 | `qa/QTKit Capture - Setting DecompressedVideoOutput CVPixelBuffer Attributes.md` | 未开始 |
| 1036 | QTKit Capture - Specifying Media Compression Settings | 1 | `qa/QTKit Capture - Specifying Media Compression Settings.md` | 未开始 |
| 1037 | QTKit Capture - Video Compression Options And Preview | 1 | `qa/QTKit Capture - Video Compression Options And Preview.md` | 未开始 |
| 1038 | Recording Audio from an App Extension | 1 | `qa/Recording Audio from an App Extension.md` | 未开始 |
| 1039 | Recording a movie (including audio) and playing a sound simultaneously | 1 | `qa/Recording a movie (including audio) and playing a sound simultaneously.md` | 未开始 |
| 1040 | Remote I/O Audio Unit - Handling changes in the inNumberOfFrames value when | 1 | `qa/Remote I-O Audio Unit - Handling changes in the inNumberOfFrames value when rend.md` | 未开始 |
| 1041 | Rendering the currently visible frame of a paused AVPlayer that has a custom | 1 | `qa/Rendering the currently visible frame of a paused AVPlayer that has a custom vid.md` | 未开始 |
| 1042 | Responding to screen capture in iOS 11. | 1 | `qa/Responding to screen capture in iOS 11.md` | 未开始 |
| 1043 | Setting the orientation of video with AV Foundation | 1 | `qa/Setting the orientation of video with AV Foundation.md` | 未开始 |
| 1044 | Signaling the end of data when using AudioConverterFillComplexBuffer | 1 | `qa/Signaling the end of data when using AudioConverterFillComplexBuffer.md` | 未开始 |
| 1045 | Specifying color space information for pixel buffers | 1 | `qa/Specifying color space information for pixel buffers.md` | 未开始 |
| 1046 | The Default Output Audio Units | 1 | `qa/The Default Output Audio Units.md` | 未开始 |
| 1047 | The header file 'alut.h' is missing from the OpenAL framework. | 1 | `qa/The header file 'alut.h' is missing from the OpenAL framework.md` | 未开始 |
| 1048 | Unable to select input device in AU Lab | 1 | `qa/Unable to select input device in AU Lab.md` | 未开始 |
| 1049 | Understanding the bytes per row value returned by CVPixelBufferGetBytesPerRow | 1 | `qa/Understanding the bytes per row value returned by CVPixelBufferGetBytesPerRow.md` | 未开始 |
| 1050 | Use NSSound instead of NSMovie for audio only playback on Mac OS X 10.3 and | 1 | `qa/qa2001/Use NSSound instead of NSMovie for audio only playback on Mac OS X 10.3 and grea` | 未开始 |
| 1051 | Using NSSound with CoreAudio on Mac OS 10.3.x | 1 | `qa/Using NSSound with CoreAudio on Mac OS 10.3.x.md` | 未开始 |
| 1052 | Using the ExtAudioFileSeek and ExtAudioFileTell Functions | 1 | `qa/Using the ExtAudioFileSeek and ExtAudioFileTell Functions.md` | 未开始 |
| 1053 | Using the iPodTime audio unit for playing audio books | 1 | `qa/Using the iPodTime audio unit for playing audio books.md` | 未开始 |
| 1054 | Video Player unexpectedly shows Alternate Track button for Subtitles and Captions | 1 | `qa/Video Player unexpectedly shows Alternate Track button for Subtitles and Caption` | 未开始 |
| 1055 | Video capture with multiple IIDC cameras | 1 | `qa/Video capture with multiple IIDC cameras.md` | 未开始 |
| 1056 | VideoToolbox compression property kVTCompressionPropertyKey_DataRateLimits | 1 | `qa/VideoToolbox compression property kVTCompressionPropertyKeyDataRateLimits explai.md` | 未开始 |
| 1057 | Voice Processing Audio Unit Quality Settings | 1 | `qa/Voice Processing Audio Unit Quality Settings.md` | 未开始 |
| 1058 | auval - Invalid Selector For AU Type Error on Mac OS X 10.7 | 1 | `qa/auval - Invalid Selector For AU Type Error on Mac OS X 10.7.md` | 未开始 |

### 图形与动画（88 份，88 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 1059 | AGL Changes for Mac OS X Leopard (v. 10.5) | 1 | `qa/AGL Changes for Mac OS X Leopard (v. 10.5).md` | 未开始 |
| 1060 | Accessing image properties with ImageIO | 1 | `qa/Accessing image properties with ImageIO.md` | 未开始 |
| 1061 | Allowing OpenGL applications to utilize the integrated GPU | 1 | `qa/Allowing OpenGL applications to utilize the integrated GPU` | 未开始 |
| 1062 | Animating the frame of a CALayer. | 1 | `qa/Animating the frame of a CALayer.md` | 未开始 |
| 1063 | Apple RGB and Generic RGB profiles explained | 1 | `qa/Apple RGB and Generic RGB profiles explained.md` | 未开始 |
| 1064 | Availability of Quartz Composer Patches in Web Kit | 1 | `qa/Availability of Quartz Composer Patches in Web Kit` | 未开始 |
| 1065 | Bonjour Printer Subtype for HTTP | 1 | `qa/Bonjour Printer Subtype for HTTP.md` | 未开始 |
| 1066 | CATiledLayer and UIKit graphics | 1 | `qa/CATiledLayer and UIKit graphics.md` | 未开始 |
| 1067 | CGBitmapContextCreate Supported Color Spaces | 1 | `qa/CGBitmapContextCreate Supported Color Spaces.md` | 未开始 |
| 1068 | CGContext Bounds | 1 | `qa/qa2001/CGContext Bounds` | 未开始 |
| 1069 | CGContextAddLineToPoint, CGContextAddCurveToPoint, et. al. | 1 | `qa/qa2001/CGContextAddLineToPoint, CGContextAddCurveToPoint, et. al` | 未开始 |
| 1070 | CGContextClosePath | 1 | `qa/qa2001/CGContextClosePath` | 未开始 |
| 1071 | CGImageRef contents are immutable | 1 | `qa/CGImageRef contents are immutable.md` | 未开始 |
| 1072 | ColorSync Color Matching on Intel-based Macs | 1 | `qa/ColorSync Color Matching on Intel-based Macs.md` | 未开始 |
| 1073 | Combinations of cupsColorSpace, cupsColorOrder and cupsBitsPerColor values | 1 | `qa/Combinations of cupsColorSpace, cupsColorOrder and cupsBitsPerColor values suppo.md` | 未开始 |
| 1074 | Compiling X11 / OpenGL applications on Mac OS X  v.10.5 Leopard | 1 | `qa/Compiling X11 - OpenGL applications on Mac OS X v.10.5 Leopard.md` | 未开始 |
| 1075 | Context Sharing Tips | 1 | `qa/Context Sharing Tips.md` | 未开始 |
| 1076 | Core Animation properties and Reference Counting | 1 | `qa/Core Animation properties and Reference Counting.md` | 未开始 |
| 1077 | Creating IOSurface-backed CVPixelBuffers for accessing video data in OpenGL | 1 | `qa/Creating IOSurface-backed CVPixelBuffers for accessing video data in OpenGL ES.md` | 未开始 |
| 1078 | Creating an OpenGL texture from an NSView | 1 | `qa/qa2001/Creating an OpenGL texture from an NSView` | 未开始 |
| 1079 | Creating color spaces that ensure color matching. | 1 | `qa/Creating color spaces that ensure color matching.md` | 未开始 |
| 1080 | Deprecated built-in variables in GLSL Shaders | 1 | `qa/Deprecated built-in variables in GLSL Shaders.md` | 未开始 |
| 1081 | Determining if a printer is capable of color output. | 1 | `qa/Determining if a printer is capable of color output.md` | 未开始 |
| 1082 | Does CGContextSaveGState save the current path? | 1 | `qa/Does CGContextSaveGState save the current path.md` | 未开始 |
| 1083 | Drawing a Path Multiple Times | 1 | `qa/qa2001/Drawing a Path Multiple Times` | 未开始 |
| 1084 | Driving OpenGL Rendering Loops | 1 | `qa/Driving OpenGL Rendering Loops.md` | 未开始 |
| 1085 | Embedding ICC Profiles | 1 | `qa/c/Embedding ICC Profiles` | 未开始 |
| 1086 | Ensuring custom effects render correctly in Photo Booth for Mac OS X Lion | 1 | `qa/Ensuring custom effects render correctly in Photo Booth for Mac OS X Lion.md` | 未开始 |
| 1087 | Ensuring hardware accelerated rendering for your OpenGL application | 1 | `qa/Ensuring hardware accelerated rendering for your OpenGL application.md` | 未开始 |
| 1088 | GetProcAdress and OpenGL Entry Points | 1 | `qa/qa2001/GetProcAdress and OpenGL Entry Points` | 未开始 |
| 1089 | Getting the name of a profile | 1 | `qa/qa2001/Getting the name of a profile` | 未开始 |
| 1090 | Getting the pixel data from a CGImage object | 1 | `qa/Getting the pixel data from a CGImage object.md` | 未开始 |
| 1091 | How can I optimize a Quartz Composer composition depending on the hardware | 1 | `qa/How can I optimize a Quartz Composer composition depending on the hardware it ru` | 未开始 |
| 1092 | How can I programmatically determine the DPI of the current video mode? | 1 | `qa/qa2001/How can I programmatically determine the DPI of the current video mode` | 未开始 |
| 1093 | How do I determine how much VRAM is available on my video card? | 1 | `qa/How do I determine how much VRAM is available on my video card.md` | 未开始 |
| 1094 | How do I get the hexadecimal value of an NSColor object? | 1 | `qa/How do I get the hexadecimal value of an NSColor object.md` | 未开始 |
| 1095 | How do I take a screenshot of my app that contains both UIKit and Camera elements? | 1 | `qa/How do I take a screenshot of my app that contains both UIKit and Camera element.md` | 未开始 |
| 1096 | How do I tell if a particular display is being hardware accelerated by Quartz | 1 | `qa/How do I tell if a particular display is being hardware accelerated by Quartz Ex.md` | 未开始 |
| 1097 | How to measure CG text | 1 | `qa/How to measure CG text.md` | 未开始 |
| 1098 | How to pause the animation of a layer tree | 1 | `qa/How to pause the animation of a layer tree.md` | 未开始 |
| 1099 | How to take an image snapshot of the screen on Mac OS X Lion | 1 | `qa/How to take an image snapshot of the screen on Mac OS X Lion.md` | 未开始 |
| 1100 | ICC Profile copyright field | 1 | `qa/qa2001/ICC Profile copyright field` | 未开始 |
| 1101 | IKImageView with drag and drop | 1 | `qa/IKImageView with drag and drop.md` | 未开始 |
| 1102 | Implementing optional methods of the IKImageBrowserItem Protocol | 1 | `qa/Implementing optional methods of the IKImageBrowserItem Protocol.md` | 未开始 |
| 1103 | Improving Image Drawing Performance on iOS | 1 | `qa/Improving Image Drawing Performance on iOS.md` | 未开始 |
| 1104 | Is ColorSync thread safe? | 1 | `qa/qa2001/Is ColorSync thread safe` | 未开始 |
| 1105 | Missing ColorSync Profiles | 1 | `qa/c/Missing ColorSync Profiles` | 未开始 |
| 1106 | Multithreaded usage of the QCRenderer | 1 | `qa/Multithreaded usage of the QCRenderer.md` | 未开始 |
| 1107 | NSOpenGLView redraw problems after a window is closed and re-opened. | 1 | `qa/NSOpenGLView redraw problems after a window is closed and re-opened.md` | 未开始 |
| 1108 | New PPD keywords available in Mac OS X version 10.3 | 1 | `qa/New PPD keywords available in Mac OS X version 10.3.md` | 未开始 |
| 1109 | OpenGL Driver Monitor Decoder Ring | 1 | `qa/qa2001/OpenGL Driver Monitor Decoder Ring` | 未开始 |
| 1110 | OpenGL ES View Snapshot | 1 | `qa/OpenGL ES View Snapshot.md` | 未开始 |
| 1111 | OpenGL ES multithreading and EAGLSharegroup | 1 | `qa/OpenGL ES multithreading and EAGLSharegroup.md` | 未开始 |
| 1112 | Printer Queue vs. Printer Name | 1 | `qa/Printer Queue vs. Printer Name.md` | 未开始 |
| 1113 | Quartz 2D Interpolation | 1 | `qa/qa2001/Quartz 2D Interpolation` | 未开始 |
| 1114 | Quartz 2D Thread Safety | 1 | `qa/Quartz 2D Thread Safety.md` | 未开始 |
| 1115 | Removing flickering in OpenGL ES applications | 1 | `qa/Removing flickering in OpenGL ES applications.md` | 未开始 |
| 1116 | Screen Capture in UIKit Applications | 1 | `qa/Screen Capture in UIKit Applications.md` | 未开始 |
| 1117 | Setting the ColorSync profile for a NSBitmapImageRep object | 1 | `qa/Setting the ColorSync profile for a NSBitmapImageRep object.md` | 未开始 |
| 1118 | Sharpening Full Scene Anti-Aliasing Details | 1 | `qa/qa2001/Sharpening Full Scene Anti-Aliasing Details` | 未开始 |
| 1119 | Shearing a Coordinate Space with NSAffineTransform | 1 | `qa/qa2001/Shearing a Coordinate Space with NSAffineTransform` | 未开始 |
| 1120 | Special Profile Sizes in ColorSync Manager | 1 | `qa/c/Special Profile Sizes in ColorSync Manager` | 未开始 |
| 1121 | Specifiying if the CPU or the GPU should be used for rendering. | 1 | `qa/Specifiying if the CPU or the GPU should be used for rendering.md` | 未开始 |
| 1122 | Specifying required OpenGL capabilities for the Mac App Store | 1 | `qa/Specifying required OpenGL capabilities for the Mac App Store` | 未开始 |
| 1123 | Successful Call to NCWNewColorWorld | 1 | `qa/c/Successful Call to NCWNewColorWorld` | 未开始 |
| 1124 | Supporting native screen scale in your graphics application | 1 | `qa/Supporting native screen scale in your graphics application.md` | 未开始 |
| 1125 | SyncCGContextOriginWithPort | 1 | `qa/qa2001/SyncCGContextOriginWithPort` | 未开始 |
| 1126 | Synchronizing OpenGL rendering updates to the vertical refresh of the display | 1 | `qa/Synchronizing OpenGL rendering updates to the vertical refresh of the display` | 未开始 |
| 1127 | Tab-based SpriteKit Apps and Scene Caching | 1 | `qa/Tab-based SpriteKit Apps and Scene Caching.md` | 未开始 |
| 1128 | Turning Off Core Graphics Clipping | 1 | `qa/Turning Off Core Graphics Clipping.md` | 未开始 |
| 1129 | Unexpected CG state changes | 1 | `qa/Unexpected CG state changes.md` | 未开始 |
| 1130 | Updating OpenGL Contexts | 1 | `qa/qa2001/Updating OpenGL Contexts` | 未开始 |
| 1131 | Using Clip Region and Buffer Rectangles with OpenGL Carbon | 1 | `qa/qa2001/Using Clip Region and Buffer Rectangles with OpenGL Carbon` | 未开始 |
| 1132 | Using Embedded EPS Profiles | 1 | `qa/c/Using Embedded EPS Profiles` | 未开始 |
| 1133 | Using GLUT and OpenGL on OS X | 1 | `qa/Using GLUT and OpenGL on OS X.md` | 未开始 |
| 1134 | Using Interface Builder's NSOpenGLView or Custom View objects for an OpenGL | 1 | `qa/Using Interface Builder's NSOpenGLView or Custom View objects for an OpenGL appl.md` | 未开始 |
| 1135 | Using PPD constraints with Paper Sizes | 1 | `qa/Using PPD constraints with Paper Sizes.md` | 未开始 |
| 1136 | Using UTIs to Identify Image Files | 1 | `qa/Using UTIs to Identify Image Files.md` | 未开始 |
| 1137 | Using cmPathBased profile locations on Mac OS X | 1 | `qa/qa2001/Using cmPathBased profile locations on Mac OS X` | 未开始 |
| 1138 | View Snapshots on iOS 7 | 1 | `qa/View Snapshots on iOS 7.md` | 未开始 |
| 1139 | What is the Timebase submenu available in the contextual menu of some patches | 1 | `qa/What is the Timebase submenu available in the contextual menu of some patches in` | 未开始 |
| 1140 | When does the RSS Feed patch in Quartz Composer refresh its contents? | 1 | `qa/When does the RSS Feed patch in Quartz Composer refresh its contents` | 未开始 |
| 1141 | Why are my Core Graphics calls drawing upside down? | 1 | `qa/qa2001/Why are my Core Graphics calls drawing upside down` | 未开始 |
| 1142 | Why are my shadows drawn upside down in iOS 3.2 and later? | 1 | `qa/Why are my shadows drawn upside down in iOS 3.2 and later.md` | 未开始 |
| 1143 | Why does my Quartz Composer composition render with a corrupted background | 1 | `qa/Why does my Quartz Composer composition render with a corrupted background in th` | 未开始 |
| 1144 | Why don't all of my PDE localizations show up in all applications? | 1 | `qa/qa2001/Why don't all of my PDE localizations show up in all applications` | 未开始 |
| 1145 | Why isn't my ColorSync CMM recognized on Mac OS X 10.5? | 1 | `qa/Why isn't my ColorSync CMM recognized on Mac OS X 10.5.md` | 未开始 |
| 1146 | glFlush() vs. glFinish() | 1 | `qa/glFlush() vs. glFinish().md` | 未开始 |

### 数据管理（62 份，62 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 1147 | 'Why does -stringByTrimmingCharactersInSet: give me an empty string result | 1 | `qa/qa2001/Why does -stringByTrimmingCharactersInSet- give me an empty string result when i` | 未开始 |
| 1148 | Accessing File Control Blocks | 1 | `qa/fl/Accessing File Control Blocks.md` | 未开始 |
| 1149 | Allocate and Disk Full Error | 1 | `qa/fl/Allocate and Disk Full Error.md` | 未开始 |
| 1150 | CFBundleIdentifier and user application access | 1 | `qa/CFBundleIdentifier and user application access.md` | 未开始 |
| 1151 | CFXML to CFPropertyListRef (and back!) | 1 | `qa/qa2001/CFXML to CFPropertyListRef (and back!)` | 未开始 |
| 1152 | CGContext parameter missing in my kEventControlDraw event | 1 | `qa/qa2001/CGContext parameter missing in my kEventControlDraw event` | 未开始 |
| 1153 | Checking the availability of iCloud Drive | 1 | `qa/Checking the availability of iCloud Drive.md` | 未开始 |
| 1154 | Cocoa Bindings in OS X Storyboards | 1 | `qa/Cocoa Bindings in OS X Storyboards` | 未开始 |
| 1155 | Configure document types for your iCloud container | 1 | `qa/Configure document types for your iCloud container.md` | 未开始 |
| 1156 | Connecting the Font Menu in Interface Builder 3 | 1 | `qa/Connecting the Font Menu in Interface Builder 3.md` | 未开始 |
| 1157 | Converting to Precomposed Unicode | 1 | `qa/Converting to Precomposed Unicode.md` | 未开始 |
| 1158 | Crash in ABAddPropertiesAndTypes | 1 | `qa/Crash in ABAddPropertiesAndTypes.md` | 未开始 |
| 1159 | Debugging issues with CloudKit subscriptions | 1 | `qa/Debugging issues with CloudKit subscriptions.md` | 未开始 |
| 1160 | Delivering touch events to a view outside the bounds of its parent view | 1 | `qa/Delivering touch events to a view outside the bounds of its parent view` | 未开始 |
| 1161 | Detecting the Caps Lock Key | 1 | `qa/Detecting the Caps Lock Key.md` | 未开始 |
| 1162 | Determining console user login status | 1 | `qa/Determining console user login status.md` | 未开始 |
| 1163 | Developing for VFS | 1 | `qa/Developing for VFS.md` | 未开始 |
| 1164 | Directories Appear as Volume Aliases | 1 | `qa/Directories Appear as Volume Aliases.md` | 未开始 |
| 1165 | Disabling and Enabling an NSTextView | 1 | `qa/Disabling and Enabling an NSTextView.md` | 未开始 |
| 1166 | Disconnected aliases on CD-ROM and Alias Manager | 1 | `qa/ops/Disconnected aliases on CD-ROM and Alias Manager` | 未开始 |
| 1167 | Drawing attributed strings that are both filled and stroked | 1 | `qa/Drawing attributed strings that are both filled and stroked` | 未开始 |
| 1168 | Embedding Hyperlinks in NSTextField and NSTextView | 1 | `qa/Embedding Hyperlinks in NSTextField and NSTextView` | 未开始 |
| 1169 | Ensure that property list keys UIPrerenderedIcon and UIRequiresPersistentWiFi | 1 | `qa/Ensure that property list keys UIPrerenderedIcon and UIRequiresPersistentWiFi ha` | 未开始 |
| 1170 | Expanding Tilde-based paths | 1 | `qa/Expanding Tilde-based paths.md` | 未开始 |
| 1171 | FSDeleteObject fails with fBsyErr, sometimes | 1 | `qa/FSDeleteObject fails with fBsyErr, sometimes.md` | 未开始 |
| 1172 | FSSetCatalogInfo versus UID and GID | 1 | `qa/qa2001/FSSetCatalogInfo versus UID and GID` | 未开始 |
| 1173 | File Manager Text Encoding Hints | 1 | `qa/qa2001/File Manager Text Encoding Hints` | 未开始 |
| 1174 | Finding your application's directory | 1 | `qa/fl/Finding your application's directory.md` | 未开始 |
| 1175 | How do I get my application to show up in the Open in... menu. | 1 | `qa/How do I get my application to show up in the Open in... menu` | 未开始 |
| 1176 | How do I use kMPCreateTaskSuspendedMask with MPCreateTask? | 1 | `qa/qa2001/How do I use kMPCreateTaskSuspendedMask with MPCreateTask` | 未开始 |
| 1177 | How do I work-around an issue where some lines in my Core Text output have | 1 | `qa/How do I work-around an issue where some lines in my Core Text output have extra.md` | 未开始 |
| 1178 | How to make NSTextField accept tab, return and enter keys. | 1 | `qa/How to make NSTextField accept tab, return and enter keys.md` | 未开始 |
| 1179 | Installing Production Provisioning Profiles | 1 | `qa/Installing Production Provisioning Profiles.md` | 未开始 |
| 1180 | Installing input methods on Mac OS X | 1 | `qa/qa2001/Installing input methods on Mac OS X` | 未开始 |
| 1181 | Integrating With The Connect to Server Dialog | 1 | `qa/Integrating With The Connect to Server Dialog.md` | 未开始 |
| 1182 | Losing the character code when using the control key | 1 | `qa/qa2005/Losing the character code when using the control key` | 未开始 |
| 1183 | Mach Absolute Time Units | 1 | `qa/Mach Absolute Time Units.md` | 未开始 |
| 1184 | NSDateFormatter and Internet Dates | 1 | `qa/NSDateFormatter and Internet Dates.md` | 未开始 |
| 1185 | NSOpenPanel - Choosing any file and ignoring packages | 1 | `qa/NSOpenPanel - Choosing any file and ignoring packages.md` | 未开始 |
| 1186 | New default journaling mode for Core Data SQLite stores in iOS 7 and OS X Mavericks | 1 | `qa/New default journaling mode for Core Data SQLite stores in iOS 7 and OS X Maveri.md` | 未开始 |
| 1187 | Notifying the Finder of changed or newly created files | 1 | `qa/qa2001/Notifying the Finder of changed or newly created files` | 未开始 |
| 1188 | Public UTIs supported by Mac OS X v10.3 | 1 | `qa/Public UTIs supported by Mac OS X v10.3.md` | 未开始 |
| 1189 | Registering and unregistering for sleep and wake notifications | 1 | `qa/Registering and unregistering for sleep and wake notifications.md` | 未开始 |
| 1190 | Sending an Email | 1 | `qa/Sending an Email.md` | 未开始 |
| 1191 | Setting default open Finder window | 1 | `qa/Setting default open Finder window.md` | 未开始 |
| 1192 | Sorting Like the Finder | 1 | `qa/Sorting Like the Finder.md` | 未开始 |
| 1193 | Storing Private Data | 1 | `qa/Storing Private Data.md` | 未开始 |
| 1194 | Storing file references in CFPreferences | 1 | `qa/Storing file references in CFPreferences.md` | 未开始 |
| 1195 | Testing for a Network Volume | 1 | `qa/Testing for a Network Volume.md` | 未开始 |
| 1196 | Text Encodings in VFS | 1 | `qa/Text Encodings in VFS.md` | 未开始 |
| 1197 | The "/.vol" directory and "volfs" | 1 | `qa/qa2001/The --.vol- directory and -volfs` | 未开始 |
| 1198 | Third party VFS can't unmount on Mac OS X 10.3 | 1 | `qa/qa2001/Third party VFS can't unmount on Mac OS X 10.3` | 未开始 |
| 1199 | Understanding Core Data iCloud Store Migration When Testing an iOS App Update | 1 | `qa/Understanding Core Data iCloud Store Migration When Testing an iOS App Update.md` | 未开始 |
| 1200 | Uniform Type Identifiers and Custom Document Type Resources | 1 | `qa/Uniform Type Identifiers and Custom Document Type Resources.md` | 未开始 |
| 1201 | Updating the metadata of iCloud containers for iCloud Drive | 1 | `qa/Updating the metadata of iCloud containers for iCloud Drive.md` | 未开始 |
| 1202 | Using External Accessory framework with Bluetooth devices. | 1 | `qa/Using External Accessory framework with Bluetooth devices.md` | 未开始 |
| 1203 | Volumes Not Showing Up On The Desktop | 1 | `qa/Volumes Not Showing Up On The Desktop.md` | 未开始 |
| 1204 | Weak Linking To Spotlight | 1 | `qa/Weak Linking To Spotlight.md` | 未开始 |
| 1205 | Why am I getting a bdNamErr when trying to use a file I just located? | 1 | `qa/Why am I getting a bdNamErr when trying to use a file I just located.md` | 未开始 |
| 1206 | Why aren't my tracking rects working? | 1 | `qa/Why aren't my tracking rects working.md` | 未开始 |
| 1207 | Why can't I save data to my application's bundle when running on the device? | 1 | `qa/Why can't I save data to my application's bundle when running on the device.md` | 未开始 |
| 1208 | Why doesn't the keyboard show when my text input view is tapped? | 1 | `qa/Why doesn't the keyboard show when my text input view is tapped.md` | 未开始 |

### Xcode（59 份，59 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 1209 | '"Error launching remote program: failed to get the task for process"' | 1 | `qa/-Error launching remote program- failed to get the task for process.md` | 未开始 |
| 1210 | '"Info.plist does not contain a CFBundleResourceSpecification" errors when | 1 | `qa/-Info.plist does not contain a CFBundleResourceSpecification- errors when upload` | 未开始 |
| 1211 | '"Xcode cannot find the software image to install this version"' | 1 | `qa/-Xcode cannot find the software image to install this version` | 未开始 |
| 1212 | '''dynamic shared library not made a weak library in output with MACOSX_DEPLOYMENT_TARGET...'' | 1 | `qa/qa2001/'dynamic shared library not made a weak library in output with MACOSXDEPLOYMENTT` | 未开始 |
| 1213 | 'WARNING: The Copy Bundle Resources build phase contains this target''s Info.plist | 1 | `qa/WARNING- The Copy Bundle Resources build phase contains this target's Info.plist` | 未开始 |
| 1214 | Automating Version and Build Numbers Using agvtool | 1 | `qa/Automating Version and Build Numbers Using agvtool` | 未开始 |
| 1215 | Backwards Compatibility With libxml2 and iPhone SDK | 1 | `qa/Backwards Compatibility With libxml2 and iPhone SDK` | 未开始 |
| 1216 | Base SDK Missing | 1 | `qa/Base SDK Missing` | 未开始 |
| 1217 | Building Objective-C static libraries with categories | 1 | `qa/Building Objective-C static libraries with categories` | 未开始 |
| 1218 | Building a Position Independent Executable | 1 | `qa/Building a Position Independent Executable.md` | 未开始 |
| 1219 | Code signing fails with error 'resource fork, Finder information, or similar | 1 | `qa/Code signing fails with error 'resource fork, Finder information, or similar det.md` | 未开始 |
| 1220 | Configuring Xcode for Code Coverage | 1 | `qa/Configuring Xcode for Code Coverage` | 未开始 |
| 1221 | Creating Core Data Managed Object Subclasses with Xcode | 1 | `qa/Creating Core Data Managed Object Subclasses with Xcode` | 未开始 |
| 1222 | Debugging Process Startup | 1 | `qa/Debugging Process Startup.md` | 未开始 |
| 1223 | Debugging arbitrary applications with Xcode | 1 | `qa/qa2001/Debugging arbitrary applications with Xcode` | 未开始 |
| 1224 | Deprecated CALL_ON_[UN]LOAD pragmas | 1 | `qa/Deprecated CALLON-UN-LOAD pragmas.md` | 未开始 |
| 1225 | Detecting the Debugger | 1 | `qa/Detecting the Debugger.md` | 未开始 |
| 1226 | Embedding Content with Swift in Objective-C | 1 | `qa/Embedding Content with Swift in Objective-C` | 未开始 |
| 1227 | Getting NSWindow's toolbar actions to show up in Interface Builder | 1 | `qa/qa2001/Getting NSWindow's toolbar actions to show up in Interface Builder` | 未开始 |
| 1228 | How do I rename my application in Xcode? | 1 | `qa/How do I rename my application in Xcode` | 未开始 |
| 1229 | How do I use asserts while debugging? | 1 | `qa/How do I use asserts while debugging.md` | 未开始 |
| 1230 | How to add a folder to the contents of a package | 1 | `qa/How to add a folder to the contents of a package` | 未开始 |
| 1231 | How to reproduce bugs reported against App Store submissions | 1 | `qa/How to reproduce bugs reported against App Store submissions` | 未开始 |
| 1232 | How to reproduce bugs reported against Mac App Store submissions | 1 | `qa/How to reproduce bugs reported against Mac App Store submissions` | 未开始 |
| 1233 | Inserting an unmatched opening brace while having the "Automatically insert | 1 | `qa/Inserting an unmatched opening brace while having the -Automatically insert clos` | 未开始 |
| 1234 | Intel-Based Macs, Dashboard, Safari, and You | 1 | `qa/qa2005/Intel-Based Macs, Dashboard, Safari, and You` | 未开始 |
| 1235 | Interface element identification in Interface Builder | 1 | `qa/Interface element identification in Interface Builder` | 未开始 |
| 1236 | Keeping macro definitions out of the Xcode editor window's function pop-up | 1 | `qa/Keeping macro definitions out of the Xcode editor window's function pop-up.md` | 未开始 |
| 1237 | Making the app name on a device consistent with the name in iTunes Connect. | 1 | `qa/Making the app name on a device consistent with the name in iTunes Connect` | 未开始 |
| 1238 | Manual Code Signing for both iOS and tvOS | 1 | `qa/Manual Code Signing for both iOS and tvOS` | 未开始 |
| 1239 | Manually adding localhost to distcc sets | 1 | `qa/Manually adding localhost to distcc sets` | 未开始 |
| 1240 | Missing Results in Xcode Project Find Window | 1 | `qa/Missing Results in Xcode Project Find Window.md` | 未开始 |
| 1241 | Operation could not be completed. No such file or directory | 1 | `qa/Operation could not be completed. No such file or directory` | 未开始 |
| 1242 | Project Builder 2.1 needs projects to be checked into CVS to enable CVS support | 1 | `qa/qa2001/Project Builder 2.1 needs projects to be checked into CVS to enable CVS support` | 未开始 |
| 1243 | Remote or Two-Machine Debugging Applications with GDB | 1 | `qa/qa2001/Remote or Two-Machine Debugging Applications with GDB` | 未开始 |
| 1244 | Resolving | 1 | `qa/Resolving (2010).md` | 未开始 |
| 1245 | Resolving | 1 | `qa/Resolving` | 未开始 |
| 1246 | Resolving App Rejections for GCC and LLVM Instrumentation | 1 | `qa/Resolving App Rejections for GCC and LLVM Instrumentation.md` | 未开始 |
| 1247 | Resolving the "No identities are available for signing" Error | 1 | `qa/Resolving the -No identities are available for signing- Error.md` | 未开始 |
| 1248 | Statically linked binaries on Mac OS X | 1 | `qa/Statically linked binaries on Mac OS X.md` | 未开始 |
| 1249 | Stub Library FAQ | 1 | `qa/plat/Stub Library FAQ` | 未开始 |
| 1250 | Swift app crashes when trying to reference Swift library libswiftCore.dylib. | 1 | `qa/Swift app crashes when trying to reference Swift library libswiftCore.dylib.md` | 未开始 |
| 1251 | Symbol to Library in GDB | 1 | `qa/Symbol to Library in GDB.md` | 未开始 |
| 1252 | Unembedding views from stack views | 1 | `qa/Unembedding views from stack views` | 未开始 |
| 1253 | Updating the Display Name of Your App | 1 | `qa/Updating the Display Name of Your App` | 未开始 |
| 1254 | Using Breakpoint Actions for Logging | 1 | `qa/Using Breakpoint Actions for Logging` | 未开始 |
| 1255 | Using Pascal strings in Project Builder | 1 | `qa/qa2001/Using Pascal strings in Project Builder` | 未开始 |
| 1256 | Using static versions of existing dynamic libraries | 1 | `qa/Using static versions of existing dynamic libraries` | 未开始 |
| 1257 | Validating Your Version of Xcode | 1 | `qa/Validating Your Version of Xcode.md` | 未开始 |
| 1258 | Viewing the interface of your Swift code | 1 | `qa/Viewing the interface of your Swift code` | 未开始 |
| 1259 | What are the predefined macros for GCC? | 1 | `qa/What are the predefined macros for GCC.md` | 未开始 |
| 1260 | What version of Xcode and SDK should I be using when building for the App Store? | 1 | `qa/What version of Xcode and SDK should I be using when building for the App Store.md` | 未开始 |
| 1261 | When to upgrade your iPhone OS SDK | 1 | `qa/When to upgrade your iPhone OS SDK` | 未开始 |
| 1262 | Why am I getting a 'Failed to start remote debugserver for <name>.app on <device>' | 1 | `qa/Why am I getting a 'Failed to start remote debugserver for .app on ' error.md` | 未开始 |
| 1263 | Why does my app launch to a black screen on iPad? | 1 | `qa/Why does my app launch to a black screen on iPad.md` | 未开始 |
| 1264 | Why is libstdc++.a missing in my Xcode project on Mac OS X v10.4 (Tiger)? | 1 | `qa/Why is libstdc++.a missing in my Xcode project on Mac OS X v10.4 (Tiger).md` | 未开始 |
| 1265 | Xcode Organizer says "Could not support development" | 1 | `qa/Xcode Organizer says -Could not support development` | 未开始 |
| 1266 | Xcode debugger does not display the value of my variables. | 1 | `qa/Xcode debugger does not display the value of my variables` | 未开始 |
| 1267 | Your (Personal Team) cannot be used to Code Sign your App for submission to | 1 | `qa/Your (Personal Team) cannot be used to Code Sign your App for submission to the.md` | 未开始 |

### 网络与互联网（43 份，43 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 1268 | Accessing HTTPS Proxy Settings | 1 | `qa/qa2001/Accessing HTTPS Proxy Settings` | 未开始 |
| 1269 | Advertising a Bonjour service on a specific set of networking interfaces. | 1 | `qa/Advertising a Bonjour service on a specific set of networking interfaces.md` | 未开始 |
| 1270 | Bonjour TXT record rate limiting in Panther | 1 | `qa/Bonjour TXT record rate limiting in Panther.md` | 未开始 |
| 1271 | Bonjour and wake from sleep | 1 | `qa/Bonjour and wake from sleep.md` | 未开始 |
| 1272 | Bonjour enforces the TXT record format in Panther | 1 | `qa/Bonjour enforces the TXT record format in Panther.md` | 未开始 |
| 1273 | Bonjour enforces the service type format in Panther | 1 | `qa/Bonjour enforces the service type format in Panther.md` | 未开始 |
| 1274 | Bonjour service types used in Mac OS X | 1 | `qa/Bonjour service types used in Mac OS X.md` | 未开始 |
| 1275 | Clearing mDNSResponder's cached records | 1 | `qa/Clearing mDNSResponder's cached records.md` | 未开始 |
| 1276 | Common QA for Bonjour | 1 | `qa/Common QA for Bonjour.md` | 未开始 |
| 1277 | Debugging a WebKit Plug-in in Xcode | 1 | `qa/Debugging a WebKit Plug-in in Xcode` | 未开始 |
| 1278 | Discovering all advertised Bonjour service types | 1 | `qa/Discovering all advertised Bonjour service types.md` | 未开始 |
| 1279 | Don't forget to cancel your Bonjour resolve | 1 | `qa/Don't forget to cancel your Bonjour resolve.md` | 未开始 |
| 1280 | Downloading through a proxy server in Mac OS X | 1 | `qa/qa2001/Downloading through a proxy server in Mac OS X` | 未开始 |
| 1281 | Duplicate Bonjour services while browsing | 1 | `qa/Duplicate Bonjour services while browsing.md` | 未开始 |
| 1282 | Getting the User and Computer Name | 1 | `qa/qa2001/Getting the User and Computer Name` | 未开始 |
| 1283 | HTTPS and Test Servers | 1 | `qa/HTTPS and Test Servers.md` | 未开始 |
| 1284 | Handing Off TCP Connections to a Different Port | 1 | `qa/nw/Handing Off TCP Connections to a Different Port` | 未开始 |
| 1285 | Handling “The network connection was lost” Errors | 1 | `qa/Handling “The network connection was lost” Errors.md` | 未开始 |
| 1286 | How do I prevent my WebKit-enabled application from writing to the shared icon | 1 | `qa/How do I prevent my WebKit-enabled application from writing to the shared icon d.md` | 未开始 |
| 1287 | How to play a sequence of movies in a Web page | 1 | `qa/How to play a sequence of movies in a Web page.md` | 未开始 |
| 1288 | How to securely serve Key files for HTTP Live Streaming with HTTPS | 1 | `qa/How to securely serve Key files for HTTP Live Streaming with HTTPS.md` | 未开始 |
| 1289 | Incoming requests for /.well-known/apple-app-site-association file | 1 | `qa/Incoming requests for -.well-known-apple-app-site-association file.md` | 未开始 |
| 1290 | Internet Connect Speed | 1 | `qa/Internet Connect Speed.md` | 未开始 |
| 1291 | Making Web Inspector work with iOS 7 from Safari 6 | 1 | `qa/Making Web Inspector work with iOS 7 from Safari 6.md` | 未开始 |
| 1292 | Mixing link-local IP addresses and routable IP addresses | 1 | `qa/Mixing link-local IP addresses and routable IP addresses.md` | 未开始 |
| 1293 | NSNetService and Automatic Reference Counting (ARC) | 1 | `qa/NSNetService and Automatic Reference Counting (ARC).md` | 未开始 |
| 1294 | Network Service Type Settings | 1 | `qa/Network Service Type Settings.md` | 未开始 |
| 1295 | Numerous Small Packet Exchanges Result In Poor TCP Performance | 1 | `qa/Numerous Small Packet Exchanges Result In Poor TCP Performance.md` | 未开始 |
| 1296 | PPPoE Server for Testing | 1 | `qa/PPPoE Server for Testing.md` | 未开始 |
| 1297 | Problems getting Bonjour TXT record information | 1 | `qa/Problems getting Bonjour TXT record information.md` | 未开始 |
| 1298 | Programmatically Performing an Open Directory Search | 1 | `qa/Programmatically Performing an Open Directory Search.md` | 未开始 |
| 1299 | Registering a Bonjour service multiple times | 1 | `qa/Registering a Bonjour service multiple times.md` | 未开始 |
| 1300 | Resolves may return an IPv6 address in Panther | 1 | `qa/Resolves may return an IPv6 address in Panther.md` | 未开始 |
| 1301 | Resumable Downloads | 1 | `qa/Resumable Downloads.md` | 未开始 |
| 1302 | TCP/IP Option Sizes | 1 | `qa/nw/TCP-IP Option Sizes` | 未开始 |
| 1303 | TLS Session Cache | 1 | `qa/TLS Session Cache.md` | 未开始 |
| 1304 | The state of mDNSResponder | 1 | `qa/The state of mDNSResponder.md` | 未开始 |
| 1305 | Troubleshooting Universal Links | 1 | `qa/Troubleshooting Universal Links.md` | 未开始 |
| 1306 | Updating the TXT record of a Bonjour service | 1 | `qa/qa2001/Updating the TXT record of a Bonjour service` | 未开始 |
| 1307 | Use empty string for Bonjour domains | 1 | `qa/Use empty string for Bonjour domains.md` | 未开始 |
| 1308 | Use the Computer Name when registering your Bonjour service | 1 | `qa/Use the Computer Name when registering your Bonjour service.md` | 未开始 |
| 1309 | Using NSStreams For A TCP Connection Without NSHost | 1 | `qa/Using NSStreams For A TCP Connection Without NSHost.md` | 未开始 |
| 1310 | purgeIdleCellConnections Log Message | 1 | `qa/purgeIdleCellConnections Log Message.md` | 未开始 |

### 用户体验（40 份，40 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 1311 | Adding and removing a submenu from a menu in Cocoa | 1 | `qa/Adding and removing a submenu from a menu in Cocoa` | 未开始 |
| 1312 | App Icons on iPhone, iPad and Apple Watch | 1 | `qa/App Icons on iPhone, iPad and Apple Watch` | 未开始 |
| 1313 | Automatic orientation support for iPhone and iPad apps | 1 | `qa/Automatic orientation support for iPhone and iPad apps.md` | 未开始 |
| 1314 | Background-only apps with NSStatusItems become active in 10.1 on NSStatusItem | 1 | `qa/qa2001/Background-only apps with NSStatusItems become active in 10.1 on NSStatusItem cl` | 未开始 |
| 1315 | Building Screen Savers for Snow Leopard | 1 | `qa/Building Screen Savers for Snow Leopard` | 未开始 |
| 1316 | Configuring the Recent Searches menu for NSSearchField | 1 | `qa/Configuring the Recent Searches menu for NSSearchField.md` | 未开始 |
| 1317 | Debugging NSTableView's "Action Invocation" binding | 1 | `qa/Debugging NSTableView's -Action Invocation- binding.md` | 未开始 |
| 1318 | Detecting phone numbers and links in an iPhone application | 1 | `qa/Detecting phone numbers and links in an iPhone application` | 未开始 |
| 1319 | Detecting the start and end edit sessions of a cell in NSTableView. | 1 | `qa/Detecting the start and end edit sessions of a cell in NSTableView.md` | 未开始 |
| 1320 | Displaying Help | 1 | `qa/qa2001/Displaying Help` | 未开始 |
| 1321 | Enabling the application menu's "Preferences" menu item on Mac OS X | 1 | `qa/Enabling the application menu's -Preferences- menu item on Mac OS X` | 未开始 |
| 1322 | Finding an NSView's current magnification. | 1 | `qa/Finding an NSView's current magnification.md` | 未开始 |
| 1323 | Focus Rings and Layer-Backed Views | 1 | `qa/Focus Rings and Layer-Backed Views.md` | 未开始 |
| 1324 | Handling Popover Controllers During Orientation Changes | 1 | `qa/Handling Popover Controllers During Orientation Changes.md` | 未开始 |
| 1325 | Hiding iAd banners when ads are not available | 1 | `qa/Hiding iAd banners when ads are not available.md` | 未开始 |
| 1326 | How can I determine the order of the languages set by the user in the Language | 1 | `qa/How can I determine the order of the languages set by the user in the Language t.md` | 未开始 |
| 1327 | How do I add annotations to my IMKit Input Method | 1 | `qa/How do I add annotations to my IMKit Input Method` | 未开始 |
| 1328 | How do I localize the Services menu string for my service | 1 | `qa/How do I localize the Services menu string for my service` | 未开始 |
| 1329 | How do I programmatically quit my iOS application? | 1 | `qa/How do I programmatically quit my iOS application.md` | 未开始 |
| 1330 | How iOS Determines the Language For Your App | 1 | `qa/How iOS Determines the Language For Your App.md` | 未开始 |
| 1331 | How many calls can I make to the Speech Framework API? | 1 | `qa/How many calls can I make to the Speech Framework API.md` | 未开始 |
| 1332 | How to create a Cocoa Disclosure Button Control | 1 | `qa/How to create a Cocoa Disclosure Button Control.md` | 未开始 |
| 1333 | How to get custom views to show up in NSToolbarItems | 1 | `qa/How to get custom views to show up in NSToolbarItems.md` | 未开始 |
| 1334 | How to opt out of video mirroring | 1 | `qa/How to opt out of video mirroring.md` | 未开始 |
| 1335 | How to remove the "Open Recent" menu item in a Document-based Cocoa application | 1 | `qa/qa2001/How to remove the -Open Recent- menu item in a Document-based Cocoa application` | 未开始 |
| 1336 | Including a custom NSWindow in a nib file | 1 | `qa/Including a custom NSWindow in a nib file` | 未开始 |
| 1337 | Launch Image Doesn't Show Up for iPhone Apps | 1 | `qa/Launch Image Doesn't Show Up for iPhone Apps.md` | 未开始 |
| 1338 | Matching a Bar Tint Color To Your Corporate or Brand Color | 1 | `qa/Matching a Bar Tint Color To Your Corporate or Brand Color.md` | 未开始 |
| 1339 | NSProgressIndicator animation and redraw | 1 | `qa/NSProgressIndicator animation and redraw.md` | 未开始 |
| 1340 | Obtaining the localized application name in Cocoa | 1 | `qa/Obtaining the localized application name in Cocoa.md` | 未开始 |
| 1341 | Preventing a View From Rotating | 1 | `qa/Preventing a View From Rotating.md` | 未开始 |
| 1342 | Preventing column reordering in NSTableView | 1 | `qa/Preventing column reordering in NSTableView.md` | 未开始 |
| 1343 | Preventing the Status Bar from Covering Your Views | 1 | `qa/Preventing the Status Bar from Covering Your Views` | 未开始 |
| 1344 | Restoring the screen brightness when an app leaves the active state | 1 | `qa/Restoring the screen brightness when an app leaves the active state.md` | 未开始 |
| 1345 | Supporting In-App Purchase in iMessage apps. | 1 | `qa/Supporting In-App Purchase in iMessage apps` | 未开始 |
| 1346 | Third-Party Input Method Management Changes in OS X Mavericks | 1 | `qa/Third-Party Input Method Management Changes in OS X Mavericks.md` | 未开始 |
| 1347 | Views incorrectly draw underneath the status bar | 1 | `qa/Views incorrectly draw underneath the status bar` | 未开始 |
| 1348 | Where should I install my help book, and how does Help Viewer locate it? | 1 | `qa/qa2001/Where should I install my help book, and how does Help Viewer locate it` | 未开始 |
| 1349 | Why does my app launch to a black screen on iOS 4? | 1 | `qa/Why does my app launch to a black screen on iOS 4` | 未开始 |
| 1350 | Why won't my UIViewController rotate with the device? | 1 | `qa/Why won't my UIViewController rotate with the device.md` | 未开始 |

### 驱动、内核与硬件（32 份，32 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 1351 | Allocating and sharing memory with user space from an IOKit driver | 1 | `qa/Allocating and sharing memory with user space from an IOKit driver.md` | 未开始 |
| 1352 | Available FireWire Isochronous Bandwidth | 1 | `qa/Available FireWire Isochronous Bandwidth.md` | 未开始 |
| 1353 | Avoiding Kernel Event Conflicts | 1 | `qa/Avoiding Kernel Event Conflicts.md` | 未开始 |
| 1354 | Bluetooth Radio Power Class for Apple Systems | 1 | `qa/qa2001/Bluetooth Radio Power Class for Apple Systems` | 未开始 |
| 1355 | Common QA and Roadmap for USB Software Development on Mac OS X | 1 | `qa/Common QA and Roadmap for USB Software Development on Mac OS X` | 未开始 |
| 1356 | Descriptor Passing Problems | 1 | `qa/Descriptor Passing Problems.md` | 未开始 |
| 1357 | Energy Star PCI Device | 1 | `qa/qa2001/Energy Star PCI Device` | 未开始 |
| 1358 | ExpressCard Prevents System Sleep | 1 | `qa/ExpressCard Prevents System Sleep.md` | 未开始 |
| 1359 | HID Manager Event Data Underruns | 1 | `qa/qa2001/HID Manager Event Data Underruns` | 未开始 |
| 1360 | How can I tell if a PCI device has on board I/O space? | 1 | `qa/qa2001/How can I tell if a PCI device has on board I-O space` | 未开始 |
| 1361 | How many PCI header types exist today? | 1 | `qa/hw/How many PCI header types exist today` | 未开始 |
| 1362 | IODeviceTree and the I/O Registry | 1 | `qa/IODeviceTree and the I-O Registry.md` | 未开始 |
| 1363 | IOKit Framework Headers | 1 | `qa/qa2001/IOKit Framework Headers` | 未开始 |
| 1364 | IOLog and Interrupt Context | 1 | `qa/IOLog and Interrupt Context.md` | 未开始 |
| 1365 | Installing an IOKit KEXT Without Rebooting | 1 | `qa/Installing an IOKit KEXT Without Rebooting.md` | 未开始 |
| 1366 | Issues with boot time KEXT loading | 1 | `qa/Issues with boot time KEXT loading.md` | 未开始 |
| 1367 | Kernel extensions built with Xcode 3.x won't load on PowerPC-based Macs running | 1 | `qa/Kernel extensions built with Xcode 3.x won't load on PowerPC-based Macs running` | 未开始 |
| 1368 | Kernel's MAC framework | 1 | `qa/Kernel's MAC framework.md` | 未开始 |
| 1369 | Making sense of IOKit error codes | 1 | `qa/Making sense of IOKit error codes.md` | 未开始 |
| 1370 | PCI SIG | 1 | `qa/hw/PCI SIG` | 未开始 |
| 1371 | PCI address/data stepping | 1 | `qa/hw/PCI address-data stepping` | 未开始 |
| 1372 | PCI class codes | 1 | `qa/hw/PCI class codes` | 未开始 |
| 1373 | Retain Counts of io_object_t Objects in IOKit.framework | 1 | `qa/Retain Counts of ioobjectt Objects in IOKit.framework.md` | 未开始 |
| 1374 | Sending SCSI or ATA commands to storage devices | 1 | `qa/Sending SCSI or ATA commands to storage devices.md` | 未开始 |
| 1375 | Supported KPIs | 1 | `qa/Supported KPIs.md` | 未开始 |
| 1376 | Suppressing the Network Configuration Dialog | 1 | `qa/Suppressing the Network Configuration Dialog` | 未开始 |
| 1377 | The "green" PCI bus | 1 | `qa/hw/The -green- PCI bus` | 未开始 |
| 1378 | The dreaded "incompatible flag -framework" error | 1 | `qa/qa2001/The dreaded -incompatible flag -framework- error` | 未开始 |
| 1379 | Tips on USB driver matching for Mac OS X | 1 | `qa/Tips on USB driver matching for Mac OS X.md` | 未开始 |
| 1380 | Using the correct Bluetooth LE Advertising and Connection Parameters for a | 1 | `qa/Using the correct Bluetooth LE Advertising and Connection Parameters for a stabl.md` | 未开始 |
| 1381 | What is a CardBus host bus adapter HBA? | 1 | `qa/hw/What is a CardBus host bus adapter HBA` | 未开始 |
| 1382 | What is unsolicited status? | 1 | `qa/fw/What is unsolicited status` | 未开始 |

### 通用（28 份，28 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 1383 | Application unavailable for download on older devices | 1 | `qa/Application unavailable for download on older devices` | 未开始 |
| 1384 | Common mistakes with delegation in Cocoa | 1 | `qa/Common mistakes with delegation in Cocoa.md` | 未开始 |
| 1385 | Creating easy-to-read short links to the App Store for your apps and company | 1 | `qa/Creating easy-to-read short links to the App Store for your apps and company.md` | 未开始 |
| 1386 | Determining if an application uses Objective-C Garbage Collection | 1 | `qa/Determining if an application uses Objective-C Garbage Collection.md` | 未开始 |
| 1387 | Empty Memory Objects | 1 | `qa/Empty Memory Objects.md` | 未开始 |
| 1388 | Environment Variables | 1 | `qa/qa2001/Environment Variables` | 未开始 |
| 1389 | Generating a Non-Maskable Interrupt (NMI) | 1 | `qa/Generating a Non-Maskable Interrupt (NMI).md` | 未开始 |
| 1390 | Getting List of All Processes on Mac OS X | 1 | `qa/qa2001/Getting List of All Processes on Mac OS X` | 未开始 |
| 1391 | How can I identify the runtime environment, Carbon or Cocoa, of the current | 1 | `qa/How can I identify the runtime environment, Carbon or Cocoa, of the current appl.md` | 未开始 |
| 1392 | In-App Purchase Product Identifiers | 1 | `qa/In-App Purchase Product Identifiers` | 未开始 |
| 1393 | Is dlopen available on all versions of Mac OS X? | 1 | `qa/Is dlopen available on all versions of Mac OS X.md` | 未开始 |
| 1394 | Launch Behavior Changes for Image Capture Architecture (ICA) Device Modules | 1 | `qa/Launch Behavior Changes for Image Capture Architecture (ICA) Device Modules on m.md` | 未开始 |
| 1395 | Launching the App Store from an iOS application | 1 | `qa/Launching the App Store from an iOS application.md` | 未开始 |
| 1396 | Preventing Sensitive Information From Appearing In The Task Switcher | 1 | `qa/Preventing Sensitive Information From Appearing In The Task Switcher.md` | 未开始 |
| 1397 | Preventing sleep | 1 | `qa/Preventing sleep.md` | 未开始 |
| 1398 | Programmatically causing restart, shutdown and/or logout | 1 | `qa/Programmatically causing restart, shutdown and-or logout.md` | 未开始 |
| 1399 | Resetting Privacy Settings in iOS and macOS | 1 | `qa/Resetting Privacy Settings in iOS and macOS` | 未开始 |
| 1400 | Setting environment variables for user processes | 1 | `qa/Setting environment variables for user processes` | 未开始 |
| 1401 | Setting up Xcode to automatically manage your provisioning profiles | 1 | `qa/Setting up Xcode to automatically manage your provisioning profiles.md` | 未开始 |
| 1402 | The package does not contain an Info.plist | 1 | `qa/The package does not contain an Info.plist` | 未开始 |
| 1403 | Understanding the UIRequiredDeviceCapabilities key | 1 | `qa/Understanding the UIRequiredDeviceCapabilities key.md` | 未开始 |
| 1404 | Updating Your Apps To Support 64-bit in iOS 11 | 1 | `qa/Updating Your Apps To Support 64-bit in iOS 11.md` | 未开始 |
| 1405 | What is the correct drawing model and the correct event model for my NPAPI | 1 | `qa/What is the correct drawing model and the correct event model for my NPAPI plug.md` | 未开始 |
| 1406 | Where are my local calendars? | 1 | `qa/Where are my local calendars` | 未开始 |
| 1407 | Why am I getting odd, unexpected results with various viewport tag settings | 1 | `qa/Why am I getting odd, unexpected results with various viewport tag settings.md` | 未开始 |
| 1408 | Why does iTunes tell me my Ad Hoc-signed application "is not a valid application"? | 1 | `qa/Why does iTunes tell me my Ad Hoc-signed application -is not a valid application` | 未开始 |
| 1409 | Why doesn't my device load a file that loads fine in the Simulator? | 1 | `qa/Why doesn't my device load a file that loads fine in the Simulator.md` | 未开始 |
| 1410 | Why is my code acting differently when I debug with Zombies? | 1 | `qa/Why is my code acting differently when I debug with Zombies.md` | 未开始 |

### 跨平台（28 份，28 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 1411 | Calling InitializeQTML from DLL Main | 1 | `qa/qtw/Calling InitializeQTML from DLL Main` | 未开始 |
| 1412 | Checking For Presence of QuickTime 3 for Windows | 1 | `qa/qtw/Checking For Presence of QuickTime 3 for Windows` | 未开始 |
| 1413 | CreatePortAssociation And  WM_QUERYNEWPALETTE Message | 1 | `qa/qtw/CreatePortAssociation And WMQUERYNEWPALETTE Message` | 未开始 |
| 1414 | Customizing Component Border Colors | 1 | `qa/qa2001/Customizing Component Border Colors` | 未开始 |
| 1415 | Developer Tools JBoss and Tomcat Do Not Start After Installing Java 1.4.2 Update | 1 | `qa/qa2001/Developer Tools JBoss and Tomcat Do Not Start After Installing Java 1.4.2 Update` | 未开始 |
| 1416 | Enabling X11 Forwarding | 1 | `qa/Enabling X11 Forwarding.md` | 未开始 |
| 1417 | Endian Concerns When Playing 'snd ' Resources | 1 | `qa/qtw/Endian Concerns When Playing 'snd ' Resources` | 未开始 |
| 1418 | Illustrating document window changes in Swing | 1 | `qa/qa2001/Illustrating document window changes in Swing` | 未开始 |
| 1419 | Important Java Directories on Mac OS X | 1 | `qa/Important Java Directories on Mac OS X.md` | 未开始 |
| 1420 | Java on Intel-based Macs | 1 | `qa/Java on Intel-based Macs` | 未开始 |
| 1421 | MSVC++ link error LNK4098 When Building QuickTime 3 for Windows Apps | 1 | `qa/qtw/MSVC++ link error LNK4098 When Building QuickTime 3 for Windows Apps` | 未开始 |
| 1422 | Mixing AWT/Swing and Cocoa-Java | 1 | `qa/Mixing AWT-Swing and Cocoa-Java.md` | 未开始 |
| 1423 | QTML, c2pstr and Pascal strings | 1 | `qa/qa2001/QTML, c2pstr and Pascal strings` | 未开始 |
| 1424 | QuickTime DirectDraw Surfaces | 1 | `qa/qtw/QuickTime DirectDraw Surfaces` | 未开始 |
| 1425 | QuickTime Preview Behavior | 1 | `qa/qtmcc/QuickTime Preview Behavior.md` | 未开始 |
| 1426 | QuickTime Sound | 1 | `qa/qtmrf/QuickTime Sound.md` | 未开始 |
| 1427 | Rendering Multi-line text in JTree nodes | 1 | `qa/qa2001/Rendering Multi-line text in JTree nodes` | 未开始 |
| 1428 | Right- and Control-Drags on Mac OS X | 1 | `qa/Right- and Control-Drags on Mac OS X.md` | 未开始 |
| 1429 | Server Processes and the Dock | 1 | `qa/qa2001/Server Processes and the Dock` | 未开始 |
| 1430 | Sharing Browser Cookies With Java Applets | 1 | `qa/qa2001/Sharing Browser Cookies With Java Applets` | 未开始 |
| 1431 | Unsolicited About Boxes | 1 | `qa/Unsolicited About Boxes.md` | 未开始 |
| 1432 | UnsupportedClassVersionError With J2SE 5.0 Release 4 | 1 | `qa/UnsupportedClassVersionError With J2SE 5.0 Release 4` | 未开始 |
| 1433 | Using Mac Toolbox routines Under Windows 98/95/NT | 1 | `qa/qtw/Using Mac Toolbox routines Under Windows 98-95-NT` | 未开始 |
| 1434 | Using Mac-style Resources | 1 | `qa/qtw/Using Mac-style Resources` | 未开始 |
| 1435 | Using Windows GDI for all drawing | 1 | `qa/qtw/Using Windows GDI for all drawing` | 未开始 |
| 1436 | Where are the LiveConnect classes on Mac OS X? | 1 | `qa/Where are the LiveConnect classes on Mac OS X.md` | 未开始 |
| 1437 | Why is my Ruby on Rails application with FastCGI generating "'load error /etc/irbrc" | 1 | `qa/Why is my Ruby on Rails application with FastCGI generating -'load error -etc-ir.md` | 未开始 |
| 1438 | X11 FAQ | 1 | `qa/qa2001/X11 FAQ` | 未开始 |

### 语言与工具（25 份，25 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 1439 | 'iPhone/iPod Touch: application executable is missing a required architecture. | 1 | `qa/iPhone-iPod Touch- application executable is missing a required architecture. At` | 未开始 |
| 1440 | Checking Distribution Entitlements | 1 | `qa/Checking Distribution Entitlements` | 未开始 |
| 1441 | Debugging Graphics with QuartzDebug | 1 | `qa/Debugging Graphics with QuartzDebug` | 未开始 |
| 1442 | Finding and Fixing Category Method Name Clashes | 1 | `qa/Finding and Fixing Category Method Name Clashes` | 未开始 |
| 1443 | Fixing the "Audio Unit with Cocoa View" Xcode 3.1.x Template on Mac OS X 10.5.x | 1 | `qa/Fixing the -Audio Unit with Cocoa View- Xcode 3.1.x Template on Mac OS X 10.5.x.md` | 未开始 |
| 1444 | Hang launching signed Applets from JavaScript | 1 | `qa/Hang launching signed Applets from JavaScript.md` | 未开始 |
| 1445 | How can a build engineer distribute an app on behalf of the team? | 1 | `qa/How can a build engineer distribute an app on behalf of the team.md` | 未开始 |
| 1446 | Improved logging in Objective-C | 1 | `qa/Improved logging in Objective-C.md` | 未开始 |
| 1447 | Loading Scripting Additions in Mac OS X | 1 | `qa/Loading Scripting Additions in Mac OS X.md` | 未开始 |
| 1448 | Missing Enterprise Distribution Certificate Private Keys | 1 | `qa/Missing Enterprise Distribution Certificate Private Keys.md` | 未开始 |
| 1449 | Resolving App ID Prefix Mismatching | 1 | `qa/Resolving App ID Prefix Mismatching.md` | 未开始 |
| 1450 | Resolving the Invalid Signature binary rejection | 1 | `qa/Resolving the Invalid Signature binary rejection` | 未开始 |
| 1451 | Resolving the Potential Loss of Keychain Access warning | 1 | `qa/Resolving the Potential Loss of Keychain Access warning.md` | 未开始 |
| 1452 | Resolving the Provisioning Profile Invalid Status | 1 | `qa/Resolving the Provisioning Profile Invalid Status.md` | 未开始 |
| 1453 | Testing Distribution Builds of Mac Apps | 1 | `qa/Testing Distribution Builds of Mac Apps.md` | 未开始 |
| 1454 | The beta-reports-active Entitlement | 1 | `qa/The beta-reports-active Entitlement.md` | 未开始 |
| 1455 | Using the QuickTime for Java libraries on OS X | 1 | `qa/qa2001/Using the QuickTime for Java libraries on OS X` | 未开始 |
| 1456 | Variable arguments in Objective-C methods | 1 | `qa/Variable arguments in Objective-C methods.md` | 未开始 |
| 1457 | Viewing iOS-Optimized PNGs | 1 | `qa/Viewing iOS-Optimized PNGs.md` | 未开始 |
| 1458 | What is the "main bundle" of a command-line foundation tool? | 1 | `qa/What is the -main bundle- of a command-line foundation tool.md` | 未开始 |
| 1459 | When should I use a wildcard App ID? | 1 | `qa/When should I use a wildcard App ID` | 未开始 |
| 1460 | Why am I getting device support errors when uploading my app? | 1 | `qa/Why am I getting device support errors when uploading my app.md` | 未开始 |
| 1461 | Why do I get an | 1 | `qa/Why do I get an` | 未开始 |
| 1462 | Why do I get an "Invalid application-identifier Entitlement" error? | 1 | `qa/Why do I get an -Invalid application-identifier Entitlement- error.md` | 未开始 |
| 1463 | icon dimensions (0x0) don't meet the size requirements. | 1 | `qa/icon dimensions (0x0) don't meet the size requirements.md` | 未开始 |

### 安全（12 份，12 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 1464 | AuthorizationCreateFromExternalForm 100022 Error Explained | 1 | `qa/AuthorizationCreateFromExternalForm 100022 Error Explained.md` | 未开始 |
| 1465 | Be careful when using AuthorizationCreate | 1 | `qa/Be careful when using AuthorizationCreate.md` | 未开始 |
| 1466 | Common app sandboxing issues | 1 | `qa/Common app sandboxing issues.md` | 未开始 |
| 1467 | Describing the kSecTrustResultUnspecified error. | 1 | `qa/Describing the kSecTrustResultUnspecified error.md` | 未开始 |
| 1468 | Mac OS X and root access | 1 | `qa/Mac OS X and root access.md` | 未开始 |
| 1469 | Making Certificates and Keys Available To Your App | 1 | `qa/Making Certificates and Keys Available To Your App.md` | 未开始 |
| 1470 | Programmatically Accessing and Manipulating Multiple Keychain Items | 1 | `qa/Programmatically Accessing and Manipulating Multiple Keychain Items.md` | 未开始 |
| 1471 | Resolving the Privacy-Sensitive Data App Rejection | 1 | `qa/Resolving the Privacy-Sensitive Data App Rejection.md` | 未开始 |
| 1472 | Security Credentials | 1 | `qa/Security Credentials.md` | 未开始 |
| 1473 | Security Framework Error Codes | 1 | `qa/Security Framework Error Codes.md` | 未开始 |
| 1474 | Stay away from custom Authorization dialogs | 1 | `qa/qa2001/Stay away from custom Authorization dialogs` | 未开始 |
| 1475 | What encryption, authentication, and proxy technologies does Safari support? | 1 | `qa/What encryption, authentication, and proxy technologies does Safari support.md` | 未开始 |

### 应用间通信（11 份，11 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 1476 | Adopting Scripting Targets for Composing Mail | 1 | `qa/Adopting Scripting Targets for Composing Mail.md` | 未开始 |
| 1477 | BOM characters in 'utxt' clipboard flavor | 1 | `qa/qa2001/BOM characters in 'utxt' clipboard flavor` | 未开始 |
| 1478 | Calling AppleScript from an Application | 1 | `qa/qa2001/Calling an AppleScript and providing parameters from an Application/qa1026.md` | 未开始 |
| 1479 | Calling an AppleScript and providing parameters from an Application | 1 | `qa/qa2001/Calling an AppleScript and providing parameters from an Application/qa1111.md` | 未开始 |
| 1480 | How to add other pasteboard types to an HFS Promise drag in Cocoa | 1 | `qa/qa2001/How to add other pasteboard types to an HFS Promise drag in Cocoa` | 未开始 |
| 1481 | How to set a custom drag image when doing an HFS Promise drag in Cocoa | 1 | `qa/qa2001/How to set a custom drag image when doing an HFS Promise drag in Cocoa` | 未开始 |
| 1482 | Opening Keyboard Settings from a Keyboard Extension | 1 | `qa/Opening Keyboard Settings from a Keyboard Extension` | 未开始 |
| 1483 | Re-enabling dragging from NSTableView to other applications | 1 | `qa/Re-enabling dragging from NSTableView to other applications.md` | 未开始 |
| 1484 | Retrieving Data from AEDesc Records - do not use the dataHandle field | 1 | `qa/qa2001/Retrieving Data from AEDesc Records - do not use the dataHandle field` | 未开始 |
| 1485 | Sandboxing and Automation in OS X | 1 | `qa/Sandboxing and Automation in OS X.md` | 未开始 |
| 1486 | Testing an Automator Action Xcode Project | 1 | `qa/Testing an Automator Action Xcode Project` | 未开始 |

### 性能（9 份，9 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 1487 | Application does not crash when launched from debugger but crashes when launched | 1 | `qa/Application does not crash when launched from debugger but crashes when launched.md` | 未开始 |
| 1488 | Customizing Process Stack Size | 1 | `qa/Customizing Process Stack Size.md` | 未开始 |
| 1489 | Disabling Processor Cores on a Multi-Core System | 1 | `qa/Disabling Processor Cores on a Multi-Core System` | 未开始 |
| 1490 | Finding EXC_BAD_ACCESS bugs in a Cocoa project | 1 | `qa/Finding EXCBADACCESS bugs in a Cocoa project.md` | 未开始 |
| 1491 | Power Management; Policy Maker vs. Power Controller | 1 | `qa/qa2001/Power Management; Policy Maker vs. Power Controller` | 未开始 |
| 1492 | Requirements for Quartz GL | 1 | `qa/Requirements for Quartz GL.md` | 未开始 |
| 1493 | Signals and Threads | 1 | `qa/qa2001/Signals and Threads` | 未开始 |
| 1494 | Sleep vs. Doze on Mac OS X | 1 | `qa/qa2001/Sleep vs. Doze on Mac OS X` | 未开始 |
| 1495 | Understanding Sample Perspective in the Sampler Instrument | 1 | `qa/Understanding Sample Perspective in the Sampler Instrument` | 未开始 |

### Apple 应用程序（4 份，4 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 1496 | Final Cut Pro X - Preferred Video Media Time Scales and Sample Durations | 1 | `qa/Final Cut Pro X - Preferred Video Media Time Scales and Sample Durations.md` | 未开始 |
| 1497 | Movie Export Component - How to ensure Final Cut Pro recognizes your exporter | 1 | `qa/Movie Export Component - How to ensure Final Cut Pro recognizes your exporter.md` | 未开始 |
| 1498 | Releasing the iTunes Windows COM from Managed Code | 1 | `qa/Releasing the iTunes Windows COM from Managed Code.md` | 未开始 |
| 1499 | Safari's "Mail [Contents/Link] of This page" to Mail Client events... | 1 | `qa/Safari's -Mail -Contents-Link- of This page- to Mail Client events.md` | 未开始 |

### 数学计算（2 份，2 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 1500 | How Do I Leverage Data in a Trained Network For Use With MPS CNN? | 1 | `qa/How Do I Leverage Data in a Trained Network For Use With MPS CNN.md` | 未开始 |
| 1501 | Using the Wide Routines in <FixMath.h> | 1 | `qa/tb/Using the Wide Routines in` | 未开始 |

### 系统管理（1 份，1 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 1502 | Does Safari support 128-bit encryption? | 1 | `qa/Does Safari support 128-bit encryption.md` | 未开始 |