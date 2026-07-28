---
title: URLSession
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession
source_url: 'https://developer.apple.com/documentation/foundation/urlsession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession.json'
content_hash: 'sha256:cee884a7ed657445'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# URLSession

<sub>类</sub>

一个协调一组相关的网络数据传输任务的对象。

<sub>iOS、iPadOS、Mac Catalyst、macOS、tvOS、visionOS、watchOS</sub>

```swift
class URLSession
```

## 概述

[URLSession](urlsession.md) 类及相关类提供了一套 API，用于从 URL 指向的端点下载数据和向其上传数据。你的 App 还可以使用这套 API 在 App 未运行时，或在 iOS 中当 App 被挂起时，执行后台下载。你可以使用相关的 [URLSessionDelegate](urlsessiondelegate.md) 和 [URLSessionTaskDelegate](urlsessiontaskdelegate.md) 来支持认证，并接收重定向和任务完成等事件。

> [!note] 注意
> [URLSession](urlsession.md) API 涉及许多不同的类，它们以相当复杂的方式协同工作，如果你只看参考文档，这一点可能不太明显。在使用这套 API 之前，请阅读 [URL 加载系统](url-loading-system.md) 主题中的概述。基础、上传和下载部分中的文章提供了使用 [URLSession](urlsession.md) 执行常见任务的示例。

你的 App 会创建一个或多个 [URLSession](urlsession.md) 实例，每个实例协调一组相关的数据传输任务。例如，如果你正在创建一个网页浏览器，你的 App 可以为每个标签页或窗口创建一个会话，或者为交互式使用创建一个会话、为后台下载创建另一个会话。在每个会话中，你的 App 会添加一系列任务，每个任务代表对特定 URL 的请求（必要时会跟随 HTTP 重定向）。

### URL 会话的类型

给定 URL 会话中的任务共享一个共同的会话配置对象，该对象定义了连接行为，例如对单个主机的最大同时连接数、是否可以使用蜂窝网络等。

[URLSession](urlsession.md) 有一个单例 [sharedSession](urlsession/shared.md) 会话（它没有配置对象），用于基本请求。它的可定制性不如你创建的会话，但如果你需求非常有限，它是一个不错的起点。你可以通过调用 `shared` 类方法来访问这个会话。对于其他类型的会话，你可以使用以下三种配置之一来创建 [URLSession](urlsession.md)：

- 默认会话的行为与 `sharedSession` 非常相似，但允许你对其进行配置。你还可以为默认会话指定一个委托（delegate），以增量方式获取数据。
- 临时会话与 `sharedSession` 类似，但不会将缓存、Cookie 或凭据写入磁盘。
- 后台会话允许你在 App 未运行时在后台执行内容的上传和下载。

有关创建每种类型配置的详细信息，请参阅 [URLSessionConfiguration](urlsessionconfiguration.md) 类中的“创建会话配置对象”。

### URL 会话任务的类型

在会话中，你可以创建任务，这些任务可选地向服务器上传数据，然后从服务器检索数据，数据形式可以是磁盘上的文件，也可以是内存中的一个或多个 [NSData](nsdata.md) 对象。[URLSession](urlsession.md) API 提供了四种类型的任务：

- 数据任务使用 [NSData](nsdata.md) 对象发送和接收数据。数据任务适用于与服务器的简短、通常是交互式的请求。
- 上传任务类似于数据任务，但它们还会发送数据（通常以文件形式），并支持在 App 未运行时进行后台上传。
- 下载任务以文件形式检索数据，并支持在 App 未运行时进行后台下载和上传。
- WebSocket 任务使用 [RFC 6455](https://tools.ietf.org/html/rfc6455) 中定义的 WebSocket 协议，通过 TCP 和 TLS 交换消息。

### 使用会话委托（delegate）

会话中的任务还共享一个共同的委托（delegate）对象。你实现这个委托来处理各种事件的发生，并在事件发生时提供和获取信息，包括：

- 认证失败时。
- 数据从服务器到达时。
- 数据可用于缓存时。

如果你不需要委托提供的功能，可以在创建会话时传递 `nil` 来使用这套 API，而不提供委托。

> [!important] 重要
> 会话对象对委托保持强引用，直到你的 App 退出或显式地使会话失效（invalidate）。如果你不使会话失效，你的 App 会泄漏内存，直到 App 终止。

你使用会话创建的每个任务都会回调到会话的委托，使用 [URLSessionTaskDelegate](urlsessiontaskdelegate.md) 中定义的方法。你也可以通过填充单独的任务特定 [delegate](urlsessiontask/delegate.md)，在这些回调到达会话委托之前拦截它们。

### 异步性与 URL 会话

与大多数网络 API 一样，[URLSession](urlsession.md) API 是高度异步的。它通过三种方式将数据返回给你的 App，具体取决于你调用的方法：

- 如果你使用 Swift，可以使用标记有 `async` 关键字的方法来执行常见任务。例如，[data(from:delegate:)](<urlsession/data(from_delegate_).md>) 获取数据，而 [download(from:delegate:)](<urlsession/download(from_delegate_).md>) 下载文件。你的调用点使用 `await` 关键字来挂起运行，直到传输完成。你还可以使用 [bytes(from:delegate:)](<urlsession/bytes(from_delegate_).md>) 方法，将数据作为 [AsyncSequence](../swift/asyncsequence.md) 接收。使用这种方法时，你使用 `for`-`await`-`in` 语法在 App 接收数据时对其进行迭代。[URL](url.md) 类型还提供了一些便捷方法，可以从共享的 URL 会话中获取字节或行数据。
- 在 Swift 或 Objective-C 中，你可以提供一个完成处理程序（completion handler）`block`，它会在传输完成时运行。
- 在 Swift 或 Objective-C 中，随着传输的进行以及在传输刚结束时，你可以在委托方法中接收回调。

除了向委托传递这些信息外，[URLSession](urlsession.md) 还提供了状态和进度属性。如果你需要根据任务的当前状态（注意其状态可能随时变化）进行程序化决策，可以查询这些属性。

### 协议支持

[URLSession](urlsession.md) 类原生支持 `data`、`file`、`ftp`、`http` 和 `https` URL 方案，并根据用户系统偏好中的配置，透明地支持代理服务器和 SOCKS 网关。

[URLSession](urlsession.md) 支持 HTTP/1.1、HTTP/2 和 HTTP/3 协议。[RFC 7540](https://tools.ietf.org/html/rfc7540) 描述的 HTTP/2 支持要求服务器支持应用层协议协商（ALPN）。

你还可以通过子类化（subclassing）[URLProtocol](urlprotocol.md) 来添加对你自己的自定义网络协议和 URL 方案的支持（供你的 App 私有使用）。

### App Transport Security (ATS)

iOS 9.0 及更高版本和 macOS 10.11 及更高版本对所有使用 [URLSession](urlsession.md) 进行的 HTTP 连接都使用 App Transport Security (ATS)。ATS 要求 HTTP 连接使用 HTTPS ([RFC 2818](https://tools.ietf.org/html/rfc2818))。

更多信息，请参阅 [NSAppTransportSecurity](../bundleresources/information-property-list/nsapptransportsecurity.md)。

### Foundation 的拷贝行为

会话和任务对象遵循 [NSCopying](nscopying.md) 协议，具体如下：

- 当你的 App 拷贝一个会话或任务对象时，你会得到同一个对象。
- 当你的 App 拷贝一个配置对象时，你会得到一个新的副本，可以独立修改。

### 线程安全

URL 会话 API 是线程安全的。你可以自由地在任何线程上下文中创建会话和任务。当你的委托方法调用提供的完成处理程序时，工作会自动调度到正确的委托队列上。

## 关系

- **继承自**：[NSObject](../objectivec/nsobject-swift.class.md)

- **遵循**：[CVarArg](../swift/cvararg.md)、[CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)、[CustomStringConvertible](../swift/customstringconvertible.md)、[Equatable](../swift/equatable.md)、[Hashable](../swift/hashable.md)、[NSObjectProtocol](../objectivec/nsobjectprotocol.md)、[Sendable](../swift/sendable.md)、[SendableMetatype](../swift/sendablemetatype.md)

## 主题

### 使用共享会话

- [sharedSession](urlsession/shared.md) — 共享的单例会话对象。

### 创建会话

- [+ sessionWithConfiguration:](<urlsession/init(configuration_).md>) — 使用指定的会话配置创建一个会话。
- [+ sessionWithConfiguration:delegate:delegateQueue:](<urlsession/init(configuration_delegate_delegatequeue_).md>) — 使用指定的会话配置、委托（delegate）和操作队列创建一个会话。
- [URLSessionConfiguration](urlsessionconfiguration.md) — 一个配置对象，用于定义 URL 会话的行为和策略。
- [configuration](urlsession/configuration.md) — 此会话配置对象的副本。

### 使用委托（delegate）

- [delegate](urlsession/delegate.md) — 创建此对象时分配的委托。
- [URLSessionDelegate](urlsessiondelegate.md) — 定义 URL 会话实例在其委托上调用以处理会话级别事件（如会话生命周期更改）的方法的协议。
- [URLSessionTaskDelegate](urlsessiontaskdelegate.md) — 定义 URL 会话实例在其委托上调用以处理任务级别事件的方法的协议。
- [delegateQueue](urlsession/delegatequeue.md) — 创建此对象时提供的操作队列。

### 执行异步传输

- [bytes(for:delegate:)](<urlsession/bytes(for_delegate_).md>) — 根据指定的 URL 请求检索 URL 的内容，并提供异步字节序列。
- [bytes(from:delegate:)](<urlsession/bytes(from_delegate_).md>) — 检索给定 URL 的内容，并提供异步字节序列。
- [AsyncBytes](urlsession/asyncbytes.md) — 一个异步字节序列。
- [data(for:delegate:)](<urlsession/data(for_delegate_).md>) — 根据指定的 URL 请求下载 URL 的内容，并异步传递数据。
- [data(from:delegate:)](<urlsession/data(from_delegate_).md>) — 检索 URL 的内容，并异步传递数据。
- [data(for:)](<urlsession/data(for_).md>) — 使用 URLRequest 加载数据的便捷方法，内部会创建并恢复一个 URLSessionDataTask。
- [data(from:)](<urlsession/data(from_).md>) — 使用 URL 加载数据的便捷方法，内部会创建并恢复一个 URLSessionDataTask。
- [download(for:delegate:)](<urlsession/download(for_delegate_).md>) — 根据指定的 URL 请求检索 URL 的内容，并异步提供已保存文件的 URL。
- [download(from:delegate:)](<urlsession/download(from_delegate_).md>) — 检索 URL 的内容，并异步提供已保存文件的 URL。
- [download(resumeFrom:delegate:)](<urlsession/download(resumefrom_delegate_).md>) — 恢复先前暂停的下载，并异步提供已保存文件的 URL。
- [upload(for:from:delegate:)](<urlsession/upload(for_from_delegate_).md>) — 根据指定的 URL 请求将数据上传到 URL，并异步传递结果。
- [upload(for:fromFile:delegate:)](<urlsession/upload(for_fromfile_delegate_).md>) — 将数据上传到 URL，并异步传递结果。
- [upload(for:from:)](<urlsession/upload(for_from_).md>) — 使用 URLRequest 上传数据的便捷方法，内部会创建并恢复一个 URLSessionUploadTask。
- [upload(for:fromFile:)](<urlsession/upload(for_fromfile_).md>) — 使用 URLRequest 上传数据的便捷方法，内部会创建并恢复一个 URLSessionUploadTask。
- [URLSessionTaskDelegate](urlsessiontaskdelegate.md) — 定义 URL 会话实例在其委托上调用以处理任务级别事件的方法的协议。

### 向会话添加数据任务

- [- dataTaskWithURL:](<urlsession/datatask(with_)-10dy7.md>) — 创建一个检索指定 URL 内容的任务。
- [- dataTaskWithURL:completionHandler:](<urlsession/datatask(with_completionhandler_)-52wk8.md>) — 创建一个检索指定 URL 内容的任务，并在完成后调用一个处理程序。
- [- dataTaskWithRequest:](<urlsession/datatask(with_)-7jpys.md>) — 创建一个根据指定 URL 请求对象检索 URL 内容的任务。
- [- dataTaskWithRequest:completionHandler:](<urlsession/datatask(with_completionhandler_)-e6xv.md>) — 创建一个根据指定 URL 请求对象检索 URL 内容的任务，并在完成后调用一个处理程序。
- [URLSessionDataTask](urlsessiondatatask.md) — 一个 URL 会话任务，将下载的数据直接返回到 App 的内存中。
- [URLSessionDataDelegate](urlsessiondatadelegate.md) — 定义 URL 会话实例在其委托上调用以处理特定于数据任务和上传任务的任务级别事件的方法的协议。

### 向会话添加下载任务

- [- downloadTaskWithURL:](<urlsession/downloadtask(with_)-1onj.md>) — 创建一个下载任务，检索指定 URL 的内容并将结果保存到文件。
- [- downloadTaskWithURL:completionHandler:](<urlsession/downloadtask(with_completionhandler_)-7cuje.md>) — 创建一个下载任务，检索指定 URL 的内容，将结果保存到文件，并在完成后调用一个处理程序。
- [- downloadTaskWithRequest:](<urlsession/downloadtask(with_)-3fb7s.md>) — 创建一个下载任务，根据指定的 URL 请求对象检索 URL 的内容，并将结果保存到文件。
- [- downloadTaskWithRequest:completionHandler:](<urlsession/downloadtask(with_completionhandler_)-4a84s.md>) — 创建一个下载任务，根据指定的 URL 请求对象检索 URL 的内容，将结果保存到文件，并在完成后调用一个处理程序。
- [- downloadTaskWithResumeData:](<urlsession/downloadtask(withresumedata_).md>) — 创建一个下载任务，以恢复先前取消或失败的下载。
- [- downloadTaskWithResumeData:completionHandler:](<urlsession/downloadtask(withresumedata_completionhandler_).md>) — 创建一个下载任务，以恢复先前取消或失败的下载，并在完成后调用一个处理程序。
- [URLSessionDownloadTask](urlsessiondownloadtask.md) — 一个 URL 会话任务，将下载的数据存储到文件。
- [URLSessionDownloadDelegate](urlsessiondownloaddelegate.md) — 定义 URL 会话实例在其委托上调用以处理特定于下载任务的任务级别事件的方法的协议。

### 向会话添加上传任务

- [使用 SwiftNIO 构建可恢复上传服务器](building-a-resumable-upload-server-with-swiftnio.md) — 通过将可恢复上传转换为常规上传，在 SwiftNIO 中支持 HTTP 可恢复上传协议。
- [- uploadTaskWithRequest:fromData:](<urlsession/uploadtask(with_from_).md>) — 创建一个任务，对指定的 URL 请求对象执行 HTTP 请求，并上传提供的数据。
- [- uploadTaskWithRequest:fromData:completionHandler:](<urlsession/uploadtask(with_from_completionhandler_).md>) — 创建一个任务，对指定的 URL 请求对象执行 HTTP 请求，上传提供的数据，并在完成后调用一个处理程序。
- [- uploadTaskWithRequest:fromFile:](<urlsession/uploadtask(with_fromfile_).md>) — 创建一个任务，执行用于上传指定文件的 HTTP 请求。
- [- uploadTaskWithRequest:fromFile:completionHandler:](<urlsession/uploadtask(with_fromfile_completionhandler_).md>) — 创建一个任务，执行用于上传指定文件的 HTTP 请求，然后在完成后调用一个处理程序。
- [- uploadTaskWithStreamedRequest:](<urlsession/uploadtask(withstreamedrequest_).md>) — 创建一个任务，根据指定的 URL 请求执行用于上传数据的 HTTP 请求。
- [- uploadTaskWithResumeData:](<urlsession/uploadtask(withresumedata_).md>) — 从一个恢复数据 blob 创建一个上传任务。要求服务器支持 HTTP 工作组最新的可恢复上传 Internet-Draft，该草案可在 https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload/ 找到。如果是从上传文件恢复，该文件必须仍然存在且未被修改。如果上传无法成功恢复，将调用 URLSession:task:didCompleteWithError:。
- [- uploadTaskWithResumeData:completionHandler:](<urlsession/uploadtask(withresumedata_completionhandler_).md>) — 从一个恢复数据 blob 创建一个 URLSessionUploadTask。如果是从上传文件恢复，该文件必须仍然存在且未被修改。
- [URLSessionUploadTask](urlsessionuploadtask.md) — 一个 URL 会话任务，在请求正文中将数据上传到网络。
- [URLSessionDataDelegate](urlsessiondatadelegate.md) — 定义 URL 会话实例在其委托上调用以处理特定于数据任务和上传任务的任务级别事件的方法的协议。

### 向会话添加流任务

- [- streamTaskWithHostName:port:](<urlsession/streamtask(withhostname_port_).md>) — 创建一个任务，与指定的主机名和端口建立双向 TCP/IP 连接。
- [- streamTaskWithNetService:](<urlsession/streamtask(with_).md>) — 创建一个任务，使用指定的网络服务建立双向 TCP/IP 连接。 _(已废弃)_
- [URLSessionStreamTask](urlsessionstreamtask.md) — 一个基于流的 URL 会话任务。
- [URLSessionStreamDelegate](urlsessionstreamdelegate.md) — 定义 URL 会话实例在其委托上调用以处理特定于流任务的任务级别事件的方法的协议。

### 向会话添加 WebSocket 任务

- [- webSocketTaskWithURL:](<urlsession/websockettask(with_)-87ipz.md>) — 为提供的 URL 创建一个 WebSocket 任务。
- [- webSocketTaskWithRequest:](<urlsession/websockettask(with_)-mtks.md>) — 为提供的 URL 请求创建一个 WebSocket 任务。
- [- webSocketTaskWithURL:protocols:](<urlsession/websockettask(with_protocols_).md>) — 给定一个 URL 和一个协议数组，创建一个 WebSocket 任务。
- [URLSessionWebSocketTask](urlsessionwebsockettask.md) — 一个通过 WebSockets 协议标准进行通信的 URL 会话任务。
- [URLSessionWebSocketDelegate](urlsessionwebsocketdelegate.md) — 定义 URL 会话实例在其委托上调用以处理特定于 WebSocket 任务的任务级别事件的方法的协议。

### 管理会话

- [- finishTasksAndInvalidate](<urlsession/finishtasksandinvalidate().md>) — 使会话失效（invalidate），允许任何未完成的任务完成。
- [- flushWithCompletionHandler:](<urlsession/flush(completionhandler_).md>) — 将 Cookie 和凭据刷新到磁盘，清除临时缓存，并确保后续请求发生在新 TCP 连接上。
- [- getTasksWithCompletionHandler:](<urlsession/gettaskswithcompletionhandler(__).md>) — 异步调用一个完成回调，其中包含会话中的所有数据、上传和下载任务。
- [- getAllTasksWithCompletionHandler:](<urlsession/getalltasks(completionhandler_).md>) — 异步调用一个完成回调，其中包含会话中的所有任务。
- [- invalidateAndCancel](<urlsession/invalidateandcancel().md>) — 取消所有未完成的任务，然后使会话失效（invalidate）。
- [- resetWithCompletionHandler:](<urlsession/reset(completionhandler_).md>) — 清空所有 Cookie、缓存和凭据存储，删除磁盘文件，将进行中的下载刷新到磁盘，并确保未来请求发生在新套接字上。
- [sessionDescription](urlsession/sessiondescription.md) — 一个 App 定义的会话描述标签。

### 处理错误

- [URL 会话错误字典键](url-session-error-dictionary-keys.md) — 与 URL 会话和任务返回的错误对象一起使用的键。
- [后台任务取消](background-task-cancellation.md) — 指示后台任务被取消原因的常量。

### 作为 Combine Publisher 执行任务

- [使用 Combine 处理 URL 会话数据任务结果](processing-url-session-data-task-results-with-combine.md) — 使用异步操作符链接收和处理从 URL 获取的数据。
- [dataTaskPublisher(for:)](<urlsession/datataskpublisher(for_)-61v3e.md>) — 返回一个发布者，它包装了给定 URL 请求的 URL 会话数据任务。
- [dataTaskPublisher(for:)](<urlsession/datataskpublisher(for_)-5kiir.md>) — 返回一个发布者，它包装了给定 URL 的 URL 会话数据任务。
- [DataTaskPublisher](urlsession/datataskpublisher.md) — 一个发布者，传递执行 URL 会话数据任务的结果。

### 已废弃

- [+ new](<urlsession/new().md>) _(已废弃)_
- [- init](<urlsession/init().md>) _(已废弃)_

## 另请参阅

### 基础

- [将网站数据获取到内存中](fetching-website-data-into-memory.md) — 通过从 URL 会话创建数据任务，直接将数据接收到内存中。
- [使用 Instruments 分析 HTTP 流量](analyzing-http-traffic-with-instruments.md) — 测量基于 HTTP 的网络性能和你 App 的使用情况。
- [URLSessionTask](urlsessiontask.md) — 在 URL 会话中执行的任务，例如下载特定资源。
