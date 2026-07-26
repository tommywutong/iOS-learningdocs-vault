---
title: 2018-10-ReadingList
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/2018-10-ReadingList/'
original_language: zh
published: 2018-11-01
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:04668ab488be3231'
translated: n/a
---

> 原文：[2018-10-ReadingList](https://dirtmelon.github.io/posts/2018-10-ReadingList/)　·　dirtmelon

https://nshipster.cn/hashable/ Hash在 swift 中的进化史

https://www.appcoda.com/memory-management-swift/ strong weak 与 unowned

https://oleb.net/2018/photos-data-model/ PhotoKit 是 iOS 提供给 app 进行相册相关操作的框架，作者从中发现了数据层部分是使用 CoreData 来编写的，讲述如何发现是使用 CreData 以及如何使用 Xcode 结合 .mom 文件来查看 Data Model 的结构

https://swiftrocks.com/writing-cleaner-view-code-by-overriding-loadview.html 如何通过 UIViewController 中的 loadView 方法来自义 ViewCtroller 的 view，从而达到将 ViewCtroller 中配置 view 的相关代码分离出来的目的，也可以结合 protocol 来减少要编写的模版代码，不过也有一些缺点。

https://swiftrocks.com/swift-associated-types-with-default-values.html 为 protocol 的关联类型提供默认值

https://www.swiftbysundell.com/posts/lightweight-presenters-in-swift 轻量的 Presenter 设计模式，套多一层中间层 Presenter 来分离各 ViewController ，各 ViewController 不直接调用其它 ViewController ，而是通过 Presenter 来进行调用。

https://www.avanderlee.com/swift/updating-swift-4-2/ Swift 4.2 一些变化 可以使用 self 来替代 strongSelf 使用 #warning 来替代 //MARK todo 使用 allCases 获取 enum 类型的所有 cases 使用 random 获取随机值或者 shuffled 获取打乱的数组

https://www.avanderlee.com/optimization/analysing-build-performance-xcode-10/ Xcode 10 中的 Build 性能分析，Xcode 10新增了一个 Build With Time Summary 的性能检测，可以分析 Build 的过程中具体过程所消耗的时间。 改进办法： Type checking of functions and expressions 类型判断有时会消耗很长的时间，可以通过设置 -Xfrontend -warn-long-expression-type-checking= 来检测那些超过 limit（时间限制，ms）的表达式，同样的，对于函数，可以使用 -Xfrontend -warn-long-function-bodies= 来开启检测。

在 debug 中开启 Whole Module 也可以优化 Build 性能。

https://www.avanderlee.com/xcode/optin-features-xcode-10/ Xcode 10 中一些配置：Code folding ，Whole Module 等。

https://www.swiftbysundell.com/posts/reusable-data-sources-in-swift 将 dataSources 从 View Controller 中分离出来，进行复用。

https://www.objc.io/blog/2018/09/18/imperative-or-functional/ 如何结合命令式和函数式编程的 tips

https://www.swiftbysundell.com/posts/different-flavors-of-view-models-in-swift 使用 View Model 将逻辑从 View Controller 中分离出来

https://www.avanderlee.com/swift/performance-collections/ 集合中函数式操作的性能优化 使用 `contains` 代替 `first(where:) != nil` 使用 `isEmpty` 代替 count 与 0 比较 使用 `isEmpty` 来检测 String 是否为空 使用 `first(where:)` 来代替 `filter` 后面追加 `first` 使用 `max()` 和 `min()` 开代替 `sorted()` 后的 `first` 和 `last` 使用 `allSatisfy(_:)` 来代替 `filter` 结合 `isEmpty` 判断是否所有对象都符合某个条件

https://nshipster.cn/ios-12/ iOS 12的一些变化 跟 app 开发有关的有： 在 iOS 12 的新 API 里，你可以把 URLRequest 对象networkServiceType 设置为 NSURLNetworkServiceTypeResponsiveData，从而让一些时间敏感的操作优先请求。 根据电话号码和邮件地址匹配联系人。 新密码的自动输入与一次性验证码在文本框里的输入。

https://nshipster.cn/cmmotionactivity/ CMMotionActivityManager 处理设备中传感器的原始数据并告诉你（有多确定）用户是否正在移动，和用户是在行走、跑步、骑行或者开车

https://swift.gg/2018/10/15/creating-and-modifying-nsurl-in-swift-4/ Swift 中 URL 的相关方法
