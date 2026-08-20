# releasenotes 分类翻译计划

> 前置说明见 `/agent.md`（翻译规范、铁律：标题与正文必须同批次翻译）与 `releasenotes/memory.md`（模块进度概览）。

## Context

`releasenotes/` 是各版本 SDK/框架的发行说明，索引标题和正文均为纯英文，从未被任何一批 PR 覆盖过。

**与其他分类不同的提醒**：发行说明时效性强、多为列表式条目（API 变更、已知问题、废弃提示），内容价值随版本老化迅速下降；且部分文档针对的系统版本极旧（如 "iOS 2.2 Release Notes"），实际查阅需求接近于零。**不建议照搬 Cocoa/Windows Views 的"整类全译"模式**，本清单只是把范围列全，具体是否要全部翻译、还是只挑用户关心的少数版本/框架，需要人工评估后再决定，不要看到清单就直接批量开工。

## 范围口径

- 覆盖 `releasenotes/` 目录下全部 215 份文档、2328 页。
- 排除标准：无（未做筛选，如上所述需要人工评估优先级）。
- 表格按 `releasenotes/` 下的物理子目录分组（该目录本身就按技术分类组织成子文件夹，如 `Cocoa/`、`Carbon/`、`Data Management/`，与 documentation 分类的技术分类基本对应，直接复用这个物理分组，不再单独按 topic 归类）。

## 翻译流程

与 `/agent.md` 规定的规范一致。翻译时必须同一个 commit 里把该文档的 frontmatter title、正文、以及 `_indexes/` 里对应的链接显示文字一起改完。

## 执行建议

先评估优先级（哪些版本/框架的发行说明还有实际查阅价值），挑出一个子集单独立项，不建议直接按下表顺序从头翻到尾。

## 完整清单（215 份 / 2328 页，按物理子目录分组，组内页数从大到小排列）


### General（101 份，2147 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 1 | OS X v10.11 API Diffs | 203 | `releasenotes/General/OS X v10.11 API Diffs` | 未开始 |
| 2 | macOS 10.12 API Diffs | 188 | `releasenotes/General/macOS 10.12 API Diffs` | 未开始 |
| 3 | iOS 10.0 API Diffs | 169 | `releasenotes/General/iOS 10.0 API Diffs` | 未开始 |
| 4 | iOS 9.0 API Diffs | 160 | `releasenotes/General/iOS 9.0 API Diffs` | 未开始 |
| 5 | OS X v10.10.3 API Diffs | 150 | `releasenotes/General/OS X v10.10.3 API Diffs` | 未开始 |
| 6 | tvOS 10.0 API Diffs | 111 | `releasenotes/General/tvOS 10.0 API Diffs` | 未开始 |
| 7 | iOS 8.1 API Diffs | 95 | `releasenotes/General/iOS 8.1 API Diffs` | 未开始 |
| 8 | iOS 9.1 API Diffs | 90 | `releasenotes/General/iOS 9.1 API Diffs` | 未开始 |
| 9 | iOS 8.3 API Diffs | 88 | `releasenotes/General/iOS 8.3 API Diffs` | 未开始 |
| 10 | macOS 10.12.1 API Diffs | 84 | `releasenotes/General/macOS 10.12.1 API Diffs` | 未开始 |
| 11 | OS X v10.11.4 API Diffs | 80 | `releasenotes/General/OS X v10.11.4 API Diffs` | 未开始 |
| 12 | OS X v10.9 API Diffs | 76 | `releasenotes/General/OS X v10.9 API Diffs` | 未开始 |
| 13 | iOS 10.1 API Diffs | 68 | `releasenotes/General/iOS 10.1 API Diffs` | 未开始 |
| 14 | OS X v10.7 API Diffs | 67 | `releasenotes/General/OS X v10.7 API Diffs` | 未开始 |
| 15 | iOS 9.3 API Diffs | 66 | `releasenotes/General/iOS 9.3 API Diffs` | 未开始 |
| 16 | iOS 8.0 API Diffs | 64 | `releasenotes/General/iOS 8.0 API Diffs` | 未开始 |
| 17 | OS X v10.8 API Diffs | 63 | `releasenotes/General/OS X v10.8 API Diffs` | 未开始 |
| 18 | watchOS 3.0 API Diffs | 62 | `releasenotes/General/watchOS 3.0 API Diffs` | 未开始 |
| 19 | tvOS 9.2 API Diffs | 49 | `releasenotes/General/tvOS 9.2 API Diffs` | 未开始 |
| 20 | watchOS 2.2 API Diffs | 31 | `releasenotes/General/watchOS 2.2 API Diffs` | 未开始 |
| 21 | watchOS 3.1 API Diffs | 29 | `releasenotes/General/watchOS 3.1 API Diffs` | 未开始 |
| 22 | watchOS 2.1 API Diffs | 28 | `releasenotes/General/watchOS 2.1 API Diffs` | 未开始 |
| 23 | iOS 8.2 API Diffs | 24 | `releasenotes/General/iOS 8.2 API Diffs` | 未开始 |
| 24 | iOS 9.2 API Diffs | 24 | `releasenotes/General/iOS 9.2 API Diffs` | 未开始 |
| 25 | CloudKit JS v2.0 API Diffs | 2 | `releasenotes/General/CloudKit JS v2.0 API Diffs` | 未开始 |
| 26 | Carbon Core Deprecations | 1 | `releasenotes/General/Carbon Core Deprecations.md` | 未开始 |
| 27 | Safari Developer Library Release Notes | 1 | `releasenotes/General/Safari Developer Library Release Notes.md` | 未开始 |
| 28 | Submitting to the Mac App Store | 1 | `releasenotes/General/Submitting to the Mac App Store` | 未开始 |
| 29 | What's New In Core Data | 1 | `releasenotes/General/What's New In Core Data.md` | 未开始 |
| 30 | What's New in Safari | 1 | `releasenotes/General/What's New in Safari.md` | 未开始 |
| 31 | What's New in iOS | 1 | `releasenotes/General/What's New in iOS.md` | 未开始 |
| 32 | What's New in tvOS | 1 | `releasenotes/General/What's New in tvOS.md` | 未开始 |
| 33 | What's New in watchOS | 1 | `releasenotes/General/What's New in watchOS.md` | 未开始 |
| 34 | iAd JS Developer Library Release Notes | 1 | `releasenotes/General/iAd JS Developer Library Release Notes.md` | 未开始 |
| 35 | iOS 10.0 Release Notes | 1 | `releasenotes/General/iOS 10.0 Release Notes.md` | 未开始 |
| 36 | iOS 10.1 Release Notes | 1 | `releasenotes/General/iOS 10.1 Release Notes.md` | 未开始 |
| 37 | iOS 10.2 Release Notes | 1 | `releasenotes/General/iOS 10.2 Release Notes.md` | 未开始 |
| 38 | iOS 10.3 Release Notes | 1 | `releasenotes/General/iOS 10.3 Release Notes.md` | 未开始 |
| 39 | iOS 11 Release Notes | 1 | `releasenotes/General/iOS 11 Release Notes.md` | 未开始 |
| 40 | iOS 11.1 SDK Release Notes | 1 | `releasenotes/General/iOS 11.1 SDK Release Notes.md` | 未开始 |
| 41 | iOS 11.2 SDK Release Notes | 1 | `releasenotes/General/iOS 11.2 SDK Release Notes.md` | 未开始 |
| 42 | iOS 11.3 SDK Release Notes | 1 | `releasenotes/General/iOS 11.3 SDK Release Notes.md` | 未开始 |
| 43 | iOS 3.0 API Diffs | 1 | `releasenotes/General/iOS 3.0 API Diffs.md` | 未开始 |
| 44 | iOS 3.1 API Diffs | 1 | `releasenotes/General/iOS 3.1 API Diffs.md` | 未开始 |
| 45 | iOS 3.1 Release Notes | 1 | `releasenotes/General/iOS 3.1 Release Notes.md` | 未开始 |
| 46 | iOS 3.2 API Diffs | 1 | `releasenotes/General/iOS 3.2 API Diffs.md` | 未开始 |
| 47 | iOS 3.2 Release Notes | 1 | `releasenotes/General/iOS 3.2 Release Notes.md` | 未开始 |
| 48 | iOS 4.0 API Diffs | 1 | `releasenotes/General/iOS 4.0 API Diffs.md` | 未开始 |
| 49 | iOS 4.0 Release Notes | 1 | `releasenotes/General/iOS 4.0 Release Notes.md` | 未开始 |
| 50 | iOS 4.0.2 Release Notes | 1 | `releasenotes/General/iOS 4.0.2 Release Notes.md` | 未开始 |
| 51 | iOS 4.1 API Diffs | 1 | `releasenotes/General/iOS 4.1 API Diffs.md` | 未开始 |
| 52 | iOS 4.1 Release Notes | 1 | `releasenotes/General/iOS 4.1 Release Notes.md` | 未开始 |
| 53 | iOS 4.2 API Diffs | 1 | `releasenotes/General/iOS 4.2 API Diffs.md` | 未开始 |
| 54 | iOS 4.2 Release Notes | 1 | `releasenotes/General/iOS 4.2 Release Notes.md` | 未开始 |
| 55 | iOS 4.3 API Diffs | 1 | `releasenotes/General/iOS 4.3 API Diffs.md` | 未开始 |
| 56 | iOS 4.3 Release Notes | 1 | `releasenotes/General/iOS 4.3 Release Notes.md` | 未开始 |
| 57 | iOS 5.0 API Diffs | 1 | `releasenotes/General/iOS 5.0 API Diffs.md` | 未开始 |
| 58 | iOS 5.0 Release Notes | 1 | `releasenotes/General/iOS 5.0 Release Notes.md` | 未开始 |
| 59 | iOS 5.1 API Diffs | 1 | `releasenotes/General/iOS 5.1 API Diffs.md` | 未开始 |
| 60 | iOS 5.1 Release Notes | 1 | `releasenotes/General/iOS 5.1 Release Notes.md` | 未开始 |
| 61 | iOS 6.0 API Diffs | 1 | `releasenotes/General/iOS 6.0 API Diffs.md` | 未开始 |
| 62 | iOS 6.0 Release Notes | 1 | `releasenotes/General/iOS 6.0 Release Notes.md` | 未开始 |
| 63 | iOS 6.1 API Diffs | 1 | `releasenotes/General/iOS 6.1 API Diffs.md` | 未开始 |
| 64 | iOS 6.1 Release Notes | 1 | `releasenotes/General/iOS 6.1 Release Notes.md` | 未开始 |
| 65 | iOS 7.0 API Diffs | 1 | `releasenotes/General/iOS 7.0 API Diffs.md` | 未开始 |
| 66 | iOS 7.0 Release Notes | 1 | `releasenotes/General/iOS 7.0 Release Notes.md` | 未开始 |
| 67 | iOS 7.1 API Diffs | 1 | `releasenotes/General/iOS 7.1 API Diffs.md` | 未开始 |
| 68 | iOS 7.1 Release Notes | 1 | `releasenotes/General/iOS 7.1 Release Notes.md` | 未开始 |
| 69 | iOS 8 Release Notes | 1 | `releasenotes/General/iOS 8 Release Notes.md` | 未开始 |
| 70 | iOS 8.1.1 Release Notes | 1 | `releasenotes/General/iOS 8.1.1 Release Notes.md` | 未开始 |
| 71 | iOS 8.2 Release Notes | 1 | `releasenotes/General/iOS 8.2 Release Notes.md` | 未开始 |
| 72 | iOS 8.3 Release Notes | 1 | `releasenotes/General/iOS 8.3 Release Notes.md` | 未开始 |
| 73 | iOS 8.4 Release Notes | 1 | `releasenotes/General/iOS 8.4 Release Notes.md` | 未开始 |
| 74 | iOS 9 Release Notes | 1 | `releasenotes/General/iOS 9 Release Notes.md` | 未开始 |
| 75 | iOS 9.1 Release Notes | 1 | `releasenotes/General/iOS 9.1 Release Notes.md` | 未开始 |
| 76 | iOS 9.2 Release Notes | 1 | `releasenotes/General/iOS 9.2 Release Notes.md` | 未开始 |
| 77 | iOS 9.3 Release Notes | 1 | `releasenotes/General/iOS 9.3 Release Notes.md` | 未开始 |
| 78 | macOS 10.13 High Sierra Release Notes | 1 | `releasenotes/General/macOS 10.13 High Sierra Release Notes.md` | 未开始 |
| 79 | macOS 10.13.1 SDK Release Notes | 1 | `releasenotes/General/macOS 10.13.1 SDK Release Notes.md` | 未开始 |
| 80 | macOS 10.13.2 SDK Release Notes | 1 | `releasenotes/General/macOS 10.13.2 SDK Release Notes.md` | 未开始 |
| 81 | macOS 10.13.4 SDK Release Notes | 1 | `releasenotes/General/macOS 10.13.4 SDK Release Notes.md` | 未开始 |
| 82 | tvOS 11.1 SDK Release Notes | 1 | `releasenotes/General/tvOS 11.1 SDK Release Notes.md` | 未开始 |
| 83 | tvOS 11.2 SDK Release Notes | 1 | `releasenotes/General/tvOS 11.2 SDK Release Notes.md` | 未开始 |
| 84 | tvOS 11.3 SDK Release Notes | 1 | `releasenotes/General/tvOS 11.3 SDK Release Notes.md` | 未开始 |
| 85 | tvOS Release Notes | 1 | `releasenotes/General/tvOS Release Notes.md` | 未开始 |
| 86 | tvOS SDK Release Notes for tvOS 10.0 | 1 | `releasenotes/General/tvOS SDK Release Notes for tvOS 10.0.md` | 未开始 |
| 87 | tvOS SDK Release Notes for tvOS 10.1 | 1 | `releasenotes/General/tvOS SDK Release Notes for tvOS 10.1.md` | 未开始 |
| 88 | tvOS SDK Release Notes for tvOS 10.2 | 1 | `releasenotes/General/tvOS SDK Release Notes for tvOS 10.2.md` | 未开始 |
| 89 | tvOS SDK Release Notes for tvOS 9.0 | 1 | `releasenotes/General/tvOS SDK Release Notes for tvOS 9.0.md` | 未开始 |
| 90 | tvOS SDK Release Notes for tvOS 9.1 | 1 | `releasenotes/General/tvOS SDK Release Notes for tvOS 9.1.md` | 未开始 |
| 91 | watchOS 2 Release Notes | 1 | `releasenotes/General/watchOS 2 Release Notes.md` | 未开始 |
| 92 | watchOS 2.1 Release Notes | 1 | `releasenotes/General/watchOS 2.1 Release Notes.md` | 未开始 |
| 93 | watchOS 2.2 Release Notes | 1 | `releasenotes/General/watchOS 2.2 Release Notes.md` | 未开始 |
| 94 | watchOS 3.0 Release Notes | 1 | `releasenotes/General/watchOS 3.0 Release Notes.md` | 未开始 |
| 95 | watchOS 3.1 Release Notes | 1 | `releasenotes/General/watchOS 3.1 Release Notes.md` | 未开始 |
| 96 | watchOS 3.1.1 Release Notes | 1 | `releasenotes/General/watchOS 3.1.1 Release Notes.md` | 未开始 |
| 97 | watchOS 3.2 Release Notes | 1 | `releasenotes/General/watchOS 3.2 Release Notes.md` | 未开始 |
| 98 | watchOS 4 Release Notes | 1 | `releasenotes/General/watchOS 4 Release Notes.md` | 未开始 |
| 99 | watchOS 4.1 SDK Release Notes | 1 | `releasenotes/General/watchOS 4.1 SDK Release Notes.md` | 未开始 |
| 100 | watchOS 4.2 SDK Release Notes | 1 | `releasenotes/General/watchOS 4.2 SDK Release Notes.md` | 未开始 |
| 101 | watchOS 4.3 SDK Release Notes | 1 | `releasenotes/General/watchOS 4.3 SDK Release Notes.md` | 未开始 |

### Mac OSX（3 份，63 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 102 | API Changes in Snow Leopard | 50 | `releasenotes/Mac OSX/API Changes in Snow Leopard` | 未开始 |
| 103 | What's New in macOS | 12 | `releasenotes/Mac OSX/What's New in macOS` | 未开始 |
| 104 | Stack Execution Release Notes | 1 | `releasenotes/Mac OSX` | 未开始 |

### Developer Tools（13 份，17 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 105 | GCC Porting Guide | 4 | `releasenotes/Developer Tools/GCC Porting Guide` | 未开始 |
| 106 | Xcode Release Notes | 2 | `releasenotes/Developer Tools/Xcode Release Notes` | 未开始 |
| 107 | Compiler Tools Release Notes | 1 | `releasenotes/Developer Tools/Compiler Tools Release Notes.md` | 未开始 |
| 108 | Dashcode 2.0 Release Notes | 1 | `releasenotes/Developer Tools/Dashcode 2.0 Release Notes.md` | 未开始 |
| 109 | Dynamic Loader Release Notes | 1 | `releasenotes/Developer Tools/Dynamic Loader Release Notes.md` | 未开始 |
| 110 | GCC 3 Release Notes | 1 | `releasenotes/Developer Tools/GCC 3 Release Notes.md` | 未开始 |
| 111 | GCC 4 Release Notes | 1 | `releasenotes/Developer Tools/GCC 4 Release Notes.md` | 未开始 |
| 112 | GDB Release Notes | 1 | `releasenotes/Developer Tools/GDB Release Notes.md` | 未开始 |
| 113 | Interface Builder Release Notes | 1 | `releasenotes/Developer Tools/Interface Builder Release Notes.md` | 未开始 |
| 114 | LLVM-GCC Release Notes | 1 | `releasenotes/Developer Tools/LLVM-GCC Release Notes.md` | 未开始 |
| 115 | Malloc Debug Environment Variables Release Notes | 1 | `releasenotes/Developer Tools/Malloc Debug Environment Variables Release Notes.md` | 未开始 |
| 116 | Terminal 2 Release Notes | 1 | `releasenotes/Developer Tools/Terminal 2 Release Notes.md` | 未开始 |
| 117 | Xcode FAQ | 1 | `releasenotes/Developer Tools/Xcode FAQ` | 未开始 |

### Java（14 份，14 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 118 | Java for OS X 2012-004 and Java for OS X v10.6 Update 9 Release Notes | 1 | `releasenotes/Java/Java for OS X 2012-004 and Java for OS X v10.6 Update 9 Release Notes.md` | 未开始 |
| 119 | Java for OS X 2012-006 and Java for OS X v10.6 Update 11 Release Notes | 1 | `releasenotes/Java/Java for OS X 2012-006 and Java for OS X v10.6 Update 11 Release Notes.md` | 未开始 |
| 120 | Java for OS X 2013-001 and Java for OS X v10.6 Update 13 Release Notes | 1 | `releasenotes/Java/Java for OS X 2013-001 and Java for OS X v10.6 Update 13 Release Notes.md` | 未开始 |
| 121 | Java for OS X v10.4, Release 7 Release Notes | 1 | `releasenotes/Java/Java for OS X v10.4, Release 7 Release Notes.md` | 未开始 |
| 122 | Java for OS X v10.4, Release 8 Release Notes | 1 | `releasenotes/Java/Java for OS X v10.4, Release 8 Release Notes.md` | 未开始 |
| 123 | Java for OS X v10.5 Update 1 Release Notes | 1 | `releasenotes/Java/Java for OS X v10.5 Update 1 Release Notes.md` | 未开始 |
| 124 | Java for OS X v10.5 Update 2 Release Notes | 1 | `releasenotes/Java/Java for OS X v10.5 Update 2 Release Notes.md` | 未开始 |
| 125 | Java for OS X v10.5 Update 3 Release Notes | 1 | `releasenotes/Java/Java for OS X v10.5 Update 3 Release Notes.md` | 未开始 |
| 126 | Java for OS X v10.5 Update 4 Release Notes | 1 | `releasenotes/Java/Java for OS X v10.5 Update 4 Release Notes.md` | 未开始 |
| 127 | Java for OS X v10.5 Update 5 Release Notes | 1 | `releasenotes/Java/Java for OS X v10.5 Update 5 Release Notes.md` | 未开始 |
| 128 | Java for OS X v10.6 Update 3 and 10.5 Update 8 Release Notes | 1 | `releasenotes/Java/Java for OS X v10.6 Update 3 and 10.5 Update 8 Release Notes.md` | 未开始 |
| 129 | Java for OS X v10.6 Update 4 and 10.5 Update 9 Release Notes | 1 | `releasenotes/Java/Java for OS X v10.6 Update 4 and 10.5 Update 9 Release Notes.md` | 未开始 |
| 130 | Java for OS X v10.6 Update 5 and 10.5 Update 10 Release Notes | 1 | `releasenotes/Java/Java for OS X v10.6 Update 5 and 10.5 Update 10 Release Notes.md` | 未开始 |
| 131 | Java for OS X v10.7 Update 1 and 10.6 Update 6 Release Notes | 1 | `releasenotes/Java/Java for OS X v10.7 Update 1 and 10.6 Update 6 Release Notes.md` | 未开始 |

### Carbon（12 份，12 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 132 | Carbon Core Release Notes | 1 | `releasenotes/Carbon/Carbon Core Release Notes.md` | 未开始 |
| 133 | Carbon Developer Tools Release Notes | 1 | `releasenotes/Carbon/Carbon Developer Tools Release Notes.md` | 未开始 |
| 134 | Carbon Framework Release Notes | 1 | `releasenotes/Carbon/Carbon Framework Release Notes.md` | 未开始 |
| 135 | Carbon Resolution Independence Release Notes | 1 | `releasenotes/Carbon/Carbon Resolution Independence Release Notes.md` | 未开始 |
| 136 | High Level Toolbox Release Notes (10.4) | 1 | `releasenotes/Carbon/High Level Toolbox Release Notes (10.4).md` | 未开始 |
| 137 | High Level Toolbox Release Notes (10.4.2) | 1 | `releasenotes/Carbon/High Level Toolbox Release Notes (10.4.2).md` | 未开始 |
| 138 | High Level Toolbox Release Notes (10.4.3) | 1 | `releasenotes/Carbon/High Level Toolbox Release Notes (10.4.3).md` | 未开始 |
| 139 | High Level Toolbox Release Notes (10.5) | 1 | `releasenotes/Carbon/High Level Toolbox Release Notes (10.5).md` | 未开始 |
| 140 | High Level Toolbox Release Notes (10.5.2) | 1 | `releasenotes/Carbon/High Level Toolbox Release Notes (10.5.2).md` | 未开始 |
| 141 | Launch Services Release Notes | 1 | `releasenotes/Carbon/Launch Services Release Notes.md` | 未开始 |
| 142 | OS Services Framework Release Notes | 1 | `releasenotes/Carbon/OS Services Framework Release Notes.md` | 未开始 |
| 143 | Speech Release Notes | 1 | `releasenotes/Carbon/Speech Release Notes.md` | 未开始 |

### （未分类，直接位于 releasenotes 根目录）（11 份，11 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 144 | Adding Complications to the Gallery | 1 | `releasenotes/Adding Complications to the Gallery.md` | 未开始 |
| 145 | CFNetwork Framework Release Notes | 1 | `releasenotes/CFNetwork Framework Release Notes.md` | 未开始 |
| 146 | DiscRecording Release Notes | 1 | `releasenotes/DiscRecording Release Notes.md` | 未开始 |
| 147 | In-App Purchase Receipt Validation for iOS 5.1 and Earlier | 1 | `releasenotes/In-App Purchase Receipt Validation for iOS 5.1 and Earlier.md` | 未开始 |
| 148 | Magic Mouse Developer Release Notes | 1 | `releasenotes/Magic Mouse Developer Release Notes.md` | 未开始 |
| 149 | ODBC Administrator does not display per-user configuration information on OS | 1 | `releasenotes/ODBC Administrator does not display per-user configuration information on OS X v.md` | 未开始 |
| 150 | Perl, Python, and Ruby Extensions Release Notes | 1 | `releasenotes/Perl, Python, and Ruby Extensions Release Notes.md` | 未开始 |
| 151 | Text Encoding Conversion Manager Release Notes | 1 | `releasenotes/Text Encoding Conversion Manager Release Notes.md` | 未开始 |
| 152 | WebObjects 5.3 Release Notes | 1 | `releasenotes/WebObjects 5.3 Release Notes.md` | 未开始 |
| 153 | What's New in Xcode 4 | 1 | `releasenotes/What's New in Xcode 4.md` | 未开始 |
| 154 | iOS 2.2 Release Notes | 1 | `releasenotes/iOS 2.2 Release Notes.md` | 未开始 |

### Cocoa（7 份，7 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 155 | Core Data Release Notes | 1 | `releasenotes/Cocoa/Core Data Release Notes.md` | 未开始 |
| 156 | Core Data Release Notes for OS X v10.6 and iOS 4 | 1 | `releasenotes/Cocoa/Core Data Release Notes for OS X v10.6 and iOS 4.md` | 未开始 |
| 157 | Garbage Collection Release Notes | 1 | `releasenotes/Cocoa/Garbage Collection Release Notes.md` | 未开始 |
| 158 | Input Method Kit Release Note | 1 | `releasenotes/Cocoa/Input Method Kit Release Note.md` | 未开始 |
| 159 | NSURL and CFURL Release Notes | 1 | `releasenotes/Cocoa/NSURL and CFURL Release Notes.md` | 未开始 |
| 160 | Objective-C Release Notes | 1 | `releasenotes/Cocoa/Objective-C Release Notes.md` | 未开始 |
| 161 | Workaround for Core Data store migration in applications built on 10.6 but | 1 | `releasenotes/Cocoa/Workaround for Core Data store migration in applications built on 10.6 but that.md` | 未开始 |

### Darwin（6 份，6 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 162 | FireWire Release Notes | 1 | `releasenotes/Darwin/FireWire Release Notes.md` | 未开始 |
| 163 | IOKit Power Management Release Notes | 1 | `releasenotes/Darwin/IOKit Power Management Release Notes.md` | 未开始 |
| 164 | Kernel Extensions Release Notes | 1 | `releasenotes/Darwin/Kernel Extensions Release Notes.md` | 未开始 |
| 165 | Symbol Variants Release Notes | 1 | `releasenotes/Darwin/Symbol Variants Release Notes.md` | 未开始 |
| 166 | USB Release Notes | 1 | `releasenotes/Darwin/USB Release Notes.md` | 未开始 |
| 167 | Unix 03 Conformance Release Notes | 1 | `releasenotes/Darwin/Unix 03 Conformance Release Notes.md` | 未开始 |

### Foundation（5 份，5 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 168 | Foundation Release Notes (macOS 10.12 and Earlier) | 1 | `releasenotes/Foundation/Foundation Release Notes (macOS 10.12 and Earlier).md` | 未开始 |
| 169 | Foundation Release Notes for OS X v10.10 and iOS v8 | 1 | `releasenotes/Foundation/Foundation Release Notes for OS X v10.10 and iOS v8.md` | 未开始 |
| 170 | Foundation Release Notes for OS X v10.9 | 1 | `releasenotes/Foundation/Foundation Release Notes for OS X v10.9.md` | 未开始 |
| 171 | Foundation Release Notes for iOS | 1 | `releasenotes/Foundation/Foundation Release Notes for iOS.md` | 未开始 |
| 172 | Foundation Release Notes for macOS 10.13 and iOS 11 | 1 | `releasenotes/Foundation/Foundation Release Notes for macOS 10.13 and iOS 11.md` | 未开始 |

### Miscellaneous（5 份，5 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 173 | Converting to Storyboards Release Notes | 1 | `releasenotes/Miscellaneous/Converting to Storyboards Release Notes` | 未开始 |
| 174 | Foundation Release Notes for macOS 10.12 and iOS 10 | 1 | `releasenotes/Miscellaneous/Foundation Release Notes for macOS 10.12 and iOS 10.md` | 未开始 |
| 175 | iOS 2.1 API Diffs | 1 | `releasenotes/Miscellaneous/iOS 2.1 API Diffs.md` | 未开始 |
| 176 | iOS 2.2 API Diffs | 1 | `releasenotes/Miscellaneous/iOS 2.2 API Diffs.md` | 未开始 |
| 177 | iOS 4.3.2 Release Notes | 1 | `releasenotes/Miscellaneous/iOS 4.3.2 Release Notes.md` | 未开始 |

### Graphics Imaging（4 份，4 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 178 | 2D Graphics Release Notes for OS X v10.5 | 1 | `releasenotes/Graphics Imaging/2D Graphics Release Notes for OS X v10.5.md` | 未开始 |
| 179 | Core Animation Release Notes | 1 | `releasenotes/Graphics Imaging/Core Animation Release Notes.md` | 未开始 |
| 180 | Quartz Composer Release Note | 1 | `releasenotes/Graphics Imaging/Quartz Composer Release Note.md` | 未开始 |
| 181 | Resolution Independent UI Release Notes | 1 | `releasenotes/Graphics Imaging/Resolution Independent UI Release Notes.md` | 未开始 |

### Apple Applications（4 份，4 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 182 | Automation Release Notes for OS X v10.7 | 1 | `releasenotes/Apple Applications/Automation Release Notes for OS X v10.7.md` | 未开始 |
| 183 | Mail Stationery Release Notes for OS X v10.5 | 1 | `releasenotes/Apple Applications/Mail Stationery Release Notes for OS X v10.5.md` | 未开始 |
| 184 | Sync Services  Release Notes (10.4) | 1 | `releasenotes/Apple Applications/Sync Services Release Notes (10.4).md` | 未开始 |
| 185 | Sync Services Release Notes (10.5) | 1 | `releasenotes/Apple Applications/Sync Services Release Notes (10.5).md` | 未开始 |

### JavaScript for Automation Release Notes（1 份，4 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 186 | JavaScript for Automation Release Notes | 4 | `releasenotes/JavaScript for Automation Release Notes` | 未开始 |

### Scripting Automation（3 份，3 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 187 | AppleScript Studio 1.4 Release Notes | 1 | `releasenotes/Scripting Automation/AppleScript Studio 1.4 Release Notes.md` | 未开始 |
| 188 | AppleScriptObjC Release Notes | 1 | `releasenotes/Scripting Automation/AppleScriptObjC Release Notes.md` | 未开始 |
| 189 | Scripting Bridge Release Note | 1 | `releasenotes/Scripting Automation/Scripting Bridge Release Note.md` | 未开始 |

### Apple Script（3 份，3 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 190 | AppleScript Release Notes | 1 | `releasenotes/Apple Script/AppleScript Release Notes.md` | 未开始 |
| 191 | AppleScript Studio Release Notes | 1 | `releasenotes/Apple Script/AppleScript Studio Release Notes.md` | 未开始 |
| 192 | AppleScript Terminology and Apple Event Codes Reference | 1 | `releasenotes/Apple Script/AppleScript Terminology and Apple Event Codes Reference.md` | 未开始 |

### Core Foundation（2 份，2 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 193 | Core Foundation Release Notes for OS X v10.9 | 1 | `releasenotes/Core Foundation/Core Foundation Release Notes for OS X v10.9.md` | 未开始 |
| 194 | Core Foundation Release Notes for iOS | 1 | `releasenotes/Core Foundation/Core Foundation Release Notes for iOS.md` | 未开始 |

### Mac OSX Server（2 份，2 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 195 | Directory Services for OS X Server v10.5 Release Notes | 1 | `releasenotes/Mac OSX Server/Directory Services for OS X Server v10.5 Release Notes.md` | 未开始 |
| 196 | WebObjects 5.4 Release Notes | 1 | `releasenotes/Mac OSX Server/WebObjects 5.4 Release Notes.md` | 未开始 |

### Data Management（2 份，2 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 197 | Core Data Release Notes for OS X v10.7 and iOS 5.0 | 1 | `releasenotes/Data Management/Core Data Release Notes for OS X v10.7 and iOS 5.0.md` | 未开始 |
| 198 | Core Foundation Release Notes for OS X (10.8 and earlier) | 1 | `releasenotes/Data Management/Core Foundation Release Notes for OS X (10.8 and earlier).md` | 未开始 |

### App Kit（2 份，2 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 199 | AppKit Release Notes (macOS 10.12 and Earlier) | 1 | `releasenotes/App Kit/AppKit Release Notes (macOS 10.12 and Earlier).md` | 未开始 |
| 200 | AppKit Release Notes for macOS 10.13 | 1 | `releasenotes/App Kit/AppKit Release Notes for macOS 10.13.md` | 未开始 |

### Objective C（2 份，2 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 201 | Objective-C Feature Availability Index | 1 | `releasenotes/Objective C/Objective-C Feature Availability Index.md` | 未开始 |
| 202 | Transitioning to ARC Release Notes | 1 | `releasenotes/Objective C/Transitioning to ARC Release Notes.md` | 未开始 |

### Hardware Drivers（2 份，2 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 203 | CCL Modem Scripting Release Notes | 1 | `releasenotes/Hardware Drivers/CCL Modem Scripting Release Notes.md` | 未开始 |
| 204 | SMB Release Notes | 1 | `releasenotes/Hardware Drivers/SMB Release Notes.md` | 未开始 |

### User Experience（2 份，2 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 205 | Cocoa Auto Layout Release Notes | 1 | `releasenotes/User Experience/Cocoa Auto Layout Release Notes` | 未开始 |
| 206 | SearchKit Release Notes | 1 | `releasenotes/User Experience` | 未开始 |

### Audio Video（2 份，2 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 207 | AV Foundation Release Notes | 1 | `releasenotes/Audio Video/AV Foundation Release Notes.md` | 未开始 |
| 208 | AV Foundation Release Notes (iOS 4.3) | 1 | `releasenotes/Audio Video/AV Foundation Release Notes (iOS 4.3).md` | 未开始 |

### Cross Platform（2 份，2 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 209 | Java for OS X v10.6 Update 1 and 10.5 Update 6 Release Notes | 1 | `releasenotes/Cross Platform/Java for OS X v10.6 Update 1 and 10.5 Update 6 Release Notes.md` | 未开始 |
| 210 | Java for OS X v10.6 Update 2 and 10.5 Update 7 Release Notes | 1 | `releasenotes/Cross Platform/Java for OS X v10.6 Update 2 and 10.5 Update 7 Release Notes.md` | 未开始 |

### Networking Internet Web（2 份，2 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 211 | Open Directory Release Notes | 1 | `releasenotes/Networking Internet Web/Open Directory Release Notes.md` | 未开始 |
| 212 | Time Machine Over SMB Specification | 1 | `releasenotes/Networking Internet Web/Time Machine Over SMB Specification.md` | 未开始 |

### Performance（2 份，2 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 213 | Accelerate Release Notes | 1 | `releasenotes/Performance/Accelerate Release Notes.md` | 未开始 |
| 214 | Affinity API Release Notes for OS X v10.5 | 1 | `releasenotes/Performance/Affinity API Release Notes for OS X v10.5.md` | 未开始 |

### NSFetchedResultsController- Moved objects sometimes reported as updated（1 份，1 页）

| # | 英文标题 | 页数 | 物理路径 | 状态 |
| --- | --- | --- | --- | --- |
| 215 | 'NSFetchedResultsController: Moved objects sometimes reported as updated' | 1 | `releasenotes/NSFetchedResultsController- Moved objects sometimes reported as updated` | 未开始 |