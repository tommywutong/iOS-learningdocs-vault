---
title: 'Emerge Tools 博客 | 这 5 个 iOS App 如何能缩短启动时间'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/improve-popular-iOS-app-startup-times'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:50dd653b58a0e1f5'
translated: true
---

> 原文：[Emerge Tools Blog | How these 5 iOS apps could improve their startup time](https://www.emergetools.com/blog/posts/improve-popular-iOS-app-startup-times)　·　Emerge Tools Blog

# 5 个 iOS App 如何能平均缩短 28% 的启动时间

2022 年 9 月 14 日　作者：Michael Eisel

iOS 性能 启动时间

![improve-popular-iOS-app-startup-times](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog9.54f9d326.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

## [毫秒至关重要](https://www.emergetools.com/blog/posts/improve-popular-iOS-app-startup-times#milliseconds-matter)

启动时间是 App 的一项关键指标，需要持续监控和优化。顶级移动 App 公司的 A/B 测试一再表明，哪怕只增加零点几秒，都会显著损害核心使用指标，比如日活跃用户数和每位用户每天在 App 上的停留时间。

Lyft 报告称，其司机 App 的启动时间[减少了 21%](https://www.youtube.com/watch?v=nmeuLSM__10&t=8s)，用户会话次数增加了 5%。Apple 也曾多次在 WWDC 演讲中将启动时间作为主题^[[1]](https://developer.apple.com/videos/play/wwdc2019/423/)[[2]](https://developer.apple.com/videos/play/wwdc2022/110362/)[[3]](https://developer.apple.com/videos/play/wwdc2022/110363/)。

这篇博文不会空泛地讲如何避免常见的反面模式（anti-pattern）来缩短启动时间，而是使用 Emerge 的 [Performance Analysis](https://www.emergetools.com/product/performanceanalysis) 产品诊断具体的 App 启动问题并寻找改进方案。本文主要关注 iOS App，但 Emerge 的工具在 Android 和 iOS 上功能完全一致。

**这些都是真实可行的优化，适用于公开发布的 App Store 构建，且无需开发者参与。**

## [我们如何测量启动](https://www.emergetools.com/blog/posts/improve-popular-iOS-app-startup-times#how-we-measured-startup)

由于这里分析的 App 均来自 App Store，没有任何调试信息或源代码，我们决定简单地将「启动时间」定义为从 App 启动的最早时间点到 `applicationDidBecomeActive(_:)` 结束为止。

对于使用 Emerge 的移动 App 团队，启动时间的定义[完全可由开发者自定义](https://docs.emergetools.com/docs/ios-performance-testing)。一个常见的用例是定义 `applicationDidBecomeActive(_:)` 之后的终点，来测量用户能够真正与 App 交互所需的时间。这意味着，与公司内部开发者所认定的启动时间相比，下面显示的启动时间测量值很可能是保守估计。

由于缺少任何调试符号（debug symbols），我们无法完全去混淆（de-obfuscate）许多函数名。如果 App 集成了[Emerge CI](https://www.emergetools.com/app/example/ios/wikipedia?buildContent=comparison)并包含调试符号，将能生成[更详细的火焰图（flamegraph）](https://www.emergetools.com/app/example/ios/wikipedia?buildContent=comparison)。

Emerge 使用最先进的实体设备集群，以确保性能测量尽可能准确。以下主线程（main thread）测量均在运行 iOS 15.4.1 的 iPhone SE（2020）上进行。

需要特别注意的是，对 App 启动时间进行**单次**测量就只是单次测量，不应将其外推为更大样本的代表。控制方差就像驯服一头野兽：从 App 是否已登录、是否刚启动过，到设备类型、甚至设备温度，一切因素都会对结果产生巨大影响。

现在来看看 5 个热门 App 如何能缩短其启动时间……

![United Airlines app icon](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Funited.webp&w=128&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

美联航

查看交互式启动时间火焰图

总启动时间：2.05 秒

可节省：40%（0.83 秒）

[![United App 性能洞察](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Funited-flamegraph.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)](https://www.emergetools.com/app/example/ios/united-performance-test?buildContent=flamegraph)

特色自动化洞察

美联航 App 此前因[体积问题](https://telkins.dev/posts/how-i-shaved-187mb-off-uniteds-airlines-439mb-ios-app/#:~:text=Let's%20inspect%20the%20biggest%20framework%2C%20UALAppCore%20.&text=OK%2C%20so%20the%20vast%20majority,very%20large%20for%20a%20framework)已被广泛讨论，但其启动时间同样有很大改进空间。以下三个问题立即浮出水面：

- **自动化洞察：** 美联航在 `JSONDecoder.decode()` 上花费了 48 毫秒，这些工作应在后台进行，或者使用更快的第三方 JSON 库（如我自己的 [ZippyJSON](https://github.com/michaeleisel/ZippyJSON)）来加速。
- 美联航在 `-[NSPersistentContainer loadPersistentStoresWithCompletionHandler:]` 上花费了 677 毫秒。此类 Core Data 工作应放在主线程之外进行。如此巨大的延迟很可能表明还存在其他反面模式。
- 美联航在 LPMessagingSDK 上花费了 103 毫秒，该 SDK 调用了 `Bundle.init(identifier:)`。这个方法接收一个 identifier，返回与之匹配的 bundle（`CFBundleIdentifier` 在 Info.plist 中）。虽然这个方法看似无害，但它必须从磁盘加载所有 bundle，直到找到匹配的 bundle ID 为止。这既包括用户提供的 bundle（如 framework），也包括 Apple 众多的 bundle。当 bundle 首次加载时，它们会在一定程度上被缓存。立即重新运行 App，启动时间会减少 20 毫秒；但对于冷启动，这笔加载开销是必须支付的。App 应延迟 LPMessagingSDK 的初始化，直到实际需要该功能时再执行（通常只有当用户进入支持页面时才会需要）。

![Chipotle app icon](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Fchipotle.webp&w=128&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Chipotle

查看交互式启动时间火焰图

总启动时间：0.57 秒

可节省：33%（0.19 秒）

[![Chipotle App 性能洞察](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Fchipotle-flamegraph.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)](https://www.emergetools.com/app/example/ios/chipotle-performance-test?buildContent=flamegraph)

特色自动化洞察

- **自动化洞察：** 美联航 App 并非唯一一个受 LPMessagingSDK 问题困扰的。Chipotle 的 App 在启动过程中有 187 毫秒花在了 LPMessagingSDK 的 `Bundle.init(identifier:)` 上，如上所述，这可以移出启动路径。

![Curb app icon](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Fcurb.webp&w=128&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Curb

查看交互式启动时间火焰图

总启动时间：0.8 秒

可节省：22%（0.18 秒）

[![Curb App 性能洞察](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Fcurb-flamegraph.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)](https://www.emergetools.com/app/example/ios/curb-performance-test?buildContent=flamegraph)

特色自动化洞察

Curb 是我们这里分析的唯一使用 Salesforce Service Cloud SDK 的 App。该 SDK 为客户关系管理工具（如支持聊天）提供 API 和 UI。与 LPMessagingSDK 一样，Salesforce Service Cloud SDK 也会在加载 bundle 时产生巨大开销。具体来说，它在 `Bundle.allFrameworks` 上花费了 83 毫秒，紧接着又在 `NSArray.filtered(using:)` 上花费了 93 毫秒。这些方法调用发生在启动的最初期（至少是我们能记录的部分），表明它们是 initializer（初始化器）。Initializer 是特殊的函数，会在启动早期隐式运行，例如在 `NSObject.load()` 方法中。

[![Emerge 高级火焰图控制](https://www.emergetools.com/images/blogs/blog9/perf-gif.gif)](https://www.emergetools.com/app/example/ios/curb-performance-test?buildContent=flamegraph)

Emerge 高级火焰图控制

如果在 UI 中切换["Collapse system calls"（折叠系统调用）](https://docs.emergetools.com/docs/performance-visualizations#remove-system-libraries)开关，可以看到它们确实是 initializer，并非由 App 代码运行，而是由 `dyld4::Loader::findAndRunAllInitializers` 运行。使用 Hopper 反编译该库后，我们发现后续的函数正在调用 `Bundle.allFrameworks`，并执行了以下操作：

```shell
var frameworksList: [Bundle]?
...
func initializeFrameworkBundles() {
...
let allFrameworks = NSBundle.allFrameworks
let predicate = Predicate(format:"bundleIdentifier BEGINSWITH %@", "com.salesforce")
frameworksList = allFrameworks.filteredArray(predicate:predicate)
...
}
```

`NSBundle.allFrameworks` 开销很大，因为它会对每个 framework 进行一些初始设置和/或从缓存中获取数据。这既包括用户提供的 framework，也包括许多 Apple framework。`NSArray.filteredArrayUsingPredicate(using:)` 调用开销大的原因类似：它会为每个 framework bundle 调用 `NSBundle.bundleIdentifier`。这意味着，除了 `NSBundle.allFrameworks` 中完成的初始设置外，它现在还必须读取每个 framework 的 Info.plist 并获取 `CFBundleIdentifier` 值。虽然由于缓存被填充，后续运行可能会更快，但仍需花费不可忽略的时间，而冷启动（cold start）仍然是一个重要场景。

Salesforce 可以通过将搜索范围缩小到 `*bundle path*/Frameworks` 中用户提供的 framework 来避免这种情况，或者更好的方法是直接按名称搜索已知可能由 Salesforce 提供的 framework。对于使用 Salesforce 的 App 开发者来说，绕过这个问题则更加困难。与 LPMessagingSDK 不同（开发者可以控制初始化时机，并将其完全移出启动路径），对于由系统自动运行的 initializer 函数，开发者没有这个选项。

致 SDK 开发者：**请**不要使用 initializer 函数。它们的影响更难衡量，也更难阻止或延迟运行。它们不仅会损害性能，还会影响稳定性，我想我们都还记得 [Facebook SDK 的灾难](https://www.theverge.com/2020/5/7/21250689/facebook-sdk-bug-ios-app-crash-apple-spotify-venmo-tiktok-tinder)。

基于此，以下是一些缓解方法：

- 对于大胆的开发者，可以尝试不链接 Service Cloud framework，而是将其作为 App bundle 的一部分包含进来，并在调用 API 之前使用 `Bundle.load()` 来加载它们（因为 SDK 通常只在非常具体、不常用的屏幕上才需要，比如客户支持）。
- 直接使用 Service Cloud REST API，而不是通过它们的库。
- 完全换用其他服务。

除了上述问题外，Salesforce Service Cloud SDK 在非 initializer 设置中花费了 67 毫秒来运行 `class_conformsToProtocol` 和 `objc_copyClassList`（可能是遍历所有类以确定哪些类符合某个协议（protocol））。所有这些设置很可能都可以移出启动过程。

至于其他 SDK，我们看到 NewRelic 由于方法调配（method swizzling）占用了 4% 的启动时间，LeanPlum 占用了 3%，而 Realm 由于 `objc_copyClassList` 占用了 1%（可能只有 1%，因为 Service Cloud SDK 先调用了该函数，预热了缓存）。虽然 Realm 可能与启动路径关系密切，但其他两个 SDK 似乎至少可以稍微延迟，以便在阻塞主线程之前先显示启动屏幕。

![Walmart app icon](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Fwalmart.webp&w=128&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

沃尔玛

查看交互式启动时间火焰图

总启动时间：0.67 秒

可节省：33%（0.22 秒）

[![沃尔玛 App 性能洞察](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Fwalmart-flamegraph.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)](https://www.emergetools.com/app/example/ios/walmart-performance-test?buildContent=flamegraph)

特色自动化洞察

- **自动化洞察：** 沃尔玛在 `print` 语句上花费了 20 毫秒，这些语句不应出现在正式的 App Store App 中。
- 沃尔玛在启动过程中还花费了 197 毫秒在 `String.init(describing:)` 上。通常，这表明 App 试图将该字符串用作唯一 ID（此时应使用 `ObjectIdentifier`），或者可能是将其作为日志记录的一部分调用，而这部分可以直接移除。

![Zoom app icon](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Fzoom.webp&w=128&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Zoom

查看交互式启动时间火焰图

总启动时间：0.27 秒

可节省：15%（0.04 秒）

[![Zoom App 性能洞察](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog9%2Fzoom-flamegraph.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)](https://www.emergetools.com/app/example/ios/zoom-performance-test?buildContent=flamegraph)

特色自动化洞察

- 最后，是我个人最喜欢的一个。Zoom 的 App 在启动过程中实际上在主线程上**休眠**了 41 毫秒。

---

## [结论](https://www.emergetools.com/blog/posts/improve-popular-iOS-app-startup-times#conclusion)

即使在最大规模的应用中，管理移动 App 性能也极具挑战性。启动时间是最常见、最容易获取的性能指标之一，但在开发过程中实现准确测量是一个主要障碍。

使用 Emerge 的 Performance Analysis 产品，我们能够分析并针对直接从 App Store 下载的五个热门 iOS App 提出启动时间改进建议。这篇博文中提出的许多洞察都来自 Emerge 的 Performance Analysis 产品的自动化洞察功能，它会自动识别并建议性能改进方案。

一旦集成到 CI（持续集成）中，开发者就可以进行更改，并立即在拉取请求（pull request）上看到该功能是降低还是提升了 App 性能。

祝所有致力于改善启动时间和 App 性能的朋友们好运，如有任何疑问，请随时告知我们！
