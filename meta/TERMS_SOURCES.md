# TERMS.md 核实过程记录

记录建表时**实际访问过**的 URL、每个来源是否查到官方中文、以及查不到的项目。日期：2026-07-26。

§1–§6 是第 1 版建表记录；**§7 是第 2 版（「按 Apple 官方中文来」裁决）的追加核实记录**。

---

## 1. 关键发现：Apple 官方简体中文文档的真实入口

`developer.apple.com/cn/design/human-interface-guidelines/*` 是 Vue SPA，直接抓 HTML **只能拿到 `<title>`**，正文全靠 JS 加载。普通抓取会误判为「没有中文内容」。

正文藏在 DocC 数据接口里，路径规律（实测得出）：

```
英文 HIG 数据：https://developer.apple.com/tutorials/data/design/human-interface-guidelines/<slug>.json
中文 HIG 数据：https://developer.apple.com/tutorials/data/zh-cn/design/human-interface-guidelines/<slug>.json
```

探测过程（失败的路径一并记下，避免以后重复踩）：

| URL | 结果 |
|---|---|
| `/tutorials/data/documentation/design/human-interface-guidelines/materials.json` | 404 |
| `/tutorials/data/documentation/human-interface-guidelines/materials.json` | 404 |
| `/tutorials/data/index/design` | 404 |
| `/design/human-interface-guidelines/materials/data.json` | 404 |
| `/cn/tutorials/data/design/human-interface-guidelines/materials.json` | 404 |
| `/tutorials/data/design/human-interface-guidelines/materials.json?locale=zh_CN` | 200，但内容仍是英文（locale 参数无效） |
| 加 `Accept-Language: zh-CN` 请求头 | 200，内容仍是英文（请求头无效） |
| **`/tutorials/data/zh-cn/design/human-interface-guidelines/materials.json`** | **200，简体中文 ✅** |

## 2. 已验证：Apple 没有中文版 API 参考文档

| URL | 结果 |
|---|---|
| `https://developer.apple.com/tutorials/data/zh-cn/documentation/swift/concurrency.json` | 200，但正文与章节标题全是英文（`"title":"Essentials"` 等） |
| `https://developer.apple.com/tutorials/data/zh-cn/documentation/uikit.json` | 200，同样全英文 |

**结论**：`zh-cn` 路径对 `documentation/*`（框架 API 参考）存在但不翻译，静默回落英文。所以 Swift 并发、Swift 语言特性、dyld/Mach-O、渲染内部机制这些领域**没有 Apple 官方中文 API 文档可依据**，只能靠 HIG + WWDC 中文标题/简介 + 社区。

---

## 3. 查到官方中文的来源（按贡献排序）

### 3.1 官方中文《人机界面指南》— 主力来源

- 索引：`https://developer.apple.com/tutorials/data/zh-cn/design/human-interface-guidelines.json`
- 分区索引（5 个，各返回中文标题清单）：
  `.../zh-cn/design/human-interface-guidelines/{foundations,patterns,components,inputs,technologies}.json`
- 组件子分区（7 个）：
  `.../zh-cn/design/human-interface-guidelines/components/{presentation,status,layout-and-organization,menus-and-actions,selection-and-input,content,system-experiences}.json`
  → 一次性拿到 **127 个官方中文组件/技术名**（TERMS.md §3.5、§3.6 全部来自这里）
- 正文页（37 个，全部 200 + 简体中文）：
  `.../zh-cn/design/human-interface-guidelines/{layout, materials, color, typography, accessibility, privacy, gestures, focus-and-selection, keyboards, pointing-devices, motion, dark-mode, drag-and-drop, modality, presentation, launching, multitasking, navigation-and-search, feedback, loading, status, system-experiences, images, entering-data, searching, settings, undo-and-redo, file-management, managing-notifications, live-viewing-apps, app-clips, spatial-layout, immersive-experiences, components, inputs, technologies, patterns}.json`

**这里查到的关键定译（附原文片段）**：

| 术语 | 官方中文 | 出处页 | 原文片段 |
|---|---|---|---|
| Liquid Glass | **不译，保留英文** | materials | 「Apple 平台有两种类型的材质：Liquid Glass 和标准材质」——通篇不出现「液态玻璃」 |
| material | 材质 | materials | 页标题「材质」 |
| vibrancy | 虚化 | materials | 「无论选取哪种材质，均在材质之上使用虚化颜色」 |
| blending mode | 融合模式 | materials | 「macOS 定义了两种融合背景内容的模式」 |
| scroll edge effect | 滚动边缘效果 | materials | 「滚动边缘效果通过模糊并减少背景内容的不透明度…」 |
| safe area | **安全区** | layout | 「安全区 定义了视图内不会被工具栏、标签页栏或者窗口可能提供的其他视图遮挡的区」 |
| layout guide | 布局指南 | layout | 「布局指南 定义了一个矩形区域」 |
| margin | 外边距 | layout | 「系统定义的安全区、外边距和指南」 |
| Dynamic Island | 灵动岛 | layout | 「如 iPhone 上的灵动岛或部分 Mac 机型上的相机防护罩」 |
| Dynamic Type | 动态字体 | layout / typography | 「如果支持 动态字体 这项功能」 |
| adaptivity | 适配性 | layout | 「帮助确保界面的高适配性」 |
| size class | 尺寸类别 | drag-and-drop | 「创建可响应所有尺寸类别和方向的自适应布局」 |
| scene / container view controller | 场景 / 容器视图控制器 | multitasking | 「探究如何使用场景和容器视图控制器让你的 UIKit App…」 |
| view hierarchy | 视图层级结构 | gestures / modality | 「在支持于视图层级结构之间导航的 App 中」 |
| Keychain | 钥匙串 | privacy / entering-data | 「将敏感信息储存在钥匙串中」 |
| App Sandbox | App 沙盒化 | privacy | 「通过 App 沙盒化保护用户的数据。沙盒化可让你的 App…」 |
| Face ID / Optic ID / Touch ID | 面容 ID / 视控 ID / 触控 ID | privacy | 「例如面容 ID、视控 ID 或触控 ID」 |
| document | **文稿** | file-management | 「文稿启动器」「打开文稿」「显示文稿的预览」 |
| Quick Look / Finder / Spotlight | 快速查看 / 访达 / 聚焦 | file-management | 「其他 App（包括访达、『文件』和『聚焦』）」 |
| focus / hover effect | 焦点、聚焦效果 / 悬停效果 | focus-and-selection | 「系统使用 悬停效果 而不是聚焦效果来提供视觉反馈」 |
| parallax effect | 视差效果 | focus-and-selection / images | 「Apple tvOS 通常使用 视差效果…」 |
| transition | 过渡效果 | motion | 「帮助其追踪过渡效果」「自定过渡效果」 |
| haptics | 触感反馈 | feedback | 「提供触感反馈可调动用户的触觉」 |
| Smart Stack | 智能叠放 | gestures | 「系统在智能叠放中显示的实时活动」 |
| modifier | 修饰符 | layout | 「指定布局修饰符来微调界面中视图的放置」 |
| control | **控制** | components/controls | 组件页标题即「控制」；「分段控制」「页面控制」「显示控制」 |
| navigation | **导览** | navigation-and-search | 分区标题「导览和搜索」；materials「控制和导览」 |

### 3.2 WWDC 中文场次标题与简介 — 并发/性能/链接类术语的唯一官方来源

Apple 把 WWDC 场次的**标题和简介**本地化成简体中文（正文转写文稿多数仍是英文，少数早期场次有中文字幕）。逐页访问：

| URL | 中文化程度 | 贡献的术语 |
|---|---|---|
| `/cn/videos/play/wwdc2020/10077/` | 标题+简介+**中文字幕全文** ✅ | **hitch=「障碍」**（字幕原文：「我们将这些用户可感知的抖动称为『障碍』」）、障碍时间、障碍比率、帧、掉帧、VSYNC（保留） |
| `/cn/videos/play/wwdc2021/10132/` | 标题+简介中文，转写文稿英文 | async/await（保留英文）、异步、完成处理程序 |
| `/cn/videos/play/wwdc2022/110351/` | 标题+简介中文 | Swift 并发、**数据争用**、Sendable（保留）、原子性、任务 |
| `/cn/videos/play/wwdc2021/10133/` | 标题+简介中文 | **Actor（保留英文）**、Actor 隔离、**数据竞争**、可变状态、协议一致性、主要 Actor |
| `/cn/videos/play/wwdc2021/10134/` | 标题+简介中文 | 结构化并发、任务组、非结构化任务、取消任务 |
| `/cn/videos/play/wwdc2021/10181/` | 标题+简介中文 | 应用性能；相关视频列表贡献「探索 UI 动画阻碍与渲染循环」→ **hitch=「阻碍」、render loop=渲染循环** |
| `/cn/videos/play/wwdc2021/10258/` | 标题+简介中文 | **hang=挂起**、反面模式、性能衰退 |
| `/cn/videos/play/wwdc2023/10248/` | 标题+简介中文 | 挂起（Instruments 分析挂起）；相关视频「利用 Xcode 和设备端检测对卡顿进行跟踪」→ hang 也被译作「卡顿」 |
| `/cn/videos/play/wwdc2022/110362/` | 标题+简介中文 | **链接、启动时间、构建时间**、运行时链接性能；相关视频「认识可合并库」→ mergeable library |
| `/cn/videos/play/wwdc2019/423/` | 标题+简介中文 | **launch=启动**（「优化 App 启动」） |
| `/cn/videos/play/wwdc2022/110353/` | 标题+简介中文 | **既存类型**、不透明结果类型、具体类型、相同类型要求、泛型、参数包 |
| `/cn/videos/play/wwdc2023/10149/` | 标题+简介中文 | **观察**（Observation）、Observable 宏（保留）、宏 |
| `/cn/videos/play/wwdc2023/10166/` | 标题+简介中文 | **宏**（macro）、Swift 宏 |
| `/cn/videos/play/wwdc2018/416/` | 标题+简介中文 | **内存占用空间**（memory footprint） |

各页的「相关视频」区块额外贡献了约 60 个官方中文场次标题，包括：「探索 SwiftUI 中的并发」「认识 AsyncSequence」「Swift 的分布式 Actor 简介」「SwiftUI 中的叠放、网格和大纲」（→ **stack=叠放**）「SwiftUI 中的『后台任务』」（→ **background task=后台任务**）「解密 SwiftUI 性能」「Grand Central Dispatch 的现代化用法」（→ GCD 保留英文）。

### 3.3 `developer.apple.com/cn/swift/`

访问：`https://developer.apple.com/cn/swift/` — 200，简体中文，但只是语言概览页。

查到：**值类型、可选值、可选类型、可选类型绑定、可选链、nil 合并、协议、泛型、闭包、扩展**（原文「使用 extension 向现有类型添加功能」——`extension` 关键字保留英文）。

**没有**：concurrency、async/await、actor、Sendable、property wrapper、result builder、macro、opaque type、memory safety。

---

## 4. 查不到官方中文的（如实记录）

| 术语 | 查过哪里 | 结果 |
|---|---|---|
| `Liquid Glass` 的中文名 | HIG materials 页中文全文 + 中文媒体搜索 | **官方就是不译**。中文媒体（36氪、界面新闻、知乎）用「液态玻璃」，但那不是 Apple 用词。TERMS.md 明确禁用「液态玻璃」 |
| `hitch` | WWDC20-10077 中文字幕、Tech Talk 中文标题 | 查到了，但**官方自相矛盾**：「障碍」与「阻碍」并存 → 第 2 版追加核实发现还有第三说「卡顿」（且是 Tech Talk 转写正文的通用词），已裁决取「卡顿」，见 §7.2 与 TERMS.md §5.7 |
| `property wrapper` | `/cn/swift/`、WWDC23-10149 章节标题 | 未译（章节标题保留英文 "SwiftUI property wrappers"）→ 用社区「属性包装器」 |
| `result builder` | 同上 | 无官方中文 → 社区「结果构建器」 |
| `chained fixups` | HIG、WWDC22-110362 中文简介 | 无 → 保留英文 |
| `rebase` / `bind`（dyld） | 同上 | 无 → 保留英文 |
| `dyld` / `Mach-O` | HIG、WWDC 中文标题 | 无 → 保留英文（Apple 中文材料也直接写英文） |
| `prewarming` | HIG 全 37 页中文正文（grep「预热」= 0 命中） | 无 → 待定，当前保留英文 |
| `entitlement` | HIG、WWDC 中文简介 | 无 → 保留英文 |
| `privacy manifest` | HIG privacy 页中文全文（grep「隐私清单」= 0 命中） | 无 → 待定 |
| `App Group` | HIG | 无 → 保留英文 |
| `continuation` | WWDC21-10132 资源区（SE-0300 标题未译） | 无 → 保留英文 |
| `Auto Layout` | HIG layout 页中文全文 | 无中文对照 → 保留英文 |
| `hit-testing` / `offscreen rendering` / `compositing` | HIG、WWDC 中文标题 | 无 → 社区译法 |
| Swift 官方中文文档（swift.org） | **未查证** | 联网预算已用尽。若要补，建议查 swift.org 是否有 zh-CN 本地化，以及 SwiftGG 译本（社区，非官方） |
| Xcode 简体中文界面用词 | **未查证** | Xcode 本身不提供简体中文界面，无从取词 |

---

## 5. 本地语料统计（无联网）

### 5.1 旧仓库 `翻译/vault/` — 只读，未执行任何写操作或 git 命令

- 已译页面规模：`documentation/` 下 9227 个 `.md`，其中**含 ≥5 行中文的约 239 篇**（全部在 `Cocoa/` 和 `Windows Views/` 下）。注意：用「含任意中文字符」筛会得到全部 9227 篇——未译页面的导航面包屑里也有中文，这个指标不可用。
- 对 TRANSLATION_STYLE.md 第 70-107 行的 34 条术语逐条统计了规范译法与竞争译法的出现次数，结果已写入 TERMS.md §2 的「旧仓库次数」和「核验结果」两列。
- 发现 5 处规范与实际不一致（accessor / retain / attribute / block / 5 条低频条目），已列入 TERMS.md §5.1–§5.5，**未自行改判任何译法**。
- macOS `uniq` 在 UTF-8 排序下会把不同中文串折叠，统计时需 `LC_ALL=C`——记录备查。

### 5.2 新语料 `apple-docs/en/`

- 实际只有 **285 篇** `.md`（264 篇 UIKit），`meta/manifest/` 列了 35 个框架但 22 个尚无正文（swift、swiftdata、dispatch、foundation、coredata、metal、widgetkit、backgroundtasks、os 等全空）。
- 因此 Swift 并发、Swift 语言特性、启动/链接三个领域在现有语料里频次接近 0，TERMS.md 对应章节是**为后续抓取预置**的。
- 词频反推的一个反例：`actor` 在 UIKit 语料里 36 次命中**全是 `factor`/`factory` 假匹配**；`async` 68 次命中**无一出现在散文中**（都在标识符或代码块里）。
- 现有语料里真正高频且需要统一中文的散文术语：view controller 958、gesture recognizer 355、collection view 281、table view 258、scene 389（词界）、drag and drop 121、safe area 20、responder chain 21、trait collection 18、diffable data source 43、state restoration 38、auto layout 34。这直接支撑了 TERMS.md §5.10 把「View Controller 保留英文」列为最高优先级裁决项。

---

## 6. 联网请求统计

约 95 次 HTTP 请求（超出 80 次的软上限约 15 次）。超支主要来自两处：探测中文 DocC 接口路径时的 7 次试错，以及批量拉取 37 个 HIG 中文正文页。后者是本表官方依据的主体，不拉就只能靠猜。

---

## 7. 追加核实（2026-07-26 第 2 版裁决）

用户裁决「术语表按 Apple 官方中文来」后，只对**裁决规则第 1、2 条里仍不确定的两项**（`accessibility`、`hitch`）做了补充核实。共 14 次请求（预算 25 次）。

### 7.1 `accessibility` — 官方两词并用，确认以哪个为准

| URL | 结果 |
|---|---|
| `https://www.apple.com/cn/accessibility/` | 301 → `https://www.apple.com.cn/accessibility/` |
| `https://www.apple.com.cn/accessibility/` | 200。主标题「**Apple 辅助功能**」，导航项「辅助功能」，正文「探索我们的辅助功能资源」 |
| `https://developer.apple.com/cn/accessibility/` | 200，但页面正文由 JS 加载，只拿到 `<title>`（英文）。**无有效证据** |
| `https://support.apple.com/zh-cn/guide/iphone/iph3e2e4367/ios` | 200。页面标题「**iPhone 上的辅助功能使用入门** - 官方 Apple 支持 (中国)」。正文为目录结构，未拿到「设置 › 辅助功能」原句 |
| `https://support.apple.com/zh-cn/guide/iphone/iph3e2e31a5/ios` | 200。页面标题「**在 iPhone 上快速打开或关闭辅助功能**」。同样只拿到目录 |
| `https://support.apple.com/zh-cn/guide/iphone/iph3e2e415f/ios` | 200。页面标题「在 iPhone 上打开和练习『旁白』」。确认 VoiceOver=旁白 |
| WebSearch `site:support.apple.com zh-cn "前往「设置」" "辅助功能"` | 返回的全是英文页，未拿到中文设置路径原句 |
| **`/tutorials/data/zh-cn/design/human-interface-guidelines/accessibility.json`**（复查） | 200。**`title` 字段 = 「无障碍」**；但正文里「无障碍」与「辅助功能」「辅助技术」**交替出现**：「支持肢体活动能力相关的**辅助技术**」「使用 Accessibility Inspector 高亮标记界面相关的无障碍问题」 |

**结论**：Apple 官方**两个词都在用**。「辅助功能」覆盖 apple.com.cn + iPhone 中文使用手册 + iOS 界面 + 开发者站导航；「无障碍」只出现在 HIG 一处（且该页自己也混用）。按用户指定的权威（iOS 系统界面用词）→ **TERMS.md 定为「辅助功能」**，「无障碍」作为变体记入 §5.16。附带确认：`Accessibility Inspector` 官方中文正文原样保留英文。

> 未能直接抓到「设置 › 辅助功能」那一行原文（Apple 支持页正文也是 JS 加载）。但三个中文支持页的**标题**都用「辅助功能」，与 apple.com.cn 一致，证据链已足够。若日后要补铁证，去抓 `support.apple.com/zh-cn` 的 DocC/JSON 接口而不是 HTML。

### 7.2 `hitch` — 官方三说，确认取哪个

| URL | 结果 |
|---|---|
| WebSearch `Apple Tech Talks 中文 "探索 UI 动画阻碍与渲染循环"` | 定位到 **Tech Talk 10855** |
| WebSearch `"Explore UI animation hitches and the render loop" Tech Talks 2020 published date` | 未拿到确切发布日；旁证指向 **2020 年 12 月**（同系列 UI 性能 Tech Talk 的第三方文章均为 2020-12） |
| **`https://developer.apple.com/cn/videos/play/tech-talks/10855/`**（两次，问不同问题） | 200。中文标题「探索 UI 动画**阻碍**与渲染循环」；中文简介「找出在你 App 里卷动轴与动画的**阻碍**」；但**中文转写文稿全文用「卡顿」**：「什么是**卡顿**？」「任何时候屏幕上出现 晚于预计的帧都属于**卡顿**」「**卡顿**的出现是由于渲染循环 没有按时完成一帧」「**提交卡顿**发生在 app 的处理中」「**渲染卡顿** 发生在渲染服务器中」。<br>**顺带查到的两条高价值证据**：「我们来观察一下滚动**集合视图**的常见例子」「当用户在屏幕上滑动手指时 **滚动视图**会随着上移内容作出响应」→ 官方在散文正文里译 collection view / scroll view，直接支撑 §5.10 |
| **`https://developer.apple.com/cn/videos/play/wwdc2020/10077/`**（两次，问不同问题） | 200。中文标题「使用 XCTest 消除动画**障碍**」；中文字幕「我们将这些用户可感知的抖动称为『**障碍**』」「当帧错过预期的 VSYNC 时 就会出现**障碍**」；**但同页中文简介写「如果动画效果出现卡顿，则可能破坏用户体验」**。<br>**顺带查到**：中文字幕用「**主线程**」（「我们正在主线程上重绘图像 主线程负责渲染用户界面的其余部分」），**未出现「主要线程」**→ 支撑 §5.12 把 `main thread` 定为「主线程」。该字幕里未出现「视图控制器」「集合视图」「表格视图」「控件」 |
| `/tutorials/data/zh-cn/design/human-interface-guidelines/navigation-bars.json` | 200，但返回的是「**工具栏**」页（Apple 已把 navigation bars 并入 toolbars）。**意外查到关键一句**：「包含**导览控制**的工具栏出现在窗口顶部」「专用于在 App 的各区域间**导览**」「在 iOS 中，**导览特定的工具栏有时会称为导航栏**」→ 确认 `navigation`→导览、`control`→控制，且 `navigation bar`→**导航栏** 是官方例外 |

**结论**：官方三说 —— 卡顿 / 障碍（WWDC20 字幕）/ 阻碍（Tech Talk 标题）。取「**卡顿**」：更晚（2020-12 > 2020-06）、更系统（唯一长出「提交卡顿」「渲染卡顿」派生词族的一支）、跨来源（WWDC20 自己的简介也用它）。详见 TERMS.md §5.7。

### 7.3 本次未再核实、沿用第 1 版记录的

`control` / `navigation` / `stack` / `existential type` / `data race` / `main actor` / `view controller` / `scene` 的官方依据在第 1 版已实测（见本文件 §3.1、§3.2），本次只补了上表那几条交叉证据，未重复拉取。§4 里「查不到官方中文」的 8 条也未重查——第 1 版已 grep 过 HIG 全 37 页中文正文，结论按裁决规则第 3 条直接定案为保留英文。
