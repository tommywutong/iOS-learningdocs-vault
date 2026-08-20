---
title: 你必须手动注销基于 block 的 NotificationCenter 观察者吗？
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2018/01/notificationcenter-removeobserver/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9a620defe3b33920'
translated: true
---

> 原文：[Do you have to manually unregister block-based NotificationCenter observers?](https://oleb.net/blog/2018/01/notificationcenter-removeobserver/)　·　Ole Begemann

# 你必须手动注销基于 block 的 NotificationCenter 观察者吗？

**长话短说：** 是的。（在 iOS 11.2 上测试过。）

几周前，我在 Twitter 上问了这个问题：

> 在 iOS 11 中，是否仍然需要注销基于 _block_ 的通知中心（notification center）观察者（observer）？Apple 文档存在歧义：[`addObserver(forName:object:queue:using:)`](https://developer.apple.com/documentation/foundation/notificationcenter/1411723-addobserver) 的文档说需要；而 [`removeObserver(_:)`](https://developer.apple.com/documentation/foundation/notificationcenter/1413994-removeobserver) 的文档则说 iOS 9+ 不再需要。
> 
> [@olebegemann](https://twitter.com/olebegemann)
> 
> Ole Begemann
> 
> [December 5, 2017](https://twitter.com/olebegemann/status/938085544780877824)

我收到了很多相互矛盾的回复。赞同和反对的比例差不多是 50/50。

那么，让我们测试一下实际会发生什么。

# 问题

我所说的基于 block 的 API 是 [`NotificationCenter.​addObserver​(forName:​object:​queue:​using:)`](https://developer.apple.com/documentation/foundation/notificationcenter/1411723-addobserver)。我们向通知中心注册一个函数，当匹配的通知到达时，这个函数会被调用。返回值是一个不透明的 token，代表这次观察（observation）：

```
class MyObserver {
    var observation: Any? = nil

    init() {
        observation = NotificationCenter.default.addObserver(
            forName: myNotification, object: nil, queue: nil) { notification in
                print("Received \(notification.name.rawValue)")
            }
    }
}
```

问题是：当 `observation` token 被销毁时（即 `MyObserver` 实例被释放时），通知中心会丢弃这个 block 并停止通知我们吗？基于 [`KeyPath`](https://developer.apple.com/documentation/swift/key-path-expressions) 的 [KVO API](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/observe(_:options:changehandler:)) 就是这样工作的，所以期望通知以同样的方式工作也是可以理解的。

还是我们必须手动调用 [`NotificationCenter.​removeObserver(_:)`](https://developer.apple.com/documentation/foundation/notificationcenter/removeobserver(_:)-2yciv)（例如在 `MyObserver` 的 [`deinit`](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/deinitialization/) 中）？

# 文档怎么说

基于选择器（selector）的观察 API [`addObserver(_:​selector:​name:​object:)`](https://developer.apple.com/documentation/foundation/notificationcenter/1415360-addobserver) 在 iOS 9/OS X 10.11 中使手动注销变为可选。当时进行这项更改时，[Foundation 发布说明明确表示](https://developer.apple.com/library/content/releasenotes/Foundation/RN-FoundationOlderNotes/index.html#10_11NotificationCenter)基于 block 的观察者仍然需要手动操作：

> 通过 `-[NSNotificationCenter addObserver​ForName:​object:​queue:​usingBlock:]` 方法添加的基于 block 的观察者，在不再使用时仍然需要注销，因为系统仍然持有对这些观察者的强引用。

从那以后有什么变化吗？

[`addObserver(forName:​object:​queue:​using:)` 的文档](https://developer.apple.com/documentation/foundation/notificationcenter/1411723-addobserver)也非常明确地指出需要注销：

> 你必须在 `addObserver(forName:​object:​queue:​using:)` 指定的任何对象被释放之前，调用 [`removeObserver(_:)`](https://developer.apple.com/documentation/foundation/notificationcenter/removeobserver(_:)-2yciv) 或 [`removeObserver(_:​name:​object:)`](https://developer.apple.com/documentation/foundation/notificationcenter/removeobserver(_:name:object:))。

然而，[`removeObserver(_:)` 的文档](https://developer.apple.com/documentation/foundation/notificationcenter/removeobserver(_:)-2yciv)似乎与此矛盾：

> 如果你的 App 目标为 iOS 9.0 及更高版本或 macOS 10.11 及更高版本，则不需要在其 `dealloc` 方法中注销观察者。

这没有区分基于 block 和基于选择器（selector）的 API。

# 测试 App

我编写了一个测试 App，让你可以检查各种场景下的行为（通过 Xcode 的控制台）。[代码在 GitHub 上可用](https://github.com/ole/NotificationUnregistering)。

以下是我的发现：

- **是的，你仍然需要手动注销基于 block 的观察（截至 iOS 11.2）。** `removeObserver(_:)` 的文档即使不是错误的，也至少具有误导性。
- 如果你不注销，通知中心将永久保留观察者 block，并持续为每个传入的通知调用它。这是否会对你的 App 造成严重破坏，取决于你在 block 中执行的操作（以及 block 捕获了哪些对象）。
- 如果你在 `deinit` 中进行注销，**你必须确保不要在观察者 block 中捕获 `self`。** 如果你这样做了，你的 `deinit` 将永远不会被调用，因为 block 持有了 `self`（阻止了它的销毁），而通知中心持有对 block 的强引用。你的对象将永远存在。

# 自动注销

处理这个不便的最佳方法是什么？我建议你为通知中心返回的观察 token 编写一个小的包装类。包装对象存储 token 并等待自己被释放。它唯一的任务是在自己的析构器（deinitializer）中调用 `removeObserver(_:)`：

```
/// 包装从 
/// NotificationCenter.addObserver(forName:object:queue:using:)
/// 接收到的观察者 token，并在 deinit 中注销。
final class NotificationToken: NSObject {
    let notificationCenter: NotificationCenter
    let token: Any

    init(notificationCenter: NotificationCenter = .default, token: Any) {
        self.notificationCenter = notificationCenter
        self.token = token
    }

    deinit {
        notificationCenter.removeObserver(token)
    }
}
```

这将通知观察的生命周期绑定到包装对象的生命周期。我们所要做的就是在私有属性中存储这个包装器，这样当它的拥有者被释放时，它也会被销毁。因此，这相当于在 `deinit` 中手动注销，但好处是你不会再忘记它。并且通过将该属性设为 `Optional​<Notification​Token>`，你可以随时通过赋值 `nil` 来注销。这种模式被称为 [_资源获取即初始化（RAII）_](https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization)。

让我们也为 `NotificationCenter` 编写一个便利方法，它负责为我们包装观察 token：

```
extension NotificationCenter {
    /// addObserver(forName:object:queue:using:) 的便利包装，
    /// 返回我们的自定义 NotificationToken。
    func observe(name: NSNotification.Name?, object obj: Any?, 
        queue: OperationQueue?, using block: @escaping (Notification) -> ())
        -> NotificationToken
    {
        let token = addObserver(forName: name, object: obj, queue: queue, using: block)
        return NotificationToken(notificationCenter: self, token: token)
    }
}
```

现在，将对 `addObserver(forName:​object:​queue:​using:)` 的所有调用替换为新 API，将 token 存储在一个属性中，你就可以免费获得自动注销。

Chris 和 Florian 也在 [Swift Talk 第 27 集：类型化通知](https://talk.objc.io/episodes/S01E27-typed-notifications-part-1)中展示了这项技术（以及其他很酷的通知相关内容）。我强烈推荐。
