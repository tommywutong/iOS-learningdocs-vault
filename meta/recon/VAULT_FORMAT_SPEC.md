# Apple Developer Archive Vault —— 文件格式逆向规范

> 逆向对象：`/Users/tommywu/Desktop/翻译/vault`（GitHub: `XiyouMobile3G-iOS/apple-developer-archive-vault`）
> 目标：照此规范生成的新文件应与仓库现有文件在字节级别不可区分。
> 全部结论均来自对产物的统计与抽样（35,884 个 `.md`，其中 35,752 个是文档页），仓库内无生成脚本。
> 引用格式：`路径:行号`。所有路径相对 vault 根。

---

## 0. 全局事实（先记住这些数字）

| 项 | 值 | 来源 |
|---|---|---|
| `.md` 总数 | 35,884 | `find . -name '*.md'` |
| 带 YAML frontmatter 的文档页 | 35,752 | 全量扫描 |
| 逻辑文档数（distinct `apple_id`） | 4,121 | 全量扫描 |
| 索引文件 | 128（`_indexes/` 下） | `find _indexes -type f` |
| 其他无 frontmatter 的 `.md` | `README.md`、`_unindexed/index.md`、`doc/*.md`(2) | — |
| `attachments/` 目录数 | 558 | `find . -type d -name attachments` |
| `.gitignore` | 单行 `.DS_Store` | `.gitignore:1` |

`doc/TRANSLATION_PLAN*.md` 是翻译工程的工作文档，**不属于归档格式**，生成器不应产出。

> ⚠️ **快照说明**：本规范逆向时（2026-07-26 21:00–22:19）仓库工作区里有 14 个文件处于 `git status` 的 `M`（已修改未提交）状态，且**在分析期间仍被另一个翻译流程持续写入**（`documentation/Cocoa/Threading Programming Guide/Run Loops.md` 的 mtime 一直在推进）。这些 diff 是"英文 → 中文"的翻译改写，正好印证了 §12 第 1–3 条的不一致来源：一次翻译提交会同时改动 ①frontmatter `title` ②导航行第二段 `documentation`→`文档` ③导航行第三段文档标题 ④pager `[Next]/[Previous]`→`[下一页]/[上一页]` ⑤正文 H1 与全文。
> 因此：**本规范中所有"翻译造成的不一致"都属于后期人工改写，不是原生成器的行为；补抓新文档时应按未翻译的英文形态产出。**

**编码/换行**：全部 UTF-8 无 BOM，LF 换行，无 CRLF。

---

## 1. YAML frontmatter

### 1.1 结构与顺序（强不变量）

每个文档页（`_indexes/`、`README.md`、`_unindexed/index.md` 除外）以 frontmatter 开头。9 个键**全部必有**，顺序**固定**，35,752/35,752 全部一致：

```
title, apple_id, resource_type, platform, topic, technology, published, source_url, archived_at
```

样例（`documentation/Accessibility Programming Guide for OS X/index.md:1-11`）：

```
---
title: Accessibility Programming Guide for OS X
apple_id: TP40001078
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/index.html
archived_at: '2026-07-15T03:49:19.624182Z'
---
```

结构上就是 `--- \n` + `yaml.safe_dump(d, sort_keys=False, allow_unicode=True)` + `--- \n`。所有引号/折行行为都能被 PyYAML 默认参数复现（**这是最重要的实现结论**）。

### 1.2 折行（必须复现）

PyYAML 默认 `width=80`。**值过长且含空格时会在空格处折行，续行缩进 2 空格。** 全量统计：35,499 个文件的 frontmatter 是 11 行，**253 个是 12 行**（折行）。

实例 `qa/How do I work-around an issue where some lines in my Core Text output have extra.md:1-12`：

```
---
title: How do I work-around an issue where some lines in my Core Text output have
  extra line spacing?
apple_id: DTS40010203
resource_type: QA
platform: iOS
topic: Data Management
technology: null
published: '2010-07-26'
source_url: https://developer.apple.com/library/archive/qa/qa1698/_index.html
archived_at: '2026-07-18T02:34:12.213675Z'
---
```

- `source_url` 最长 269 字符却**不折行**——URL 无空格，PyYAML 无处可断。
- 带引号的长 title 同样折行，且引号只在首行开头出现，例如 `qa/-Payment requests are restricted to products returned as valid via Store Kit's d/-Payment requests are restricted to products returned as valid via Store Kit's d.md:2-3`：

```
title: '"Payment requests are restricted to products returned as valid via Store Kit''s
  didReceiveResponse method." when testing In App Purchase in the Sandbox environment'
```

### 1.3 逐字段取值格式

#### `title`
- 页面标题原文（**不是**文档标题；多页文档里每页的 `title` 是该页自己的标题，见 §2.3 的例外说明）。
- 引号规则 = PyYAML 的 "必要时加单引号"：只有 2,062 个文件的 title 带引号，**从不出现双引号**（`grep -c '^title: "'` = 0）。加引号的触发条件（观察到的全部情形）：
  - 含 `: `（冒号+空格）→ `title: 'Activity Rings: Contributing to Activity Rings on Apple Watch'`
  - 以 `"` 开头 → `title: '"Xcode cannot find the software image to install this version"'`（`qa/-Xcode cannot find the software image to install this version/...`）
  - 以 `'` 开头 → 内部单引号双写：`title: '''aete'' in Java'`、`title: '''ptyp'' Resource Documentation'`
- 中文标题**不加引号**（`allow_unicode=True`），例：`documentation/Windows Views/Collection View Programming Guide for iOS/Collection View Basics.md:2` → `title: iOS Collection View 编程指南`
- 163 个文件的 title 已译成中文，其余为英文。**两者格式规则完全一样**，翻译只改值不改结构。
- 极少数空值：2 个 `title:` 空、3 个 `title: ''`。

#### `apple_id`
不加引号，除非纯数字。观察到的 5 种形态：

| 形态 | 数量 | 例 |
|---|---|---|
| `DTS` + 8 位数字 | 21,062 | `apple_id: DTS40010203` |
| `TP` + 8 位数字 | 13,594 | `apple_id: TP40001078` |
| 8 位数字 + `i` | 1,067 | `apple_id: 40000000i`（示意） |
| `TP` + 7 位数字 | 17 | — |
| 纯 8 位数字 → **加单引号** | 12 | `apple_id: '40000000'` |

（最后一种是 PyYAML 对 "看起来像整数的字符串" 的必然行为。）

#### `resource_type`
不加引号，仅 4 个取值：

```
Sample Code  (21,868 页)
Guide        ( 9,842 页)
Release Note ( 2,540 页)
QA           ( 1,502 页)
```

#### `platform`
不加引号，多平台用 **半角竖线 `|` 分隔，两侧无空格**。示例：
- `platform: macOS`（26,387 页）
- `platform: iOS|macOS`（788 页）
- `platform: watchOS|tvOS|iOS|macOS`（450 页）
- `platform: Safari (Mobile)|Safari|iOS|macOS`（89 页）—— token 内部允许空格和括号
- `platform: watchOS|tvOS|Safari (Mobile)|iOS|Xcode Developer Tools|macOS`（8 页，最长）

出现过的全部 token：`watchOS`、`tvOS`、`iAd System JS`、`Safari (Mobile)`、`Safari`、`CloudKit JS`、`iAd Producer`、`Java`、`iOS`、`Xcode Developer Tools`、`macOS`。

**书写顺序固定**（43 种组合全部相容于同一个全序，按出现位置从左到右）：

```
watchOS < tvOS < iAd System JS < Safari (Mobile) < Safari < CloudKit JS
        < iAd Producer < Java < iOS < Xcode Developer Tools < macOS
```

> 注意：这个书写顺序**不是**索引分组用的"主平台"顺序，两者是两套规则，见 §6.4。

#### `topic`
不加引号；**无值时写字面量 `null`（不带引号）**，共 15,660 页。全部取值（穷尽）：

```
null / Graphics & Animation / General / Audio, Video, & Visual Effects / User Experience
Data Management / Networking, Internet, & Web / Cross Platform / Xcode
Drivers, Kernel, & Hardware / Interapplication Communication / Performance
Languages & Utilities / Security / Apple Applications / Mathematical Computation
System Administration
```

注意 `&`、`,` 都是裸写不转义、不加引号。

#### `technology`
同 `topic`：不加引号，无值写 `null`（20,727 页）。取值是框架名，例：`AppKit`、`QuickTime`、`OpenGL`、`Foundation`、`AVFoundation`、`AudioUnit`、`UIKit`、`ApplicationServices`、`QuartzCore`、`CoreServices`、`Metal`、`SceneKit`、`CloudKit`、`WatchKit`、`WebKit` …

#### `published`
**总是单引号包裹的 `YYYY-MM-DD`**，35,752/35,752 一致：`published: '2015-04-08'`。
（PyYAML 对日期形态的字符串必然加引号。）

#### `source_url`
不加引号、不折行、原始 HTML 页面的完整 URL。前缀恒为 `https://developer.apple.com/library/archive/`，其后是 Apple 原始路径。例：
- `https://developer.apple.com/library/archive/qa/qa1698/_index.html`
- `https://developer.apple.com/library/archive/qa/hw/hw81.html`
- `https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/CollectionViewPGforIOS/CollectionViewBasics/CollectionViewBasics.html`

#### `archived_at`
**总是单引号包裹的 UTC ISO8601，微秒 6 位 + `Z`**：`archived_at: '2026-07-18T02:34:12.213675Z'`，35,752/35,752 一致。
即 `datetime.now(timezone.utc).isoformat().replace('+00:00','Z')` 的形态。抓取时间逐页不同（同一文档的不同页时间戳也不同），范围在 2026-07-15 ~ 2026-07-18。

---

## 2. 目录结构与文件名

### 2.1 顶层

```
/README.md
/_indexes/…                     索引层（无 frontmatter）
/_unindexed/…                   未编入导航索引的页面 + 共享图片资源
/documentation/                 Guide 类（60 个条目）
/qa/                            Technical Q&A（576 个条目）
/samplecode/                    Sample Code（1,760 个条目）
/releasenotes/                  Release Notes（36 个条目）
/referencelibrary/              1 个分类目录 "Getting Started"
/featuredarticles/              7 个条目
/recipes/                       3 个条目
/ApplePay_Guide/                1 个条目
/LucidDreams/                   1 个条目
/.obsidian/                     4 个 json
/doc/                           翻译工程文档（非归档产物）
```

顶层目录名 = Apple 原 URL 中 `/library/archive/` 之后的第一段，**原样保留**（含下划线的 `ApplePay_Guide`、驼峰的 `LucidDreams`）。

### 2.2 分类层（可选）

`documentation` / `qa` / `releasenotes` / `referencelibrary` 有二级"分类"目录，分类 id 取自原 URL 第二段，目录名是它的**人类可读形式**（驼峰拆词 / 下划线转空格）：

| URL 分类 id | 目录名 |
|---|---|
| `3DDrawing` | `3D Drawing` |
| `WindowsViews` | `Windows Views` |
| `MacOSX` | `Mac OSX` |
| `QuickTime` | `Quick Time` |
| `WebObjects` | `Web Objects` |
| `iPhone` | `iPhone`（首字母小写保持） |
| `IDEs` | `IDEs`（全大写不拆） |
| `FinalCutProX` | `Final Cut Pro X` |
| `amt_pe`（qa） | `amt pe` |
| `GettingStarted` | `Getting Started` |
| `ObjectiveC`（releasenotes） | `Objective C` |

完整映射见 `_indexes/documentation.md:7-95`、`_indexes/qa.md:7`+、`_indexes/releasenotes.md:7`+、`_indexes/referencelibrary.md:7`——每行 `## [<目录名>](<type>/<分类id>.md)（N 份）` 同时给出了两侧。

**没有分类的文档直接放在类型目录下**（`documentation/LLVM Compiler Overview.md`、`documentation/Accessibility Programming Guide for OS X/`）。这些文档在 `_indexes/documentation.md:97` 的 `## 文档` 段落里列出。
`samplecode` / `featuredarticles` / `recipes` / `ApplePay_Guide` / `LucidDreams` **无分类层**。

### 2.3 文档层：单页 vs 多页

- **多页文档** → 专属目录，目录名 = `sanitize(文档标题)`，所有页面 `.md` 平铺在里面，`attachments/` 也在这一层：
  ```
  documentation/Windows Views/Collection View Programming Guide for iOS/
      About iOS Collection Views.md          ← 入口页
      Collection View Basics.md
      …
      Document Revision History.md
      attachments/Art/*.png
  ```
- **单页 + 有图** → 也建目录，目录内只有一个同名 `.md` 和 `attachments/`（136 例）：
  ```
  qa/Accessing Audio Files in Asset Catalogs/
      Accessing Audio Files in Asset Catalogs.md
      attachments/
  ```
- **单页 + 无图** → 直接一个 `.md`，放在类型/分类目录下：`qa/Accessing Image Metadata in iOS.md`、`documentation/Quick Time/QuickTime Movie Creation Guide.md`
- **单页但页名 ≠ 文档名** → 仍建目录：`qa/hw/A SCSI little secret/hw81.md`（文档标题 `A SCSI little secret`，页面名回落成 HTML 文件名 `hw81`）

### 2.4 `sanitize()` —— 标题 → 文件/目录名（核心算法）

在 2,311 个"英文标题 + 专属目录"样本上，下述实现命中 **2,291/99.1%**；在 1,781 个单页样本上命中 1,228（其余不匹配是因为页名来自 HTML stem，见 §2.5）：

```python
def sanitize(name: str) -> str:
    s = re.sub(r'<[^>]*>', '', name)          # 1. 先剥 HTML 标签
    s = re.sub(r'[_*#]', '', s)               # 2. 删除：_ * #
    s = re.sub(r'[<>:"/\\|?\[\]]', '-', s)    # 3. 替换为 '-'：< > : " / \ | ? [ ]
    s = re.sub(r'\s+', ' ', s).strip()        # 4. 空白折叠 + 两端去空白
    s = s[:80]                                # 5. 截断到 80 字符
    s = s.rstrip(' .-')                       # 6. 去掉尾部空格/点/连字符
    return s
```

逐条证据（title → 实际文件名）：

| title | 结果 | 规则 |
|---|---|---|
| `Your Third iOS App: iCloud` | `Your Third iOS App- iCloud` | `:`→`-` |
| `Image I/O Programming Guide` | `Image I-O Programming Guide` | `/`→`-` |
| `"Error launching remote program: failed to get the task for process"` | `-Error launching remote program- failed to get the task for process` | `"`→`-`、`:`→`-`、尾部 `-` 被剥掉、**首部 `-` 保留** |
| `Camera Hither Distance Must Be > 0` | `Camera Hither Distance Must Be - 0` | `>`→`-` |
| `Deprecated CALL_ON_[UN]LOAD pragmas` | `Deprecated CALLON-UN-LOAD pragmas` | `_` 删除、`[`/`]`→`-` |
| `LaserWriter 8 Support for *JCL/PCL` | `LaserWriter 8 Support for JCL-PCL` | `*` 删除、`/`→`-` |
| `Using the kQTPropertyClass_DRM properties with QuickTime` | `Using the kQTPropertyClassDRM properties with QuickTime` | `_` 删除 |
| `How do I use asserts while debugging?` | `How do I use asserts while debugging` | 尾 `?`→`-` 再被剥掉 |
| `LaserWriter 8.3 %%?BeginQuery: RBIAppleDevice Query` | `LaserWriter 8.3 %%-BeginQuery- RBIAppleDevice Query` | 中间的 `?`→`-`（证明 `?` 是替换不是删除）；`%` 保留 |
| `Why am I getting a 'Failed to start remote debugserver for <name>.app on <device>' error?` | `Why am I getting a 'Failed to start remote debugserver for .app on ' error` | `<name>` / `<device>` 被当 HTML 标签整段剥掉 |
| `NSPersistentDocument Core Data Tutorial for Mac OS X v10.4.` | `NSPersistentDocument Core Data Tutorial for Mac OS X v10.4` | 尾 `.` 剥掉 |
| `Safari's "Mail [Contents/Link] of This page" to Mail Client events...` | `Safari's -Mail -Contents-Link- of This page- to Mail Client events` | 综合 |
| `'dynamic shared library not made a weak library in output with MACOSX_DEPLOYMENT_TARGET...'` | `'dynamic shared library not made a weak library in output with MACOSXDEPLOYMENTT` | `_` 删除后再截 80 |

**保留不动的字符**（在真实目录名中出现过）：空格、`!`、`&`、`'`、`(`、`)`、`+`、`,`、`-`、`.`、`;`、`—`(em dash)、`’`(弯撇号)、`%`、中文。

**截断**：80 字符是硬上限（stem 长度 max = 80，加 `.md` 后 83）。截断在冲突后缀之前，因此带后缀时可达 82 字符：`samplecode/Denoise/Sources-Classes-Toolkits-Model-OpenGL-Objects-Teapot-Core-Implementations-Textur-2.md`（stem 82）。

**冲突消歧**：同目录同名时追加 `-2`、`-3`、…（从 2 起，观察到最大 `-6`）。
例：`documentation/Cocoa/Using the Java Bridge/Legacy Documentclose button.md` … `Legacy Documentclose button-6.md`。
文档目录也会带后缀：`documentation/Hardware Drivers/15-inch MacBook Pro Developer Note (2007)-3/`。

### 2.5 页面文件名的两条来源（重要，不一致点）

页名优先取**页面自身的标题**并 `sanitize()`；取不到就**原样使用 HTML 文件 stem（不做 sanitize）**：

- 标题派生：`documentation/Windows Views/Collection View Programming Guide for iOS/About iOS Collection Views.md`
- stem 派生：`documentation/3D Drawing/Metal Best Practices Guide/RenderCommandEncoders.md`（源 `RenderCommandEncoders.html`）、`documentation/3D Drawing/Metal Best Practices Guide/index.md`（源 `index.html`）、`qa/hw/A SCSI little secret/hw81.md`、`featuredarticles/Using Doxygen to Create Xcode Documentation Sets/_index.md`
- stem 派生的证据：263 个 `.md` basename 里含 `_`（sanitize 会删 `_`），如 `documentation/Xcode/Asset Catalog Format Reference/AR_Resource_Group.md`、`documentation/Cocoa/Core Data Programming Guide/MO_Lifecycle.md`

**旧版 QA 的病态页名**：老页面的 H1 是页面装饰而不是标题，于是页名变成 `Legacy Documentclose button.md` / `Not Recommended Documentclose button.md`（各带 `-2`…后缀）。见 `qa/hw/DDC Information Source/Legacy Documentclose button.md`、`_indexes/qa/hw.md:9-11`。**新抓文档不应刻意复现这个 bug**，但要知道存在。

### 2.6 samplecode 源码页名

`<原相对路径，'/' 换成 '-'>.md`，扩展名保留后再接 `.md`：

| 原路径 | 文件名 |
|---|---|
| `main.m` | `main.m.md` |
| `Classes/ABUIGroupsAppDelegate.h` | `Classes-ABUIGroupsAppDelegate.h.md` |
| `GLSLShowpiece Lite/Surfaces/Klein Surface/Sources/KleinSurface.mm` | `GLSLShowpiece Lite-Surfaces-Klein Surface-Sources-KleinSurface.mm.md` |
| `MyGreatAUEffectWithCocoaUI(Lion)/PublicUtility/CAMutex.cpp` | `MyGreatAUEffectWithCocoaUI(Lion)-PublicUtility-CAMutex.cpp.md` |

同样受 80 字符截断 + `-N` 冲突后缀约束（`samplecode/Denoise/` 是最好的例子）。段内本身含 `-` 时不可逆——真实路径要看正文 H1。

### 2.7 `attachments/` 与图片

- 位置：**文档目录下一层**（与页面 `.md` 同级）。`documentation/Windows Views/Collection View Programming Guide for iOS/attachments/Art/cv_objects_2x.png`
- **保留原 HTML 中的相对子目录结构**：`Art/`（379 例）、`System/`（133）、`art/`（120）、`chapters/`（50）、`Concepts/`（46）、`Tasks/`、`Articles/`、`images/`、`Reference/` 等；可以多级：`attachments/chapters/RM_YourFirstApp_iOS/Art/object_library.png`、`attachments/Concepts/Art/connections.gif`
- 图片文件名 = 原文件名，一字不改（含 `_2x` 后缀、大小写）。`../` 前缀在落盘时被剥掉。
- 少量文档没有自己的 `attachments/`，图片指向 `_unindexed/`：`recipes/Repositories Organizer Help/Setting Up a Git Repository.md:20` → `![bullet](../../_unindexed/Resources/1282/Images/task_2x.png)`

### 2.8 `_unindexed/`

镜像 Apple 原始 URL 路径（**不做重命名**），共 701 个 `.md` + 大量图片：
`_unindexed/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DirectToWeb/DirectToWeb.8.md`、`_unindexed/documentation/Networking/Reference/IdentityServices_Ref/CSIdentity/index.md`。
这些页面**有完整 frontmatter**，导航行第二段是 `未编入索引的页面`（纯文本，无链接）。
`_unindexed/index.md` 无 frontmatter，格式见 §6.6。

---

## 3. 页面正文骨架

### 3.1 头部模板（强不变量）

```
---
<9 个 frontmatter 键，可能因折行多 1 行>
---
> 导航：…                       ← 紧接 --- 后，无空行
                                ← 空行 1
                                ← 空行 2
[翻页行]                        ← 仅多页文档有；单页文档这里是空行 3
                                ← 空行
<正文第一行>
```

原始字节（`documentation/Xcode/What's New in Xcode — Archive/New Features in Xcode 7.md`，frontmatter 之后）：

```
'> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [What'
"'s New in Xcode — Archive](What%E2%80%99s%20New%20in%20Xcode%20-%20Archive.md)\n\n\n[Next](New%20Fe"
'atures%20in%20Xcode%206.md)[Previous](What%E2%80%99s%20New%20in%20Xcode%20-%20Archive.md)\n\n# …'
```

无翻页行时（`documentation/LLVM Compiler Overview.md`）：

```
'> 导航：[总目录](../README.md) · [documentation](../_indexes/documentation.md)\n\n\n\n# LLVM Compiler Overview\n\n…'
```

即：`nav + "\n"` + `"\n\n"` + (`pager + "\n"` 或 空) + `"\n"` + 正文。
全量首 6 行形态统计（前 3 名）：

```
24,738  NAV, 空, 空, PAGER, 空, H1     e.g. documentation/Xcode/What's New in Xcode — Archive/New Features in Xcode 7.md
 3,569  NAV, 空, 空, 文本, 文本, 文本   e.g. documentation/Networking/Core Services Identity Reference/CompositePage.md
 1,516  NAV, 空, 空, 空, 文本, 空       e.g. documentation/Carbon/Programming with the Appearance Manager/Case Studies….md
```

### 3.2 文件结尾

- **有翻页行**：文件以 `翻页行 + "\n\n"` 结束（末尾一个空行）。25,606 个文件如此。
  `documentation/Xcode/What's New in Xcode — Archive/New Features in Xcode 7.md` 结尾字节：
  `'…\n\n[Next](New%20Features%20in%20Xcode%206.md)[Previous](What%E2%80%99s%20New%20in%20Xcode%20-%20Archive.md)\n\n'`
- **无翻页行**：绝大多数以单个 `"\n"` 结束（`documentation/LLVM Compiler Overview.md` → `'…project.\n'`）。
- 全量尾部换行统计：`\n\n` 26,235 个、`\n` 9,510 个、`\n\n\n` 7 个，**`\n` 数为 0（无末尾换行）的文件：0 个**。
  `documentation/` 内细分：1 个 LF → 5,477 文件、2 个 LF → 3,745、3 个 LF → 5、0 个 → 0。
- **不一致**：98 个带翻页行的文件只有 1 个尾换行；566 个以表格结尾的文件有 2 个尾换行、125 个只有 1 个；54 个以普通段落结尾的有 2 个。**其中带 CJK 的（翻译过的）文件里，101 个只剩 1 个尾换行**——翻译改写破坏了原有约定。→ 生成器请统一按"有 pager 用 `\n\n`，否则 `\n`"。

---

## 4. 导航行（breadcrumb）

### 4.1 格式

```
> 导航：[总目录](<…/>README.md) · [<顶层目录名>](<…/>_indexes/<顶层目录名>.md) · [<文档标题>](<入口页文件名>.md)
```

- 引导：`> 导航：`（中文全角冒号 U+FF1A），紧接 frontmatter 的 `---` 之后，**35,881 行全部一致**。
- 分隔符：` · `（空格 + U+00B7 + 空格）。
- 段数：3 段（30,946 个文件）、2 段（4,914，单页文档 / 无所属文档）、1 段（21，全部是 `_indexes/` 里的索引文件）。**从不出现 4 段。**

### 4.2 相对深度

`../` 的个数 **等于文件路径中的目录层数**（= `path.count('/')`）。全量校验完全一致：

| 文件路径深度 | `../` 数 | 例 |
|---|---|---|
| 1（`qa/X.md`） | 1 | `qa/Accessing Image Metadata in iOS.md:12` → `[总目录](../README.md) · [qa](../_indexes/qa.md)` |
| 2（`qa/Doc/X.md`） | 2 | `qa/Adding Bluetooth LE MIDI Support/Adding Bluetooth LE MIDI Support.md:12` → `../../README.md` |
| 3（`documentation/Cat/Doc/X.md`） | 3 | `documentation/Windows Views/Collection View Programming Guide for iOS/Collection View Basics.md:12` → `../../../README.md` |
| 6（`_unindexed/...`） | 6 | `_unindexed/documentation/Networking/Reference/IdentityServices_Ref/CSIdentity/index.md:12` → `../../../../../../README.md` |

### 4.3 第二段（分类索引）

标签 = **顶层目录名原样**：`samplecode`(21,818)、`documentation`(9,068)、`releasenotes`(2,322)、`qa`(1,500)、`referencelibrary`(53)、`LucidDreams`(40)、`featuredarticles`(34)、`recipes`(20)、`ApplePay_Guide`(6)。
`_unindexed/` 下的页面第二段是**纯文本 `未编入索引的页面`（无方括号无链接）**，701 个文件。

**不一致（翻译造成）**：159 个已翻译文件把标签写成 `[文档]`（`documentation/Windows Views/Collection View Programming Guide for iOS/Collection View Basics.md:12`），而另有 138 个已翻译文件仍写 `documentation`。→ 生成器一律用英文目录名。
（同一事实的另一种计数：`documentation/` 目录内 9,112 个文件写 `documentation`、115 个写 `文档`；两次统计口径不同，量级一致。典型反例是 `documentation/Cocoa/Key-Value Coding Programming Guide/index.md:12` —— 正文全中文但 nav 标签仍是 `documentation`。）

### 4.4 第三段（所属文档 → 入口页）

- 标签 = **该文档的 `title`**（30,837/30,946 与本页 frontmatter `title` 完全相同；109 个不一致的是"nav 标签已译、frontmatter 未译"的部分翻译文件，如 `documentation/Cocoa/Core Data Programming Guide/RevisionHistory.md:12` 写 `[Core Data 编程指南](index.md)` 而 frontmatter 是 `Core Data Programming Guide`）。
- 链接 = **同目录下的入口页文件名**，绝不含 `/`（30,946/30,946）。
- 入口页文件名分布：具名 30,015、`index.md` 931。**从不出现 `_index.md`**（尽管该文件存在于 `featuredarticles/Using Doxygen to Create Xcode Documentation Sets/`——那个文档只有 1 页，没有第三段）。
- **如何判定入口页**：nav 只有 2 段的那一页就是入口页（samplecode 1,760/1,760、releasenotes 212/212 全部成立）；等价地，它是唯一"有 `[Next]` 无 `[Previous]`"的页。
- 入口页名**不能**从目录名推导：
  - `samplecode/`：1,755 个 = `<目录名>.md`，5 个例外（`ImageKit with Core Data/Image Kit with Core Data.md`、`SceneKit Animations/Scene Kit Animations.md`、`PrintPhoto- Using the Printing API with Photos/PrintPhoto.md` …）
  - `releasenotes/`：25 个多页文档里只有 2 个 = `<目录名>.md`（`General/tvOS 10.0 API Diffs/` 的入口是 `tvOS 9.2 to tvOS 10.0 API Diffs.md`，`General/iOS 10.0 API Diffs/` 的是 `iOS 9.3 to iOS 10.0 API Differences.md`）
  - `referencelibrary/Getting Started/Start Developing iOS Apps Today (Retired)/` 的入口甚至是 `Document Revision History.md`（`_indexes/referencelibrary/GettingStarted.md:16`）

---

## 5. 翻页链接（pager）

### 5.1 位置

**页首与页尾各一次，两处内容完全相同**。全量：2 行 25,754 个文件、0 行 9,979 个、1 行 18 个、3 行 1 个。
首个 pager 的行号（正文起算的 0-based index）：3（25,714 个，即模板位置）；index 9/14 的 52+6 个是原 HTML 自带的页面装饰（见 §5.3），不是生成器产物。

### 5.2 格式（穷尽枚举）

| 形态 | 出现次数 | 说明 |
|---|---|---|
| `[Next](…)[Previous](…)` | 42,045 | **默认形态：两个链接紧贴，中间无空格、无分隔符；Next 在前** |
| `[Next](…)` | 4,612 | 入口页（无上一页） |
| `[Previous](…)` | 4,462 | 末页（无下一页） |
| `[下一页](…)[上一页](…)` | 200 | 翻译版 |
| `[上一页](…)` / `[下一页](…)` | 41 / 41 | 翻译版单侧 |
| `[下一页](…) [上一页](…)` | 12 | **不一致**：多了一个空格 |
| `[下一页](…) · [上一页](…)` | 10 | **不一致**：加了 `·` |
| `[下一页](…)[上一页](…) ` | 4 | **不一致**：行尾多空格 |
| `[下一篇](…) [上一篇](…)` | 16 | **不一致**：第三套中文措辞 + 空格。`documentation/Cocoa/Event-Driven XML Programming Guide/XML Glossary.md:15` → `[下一篇](Document%20Revision%20History.md) [上一篇](Validation%20Tips%20and%20Techniques.md)` |
| `[Previous](…) \| [Back Up One Level](…) \| [Next](…)` | 85 | 旧 WebObjects 文档正文里的原页面导航，非模板 |
| `[Previous](…) \| [Next](…) \| [PDF](…)` | 8 | 同上 |

**第四种翻页写法（无 `[Next]/[Previous]` 标签，用章节标题当链接文字，放在文件末尾）**：入口页只有"下一章"一行；中间章节是"上一章 + 空行 + 下一章"两行（**顺序与页首 pager 相反**）：
- `documentation/Cocoa/Key-Value Coding Programming Guide/index.md:57` → `[访问对象属性](BasicPrinciples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3talkciffekqkjivcq)`
- `documentation/Cocoa/Key-Value Coding Programming Guide/BasicPrinciples.md:105-107` → `[关于键值编码](index.md#apple-…)` / 空行 / `[访问集合属性](AccessingCollectionProperties.md#apple-…)`
- `documentation/User Experience/Auto Layout Guide/index.md:83`、`ApplePay_Guide/Apple Pay Programming Guide/Configuration.md:47,49` 同型

例：`featuredarticles/Apple URL Scheme Reference/Map Links.md:15` 与 `:91` 都是
`[Next](iTunes%20Links.md)[Previous](SMS%20Links.md)`

### 5.3 特殊情况

- 目标页未被抓取时，pager 指向绝对 URL：`referencelibrary/Getting Started/About HTTP Live Streaming.md:15` → `[Next](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/AboutHTTPLiveStreaming/RevisionHistory.html)`；`samplecode/Talking Heads.md:15` 同理。
- **按资源类型的差异**：
  - `samplecode/`：21,828/21,828 页全部有 pager（首尾各一次），且全用英文。
  - `releasenotes/`：只有 43/2,322 个文件有 pager，且都指向站外 URL；**所有多页 release notes（含全部 API Diffs）完全没有 pager**。
  - `qa/`：0 个 pager。
  - `recipes/`、`ApplePay_Guide/`：0 个模板 pager（ApplePay 用的是"带标题的上/下页链接"放在正文末两行，见 `ApplePay_Guide/Apple Pay Programming Guide/Configuration.md:47` 与 `:49`）。
  - `LucidDreams/`：40/40 全部有。

---

## 6. 索引层 `_indexes/`

**索引文件没有 YAML frontmatter**，第一行就是 `# 标题`。

### 6.1 通用骨架

```
# <标题>
                                     ← 空行
> 导航：[总目录](<…/>README.md)[ · [<type>](../<type>.md)]
                                     ← 空行
共 <N> 份文档。
                                     ← 空行
<分组与条目，段落间一律空一行>
```

`_indexes/documentation.md:1-5`：
```
# documentation

> 导航：[总目录](../README.md)

共 598 份文档。
```
`_indexes/documentation/Cocoa.md:1-5`：
```
# documentation / Cocoa

> 导航：[总目录](../../README.md) · [documentation](../documentation.md)

共 120 份文档。
```
计数措辞恒为 `共 <数字> 份文档。`（中文句号），分组标题恒为 `（<数字> 份）`（全角括号，数字与 `份` 之间一个半角空格）。

### 6.2 文档条目行（12,363 行全部匹配同一语法）

```
- **[<title>](<相对路径>)** — <resource_type> · <published>，<platform>[ · <technology>][，<N> 页]
```

- `— ` 是 em dash + 空格，两侧各一个半角空格；`resource_type` 与 `published` 之间是 ` · `；`published` 与 `platform` 之间是 **全角逗号 `，`（无空格）**。
- `technology` 为 `null` 时整段（含 ` · `）省略。
- 页数为 1 时整段（含 `，`）省略；否则 `，<N> 页`。
- `title` 用文档的 frontmatter `title`（已翻译的用中文）；路径始终是英文实际路径。

实例：
- `_indexes/by-type/guide.md:9` → `- **[CloudKit Web Services Reference](../../documentation/Data%20Management/CloudKit%20Web%20Services%20Reference/index.md)** — Guide · 2016-06-13，CloudKit JS，32 页`
- `_indexes/by-type/guide.md:15` → `- **[Accessibility Programming Guide for iOS](../../documentation/User%20Experience/Accessibility%20Programming%20Guide%20for%20iOS/Introduction.md)** — Guide · 2012-02-16，tvOS|iOS · UIKit，4 页`
- `_indexes/by-type/guide.md:13` → `- **[A Short Practical Guide to Blocks](../../featuredarticles/A%20Short%20Practical%20Guide%20to%20Blocks.md)** — Guide · 2010-08-15，watchOS|iOS|macOS`（单页，无页数段）
- `_indexes/documentation/Cocoa.md:11` → `- **[归档与序列化编程指南](../../documentation/Cocoa/Archives%20and%20Serializations%20Programming%20Guide/Introduction.md)** — Guide · 2012-07-17，watchOS|tvOS|iOS|macOS · Foundation，10 页`

**子页条目**（缩进 2 空格，无粗体，无元信息）：
```
  - [<页面显示名>](<相对路径>)
```
`_indexes/documentation/Cocoa.md:12` → `  - [Object Graphs](../../documentation/Cocoa/Archives%20and%20Serializations%20Programming%20Guide/Object%20Graphs.md)`
samplecode 的子页显示名是**原始相对路径（带 `/`）**：`_indexes/samplecode.md:12` → `  - [Classes/ABUIGroupsAppDelegate.h](../samplecode/ABUIGroups/Classes-ABUIGroupsAppDelegate.h.md)`

**哪些索引列子页**（统计）：

| 索引 | 子页行 | 文档行 |
|---|---|---|
| `_indexes/<type>.md` | 有 | 有 |
| `_indexes/<type>/<Cat>.md` | 有 | 有 |
| `_indexes/by-type/*.md` | **0** | 有 |
| `_indexes/by-platform/*.md` | **0** | 有 |

子页顺序 **不是** pager 顺序（`Document Revision History` 常出现在列表中间）。

### 6.3 各层索引的分组结构

#### `_indexes/<type>.md` —— 有分类的类型（documentation / qa / releasenotes / referencelibrary）
只列分类，不列文档（除未分类部分）：
```
## [<分类目录名>](<type>/<分类id>.md)（N 份）
```
`_indexes/documentation.md:7` → `## [3D Drawing](documentation/3DDrawing.md)（3 份）`
之后（仅 documentation 有）：
- `## 文档`（`_indexes/documentation.md:97`）—— 该类型下**无分类**的文档，用 §6.2 条目 + 子页
- `## 未编入索引的页面`（`_indexes/documentation.md:244`）—— 指向 `_unindexed/` 的裸链接列表：
  `- [WebObjects Release 3.0](../_unindexed/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DeltaDoc/DeltaDoc.md)`
  （只有 `_indexes/documentation.md` 有这一段。）

#### `_indexes/<type>.md` —— 无分类的类型（samplecode / featuredarticles / recipes / ApplePay_Guide / LucidDreams）
```
## 文档
[### <平台>（N 份）]      ← 仅当文档总数 ≥ 20 时按平台分组
- **[…]** …
  - […]
```
`_indexes/samplecode.md:7,9` → `## 文档` / `### iOS（258 份）`（平台分组，只有 `###`，无 `####`）
`_indexes/featuredarticles.md:7-8`（7 份 < 20）→ `## 文档` 后直接列条目
`_indexes/ApplePay_Guide.md:7-8`、`_indexes/recipes.md:7-8` 同理

#### `_indexes/<type>/<Cat>.md`（二级分类索引，45+37+24+1 = 107 个）
```
# <type> / <分类目录名>
> 导航：[总目录](../../README.md) · [<type>](../<type>.md)
共 N 份文档。
[## <平台>（N 份）]        ← 仅当 N ≥ 20；否则直接列条目
- **[…]** …
  - […]
```
- 有分组：`_indexes/documentation/Cocoa.md:7` → `## iOS（40 份）`；`_indexes/qa/hw.md:7` → `## macOS（84 份）`（即使只有一个平台也照写）
- 无分组：`_indexes/documentation/3DDrawing.md`（3 份）从 `:7` 直接是条目行
- 阈值经验证：全部 107 个文件都满足 "N ≥ 20 ⇔ 有 `##` 平台分组"（实测无反例）

#### `_indexes/by-type/*.md`（4 个：`guide.md`、`qa.md`、`release-note.md`、`sample-code.md`）
```
# <Resource Type>            e.g. "# Guide"、"# Sample Code"、"# Release Note"、"# QA"
> 导航：[总目录](../../README.md)
共 N 份文档。
## <平台>（N 份）             ← 唯一一层分组，永不再细分
- **[…]** …                  ← 不列子页
```
文件名 = resource_type 的 kebab-case：`Guide`→`guide`、`Sample Code`→`sample-code`、`Release Note`→`release-note`、`QA`→`qa`。
`_indexes/by-type/sample-code.md:1,7,269,1751,1762,1767,1775` → `# Sample Code` / `## iOS（259 份）` / `## macOS（1479 份）` / `## Safari（8 份）` / `## tvOS（2 份）` / `## watchOS（5 份）` / `## Xcode Developer Tools（8 份）`

#### `_indexes/by-platform/*.md`（8 个）
最深，共 4 层：
```
# <Platform>                                        ← e.g. "# tvOS"、"# Xcode Developer Tools"
> 导航：[总目录](../../README.md)
共 N 份文档。
## <顶层类型>（N 份）                                 ← e.g. "## documentation（174 份）"
### [<分类目录名>](../<type>/<分类id>.md)（N 份）      ← 有分类的类型
#### <Topic>（N 份） / #### 未分类主题（N 份）         ← 仅当该分类组 ≥ 20 份
### 其他                                             ← 该类型下无分类的文档，标题无计数
#### <Topic>（N 份）
### <Topic>（N 份）                                   ← 无分类的类型（如 samplecode）直接按 topic 分
- **[…]** …                                          ← 不列子页
```
citations：
- `_indexes/by-platform/tvos.md:1,7,9,11` → `# tvOS` / `## documentation（1 份）` / `### [General](../documentation/General.md)（1 份）` / 条目
- `_indexes/by-platform/ios.md:52,54` → `### [Cocoa](../documentation/Cocoa.md)（40 份）` / `#### Data Management（27 份）`
- `_indexes/by-platform/ios.md:117` → `### [Core Foundation](../documentation/CoreFoundation.md)（11 份）` 后**没有** `####`（11 < 20）
- `_indexes/by-platform/macos.md:1675,1677` → `### 其他` / `#### Apple Applications（4 份）`
- `_indexes/by-platform/macos.md:70,202` → `#### 未分类主题（30 份）`（= `topic: null`）
- `_indexes/by-platform/ios.md:7,9` → `## ApplePay_Guide（1 份）` 后直接条目（无分类类型且 < 20）

阈值实测：`###` 分类组带 `####` topic 子组的最小 N = 21，不带的最大 N = 19 → **阈值 20**。

### 6.4 索引分组用的"主平台"（与 §1.3 的书写顺序不同）

一个文档只进入 **一个** `by-platform` 文件、在分类索引里也只进 **一个** `## <平台>` 组。43 种 `platform` 组合到主平台的映射完全无歧义，等价于按下述优先级取第一个命中：

```
iOS > macOS > watchOS > tvOS > Xcode Developer Tools > Java > Safari
     > CloudKit JS > Safari (Mobile) > iAd Producer > iAd System JS
```

抽样验证：`watchOS|tvOS|iOS|macOS`→iOS，`Safari (Mobile)|Safari|iOS|macOS`→iOS，`watchOS|macOS`→macOS，`Java|macOS`→macOS，`Xcode Developer Tools|macOS`→macOS，`watchOS|Xcode Developer Tools`→watchOS，`watchOS|tvOS|Xcode Developer Tools`→watchOS，`Safari|Xcode Developer Tools`→Xcode Developer Tools，`CloudKit JS|iOS`→iOS。
`Safari (Mobile)` / `iAd Producer` / `iAd System JS` 永不成为主平台（README 里也没有它们的入口）。

### 6.5 索引文件清单（128 个）

```
_indexes/{ApplePay_Guide,LucidDreams,documentation,featuredarticles,qa,recipes,referencelibrary,releasenotes,samplecode}.md   (9)
_indexes/by-platform/{cloudkit-js,ios,java,macos,safari,tvos,watchos,xcode-developer-tools}.md                                (8)
_indexes/by-type/{guide,qa,release-note,sample-code}.md                                                                      (4)
_indexes/documentation/*.md   (45)   ← 文件名用分类 id（驼峰），如 3DDrawing.md、WindowsViews.md
_indexes/qa/*.md              (37)   ← amt_pe.md（保留下划线）、hw.md、qa2001.md …
_indexes/releasenotes/*.md    (24)
_indexes/referencelibrary/GettingStarted.md (1)
```

### 6.6 `_unindexed/index.md`

无 frontmatter，第一行就是导航行（这是唯一这样做的文件）：
```
> 导航：[总目录](../README.md) · 未编入索引的页面

# Apple Developer Archive

- [12-inch PowerBook G4 Developer Note](../documentation/Hardware/12-inch%20PowerBook%20G4%20Developer%20Note.md)
…
```
（`_unindexed/index.md:1,3,5`）—— 按标题排序的全库页面裸链接清单，同标题重复出现（每页一行）。

---

## 7. README.md

无 frontmatter。完整结构（`README.md:1-…`，共 6 段）：

```
# Apple Developer Documentation Archive（Obsidian 版）

<一段说明>

## 统计

- 文档：4121 份
- 页面：35753 个 Markdown 文件
- 来源：https://developer.apple.com/library/archive/navigation/

## 按归档分类浏览

- [<顶层目录名>](_indexes/<顶层目录名>.md)（N 份）      ← 9 行

## 按资源类型浏览

- [<Resource Type>](_indexes/by-type/<kebab>.md)（N 份）  ← 4 行

## 按平台浏览

- [<Platform>](_indexes/by-platform/<kebab>.md)（N 份）   ← 8 行

## 使用提示

- 每页顶部有导航面包屑：总目录 → 分类索引 → 所属文档。
- 打开右侧「反向链接」面板可查看哪些页面引用了当前页。
- 「关系图谱」可浏览整个归档的链接结构。
- 图片保存在每份文档目录下的 attachments/ 中，离线可读。
```

措辞细节：
- 统计三项用 `- 文档：`/`- 页面：`/`- 来源：`（全角冒号），数值与单位之间半角空格（`4121 份`、`35753 个 Markdown 文件`）。
- 三个浏览区的列表项一律 `- [标签](路径)（N 份）`。
- "按归档分类浏览" 的 9 项按目录名 **ASCII 序**排（`ApplePay_Guide`、`LucidDreams` 在前，然后小写的 `documentation`…）。
- 文件以单个 `\n` 结束。

**README 里的两处不实/不一致（生成器要注意）**：
1. 第 3 行声称"文档间链接为 wiki 链接"——**这是假的**，全库没有一个 `[[…]]` wiki 链接（见 §9）。
2. "页面：35753 个 Markdown 文件" 与实测的 35,752 个文档页、35,884 个 `.md` 都对不上（差 1 / 差 131）。

---

## 8. 正文 Markdown 约定

### 8.1 标题层级

全量标题计数：`#` 36,003、`##` 28,952、`###` 21,624、`####` 11,811、`#####` 2,757、`######` 32。
每页第一个标题的层级：`#` 32,234、`##` 1,817、`###` 373、`####` 237、`#####` 48、无标题 343。

- **主流：正文首个标题是 `# <本页标题>`**，与 frontmatter `title` 一致。`documentation/Windows Views/Collection View Programming Guide for iOS/Collection View Basics.md:17` → `# Collection View 基础`
- 源自 `index.html` / `_index.html` 的入口页常从 `##` 开始：`ApplePay_Guide/Apple Pay Programming Guide/index.md:16` → `## About Apple Pay`；`documentation/3D Drawing/Metal Best Practices Guide/RevisionHistory.md:16` → `## Document Revision History`
- **`#### Contents:` 目录块出现在它所链接的 `###` 章节之上**（层级"倒挂"，属原 HTML 结构）：`releasenotes/CFNetwork Framework Release Notes.md:22` → `#### Contents:`，`:29` → `### CFError`
- `samplecode/` 几乎只用 `#`（源码页 = 一个 `#` + 一个代码块）。
- 部分"已退休"页面有两个 `#`（横幅 + 真标题）：`referencelibrary/Getting Started/Start Developing iOS Apps Today (Retired)/Configuring the View.md:17` → `# Retired Document`，`:21` → `# Configuring the View`
- **`#` 与标题文字之间可能不止一个空格**（`documentation/` 内统计）：`##` + 2 空格 1,032 次、`####` + 2 空格 375、`###` + 2 空格 309、`#` + 2 空格 288、`#` + 3 空格 259。例：`documentation/Carbon/Programming with the Appearance Manager/About the Appearance Manager.md:22` → `#   About the Appearance Manager`
- **跳级**：`documentation/` 内 597 个文件（6.5%）存在 ≥2 级的跳跃。
- **用粗体冒充标题**也存在：`documentation/Security/Secure Coding Guide/Validating Input and Interprocess Communication.md:201` → `**__Distributed Objects__**`；行内式小标题 `__Great battery life.__ As energy efficiency goes down…`（`documentation/Performance/Energy Efficiency Guide for iOS Apps/index.md:24`，106 处）；标题标记完全丢失变成普通段落（`documentation/Networking/Network Services Location Manager (Legacy)/NSL32.md:17`）。
- **旧 WebObjects/Carbon 页面的页首装饰**：`__PATH__` 单独一行或 `__PATH__Documentation > [Carbon](…) > User Experience`，随后一行 `---`（**正文里的水平线，解析 frontmatter 时不要误判**）。`documentation/Legacy Technologies/WebObjects 4.0 Developer Documentation/EOSortOrdering.md:15-24`、`documentation/Carbon/Programming with the Appearance Manager/About the Appearance Manager.md:16-22`

### 8.2 图/表/清单标题

格式：`__<Figure|Table|Listing> <编号>__` + **两个 U+00A0（不换行空格）** + 说明文字。

- `documentation/Device Drivers/Accessing Hardware From Applications/Finding and Accessing Devices.md:111`
  实际字节：`'__Figure 3-1__\xa0\xa0The I/O Registry Explorer application, showing various keys…'`
- `qa/Adding Bluetooth LE MIDI Support/Adding Bluetooth LE MIDI Support.md:54` → `__Listing 1__` + `\xa0\xa0` + `Presenting a CABTMIDICentralViewController`

分隔符统计（全库）：`\xa0\xa0` 8,887 次、**无分隔符 1,004 次**、标题独占一行（后跟空行）233 次、单个半角空格 36 次、两个半角空格 9 次。
`documentation/` 内的细分（含中文标签）：`\xa0\xa0` 7,915、无分隔 915、两个半角空格 122、**U+3000（全角空格）90**、单个半角空格 30。

**中文标签映射**：`Figure`→`图`、`Table`→`表`、`Listing`→`清单`，编号仍是 ASCII，标签与编号间一个半角空格：
- `documentation/Windows Views/View Programming Guide for iOS/Views.md:61` → `__表 3-1__` + `\xa0\xa0` + `几个关键视图属性的用途`
- `documentation/Windows Views/View Programming Guide for iOS/Views.md:82` → `__图 3-1__` + `\xa0\xa0` + …
- `documentation/Windows Views/View Programming Guide for iOS/Views.md:103` → `__清单 3-1__` + `\xa0\xa0` + …
- `documentation/Cocoa/Key-Value Coding Programming Guide/BasicPrinciples.md:26` → `__清单 2-1__` + **U+3000** + `` `BankAccount` 对象的属性 ``（字节 `e3 80 80`）

标题与图片之间**有时空一行有时不空**：`Views.md:82/83/84`（空一行）vs `documentation/Performance/Energy Efficiency Guide for iOS Apps/FundamentalConcepts.md:54/55`（不空）。
**无分隔符的例子**：`documentation/Xcode/Markup Formatting Reference/AddingMarkup.md:30` → `__Figure 3-1__Single line comment example`；`documentation/General/App Extension Programming Guide/Share.md:98` → `__Listing 12-1__An example implementation of \`didSelectPost\``
**不一致但可预测**：该差异**按文档一致**——529 个文档目录全用 `\xa0\xa0`，32 个全部无分隔符。生成器默认用 `\xa0\xa0`。
强调标记用 `__…__`（10,019 次），`**…**` 仅 10 次。

### 8.3 表格

管道表，**行首行尾都有 `|`，单元格两侧各一个空格**。存在两种互不相容的表头写法：

**A 型（无分隔行，表头用 `__粗体__`）** —— 主流，GFM 下渲染不正常但仓库里就是这样：
```
| __Date__ | __Notes__ |
| 2013-07-29 | Updated for iOS 6.0. … |
```
`documentation/3D Drawing/SceneKit Programming Guide/Document Revision History.md:21-23`；`qa/Adding Bluetooth LE MIDI Support/Adding Bluetooth LE MIDI Support.md:106-107`；`samplecode/ABUIGroups/Document Revision History.md:21-22`

**B 型（标准 GFM，有 `| --- | --- |`）**：
```
| Date | Notes |
| --- | --- |
| 2017-03-27 | Updated Display Management best practices. |
```
`documentation/3D Drawing/Metal Best Practices Guide/RevisionHistory.md:20-23`；`ApplePay_Guide/Apple Pay Programming Guide/RevisionHistory.md:20-22`
中文版：`documentation/Cocoa/Core Data Programming Guide/RevisionHistory.md:20-21` → `| 日期 | 说明 |` / `| --- | --- |`

全量：表格行 1,025,853 行，分隔行 245,244 行。
`documentation/` 内 3,509 个含表格的文件里，**1,205 个没有任何 `| --- |` 行**（34%）。Document Revision History 页更极端：518 个里只有 51 个（10%）带分隔行。
- **对齐**：全库**没有**任何冒号对齐写法（`| :--- |`、`| ---: |`、`| :---: |` 均 0 次）。分隔行恒为 `| --- | --- |`（正好 3 个连字符，两侧各一空格）。
- **单元格内的多段落被压成一行，段落边界变成两个半角空格**（不用 `<br>`；全库 `<br>` 仅 58 次且都在 HTML 代码示例里）。`documentation/Windows Views/View Programming Guide for iOS/Views.md:65`
- **空单元格占位行**：`|  | Added information about … |`（`documentation/General/Concurrency Programming Guide/Document Revision History.md:25`，日期列留空表示续行）；全空行 `|  |  |  |` 出现 1,896 次。
- **连表头都没有的裸数据表**：`documentation/Performance/Energy Efficiency Guide for iOS Apps/FundamentalConcepts.md:65-68`
- 表头是否加粗不一致（DRH 页）：`| __Date__ | __Notes__ |` 460 · `| Date | Notes |` 23 · `| __日期__ | __说明__ |` 31 · `| 日期 | 说明 |` 5。
**布局表遗留**：旧页面把整篇内容塞进一个巨大单元格，表头是一串空单元格 `|  |  | … |` + 对应的 `| --- | … |`（`qa/hw/A SCSI little secret/hw81.md:22-24` 是 25 列）。samplecode 入口页的元信息表也是 `|  |  |` + `| --- | --- |` 起头（`samplecode/ABUIGroups/ABUIGroups.md:19-23`）。
API Diffs 的变更表用 From/To 行，代码放在**单元格内的行内三反引号**里（`releasenotes/General/tvOS 10.0 API Diffs/UIKit Changes for Objective-C.md:27-30`）。

### 8.4 代码块

- **一律三反引号栅栏，独占一行；从不缩进式，从不 `~~~`。**
- 语言标注**可选**，全量：无标注 63,882、`objc` 12,185、`c` 5,983、`swift` 1,645、`xml` 145、`shell` 86、`json` 15、`text` 3、`bash` 3、`sh` 3、`perl` 1。**没有 `objective-c`、`javascript`、`python` 等。**
- 语言标注与扩展名不是严格映射（同一扩展在不同文档里标注不同）。samplecode 的实测倾向：
  `.m`→`objc`(4057)、`.mm`→`objc`(224)、`.h`→`objc`(3457)/`c`(2197)/无(906)、`.c`→`c`(2434)、`.cpp`/`.cp`→`c`、`.r`(Rez)→`c`、`.metal`→`c`、`.swift`→`swift`(852)、`.sdef`→`xml`、`.txt`→无(962) 或 `shell`(31)、`.command`→`sh`、`.java`/`.js`/`.py`/`.md`/`.html`/`.css`/`.applescript`→无标注。
  例：`samplecode/DateCell/main.m.md:19` → ```` ```objc ````；`samplecode/7Edit/Source-DebugUtils.c.md:19` → ```` ```c ````；`samplecode/ABUIGroups/ReadMe.txt.md:19` → ```` ``` ````
- **不存在** `.plist` / `.xib` / `.storyboard` / `.pch` / `Makefile` 页面。
- 旧页面里代码有时被压成**行内**三反引号且换行被折成空格（`qa/qd3d/-28482 Errors When Selecting Markers.md:36`、`recipes/Repositories Organizer Help/Setting Up a Git Repository.md:30`）。
- **栅栏可以在引用块里**（2,212 行，集中在 WebObjects 遗留文档）：`documentation/Legacy Technologies/WebObjects 4.0 Developer Documentation/EOSortOrdering.md:58-66`，每行以 `> ` 开头，`> ``` ` 开栅栏。
- **栅栏可以在列表项里**（缩进 2 空格）：`documentation/Xcode/Markup Formatting Reference/AddingMarkup.md:22-24` → `- ``` ` / `  single line comment marker  markup formatted text` / `  ``` `
- **第三种（损坏的）代码呈现：代码被渲染成"有序列表 + 行内代码"**，10,367 行分布在 266 个文件；列表编号来自源文件行号，因此源码空行处编号有断口：
  `documentation/Cocoa/Key-Value Coding Programming Guide/BasicPrinciples.md:28-32`
  ```
  1. `@interface BankAccount : NSObject`
  3. `@property (nonatomic) NSNumber* currentBalance; // 一个属性`
  4. `@property (nonatomic) Person* owner; // 对一关系`
  5. `@property (nonatomic) NSArray< Transaction* >* transactions; // 对多关系`
  7. `@end`
  ```
  单行代码同样如此：`BasicPrinciples.md:36` → `` 1. `[myAccount setCurrentBalance:@(100.0)];` ``
- 缩进式（4 空格）代码块也存在（`documentation/` 内 35,687 行匹配），主要在 HTML / 驱动类文档中。

### 8.5 列表

- 无序：**一律 `- `**（4,000 文件抽样、排除代码块后：`- ` 10,323 次，`* ` 4 次，`+ ` 9 次——后两者基本是残留噪声）。
- 嵌套缩进 **2 空格**（530 次），也有 3/4 空格（88 / 72 次）。
- 有序：`1. ` 形式（点号；`)` 仅 7 次），编号**真实递增**而非全为 `1.`（`1.` 起始 540 次 vs 非 1 起始 2,788 次）。
- 有序列表的续行/嵌套内容缩进 **3 空格**（对齐 `1. ` 之后）：`referencelibrary/Getting Started/Start Developing iOS Apps Today (Retired)/Configuring the View.md:34,36`
- **嵌套缩进宽度整体不一致**（`documentation/` 内）：2 空格 2,481 · 3 空格 1,009 · 4 空格 580 · 6 空格 158 · 1 空格 93 · 5 空格 61。无序列表标记全量 `- ` 67,734，`+ ` 374（代码/diff 示例内），`* ` 19。有序 `1.` 25,774，`1)` 仅 18。
- 列表项下的续行段落：2 空格缩进 + 前后空行。`documentation/General/Concurrency Programming Guide/Glossary.md:19-21` → `- __application__` / 空行 / `  A specific style of [program](#apple-…) that displays a graphical interface to the user.`
- **空列表项**存在：`documentation/Networking/Network Services Location Manager (Legacy)/NSL32.md:21` 就是一行 `- `，说明文字被孤立在 `:23`。
- 少数旧文档**保留了源 HTML 的硬折行**（现代页一律一段一行不折）：`documentation/Quick Time/QuickTime 5.md:20-29`

### 8.6 强调与行内代码

- **粗体 `__…__`**（24,196 次，排除代码块），`**…**` 1,900 次（主要出现在 `releasenotes/` 与翻译过的文件）。
- **斜体 `_…_`**（43,982 次），`*…*` 1,350 次。
- 行内代码单反引号，大量用于 API 名/路径/键名。
- 字面星号会被转义：`qa/qd3d/-28482 Errors When Selecting Markers.md:52` → `\*`、`:74` → `_\* Required information_`
- **排版字符保留原始 Unicode，不转成实体**：弯引号 `’`（如 `documentation/Xcode/What's New in Xcode — Archive/What’s New in Xcode - Archive.md` 文件名里就有）、em dash `—`、`…`、`&`（裸写）。
- **U+00A0 大量存在**（全库 50,508 个，`documentation/` 内 39,351 个）：图表标题分隔符、`## Q:` 之后、表格单元格内。
- `documentation/` 内构件计数：行内代码 185,800 · `__bold__` 82,489 · `_italic_` 35,082 · `**bold**` 14,775 · `*italic*` 5,080。`**` 集中在 Device Drivers 与旧 Quick Time 文档，以及 `**__X__**` 双包裹惯用法。
- 排版字符原始 Unicode 计数（`documentation/`）：弯单引号 `’‘` 28,069 · 弯双引号 `“”` 15,641 · em dash `—` 11,697 · `…` 732 · U+3000 93。
- **HTML 实体基本已全部解码**。`documentation/` 内残留总数极少：`&amp;` 18、`&lt;` 11、`&gt;` 10、`&quot;` 7、`&nbsp;` 6、`&deg;` 4、`&apos;` 3、`&#9;` 2、`&#231;` 2、`&#13;` 2、`&#10;` 2；**`&#8217;` 零次**。全部残留都合理地位于代码示例中或在讨论实体本身：`documentation/Device Drivers/Writing PCI Drivers/Writing a Driver for a PCI Device.md:65`、`documentation/Cocoa/Event-Driven XML Programming Guide/XML Glossary.md:92`。
- **书名/文档名的写法**：英文页用斜体包住链接 —— `documentation/General/Concurrency Programming Guide/Introduction.md:45` → `…see _[Threading Programming Guide](../../Cocoa/Threading%20Programming%20Guide/Introduction.md#apple-…)_.`；中文页用《》包住链接 —— `documentation/Cocoa/Key-Value Coding Programming Guide/index.md:52` → `…具体参阅《[键值观察编程指南](../Key-Value%20Observing%20Programming%20Guide/…)》。`

### 8.7 提示/警告框

三种写法并存（**不一致**）：

**(a) 主流：普通段落 + `__Note:__` 行内前缀，不用引用块，不用 admonition。分隔符是半角空格，不是 NBSP**（与图表标题相反）：2 空格 121 次、无分隔 102 次、1 空格 39 次。
- `documentation/Security/Secure Coding Guide/Validating Input and Interprocess Communication.md:199` → `__Note:__ Mach messaging in macOS is not a supported API. …`
- `documentation/Security/Secure Coding Guide/Race Conditions and Secure File Operations.md:191` → `__Note:__` + 两个半角空格 + `For maximum portability…`（字节 `5f5f 4e6f 7465 3a5f 5f20 20…`）
- 标签用词：`Note:`（主流）、`Important:`（~6）、`Warning:`（~10）、`Tip:`。只有 13 处缩进在列表项内，只有 5 处被引用块包裹（`> __Note:__`）。
- **callout 几乎从不翻译**：全库唯一一处中文 callout 是 `documentation/Cocoa/Error Handling Programming Guide/Error Objects, Domains, and Codes.md:133` → `__注意：__` + **U+3000** + `下面的例子…`；其他译文页把提示揉进正文，不留标记。

**(b) GitHub alert：存在但 100% 为空。** `documentation/` 内 464 个 `[!NOTE]/[!IMPORTANT]/[!WARNING]/[!TIP]` 标记分布在 197 个文件（全在现代 `Xcode/` 组），实测 431 对全部是标记行后紧跟一行 `> ` 然后什么都没有。
- `documentation/Xcode/Markup Formatting Reference/AddingMarkup.md:62-64` → `> [!NOTE]` / `> ` / 空行
- `documentation/Xcode/Xcode Server API Reference/index.md:20`、`documentation/Xcode/Asset Catalog Format Reference/AssetTypes.md:26`
- 其他类型同样：`ApplePay_Guide/Apple Pay Programming Guide/Configuration.md:44-45`；`releasenotes/Adding Complications to the Gallery.md:18-19`（27+22+1 处）

**(c) 行内粗体前缀（非 Note 语义）**：`__Important:__ This is a preliminary document…`（`releasenotes/Mac OSX/API Changes in Snow Leopard/API Changes in Snow Leopard.md:22`、`qa/qd3d/-28482 Errors When Selecting Markers.md:20`）。

**术语表（glossary）复用同一个"行首粗体"形状，导致 `__Bold.__ text` 在语义上歧义**（callout / 小标题 / 术语条目三者同形）。两种术语表布局：
- 列表项 + 缩进定义：`documentation/General/Concurrency Programming Guide/Glossary.md:19-21`
- 段落 + 全角冒号（冒号在粗体**外**）：`documentation/Cocoa/Event-Driven XML Programming Guide/XML Glossary.md:21` → `__原子值（atomic value）__：具有 XML Schema 标准所定义简单类型的值。…`

### 8.8 锚点

- **正文里从不定义锚点**：全库没有 `<a name=`、`<a id=`、`{#…}`、`^id` 之类的标题 id 定义。`#apple-…` 全部是**悬空锚点**（Obsidian/GitHub 会落到文件顶部）。
- 锚点串的构造（已完全逆向）：
  ```python
  anchor = 'apple-' + base64.b32encode(apple_ref.encode()).decode().lower().rstrip('=')
  # apple_ref 形如 '//apple_ref/doc/uid/TP40012334-CH5-SW1' 或 '//apple_ref/doc/uid/TP40003577'
  ```
  验证：`base32('//apple_ref/doc/uid/TP40012334-CH5-SW1').lower().rstrip('=')` == `f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqnjnknltc`，正是 `documentation/Windows Views/Collection View Programming Guide for iOS/Collection View Basics.md` 中 `Creating%20Custom%20Layouts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmzufvbuqnjnknltc` 的锚点。
  另两例：`apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzx` ← `//apple_ref/doc/uid/TP40003577`；`apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2donrufvbuqmrnknltc` ← `//apple_ref/doc/uid/TP40014764-CH2-SW1`。
- 全库 `#apple-` 锚点用法 110,316 次（其中 41,923 次是纯同页 `#apple-…`）。**唯一的锚点前缀就是 `#apple-`**，没有别的形态。
- 页内目录也用这种锚点：`featuredarticles/A Short Practical Guide to Blocks.md:24-25`

### 8.9 图片

```
![<alt>](<相对路径>)
```
- alt 文本来源（优先级递降）：HTML 的 `alt` 属性 → 原始 `src` 相对路径 → 带前缀的变体。观察到的形态：
  - 真实 alt：`documentation/Cocoa/…` → `![Browser example](attachments/art/browser.gif)`、`![NSConnections between a server and two client processes](attachments/Concepts/Art/connections.gif)`
  - 原 src 路径当 alt：`![../Art/copyApplicationWindow.jpg](attachments/Art/copyApplicationWindow.jpg)`、`![Art/cv_layout_basics_2x.png](attachments/Art/cv_layout_basics_2x.png)`
  - `image: ` 前缀：`ApplePay_Guide/Apple Pay Programming Guide/Configuration.md:42` → `![image: ../Art/enable_apple_pay.png](attachments/Art/enable_apple_pay_2x.png)`
  - `Figure N ` 前缀：`qa/Testing an Automator Action Xcode Project/Testing an Automator Action Xcode Project.md:30`
  - 翻译过的中文 alt：`![日历图标](attachments/Art/iCal.png)`、`![图像： ../Art/…](…)`
  - **导航装饰图**（原 HTML 的上/下/目录按钮）：`![Table of Contents]` 2,028 次、`![Previous]` 530、`![Next]` 516、`![Up]` 370、`![bullet]` 205
  - 真实描述型 alt（长句）：`documentation/Carbon/Carbon Overview/Carbon Basics.md:29` → `![Illustrates the programming layers on Mac OS X, from the kernel environment at the bottom to the application frameworks at the top.](attachments/Art/osxlayers.gif)`
- **`attachments/` 子目录大小写按原样保留**（`documentation/` 内统计）：`attachments/Art/*` 3,477 · `attachments/art/*` 1,436 · `attachments/images/*` 1,068 · `attachments/Topics/*` 334 · `attachments/Concepts/*` 235，另有按书命名的 `attachments/DiscoveringWO/*`、`attachments/EOControlRef/*` 等。
- **没有尺寸提示、没有 `{width=…}`、没有 title 属性。** `<img>` 只在 HTML/Safari 类文档的代码示例里出现（约 5 个文件）。
- **@1x/@2x 成对的 `<img>` 常被压成同一行的两个完全相同的图片链接**：
  `releasenotes/Mac OSX/What's New in macOS/OS X Lion v10.7.md:35` → `![../Art/syncing_intro.jpg](attachments/Art/syncing_intro.jpg)![../Art/syncing_intro.jpg](attachments/Art/syncing_intro.jpg)`
- PDF 源图被换成 PNG：`![image: Art/firstViewController.pdf](attachments/Art/firstViewController.png)`（`releasenotes/Miscellaneous/Converting to Storyboards Release Notes/Converting to Storyboards Release Notes.md:99`）
- 残留 HTML `<img>` 极少（个别文档，如 `documentation/Internet Web/Safari CSS Visual Effects Guide/Using Masks.md` 5 处）。
- **退化的图片行**：有些图片被压成裸 `!` 或 `!!`（图片文件仍在 `attachments/` 里但无引用）。`qa/Adding Bluetooth LE MIDI Support/Adding Bluetooth LE MIDI Support.md:40` → `!!`，`:44` → `!`。qa 里 225 行、referencelibrary 101 行。**新生成器不要复现这个 bug。**

### 8.10 Document Revision History

两种形态：
- **独立页**（多页文档）：文件名 `Document Revision History.md` 或 `RevisionHistory.md`（stem 派生）。结构：pager → `# Document Revision History`（或 `## `）→ `This table describes the changes to _<文档标题>_.` → 表格 → pager。
  `documentation/3D Drawing/SceneKit Programming Guide/Document Revision History.md:15-25`
  `documentation/3D Drawing/Metal Best Practices Guide/RevisionHistory.md:16-23`
- **内嵌**（现代 qa，536/536）：正文末尾 `---` 水平线 → `#### Document Revision History` → 表格。
  `qa/How do I work-around an issue where some lines in my Core Text output have extra.md:51,53,55-56`

`documentation/` 内 518 个 Revision 页的统计：
- 文件名：`Document Revision History.md`（多数）、`RevisionHistory.md`、`OSXAXRevisionHist.md`（stem 派生）
- 标题：`# Document Revision History` 460 · `# 文档修订历史` 32 · `## Document Revision History` 23 · `## 文档修订历史` 3（层级跟随该页的 A/B 变体）
- 引导句：`This table describes the changes to _<书名>_.` / `下表说明了《<书名>》的变更。`
- 列固定两列：`Date`/`Notes` 或 `日期`/`说明`；日期 `YYYY-MM-DD`，**新的在前**
- **只有 51/518（10%）带 `| --- |` 分隔行**
- 完整示例（带分隔行）：`documentation/Mac Automation Scripting Guide/RevisionHistory.md:16-22`；（不带分隔行）`documentation/General/Concurrency Programming Guide/Document Revision History.md:17-25`
- 作为末章，其 pager 只有 `[Previous]`

---

## 9. 链接

### 9.1 链接种类统计（全量）

```
339,379  https://developer.apple.com/…      站外绝对链接
288,054  相对 .md 链接
 41,923  同页 #apple-… 锚点
 14,111  https://www.apple.com/…
  9,242  attachments/… 图片
    495  https://help.apple.com/…
    342  applescript://…
    329  ../…/_unindexed/…
    ~1k  其他站外（khronos.org、opengl.org、github.com、w3.org、ietf.org …）
```

### 9.2 URL 编码规则（已完全逆向）

内部链接路径 = `urllib.parse.quote(相对路径)`（Python 默认 `safe='/'`）。298,073 个链接中 297,670 个能被这一行完美复现（失配的 403 个全是 `mailto:`/`ftp:`/`applescript:`/`BugDB:` 之类的非文件 URL 和 3 处漏编码的逗号）。

- 空格 → `%20`（267,680 次，**不是 `+`，不是保留空格**）
- `,` → `%2C`（3,175） · `(` → `%28`、`)` → `%29`（各 1,477） · `'` → `%27`（941） · `+` → `%2B`（590） · `&` → `%26`（18）
- `’`(U+2019) → `%E2%80%99`；中文 → UTF-8 逐字节百分号编码（`%E6%96%87%E7%A8%BF…`）
- **不编码**：`-`、`_`、`.`、`~`、字母数字、`/`
- `.md` 扩展名保留；锚点直接附在 `.md` 之后：`Setting%20Up%20a%20Subversion%20Repository.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydgnjqfvbuqmznknltc`

实例：
- 同目录：`featuredarticles/Apple URL Scheme Reference/Map Links.md:15` → `[Next](iTunes%20Links.md)`
- 跨文档（回到根再下钻）：`referencelibrary/Getting Started/Getting Started with Audio & Video.md:28` → `[Core Audio Overview](../../documentation/Music%20Audio/Core%20Audio%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzx)`
- 索引 → 文档：`_indexes/documentation/Cocoa.md:9` → `../../documentation/Cocoa/Advanced%20Memory%20Management%20Programming%20Guide/About%20Memory%20Management.md`
- 括号：`_indexes/recipes.md:9` → `../recipes/Distributed%20Builds%20Preferences%20Help/Distributed%20Builds%20Preferences%20Help%20%28Legacy%29.md`

### 9.3 什么时候保留 developer.apple.com 绝对链接

**逐 URL 判断，不是逐标题**：只要该 URL 对应的页面在本次抓取中被落盘，就改写成相对 `.md`；否则原样保留（**含原始的 `#//apple_ref/doc/uid/…` 片段**）。同一文件里两种混存是正常的：
`referencelibrary/Getting Started/Getting Started with Audio & Video.md:28,32,33,34` 是相对链接，而 `:35` → `[Getting Started with Hardware and Drivers](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_HardwareDrivers/_index.html#//apple_ref/doc/uid/TP40003522)` 保持绝对。

必然保留绝对 URL 的场景：
1. 目标未抓取（含 pager 目标：`referencelibrary/Getting Started/About HTTP Live Streaming.md:15`）
2. 非 `/library/archive/` 的 developer.apple.com 链接（新版文档门户、WWDC 视频、开发者账号、Bug Reporter）：`featuredarticles/Apple URL Scheme Reference/Map Links.md:34` → `https://developer.apple.com/documentation/mapkit/mkcoordinatespan`；`ApplePay_Guide/Apple Pay Programming Guide/Configuration.md:22` → `https://developer.apple.com/account`
3. 旧页面残留的 ADC 页面装饰（面包屑、"retired" 声明、Terms of Use、Privacy Policy）100% 绝对：`qa/hw/A SCSI little secret/hw81.md:16,73,74`
4. API Diffs 里的符号链接全部指向 `developer.apple.com/documentation/…`
5. 一切非 Apple 域名照原样

### 9.4 Obsidian wiki 链接：**没有**

- `[[` 在 3,742 个文件里出现，但**全部是 Objective-C 代码**（`[[NSNotificationCenter defaultCenter] …]`、`[[NSOperationQueue alloc] init]`）。
  `featuredarticles/A Short Practical Guide to Blocks.md:48` → `    [[NSNotificationCenter defaultCenter] addObserver:self`
- **全库 0 个真正的 `[[wiki link]]`**。所有文档间链接都是标准 Markdown `[text](percent-encoded-relative-path.md)`。README 第 3 行的说法是错的。
- 生成器请一律用标准 Markdown 链接。

---

## 10. `.obsidian/` 配置

4 个文件：

| 文件 | 内容 |
|---|---|
| `.obsidian/app.json` | `{}`（无换行，2 字节） |
| `.obsidian/appearance.json` | `{}` |
| `.obsidian/core-plugins.json` | 32 个核心插件开关的完整表 |
| `.obsidian/workspace.json` | 本机工作区状态（会随打开而变，不应纳入生成） |

`core-plugins.json` 里开启的与格式相关的项：`"backlink": true`、`"outgoing-link": true`、`"graph": true`、`"properties": true`、`"outline": true`；关闭：`"footnotes": false`、`"markdown-importer": false`、`"zk-prefixer": false`、`"slides": false`、`"webviewer": false`。

**没有任何影响文件格式的设置**——特别是：**没有 `newLinkFormat` / `useMarkdownLinks` / `attachmentFolderPath` 配置**（`app.json` 是空对象），所以链接格式完全由生成器决定，也就解释了为什么用的是标准 Markdown 相对链接而不是 wiki 链接。

---

## 11. 各资源类型速查表

| | `documentation/` | `qa/` | `samplecode/` | `releasenotes/` | `referencelibrary/` | `recipes/` | `featuredarticles/` | `ApplePay_Guide/` | `LucidDreams/` |
|---|---|---|---|---|---|---|---|---|---|
| 分类层 | 有（45） | 有（37，也可无） | 无 | 有（24） | 有（1） | 无 | 无 | 无 | 无 |
| `resource_type` | Guide | QA | Sample Code | Release Note | Guide | Guide | Guide | Guide | Sample Code |
| 入口页 | 具名 or `index.md` | 单页即入口 | `<目录名>.md`（5 例外） | H1 派生，常≠目录名 | 混合 | `<名> (Legacy).md` | 混合，有 `_index.md` | `index.md` | `<目录名>.md` |
| 模板 pager | 有（多页） | **0** | 100% 全部页 | 仅 43/2322，且指向站外 | 部分 | **0** | 有 | **0**（改用带标题的上下页链接） | 100% |
| 首标题层级 | `#`（入口页常 `##`） | `#` | `#` | `#` | `#` / `##` | `#` | `#` | `##` | `#` |
| 修订历史 | 独立页 | 内嵌 `#### Document Revision History` | 独立页 `Document Revision History.md` | 极少（仅 Xcode Release Notes 有） | 独立页 | 无 | 独立页 | `RevisionHistory.md`（`##` + 标准 GFM 表） | 独立页（`#`） |
| 特色结构 | `__Figure/Table/Listing N-N__` + 2×NBSP | `Technical Q&A QA####` 段 + `# 标题` + `## Q:`+NBSP+空格 + 段首 `A: ` | 入口页 3 行元信息表（`__Last Revision:__` / `__Build Requirements:__` / `__Runtime Requirements:__`）；源码页 = `# 原路径` + 一个代码块 | `#### Contents:` 目录、`### Notes and Known Issues`、API Diffs 的 From/To 表与"Added 串接成一行"退化 | `## Introduction`/`### Start Here`/`#### Want to…` | `![bullet](…task_2x.png)To …` + 编号步骤 + `### Related Articles` | 无特别 | `> [!NOTE]`（常为空） | 入口页 3 列元信息表 |

qa 现代页样例（`qa/Accessing Image Metadata in iOS.md`，frontmatter 之后原始字节）：
```
'> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)\n\n\n\nTechnical Q&A QA1622\n\n# Accessing Image Metadata in iOS\n\n## Q:\xa0 How do I get image metadata in iOS?\n\nA: The _[UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller…'
```
注意 `## Q:` 之后是 **U+00A0 + 半角空格**（全量 519 处一致），并且**没有 `## A:` 标题**——答案是以 `A: ` 开头的普通段落。

---

## 12. 不一致 / 存疑清单（生成新文件时必须先决策）

| # | 项 | 变体与出现场景 | 建议 |
|---|---|---|---|
| 1 | 导航行第二段标签 | `documentation`（8,930）vs `文档`（159）——`文档` 只出现在已翻译文件，且另有 138 个已翻译文件仍用英文 | 用英文目录名 |
| 2 | 导航行第三段标签 vs frontmatter `title` | 30,837 一致；109 个不一致（nav 已译、frontmatter 未译，如 `documentation/Cocoa/Core Data Programming Guide/RevisionHistory.md:12`） | 与 frontmatter `title` 保持一致 |
| 3 | 翻页行分隔 | `[Next](…)[Previous](…)` 无分隔（42,045）；中文版出现 `[下一页](…) [上一页](…)`（12）、`[下一页](…) · [上一页](…)`（10）、行尾多空格（4） | 一律无分隔 |
| 4 | 文件尾换行 | 有 pager → `\n\n`（25,606）；无 pager → `\n`（大多数）。但 98 个有 pager 的只 1 个换行（多为翻译过的），566 个表格结尾有 2 个、125 个只 1 个，54 个段落结尾有 2 个，7 个有 3 个 | 按 "有 pager `\n\n`，否则 `\n`" |
| 5 | 图/表/清单标题分隔符 | `__Figure 3-1__` + `\xa0\xa0`（8,887，529 个文档）vs 无分隔符（1,004，32 个文档）vs 单/双半角空格（36/9）vs 独占一行（233）。**按文档一致，跨文档不一致** | 用 `\xa0\xa0` |
| 6 | 表格表头 | A 型 `\| __Date__ \| __Notes__ \|` 无 `\| --- \|` 分隔行（qa 536/536、samplecode、多数 documentation）vs B 型标准 GFM（Metal Best Practices Guide、ApplePay、翻译过的 Core Data） | 与被抓文档的原模板一致；若无依据用 A 型（占多数） |
| 7 | 粗体标记 | `__x__`（24,196）vs `**x**`（1,900，集中在 `releasenotes/` 和翻译文件） | `__x__` |
| 8 | 代码块语言标注 | 63,882 无标注 vs 20,000+ 有标注；同一扩展名在不同文档标注不同（`.h` → `objc`/`c`/无） | 无法从扩展名唯一决定，**存疑**；建议沿用同类型文档的多数标注 |
| 9 | 入口页文件名 | `<目录名>.md`（samplecode 1755/1760）vs H1 派生（releasenotes 23/25 不等于目录名）vs `index.md`（931）vs `_index.md`（1）vs `Document Revision History.md`（1，`referencelibrary/.../Start Developing iOS Apps Today (Retired)/`） | 由页面自身标题/HTML stem 决定，不要从目录名推 |
| 10 | 页面文件名来源 | `sanitize(页标题)` vs 原样 HTML stem（263 个 basename 含 `_` 可证）。**无法从产物判定生成器为何在某页回落到 stem**（推测是页面 H1 抽取失败） | 存疑；优先用标题，抽不到再用 stem |
| 11 | 病态页名 | `Legacy Documentclose button.md` / `Not Recommended Documentclose button.md`（含 `-2`…`-6`），源于把老 QA 页的"关闭按钮"当成 H1 | 已知 bug，不复现 |
| 12 | 退化的图片行 | 裸 `!` / `!!`（qa 225 行、referencelibrary 101 行、featuredarticles 2 行），图片仍在 `attachments/` 但无引用 | 已知 bug，不复现 |
| 13 | 重复图片 | 同一图片在同一行连写两次（@1x/@2x 塌陷）：`releasenotes/Mac OSX/What's New in macOS/OS X Lion v10.7.md:35`；也有只留一份的（`ApplePay_Guide/.../index.md:24`） | 存疑；建议只输出一份 |
| 14 | 空的 alert 块 | `> [!IMPORTANT]` 后紧跟 `> `（无内容）：`releasenotes/Adding Complications to the Gallery.md:18-19`；`releasenotes/` 里 27+22+1 处 | 已知内容丢失，不复现 |
| 15 | 文档目录名 vs frontmatter title | 20 个 `*Developer Note*` 文档的目录名带年份 `(2007)`/`(2008)` 而 frontmatter `title` 不带（如 `documentation/Hardware Drivers/15-inch MacBook Pro Developer Note (2007)-3/`），说明目录名取自**导航索引里的文档名**，与页面 title 不是同一来源 | 目录名用导航索引的文档名 |
| 16 | `apple_id` 唯一性 | 4,121 个 distinct id 对应 4,121 个文档，但有 4 个 id 跨多个目录（`TP40004673` 12 页跨 4 个目录、`TP40006773` 385 页、`TP40006772` 312 页、`DTS10002174` 2 目录）；索引里也因此有 54 处页数不符 | 存疑；索引页数按"同 apple_id 的页数"算会出错 |
| 17 | README 数字 | `35753 个 Markdown 文件` 与实测 35,752 文档页 / 35,884 总 `.md` 都不符 | 存疑，来源不明 |
| 18 | README 声明 wiki 链接 | 与事实相反（0 个 `[[]]`） | 文案错误 |
| 19 | 未编入索引段落 | 只有 `_indexes/documentation.md:244` 有 `## 未编入索引的页面`，其他 8 个类型索引都没有（尽管 `_unindexed/` 里也有 releasenotes/referencelibrary 的页面图片） | 存疑 |
| 20 | 分组阈值 20 | 实测"带子分组的最小 N = 21，不带的最大 N = 19"，**N = 20 的样本不存在** | 阈值取 `>= 20`（存疑，可能是 `> 20`） |
| 21 | 页首"第 15 行槽位" | `releasenotes/` 里这一行可能是 pager、`Document Generated: 2017-08-24 16:34:04 -0700`（`releasenotes/App Kit/AppKit Release Notes for macOS 10.13.md:15`）、ADC 面包屑（`releasenotes/Mac OSX/API Changes in Snow Leopard/AppKit Changes.md:15-19`）或空 | 按源页面内容决定；不要假定 H1 固定在第 17 行 |
| 22 | 中文翻页措辞 | `[下一页]/[上一页]`（200+）vs `[下一篇]/[上一篇]`（16，且带空格，`documentation/Cocoa/Event-Driven XML Programming Guide/XML Glossary.md:15`） | 用 `[下一页]/[上一页]`；新生成器一律用英文 `[Next]/[Previous]` |
| 23 | 底部翻页的第二形态 | 无 `[Next]/[Previous]` 标签、用章节标题当链接文字，且**上一章在前、下一章在后**（与页首相反），两行之间空一行。`documentation/Cocoa/Key-Value Coding Programming Guide/BasicPrinciples.md:105-107`、`ApplePay_Guide/.../Configuration.md:47,49` | 存疑：与页面模板（变体 B）绑定，不能与 `[Next][Previous]` 混用 |
| 24 | `#` 后空格数 | 1 个（主流）vs 2 个（`##` 1,032 次）vs 3 个（`#` 259 次，`documentation/Carbon/Programming with the Appearance Manager/About the Appearance Manager.md:22`） | 用 1 个 |
| 25 | 图表标题分隔符第三/第四种 | 除 `\xa0\xa0` 与无分隔外，还有 **U+3000**（90 次，中文页 `documentation/Cocoa/Key-Value Coding Programming Guide/BasicPrinciples.md:26`）与 1/2 个半角空格 | 用 `\xa0\xa0` |
| 26 | `__Note:__` 的分隔符 | **两个半角空格**（121）/ 无（102）/ 一个半角空格（39）——注意这里**不是** NBSP，与图表标题相反 | 用两个半角空格 |
| 27 | 代码呈现第三形态 | "有序列表 + 行内代码"（10,367 行 / 266 文件），编号 = 源文件行号，空行处编号断口（`documentation/Cocoa/Key-Value Coding Programming Guide/BasicPrinciples.md:28-32`）；另有缩进 4 空格式（35,687 行）与引用块内栅栏（2,212 行） | 已知转换缺陷，新生成器用栅栏 |
| 28 | 正文里的裸 `---` | 旧 WebObjects/Carbon 页面在 `__PATH__` 装饰之后放一行 `---`（`documentation/Legacy Technologies/WebObjects 4.0 Developer Documentation/EOSortOrdering.md:22`）；现代 qa 用它分隔修订历史 | 解析 frontmatter 时只认文件最前面的一对 `---` |
| 29 | 表格分隔行缺失比例 | 全库表格行 1,025,853 / 分隔行 245,244；`documentation/` 内 1,205/3,509 文件完全没有分隔行；DRH 页只有 51/518 有 | 与原模板一致；无依据则不写分隔行（占多数） |
| 30 | 嵌套列表缩进 | 2/3/4/6/1/5 空格都有（2,481/1,009/580/158/93/61） | 无序用 2 空格，有序续行用 3 空格 |
| 31 | 硬折行 | 极少数旧文档保留源 HTML 的段内硬折行（`documentation/Quick Time/QuickTime 5.md:20-29`），现代页一律一段一行 | 一段一行 |

---

## 13. 生成器最小实现清单

1. **frontmatter**：`"---\n" + yaml.safe_dump(OrderedDict(9 keys), sort_keys=False, allow_unicode=True, default_flow_style=False) + "---\n"`，不改 `width`。
2. **文件/目录名**：§2.4 的 `sanitize()`；页名优先取页标题，回落 HTML stem；同名加 `-2`/`-3`；截断 80 在加后缀之前。
3. **导航行**：`"> 导航：[总目录](" + "../"*depth + "README.md) · [" + toptype + "](" + "../"*depth + "_indexes/" + toptype + ".md)"`，多页文档再追加 `" · [" + doc_title + "](" + quote(entry_filename) + ")"`。
4. **模板**：`nav + "\n\n\n" + (pager + "\n" if pager else "") + "\n" + body`。
5. **pager**：`f"[Next]({quote(nxt)})" + f"[Previous]({quote(prv)})"`，页首页尾各一份；末尾 `+ "\n\n"`。
6. **链接**：`urllib.parse.quote(rel_path)` + `("#apple-" + b32(apple_ref).lower().rstrip("="))`。
7. **图片**：`![{alt}](attachments/{原相对路径去掉 ../})`。
8. **索引**：§6 的 4 层结构 + §6.2 的条目语法 + §6.4 的主平台优先级 + 阈值 20。
9. **README**：§7 的固定 6 段，数字重算。
10. **不要**生成 wiki 链接、不要动 `.obsidian/app.json`、不要复现 §12 的 #11/#12/#14 三个已知 bug。
