---
title: 'Emerge Tools 博客 | 内存泄漏：一个 Xcode 侦探故事'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/the-memory-leak-an-xcode-detective-story'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:420a9d5e2d3ee99b'
translated: true
---

> 原文：[Emerge Tools 博客 | 内存泄漏：一个 Xcode 侦探故事](https://www.emergetools.com/blog/posts/the-memory-leak-an-xcode-detective-story)　·　Emerge Tools 博客

# 内存泄漏：一个 Xcode 侦探故事

2024 年 9 月 11 日

作者：

Jacob Bartlett

iOSSwift客座文章

![内存泄漏：一个 Xcode 侦探故事](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcover.e9bc06ac.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

我最近遇到了一个关于深层链接（deep link）的有趣 bug。

有时，在点击推送通知时，一些用户报告目标屏幕出现了两次——App 会打开，导航到正确的屏幕，但屏幕的 push 过渡效果会发生两次。

我开始调查，没有意识到这个兔子洞有多深。

### [深层链接的工作原理](https://www.emergetools.com/blog/posts/the-memory-leak-an-xcode-detective-story#how-deep-linking-works)

在调试之前，关键是确保我们理解正在处理的系统，所以让我们先对深层链接达成共识。

我的 App 采用了一种相当常见的基于协调器（coordinator）的架构：顶层有一个 `AppCoordinator`，每个标签页有子协调器。它们处理整个 App 的导航。如果你不熟悉这种架构，可以查看 [SwiftUI Apps at Scale](https://jacobbartlett.substack.com/p/swiftui-apps-at-scale) 了解更多细节。

深层链接允许用户从超链接或推送通知直接导航到 App 中的特定屏幕。这是提高 App 用户参与度的重要工具。

我们使用顶层的 `DeepLinkHandler` 构建了深层链接，并将它的接口传递给了 App 的每个协调器。

```swift
public protocol DeepLinkHandler {
  func open(url: URL)
  func publisher(for link: DeepLink) -> AnyPublisher<Void, Never>
}
```

我们的顶层 `SceneDelegate` 通过一个委托（delegate）回调 `scene(openURLContexts:)` 来响应链接，将 URL 传递给深层链接处理器。

在内部，深层链接处理器使用一个正则表达式将 URL 转换为 `DeepLink` 枚举 case，并向链接对应的 Combine 发布者（publisher）发送信号。

子协调器被设置为监听特定的发布者，并在从 `DeepLinkHandler` 接收到信号时触发导航：

```swift
// MyDataCoordinator.swift
func listenToDeepLinks() {
  deepLinkHandler
      .publisher(for: .myDataDeepLink)
      .sink { [weak self] in 
          self?.navigate(to: .myDataScreen)
      }
      .store(in: &cancellables)
}
```

这个设置到目前为止运行得很好。

### [寻找复现步骤](https://www.emergetools.com/blog/posts/the-memory-leak-an-xcode-detective-story#seeking-repro)

一旦我们理解了系统的预期行为，修复 bug 最关键的要素就是复现步骤——可靠地重现问题所需的步骤。

我不会用我（冗长得令人尴尬的）调查过程来烦你，但我最终达到了复现的黄金标准——100% 重现 bug 的步骤。

当我登出并重新登录后，深层链接总会导致这种双重 push 导航动画。如果我退出并重新启动 App，开始一个新的 App 会话，深层链接就会正常工作。

这个关键线索告诉我下一步该往哪里看。

### [大量打印语句](https://www.emergetools.com/blog/posts/the-memory-leak-an-xcode-detective-story#lots-of-print-statements)

我承认，在调试方面我是个老派的人。

Xcode 给了我们大量花哨的调试工具，从可执行代码的断点，到使用 LLDB 调试器步入调用栈。

但我喜欢老式的打印语句。大量的打印语句。

让我们在调用栈中撒满它们。按照我们的 bug 复现步骤——登出并重新登录——现在我们可以分析点击深层链接时的控制台输出。

```swift
// SceneDelegate.swift 
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
  guard let urlContext = URLContexts.first else { return }
  let url = urlContext.url
  print(url)
  deepLinkHandler.open(url: url)
}
```

在打开深层链接时，`SceneDelegate` 中的打印语句按预期工作，只触发了一次。所以我们知道系统处理 URL 的方式没有异常。

```swift
// DeepLinkHandler.swift 
public func open(url: URL) {
  guard let link = DeepLink.link(from: url) else { return }
  print(link)
  _publisher(for: link).send(())
}
```

我们的深层链接处理器似乎也表现正常；打印了一次链接，并向 Combine 发布者发送了一次信号。

```swift
// MyDataCoordinator.swift
func listenToDeepLinks() {
  deepLinkHandler
      .publisher(for: .myDataDeepLink)
      .sink { [weak self] in 
          print(self)
          self?.navigate(to: .myDataScreen)
      }
      .store(in: &cancellables)
}
```

处理深层链接的协调器行为异常。

它打印了 _两次_。

这可能是我们的决定性证据。这个深层链接监听器被触发了两次，导致 `navigate(to:)` 方法被调用了两次，从而引起了用户报告的双重导航 bug！

### [内存泄漏](https://www.emergetools.com/blog/posts/the-memory-leak-an-xcode-detective-story#a-memory-leak)

凭借我编写糟糕代码的辉煌职业生涯，我培养出了一些敏锐的本能。那种偶尔能让我看起来像雨人的本能。

- 每当有人看到无法解释的 403 HTTP 错误时，那就是 CORS。
- 每当实习生的表格视图不工作时，他们忘记了设置 delegate。
- 每当某件事发生两次时，那就是内存泄漏（memory leak）。

我将打印语句升级，记录协调器实例的堆内存（heap memory）地址，以便获取更多信息。

```swift
print(Unmanaged.passUnretained(self).toOpaque())
```

再次运行复现步骤，触发深层链接，并观察到它被触发了两次。我的直觉是对的：

![打印内存地址](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog26%2F1.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

调试器打印出的堆内存地址是：

- `0x00006000000108d0`
- `0x000060000002b7b0`

这意味着深层链接本身只被处理了一次，但处理它的协调器却有_多个实例_。这就是我们观察到双重 push 导航的原因。

我们可以通过查看 Xcode 的 Debug 导览来进一步验证，重现 bug，然后选择“View Memory Graph Hierarchy”。在这里搜索 `MyDataCoordinator`，可以看到两个实例。

![内存图调试器中的 2 个实例](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog26%2F2.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

### [什么是内存泄漏？](https://www.emergetools.com/blog/posts/the-memory-leak-an-xcode-detective-story#what-is-a-memory-leak)

在继续之前，让我们确保大家对概念达成一致。

在运行的程序中使用的所有对象都保存在计算机的 RAM 或内存中（是的，我知道这有点简化）。

为了避免占用计算机系统的所有资源，编程语言被设计为“释放”程序不再需要的内存。根据语言的设计方式，这种内存管理可以是：

- 像 C/C++ 中的手动内存管理，开发者自己使用 `malloc` 和 `release` 来分配和释放内存。
- 像 Kotlin 或 Java 这样的语言有一个“垃圾回收器”，它会定期遍历系统内存并移除未使用的对象。
- Rust 使用一种编译器安全的**所有权（ownership）**系统来决定何时释放对象的内存。

Swift 使用引用计数（reference counting）来处理内存：

- **强引用（strong reference）**——即指向堆内存中类地址的指针——将 `refCount` 增加 1。
- **弱引用（weak reference）**指向内存，但不会增加 `refCount`。
- 当 [HeapObject](https://github.com/swiftlang/swift/blob/main/stdlib/public/runtime/HeapObject.cpp) 的 `refCount` 变为零时，它会立即被释放。

在 Swift 中，当开发者在管理这些引用时犯错时，可能会发生内存泄漏。他们可能无意中设置了一个从未被释放的强引用——也许是在一个捕获了 self 的闭包（closure）中——从而导致被引用的对象永远保留在内存中。

如果泄漏的对象自身拥有强引用，它还会以级联的方式保持它所强引用的所有对象存活。

要深入了解 Swift 底层内存工作原理，请查看 [COW2LLVM: The isKnownUniquelyReferenced Deep-Dive](https://jacobbartlett.substack.com/p/cow2llvm-the-isknownuniquelyreferenced) 或 [The Case Against unowned self](https://jacobbartlett.substack.com/p/the-case-against-unowned-self)。

### [一个巨大的内存泄漏](https://www.emergetools.com/blog/posts/the-memory-leak-an-xcode-detective-story#a-big-big-memory-leak)

我们现在有了清晰的认知——并且对这个系统的行为有了相当好的理解：

- 当你登出并重新登录时，当你从用户引导（onboarding）和认证屏幕过渡到主 App 时，主标签页协调器的新实例会被重新创建。
- 我们的 App 有一个内存泄漏，导致 `MyDataCoordinator` 在整个 App 会话期间保持存活。
- 因此，旧协调器中的深层链接监听器仍然活跃，导致深层链接导航被触发了两次。

令人担忧的是，这表明问题的范围比我最初从一个看似较小的导航问题预期的要大得多。

`MyDataCoordinator` 作为标签页上的顶层协调器，拥有几个包含子功能的子协调器。

因此，每当用户登出并重新登录时，所有这些功能的导航层次结构都保留在内存中。这还包括协调器、工厂类、服务以及许多在内存中缓存的 `@ObservedObject` 视图模型（view model）。

### [关键所在](https://www.emergetools.com/blog/posts/the-memory-leak-an-xcode-detective-story#the-name-of-the-game)

现在我们理解了问题，就很容易验证何时解决了它。

我们不需要通过触发深层链接的繁琐步骤，只需要确保在登出时 `MyDataCoordinator` 被释放。

在调试内存泄漏时，`deinit` 是你最好的朋友。我将它们添加到了所有 3 个主标签页协调器中。

```swift
deinit {
  print("deinit (self)")
}
```

登出时，其中两个标签页协调器调用了 `deinit`，但 `MyDataCoordinator`（持有有问题的深层链接）却没有。这意味着它强引用的所有实体和子协调器也保持存活。

现在我们知道关键所在了：当登出时 `deinit` 被触发，我们就赢了。

### [搜寻并摧毁](https://www.emergetools.com/blog/posts/the-memory-leak-an-xcode-detective-story#search-and-destroy)

回到内存图调试器，我们寻找决定性证据：一个不应该存在的强引用。

我们可以检查每个实例的内存图，通过比较很容易看出哪个是“好的”——这个版本的 `MyDataCoordinator` 整齐地存在于内存图中，与我们的主要导航基础设施（如 `SceneDelegate` 和 `AppCoordinator`）在一起。

然而，似乎还有一个来自视图模型的循环引用（circular reference），这是我们不期望的。

![“好的”实例](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog26%2F3.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

泄漏的实例相当明显：有一个单独的引用保持我们的协调器存活，旁边是一堆底层内存实体。

![泄漏的实例](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog26%2F4.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

由于这个强引用没有名称，这表明存在一个匿名函数（即一个闭包），而不是一个具有强引用的命名类。

想要表现得非常聪明，我打开了 Instruments 来在我的协调器中搜索泄漏和分配。不幸的是，输出没有给我们任何新信息。

![Instruments 分配工具](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog26%2F5.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

使用 Xcode 的工具，我们已经尽力了。我们需要一个新的策略：有条不紊地阅读我们的代码库，搜索有问题的闭包。

### [分而治之](https://www.emergetools.com/blog/posts/the-memory-leak-an-xcode-detective-story#divide-and-conquer)

当任何 bug 的来源不够清晰时，一个好的方法是缩小错误的影响范围。

通过时间来做这件事的方法是用像 `git bisect` 这样的命令。通过空间来做，你可以使用一个更粗暴的工具：**注释掉大量代码**。

首先，我可以在仍然能够构建 App 的前提下注释掉尽可能多的代码，包括所有子协调器、导航逻辑和私有方法。然后我检查 `MyDataCoordinator` 在登出时是否会被释放。

是的！

![deinit 被调用](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog26%2F6.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

我系统地重复这种方法，一次隔离一个方法和子协调器，每次构建后都重复 bug 复现步骤。

直到我发现了罪魁祸首。

### [罪魁祸首](https://www.emergetools.com/blog/posts/the-memory-leak-an-xcode-detective-story#the-culprit)

我隔离了有问题的代码块。

这 12 行代码决定了是泄漏整个导航栈，还是 App 按预期行为运行。

这个块也是我们深层链接逻辑的一部分，但它比简单的屏幕导航更复杂。

为了防止欺诈，用户只有在账户创建足够久之后才能访问此功能。一旦他们符合条件，我们会通过 CRM 发送链接。因此，在执行导航之前，我们首先与 API 进行异步检查，确认用户的账户是否符合条件。如果成功，我们就执行导航。

以下是代码——看看你是否能发现问题！

```swift
private func setupSpecialOffersDeepLink() {
  deepLinkHandler
      .publisher(for: .specialOffersDeepLink)
      .sink(receiveValue: {
          Task { [weak self] in
              if (await self?.offersService.userIsEligible() == true) {
                  self?.navigate(to: .specialOffersScreen)
              }
          }
      })
      .store(in: &cancellables)
}
```

老实说，这个问题既明显也不明显。等我解释了之后，你可能会拍自己的脑门。

### [修复泄漏](https://www.emergetools.com/blog/posts/the-memory-leak-an-xcode-detective-story#fixing-the-leak)

这段代码，表面上看，似乎在做所有能避免循环引用（retain cycle）的事情。它在使用 self 之前弱捕获了 self。它将 Combine 发布者存储在一组 `cancellables` 中。

但有一个问题。

只有当你真正理解闭包在 Swift 中做了什么时，这一点才变得清晰。

当我们使用 `Task { [weak self] in` 弱捕获 self 时，我们确实创建了一个对 self 的弱引用。

然而，这个捕获本身发生在一个已经存在的闭包内部，即传递给 Combine 的 `.sink(receiveValue: {` 的闭包。

闭包是一段存储在堆上的代码，独立于创建它的类。因此，在 Task 的 `[weak self]` 中使用的 self 是对 self 的一个隐式强引用，而不是对原始实体的弱引用。

我们需要将 `[weak self]` 放在 `.sink` 闭包上，而不是 Task 初始化器上：

```swift
private func setupSpecialOffersDeepLink() {
  deepLinkHandler
      .publisher(for: .specialOffersDeepLink)
      .sink(receiveValue: { [weak self] in
          Task {
              if (await self?.offersService.userIsEligible() == true) {
                  self?.navigate(to: .specialOffersScreen)
              }
          }
      })
      .store(in: &cancellables)
}
```

更新代码后，运行复现步骤，在登出时我们看到了 `deinit` 被调用！内存泄漏解决了。

查看内存图调试器，我们看到了预期的单个 `MyDataCoordinator` 实例，没有任何我们不期望的有问题的引用。

![修复后的内存图](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog26%2F7.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

### [结论](https://www.emergetools.com/blog/posts/the-memory-leak-an-xcode-detective-story#conclusion)

所以我遇到了一个内存泄漏。

一个由错误使用 `[weak self]` 引起的泄漏。🤷‍♂️。

但这个 bug 感觉值得写下来。用户报告的看似次要的“奇怪导航动画”——点击深层链接有时会导致 push 动画发生两次——我无法想象其背后竟然是这样一个严重的问题：每当用户重新登录时，App 一半的功能在内存中重复，而解决方案又如此简单，只需将 `[weak self]` 的捕获位置向上移动一行。

有问题的嵌套闭包在表面上是可接受的代码，带有一个非常微妙的循环引用。一旦通过代码审查并合并，这个 bug 一点也不明显。

这个故事有一个寓意。你上次用你的 App 检查 Xcode 内存图调试器是什么时候？也许在你的积压工作中有一个不起眼的 P4 bug，表面下潜伏着一个巨大的内存泄漏。

🍺

这是一篇来自 **Jacob Bartlett** 的 Emerge Tools 客座文章。如果你想看更多他的内容，可以[订阅 Jacob's Tech Tavern](https://jacobbartlett.substack.com)，每隔两周接收关于 iOS、Swift、技术和独立项目的深度文章；或者[在 Twitter 上关注他](https://twitter.com/jacobs_handle)。
