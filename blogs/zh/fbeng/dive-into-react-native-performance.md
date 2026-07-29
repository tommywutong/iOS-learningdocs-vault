---
title: 深入探究 React Native 性能
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2016/03/28/android/dive-into-react-native-performance/'
original_language: en
published: 2016-03-28
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:02e86a03bb803c79'
translated: true
---

> 原文：[Dive into React Native performance](https://engineering.fb.com/2016/03/28/android/dive-into-react-native-performance/)　·　Meta Engineering — iOS

[React Native](https://facebook.github.io/react-native/) 允许你使用 [React](https://facebook.github.io/react/) 和 [Relay](https://facebook.github.io/relay/) 的声明式编程模型，用 JavaScript 构建 iOS 和 Android 应用。这使得代码更简洁、更易理解；无需编译周期即可快速迭代；并能轻松跨多个平台共享代码。你可以更快地发布，专注于真正重要的细节，让你的 App 看起来和用起来都棒极了。优化性能是其中至关重要的一环。以下是关于我们如何将 React Native App 启动速度提升一倍的故事。

## 为何如此紧迫？

对于运行更快的 App 来说，内容加载迅速，意味着人们能有更多时间与之交互，而流畅的动画则让 App 使用起来更愉悦。在新兴市场，[2011 级别的手机](https://engineering.fb.com/posts/952628711437136/classes-performance-and-network-segmentation-on-android/) 搭配 [2G 网络](https://newsroom.fb.com/news/2015/10/news-feed-fyi-building-for-all-connectivity/) 仍占主流，对性能的关注可以决定一个 App 是可用的还是不可用的。

自从在 [iOS](https://facebook.github.io/react/blog/2015/03/26/introducing-react-native.html) 和 [Android](https://engineering.fb.com/posts/1189117404435352/react-native-for-android-how-we-built-the-first-cross-platform-react-native-app/) 上发布 React Native 以来，我们一直在改进列表视图滚动性能、内存效率、UI 响应能力和 App 启动时间。启动阶段奠定了 App 的第一印象，并且对框架的各个部分都提出了挑战，因此它是最有价值也是最棘手的问题。

## 始终进行测量

我们将 [Facebook for iOS](https://itunes.apple.com/app/facebook/id284882215) App 中的活动仪表盘（Events Dashboard）功能转换为了 React Native（导航到 App 中的 **更多** 选项卡，然后点击 **活动** 即可查看）。这之所以是测试性能的理想选择，是因为原生产品已经高度优化，并提供了典型的“交互式项目列表”体验。

![](https://engineering.fb.com/wp-content/uploads/2016/03/GBZ5wQDCizZf8yYEAEM_gjcAAAAAbj0JAAAB.jpg)

<sub>图 1：活动仪表盘界面</sub>

接下来，我们设置了一个自动化的 [CT-Scan](https://engineering.fb.com/posts/924676474230092/mobile-performance-tooling-infrastructure-at-facebook/) 性能测试，该测试能帮助我们导航到最右边的选项卡，然后自动打开和关闭活动仪表盘 50 次。在这每次迭代过程中，我们都能测量从点击“活动”按钮到活动内容在屏幕上显示出来所花费的时间。我们还添加了更详细的性能标记，以便清楚地了解启动过程中的哪些步骤较慢并占用了 CPU 时间。

以下是我们测量的一些步骤的概述：

1. **原生初始化：** 初始化 JavaScript 虚拟机以及所有[原生模块](https://facebook.github.io/react-native/docs/native-modules-ios.html)（磁盘缓存、网络、UI 管理器等）。
2. **JS 初始化 + require：** 从磁盘读取压缩后的 JavaScript bundle 文件，并将其加载到 JavaScript 虚拟机中，虚拟机将在 require 初始模块（主要是 [React](https://facebook.github.io/react/)、[Relay](https://facebook.github.io/relay/) 及其依赖项）时解析文件并生成字节码。
3. **获取前：** 加载并执行活动仪表盘应用代码，构建 [Relay](https://facebook.github.io/relay/) 查询，并开始从磁盘缓存读取数据。
4. **获取：** 从磁盘缓存获取数据。
5. **JS 渲染：** 实例化所有 React 组件，并将其发送到原生 UI 管理器模块进行显示。
6. **原生渲染：** 在 shadow thread 上通过计算 [FlexBox](https://facebook.github.io/react-native/docs/flexbox.html) 布局来确定视图大小；在主线程上创建和定位视图。

![](https://engineering.fb.com/wp-content/uploads/2016/03/GEF5wQCX-cXZUeEAADQ_6S4AAAAAbj0JAAAB.jpg)

<sub>图 2：活动仪表盘启动性能</sub>

我们当时的黄金法则是：永远不要让测试结果出现衰退。我们持续运行它以跟踪性能改进和衰退，开发者可以在推送变更之前，针对特定的提交运行它，以获得详细的性能分析。我们还建立了其他测试，以同样的方式测量滚动性能和内存使用情况。

## 启动时发生了什么

有了自动化的性能跟踪，我们需要一个工具来提供更多细节，以便了解启动过程中具体需要改进哪些方面。我们在整个框架中添加了详细的开始/停止性能标记，收集数据，并使用 [catapult viewer](https://github.com/catapult-project/catapult/tree/master/tracing) 来识别热点和跨线程的阻塞交互。你可以从[开发者菜单](https://facebook.github.io/react-native/docs/debugging.html)触发对你 App 的性能分析。

在 React Native 中，你的代码在 JavaScript 线程上执行。无论何时你想将数据写入磁盘、发起网络请求或访问任何其他原生资源（例如相机），你的代码都需要调用原生模块。当你使用 React 渲染组件时，它们会被转发到 UI 管理器原生模块，然后该模块会在主线程上执行布局并创建最终的视图。[Bridge](http://tadeuzagallo.com/blog/react-native-bridge/) 会将你的调用转发到模块，并在需要时回调你的代码。在 React Native 中，所有原生调用都必须是异步的，以避免阻塞主线程或 JS 线程。

在下面的活动仪表盘启动可视化图中，我们可以看到，运行在 JS 队列上的 App 触发了对要显示的活动内容的缓存读取，这是在异步本地存储队列上触发的。一旦它获取回缓存数据，App 就在 JS 队列上使用 React 渲染活动单元格，然后将其传递给 shadow queue 进行布局，最后送到主队列进行视图创建。这个示例展示了多次缓存读取（可能使用一次通用读取操作会更快）以及 JS 线程上可能被合并的几次 React 渲染操作。

![](https://engineering.fb.com/wp-content/uploads/2016/03/GCefvQD26BsmvqsAAFRTmREAAAAAbj0JAAAB.jpg)

<sub>图 3：活动仪表盘启动可视化</sub>

## 性能改进

以下是我们为实现目标所做的一些最显著的高效性和调度性改进，并附上了相关提交的链接。

### 减少工作量

[清理 Require/Babel helpers](https://github.com/facebook/react-native/commit/b90fe8e2e8fd173498c268abf39a21b665e019ed)（高影响）：移除了在 `require()` 期间执行的、特定于我们网站且 React Native 并不需要的辅助代码。

[避免在加载 bundle 时复制和解码字符串](https://github.com/facebook/react-native/commit/f5670f8ab5cd045402ed037ade372c182902d19e)（中等影响）：将 UTF-8 字符串传递给 [JavaScriptCore](http://trac.webkit.org/wiki/JavaScriptCore) 虚拟机将导致其触发到 UCS-2 格式的较慢转换。改用 ASCII 格式编码则可以避免这种转换。去除[中间的 NSString 表示](https://github.com/facebook/react-native/commit/4a3857ef1dc073f4a58274b77e7f775ca81b39dd)也通过避免一次额外的转换来提高性能。我们通过对 bundle 加载步骤进行广泛的基准测试发现了这些改进。

[剥离仅用于 DEV 的模块](https://github.com/facebook/react-native/commit/7a794cc72bf5c2ea6da4dbda3a452bafc2997885)（低影响）：与编译型代码不同，JavaScript 没有可以在发布模式下剥离调试功能的预处理器。通过使用 [Babel](https://babeljs.io/) 转换，我们成功移除了存在于 ` __DEV__` 语句背后的代码，有效减小了 bundle 的大小，从而缩短了 JavaScript 解析时间。

**在服务端生成活动描述**（低影响）：不再获取数据来生成描述哪些朋友会参加某个活动的句子，而是在服务端生成它，从而减少了我们必须接收和解析的数据量，并避免了所有客户端处理来生成该句子。

### 调度

[延迟 require](https://github.com/facebook/react-native/commit/d088750163bd45cb60c4c6796ed97624fb6f91bf)（低影响）：不是预先执行所有 JavaScript 模块的 `require` 调用，而是在第一次需要时才触发 `require` 调用。这种优化有效地避免了 require 从未使用过的模块，[而且它已被证明在 Web 上是成功的](https://www.youtube.com/watch?v=SnAq9tbeRm4)。

[Relay 增量缓存读取](https://github.com/facebook/relay/commit/cc7c0e5b16999e045937a5f75a4ef0fe05b4695e)（高影响）：Relay 最初是为 Web 编写的，只有内存响应缓存。第一个磁盘响应缓存会从磁盘读取整个缓存。通过仅读取满足特定查询所需的内容，我们显著减少了 I/O 开销和原生到 JS 的 Bridge 流量。

[解批处理 Bridge 调用，批处理 Relay 调用](https://github.com/facebook/react-native/commit/31f9a690f3b3524adf08aa9d8c01843e8524453e)（高影响）：我们最初认为，将 JS 调用批量发送到原生端会减少通过原生到 JS Bridge 调用的开销，但性能分析显示，JS 对原生调用的开销并非瓶颈：实际上，延迟 UI 或缓存读取调用以等待与后续调用一起批处理，也延迟了原生线程上的工作，从而损害了性能。在其他情况下，例如 Relay 缓存读取为多个键获取数据时，[批处理](https://github.com/facebook/react-native/commit/a64ee7d8c5b717051f0659bf25ec38a8bd583d54)被证明是一项显著的改进。

[早期 UI 刷新](https://github.com/facebook/react-native/commit/c25c98c00c8c195f85c9fb17eae3cb0c36b465f5)（低影响）：我们还批处理 UI 更新以强制执行一致性，但事实证明，一旦布局命令准备就绪就立即发送它们效率更高，因为原生 UI 管理器可以与 JavaScript 线程并行工作。

[延迟加载原生模块](https://github.com/facebook/react-native/commit/060664fd3d9331f062696e68179bac9cd4544a06)（低影响）：仅在第一次使用某个原生模块时才对其进行初始化，从而避免初始化我们不需要的模块。

[延迟文本组件上的触摸绑定](https://github.com/facebook/react-native/commit/4ce03582a0013e60417dedbf2f760d00e687e540)（低影响）：绑定触摸事件回调会花费大量时间。我们不再预先完成所有工作，而是现在只绑定 Touch Down 事件（当你首次触摸目标时），并且仅在你开始触摸该元素时才绑定所有其他回调。

**推迟热门活动查询**（中等影响）：第一屏信息由活动查询填充，热门活动随后显示。推迟该查询减少了填充活动屏幕时的争用。

## 准备以光速前行

几个月前，在 iPhone 5 上，活动仪表盘的启动需要两秒钟。经过来自[伦敦](https://www.facebook.com/careers/locations/london/)、[门洛帕克](https://www.facebook.com/careers/locations/menlo-park/)和[纽约](https://www.facebook.com/careers/locations/newyork/)的 React Native 性能团队、React Native 团队、React 团队和 Relay 团队的大量努力，活动仪表盘的启动速度现在快了一倍。我们所做的大部分改进都是在框架层面完成的，这意味着你的 React Native App 在迁移到最新版本的 React Native 时将自动受益。

这些改进只是开始：我们将继续致力于让技术栈的每一部分都更快，从 JavaScript 解析时间到数据获取性能。并且[你可以贡献力量](https://github.com/facebook/react-native)，学习如何[让你的 App 更快](https://www.youtube.com/watch?v=0MlT74erp60)，并在我们的[社区](https://www.facebook.com/groups/react.native.community/)中提出任何可能的问题！
