# Apple Developer Archive Vault 中文翻译规范

本规范从仓库中已完成的 178 页译文里反推提取，**必须严格遵守**。目标是让你的译文与已合并的译文无法区分。

仓库根目录：`/Users/tommywu/Desktop/翻译/vault`

---

## 一、绝对禁止

1. **禁止执行任何 git 命令**（不 add、不 commit、不 checkout、不 stash）。提交由调度方统一处理。
2. **禁止修改 `doc/TRANSLATION_PLAN.md` 和 `doc/TRANSLATION_PLAN_WINDOWS_VIEWS.md`**。状态表由调度方统一更新。
3. **禁止改动任何链接的目标路径和锚点**。只能改链接的显示文字。
   - 正确：`[Using Timers](Using%20Timers.md#apple-f4xwc4...)` → `[使用定时器](Using%20Timers.md#apple-f4xwc4...)`
   - 错误：把 `Using%20Timers.md` 改成 `使用定时器.md`，或删掉 `#apple-...` 锚点
4. **禁止改文件名、禁止新建文件、禁止删文件、禁止动 `attachments/` 目录**。
5. **禁止保留双语**（不要"英文原文 + 中文译文"并列），一律原地替换。
6. **禁止漏译**。每一个自然段、每一个列表项、每一个表格单元格的说明文字都要处理完。不允许"...（后续内容略）"。

---

## 二、YAML frontmatter

**只翻译 `title` 一个字段**，其余字段（`apple_id`、`resource_type`、`platform`、`topic`、`technology`、`published`、`source_url`、`archived_at`）**一个字符都不能动**。

`title` 用该文档的统一中文译名（调度方会在任务里指定，同一文档所有页面的 `title` 必须完全一致）。

```yaml
---
title: 定时器编程主题          # ← 只改这行
apple_id: 10000061i           # ← 不动
resource_type: Guide          # ← 不动
platform: watchOS|tvOS|iOS|macOS   # ← 不动
topic: Data Management        # ← 不动
technology: Foundation        # ← 不动
published: '2009-07-14'       # ← 不动
source_url: https://...       # ← 不动
archived_at: '2026-07-15...'  # ← 不动
---
```

## 三、导航行

面包屑固定译法（路径不动）：

```
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)
```
→
```
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)
```

若面包屑第三项是本文档入口页，其显示文字改成该文档的中文译名。

页首和页尾的翻页链接：
- `[Next]` → `[下一页]`
- `[Previous]` → `[上一页]`

（页首、页尾两处都要改，路径不动。）

## 四、正文译法

### 保留英文，不译
- 所有 API / 类 / 方法 / 协议 / 常量 / 通知名：`NSTimer`、`NSRunLoop`、`invalidate`、`setDelegate:`、`NSApplicationDidFinishLaunchingNotification`
- 框架名：`Foundation`、`UIKit`、`AppKit`、`Core Data`、`QuartzCore`
- 已成惯例的复合概念：`Collection View`、`Scroll View`、`View Controller`、`Interface Builder`、`Xcode`、`nib`、`Storyboard`
- 代码里的一切标识符

### 术语表（强制统一，从既有译文提取）

| 英文 | 中文 |
|---|---|
| delegate | 委托（**不要用"代理"**） |
| accessor / accessor method | 存取方法 |
| run loop | 运行循环 |
| thread | 线程 |
| protocol | 协议 |
| key path | 键路径 |
| predicate | 谓词 |
| notification center | 通知中心 |
| instance | 实例 |
| subclass | 子类（动词：派生子类） |
| superclass | 超类 |
| archive / archiving | 归档 |
| serialization | 序列化 |
| managed object | 托管对象 |
| managed object context | 托管对象上下文 |
| persistent store | 持久化存储 |
| fault / faulting | 故障 / 故障机制 |
| uniquing | 唯一化 |
| property | 属性（`property` 关键字本身保留英文） |
| attribute | 属性（属性字符串语境）/ 特性 |
| entity | 实体 |
| fetch request | 获取请求 |
| observer | 观察者 |
| invalidate | 失效（动词） |
| retain / release | 保留 / 释放 |
| autorelease pool | 自动释放池 |
| reference counting | 引用计数 |
| block | block（保留英文） |
| selector | 选择器 |
| category | 分类 |
| extension | 扩展 |
| responder chain | 响应者链 |
| target-action | 目标-动作 |
| deprecated | 已废弃 |

### 首次出现标注原文
重要术语在**每个页面内首次出现**时，用「中文（英文）」标注，之后只用中文：
- `存取方法（accessor）`、`原始（primitive）存取方法`、`委托（delegate）`

### 图表标题
- `__Figure 3-1__  Some caption` → `__图 3-1__  某某说明`
- `__Table 1__  Some caption` → `__表 1__  某某说明`
- 编号格式和后面的空格数保持原样

### 图片
- 描述性 alt 文字要译：`![Browser example](attachments/art/browser.gif)` → `![浏览器示例](attachments/art/browser.gif)`
- 路径式 alt 不译，原样保留：`![image: ../art/department_fault.pdf](...)` 保持不变
- **图片路径永远不动**

### 语气
- 用第二人称"你"（既有译文的做法），不用"您"
- 陈述句为主，不加原文没有的语气词
- 保持原文的段落切分，不合并、不拆分段落
- Markdown 结构（标题层级 `#`、列表符号、加粗 `__x__` / `**x**`、斜体 `_x_`）完全保持原样

## 五、代码块

1. **补语言标注**：裸的 ` ``` ` **起始**符补上 `objc`（这批文档绝大多数是 Objective-C）、`swift`、`c`、`xml`、`json`、`bash` 中合适的一个。
   - **只补起始符**。结束符本来就该是裸 ` ``` `，**不要动结束符**。
   - 判断不了语言的（纯数据、纯输出、伪代码）就保持裸 ` ``` `。
2. **代码本身一个字符都不改**（标识符、字符串字面量、缩进、空行全部保持）。
3. **只把代码注释译成中文**：`// Create a timer` → `// 创建一个定时器`
4. 行内代码 `` `NSTimer` `` 内的内容不译。

## 六、表格

- 表头和单元格里的**说明文字**要译，**API 名 / 常量名 / 类型名不译**
- 表格的 Markdown 结构（`|` 分隔、`| --- |` 分隔行）保持完整；若发现原文缺 `| --- |` 分隔行导致表格错位，顺手补上
- 列数必须与原表一致

## 七、Document Revision History 页面

- 页面标题 `# Document Revision History` → `# 文档修订历史`
- 表头 `Date` / `Notes` → `日期` / `说明`
- 日期数值保持原样（如 `2009-07-14`、`July 14, 2009` 保留原格式，不转成中文日期）
- Notes 列的说明文字要译

## 八、Index.md 这类纯索引页

- 页面标题、表头说明文字要译（如"数字表示对该主题的一次引用。"）
- 索引条目本身若是英文 API 名，**不译**
- 字母导航 `[A] [B] [C]...` 不动

## 八点五、实战中反复踩过的四个坑（务必先看）

### 1. NBSP（U+00A0）陷阱 —— 本项目最高频的缺陷
`__Figure/Table/Listing N-N__` 标签后面的分隔符**往往是两个 NBSP（U+00A0），不是普通空格**。Read 工具会把它渲染成普通空格，于是你按 Read 看到的内容构造 `old_string` 去 Edit 就会报「字符串未找到」。

- **遇到匹配失败**：把「编号标签」和「说明文字」拆成两次 Edit，绕开 NBSP 不触碰。
- **代码块内、以及行内 `code` 跨度内的 NBSP 属于代码字节，必须原样保留**，绝不能替换成普通空格。曾经有译文把 XML 示例缩进的 130 个 NBSP 全换成空格，也有把 `NSScanner` 示例里演示空格差异的 NBSP 换掉、导致整段说明失去意义。
- 正文/图表标题里的 NBSP 变成普通空格是可以接受的（仓库既有 178 页译文都是如此），但**代码里的一个都不能变**。
- 自检：`grep -c $'\xc2\xa0' 文件` 比对译前译后，代码内数量必须相等。

### 2. 文件末尾换行数
仓库惯例是文件以空行结尾（即以 `\n\n` 结束）。用 Write 整篇写回时**极易吞掉最后一个换行**。写完必须确认末尾换行数与原文一致。

### 3. 大文件不要用一次 Write 写回
超过约 20 KB 的页面，一次 Write 输出会被截断，造成**静默的内容丢失**。改用 Edit 按 `##` 小节或语义段落块逐段替换，全部替换完再 Read 通读一遍确认没有遗留英文段落、没有内容丢失。

### 4. 页面 H1 要译
139 个已译页面里只有 4 个 H1 没有中文，且那 4 个的标题整体就是一个约定保留英文的术语（如 `# Split View Controller`）。除此之外，H1 一律译成中文，保留英文术语可以内嵌其中（如 `# Collection View 基础`、`# 关于 View Controller`）。同一术语的单复数在中文里统一取单数。

## 九、完成后自检（必做）

在报告完成前，逐条自查：

1. 该文档目录下**任务清单里列出的每一个页面文件**都已处理，没有遗漏
2. 每个文件的 frontmatter 除 `title` 外零改动
3. 所有链接的 `](...)` 部分与改前完全一致（路径 + 锚点）
4. 所有 `attachments/` 路径未变
5. 该文档内不再有成段的英文正文残留（API 名、代码、保留术语除外）
6. 代码块起始符已补语言标注，结束符仍是裸 ` ``` `
7. 同一文档所有页面的 frontmatter `title` 完全一致
8. `[Next]`/`[Previous]` 已全部改成 `[下一页]`/`[上一页]`

## 十、交付报告格式

完成后，用以下格式返回（这是你的返回值，不是给人看的消息）：

```
文档：<文档标题>
处理页面数：N
逐页清单：
  - <文件名>：已译，代码块补标 X 处，修复格式问题 Y 处
  - ...
遇到的问题：<如某页有无法判断语言的代码块、原文本身有错等；没有就写"无">
```
