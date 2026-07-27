---
title: 使用 Combine 处理 URL 会话数据任务的结果
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processing-url-session-data-task-results-with-combine
source_url: 'https://developer.apple.com/documentation/foundation/processing-url-session-data-task-results-with-combine'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processing-url-session-data-task-results-with-combine.json'
content_hash: 'sha256:0b5de4d3220d166c'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md) · [URLSession](urlsession.md)

# 使用 Combine 处理 URL 会话数据任务的结果

<sub>文章</sub>

使用一系列异步操作符来接收和处理从 URL 获取的数据。

## 概述

使用 URL 会话执行任务本质上是异步的；从网络端点、文件系统和其他基于 URL 的来源获取数据需要时间。URL 加载系统通过将结果异步传递给委托或完成处理程序来应对这一点。[Combine](../combine.md) 框架也处理异步性；使用它来处理你的 URL 任务结果，可以简化并增强你的代码。

### 创建数据任务发布者

[URLSession](urlsession.md) 提供了一个 Combine 发布者 [DataTaskPublisher](urlsession/datataskpublisher.md)，它发布从 [URL](url.md) 或 [URLRequest](urlrequest.md) 获取数据的结果。你可以用 [dataTaskPublisher(for:)](<urlsession/datataskpublisher(for_)-5kiir.md>) 方法来创建这个发布者。任务完成后，它会发布以下二者之一：

- 一个元组，包含获取到的数据和一个 [URLResponse](urlresponse.md)（如果任务成功）。
- 一个错误（如果任务失败）。

与传递给 [- dataTaskWithURL:completionHandler:](<urlsession/datatask(with_completionhandler_)-52wk8.md>) 的完成处理程序不同，你的代码接收到的类型不是可选值，因为发布者已经将数据或错误解包了。

当使用 [URLSession](urlsession.md) 基于完成处理程序的代码时，你需要在处理程序闭包中完成所有工作：错误处理、数据解析等等。而当你改用数据任务发布者时，可以将许多这类职责转移给 Combine 操作符。

### 使用 Combine 操作符将传入的原始数据转换为你的类型

当数据任务成功完成时，它会向你的 App 传递一段原始 [Data](data.md)。大多数 App 都需要将这些数据转换为自己的类型。Combine 提供了执行这些转换的操作符，让你能够声明一系列处理操作。

数据任务发布者会产生一个包含 [Data](data.md) 和 [URLResponse](urlresponse.md) 的元组。你可以使用 [map(_:)](<../combine/publisher/map(__)-99evh.md>) 操作符将这个元组的内容转换为另一种类型。如果你想在检查数据之前先检查响应，可以使用 [tryMap(_:)](<../combine/publisher/trymap(__).md>)，并在响应不可接受时抛出错误。

要将原始数据转换为符合 [Decodable](../swift/decodable.md) 协议的自有类型，请使用 Combine 的 [decode(type:decoder:)](<../combine/publisher/decode(type_decoder_).md>) 操作符。

下面的示例结合了这两个操作符，将来自某个 URL 端点的 JSON 数据解析为一个自定的 `User` 类型：

```swift
struct User: Codable {
    let name: String
    let userID: String
}
let url = URL(string: "https://example.com/endpoint")!
cancellable = urlSession
    .dataTaskPublisher(for: url)
    .tryMap() { element -> Data in
        guard let httpResponse = element.response as? HTTPURLResponse,
            httpResponse.statusCode == 200 else {
                throw URLError(.badServerResponse)
            }
        return element.data
        }
    .decode(type: User.self, decoder: JSONDecoder())
    .sink(receiveCompletion: { print ("Received completion: \($0).") },
          receiveValue: { user in print ("Received user: \(user).")})
```

### 重试瞬时错误，并捕获、替换持续存在的错误

任何使用网络的 App 都应该预期会遇到错误，你的 App 应该优雅地处理这些错误。由于瞬时网络错误相当常见，你可能希望立即重试一个失败的数据任务。使用 [URLSession](urlsession.md) 的完成处理程序惯用法时，你需要创建一个全新的任务来执行重试。而使用数据任务发布者时，你可以改用 Combine 的 [retry(_:)](<../combine/publisher/retry(__).md>) 操作符。它通过将对上游发布者的订阅重新创建指定的次数来处理错误。不过，由于网络操作代价高昂，只应重试少量次数，并确保所有请求都是幂等的。

你还可以使用 Combine 操作符来替换错误，而不是让它到达订阅者：

- [catch(_:)](<../combine/publisher/catch(__).md>) 用另一个发布者替换错误。你可以将它与另一个 [DataTaskPublisher](urlsession/datataskpublisher.md) 搭配使用，例如一个从后备 URL 加载数据的发布者。
- [replaceError(with:)](<../combine/publisher/replaceerror(with_).md>) 用你提供的一个元素替换错误。如果这在你的应用程序中说得通，你可以用它为原本期望从该 URL 加载的值提供一个替代品。

下面的示例展示了这两种技巧：先重试一次失败的请求，之后再使用一个后备 URL。如果原始请求、重试请求或后备请求中任意一个成功，[sink(receiveValue:)](<../combine/publisher/sink(receivevalue_).md>) 操作符就会从该端点接收数据。如果三者都失败，sink 会收到一个 [Subscribers.Completion.failure(_:)](<../combine/subscribers/completion/failure(__).md>)。

```swift
let pub = urlSession
    .dataTaskPublisher(for: url)
    .retry(1)
    .catch() { _ in
        self.fallbackUrlSession.dataTaskPublisher(for: fallbackURL)
    }
cancellable = pub
    .sink(receiveCompletion: { print("Received completion: \($0).") },
          receiveValue: { print("Received data: \($0.data).") })
```

### 使用调度操作符在派发队列之间转移工作

当使用 [URLSession](urlsession.md) 的委托和完成处理程序惯用法时，会话会在一个固定的 [delegateQueue](urlsession/delegatequeue.md) 上回调你的代码。有时候，这意味着你的回调代码必须手动使用派发队列或其他调度 API，才能将工作放到特定的队列上。

有了 [DataTaskPublisher](urlsession/datataskpublisher.md)，你可以改用 Combine 的调度操作符。使用 [receive(on:options:)](<../combine/publisher/receive(on_options_).md>) 来指定你希望链中后续操作符和你的订阅者如何调度工作。[DispatchQueue](../dispatch/dispatchqueue.md) 和 [RunLoop](runloop.md) 都实现了 Combine 的 [Scheduler](../combine/scheduler.md) 协议，因此你可以用它们来接收 URL 会话数据。下面这段代码确保 sink 在主派发队列上记录其结果。

```swift
cancellable = urlSession
    .dataTaskPublisher(for: url)
    .receive(on: DispatchQueue.main)
    .sink(receiveCompletion: { print ("Received completion: \($0).") },
          receiveValue: { print ("Received data: \($0.data).")})
```

### 与多个订阅者共享数据任务发布者的结果

你可能希望在应用程序的不同部分使用来自该 URL 端点的数据。由于网络请求代价高昂，不要不必要地重复发出请求。Combine 让你可以为单个 [DataTaskPublisher](urlsession/datataskpublisher.md) 使用多个订阅者，同时让该发布者只用一次请求就为所有订阅者提供服务。

要支持多个下游订阅者，请使用 [share()](<../combine/publisher/share().md>) 操作符。这个操作符的工作方式类似于 [Publishers.Multicast](../combine/publishers/multicast.md) 和 [PassthroughSubject](../combine/passthroughsubject.md) 发布者的组合。你可以将多个操作符链或订阅者连接到 [share()](<../combine/publisher/share().md>) 操作符上，任何上游发布者都只会看到一个下游。对于 [DataTaskPublisher](urlsession/datataskpublisher.md) 而言，这意味着它只会执行一次数据任务。

下面的示例将一个 URL 会话数据任务用于两个互不相关的目的。一个订阅者使用返回的数据来解析前面见过的自定 `User` 类型，并将其记录在主派发队列上。第二个订阅者只关心 [URLResponse](urlresponse.md)，它会检查该响应以打印 HTTP 状态码，并不关心自己使用哪个队列。通过使用 [share()](<../combine/publisher/share().md>)，数据任务发布者只需从该 URL 端点加载一次，就能为两个订阅者提供服务。

```swift
let sharedPublisher = urlSession
    .dataTaskPublisher(for: url)
    .share()

cancellable1 = sharedPublisher
    .tryMap() {
        guard $0.data.count > 0 else { throw URLError(.zeroByteResource) }
        return $0.data
    }
    .decode(type: User.self, decoder: JSONDecoder())
    .receive(on: DispatchQueue.main)
    .sink(receiveCompletion: { print ("Received completion 1: \($0).") },
          receiveValue: { print ("Received id: \($0.userID).")})

cancellable2 = sharedPublisher
    .map() {
        $0.response
    }
    .sink(receiveCompletion: { print ("Received completion 2: \($0).") },
           receiveValue: { response in
            if let httpResponse = response as? HTTPURLResponse {
                print ("Received HTTP status: \(httpResponse.statusCode).")
            } else {
                print ("Response was not an HTTPURLResponse.")
            }
    }
)

```

为了证明这段代码只加载一次数据，可以临时在 [share()](<../combine/publisher/share().md>) 操作符之前放一个 [print(_:to:)](<../combine/publisher/print(__to_).md>) 调试操作符。当 App 运行时，Xcode 的控制台输出会显示它只从数据任务发布者收到了一个值，即便两个订阅者都收到了各自期望的结果。

请注意，一旦 [DataTaskPublisher](urlsession/datataskpublisher.md) 从下游订阅者那里出现未满足的需求，URL 会话就会开始加载数据。在这种情况下，这发生在第一个 sink 订阅者附加上去的时候。如果你需要额外的时间来附加其他订阅者，可以使用 [makeConnectable()](<../combine/publisher/makeconnectable().md>) 将 [Publishers.Share](../combine/publishers/share.md) 发布者包装成一个 [ConnectablePublisher](../combine/connectablepublisher.md)。在连接好所有订阅者之后，对该可连接发布者调用 [connect()](<../combine/connectablepublisher/connect().md>)，以允许数据加载开始。

## 另请参阅

### 将任务作为 Combine 发布者执行

- [dataTaskPublisher(for:)](<urlsession/datataskpublisher(for_)-61v3e.md>) — 返回一个发布者，它为给定的 URL 请求包装了一个 URL 会话数据任务。
- [dataTaskPublisher(for:)](<urlsession/datataskpublisher(for_)-5kiir.md>) — 返回一个发布者，它为给定的 URL 包装了一个 URL 会话数据任务。
- [DataTaskPublisher](urlsession/datataskpublisher.md) — 一个传递执行 URL 会话数据任务结果的发布者。
