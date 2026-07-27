# Apple 现行文档中译规范

本规范适用于 `apple-docs/` 下的现行文档（`developer.apple.com/documentation`）。

> **和旧归档那份规范的关系**：术语表继承旧仓库（见 `TERMS.md`），但**工作方式完全不同**。旧归档是原地替换英文，这里是 `en/` 保留英文基线、`zh/` 写译文。原因：现行文档是 Apple 在维护的活内容，每年会改，留着英文基线才能靠 `content_hash` 做增量 diff、只重译变化的部分。

---

## 一、绝对禁止

1. **禁止修改 `en/` 下的任何文件。** 那是英文基线，是增量重抓的比对基准。译文只写 `zh/`。
2. **禁止执行任何 git 命令**（不 add、不 commit、不 checkout、不 stash）。提交由调度方统一处理。
3. **禁止改动 frontmatter 除 `title` 以外的任何字段。** 一个字符都不行——`content_hash`、`platforms`、`doc_path`、`source_url` 都是机器生成、机器消费的。
4. **禁止改动任何链接的目标和锚点。** 只能改显示文字。
   - 正确：`[UIApplicationMain](uiapplicationmain.md)` → `[UIApplicationMain](uiapplicationmain.md)`（API 名不译，链接不动）
   - 正确：`[App and environment](app-and-environment.md)` → `[App 与环境](app-and-environment.md)`
   - 错误：把 `app-and-environment.md` 改成 `app-与环境.md`
5. **禁止改动图片路径。** `![](../../../attachments/…)` 里的路径不动，只译 alt 文字和 `<sub>` 图注。
6. **禁止改动代码块内的代码。** 只能译注释。声明块（`declaration`）连注释都没有，一个字符都别碰。
7. **禁止增删任何结构。** 段落数、列表项数、表格行列数、标题层级、callout 数量都必须和英文原文一致。机械校验会逐项比对（`tools/validate.py`）。
8. **禁止漏译。** 每个自然段、每个列表项、每个表格单元格的说明文字、每条 `See Also` 的摘要都要处理完。不允许「…（后续内容略）」。

---

## 二、文件位置与 frontmatter

译文路径 = 英文路径把 `/en/` 换成 `/zh/`，其余完全一致。

```
apple-docs/en/uikit/about-the-app-launch-sequence.md   ← 原文，不动
apple-docs/zh/uikit/about-the-app-launch-sequence.md   ← 译文，你写这个
```

frontmatter **只改两处**：

```yaml
---
title: 关于 App 启动序列        # ← 译成中文
framework: UIKit                # ← 不动
symbol_kind: article            # ← 不动
role: article                   # ← 不动
role_heading: Article           # ← 不动（见下方结构性文字对照表，正文里的 <sub> 才译）
platforms: ['iOS 13.0+', ...]   # ← 不动
languages: [swift, occ]         # ← 不动
beta: false                     # ← 不动
deprecated: false               # ← 不动
doc_path: /documentation/...    # ← 不动
source_url: https://...         # ← 不动
doc_json: https://...           # ← 不动
content_hash: 'sha256:...'      # ← 不动
translated: true                # ← 改成 true
---
```

---

## 三、结构性文字的固定译法

渲染器生成的结构性文字，**必须用下表的固定译法**，不要自由发挥（同一语料里译法不统一比译得不够漂亮糟糕得多）。

这一节由 `tools/validate.py` 的 `FIXED_LINES` / `FIXED_INLINE` 强制执行，
漏译的存量可以用 `python3 tools/fix_structural.py --apply` 批量统一。
加这道检查之前漏出去过 150 处——因为这些标题只有一两个单词，够不到「残留英文」
的 8 词阈值，`## 概述` 与 `## Overview` 曾在同一个仓库里共存。

| 英文原文 | 固定中文译法 |
|---|---|
| `> Navigation: ` | `> 导航：` |
| `## Topics` | `## 主题` |
| `## See Also` | `## 另请参阅` |
| `## Relationships` | `## 关系` |
| `## Parameters` | `## 参数` |
| `## Default Implementations` | `## 默认实现` |
| `## Download` | `## 下载` |
| `## Overview`（Apple 原文里的） | `## 概述` |
| `## Transcript`（WWDC） | `## 逐字稿` |
| `## Resources`（WWDC） | `## 相关资源` |
| `## Chapters`（WWDC） | `## 章节` |
| `### Essentials` | `### 基础` |
| `### Reference` | `### 参考` |
| `### Related Documentation` | `### 相关文档` |
| `### Constants` | `### 常量` |
| `### Variables` | `### 变量` |
| `### Functions` | `### 函数` |
| `### Macros` | `### 宏` |
| `### Classes` | `### 类` |
| `### Structures` | `### 结构体` |
| `### Protocols` | `### 协议` |
| `### Enumerations` | `### 枚举` |
| `### Enumeration Cases` | `### 枚举 case` |
| `### Type Aliases` | `### 类型别名` |
| `### Initializers` | `### 初始化方法` |
| `### Instance Methods` | `### 实例方法` |
| `### Instance Properties` | `### 实例属性` |
| `### Type Methods` | `### 类型方法` |
| `### Type Properties` | `### 类型属性` |
| `### Deprecated` | `### 已废弃` |
| `### Error codes` | `### 错误码` |
| `### Supporting types` | `### 支持类型` |
| `_(deprecated)_` | `_(已废弃)_` |
| `_(beta)_` | `_(beta)_`（保留） |
| `> [!warning] Deprecated` | `> [!warning] 已废弃` |

`<sub>` 里的角色标签：

| 英文 | 中文 |
|---|---|
| `<sub>Article</sub>` | `<sub>文章</sub>` |
| `<sub>Framework</sub>` | `<sub>框架</sub>` |
| `<sub>Sample Code</sub>` | `<sub>示例代码</sub>` |
| `<sub>API Collection</sub>` | `<sub>API 集合</sub>` |
| `<sub>Instance Method</sub>` | `<sub>实例方法</sub>` |
| `<sub>Instance Property</sub>` | `<sub>实例属性</sub>` |
| `<sub>Type Method</sub>` | `<sub>类型方法</sub>` |
| `<sub>Initializer</sub>` | `<sub>初始化方法</sub>` |
| `<sub>Enumeration Case</sub>` | `<sub>枚举 case</sub>` |

平台清单那种 `<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>` **不译**（平台名是专有名词）。

---

## 四、Obsidian callout

保留 `[!类型]` 不变，只译后面的标签文字和内容：

```markdown
> [!important] Important          →   > [!important] 重要
> Use UIKit classes only from…    →   > 只能从 App 的主线程使用 UIKit 类…
```

标签固定译法：`Note` → `注意`、`Important` → `重要`、`Warning` → `警告`、`Tip` → `提示`、`Deprecated` → `已废弃`、`Throws` → `抛出`、`Complexity` → `复杂度`、`Precondition` → `前置条件`、`Postcondition` → `后置条件`。

---

## 五、代码块

现行文档里有两类代码块，处理方式不同：

**1. 声明块**（`symbol_kind` 不是 article 的页面，正文第一个代码块）——**一个字符都不许改**：

````markdown
```swift
@MainActor protocol UISearchBarDelegate : UIBarPositioningDelegate
```
````

**2. 示例代码块**——只译注释，代码本身（标识符、字符串字面量、缩进、空行）全部保持：

````markdown
```swift
// Create a timer          →   // 创建一个定时器
let timer = Timer(...)     →   let timer = Timer(...)    ← 不动
```
````

语言标注（```` ```swift ````、```` ```objc ````）不动。行内代码 `` `NSTimer` `` 内容不译。

---

## 六、正文译法

### 保留英文，不译
- 一切 API / 类 / 方法 / 协议 / 常量 / 通知名：`UIApplication`、`viewIsAppearing(_:)`、`NSTimer`
- 框架名：`UIKit`、`SwiftUI`、`Foundation`、`Core Data`、`Combine`
- Swift 关键字与语言构造：`actor`、`async`、`await`、`Sendable`、`@MainActor`
- 工具名与文件格式名：`Interface Builder`、`Storyboard`、`nib`、`XIB`
  > ⚠️ **2026-07-26 变更**：`Collection View`、`View Controller`、`Scroll View`、`Scene` 原先也列在这一条里，现已按 Apple 官方中文**改为译成中文**——集合视图、视图控制器、滚动视图、场景。裁决记录见 `TERMS.md` §5.10。对应的**类名**（`UICollectionView`、`UIViewController`、`UIScrollView`、`UIScene`）仍然保留英文，走上面「一切 API / 类 / 方法」那一条。
- 平台名：`iOS`、`iPadOS`、`visionOS`、`Mac Catalyst`
- 代码里的一切标识符

### 术语
以 `TERMS.md` 为唯一依据。表里没有的术语：
1. 先在 `zh/` 已译文件里 grep 看有没有先例，有就跟随
2. 没有先例且没把握的，**保留英文**，并在交付报告里列出来等裁决
3. **不要自创译法**

重要术语在**每个页面内首次出现**时用「中文（英文）」标注，之后只用中文。

### 语气
- 用第二人称「你」，不用「您」（继承旧仓库既有译文的做法）
- Apple 原文大量用 "your app"，译成「你的 App」——`App` 保留英文，这是 Apple 中文的一贯做法
- 陈述句为主，不加原文没有的语气词
- 保持原文的段落切分，不合并、不拆分

### 图片
- 描述性 alt 要译：`![A diagram of the launch sequence](路径)` → `![启动序列示意图](路径)`
- 超长 alt 被渲染器挪到了下一行的 `<sub>` 图注里，**图注也要译**（那是完整的辅助功能描述，通常是一整段）
- **路径永远不动**

---

## 七、完成后自检（必做）

在报告完成前，逐条自查，然后**跑一遍机械校验**：

```bash
python3 tools/validate.py apple-docs/zh/<你负责的目录>
```

校验必须零问题才算完成。它会检查：

1. frontmatter 除 `title` / `translated` 外零改动
2. 链接与图片目标集合与原文完全一致
3. 代码块数量、语言标注、行数一致，非注释行逐字符一致
4. 标题层级序列、列表项数、表格行数、callout 类型一致
5. 译文里没有残留的成句英文

---

## 八、交付报告格式

```
负责范围：<目录或文档清单>
处理文件数：N
逐文件清单：
  - <相对路径>：已译
  - ...
机械校验：python3 tools/validate.py <路径> → 通过 / 有 N 个问题（列出来）
新术语（TERMS.md 里没有的）：
  - <英文> → <我的处理：保留英文 / 暂译为 X>，理由
遇到的问题：<原文本身有错、结构无法保持一致等；没有就写「无」>
```
