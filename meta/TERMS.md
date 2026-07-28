# Apple 现行开发者文档 中译术语表

本表是所有翻译 agent 的**唯一术语依据**。与 `../../TRANSLATION_STYLE.md`（译文体例规范）配套使用：体例问题查那份，词汇问题查这份。

核实过程与访问过的 URL 记录在同目录 `TERMS_SOURCES.md`。

---

## 修订说明（第 2 版，2026-07-26）

本次修订依据用户裁决一句话：**「术语表按 Apple 官方中文来」**。执行优先级如下：

1. **有 Apple 官方简体中文依据的 → 一律采用官方译法**，即使与旧仓库规范或中文社区惯例冲突。
2. **官方自己有两种译法的 → 取更晚、更正式的那个**，另一变体与选择理由记在第五节。
3. **没有官方中文依据的 → 不动**，维持第 1 版的处置（继承旧仓库译法或保留英文），但把「旧规范 vs 实际语料词频」的分歧写清楚，便于日后复查。
4. **官方从不翻译的（API / 关键字 / 框架名 / 产品名）→ 继续保留英文**，不受本次裁决影响（`actor`、`Sendable`、`async/await`、`Liquid Glass` 等）。

第 1 版第五节列出的 **16 条待裁决已全部裁决完毕**，结论已合并进正文各节表格；第五节改写成「已裁决记录」，逐条保留分歧点、两个候选、依据来源和最终选择理由，**这一节是复查档案，不要删**。

本次改判的高频术语（影响面最大的几条）：

| 英文 | 第 1 版 | 第 2 版 | 依据 |
|---|---|---|---|
| view controller | 保留英文 `View Controller` | **视图控制器** | 官方 |
| collection view | 保留英文 `Collection View` | **集合视图** | 官方 |
| scroll view | 保留英文 `Scroll View` | **滚动视图** | 官方 |
| control | 控件（社区） | **控制** | 官方 |
| navigation | 导航（社区） | **导览**（组件「导航栏」例外） | 官方 |
| stack（VStack 等） | 未定 | **叠放** | 官方 |
| accessibility | 无障碍 | **辅助功能** | 官方（iOS 界面用词） |
| hitch | 卡顿（暂定） | **卡顿**（确认，升级为官方依据） | 官方（更晚来源） |
| data race | 数据竞争 | **数据争用** | 官方（更晚、更正式来源） |
| main actor | 主 Actor | **主要 Actor** | 官方 |

> **⚠️ 与旧仓库的有意分歧（重要）**
>
> 本表的选择会和旧仓库 `apple-developer-archive-vault`（`翻译/vault/`）**已译的 239 篇不一致**——旧译文按旧规范把 `View Controller`、`Collection View`、`Scroll View` 等保留成了英文，本表改成了官方中文。
>
> **这是两个独立语料的有意分歧，不要去改旧仓库**（连读取都不必），也不要拿旧仓库的用词来「纠正」新译文。旧仓库在本表里只充当**词频证据来源**，不充当译法仲裁者。

---

## 一、使用说明（翻译 agent 必读）

### 1.1 查表顺序

遇到一个术语，按下面顺序决定译法，**先命中先用，不要跳级**：

1. 查**第四节「一律保留英文」**的判断规则 → 命中就保留英文，不译。
2. 查**第三节「术语表」** → 命中就用该译法。第三节里标「官方」的条目**优先级最高**，因为它们是 2026-07-26 裁决的直接产物。
3. 查**第二节「继承自旧仓库」** → 命中就用该译法。这批译法是既成事实（旧仓库 239 篇译文的实际用词），**即使你认为有更好的译法也不许改**。
4. 表里完全没有 → 见下面 1.2。

**第五节不参与查表。** 它是 2026-07-26 的裁决档案，结论已经全部合并进第二、三、四节；只在你想复查「为什么是这个译法」时去看。**第五节里不再有任何「临时处置」，也没有未决项。**

> 第 2 版的一个顺序变化：第 1 版里第二节（旧仓库）优先于第三节（新增），现在**第三节标「官方」的条目反过来压过第二节和第四节**。这正是「按 Apple 官方中文来」的含义。目前实际发生冲突的只有 §5.6 / §5.10 涉及的那几条（control、navigation、view controller、collection view、scroll view），都已经在正文表格里改到位，不会让你自己去判。

### 1.2 表里没有的术语怎么办

- **能用通行中文表达的**（如 `button`→按钮、`file`→文件、`error`→错误）：直接译，不用请示。本表只收录「有分歧风险」或「必须统一」的词，不收录这类。
- **API / 标识符 / 产品名**：按第四节规则保留英文。
- **拿不准、且该词在本篇文档里反复出现（≥3 次）**：**保留英文原词**，并在交付报告的「遇到的问题」里列出该词 + 你的建议译法。**绝对不要临时自创一个译法然后铺满全篇**——不一致的中文比留着英文更难修。
- **拿不准、且只出现 1-2 次**：用「中文（English）」形式写，中文取最保守的直译。

### 1.3 首次出现是否标注原文

继承旧仓库做法：**重要术语在每个页面内首次出现时，用「中文（英文）」标注，之后只用中文。**

- 例：`响应者链（responder chain）`、`安全区（safe area）`、`结构化并发（structured concurrency）`
- **需要标注的**：本表第二、三节里的概念性术语。
- **不需要标注的**：已经是中文常识的（视图、线程、协议、属性、动画）；本身就保留英文的（`Sendable`、`async/await`、`dyld`）；纯 UI 组件名（按钮、工具栏、边栏）。
- 标注只做**一次**，按页面计，不按整篇文档计。
- 括号用**半角圆括号**，与英文原词一起：`委托（delegate）`。

### 1.4 高频陷阱

1. `delegate` → **委托**，不是「代理」。现行文档里同样适用。
2. `document` → **文稿**（Apple 官方中文用词，如「文稿启动器」「打开文稿」）；`documentation` → **文档**。两者不要混。
3. `Liquid Glass` → **保留英文**。Apple 官方中文文档全篇直接写 `Liquid Glass`，**不要写「液态玻璃」**（那是中文媒体的叫法）。
4. **`view controller` / `collection view` / `scroll view` / `table view` 一律译成中文**（视图控制器 / 集合视图 / 滚动视图 / 表格视图）。第 1 版要求保留英文，**已在第 2 版推翻**，见 §5.10。`view controller` 在现行语料里出现 958 次，是全项目最高频的术语簇，**不允许出现半篇中文半篇英文**。
5. `control` → **控制**（不是「控件」）、`navigation` → **导览**（不是「导航」）。见 §5.6。两个例外：
   - 组件 `navigation bar` 官方就叫「**导航栏**」（HIG 原话：「在 iOS 中，导览特定的工具栏有时会称为导航栏」）。
   - 渲染器生成的面包屑行 `> Navigation: ` 仍固定译作「`> 导航：`」，见 `TRANSLATION_STYLE.md` §三。那是**结构性文字**，已被机械校验和既有译文锁定，**不要改成「导览」**。
6. `accessibility` → **辅助功能**（不是「无障碍」）。见 §5.16。
7. `hitch` → **卡顿**、`hang` → **挂起**。两者都是官方用词，**不要互换**，见 §5.7、§5.8。

### 1.5 依据来源标记含义

| 标记 | 含义 |
|---|---|
| **官方** | Apple 简体中文材料里的实际用词，URL 见 `TERMS_SOURCES.md`。可信度最高。 |
| **官方（择一）** | Apple 中文材料里有两种以上译法，本表按「更晚、更正式」原则择一。另一变体记在第五节。 |
| **官方派生** | 官方给了组成部分但没给这个组合词，由官方部件拼出（如 table=表格 + view=视图 → 表格视图）。 |
| **旧仓库** | `翻译/vault/` 已完成译文中的实际用词，附出现次数。 |
| **社区** | 中文技术社区长期通行、无官方对照的译法。 |
| **自定** | 本项目自定，无外部依据。数量已尽量压到最低。 |
| **保留英文** | 有意不译。 |

> 关于官方来源的一个重要事实：**Apple 只把《人机界面指南》和 WWDC 场次标题/简介本地化成简体中文，框架 API 参考文档（`developer.apple.com/documentation/*`）没有中文版**（已实测验证，见 `TERMS_SOURCES.md` §2）。所以设计/交互/系统体验类术语官方依据充足，而 Swift 语言细节、dyld/Mach-O、渲染内部机制这些领域官方依据稀薄——那些条目多为社区或自定，标注已如实反映。

---

## 二、继承自旧仓库的术语（34 条，译法不可改动）

原样继承**旧仓库**（`apple-developer-archive-vault`）那份 `TRANSLATION_STYLE.md` 第 70-107 行的术语表。「旧仓库次数」是在 `翻译/vault/documentation/` 下已译页面中该中文词的实际出现次数（有效语料约 239 篇）。

| 英文 | 中文 | 依据 | 旧仓库次数 | 核验结果 |
|---|---|---|---|---|
| delegate | 委托（**不要用「代理」**） | 旧仓库 | 223 | ✅ 干净。「代理」51 次中 47 次是「代理对」(surrogate pair)，与本义无关 |
| accessor / accessor method | 存取方法 | 旧仓库 | 29 | ⚠️ 实际译文以「访问器」(75) 为主 → **已裁决 §5.1：维持「存取方法」**（无官方中文依据，不改） |
| run loop | 运行循环 | 旧仓库 | 25 | ✅ |
| thread | 线程 | 旧仓库 | 107 | ✅ |
| protocol | 协议 | 旧仓库 | 136 | ✅ 官方亦用（`developer.apple.com/cn/swift/`） |
| key path | 键路径 | 旧仓库 | 70 | ✅ 无竞争译法 |
| predicate | 谓词 | 旧仓库 | 63 | ✅（「断言」39 次是 assertion，非竞争项） |
| notification center | 通知中心 | 旧仓库 | 61 | ✅ |
| instance | 实例 | 旧仓库 | 514 | ✅ |
| subclass | 子类（动词：派生子类） | 旧仓库 | 198 | ✅ |
| superclass | 超类 | 旧仓库 | 49 | ✅（「父类」7、「基类」2，轻微漂移，不改判） |
| archive / archiving | 归档 | 旧仓库 | 171 | ✅ |
| serialization | 序列化 | 旧仓库 | 37 | ✅ |
| managed object | 托管对象 | 旧仓库 | 294 | ✅ |
| managed object context | 托管对象上下文 | 旧仓库 | 82 | ✅ |
| persistent store | 持久化存储 | 旧仓库 | 113 | ✅ |
| fault / faulting | 故障 / 故障机制 | 旧仓库 | 120（含「故障化」26） | ✅ |
| uniquing | 唯一化 | 旧仓库 | 13 | ✅ |
| property | 属性（`property` 关键字本身保留英文） | 旧仓库 | 1121 | ✅ |
| attribute | 属性（属性字符串语境）/ 特性 | 旧仓库 | 44（「特性」） | ⚠️ 与 property 未有效区分 → **已裁决 §5.3：维持旧规范表述**（无官方中文依据，不改） |
| entity | 实体 | 旧仓库 | 317 | ✅ |
| fetch request | 获取请求 | 旧仓库 | 32 | ✅ |
| observer | 观察者 | 旧仓库 | 102 | ✅ |
| invalidate | 失效（动词） | 旧仓库 | 21 | ✅ 偏少但无竞争 |
| retain / release | 保留 / 释放 | 旧仓库 | 79 / 208 | ⚠️ retain：「持有」91 次反超「保留」79 次 → **已裁决 §5.2：维持「保留」**（无官方中文依据，不改） |
| autorelease pool | 自动释放池 | 旧仓库 | 52 | ✅ |
| reference counting | 引用计数 | 旧仓库 | 12 | ✅ 偏少但无竞争 → **已裁决 §5.5：维持** |
| block | `block`（保留英文） | 旧仓库 | 英文 block 2274 | ⚠️ 但中文「块」约 113 次（「自动释放池块」35） → **已裁决 §5.4：维持保留英文**（无官方中文依据，不改） |
| selector | 选择器 | 旧仓库 | 11 | ⚠️ 语料支撑薄；且与 `picker`（官方＝选择器）同形 → **已裁决 §5.5、§5.12：维持**（`picker` 必须标注原文） |
| category | 分类 | 旧仓库 | 7 | ⚠️ 语料支撑薄 → **已裁决 §5.5：维持** |
| extension | 扩展 | 旧仓库 | 约 49（语言义） | ✅ 官方亦用 |
| responder chain | 响应者链 | 旧仓库 | 37 | ✅（「响应链」仅 1） |
| target-action | 目标-动作 | 旧仓库 | 2 | ⚠️ 实际几乎不译（英文 `target-action` 109 次） → **已裁决 §5.5：维持** |
| deprecated | 已废弃 | 旧仓库 | 2 | ⚠️ 实际几乎不译（英文 408 次） → **已裁决 §5.5：维持「已废弃」**（与 `TRANSLATION_STYLE.md` §三 `_(deprecated)_`→`_(已废弃)_` 保持一致，不改成「已弃用」） |

**规则**：上表 34 条译法一律照用。带 ⚠️ 的 8 条经 2026-07-26 裁决**全部维持原译法**——理由统一：这 8 条 Apple 官方中文材料里查不到对照（HIG 不涉及 Objective-C 内存管理与 Core Data 内部概念，WWDC 中文标题/简介也没覆盖），按裁决规则第 3 条「没有官方中文依据的不动」处理。分歧证据（旧规范 vs 实际语料词频）完整保留在第五节 §5.1–§5.5，供日后复查或推翻。

---

## 三、新增术语

### 3.1 Swift 并发

| 英文 | 中文 | 依据来源 | 备注 |
|---|---|---|---|
| Swift concurrency | Swift 并发 | 官方（WWDC22-110351 中文标题） | |
| concurrency | 并发 | 官方 | |
| asynchronous / synchronous | 异步 / 同步 | 官方（WWDC21-10132 中文简介） | |
| async / await | **保留英文** | 官方（中文标题「认识 Swift 中的 async/await」直接保留） | Swift 关键字。「async 函数」「await 一个调用」这样混写即可 |
| structured concurrency | 结构化并发 | 官方（WWDC21-10134 中文标题） | |
| unstructured task | 非结构化任务 | 官方（WWDC21-10134 中文简介） | |
| task | 任务 | 官方 | 类型名 `Task` 保留英文 |
| task group | 任务组 | 官方（WWDC21-10134 中文简介） | 类型名 `TaskGroup` 保留 |
| task cancellation | 任务取消 / 取消任务 | 官方（同上，「如何取消正在进行的任务」） | |
| actor | **Actor**（保留英文，首字母大写） | 官方（WWDC21-10133 中文标题「利用 Swift Actor 保护可变状态」；简介「探索 Actor 如何工作」） | **不译成「角色」「演员」「参与者」**。官方同一页有一处误译「角色隔离」，不采纳 |
| actor isolation | Actor 隔离 | 官方（WWDC21-10133 中文简介） | |
| isolated / nonisolated | **保留英文** | 保留英文 | Swift 关键字 |
| Sendable | **保留英文** | 官方（WWDC22-110351 中文简介「Sendable 检查」） | 协议名 |
| data race | **数据争用** | 官方（择一）（WWDC22-110351 中文标题「消除数据争用」） | **原为「数据竞争」，按官方改为「数据争用」**。官方两说，取更晚更正式的（2022 场次标题 > 2021 场次简介），见 §5.11。`race condition`→竞态条件（社区，无官方）不变 |
| mutable state | 可变状态 | 官方（WWDC21-10133） | |
| atomicity | 原子性 | 官方（WWDC22-110351 中文简介） | |
| protocol conformance | 协议一致性 | 官方（WWDC21-10133 中文简介） | 动词 conform to → 「符合」 |
| completion handler | 完成处理程序 | 官方（WWDC21-10132 中文简介） | 不用「完成回调」 |
| AsyncSequence / AsyncStream | **保留英文** | 官方（WWDC21「认识 AsyncSequence」） | 类型名 |
| distributed actor | 分布式 Actor | 官方（WWDC22 中文标题） | |
| continuation | **保留英文** | 无中文依据 | **已裁决 §5.14：保留英文**。写成「continuation」，首次可加一句解释 |
| suspension point | 挂起点 | 社区 | 与 `hang`→挂起 同字，靠上下文区分 |
| cooperative thread pool | 协作线程池 | 自定 | 无官方依据 |
| GCD / Grand Central Dispatch | **保留英文** | 官方（WWDC17 中文标题保留 `Grand Central Dispatch`） | |
| main thread | 主线程 | 官方（择一）（WWDC20-10077 中文字幕「我们正在主线程上重绘图像 主线程负责渲染用户界面的其余部分」） | 官方另有一处作「主要线程」（WWDC21-10133 中文简介）；取中文字幕正文的「主线程」，见 §5.12 |
| main actor（散文中） | **主要 Actor** | 官方（WWDC21-10133 中文简介） | **原为「主 Actor」，按官方改为「主要 Actor」**（§5.12）。这是本次唯一「跟随官方后与 `main thread`→主线程 构词不一致」的条目，理由见 §5.12 |
| `@MainActor` | **保留英文** | 保留英文 | 属性包装器/属性名，规则 1 |

### 3.2 Swift 语言特性

| 英文 | 中文 | 依据来源 | 备注 |
|---|---|---|---|
| generic / generics | 泛型 | 官方（`/cn/swift/`；WWDC22「采用 Swift 泛型」） | |
| existential type | **既存类型** | 官方（WWDC22-110353 中文简介「如何使用既存类型」） | 社区常写「存在类型」；**已裁决 §5.13：从官方**，首次标注「既存类型（existential type）」 |
| opaque result type | 不透明结果类型 | 官方（WWDC22-110353 中文简介） | `some` / `any` 关键字保留英文 |
| concrete type | 具体类型 | 官方（同上） | |
| same-type requirement | 相同类型要求 | 官方（同上） | |
| parameter pack | 参数包 | 官方（WWDC23 中文标题「使用参数包泛化 API」） | |
| macro | 宏 | 官方（WWDC23「编写 Swift 宏」「深入了解 Swift 宏」） | 具体宏名保留英文：`@Observable` 宏、`#Preview` 宏 |
| value type / reference type | 值类型 / 引用类型 | 官方（`/cn/swift/`「利用值类型」） | |
| optional | 可选值（值）/ 可选类型（类型） | 官方（`/cn/swift/`「借助可选值」「凭借可选类型绑定」） | optional binding→可选绑定；optional chaining→可选链；nil coalescing→nil 合并（均为官方） |
| closure | 闭包 | 官方（`/cn/swift/`） | escaping closure→逃逸闭包（社区）；trailing closure→尾随闭包（社区） |
| property wrapper | 属性包装器 | 社区 | 无官方中文；社区高度一致 |
| result builder | 结果构建器 | 社区 | 无官方中文 |
| associated type | 关联类型 | 社区 | |
| copy-on-write | 写时复制 | 社区 | 首次可标注「写时复制（copy-on-write，COW）」 |
| ownership | 所有权 | 社区 | |
| borrowing / consuming | **保留英文** | 保留英文 | Swift 关键字。作普通英文动词时正常译（"consuming memory"→占用内存） |
| type erasure | 类型擦除 | 社区 | |
| memory safety | 内存安全 | 社区 | |
| exclusivity | 独占访问 | 社区 | |
| inout | **保留英文** | 保留英文 | 关键字 |
| interoperability | 互操作性 | 官方（`/cn/swift/` 语境） | |

### 3.3 SwiftUI

| 英文 | 中文 | 依据来源 | 备注 |
|---|---|---|---|
| view | 视图 | 官方（HIG 组件名「图像视图」「滚动视图」「文本视图」「大纲视图」） | |
| modifier / view modifier | 修饰符 | 官方（HIG 布局页「指定布局修饰符来微调界面中视图的放置」） | |
| observation | 观察 | 官方（WWDC23-10149 中文标题「探索 SwiftUI 中的观察」） | |
| Observable / ObservableObject | **保留英文** | 官方（WWDC23-10149 中文简介「Observable 宏」） | 宏名 / 协议名 |
| state | 状态 | 官方（HIG） | `@State` 保留英文；「`@State` 属性」这样写 |
| binding | 绑定 | 社区 | `@Binding` 保留英文。注意 HIG 里「键绑定」是游戏 key binding，另一回事 |
| environment | 环境 | 官方（HIG「随设备上环境的变化而自动调整」「离开当前环境」） | `@Environment` 保留英文 |
| layout | 布局 | 官方（HIG「布局」） | |
| transition | 过渡 / 过渡效果 | 官方（HIG 动态效果页「自定过渡效果」「追踪过渡效果」） | |
| animation | 动画 | 官方 | |
| stack (VStack/HStack/ZStack) | **叠放** | 官方（WWDC20 中文标题「SwiftUI 中的叠放、网格和大纲」；HIG「智能叠放」=Smart Stack） | **原为未定（社区「堆栈」），按官方改为「叠放」**（§5.9）。类型名 `VStack`/`HStack`/`ZStack` 保留英文。**数据结构的 stack 不受影响**：`call stack`→调用栈、`stack trace`→栈回溯、`stack frame`→栈帧 |
| grid | 网格 | 官方（WWDC20 中文标题「SwiftUI 中的叠放、网格和大纲」） | |
| outline | 大纲 | 官方（同上；HIG「大纲视图」） | |
| declarative | 声明式 | 社区 | |
| preview | 预览 | 官方（HIG「显示文稿的预览」） | |
| preference (SwiftUI `PreferenceKey`) | 偏好 | 自定 | 无官方依据；与「设置（Settings）」区分开 |
| identity (SwiftUI 视图身份) | 视图身份 | 社区 | |

### 3.4 UIKit / 布局 / 渲染

| 英文 | 中文 | 依据来源 | 备注 |
|---|---|---|---|
| scene | **场景** | 官方（HIG 多任务处理页「使用场景和容器视图控制器」） | **`TRANSLATION_STYLE.md` 第 1 版曾把 `Scene` 列入「保留英文」，已按官方改为「场景」**（§5.10）。`UIScene` 等类名保留 |
| container view controller | 容器视图控制器 | 官方（同上） | |
| view controller | **视图控制器** | 官方（HIG 多任务处理页「使用场景和容器视图控制器」） | **原为保留英文 `View Controller`，按官方改为「视图控制器」**（§5.10）。语料 958 次，最高频。`UIViewController` 等类名仍保留英文 |
| collection view | **集合视图** | 官方（Tech Talk 10855 中文转写「我们来观察一下滚动集合视图的常见例子」） | **原为保留英文 `Collection View`，按官方改为「集合视图」**（§5.10）。语料 281 次。`UICollectionView` 类名保留 |
| table view | **表格视图** | 官方派生（HIG `table`=表格 + `view`=视图） | **原为保留英文，按官方派生改为「表格视图」**（§5.10）。语料 258 次。`UITableView` 类名保留 |
| scroll view | **滚动视图** | 官方（HIG 组件名「滚动视图」；Tech Talk 10855 中文转写「滚动视图会随着上移内容作出响应」） | **原为保留英文 `Scroll View`，按官方改为「滚动视图」**（§5.10）。`UIScrollView` 类名保留 |
| navigation controller | **导览控制器** | 官方派生（navigation=导览 + controller=控制器） | 见 §5.6。`UINavigationController` 类名保留英文；组件 `navigation bar`→**导航栏**（官方例外，见下） |
| navigation bar | **导航栏** | 官方（HIG 工具栏页「在 iOS 中，导览特定的工具栏有时会称为导航栏」） | **`navigation`→导览 的唯一官方例外**：这个具体组件官方就叫「导航栏」，不要改成「导览栏」 |
| view hierarchy | 视图层级结构 | 官方（HIG 手势页、模态化页） | |
| first responder | 第一响应者 | 社区（承接旧表「响应者链」） | |
| hit-testing | 命中测试 | 社区 | 无官方中文 |
| safe area | **安全区** | 官方（HIG 布局页「安全区 定义了视图内不会被工具栏、标签页栏或者窗口可能提供的其他视图遮挡的区」） | **不用「安全区域」** |
| layout guide | 布局指南 | 官方（HIG 布局页「布局指南 定义了一个矩形区域」） | |
| margin / layout margin | 外边距 | 官方（HIG 布局页「系统定义的安全区、外边距和指南」） | |
| size class | 尺寸类别 | 官方（HIG 拖放/iPad 页「所有尺寸类别和方向」） | |
| adaptivity / adaptive layout | 适配性 / 自适应布局 | 官方（HIG 布局页「界面的高适配性」） | |
| trait collection | 特性集合 | 自定（承接旧表 attribute→特性） | 无官方中文 |
| Auto Layout | **保留英文** | 无中文依据 | **已裁决 §5.15：保留英文**（HIG layout 页中文全文无对照；是技术名而非普通短语） |
| Dynamic Type | 动态字体 | 官方（HIG 布局页/字体排印页「动态字体 这项功能」） | 产品级功能名，可加引号「动态字体」 |
| Dark Mode | 深色模式 | 官方（HIG「深色模式」） | |
| material | 材质 | 官方（HIG「材质」） | |
| **Liquid Glass** | **保留英文** | 官方（HIG 材质页通篇直接写 `Liquid Glass`，未译） | **不要写「液态玻璃」** |
| vibrancy | 虚化 | 官方（HIG 材质页「虚化颜色」「虚化效果」） | 反直觉但是官方定译 |
| blur | 模糊 | 官方（HIG 材质页） | |
| blending mode | 融合模式 | 官方（HIG 材质页「两种融合背景内容的模式」） | |
| scroll edge effect | 滚动边缘效果 | 官方（HIG 材质页） | |
| translucency / opacity | 半透明 / 不透明度 | 官方（HIG 材质页） | |
| render loop | 渲染循环 | 官方（Tech Talk 中文标题「探索 UI 动画阻碍与渲染循环」） | |
| frame（画面帧） | 帧 | 官方（WWDC20-10077 中文字幕） | 与 `frame`（视图矩形）区分：后者作「frame」保留或译「框架矩形」 |
| dropped frame | 掉帧 | 官方（WWDC20-10077 中文字幕） | |
| VSYNC | **保留英文** | 官方（WWDC20-10077 中文字幕保留） | |
| hitch | **卡顿** | 官方（择一）（Tech Talk 10855 中文转写全文：「什么是卡顿？」「任何时候屏幕上出现 晚于预计的帧都属于卡顿」；WWDC20-10077 中文**简介**亦作「如果动画效果出现卡顿」） | **已裁决 §5.7**。官方三说：卡顿 / 障碍（WWDC20-10077 字幕）/ 阻碍（Tech Talk 10855 标题）。取「卡顿」——最晚、最系统。派生：`hitch time`→卡顿时长、`hitch ratio`→卡顿率、`commit hitch`→提交卡顿、`render hitch`→渲染卡顿（均见官方转写）。首次标注「卡顿（hitch）」 |
| hang | **挂起** | 官方（择一）（WWDC21-10258「了解和消除 app 挂起」；WWDC23-10248「使用 Instruments 分析挂起」） | **已裁决 §5.8**。官方另有一处作「卡顿」（WWDC22 标题）——**不采纳，否则与 `hitch`→卡顿 撞车**。与 Swift `suspension point`→挂起点 同字，靠上下文区分 |
| frame pacing | 帧节奏 | 自定 | WWDC20-10077 字幕用「节奏」「步频」描述帧节拍，未定名 |
| offscreen rendering | 离屏渲染 | 社区 | 无官方中文 |
| compositing | 合成 | 社区 | |
| rasterize | 光栅化 | 社区 | |
| layer（`CALayer`） | 图层 | 社区 | `CALayer` 类名保留 |
| layer tree | 图层树 | 社区 | |
| memory footprint | 内存占用空间 | 官方（WWDC18-416 中文简介） | |
| anti-pattern | 反面模式 | 官方（WWDC21-10258 中文简介） | |
| regression（性能/功能退化） | 衰退 | 官方（WWDC21 中文标题「诊断 app 中的功能和性能衰退」） | |
| diffable data source | 可差分数据源 | 自定 | 无官方中文；首次标注原文 |
| snapshot（数据源快照） | 快照 | 社区 | |
| compositional layout | 组合式布局 | 自定 | 无官方中文；首次标注原文 |
| cell | 单元格 | 社区 | `UICollectionViewCell` 类名保留 |
| state restoration | 状态恢复 | 社区 | |
| gesture / gesture recognizer | 手势 / 手势识别器 | 官方（HIG「手势」） | |
| drag and drop | 拖放 | 官方（HIG「拖放」） | |
| haptics / haptic feedback | 触感反馈 | 官方（HIG「提供触感反馈」） | |
| focus | 焦点（名词）/ 聚焦（动作、效果） | 官方（HIG「聚焦和选择」；「获得焦点的项目」「聚焦效果」） | ⚠️ 「聚焦」也是 Spotlight 的官方中文名，靠上下文区分 |
| hover effect | 悬停效果 | 官方（HIG 聚焦和选择页） | |
| parallax effect | 视差效果 | 官方（HIG 聚焦和选择页、图像页） | |
| modality / modal | 模态化 / 模态 | 官方（HIG「模态化」；「模态视图」） | |
| presentation | 呈现方式（名词）/ 呈现（动词） | 官方（HIG 组件分组「呈现方式」） | |

### 3.5 UI 组件官方中文名（Apple HIG 定译，一律照用）

以下全部来自 Apple 官方中文《人机界面指南》的组件页标题，是**最硬的依据**。经 2026-07-26 裁决，**本节整表照用，不再有例外**。

| 英文 | 中文 | | 英文 | 中文 |
|---|---|---|---|---|
| control | **控制**（**不是「控件」**，§5.6） | | popover | 弹出窗口 |
| sheet | 表单（§5.12，首次标注原文） | | alert | 提醒 |
| action sheet | 操作表单 | | picker | 选择器（§5.12，**必须**标注原文） |
| toggle | 切换 | | slider | 滑块 |
| stepper | 步进器 | | segmented control | 分段控制 |
| page control | 页面控制 | | disclosure control | 显示控制 |
| pop-up button | 弹出式按钮 | | pull-down button | 下拉式按钮 |
| tab bar / tab view | 标签页栏 / 标签页视图 | | sidebar | 边栏 |
| toolbar | 工具栏 | | status bar | 状态栏 |
| menu bar | 菜单栏 | | context menu | 上下文菜单 |
| edit menu | 编辑菜单 | | Dock menu | 程序坞菜单 |
| split view | 拆分视图 | | scroll view | **滚动视图**（§5.10，不再保留英文） |
| column view | 分栏视图 | | outline view | 大纲视图 |
| image view | 图像视图 | | web view | 网页视图 |
| text view / text field | 文本视图 / 文本栏 | | search field | 搜索栏 |
| label | 标签 | | box | 方框 |
| collection | 集合（`collection view`→**集合视图**） | | list / table | 列表 / 表格（`table view`→**表格视图**） |
| progress indicator | 进度指示符 | | rating indicator | 评分指示符 |
| gauge | 仪表 | | chart | 图表 |
| color well / image well | 颜色池 / 图像池 | | combo box | 组合框 |
| window | 窗口 | | panel | 面板 |
| ornament | 挂饰 | | lockup | 联锁 |
| activity view | 活动视图 | | navigation | **导览**（**不是「导航」**，§5.6；例外：`navigation bar`→导航栏） |

### 3.6 系统体验 / 产品功能名（Apple 官方中文）

| 英文 | 中文 | 依据来源 | 备注 |
|---|---|---|---|
| widget | 小组件 | 官方（HIG「小组件」） | `WidgetKit` 框架名保留 |
| Live Activity | 实时活动 | 官方（HIG「实时活动」） | `ActivityKit` 保留 |
| Dynamic Island | 灵动岛 | 官方（HIG 布局页） | |
| Smart Stack | 智能叠放 | 官方（HIG 手势页） | |
| complication | 复杂功能 | 官方（HIG「复杂功能」） | |
| watch face | 表盘 | 官方（HIG「表盘」） | |
| App Clip | 轻 App | 官方（HIG「轻 App」） | |
| notification | 通知 | 官方（HIG「通知」） | |
| Quick Look | 快速查看 | 官方（HIG 文件管理页） | |
| Spotlight | 聚焦 | 官方（HIG 文件管理页「访达、『文件』和『聚焦』」） | 产品名，加引号 |
| Finder | 访达 | 官方（同上） | |
| VoiceOver | 旁白 | 官方（HIG「旁白」） | 加引号「旁白」 |
| accessibility | **辅助功能** | 官方（择一）（`apple.com.cn/accessibility` 主标题「Apple 辅助功能」；iPhone 使用手册章节「iPhone 上的辅助功能使用入门」「在 iPhone 上快速打开或关闭辅助功能」；iOS 中文界面「设置 › 辅助功能」） | **原为「无障碍」，按官方改为「辅助功能」**（§5.16）。HIG 中文页两词并用（章节标题「无障碍」、正文亦出现「辅助功能」「辅助技术」）；按用户裁决以 iOS 系统界面用词为权威。派生：`accessibility label`→辅助功能标签、`accessibility element`→辅助功能元素。**引用 HIG 那一章的标题时照原样写「无障碍」** |
| assistive technology | 辅助技术 | 官方（HIG 辅助功能页「支持肢体活动能力相关的辅助技术」） | |
| Switch Control | 切换控制 | 官方（HIG 辅助功能页） | |
| Assistive Access | 辅助访问 | 官方（HIG 辅助功能页） | |
| `Accessibility`（框架名）/ `Accessibility Inspector`（工具名） | **保留英文** | 官方（HIG 辅助功能页中文正文原样写 `Accessibility Inspector`：「使用 Accessibility Inspector 高亮标记界面相关的无障碍问题」） | 规则 2 |
| SF Symbols | SF 符号（概念）/ `SF Symbols`（App 名） | 官方（HIG「SF 符号」） | |
| Scribble | 随手写 | 官方（HIG「Apple Pencil 和随手写」） | |
| Digital Crown | 数码旋钮 / 表冠 | 官方（HIG） | |
| SharePlay | 同播共享 | 官方（HIG「同播共享」） | |
| AirPlay | 隔空播放 | 官方（HIG「隔空播放」） | |
| Sign in with Apple | 通过 Apple 登录 | 官方（HIG） | |
| Always On | 全天候显示 | 官方（HIG） | |
| Live Photo | 实况照片 | 官方（HIG） | |
| Top Shelf | 推荐项目 | 官方（HIG） | |
| snippet | 摘要卡片 | 官方（HIG） | |
| App Shortcuts | App 快捷指令 | 官方（HIG） | |
| Home Screen quick action | 主屏幕快速操作 | 官方（HIG） | |
| onboarding | 用户引导 | 官方（HIG「用户引导」） | |
| Face ID / Touch ID / Optic ID | 面容 ID / 触控 ID / 视控 ID | 官方（HIG 隐私页） | |
| Apple Pay / Wallet | Apple Pay / 钱包 | 官方（HIG） | |
| **app**（应用程序） | **App** | 官方（Apple 中文全线用 `App`，不用「应用」「应用程序」） | 大写 A，前后加空格 |

### 3.7 启动 / 链接 / 二进制

本领域官方中文依据最薄。除下表明确标注「官方」的，其余谨慎使用。

| 英文 | 中文 | 依据来源 | 备注 |
|---|---|---|---|
| launch | 启动 | 官方（WWDC19-423 中文标题「优化 App 启动」） | |
| launch time | 启动时间 | 官方（WWDC22-110362 中文标题「缩短构建和启动时间」） | |
| build time | 构建时间 | 官方（同上） | |
| link / linking | 链接 | 官方（WWDC22-110362 中文简介「运行时链接性能」） | |
| linker | 链接器 | 社区 | static/dynamic linker → 静态/动态链接器 |
| static library / dynamic library | 静态库 / 动态库 | 社区 | |
| mergeable library | 可合并库 | 官方（WWDC23 中文标题「认识可合并库」） | |
| framework | 框架（泛指）/ 保留英文（具名时） | 官方 + 旧规范 | `UIKit`、`Foundation` 等具体框架名一律保留 |
| dyld | **保留英文** | 无中文依据 | |
| Mach-O | **保留英文** | 格式名 | |
| dyld shared cache | dyld 共享缓存 | 自定（`shared cache`→共享缓存为社区通行） | |
| chained fixups | **保留英文** | 无任何中文依据 | 首次可加解释性说明，不要自造译名 |
| rebase / bind（dyld 动作） | **保留英文** | 无统一中文 | 与 git rebase 无关，不要译「变基」 |
| lazy binding | 延迟绑定 | 社区 | |
| prewarming | **保留英文** | 无中文依据 | **已裁决 §5.14：保留英文**（HIG 全 37 页中文正文 grep「预热」0 命中）。首次可加解释性说明 |
| code signing | 代码签名 | 社区 | |
| entitlement | **保留英文** | 无中文依据 | **已裁决 §5.14：保留英文**（社区有「授权文件」「权限」，都不准确） |
| symbol / symbol table | 符号 / 符号表 | 社区 | 与 SF 符号语境区分 |
| dSYM / symbolication | dSYM / 符号化 | 社区 | |

### 3.8 系统 / 存储 / 后台

| 英文 | 中文 | 依据来源 | 备注 |
|---|---|---|---|
| App Sandbox / sandbox | App 沙盒化 / 沙盒 | 官方（HIG 隐私页「通过 App 沙盒化保护用户的数据。沙盒化可让你的 App…」） | |
| Keychain | 钥匙串 | 官方（HIG 隐私页「将敏感信息储存在钥匙串中」、数据输入页「钥匙串认证」） | `Keychain Services` 框架名保留 |
| background task | 后台任务 | 官方（WWDC22 中文标题「SwiftUI 中的『后台任务』」） | `BackgroundTasks` 框架名保留 |
| background execution | 后台运行 | 官方（HIG 轻 App 页「执行后台操作」） | |
| expiration handler | 到期处理程序 | 自定（对齐官方 handler→处理程序） | |
| authentication / authorization | 认证 / 授权 | 官方（HIG 隐私页「钥匙串认证」「自定认证方案」） | |
| privacy | 隐私 | 官方（HIG「隐私」） | |
| privacy manifest | **保留英文** | 无中文依据 | **已裁决 §5.14：保留英文**（HIG privacy 页中文全文 grep「隐私清单」0 命中）。首次可加解释性说明 |
| App Group | **保留英文** | 无官方中文 | |
| document | **文稿** | 官方（HIG 文件管理页「文稿启动器」「打开文稿」「文稿的预览」） | ⚠️ 与 `documentation`→文档 严格区分 |
| documentation | 文档 | 官方（HIG 页脚导航「文档」） | |
| container（App 容器/文件系统） | 容器 | 社区 | 与「容器视图控制器」的 container 同字 |
| user defaults / `UserDefaults` | **保留英文** | API 名 | |
| file coordination | 文件协调 | 社区 | |
| data protection | 数据保护 | 社区 | |
| encryption | 加密 | 官方（HIG 隐私页「加密的钥匙串」） | |

### 3.9 Xcode / App 图标

| 英文 | 中文 | 依据来源 | 备注 |
|---|---|---|---|
| alternate app icon | 备用 App 图标 | 项目既有译文（Xcode 构建设置参考及关联页面） | 不用「备选 App 图标」 |
| Alternate App Icon Sets | 备用 App 图标集 | 项目既有译文（Xcode 构建设置参考） | 作为 Xcode 构建设置名时，首次写成「备用 App 图标集（Alternate App Icon Sets）」 |
| project navigator | 项目导航器 | 项目既有译文 | 常用界面名称，无需单独附英文 |
| source control | 源代码管理 | 项目既有译文 | 不用「源代码控制」 |
| Thread Sanitizer | **保留英文** | Xcode 工具名 / 项目既有多数译文 | 不译成「线程消毒器」 |
| Undefined Behavior Sanitizer | **保留英文** | Xcode 工具名 / 项目既有多数译文 | 不译成「未定义行为消毒器 / 清理器」 |

---

## 四、一律保留英文（含判断规则）

### 4.1 判断规则（按顺序套用）

**规则 1｜标识符原则：任何能被编译器识别的名字，一律保留英文，一个字符都不改。**
包括：类名、结构体、枚举、协议名、方法名、函数名、属性名、变量名、常量名、通知名、枚举 case、宏名、关键字、属性包装器名、编译器指令、KVC 键名。
判定方法：**如果把它译成中文，代码就编译不过 / 就搜不到了 → 保留英文。**
例：`NSTimer`、`UIViewController`、`invalidate`、`setDelegate:`、`Sendable`、`@MainActor`、`@Observable`、`some`、`any`、`async`、`await`、`actor`、`isolated`、`borrowing`、`consuming`、`inout`、`#Preview`、`UIApplicationDidFinishLaunchingNotification`。

**规则 2｜框架名与产品名原则：Apple 自己在中文材料里不译的名字，你也不译。**
- 框架 / 库：`Foundation`、`UIKit`、`AppKit`、`SwiftUI`、`SwiftData`、`Core Data`、`Core Animation`、`QuartzCore`、`Metal`、`Combine`、`WidgetKit`、`ActivityKit`、`StoreKit`、`CryptoKit`、`Dispatch`、`os`、`Security`。
- 工具 / 平台：`Xcode`、`Swift`、`Objective-C`、`Instruments`、`TestFlight`、`Interface Builder`、`Simulator`、`LLDB`、`Swift Playgrounds`、`App Store`、`Xcode Cloud`。
- 系统名：`iOS`、`iPadOS`、`macOS`、`watchOS`、`tvOS`、`visionOS`。
- 设计语言：**`Liquid Glass`**（官方中文文档确认不译）。
- 技术名：`Grand Central Dispatch` / `GCD`、`ARC`、`KVO`、`KVC`、`dyld`、`Mach-O`、`VSYNC`、`SF Symbols`（作 App 名时）。

**规则 3｜代码环境原则：代码块内部、行内代码反引号内部，除注释外一律不动。**
代码注释译成中文；字符串字面量不译；缩进、空行、标识符全部保持。

**规则 4｜无依据原则：查不到官方中文、社区也无共识、又是核心概念的，保留英文而不是自创。**
当前落在这条的：`chained fixups`、`rebase`/`bind`（dyld 动作）、`continuation`、`App Group`、`entitlement`、`privacy manifest`、`prewarming`、`Auto Layout`、`Sendable`、`AsyncSequence`、`AsyncStream`、`Observable`。

**规则 5｜工具与文件格式名：** `Interface Builder`、`Storyboard`、`nib`、`XIB`。这四个是 Xcode 的工具名与文件格式名（`.storyboard` / `.nib` / `.xib` 是真实存在的文件后缀），Apple 中文材料也不译。

> **⚠️ 第 2 版重要变更**：第 1 版的规则 5 还包含 `Collection View`、`Scroll View`、`View Controller`（连同 `TRANSLATION_STYLE.md` 里的 `Scene`）。**这几条已按 Apple 官方中文全部改为译成中文**——集合视图、滚动视图、视图控制器、场景，见 §5.10。它们**不再属于「保留英文」**。
>
> 仍然保留英文的只有对应的**类名**：`UICollectionView`、`UIScrollView`、`UIViewController`、`UIScene`（规则 1 标识符原则）。散文里的 `a view controller` 一律写「一个视图控制器」。

### 4.2 一个反例（不要过度保留）

`delegate`、`property`、`protocol`、`extension`、`selector`、`category`、`block` 这些**既是概念也是关键字**的词：
- 出现在**散文里指概念** → 按第二节译（委托、属性、协议、扩展、选择器、分类；`block` 例外，保留英文）。
- 出现在**代码里 / 反引号里 / 指关键字本身** → 保留英文。
- 例：`委托（delegate）对象负责……` ✅ ／ `用 @property 声明` ✅ ／ ~~`用 @属性 声明`~~ ❌

---

## 五、已裁决记录（2026-07-26）

第 1 版列在这里的 16 条待裁决，**已按用户裁决「术语表按 Apple 官方中文来」全部处理完毕**，结论已合并进第二、三、四节。

**本节是复查档案，不是查表用的。** 每条保留：分歧点 → 两个（或更多）候选 → 依据来源 → **最终选择与理由** → 落到正文哪里。日后若要推翻某条，改这里 + 改对应正文表格两处。

### 5.0 裁决汇总

| # | 术语 | 第 1 版 | **第 2 版（最终）** | 裁决规则 |
|---|---|---|---|---|
| 5.1 | accessor | 存取方法 | 存取方法（**维持**） | 规则 3：无官方依据不动 |
| 5.2 | retain | 保留 | 保留（**维持**） | 规则 3 |
| 5.3 | attribute / property | 特性 / 属性 | 特性 / 属性（**维持**） | 规则 3 |
| 5.4 | block | 保留英文 | 保留英文（**维持**） | 规则 3 |
| 5.5 | target-action / deprecated / category / selector / reference counting | 旧规范译法 | 旧规范译法（**维持**，含 deprecated→已废弃） | 规则 3 |
| 5.6 | control / navigation | 控件 / 导航（社区） | **控制 / 导览**（改） | 规则 1：官方优先 |
| 5.7 | hitch | 卡顿（暂定，标社区理由） | **卡顿**（确认，依据升级为官方） | 规则 2：官方三说取更晚 |
| 5.8 | hang | 挂起 | 挂起（**维持**，依据说明加强） | 规则 2：官方两说取更晚 |
| 5.9 | stack（VStack 等） | 未定 | **叠放**（改） | 规则 1 |
| 5.10 | view controller / collection view / table view / scroll view / scene | 保留英文 | **视图控制器 / 集合视图 / 表格视图 / 滚动视图 / 场景**（改） | 规则 1 |
| 5.11 | data race | 数据竞争 | **数据争用**（改） | 规则 2：官方两说取更晚更正式 |
| 5.12 | sheet↔form、picker↔selector、main actor | 见下 | sheet=表单 / picker=选择器（标原文）/ **主要 Actor**（改） | 规则 1 |
| 5.13 | existential type | 既存类型 | 既存类型（**维持**） | 规则 1 |
| 5.14 | 8 条无中文依据项 | 保留英文 | 保留英文（**维持**，`privacy manifest`/`prewarming` 从「待定」定为保留英文） | 规则 3 / 4 |
| 5.15 | Auto Layout | 保留英文 | 保留英文（**维持**） | 规则 4 |
| 5.16 | accessibility | 无障碍 | **辅助功能**（改） | 规则 1 + 用户指定权威 |

**改动 8 条（5.6、5.7 依据升级、5.9、5.10、5.11、5.12 之 main actor、5.16，以及 5.14 中两条从「待定」定案），维持 8 条。剩余未决项：0。**

**「官方自相矛盾、需要说明选择理由」的 4 条：§5.7 `hitch`、§5.8 `hang`、§5.11 `data race`、§5.16 `accessibility`**（另有 §5.12 的 `main thread` / `main actor` 构词不一致，一并说明）。

---

### 5.1 `accessor` — 存取方法 vs 访问器 → **维持「存取方法」**

- **分歧点**：旧规范定「存取方法」，但旧仓库实际用「访问器」**75** 次、「存取方法」**29** 次、「访问方法」9 次，三分天下。集中在 `vault/documentation/Cocoa/Key-Value Coding Programming Guide/`。
- **候选**：① 存取方法（旧规范）② 访问器（实际语料 2.6:1 占优，且现代中文技术写作更通行）
- **依据来源**：**Apple 官方中文查无此词**——HIG 不涉及 Objective-C 存取方法，WWDC 中文标题/简介亦无。属规则 3。
- **最终选择**：**存取方法**（维持第 1 版）。理由：裁决只覆盖「有官方依据」的条目；本条无官方依据，按规则 3 不动。
- **⚠️ 留给复查的分歧**：这是「旧规范 vs 实际语料词频」冲突最大的一条——语料是 75:29 倒向「访问器」。如果日后想让新语料跟随实际用词而非规范文字，这条是第一顺位候选。改的话要同时改 §2 表格。
- **落点**：§2 表格 `accessor` 行。

### 5.2 `retain` — 保留 vs 持有 → **维持「保留」**

- **分歧点**：旧仓库「持有」**91** 次 > 「保留」**79** 次。`release`→「释放」208 次无争议。
- **候选**：① 保留（旧规范）② 持有（语料略占优，语义更贴 ARC 语义）
- **依据来源**：**无官方中文**（Apple 中文材料不涉及 MRC 内存管理动词）。属规则 3。
- **最终选择**：**保留**（维持）。理由同 §5.1。
- **⚠️ 留给复查的分歧**：91:79 的差距不大但方向明确；「保留」在中文里还有「retain 之外的日常义」，容易和 `reserved`/`preserve` 混。
- **落点**：§2 表格 `retain / release` 行。

### 5.3 `attribute` vs `property` 都译「属性」 → **维持旧规范表述**

- **分歧点**：「属性」1121 次，「特性」仅 44 次，且 Core Data 同一文件内两者混用（`Core Data Programming Guide/KeyConcepts.md` 等）。旧规范的「属性字符串语境用属性 / 其余用特性」在实际译文里没被守住。
- **候选**：① 沿用旧规范表述 ② 明确二分：Core Data / XML 语境 `attribute`→「特性」，`property`→「属性」，首次均标注原文
- **依据来源**：**无官方中文**可裁（HIG 无 Core Data 内容）。属规则 3。
- **最终选择**：**沿用旧规范表述**（维持）。
- **⚠️ 留给复查的分歧**：这条本质上是「规范没被执行」而不是「规范错了」。真正需要防范的是同一页里 `attribute` 和 `property` 都写成「属性」导致读者分不清——所以**实操上仍要求首次出现时标注原文**（`特性（attribute）` / `属性（property）`），这一点已在 §1.3 覆盖。
- **落点**：§2 表格 `attribute` 行。

### 5.4 `block` — 保留英文 vs 「块」 → **维持保留英文**

- **分歧点**：规范说保留英文（英文 `block` 2274 次），但中文「块」实际约 113 次，其中「自动释放池块」35 次、「代码块」11 次。
- **候选**：① 一律保留英文 ② `block` 单独出现保留英文，固定搭配 `autorelease pool block`→「自动释放池块」照旧译文
- **依据来源**：**无官方中文**。属规则 3 / 4（`block` 也是 Objective-C 关键字 `^`-语法的概念名）。
- **最终选择**：**保留英文 `block`**（维持）。2274:113 的比例足以说明这就是既成事实。
- **⚠️ 留给复查的分歧**：旧仓库里那 113 处中文「块」（尤其「自动释放池块」35 次）属**旧语料的既成事实，不回改**；新语料统一写「自动释放池 block」或直接 `autorelease pool block`。这是新旧仓库有意分歧的一个小样本。
- **落点**：§2 表格 `block` 行；§4.2 反例。

### 5.5 语料几乎不支撑的 5 条继承术语 → **全部维持**

- **分歧点**：`target-action`→目标-动作（仅 2 次，英文 109 次）、`deprecated`→已废弃（仅 2 次，英文 408 次）、`category`→分类（7 次）、`selector`→选择器（11 次）、`reference counting`→引用计数（12 次）。这几条是「规范写了但译者基本没用」。
- **候选**：① 全部按旧规范 ② `deprecated`→改成更通行的「已弃用」，其余维持
- **依据来源**：**无官方中文**。属规则 3。
- **最终选择**：**全部按旧规范**，包括 `deprecated`→**已废弃**。
  - 追加理由（这条不只是「无依据不动」）：`TRANSLATION_STYLE.md` 第三节的结构性文字对照表**已经**把 `_(deprecated)_` 固定成 `_(已废弃)_`、`> [!warning] Deprecated` 固定成 `已废弃`。`deprecated` 在现行文档里极高频（API 弃用标注遍布），若正文写「已弃用」而结构性标记写「已废弃」，会在同一页面里制造两个词。**一致性优先于「哪个更通行」。**
- **落点**：§2 表格对应 5 行；`TRANSLATION_STYLE.md` §三（无需改动，已一致）。

### 5.6 `control`→控制 / `navigation`→导览 ★ → **改用官方「控制」「导览」**

- **分歧点**：官方与社区完全对立，且这两个词在 UIKit 文档里极高频。
- **候选**：
  - ① **官方**：「控制」「导览」。HIG 组件页标题即「控制」，派生「分段控制」「页面控制」「显示控制」；分区标题「导览和搜索」，材质页「控制和导览」，工具栏页「包含导览控制的工具栏出现在窗口顶部」「专用于在 App 的各区域间导览」。
  - ② **社区**：「控件」「导航」。中文 iOS 开发社区几乎 100% 这么说（`UINavigationController`=导航控制器）。
  - ③ 第 1 版曾提出的「分层处理」（HIG 类文档用官方、API 文档用社区）——**已否决**，那会在同一 vault 里制造两套词。
- **依据来源**：官方（HIG 中文组件页、导览和搜索页、材质页、工具栏页）。
- **最终选择**：**官方「控制」「导览」，全库统一**。用户裁决明确：有官方依据就用官方，即使与社区惯例冲突。
- **两个例外（必须记住）**：
  1. 具体组件 `navigation bar` 官方叫「**导航栏**」，不是「导览栏」。HIG 工具栏页原话：「在 iOS 中，导览特定的工具栏有时会称为**导航栏**。」即：**行为/概念用「导览」，那个具体控件用「导航栏」。**
  2. 渲染器面包屑行 `> Navigation: `→「`> 导航：`」**不改**（`TRANSLATION_STYLE.md` §三 结构性文字对照表）。理由：那不是 Apple 的术语，是本项目抓取器生成的行首标记，已被 `tools/validate.py` 与既有译文锁定；改它等于批量改所有已译文件，收益为零。
- **可预见的副作用（已接受）**：`navigation controller`→「导览控制器」、`navigation stack`→「导览叠放」这类派生词读起来会和中文社区习惯不同。类名 `UINavigationController`、`NavigationStack` 一律保留英文，所以搜索性不受影响。
- **落点**：§1.4 陷阱 5；§3.4（navigation controller / navigation bar 两行）；§3.5 组件表 control、navigation 两格。

### 5.7 `hitch` ★ → **「卡顿」**（官方自相矛盾，已选定并说明理由）

**官方中文有三种叫法**，全部在本次复核中确认：

| 官方译法 | 出处 | 时间 | 性质 |
|---|---|---|---|
| 「**障碍**」 | WWDC20-10077《使用 XCTest 消除动画障碍》中文**标题 + 中文字幕**：「我们将这些用户可感知的抖动称为『障碍』」「当帧错过预期的 VSYNC 时 就会出现障碍」，派生「障碍时间」「障碍比率」 | 2020-06 | 标题 + 字幕 |
| 「**阻碍**」 | Tech Talk 10855《探索 UI 动画阻碍与渲染循环》中文**标题** + 简介「找出在你 App 里卷动轴与动画的阻碍」 | 2020-12 | 仅标题/简介，且该简介中文质量明显偏低（「卷动轴」= scroll，非规范用词） |
| 「**卡顿**」 | ① WWDC20-10077 中文**简介**：「但如果动画效果出现卡顿，则可能破坏用户体验」<br>② Tech Talk 10855 中文**转写文稿全文**：「什么是卡顿？」「任何时候屏幕上出现 晚于预计的帧都属于卡顿」「卡顿的出现是由于渲染循环 没有按时完成一帧」「提交卡顿发生在 app 的处理中」「渲染卡顿 发生在渲染服务器中」 | 2020-06 / 2020-12 | 简介 + **整篇转写文稿** |

- **最终选择**：**卡顿**。
- **选择理由（三条，按权重）**：
  1. **更晚**：Tech Talk 10855（2020 年 12 月）晚于 WWDC20-10077（2020 年 6 月），而它的**正文转写通篇用「卡顿」**，标题的「阻碍」只是一处孤例。
  2. **更系统**：只有「卡顿」这一支在官方材料里长出了完整的派生词族——**提交卡顿**（commit hitch）、**渲染卡顿**（render hitch）、卡顿时长、卡顿率。「障碍」只派生出「障碍时间」「障碍比率」，「阻碍」一个派生词都没有。
  3. **跨来源交叉支持**：连 WWDC20-10077 自己的中文**简介**都写「卡顿」，与它自己字幕里的「障碍」矛盾。也就是说「卡顿」在两个不同场次、两种不同材料里都出现，「障碍」「阻碍」各只属于一个来源。
- **附带好处**（不作为主要理由）：「卡顿」与中文社区通行说法一致；而「障碍」在中文里完全丧失了「画面延迟」的意象，「阻碍」更像 obstruction。
- **落记的两个变体**：「障碍」（WWDC20-10077 字幕）、「阻碍」（Tech Talk 10855 标题）。**遇到引用这两个官方标题时照抄原标题，不要改写**；正文一律「卡顿」。
- **落点**：§3.4 `hitch` 行；§1.4 陷阱 7。

### 5.8 `hang` — 挂起 vs 卡顿 → **「挂起」**（官方自相矛盾，已选定并说明理由）

- **分歧点**：官方两说。
  - 「**挂起**」：WWDC21-10258《了解和消除 app 挂起》、WWDC23-10248《使用 Instruments 分析挂起》——两个中文场次标题。
  - 「**卡顿**」：WWDC22《Track down hangs…》中文标题《利用 Xcode 和设备端检测对卡顿进行跟踪》。
- **最终选择**：**挂起**。
- **选择理由**：
  1. **更晚**：WWDC23-10248（2023）晚于 WWDC22 那一场，且用「挂起」。
  2. **数量与一致性**：官方两处用「挂起」、仅一处用「卡顿」。
  3. **避免撞车（决定性）**：§5.7 已把 `hitch` 定为「卡顿」。`hitch`（掉几帧，毫秒级）和 `hang`（主线程被卡住，数百毫秒到数秒）是**两个不同的性能问题**，Apple 英文文档严格区分。如果两者都叫「卡顿」，整个性能章节就没法读了。
- **落记的变体**：「卡顿」（WWDC22 中文标题）。引用该标题时照抄。
- **注意同字冲突**：Swift 并发的 `suspension point`→「挂起点」与本条同字，靠上下文区分（一个是性能故障，一个是 async 语义），首次出现均标注原文。
- **落点**：§3.4 `hang` 行；§3.1 `suspension point` 行；§1.4 陷阱 7。

### 5.9 `stack`（VStack/HStack/ZStack）— 叠放 vs 堆栈 → **改用官方「叠放」**

- **分歧点**：官方「叠放」vs 社区「堆栈」。
- **依据来源**：官方 —— WWDC20 中文标题《SwiftUI 中的叠放、网格和大纲》；HIG「智能叠放」= Smart Stack。
- **最终选择**：**叠放**（SwiftUI 布局容器语境）。
- **理由**：有官方依据，按规则 1；且顺带避免与数据结构 stack（栈）混淆。
- **明确不受影响的**：`call stack`→调用栈、`stack trace`→栈回溯、`stack frame`→栈帧、`stack memory`→栈内存。类型名 `VStack`/`HStack`/`ZStack`/`NavigationStack` 保留英文。
- **落点**：§3.3 `stack` 行。

### 5.10 复合概念：保留英文 vs 官方中文 ★ → **全部改用官方中文**

- **分歧点**：全项目最高频的术语簇，选错代价最大。
  - 第 1 版（继承旧规范）：保留 `Collection View`、`Scroll View`、`View Controller`（`TRANSLATION_STYLE.md` 里还多列了 `Scene`）。
  - Apple 官方中文：**视图控制器、集合视图、滚动视图、场景**。
- **依据来源（本次新增了两条硬证据）**：
  - HIG 多任务处理页中文：「探究如何使用**场景和容器视图控制器**让你的 UIKit App…」→ scene=场景、container view controller=容器视图控制器、view controller=视图控制器。
  - HIG 组件页中文：「**滚动视图**」为组件标题；`collection`=集合。
  - **Tech Talk 10855 中文转写文稿**（本次复核新查到）：「我们来观察一下滚动**集合视图**的常见例子」「当用户在屏幕上滑动手指时 **滚动视图**会随着上移内容作出响应」——这是 Apple 自己在**散文正文**里译这两个词，比组件标题更有说服力。
- **语料频次（选错代价的量化）**：`view controller` **958** 次、`gesture recognizer` 355、`collection view` **281**、`table view` **258**、`scene` 389。
- **最终选择**：**视图控制器 / 集合视图 / 表格视图 / 滚动视图 / 场景**，全部译成中文。
  - `table view`→表格视图 是**官方派生**（HIG `table`=表格 + `view`=视图），官方没有直接给这个组合词，但不译它会和已译的「集合视图」自相矛盾。
  - `Interface Builder` / `Storyboard` / `nib` / `XIB` **继续保留英文**（工具名与文件格式名，§4.1 规则 5）。
  - 所有对应**类名**继续保留英文：`UIViewController`、`UICollectionView`、`UITableView`、`UIScrollView`、`UIScene`。
- **理由**：① 有官方依据，规则 1；② 这几个词高频到无法回避，全篇英文会让译文读起来像没译。
- **⚠️ 这条是与旧仓库分歧的主要来源**：旧仓库 239 篇译文里这些词是英文。见文件顶部「修订说明」——**不要回改旧仓库**。
- **落点**：§1.4 陷阱 4；§3.4（view controller / collection view / table view / scroll view / scene 各行）；§3.5 组件表；§4.1 规则 5（已重写）；`TRANSLATION_STYLE.md` §六「保留英文，不译」（已同步改掉）。

### 5.11 `data race` — 数据竞争 vs 数据争用 → **改用「数据争用」**（官方自相矛盾，已选定并说明理由）

- **分歧点**：官方两说。
  - 「**数据争用**」：WWDC22-110351 中文**标题**《消除数据争用》（2022）。
  - 「**数据竞争**」：WWDC21-10133 中文**简介**「会发生数据竞争」（2021）。
- **最终选择**：**数据争用**。
- **选择理由**：
  1. **更晚**：2022 > 2021。
  2. **更正式**：出现在**场次标题**里，标题的本地化审校比简介更严格。
- **第 1 版倾向被推翻**：第 1 版选「数据竞争」，理由是社区通行且与 `race condition`→竞态条件成体系。裁决规则 1/2 明确官方优先，故推翻。
- **⚠️ 留下的体系裂缝（如实记录）**：`race condition` 官方无中文，仍按社区作「**竞态条件**」。于是同一页可能同时出现「数据争用」和「竞态条件」，看起来不成套。若日后觉得不能接受，只有两条路：把 `data race` 改回「数据竞争」（违反本次裁决），或把 `race condition` 自定为「争用条件」（自造译法，违反 §1.2）。**当前接受这道裂缝**，因为两个词在文档里很少同页出现。
- **落点**：§3.1 `data race` 行。

### 5.12 三组同形冲突 → 全部按官方定案

| 冲突 | 分歧点 | **最终选择** | 依据与理由 |
|---|---|---|---|
| `sheet`=表单（官方）↔ `form`=表单 | HIG 组件名 `sheets`=表单，但 `form` 天然也是「表单」 | `sheet`→**表单**（官方）；`form`→按语境作「**表格**」或「**填写表单**」；**两者首次出现都标注原文** | 官方给了 `sheet`，没给 `form`；有依据的一方占用「表单」，无依据的一方让位 |
| `picker`=选择器（官方）↔ `selector`=选择器（§2 旧表） | 两者都高频，同形 | 两者**都保持「选择器」**；`picker` 出现时**必须**写「选择器（picker）」，`selector` 指 Objective-C 选择器时首次写「选择器（selector）」 | `picker` 有官方依据不能改；`selector` 属 §2 不可改动条目。既然都不能改，就用强制标注原文来消歧 |
| `main actor` | 官方作「主要 Actor」（WWDC21-10133 中文简介），读起来像机器直译；社区作「主 Actor」 | `@MainActor`→**保留英文**（规则 1 标识符）；散文中的 main actor→**主要 Actor**（**改**，原为「主 Actor」） | 有官方依据，规则 1。**这是唯一一条跟随官方后与 `main thread`→主线程 构词不一致的条目**，理由见下 |

**关于 `main thread`→主线程 与 `main actor`→主要 Actor 为何不一致**（官方自相矛盾的第 4 例，需要说明）：

- 官方对 `main thread` 有两种译法：WWDC21-10133 中文**简介**作「在**主要线程**上运行」；WWDC20-10077 中文**字幕正文**作「我们正在**主线程**上重绘图像 主线程负责渲染用户界面的其余部分」（本次复核确认）。按规则 2「取更晚、更正式」——这里取**转写正文**而非一句简介，且「主线程」在官方材料里反复出现，故定为**主线程**。
- 官方对 `main actor` **只有一种**译法：「主要 Actor」，就出自那句同时写了「主要线程」的 WWDC21-10133 简介。没有竞争译法可选，按规则 1 只能采用**主要 Actor**。
- 结果就是：同一个 `main` 在「线程」上译成「主」、在「Actor」上译成「主要」。**这是 Apple 自己的不一致，本表如实跟随，没有替官方统一。** 如果你更希望统一成「主 Actor」，这是一次**明确的用户覆盖**（会偏离规则 1），改 §3.1 一行即可。实操影响很小——绝大多数场合出现的是 `@MainActor`，而它保留英文。
- **落点**：§3.1（main thread / main actor / `@MainActor` 三行）；§3.5 组件表 sheet、picker 两格。

### 5.13 `existential type` — 既存类型（官方）vs 存在类型（社区）→ **维持官方「既存类型」**

- **分歧点**：官方「既存类型」（WWDC22-110353 中文简介「如何使用既存类型」）vs 社区「存在类型」。
- **最终选择**：**既存类型**，首次标注「既存类型（existential type）」。
- **理由**：官方唯一译法，规则 1。第 1 版已按此写入 §3.2，本次裁决**确认不改**。
- **落点**：§3.2 `existential type` 行。

### 5.14 完全查不到中文依据的 → **全部保留英文**（含两条从「待定」定案）

按裁决规则 3/4：官方没给的不动、无共识的不自造。

| 术语 | 查证结果 | **最终选择** | 变化 |
|---|---|---|---|
| `chained fixups` | HIG 无、WWDC 中文标题/简介无、无社区共识 | 保留英文 | 维持 |
| `rebase` / `bind`（dyld 动作） | 同上 | 保留英文 | 维持。**与 git rebase 无关，不要译「变基」** |
| `continuation` | SE-0300 未译，官方中文简介直接写英文 | 保留英文 | 维持。首次可加一句解释 |
| `entitlement` | Apple 中文材料未见统一译法 | 保留英文 | 维持。社区有「授权文件」「权限」，都不准确 |
| `App Group` | 无官方中文 | 保留英文 | 维持 |
| `privacy manifest` | HIG privacy 页中文全文 grep「隐私清单」= 0 命中 | 保留英文 | **定案**（第 1 版倾向「隐私清单」但列为待定；现按规则 3/4 定为保留英文，不采纳该倾向） |
| `prewarming` | HIG 全 37 页中文正文 grep「预热」= 0 命中 | 保留英文 | **定案**（第 1 版倾向「预热」但列为待定；现定为保留英文，首次可加解释） |
| `Auto Layout` | HIG layout 页中文全文无对照 | 保留英文 | 维持，见 §5.15 |

- **落点**：§3.7、§3.8 对应行；§4.1 规则 4 的清单（已补全 `privacy manifest`、`prewarming`、`Auto Layout`）。

### 5.15 `Auto Layout` → **保留英文**

- **分歧点**：无官方中文；社区有「自动布局」但也常直接写英文。
- **语料**：现行 UIKit 语料 34 次，全部出现在散文中。
- **最终选择**：**保留英文 `Auto Layout`**。理由：这是 Apple 的技术名（首字母大写、有专属文档章节），不是普通短语；规则 4。
- **落点**：§3.4 `Auto Layout` 行。

### 5.16 `accessibility` — 无障碍 vs 辅助功能 ★ → **改用「辅助功能」**（官方并用两词，已选定并说明理由）

- **分歧点**：Apple 官方**两个词都在用**，本次复核逐个确认：

| 官方译法 | 出处 | 性质 |
|---|---|---|
| 「**辅助功能**」 | ① `apple.com.cn/accessibility` 主标题「**Apple 辅助功能**」，导航项「辅助功能」，正文「探索我们的辅助功能资源」<br>② iPhone 使用手册（中文）章节标题「**iPhone 上的辅助功能使用入门**」「在 iPhone 上快速打开或关闭**辅助功能**」<br>③ iOS 中文界面「**设置 › 辅助功能**」<br>④ developer.apple.com 中文站技术分类「辅助功能」 | **产品界面 + 用户文档 + 官网**，三线一致 |
| 「**无障碍**」 | HIG 中文 `accessibility` 页 **title 字段 = 「无障碍」**；正文「如果在设计时包括无障碍，你会收获更广泛的受众和更具包容性的体验」 | 仅设计指南一处 |
| 两词**混用** | 同一份 HIG 中文页里两词交替出现：「…了解你的 App 如何将自身呈现给使用系统**无障碍**功能的用户」与「支持肢体活动能力相关的**辅助技术**」并存 | 官方自己没统一 |

- **最终选择**：**辅助功能**（全库统一）。
- **选择理由**：
  1. **用户明确指定权威**：「iOS 系统设置里的叫法是权威」——iOS 中文界面就是「设置 › 辅助功能」。
  2. **覆盖面**：「辅助功能」出现在**产品界面、用户手册、apple.com.cn、开发者站导航**四处；「无障碍」只出现在 HIG 一处。
  3. **可搜索性**：读者在设备上看到的是「辅助功能」，译文用同一个词才能对应上。
- **落记的变体**：「无障碍」（HIG 中文 accessibility 页标题）。**引用 HIG 那一章的标题时照抄「无障碍」，不要改写成「辅助功能」**；除此之外正文一律「辅助功能」。
- **派生词**：`accessibility label`→辅助功能标签、`accessibility element`→辅助功能元素、`accessibility trait`→辅助功能特性、`assistive technology`→**辅助技术**（官方，HIG 原文）。
- **保留英文的**：`Accessibility` 框架名、`Accessibility Inspector` 工具名（HIG 中文正文本身就原样写英文：「使用 Accessibility Inspector 高亮标记…」）。
- **落点**：§1.4 陷阱 6；§3.6（accessibility / assistive technology / 框架名三行）。

---

## 六、语料事实备注（影响本表的适用范围）

- 新语料目前**只下载了 285 篇**，其中 264 篇是 UIKit；`meta/manifest/` 里有 35 个框架的清单，但 `swift`、`swiftdata`、`dispatch`、`foundation`、`coredata`、`metal`、`widgetkit`、`backgroundtasks`、`os` 等**尚无正文**。
- 因此 §3.1（Swift 并发）、§3.2（Swift 语言）、§3.7（启动/链接）的术语在**当前**语料里出现频次接近 0——它们是为后续抓取的框架**预置**的，不是从现有语料统计出来的。抓取扩容后应回头复核。
- 一个实测教训：现有 UIKit 语料里 `actor` 的 36 次命中**全部是 `factor` / `factory` 的假匹配**，`async` 的 68 次命中里没有一次出现在散文中。不要用词频反推「这个术语很重要」。
