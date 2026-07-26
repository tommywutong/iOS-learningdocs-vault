---
title: URL-loading-system
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/url-loading-system/'
original_language: zh
published: 2019-11-30
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4392c47ab63ffe01'
translated: n/a
---

> 原文：[URL-loading-system](https://dirtmelon.github.io/posts/url-loading-system/)　·　dirtmelon

原文：[URL Loading System

Apple Developer Documentation](https://developer.apple.com/documentation/foundation/url_loading_system)

通过标准的互联网协议来与 URL 交流和与服务器通讯。

## 概览

URL Loading System 可以获取通过 URL 来辨别的资源，使用如 https 的标准协议或者一些你创造的自定义协议。加载是异步执行的，所以你的应用可以继续响应操作和在返回数据或者错误时进行处理。 你可以使用 [URLSession](https://developer.apple.com/documentation/foundation/urlsession) 对象来创建一个或者多个 [URLSessionTask](https://developer.apple.com/documentation/foundation/urlsessiontask) 对象，`URLSessionTask` 可以抓取和返回数据，下载文件，或者上传数据和文件到服务器。你可以使用 [URLSessionConfiguration](https://developer.apple.com/documentation/foundation/urlsessionconfiguration) 来配置会话（session），它可以控制像如何使用缓存和 cookies ，是否允许在蜂窝网络下进行连接等行为。

你可以使用一个会话来重复创建任务（tasks）。举个例子，一个浏览器可以有不同的会话提供给标准模式和隐私模式使用，隐私模式的会话不缓存数据。下图表示了两个会话如何通过 configuration 来创建多个任务。

![6789dd96-afdc-4c18-b8eb-01f9012dc04d](https://raw.githubusercontent.com/dirtmelon/blog-images/main/6789dd96-afdc-4c18-b8eb-01f9012dc04d.png)

每个会话都与一个 delegate 相关联，通过 delegate 来接收时而出现的更新（或者错误）。默认的 delegate 会调用你提供的 completion handler block，如果你选择提供自定义的 delegate，那么 block 就不会执行。

你可以配置一个会话在后台运行，所以当你的 app 退到后台时，系统可以下载数据并唤醒 app 来接收数据。

## 获取网络数据到内存中

URL session 通过创建一个数据任务来获取数据到内存中。

### 概览

当与服务器进行一些较轻量的连接时，你可以使用 [URLSessionDataTask](https://developer.apple.com/documentation/foundation/urlsessiondatatask) 来获取数据到内存中（[URLSessionDownloadTask](https://developer.apple.com/documentation/foundation/urlsessiondownloadtask) 则是用来存取数据到文件系统中）。`URLSessionDataTask` 非常适用于调用 Web 服务。

你可以使用一个 `URLSession` 对象来创建一个 任务 。如果你的需求很简单，你可以使用 [shared](https://developer.apple.com/documentation/foundation/urlsession/1409000-shared) 对象。如果你想通过 delegate 回调和传输进行交互，那么你需要创建一个 `URLSession` 对象，而不是使用 `shared` 对象。当创建 `URLSession` 时，你可以使用 [URLSessionConfiguration](https://developer.apple.com/documentation/foundation/urlsessionconfiguration) 对象来进行配置，同时也可以给 `URLSession` 设置遵循了 [URLSessionDelegate](https://developer.apple.com/documentation/foundation/urlsessiondelegate) 协议或者它的子协议的类作为 delegate 。可以重复使用 `URLSession` 来创建多个 任务 ，因此对于所需的每个唯一配置，请创建一个 `URLSession` ，并将其存储为属性。

> 注意 不要创建多余的 `URLSession` 。举个例子，如果你的 app 不同的部分需要一个相似配置的 `URLSession` ，创建一个 `URLSession` 并进行共享。

当你已有一个 `URLSession` ，你可以通过一个 `dataTask()` 方法来创建一个数据任务。 任务被创建时是处于被挂起状态，可以通过调用 [resume()](https://developer.apple.com/documentation/foundation/urlsessiontask/1411121-resume) 来启动任务。

### 通过 Completion Handler 来接收结果

获取数据最简单的方法是创建一个使用 completion handler 的数据任务。通过这种安排，任务将服务器的响应，数据以及可能的错误传递到你提供的 completion handler。下图显示了会话和任务之间的关系，以及如何将结果传递到 completion handler。

![bf4501ff-82b2-4dd4-9ec3-243ef0e70d21](https://raw.githubusercontent.com/dirtmelon/blog-images/main/bf4501ff-82b2-4dd4-9ec3-243ef0e70d21.png)

通过调用 `URLSession` 的 [dataTask(with:)](https://developer.apple.com/documentation/foundation/urlsession/1411554-datatask) 方法可以创建一个使用 completion handler 的数据任务。你的 completion handler 需要处理以下3件事：

1. 验证错误参数是否为空。如果不是，则说明发生了传输错误，处理错误并退出。
2. 检查响应参数以验证状态码是否为成功的状态码，且MIME类型是期望值。如果不是，处理服务器错误并退出。
3. 根据需要使用数据对象

以下代码展示了如何使用 `startLoad()` 方法来获取一个 URL 的内容。首先使用`URLSession` 的 `shared` 对象创建一个数据任务，将其结果传递给 completion handler 。在检查本地和服务器错误后，将数据转换为字符串，并使用 `WKWebView` 来进行加载。当然，你的应用程序可能还有其他用途来获取数据，例如将其解析为数据模型。

```swift
func startLoad() {
    let url = URL(string: "https://www.example.com/")!
    let task = URLSession.shared.dataTask(with: url) { data, response, error in
        if let error = error {
            self.handleClientError(error)
            return
        }
        guard let httpResponse = response as? HTTPURLResponse,
            (200...299).contains(httpResponse.statusCode) else {
            self.handleServerError(response)
            return
        }
        if let mimeType = httpResponse.mimeType, mimeType == "text/html",
            let data = data,
            let string = String(data: data, encoding: .utf8) {
            DispatchQueue.main.async {
                self.webView.loadHTMLString(string, baseURL: url)
            }
        }
    }
    task.resume()
}
```

> 重要 completion handler 是在不同的 GCD 队列中调用。因此如果需要更新 UI ，则需要明确地指出是在主队列中调用。

### 通过 delegate 来接收详细信息和结果

为了在执行任务活动时获得更高级别的访问权限，在创建数据任务时，您可以在会话上设置 delegate ，而不是提供 completion handler 。下图展示了这种做法。

![730c8e1b-654f-4eb9-9c63-d439a69ac5d2](https://raw.githubusercontent.com/dirtmelon/blog-images/main/730c8e1b-654f-4eb9-9c63-d439a69ac5d2.png)

通过这种方法，部分数据在到达时会调用 [URLSessionDataDelegate](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate) 的[urlSession(_:dataTask:didReceive:)](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/1411528-urlsession) 方法，直到传输完成或出现错误。随着任务的进行，delegate 还接收其他类型的事件。

使用 delgate 模式时，您需要创建自己的 `URLSession` 对象，而不是使用 `URLSession` 的 `shared` 对象。创建一个新的会话允许你将自己的类设置为会话的 delegate ，如下面代码所示。

```swift
private lazy var session: URLSession = {
    let configuration = URLSessionConfiguration.default
    configuration.waitsForConnectivity = true
    return URLSession(configuration: configuration,
                      delegate: self, delegateQueue: nil)
}()
```

声明你的类实现了一个或多个委托协议（[URLSessionDelegate](https://developer.apple.com/documentation/foundation/urlsessiondelegate) ，[URLSessionTaskDelegate](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate) ，[URLSessionDataDelegate](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate) 和[URLSessionDownloadDelegate](https://developer.apple.com/documentation/foundation/urlsessiondownloaddelegate) ）。然后通过 [init(configuration:delegate:delegateQueue:)](https://developer.apple.com/documentation/foundation/urlsession/1411597-init) 创建 URL 会话对象。你可以定制对应的配置对象。例如，将 `waitsForConnectivity` 设置为 `true` 是个好想法。这样，会话将等待适当的连接，而不是在所需的连接不可用时立即失败。

下面代码展示了 `startLoad()` 方法是如何使用会话来启动数据任务，和使用 delegate 的回调方法来处理接收到的数据和错误。下面代码实现了三个 delegate 的回调方法：

- [urlSession(_:dataTask:didReceive:completionHandler:)](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/1410027-urlsession) 验证响应是否具有成功的 HTTP 状态代码，且 MIME 类型为 text/html 或 text/plain。如果这两种情况都不是，则取消任务，否则可以继续进行任务。
- [urlSession(_:dataTask:didReceive:)](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/1411528-urlsession) 处理任务接收到的每个数据对象，并将其添加 `receivedData` 的缓冲区中。
- [urlSession(_:task:didCompleteWithError:)](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/1411610-urlsession) 首先查看是否发生了传输级的错误。如果没有错误，就尝试将 `receivedData` 缓冲区转换为字符串并设置为 webView 的内容。

```swift
var receivedData: Data?

func startLoad() {
    loadButton.isEnabled = false
    let url = URL(string: "https://www.example.com/")!
    receivedData = Data()
    let task = session.dataTask(with: url)
    task.resume()
}

// delegate methods

func urlSession(_ session: URLSession, dataTask: URLSessionDataTask, didReceive response: URLResponse,
                completionHandler: @escaping (URLSession.ResponseDisposition) -> Void) {
    guard let response = response as? HTTPURLResponse,
        (200...299).contains(response.statusCode),
        let mimeType = response.mimeType,
        mimeType == "text/html" else {
        completionHandler(.cancel)
        return
    }
    completionHandler(.allow)
}

func urlSession(_ session: URLSession, dataTask: URLSessionDataTask, didReceive data: Data) {
    self.receivedData?.append(data)
}

func urlSession(_ session: URLSession, task: URLSessionTask, didCompleteWithError error: Error?) {
    DispatchQueue.main.async {
        self.loadButton.isEnabled = true
        if let error = error {
            handleClientError(error)
        } else if let receivedData = self.receivedData,
            let string = String(data: receivedData, encoding: .utf8) {
            self.webView.loadHTMLString(string, baseURL: task.currentRequest?.url)
        }
    }
}
```

各种 delegate 提供的方法除了上述代码中所示的方法之外，还用于处理身份验证挑战，重定向和其他特殊情况。在 `URLSession` 讨论中，使用 URL 会话描述了在传输过程中可能发生的各种回调。

## NSURLSession

负责协调组织一组相关的网络数据传输任务

`NSURLSession` 类和相关类提供了一个 API ，用于从 URL 指示的链接下载数据或将数据上传 。该 API 还可以使你的应用在后台或处于暂停状态时执行后台下载。丰富的 delegate 方法支持身份验证，并允许你的应用收到有关重定向等事件的通知。

### 会话类型

拥有相同会话的任务会分享一个共同的会话配置，配置定义了连接的行为，如最大连接数，是否允许使用蜂窝网络等。

`NSURLSession` 有用于基本请求的单例 `sharedSession` （没有配置对象）。它不像你创建的会话那样可进行自定义，如果你的要求不多，可以尝试下使用它。也可以通过下面三种配置来进行初始化：

1. default session ： 跟 `sharedSession` 非常相似，但是允许你设置更多配置，并且可以通过 delegate 来增量获取数据。
2. ephemeral session ：临时会话，跟 `sharedSession` 的不同之处在于它不会将缓存，cookie或者认证凭证存储到硬盘中。
3. Background session ：允许你在后台执行上传或者下载任务

### 任务类型

在会话中，你创建的任务可以有选择地将数据上传到服务器，然后可以选择将接收到的数据转为文件存放到硬盘中还是转为 `NSData` 对象存放到内存中。 `NSURLSession` API 提供三种类型的任务：

1. data task ：使用 `NSData` 对象来接收和发送数据。通常用于执行一些数据较小的，可与服务器进行交互的请求
2. upload task ：跟 data task 类似，但是通常用于上传文件形式的数据，支持后台上传
3. Download task ：以文件形式下载数据，支持后台下载

### 使用会话 delegate

会话的任务会共享 delegate ，delegate 允许你在各种事件发生时（如认证失败，接收到来自服务的数据，数据准备好缓存等）进行处理和获取信息。如果你不需要设置 delegate ，可以在创建会话时传递 nil 参数。

> 重要 会话对象会强引用 delegate ，直到你的 app 退出或者显式终止会话。所以如果你不显式中止会话，那么就会有内存泄露。

### 会话和异步

跟大多数网络 API 一样， `NSURLSession`也是高度异步的。它可以通过以下两种方式返回数据：

- 通过在传输成功完成或出现错误时调用 completion handler。
- 在接收数据和传输完成时调用会话 delegate 的方法。

同时 `NSURLSession` API 还提供了状态和进度属性，你可以根据任务当前的状态来进行决策（状态随时有可能改变）。

`NSURLSession` 同时还是支持取消，重启，恢复和挂起任务，并提供从被中断处恢复已被挂起，取消或者下载失败的任务。

### 支持的协议

`NSURLSession` 支持 data ， file ， ftp ， http ， 和 https 协议，并可以根据用户的系统偏好设置支持代理服务器和 socks 网关。

NSURLSession支持 HTTP/1.1 和 HTTP/2 协议。如 [RFC 7540](https://tools.ietf.org/html/rfc7540) 所述，HTTP/2 支持需要服务器支持应用程序层协议协商（ALPN）。

还可以通过将 NSURLProtocol 子类化，添加对自己的自定义网络协议和 URL 方案的支持（应用私有）。

### App Transport Security (ATS)

从 iOS 9.0 和 OS X 10.11 开始，默认情况下为使用 `NSURLSession` 建立的 HTTP 连接都启用 HTTPS ([RFC 2818](https://tools.ietf.org/html/rfc2818))。 更多信息可以查看 [Information Property List Key Reference](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009247) 的 [NSAppTransportSecurity](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33)

### NSCopying 相关行为

会话和任务对象都遵循 [NSCopying](https://developer.apple.com/documentation/foundation/nscopying?language=objc) 协议：

- 当你复制一个会话或者任务对象时，你得到的是相同的对象
- 当你复制一个配置对象时，你得到的是一个新的可以独立修改的对象

### 线程安全

URLSession 的 API 都是线程安全的，你可以在不同的线程中创建会话和任务。当你的 delegate 调用对应的方法时，任务会自动安排在正确的 delegate 队列上。

## NSURLRequest

`NSURLRequest` 封装了加载请求的两个必要属性：加载所需要的 URL 和加载策略。同时，URLRequest 还包括 HTTP 方法（GET ， POST 等）和 HTTP 头。最后，可以通过自定义属性来实现自定义协议。

### 预留的 HTTP 头部属性

URL Loading System 会为你处理 HTTP 协议各个方面的配置（HTTP 1.1 持久连接，代理，身份验证等）。作为这个支持的一部分，URL Loading System 会预留以下 HTTP 头部属性：

- Content-Length
- Authorization
- Connection
- Host
- Proxy-Authenticate
- Proxy-Authorization
- WWW-Authenticate

如果你设置了其中一个的属性，系统可以会忽略掉你设置的值，或者重写它，或者只是不进行发送。此外，确切的行为可能会随着时间而改变。为避免此类问题，请勿直接设置这些头部属性。

URL Loading System 会根据请求正文是否具有已知长度来判断是否需要设置 `Content-Length` ：

- 如果已经知道长度，它就会使用身份传输编码并将 `Content-Length` 设置为已知长度。你可以在设置请求正文为 data 对象时看到这种效果
- 如果不知道长度，则使用分块传输编码，并省略 `Content-Length` 。将请求正文设置为流时会看到这种效果。

## 上传数据到网站

很多 app 都与服务器一起工作并支持上传图片或者文档或者上传一些结构化的数据如 JSON 。你可以使用 [NSURLSession](https://developer.apple.com/documentation/foundation/nsurlsession?language=objc) 对象来创建 [NSURLSessionUploadTask](https://developer.apple.com/documentation/foundation/nsurlsessionuploadtask?language=objc) 对象。上传任务会使用 [URLRequest](https://developer.apple.com/documentation/foundation/urlrequest?language=objc) 来展示如何执行上传任务。

### 准备好需要上传的数据

上传的数据可以是文件的一部分，流，data 。

很多 Web 服务都支持 JSON 格式的数据，你可以使用 [JSONEncoder](https://developer.apple.com/documentation/foundation/jsonencoder?language=objc) 来 [Encodable](https://developer.apple.com/documentation/swift/encodable?language=objc) 如数组，字典类型。如下面代码所示，你可以声明一个遵循 [Codable](https://developer.apple.com/documentation/swift/codable?language=objc) 协议的结构体，创建一个对象，然后使用 `JSONEncoder` 来将其编码成 JSON 数据。

```swift
struct Order: Codable {
    let customerId: String
    let items: [String]
}

// ...

let order = Order(customerId: "12345",
                  items: ["Cheese pizza", "Diet soda"])
guard let uploadData = try? JSONEncoder().encode(order) else {
    return
}
```

还有其他很多方式来创建数据对象，如将图片编码成 JPEG 或者 PNG 数据，或者将字符串编码成 UTF-8 数据。

### 配置上传请求

上传任务需要一个 `URLRequest` 对象，需要根据服务器的支持和要求将设置 [httpMethod](https://developer.apple.com/documentation/foundation/urlrequest/2011415-httpmethod?language=objc) 为 `POST` 或 `PUT` 。使用 [setValue(_:forHTTPHeaderField:)](https://developer.apple.com/documentation/foundation/urlrequest/2011447-setvalue?language=objc) 方法可以设置 HTTP 头部任何属性，除了 `Content-Length` 。会话会根据你的数据大小自动计算出 `Content-Length` 。

```swift
let url = URL(string: "https://example.com/post")!
var request = URLRequest(url: url)
request.httpMethod = "POST"
request.setValue("application/json", forHTTPHeaderField: "Content-Type")
```

### 创建和启动上传任务

结合配置好的数据和请求，调用会话的 [uploadTaskWithRequest:fromData:completionHandler:](https://developer.apple.com/documentation/foundation/nsurlsession/1411518-uploadtaskwithrequest?language=objc) 方法来创建上传任务对象 [NSURLSessionTask](https://developer.apple.com/documentation/foundation/nsurlsessiontask?language=objc) 。任务开始时是挂起状态，所以需要调用 [resume](https://developer.apple.com/documentation/foundation/nsurlsessiontask/1411121-resume?language=objc) 方法来启动任务。

```swift
let task = URLSession.shared.uploadTask(with: request, from: uploadData) { data, response, error in
    if let error = error {
        print ("error: \(error)")
        return
    }
    guard let response = response as? HTTPURLResponse,
        (200...299).contains(response.statusCode) else {
        print ("server error")
        return
    }
    if let mimeType = response.mimeType,
        mimeType == "application/json",
        let data = data,
        let dataString = String(data: data, encoding: .utf8) {
        print ("got data: \(dataString)")
    }
}
task.resume()
```

### 替代方案：设置 delegate

可以通过给会话设置 delegate ，然后接入 `NSURLSessionDelegate` 和 `NSURLSessionTaskDelegate` 协议的方法来处理服务器返回的数据或者传输错误。

## 上传流数据

流媒体和长期运行的 app 使用持续流来上传数据，而不是发送单个数据或者文件。你可以配置一个 [NSURLSessionUploadTask](https://developer.apple.com/documentation/foundation/nsurlsessionuploadtask?language=objc) 对象（ [NSURLSessionTask](https://developer.apple.com/documentation/foundation/nsurlsessiontask?language=objc) 子类）来与你提供的流进行工作，然后不定地填充流。

任务通过会话的 delegate 来获取流，所以你需要创建会话和设置会话的 delegate 。

### 创建会话

创建会话时设置 delegate 和配置。

```swift
lazy var session: URLSession = URLSession(configuration: .default,
                                          delegate: self,
                                          delegateQueue: .main)
```

### 创建流上传任务

调用 [NSURLSession](https://developer.apple.com/documentation/foundation/nsurlsession?language=objc) 的 [uploadTaskWithStreamedRequest:](https://developer.apple.com/documentation/foundation/nsurlsession/1410934-uploadtaskwithstreamedrequest?language=objc) 来创建流上传任务。

```swift
let url = URL(string: "http://127.0.0.1:12345")!
var request = URLRequest(url: url,
                         cachePolicy: .reloadIgnoringLocalCacheData,
                         timeoutInterval: 10)
request.httpMethod = "POST"
let uploadTask = session.uploadTask(withStreamedRequest: request)
uploadTask.resume()
```

### 使用流的绑定对来提供输入流

你可以使用 [NSInputStream](https://developer.apple.com/documentation/foundation/nsinputstream?language=objc) 来提供上传任务所需要的流数据。任务读取来自这个流的数据和上传到服务器。

一个提供数据给输入流的方式是使用流的绑定对。绑定对包含了 [NSOutputStream](https://developer.apple.com/documentation/foundation/nsoutputstream?language=objc) ，你可以输入数据到 `NSOutputStream` 中。由于绑定对的关系，你输入到 `NSOutputStream` 的数据可以在 `NSInputStream` 中获取。

![a29fb2be-5f7f-4c56-9ef6-4090ecfbae82](https://raw.githubusercontent.com/dirtmelon/blog-images/main/a29fb2be-5f7f-4c56-9ef6-4090ecfbae82.png)

下面代码展示了一个持有 `NSIntputStream` 和 `NSOutputStream` 的结构体 `Streams` ，使用 [getBoundStreamsWithBufferSize:inputStream:outputStream:](https://developer.apple.com/documentation/foundation/nsstream/1412683-getboundstreamswithbuffersize?language=objc) 方法来配置 `NSInputStream` 和 `NSOutputStream` 。

```swift
struct Streams {
    let input: InputStream
    let output: OutputStream
}
lazy var boundStreams: Streams = {
    var inputOrNil: InputStream? = nil
    var outputOrNil: OutputStream? = nil
    Stream.getBoundStreams(withBufferSize: 4096,
                           inputStream: &inputOrNil,
                           outputStream: &outputOrNil)
    guard let input = inputOrNil, let output = outputOrNil else {
        fatalError("On return of `getBoundStreams`, both `inputStream` and `outputStream` will contain non-nil streams.")
    }
    // configure and open output stream
    output.delegate = self
    output.schedule(in: .current, forMode: .default)
    output.open()
    return Streams(input: input, output: output)
}()
```

在创建绑定对时，确保在从输入流读取数据之前，需要指定足够大的缓存区大小，以容纳所有要写入输出流的数据。 设置 `NSOutputStream` 对应的 delegate，可以指示接收输出流何时可以接收新数据。

### 提供流给上传任务

通过 `NSURLSessionTaskDelegate` 的 `urlSession:task:needNewBodyStream:` 方法可以提供流给上传任务：

```swift
func urlSession(_ session: URLSession, task: URLSessionTask,
                needNewBodyStream completionHandler: @escaping (InputStream?) -> Void) {
    completionHandler(boundStreams.input)
}
```

### 当流准备好时写入数据

当输出流准备好时写入数据到其中。当流准备就绪时，会调用 `NSStreamDelegate` 的方法 [stream:handleEvent:](https://developer.apple.com/documentation/foundation/nsstreamdelegate/1410079-stream?language=objc) ，当 `eventCode` 参数包含 [NSStreamEventHasSpaceAvailable](https://developer.apple.com/documentation/foundation/nsstreamevent/nsstreameventhasspaceavailable?language=objc) 时，表示流准备好接收更多数据。

如果你未准备好写入数据，或者想在自己的周期内写入数据。可以自定义标志来判断是否写入到流中。 当时处理流时，还需要坚持 `eventCode` 参数是否包含 [NSStreamEventErrorOccurred](https://developer.apple.com/documentation/foundation/nsstreamevent/nsstreameventerroroccurred?language=objc) ，这意味着流任务失败，需要关闭流和禁止上传。

```swift
func stream(_ aStream: Stream, handle eventCode: Stream.Event) {
    guard aStream == boundStreams.output else {
        return
    }
    if eventCode.contains(.hasSpaceAvailable) {
        canWrite = true
    }
    if eventCode.contains(.errorOccurred) {
        // Close the streams and alert the user that the upload failed.
    }
}
```

当你处理 [NSStreamEventHasSpaceAvailable](https://developer.apple.com/documentation/foundation/nsstreamevent/nsstreameventhasspaceavailable?language=objc) 事件时，你可以在已经准备好接收更多数据时写入数据到流中。你可以通过调用 [write:maxLength:](https://developer.apple.com/documentation/foundation/nsoutputstream/1410720-write?language=objc) 方法来写入数据，需要提供原始数据的引用和可以写入的最大字节数。 下面代码使用了一个计时器来等待 `canWrite` 属性为 `true` 。如果 `canWrite` 为 `true` 那么就可以创建一个记录当前日期的字符串，并将其转化成原始字节。然后调用 [write:maxLength:](https://developer.apple.com/documentation/foundation/nsoutputstream/1410720-write?language=objc) 方法写入到输出流中。因为输出流已经跟输入流绑定，所以上传任务会自动读取这些字节并发送到目标 URL 中。

```swift
timer = Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) {
    [weak self] timer in
    guard let self = self else { return }

    if self.canWrite {
        let message = "*** \(Date())\r\n"
        guard let messageData = message.data(using: .utf8) else { return }
        let messageCount = messageData.count
        let bytesWritten: Int = messageData.withUnsafeBytes() { (buffer: UnsafePointer<UInt8>) in
            self.canWrite = false
            return self.boundStreams.output.write(buffer, maxLength: messageCount)
        }
        if bytesWritten < messageCount {
            // Handle writing less data than expected.
        }
    }
}
```

> 提示 如果你的数据来自于一个异步处理的流程，例如一个媒体设备的回调，你还是需要等待输出流准备才可以进行写入。在这种情况下，你可以使用一个缓存区来存取你的数据。

## 下载来自网站的文件

一些以文件形式存储的网络资源，例如图片，文档，你可以使用下载任务来下载它们到本地的文件系统中。

### 使用 Completion Handler 来创建简单的下载任务

你可以使用 [NSURLSession](https://developer.apple.com/documentation/foundation/nsurlsession?language=objc) 创建 [NSURLSessionDownloadTask](https://developer.apple.com/documentation/foundation/nsurlsessiondownloadtask?language=objc) 来下载文件。如果你在下载时不在乎下载进度或者其它 delegate 回调，你可以使用 completion handler 。不管是完成下载还是发生错误，下载完成时都会调用 completion handler 。

Completion handler 有可能接收到错误，如无法连接网络。如果没有错误，你有可能接收到 [NSURLResponse](https://developer.apple.com/documentation/foundation/nsurlresponse?language=objc) ，你需要检查它来确认接收到的是一个成功的来自服务器的响应。

如果成功下载，你会接收到一个指示出已下载文件在本地文件系统位置的 URL 。它是临时的，如果你需要永久保存它，在 completion handler 返回前你需要复制或者移动它到其它位置。

下面代码展示了如何使用通过 completion handler 来创建下载任务，以及如何验证错误，保存结果。

```swift
let downloadTask = URLSession.shared.downloadTask(with: url) {
    urlOrNil, responseOrNil, errorOrNil in
    // check for and handle errors:
    // * errorOrNil should be nil
    // * responseOrNil should be an HTTPURLResponse with statusCode in 200..<299

    guard let fileURL = urlOrNil else { return }
    do {
        let documentsURL = try
            FileManager.default.url(for: .documentDirectory,
                                    in: .userDomainMask,
                                    appropriateFor: nil,
                                    create: false)
        let savedURL = documentsURL.appendingPathComponent(
            fileUrl.lastPathComponent)
        try FileManager.default.moveItem(at: fileUrl, to: savedURL)
    } catch {
        print ("file error: \(error)")
    }
}
downloadTask.resume()
```

### 使用 delegate 来接收进度更新

使用 delegate 可以接收下载进度更新，你可以接入 [NSURLSessionTaskDelegate](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate?language=objc) 和 [NSURLSessionDownloadDelegate](https://developer.apple.com/documentation/foundation/nsurlsessiondownloaddelegate?language=objc) 协议的方法。

```swift
private lazy var urlSession = URLSession(configuration: .default,
                                         delegate: self,
                                         delegateQueue: nil)
private func startDownload(url: URL) {
    let downloadTask = urlSession.downloadTask(with: url)
    downloadTask.resume()
    self.downloadTask = downloadTask
}
```

### 接收进度更新

当下载开始执行后，你可以通过 [URLSession:downloadTask:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:](https://developer.apple.com/documentation/foundation/nsurlsessiondownloaddelegate/1409408-urlsession?language=objc) 定期接收到进度更新。你可以通过字节计数来更新 app 中的进度 UI 。

下面代码展示了如何计算下载进度，因为回调是在不确定的 GCD 队列中执行的，所以你需要明确指定在主队列中执行 UI 更新。

```swift
func urlSession(_ session: URLSession,
                downloadTask: URLSessionDownloadTask,
                didWriteData bytesWritten: Int64,
                totalBytesWritten: Int64,
                totalBytesExpectedToWrite: Int64) {
     if downloadTask == self.downloadTask {
        let calculatedProgress = Float(totalBytesWritten) / Float(totalBytesExpectedToWrite)
        DispatchQueue.main.async {
            self.progressLabel.text = self.percentFormatter.string(from:
                NSNumber(value: calculatedProgress))
    }
}
```

> 提示 如果你只是使用 [UIProgressView](https://developer.apple.com/documentation/uikit/uiprogressview?language=objc) 来更新进度 UI ，那么你可以将任务的 [progress](https://developer.apple.com/documentation/foundation/nsurlsessiontask/2908821-progress?language=objc) 属性设置给 `UIProgressView` 的 [observedProgress](https://developer.apple.com/documentation/uikit/uiprogressview/1619840-observedprogress?language=objc) 属性即可，不需要自己计算进度。

### 在 delegate中处理下载错误

在 [URLSession:downloadTask:didFinishDownloadingToURL:](https://developer.apple.com/documentation/foundation/nsurlsessiondownloaddelegate/1411575-urlsession?language=objc) 方法中需要进行判断文件是否存在，响应码是否正确，和对文件进行移动。

```swift
func urlSession(_ session: URLSession,
                downloadTask: URLSessionDownloadTask,
                didFinishDownloadingTo location: URL) {
    // check for and handle errors:
    // * downloadTask.response should be an HTTPURLResponse with statusCode in 200..<299

    do {
        let documentsURL = try
            FileManager.default.url(for: .documentDirectory,
                                    in: .userDomainMask,
                                    appropriateFor: nil,
                                    create: false)
        let savedURL = documentsURL.appendingPathComponent(
            location.lastPathComponent)
        try FileManager.default.moveItem(at: location, to: savedURL)
    } catch {
        // handle filesystem error
    }
}
```

如果有错误产生，就会调用 delegate 的 [URLSession:task:didCompleteWithError:](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1411610-urlsession?language=objc) 方法。

## 暂停和重启下载

应用或者用户有时候可能需要取消正在进行的下载，然后再继续进行下载，通过支持断点续传下载，你可以节省用户的时间和流量。

同样可以借助这个技术来恢复因失去连接而被中断的下载任务。

### 取消下载时存储恢复时需要的数据

你可以通过调用 [NSURLSessionDownloadTask](https://developer.apple.com/documentation/foundation/nsurlsessiondownloadtask?language=objc) 的 [cancelByProducingResumeData:](https://developer.apple.com/documentation/foundation/nsurlsessiondownloadtask/1411634-cancelbyproducingresumedata?language=objc) 方法来取消任务，当完成取消时会调用 completion handler ，而 completion handler 会接收到一个 `resumeData` 参数。如果它不为空，它就是你恢复下载时所需要用的 token ，需要将它存储起来。

```swift
downloadTask.cancel { resumeDataOrNil in
    guard let resumeData = resumeDataOrNil else {
      // download can't be resumed; remove from UI if necessary
      return
    }
    self.resumeData = resumeData
}
```

只有以下几种形式的任务可以恢复：

- 从你第一次请求起，资源没有做任何改动
- 任务是 HTTP 或者 HTTPS 的 GET 请求
- 服务器提供 ETag 或者 Last-Modified 在响应头重
- 服务器支持指定字节范围的请求
- 临时文件未被系统删除

### 下载失败时存储恢复时需要的数据

你还可以恢复由于暂时失去网络连接而失败的下载任务，如用户离开 WiFi 范围。

当下载失败时，会话会调用 delegate 的 [URLSession:task:didCompleteWithError:](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1411610-urlsession?language=objc) 方法，如果 error 不为空，那么就检查 userInfo 中 [NSURLSessionDownloadTaskResumeData](https://developer.apple.com/documentation/foundation/nsurlsessiondownloadtaskresumedata?language=objc) 字段是否有数据，如果有，就把对应的数据存储起来，用于恢复下载任务，如果没有，则表示下载任务是不可恢复的。

```swift
func urlSession(_ session: URLSession, task: URLSessionTask, didCompleteWithError error: Error?) {
    guard let error = error else {
        // Handle success case.
        return
    }
    let userInfo = (error as NSError).userInfo
    if let resumeData = userInfo[NSURLSessionDownloadTaskResumeData] as? Data {
        self.resumeData = resumeData
    }
    // Perform any other error handling.
}
```

### 使用已保存的恢复用的数据来恢复下载任务

当需要恢复下载任务时，使用 [NSURLSession](https://developer.apple.com/documentation/foundation/nsurlsession?language=objc) 的 [downloadTaskWithResumeData:completionHandler:](https://developer.apple.com/documentation/foundation/nsurlsession/1411598-downloadtaskwithresumedata?language=objc) 或者 [downloadTaskWithResumeData:](https://developer.apple.com/documentation/foundation/nsurlsession/1409226-downloadtaskwithresumedata?language=objc) 方法来创建一个新的 `NSURLSessionDownloadTask` ，同时需要使用之前存储的 `resumeData` 作为初始化参数。

```swift
guard let resumeData = resumeData else {
    // inform the user the download can't be resumed
    return
}
let downloadTask = urlSession.downloadTask(withResumeData: resumeData)
downloadTask.resume()
self.downloadTask = downloadTask
```

如果下载任务成功恢复，任务会调用 delegate 的 [URLSession:downloadTask:didResumeAtOffset:expectedTotalBytes:](https://developer.apple.com/documentation/foundation/nsurlsessiondownloaddelegate/1408142-urlsession?language=objc) 方法。你可以使用 `offset` 和 `byte` 计数参数来通知用户下载已经恢复，而且有保存之前的进度。

## 在后台下载文件

在你的 app 不活跃时创建任务来下载文件。 对于那些需要较长时间和不紧急的传输任务，你可以使用 `background` 创建和运行。任务会在 app 被退到后台时运行，在 app 变为活跃时可以获取已下载的文件。

### 创建后台会话

为了执行后台下载，需要使用 `background` 操作来配置 [NSURLSession](https://developer.apple.com/documentation/foundation/nsurlsession?language=objc) 。

1. 通过 `NSURLSession` 的类方法 [backgroundSessionConfigurationWithIdentifier:](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1407496-backgroundsessionconfigurationwi?language=objc) 创建一个后台 [NSURLSessionConfiguration](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration?language=objc) 对象，会话 ID 在 app 里是唯一的。但是大多数 app 只需要很少的后台会话（通常只有一个），你可以把会话 ID 写死。
2. 为了在任务完成时让系统唤醒你的 app，需要设置 [sessionSendsLaunchEvents](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1617174-sessionsendslaunchevents?language=objc) 为 `true` 。
3. 对于一些不需要立即完成的任务，可以设置 [discretionary](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411552-discretionary?language=objc) 为 `true` ，这样系统可以等待到最佳状态来执行传输，如等到设备充电或者连接到 Wi-Fi 。
4. 使用 `NSURLSessionConfiguration` 对象来创建 `NSURLSession` 对象。

```swift
private lazy var urlSession: URLSession = {
    let config = URLSessionConfiguration.background(withIdentifier: "MySession")
    config.isDiscretionary = true
    config.sessionSendsLaunchEvents = true
    return URLSession(configuration: config, delegate: self, delegateQueue: nil)
}()
```

### 创建和调用下载任务

你可以通过 [downloadTaskWithURL:](https://developer.apple.com/documentation/foundation/nsurlsession/1411482-downloadtaskwithurl?language=objc) 或者 [downloadTaskWithRequest:](https://developer.apple.com/documentation/foundation/nsurlsession/1411481-downloadtaskwithrequest?language=objc) 方法来创建下载任务。

1. 使用 `downloadTaskWithURL:` 来创建下载任务。
2. 也可以通过设置 [earliestBeginDate](https://developer.apple.com/documentation/foundation/nsurlsessiontask/2873413-earliestbegindate?language=objc) 来在未来某个时间启动下载任务。设置了之后，下载任务并不是一定会在这个时间启动，只是不会早于这个时间。
3. 为了使得系统的网络调度更有效率，可以设置 [countOfBytesClientExpectsToSend](https://developer.apple.com/documentation/foundation/nsurlsessiontask/2873401-countofbytesclientexpectstosend?language=objc) 和 [countOfBytesClientExpectsToReceive](https://developer.apple.com/documentation/foundation/nsurlsessiontask/2873414-countofbytesclientexpectstorecei?language=objc) 属性。通过设置这些属性，可以设置请求的字节数的上限。
4. 调用 [resume](https://developer.apple.com/documentation/foundation/nsurlsessiontask/1411121-resume?language=objc) 来启动任务。

```swift
let backgroundTask = urlSession.downloadTask(with: url)
backgroundTask.earliestBeginDate = Date().addingTimeInterval(60 * 60)
backgroundTask.countOfBytesClientExpectsToSend = 200
backgroundTask.countOfBytesClientExpectsToReceive = 500 * 1024
backgroundTask.resume()
```

### 处理 App 被暂停的情况

App 不同的状态会影响 app 跟后台下载任务的交互。在 iOS ，app 有前台，挂起和被系统终止几种状态， [Managing Your App’s Life Cycle](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle?language=objc) 有更详细的介绍。 当 app 在后台，下载是在另外一个进程执行时，系统可能会挂起 app 。下载完成后，系统恢复 app ，然后调用 [UIApplicationDelegate](https://developer.apple.com/documentation/uikit/uiapplicationdelegate?language=objc) 的 [application:handleEventsForBackgroundURLSession:completionHandler:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622941-application?language=objc) 方法。 这个方法会传一个 completion handler 作为最后的参数。你需要把这个 handler 存储到 app 中。

```swift
func application(_ application: UIApplication,
                 handleEventsForBackgroundURLSession identifier: String,
                 completionHandler: @escaping () -> Void) {
        backgroundCompletionHandler = completionHandler
}
```

当所有项目都完成传送，系统会调用 [NSURLSessionDelegate](https://developer.apple.com/documentation/foundation/nsurlsessiondelegate?language=objc) 的 [URLSessionDidFinishEventsForBackgroundURLSession:](https://developer.apple.com/documentation/foundation/nsurlsessiondelegate/1617185-urlsessiondidfinisheventsforback?language=objc) 方法，在这个例子中，我们需要调用之前存储的 `backgroundCompletionHandler` 。 `URLSessionDidFinishEventsForBackgroundURLSession:` 有可能在子队列中调用，所以需要在主队列中调用：

```swift
func urlSessionDidFinishEvents(forBackgroundURLSession session: URLSession) {
    DispatchQueue.main.async {
        guard let appDelegate = UIApplication.shared.delegate as? AppDelegate,
            let backgroundCompletionHandler =
            appDelegate.backgroundCompletionHandler else {
                return
        }
        backgroundCompletionHandler()
    }
}
```

### 获取文件，或者移动到永久的地址

一旦你的 app 调用 completion handler ，下载任务就已经完成它的工作，然后调用 delegate 的 [URLSession:downloadTask:didFinishDownloadingToURL:](https://developer.apple.com/documentation/foundation/nsurlsessiondownloaddelegate/1411575-urlsession?language=objc) 方法。在这个例子中，文件是已经完全下载了，在你的 delegate 方法返回前都可以获取到。如果你只需要一次读取它，你可以直接通过临时地址直接获取文件。如果你想要保存文件，就需要把它移动到永久的地址。比如 Documents 目录，像 [Downloading Files from Websites](https://developer.apple.com/documentation/foundation/url_loading_system/downloading_files_from_websites?language=objc) 描述那样。

### App 被杀死后重新创建任务

如果系统在 app 被挂起时杀死 app ，系统会在后台重启 app 。作为你启动时步骤的一部分，使用相同的会话 ID 重新创建后台会话，这样使得系统可以通过你的任务来重新连接任务。不管 app 是通过用户还是系统登录都可以进行此操作。一旦 app 重新启动，这一系列的任务跟 app 被挂起然后恢复时一样，像之前讨论的处理 App 被暂停的情况类似。

### 遵守后台的传输限制

在后台会话中，实际的转移是通过与你 app 的流程不同的流程执行的。由于重新启动应用程序的流程相当昂贵，因此某些功能不可用，因此受到以下限制：

- 必须要提供 delegate 给会话来传递事件。
- 只支持 HTTP 和 HTTPS 协议（不支持自定义协议）。
- 始终遵循重定向。即使你引入 [URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1411626-urlsession?language=objc) 方法，也不会进行调用。
- 只支持文件的上传任务（data 对象的上传或者流会在 app 退出时失败）。

### 高效地使用后台会话

当系统恢复或者重新启动你的 app 时，它会使用速率限制器来防止滥用后台下载。当你的 app 在后台开启一个新的下载任务时，任务会等到延迟到期才开始。每当系统恢复或重新启动你的 app 时，延迟的时间都会增加。 因此，如果你的 app 开始一次后台下载任务，然后在下载完成时恢复 app ，启动一个新的下载任务，它会大大增加延迟时间。一个有效的替代方案时是使用一小部分的后台会话（最好是一个），然后使用这些会话来一次性启动多个下载任务。这样使得系统可以一次执行多个下载任务，且在下载完成后恢复 app 。 请记住每个任务都有它自己的开销。如果你发现你在启动时需要执行几千个下载任务，请考虑修改你的设计来执行次数更少，数据更大的传输。

> 当用户将你的 app 切换到前台时，延迟时间会被重置为 0 。如果延迟时间过去后系统仍没有恢复或者重启你的 app ，延迟时间也会被重置。

## 获取缓存数据

控制 URL 请求来如何使用缓存数据 URL Loading System 缓存响应的数据到内存和硬盘中，借此来提升性能和减少网络传输时间。 可以使用 [NSURLCache](https://developer.apple.com/documentation/foundation/nsurlcache?language=objc) 类来缓存网络响应的资源。你可以通过 `URLCache` 的 `sharedURLCache` 来获取缓存的单例，也可以创建自己需要的缓存，给你的 [NSURLSessionConfiguration](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration?language=objc) 对象设置特定的缓存。

### 设置 URL 请求的缓存策略

每个 [URLRequest](https://developer.apple.com/documentation/foundation/urlrequest?language=objc) 都包含一个 [URLRequest.CachePolicy](https://developer.apple.com/documentation/foundation/urlrequest/cachepolicy?language=objc) 来指示如何执行缓存。你可以通过改变这个策略来控制请求的缓存。 为了方便， [NSURLSessionConfiguration](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration?language=objc) 提供了一个 [requestCachePolicy](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1411655-requestcachepolicy?language=objc) 属性，所有通过这个配置发起的请求都会继承这个请求策略。只缓存 HTTP 和 HTTPS 的响应数据。

### 直接获取缓存

你可以通过 URLSession 对象的 [configuration](https://developer.apple.com/documentation/foundation/nsurlsession/1411477-configuration?language=objc) 属性的 URLCache 属性来获取或者设置 URLSession 的缓存对象。 通过 [cachedResponseForRequest:](https://developer.apple.com/documentation/foundation/nsurlcache/1411817-cachedresponseforrequest?language=objc) 方法可以查找 Request 对应的缓存。如果有对应的缓存数据，就会返回 [NSCachedURLResponse](https://developer.apple.com/documentation/foundation/nscachedurlresponse?language=objc) ，否则返回 nil 。 你可以通过缓存来查询资源的占用情况。 [currentDiskUsage](https://developer.apple.com/documentation/foundation/nsurlcache/1407771-currentdiskusage?language=objc) 和 [diskCapacity](https://developer.apple.com/documentation/foundation/nsurlcache/1413505-diskcapacity?language=objc) 表示缓存使用的文件系统资源，而 [currentMemoryUsage](https://developer.apple.com/documentation/foundation/nsurlcache/1408199-currentmemoryusage?language=objc) 和 [memoryCapacity](https://developer.apple.com/documentation/foundation/nsurlcache/1409781-memorycapacity?language=objc) 则表示了内存占用。 你可以通过 [removeCachedResponseForRequest:](https://developer.apple.com/documentation/foundation/nsurlcache/1415377-removecachedresponseforrequest?language=objc) 方法来移除特定的缓存，也可以通过 [removeCachedResponsesSinceDate:](https://developer.apple.com/documentation/foundation/nsurlcache/1415231-removecachedresponsessincedate?language=objc) 来移除指定日期之后的缓存，也可以使用 [removeAllCachedResponses](https://developer.apple.com/documentation/foundation/nsurlcache/1417802-removeallcachedresponses?language=objc) 方法来移除所有缓存。

### 通过代码管理缓存

你可以通过调用 [storeCachedResponse:forRequest:](https://developer.apple.com/documentation/foundation/nsurlcache/1410340-storecachedresponse?language=objc) 方法，提供 CachedURLResponse和 URLRequest 对象来直接写入缓存中。 通常情况下，你可以在 URLSessionTask 对象处理响应时管理响应的缓存。为了在每个响应的基础上管理缓存，需要实现 [NSURLSessionDataDelegate](https://developer.apple.com/documentation/foundation/nsurlsessiondatadelegate?language=objc) 协议的 [URLSession:dataTask:willCacheResponse:completionHandler:](https://developer.apple.com/documentation/foundation/nsurlsessiondatadelegate/1411612-urlsession?language=objc) 方法。这个方法只在上传和数据任务时调用，后台会话和临时配置不会调用。 这个方法提供了两个参数，CachedURLResponse 对象和 completion handler ，你必须在方法中直接调用 completion handler ：

- 可以直接使用提供的 CachedURLResponse 对象进行缓存；
- nil ，不进行缓存；
- 重新创建一个 CachedURLResponse 对象，结合提供的 CachedURLResponse 对象，同时也可以指定 [storagePolicy](https://developer.apple.com/documentation/foundation/nscachedurlresponse/1412269-storagepolicy?language=objc) 和 [userInfo](https://developer.apple.com/documentation/foundation/nscachedurlresponse/1411900-userinfo?language=objc)

```swift
func urlSession(_ session: URLSession, dataTask: URLSessionDataTask,
                willCacheResponse proposedResponse: CachedURLResponse,
                completionHandler: @escaping (CachedURLResponse?) -> Void) {
    if proposedResponse.response.url?.scheme == “https” {
        let updatedResponse = CachedURLResponse(response: proposedResponse.response,
                                                data: proposedResponse.data,
                                                userInfo: proposedResponse.userInfo,
                                                storagePolicy: .allowedInMemoryOnly)
        completionHandler(updatedResponse)
    } else {
        completionHandler(proposedResponse)
    }
}
```

## 处理身份认证

当服务器对某个 URL 请求需要进行身份证验证时，做出适当的响应。 当你的 app 通过 [NSURLSessionTask](https://developer.apple.com/documentation/foundation/nsurlsessiontask?language=objc) 发起请求时，服务器可能会在继续前以一个或者多个的验证要求进行响应。会话任务会尝试处理。如果处理不了，则会调用会话的 [delegate](https://developer.apple.com/documentation/foundation/nsurlsession/1411530-delegate?language=objc) 来进行处理。 为了处理服务器发起的验证请求，你需要实现本文中描述的 delegate 方法。如果你未实现 delegate 对应的方法，那么服务器可能会拒绝你的请求，并且你收到的响应将带有 401 HTTP 状态码（禁止），而不是你期望的数据。

### 确定适当的 delegate 方法

接入 delegate 两个或者其中一个验证方法，取决于你接收到的验证要求的性质。

- 接入 [NSURLSessionDelegate](https://developer.apple.com/documentation/foundation/nsurlsessiondelegate?language=objc) 的 [URLSession:didReceiveChallenge:completionHandler:](https://developer.apple.com/documentation/foundation/nsurlsessiondelegate/1409308-urlsession?language=objc) 的方法来处理会话层级的验证要求。它跟 TLS 验证类似。一旦你成功处理这些验证要求，就会影响到所有通过这个会话 [NSURLSession](https://developer.apple.com/documentation/foundation/nsurlsession?language=objc) 创建的任务
- 接入 [NSURLSessionTaskDelegate](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate?language=objc)[URLSession:task:didReceiveChallenge:completionHandler:](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1411595-urlsession?language=objc) 的方法来处理任务特定的验证要求。这些要求跟输入用户名/密码验证类似。每个会话都有可能需要进行验证请求。

> [NSURLProtectionSpace Authentication Method Constants](https://developer.apple.com/documentation/foundation/nsurlprotectionspace/nsurlprotectionspace_authentication_method_constants?language=objc) 中有说明用于会话或者任务认证的方法。

作为一个简单的例子，想象一下当你请求一个受到 HTTP 的基础认证保护的 URL 请求时（像 [RFC 7617](https://tools.ietf.org/html/rfc7617) 定义的那样）。因为它是任务层级的认证挑战，所以你需要引入 [URLSession:task:didReceiveChallenge:completionHandler:](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate/1411595-urlsession?language=objc) 方法来进行处理。

> 如果你使用 HTTPS 进行连接，你还会接受到服务器信任的挑战。 [Performing Manual Server Trust Authentication](https://developer.apple.com/documentation/foundation/url_loading_system/handling_an_authentication_challenge/performing_manual_server_trust_authentication?language=objc) 有提供更多信息来处理这种会话层级的挑战

![df4288af-90f3-4504-b657-a5ae9b3e994b](https://raw.githubusercontent.com/dirtmelon/blog-images/main/df4288af-90f3-4504-b657-a5ae9b3e994b.png)

### 判断认证挑战的类型

当你接收到一个认证挑战，使用你的 delegate 方法来判断挑战的类型。delegate 方法会接收一个 [NSURLAuthenticationChallenge](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallenge?language=objc) 对象。它描述了正在使用的认证挑战。它包含一个 [protectionSpace](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallenge/1410012-protectionspace?language=objc) 属性，而 [protectionSpace](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallenge/1410012-protectionspace?language=objc) 属性又包含一个 [authenticationMethod](https://developer.apple.com/documentation/foundation/nsurlprotectionspace/1415028-authenticationmethod?language=objc) 属性来指明认证挑战的类型（如一个需要用户名和密码的请求，或者客户端证书）。你可以使用这个值来判断你是否可以处理这个认证挑战。

你可以通过调用传递过来的 completion handler 来响应认证挑战。你需要传递一个 [NSURLSessionAuthChallengeDisposition](https://developer.apple.com/documentation/foundation/nsurlsessionauthchallengedisposition?language=objc) 参数来表示你如何处理这个认证挑战的。你可以使用这个 disposition 参数来提供证书，取消请求或者进行默认的处理方式。

- 下面代码展示了如何根据 `authMethod` 来处理认证挑战，如果是 `NSURLAuthenticationMethodHTTPBasic` ，就使用默认的处理方法。

```swift
let authMethod = challenge.protectionSpace.authenticationMethod
guard authMethod == NSURLAuthenticationMethodHTTPBasic else {
    completionHandler(.performDefaultHandling, nil)
    return
}
```

### 创建证书对象

为了成功响应认证挑战，你需要根据认证挑战的类型来提交一个合适的证书。对于 HTTP 基础和 HTTP 摘要的认证挑战，你需要提供用户名和密码。下面代码展示了一个辅助类如何生成一个由用户输入的 [NSURLCredential](https://developer.apple.com/documentation/foundation/nsurlcredential?language=objc) 对象。

```swift
func credentialsFromUI() -> URLCredential? {
    guard let username = usernameField.text, !username.isEmpty,
        let password = passwordField.text, !password.isEmpty else {
            return nil
    }
    return URLCredential(user: username, password: password,
                         persistence: .forSession)
}
```

在这个例子中，返回的 `NSURLCredential` 包含 [NSURLCredentialPersistenceForSession](https://developer.apple.com/documentation/foundation/nsurlcredentialpersistence/nsurlcredentialpersistenceforsession?language=objc) 的持久化属性，所以它只存储在 `NSURLSession` 对象中，由这个对象创建的任务也包含对应的 `URLCredential` 。

### 调用 Completion handler

一旦你创建了证书对象，你需要调用 completion handler 来响应挑战。

- 如果你无法创建证书，或者用户明确地取消了，调用 completion handler 和传递 [NSURLSessionAuthChallengeCancelAuthenticationChallenge](https://developer.apple.com/documentation/foundation/nsurlsessionauthchallengedisposition/nsurlsessionauthchallengecancelauthenticationchallenge?language=objc) 参数。
- 如果你创建了证书对象，调用 completion handler 和传递 [NSURLSessionAuthChallengeUseCredential](https://developer.apple.com/documentation/foundation/nsurlsessionauthchallengedisposition/nsurlsessionauthchallengeusecredential?language=objc) 参数。

```swift
guard let credential = credentialOrNil else {
    completionHandler(.cancelAuthenticationChallenge, nil)
    return
}
completionHandler(.useCredential, credential)
```

如果你创建的证书被服务器接受，任务就会开始上传和下载数据。

### 优雅地处理错误

当服务器拒绝你的证书时，系统会再次调用你的 delegate 方法。`NSURLAuthenticationChallenge` 的 [proposedCredential](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallenge/1417749-proposedcredential?language=objc) 属性即所提供的证书，同时 [previousFailureCount](https://developer.apple.com/documentation/foundation/nsurlauthenticationchallenge/1416522-previousfailurecount?language=objc) 表示证书请求失败的次数。你可以根据这些属性来判断下一步怎么处理。
