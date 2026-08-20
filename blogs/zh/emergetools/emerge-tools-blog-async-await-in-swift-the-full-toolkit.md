---
title: 'Emerge Tools Blog | Swift 中的 Async await：完整工具包'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:7967d4f36025a698'
translated: true
---

> 原文：[Emerge Tools Blog | Async await in Swift: The Full Toolkit](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit)　·　Emerge Tools Blog

# Swift 中的 Async await：完整工具包

2024 年 7 月 22 日

Jacob Bartlett

SwiftiOS客座文章

![Swift 中的 Async await：完整工具包](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcover.afa0c323.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

这是我最喜欢的 iOS 面试问题之一：

> "请告诉我 Swift 并发中可用的工具，以及你会在什么情况下使用它们。"

我喜欢这个问题，因为它具有开放性，能让面试者展示初级、中级或高级的知识水平。它不仅仅是要求列举语法，还能考察面试者是否能判断在哪些情况下使用哪种工具最合适。

今天，我们将逐一介绍 Swift 并发工具包中的多种技术。我们会在适当的时候讨论理论，同时也会为每种工具提供一个可能的最佳使用场景。

## [工具包](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#the-toolkit)

- [async / await](#async-await)
- [async let](#async-let)
- [Task](#task)
- [任务组](#task-group)
- [Actor](#actors)
- [MainActor](#main-actor)
- [Sendable](#sendable)
- [Continuation（理论）](#continuations-theory)
- [Continuation（实践）](#continuations-practice)
- [AsyncSequence](#async-sequence)
- [AsyncStream](#async-stream)
- [Async Algorithms](#async-algorithms)

### [async / await](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#async-await)

这是 Swift 并发最基础的语法构建块。

将函数标记为 `async` 会告诉 Swift 编译器该函数可以被挂起。`await` 关键字则标记了这些挂起点。当到达一个挂起点时，Swift 运行时可以将栈帧的状态作为*async 帧*存储在堆上，以便稍后恢复执行。

当函数在 `await` 调用处被挂起时，它正在执行的线程可以用来执行其他工作。当等待的工作完成后，运行时可以恢复该函数的执行。

让我们从一个非常简单的语法示例开始，从 API 获取数据：

```swift
func fetchUserData() async -> User { 
  let userData = await userAPI.fetchUserData()
  return userData
}
```

`async` 函数只能从异步上下文中调用。这意味着另一个 async 函数、一个 Task，甚至可能是一个 `async` 的 `main()` 函数（在命令行应用中）。

### [async let](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#async-let)

并发最基本的用例是让 CPU 在等待慢速操作（例如网络请求）完成时执行其他工作。下一个最基本的用例可能是并行执行多个慢速操作。`async let` 是实现这一目标的最简单方法。

如果简单使用 async/await，可能会给代码引入瓶颈：

```swift
func populateStorefront() async {
  // 耗时 0.4 秒
  self.products = await fetchProducts()

  // 耗时 0.3 秒
  self.promotions = await fetchPromotions()

}

// 总执行时间：0.7 秒
```

这里的问题是两个慢速网络请求是*顺序*等待的。通过让这些等待时间重叠，即让请求*并行*运行，我们可以显著提高性能。

使用 async let，我们可以同时启动这些操作：执行不会挂起，直到第一个 await 处，此时两个网络请求都已发出。

```swift
func populateStorefront() async {
  // 网络请求几乎同时开始
  async let products = fetchProducts()
  async let promotions = fetchPromotions()

  // 等待 0.4 秒
  self.products = await products

  // 无需等待——结果已在
  self.promotions = await promotions
}

// 总执行时间：0.4 秒
```

这使你可以管理瓶颈，并高效地执行任意的异步工作负载——对于可以使用 async let 调用的函数类型没有限制。

### [Task](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#task)

如果说 async/await 是 Swift 并发的语法构建块，那么 Task 就是基础数据结构：“异步工作的单元”。

Task 本身非常有用——它们是 Swift 并发提供的从同步上下文内部启动异步工作的唯一方式：

```swift
func fetchAndSetProducts() {
  Task {
      let products = await fetchProducts()
      self.products = products
  }
}
```

这被称为*非结构化并发*，因为这个新 Task 没有父级关系——它不属于现有的*任务树*。

Task 以树状层次结构组织，父 Task 可以衍生多个子 Task。如果 Task 被取消，取消状态会从父 Task 级联到其所有子 Task。Task 在被取消时会继续工作——但我们可以在代码中检查此状态并终止处理。这被称为*协作取消*。

当你将 Task 用作属性、考虑可能的取消并等待结果时，会出现更高级的 Task 用例：

```swift
var calculationTask: Task<Double, Error>?

func calculateProfits() async throws -> Double? {
  calculationTask = Task {
      let data = await fetchFinancialData()
      try Task.checkCancellation()
      return performExpensiveNumberCrunching(on: data)
  }

  return try await calculationTask?.value
}
```

这使你可以避免在 Task 已被取消时执行昂贵的工作。

### [任务组](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#task-group)

任务组是另一种更高级的并行化方法。

与允许你同时等待*固定数量*的*任意*函数的 `async let` 相比，任务组允许你等待*任意数量*的*特化*函数。

如果这不清楚，让我们用一个简单的例子来演示——我们想为数组中的每个学生向后端提交考试成绩：

```swift
func submitExamResults(for students: [Student]) async {
  await withTaskGroup(of: Void.self) { group in 
      for student in students {
          group.addTask {
              await submit(results: student.examResults)
          }
      }
  }
}
```

在这里，我们同时对每个学生的考试成绩运行相同的函数 `submit(results:)` 方法，并在所有这些函数完成时返回。

`await withTaskGroup` 是这里的核心语法，我们传递 `Void` 类型，因为组中的异步函数不返回任何东西——我们只是想要并行执行工作。我们也可以使用 `withThrowingTaskGroup` 来添加错误处理，将 `await` 替换为 `try await`。

任务组在其初始化器中通过渐进式公开隐藏了另一个用例：从异步任务的结果中构建返回值。

例如，这里我们一次批量获取多张图片：

```swift
func profileImages(from urls: [URL]) async -> [UIImage] {
  await withTaskGroup(of: UIImage.self, returning: [UIImage]) { group in
      for url in urls {
          group.addTask { fetchImage(for: url) }
      }
      var images: [UIImage]
      for await image in group {
          images.append(image)
      }
      return images
  }
}
```

> *快速提醒——这些不一定会按原始顺序返回结果！*

这里构建返回值利用了任务组遵循 AsyncSequence 的事实，这允许我们使用 `for await in` 语法。稍后会详细介绍。

### [Actor](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#actors)

Actor 是引用类型的实体，它强制对其方法和状态进行串行访问。这使得它们非常适合需要并发访问数据同时避免竞态条件的工作。

你可以将 Actor 想象成在内部串行优先级队列上运行所有工作的类。在 Swift 并发中，这被称为[串行执行器](https://swiftrocks.com/how-actors-work-internally-in-swift)。

认证是 Actor 的经典用例：

```swift
actor AuthService {
  
  /// 返回最新的身份验证令牌。
  /// 如果本地的 bearer 令牌已过期，则会刷新它。
  ///
  func getBearerToken() async throws -> String {
      try await fetchValidAuthToken()
  }
}
```

由于你精通 async let 和任务组，你的 App 可能会同时执行许多网络请求。因此，`AuthService` 需要能够安全地从多个地方同时调用。

此外，我们只想在（每个过期周期内）刷新一次过期的身份验证令牌，所以每个网络请求必须停下来等待*同一个令牌*，而不是每个请求都触发一次单独的刷新。

Actor 是*可重入*的。它们强制对其状态进行串行访问，Actor 上的方法一次只能由一个 Task 执行。但是，方法仍然可以在 `await` 处挂起。在此挂起期间，同一个方法可能会被另一个 Task 启动。该 Task 又可能挂起，然后两个 Task 中的任何一个都可能恢复执行。

这种多线程执行被称为*交错执行*。

我们可以利用关于可重入性和交错执行的知识，结合 Task，来实现理想的认证场景：

```swift
actor AuthService {
  
  private var tokenTask: Task<String, Error>?
  
  func getBearerToken() async throws -> String {
      
      if tokenTask == nil {
          // actor 确保一次只能存在一个 Task
          tokenTask = Task { try await fetchValidAuthToken() }
      }
         
      defer { tokenTask = nil }

      // 所有请求在此处挂起，等待 Task 完成
      return try await tokenTask!.value
  }
}
```

现在，我们所有的网络请求完美地协同工作。

> *这可能是本文中最难的代码，所以请花时间逐步理解它。如果你想深入了解，可以阅读 [Advanced Swift Actors: Re-entrancy & Interleaving](https://jacobbartlett.substack.com/p/advanced-swift-actors-re-entrancy)。*

### [MainActor](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#main-actor)

Actor 确保其所有代码执行和状态更改都在串行执行器上运行，该执行器执行所有工作，就像在单个串行队列上一样。

对此有很多用例，但有一个自然产生：单线程 UI 工作。与主队列一样，有一个主要 Actor 在主线程上执行其所有工作。

你可以将函数——或整个类——约束到主要 Actor，以确保它们永远不会在主线程之外执行工作。这对于任何触及 UI 的代码来说都是良好实践，例如你的视图模型或视图控制器：

```swift
@MainActor @Observable 
final class LibraryViewModel { 
  var books: [Book] = [] 
  func fetchBooks() async { 
      books = await libraryAPI.fetchBooks()
  } 
}
```

你可能正在使用非结构化并发在同步 UI 线程上异步获取所需的模型。确保这也被约束到主要 Actor 是良好实践。通过在 Task 闭包中应用 `@MainActor` 特性可以轻松做到这一点。

```swift
func didPressButton() {
  Task { @MainActor in
      self.result = await buttonAction()
  }
}
```

在开始使用 Swift 并发时，一个非常常见的误解是不能在不阻塞主线程的情况下 `await` 约束到 `@MainActor` 的函数。

但这误解了 Swift 并发的设计方式：*[使用 Swift 并发编写的代码维护了一个运行时契约，确保线程始终能够向前推进](https://developer.apple.com/videos/play/wwdc2021/10254/?time=1216)*。

因此，当你在一个约束到主要 Actor 的函数上遇到 `await` 时，该函数会挂起，但主要 Actor 仍然能够在*其他地方*的其他方法上向前推进。一旦等待完成，该函数的其余部分会排队回到主要 Actor 的执行器上，以便在 UI 线程上完成运行。

### [Sendable](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#sendable)

Swift 并发的主要目标之一是在编译时防止数据争用（data race）。`Sendable` 协议是该难题中最关键的部分。

当一个类型遵循 Sendable 协议时，这意味着它是线程安全的。Sendable 类型可以安全地跨越任意并发上下文传递，而不会出现数据争用风险。这意味着它们可以被传递到 async 函数、Actor 和非结构化任务中，而不会遇到危险的并发问题。

Sendable 协议在 Swift 标准库中被广泛使用。此外，仅由 Sendable 类型组成的属性的具体值类型（结构体和枚举）是隐式 Sendable 的。如果关联类型是 Sendable，泛型值类型也可以遵循：

```swift
// Exam *不是*隐式 Sendable 的
struct Exam<Subject> { 
  var paper: Subject 
}

// Exam *是*隐式 Sendable 的
struct Exam<Subject: Sendable> { 
  var paper: Subject
}
```

如果类的属性是不可变的，类也可以遵循 Sendable 协议：

```swift
final class Employee: Sendable { 
  let employeeID: String
}
```

Actor 是隐式 Sendable 的。

闭包参数特性也可以标记为 `@Sendable`——这意味着传递到闭包中的任何值也必须是 Sendable 的，并且不能通过引用捕获。

这是一个相对无趣的方法：

```swift
func callClosureInATask(_ closure: @escaping () -> Void) {
  Task {
      closure()
  }
}
```

如果在 Xcode 中，我们开启 Swift 6 严格并发检查，我们会收到关于 `closure()` 的编译器警告：

`Capture of 'then' with non-sendable type '() -> Void' in a `@Sendable` closure`

我们可以将闭包标记为 `@Sendable` 来告诉编译器它是安全的：

```swift
func callClosureInATask(_ closure: @escaping @Sendable () -> Void) {
  Task {
      closure()
  }
}
```

现在，编译器警告消失了。Sendable 闭包按值捕获参数，避免了由冲突的、同时的变异引起的数据争用风险。

### [Continuation（理论）](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#continuations-theory)

Continuation 是 Swift 并发中一个关键的运行时实现细节：轻量级对象，当函数到达挂起点（`await`）时存储其状态，并允许稍后恢复执行。

听起来很熟悉？因为确实如此——[在运行时，continuation 由 async 帧表示](https://developer.apple.com/videos/play/wwdc2021/10254/?time=1038)。

众所周知，线程的开销很高。创建新线程需要大量内存，并且从线程到另一个线程的上下文切换需要相对较长的时间。Swift 并发使用 continuation 的抽象来廉价地管理异步上下文之间的切换，使系统能够达到理想的“每个 CPU 核心一个线程”的目标。

这与 Grand Central Dispatch 非常相似，其中队列是一种廉价、快速、轻量级的抽象，可以避免线程管理的开销。

### [Continuation（实践）](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#continuations-practice)

稍微令人困惑的是，也可以直接创建 continuation。

Continuation 可以弥合传统的基于闭包的异步 API 与现代 Swift 并发之间的差距。我们可以 `await`，创建一个 continuation，在闭包回调内部执行工作，然后使用结果或错误恢复 continuation，返回到挂起点。

iOS 拥有深厚的旧版 Objective-C 框架基础。将这些工具与 Swift 并发桥接通常涉及创建一个轻量级的 continuation 包装器。

在这里，我们使用 `ASWebAuthenticationSession` 在我们的 App 中实现 OAuth。这会呈现一个模态网页视图，允许用户使用 Google 登录，并返回一个包含身份验证令牌的回调 URL。

```swift
func runOAuthSession() async throws -> URL? {
  let authURL = URL(string: "https://authurl.com")!
  let scheme = "authapp://"
  return try await withCheckedThrowingContinuation { continuation in
      let session = ASWebAuthenticationSession(
          url: authURL,
          callbackURLScheme: scheme
      ) { url, error in
          if let error = error {
              // 出现问题
              continuation.resume(throwing: error) 
          } else {
              // 成功登录
              continuation.resume(returning: url) 
          }
      }
      session.start()
  }
}
```

### [AsyncSequence](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#async-sequence)

`AsyncSequence` 是一个协议，设计为 Swift 标准库中 [Sequence 协议](https://github.com/swiftlang/swift/blob/main/stdlib/public/core/Sequence.swift#L325) 的类比。

Sequence 表示一种提供对其元素进行顺序、迭代访问的类型。Sequence 通过一个[迭代器](https://github.com/swiftlang/swift/blob/main/stdlib/public/core/Sequence.swift#L177)实现，该迭代器提供 `next()` 元素，并且可以使用 `for-in` 语法在代码中使用循环进行迭代。

AsyncSequence 的行为方式相同，只是其迭代器上的 `next()` 方法是 `async` 的，这意味着运行时可以在序列产生的每个值之间挂起执行。我们甚至可以使用 `for-await-in` 语法围绕 AsyncSequence 创建循环。

AsyncSequence 提供了与 Combine 的无缝互操作。你可以使用发布者上的 `.values` 属性将任何 Publisher 转换为 AsyncSequence，将其转换为一个遵循 AsyncSequence 的 AsyncPublisher：

```swift
import Combine

let usersPublisher = PassthroughSubject<User, Never>()

func addAllUsers() async {
  for await user in usersPublisher.values {
      addFriend(user)
  }
}
```

我最近遇到了一个关于 AsyncSequence 的有趣“bug”。我们试图将两个 Combine 发布者转换为 async 序列，然后使用 `for-await-in` 循环处理这些值——但只有一组值被处理了。如果我们先将发布者合并为一个，序列就可以正常工作。

```swift
// 只处理好友，不处理照片
func handleFriendsAndPhotos() async {
  for await friend in friendsPublisher.values {
      // ...
  }
  
  for await photos in photosPublisher.values {
      // ...
  }
}

// 正常处理好友和照片
func handleFriendsAndPhotos() async {
  for await (friends, photos) in friendsPublisher
      .merge(with: photosPublisher) 
      .values {
          // ...
  }
}
```

你能发现问题吗？

我们最终意识到第一个 `for-await-in` 循环永远不会“结束”——它会永远监听第一个异步迭代器的值。因此，第二个用于另一个发布者的 `for-await-in` 循环永远无法执行！

### [AsyncStream](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#async-stream)

`AsyncStream` 是一种特殊的 AsyncSequence——一个你可以通过手动发送值来实例化和控制的具体类型（concrete type）。

AsyncStream 通过创建一个 continuation 并向其生成值来工作。这在包装发出多个回调的基于闭包的 API 时非常有用。AsyncStream 不是只返回（或抛出）一次的单个 continuation，它允许我们处理来自每个单独回调的值。

在这里，我们创建了一个 AsyncStream 与 `URLSessionDownloadDelegate` 一起使用，以跟踪长时间运行的文件下载的进度。

```swift
func trackDownload() -> AsyncStream<Double> {
  AsyncStream<Double> { continuation in 
      let delegate = DownloadProgressDelegate(continuation: continuation)
      URLSession.shared.delegate = progressDelegate
  }
}

final class DownloadProgressDelegate: NSObject, URLSessionDownloadDelegate {
  // ...
  let continuation: AsyncStream<Double>.Continuation

  func urlSession(_ session: URLSession,
                  downloadTask: URLSessionDownloadTask,
                  didWriteData bytesWritten: Int64,
                  totalBytesWritten: Int64,
                  totalBytesExpectedToWrite: Int64) {
      let progress = Double(totalBytesWritten) / Double(totalBytesExpectedToWrite)
      continuation.yield(progress * 100)
  }

}
```

### [Async Algorithms](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#async-algorithms)

Async Algorithms 严格来说并不是 Swift 并发的一部分，因为它是标准库之外的包。话虽如此，它通常被认为是 Combine 的替代品，所以不提它是不应该的。

[Async Algorithms](https://github.com/apple/swift-async-algorithms) 是开源 [Swift Algorithms](https://github.com/apple/swift-algorithms) 包的 Swift 并发对应物。它主要处理带有 AsyncSequence 的可迭代值序列。它包含影响值时机的算法，例如 `throttle()` 和 `debounce()`，将多个序列组合在一起的算法，例如 `zip()` 或 `combineLatest()`，以及修改输入的算法，例如 `compacted()`、`adjacentPairs()` 或 `removeDuplicates()`。

Async Algorithms 可以完成 Combine 的大部分功能，因此它们的用例类似：创建管道来响应异步值：

```swift
import AsyncAlgorithms

let sequence1: AsyncStream<Int> = //...
let sequence2: AsyncStream<Int> = //...

func handleDebouncedCombinedSequence() async {
  for await value in sequence1
      .combineLatest(with: sequence2)
      .removeDuplicates()
      .debounce(for: .seconds(1)) {    
          handle(value)
  }
}
```

## [结论](https://www.emergetools.com/blog/posts/swift-async-await-the-full-toolkit#conclusion)

了解语法和理论只是成功的一半。

作为一名工程师，至关重要的是了解你的完整工具包，并识别它在哪些情况下是最佳解决方案。

你已经知道获得这种经验的最佳方式：编写大量代码！

当你的代码尝试在错误的 Actor 上运行时，会遇到编译器错误；框架 API 会迫使你学习 continuation；使用 async let 后，性能瓶颈会神奇地消失。练习新技术，并将它们整合到你的工具包中。

🍺

Jacob Bartlett

这是来自 **Jacob Bartlett** 的 Emerge Tools 客座文章。如果你想阅读更多他的内容，可以[订阅 Jacob's Tech Tavern](https://jacobbartlett.substack.com)，每两周接收关于 iOS、Swift、技术和独立项目的深度文章；或者[在 Twitter 上关注他](https://twitter.com/jacobs_handle)。
