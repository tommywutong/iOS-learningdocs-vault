---
title: 'Cocoa 中一个简单、可扩展的 HTTP 服务器 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/07/simple-extensible-http-server-in-cocoa.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:16fb67d94b076a2b'
translated: true
---

> 原文：[A simple, extensible HTTP server in Cocoa | Cocoa with Love](https://www.cocoawithlove.com/2009/07/simple-extensible-http-server-in-cocoa.html)　·　Cocoa with Love (Matt Gallagher)

HTTP 是用于计算机之间通信的较简单的协议之一。在 iPhone 上，由于没有用于数据同步或文件共享的 API，嵌入 HTTP 服务器是将数据从 iPhone App 传输到计算机的最佳方式之一。在这篇文章中，我将向你展示如何编写自己简单但可扩展的 HTTP 服务器。这些服务器类同样适用于 Mac OS X（Cocoa 无需修改）。

## 引言

在这篇文章中，我将展示以下示例 App：

![](https://www.cocoawithlove.com/assets/objc-era/httpserver.png)

这个 App 非常简单：你可以编辑文本并将其保存到一个文件中（它始终保存到同一个文件）。

在 App 运行期间，它还会在端口 8080 上运行一个 HTTP 服务器。如果请求路径为“/”，它将返回已保存文件的内容。所有其他请求都会返回 501 错误。

要从 iPhone App 传输文本文件，只需在任何 Web 浏览器中输入手机的 IP 地址，后跟“:8080”即可。

## HTTPServer 和 HTTPResponseHandler 类

我用于 HTTP 服务器的方法涉及两个类：服务器（监听连接并读取数据直到 HTTP 头部结束）和响应处理器（发送响应并可以选择从连接中读取头部之后的数据）。

对我来说，关键的设计选择是每个新响应实现的简单性：服务器和响应类的设计使得新的响应实现只需要实现三个方法：

- `canHandleRequest:method:url:headerFields:` — 决定该实现是否能处理特定请求
- `startResponse` — 开始写入（或完整写入）响应
- `load` — 所有子类（subclass）都应实现标准的 `+[NSObject load]` 方法，以向基类注册自己

这只是一个很小的 HTTP 服务器，但这种方法应该能让你快速将 HTTP 通信集成到任何 App 中。

## 打开用于监听的套接字

大多数服务器通信（包括 HTTP）都以创建用于监听的套接字开始。

在 Cocoa 中，可以完全使用 BSD 套接字代码来创建和配置套接字，但在可能的情况下，使用 CoreFoundation 的 `CFSocket` API 通常稍微容易一些。不幸的是，这也只是略微容易——我们仍然需要编写大量样板代码来打开一个套接字。

来自 `-[HTTPServer start]` 方法：

```objc
socket = CFSocketCreate(kCFAllocatorDefault, PF_INET, SOCK_STREAM,
    IPPROTO_TCP, 0, NULL, NULL);
if (!socket)
{
    [self errorWithName:@"Unable to create socket."];
    return;
}

int reuse = true;
int fileDescriptor = CFSocketGetNative(socket);
if (setsockopt(fileDescriptor, SOL_SOCKET, SO_REUSEADDR,
    (void *)&reuse, sizeof(int)) != 0)
{
    [self errorWithName:@"Unable to set socket options."];
    return;
}

struct sockaddr_in address;
memset(&address, 0, sizeof(address));
address.sin_len = sizeof(address);
address.sin_family = AF_INET;
address.sin_addr.s_addr = htonl(INADDR_ANY);
address.sin_port = htons(HTTP_SERVER_PORT);
CFDataRef addressData =
    CFDataCreate(NULL, (const UInt8 *)&address, sizeof(address));
[(id)addressData autorelease];

if (CFSocketSetAddress(socket, addressData) != kCFSocketSuccess)
{
    [self errorWithName:@"Unable to bind socket to address."];
    return;
}
```

这是一大段代码，但它实际上只做了一件事：打开一个套接字，用于监听 `HTTP_SERVER_PORT`（这个 App 的端口为 8080）上的 TCP 连接。

还有一些额外的工作，因为我喜欢指定 `SO_REUSEADDR`。这允许我们在端口处于打开但空闲状态时收回它（这在崩溃或强制退出 App 后立即重新启动程序时很常见）。

## 接收传入连接

套接字设置完成后，Cocoa 会处理更多的工作，事情变得更简单。

我们可以通过从上面的 `fileDescriptor` 构造一个 `NSFileHandle` 并监听连接通知（notification）来接收每个传入连接。

来自 `-[HTTPServer start:]` 方法（紧接在上面的代码之后）：

```objc
listeningHandle = [[NSFileHandle alloc]
    initWithFileDescriptor:fileDescriptor
    closeOnDealloc:YES];

[[NSNotificationCenter defaultCenter]
    addObserver:self
    selector:@selector(receiveIncomingConnectionNotification:)
    name:NSFileHandleConnectionAcceptedNotification
    object:nil];
[listeningHandle acceptConnectionInBackgroundAndNotify];
```

当 `receiveIncomingConnectionNotification:` 被调用时，每个新的传入连接都会获得自己的 `NSFileHandle`。如果你在跟踪记录，那就是：

- 1 个文件句柄（`listeningHandle`），从套接字 `fileDesriptor` 手动创建，用于在套接字上监听新连接。
- 1 个文件句柄，为通过 `listeningHandle` 接收的*每个*新连接自动创建。我们将继续监听这些新句柄（`incomingRequests` 字典中的键（key）），以记录每个连接的数据。

现在，既然我们收到了一个新的、自动创建的文件句柄，我们创建一个 `CFHTTPMessageRef`（将存储我们通过文件句柄接收到的传入数据）。我们将这些信息和 `CFHTTPMessageRef` 分别作为键和值存入 `incomingRequests` 字典中，以便通过每个文件句柄轻松访问对应的 `CFHTTPMessageRef`。

`CFHTTPMessageRef` 既是存储，也是传入数据的解析器。每次添加数据时，我们都可以调用 `CFHTTPMessageIsHeaderComplete()` 来检查 HTTP 头部是否完成，然后生成一个响应处理器。

响应处理器在 `-[HTTPServer receiveIncomingDataNotification:]` 方法中生成：

```objc
if(CFHTTPMessageIsHeaderComplete(incomingRequest))
{
    HTTPResponseHandler *handler =
        [HTTPResponseHandler
            handlerForRequest:incomingRequest
            fileHandle:incomingFileHandle
            server:self];
    
    [responseHandlers addObject:handler];
    [self stopReceivingForFileHandle:incomingFileHandle close:NO];

    [handler startResponse];
    return;
}
```

此时，服务器停止监听该连接的文件句柄，但不会关闭它，因为文件句柄被传递给了 `HTTPResponseHandler`，以便 HTTP 响应可以通过同一个文件句柄发送回去。

## 灵活的响应处理

`+[HTTPResponseHandler handlerForRequest:fileHandle:server:]` 方法选择返回哪个子类（subclass），将决定响应的全部内容。它通过遍历按优先级排序的已注册处理器数组，并询问每个处理器是否要处理该请求来实现这一点。

```objc
+ (Class)handlerClassForRequest:(CFHTTPMessageRef)aRequest
    method:(NSString *)requestMethod
    url:(NSURL *)requestURL
    headerFields:(NSDictionary *)requestHeaderFields
{
    for (Class handlerClass in registeredHandlers)
    {
        if ([handlerClass canHandleRequest:aRequest
            method:requestMethod
            url:requestURL
            headerFields:requestHeaderFields])
        {
            return handlerClass;
        }
    }
    
    return nil;
}
```

为了让这工作，所有 `HTTPResponseHandler` 子类（subclass）都需要向基类注册。最简单的方法是在每个子类中添加 `+[NSObject load]` 方法的实现：

```objc
+ (void)load
{
    [HTTPResponseHandler registerHandler:self];
}
```

在示例 App 中，除了默认的响应处理器之外，唯一的响应处理器是 `AppTextFileResponse`。当 `requestURL` 等于“/”时，这个类选择处理该响应。

来自 `AppTextFileResponse` 类：

```objc
+ (BOOL)canHandleRequest:(CFHTTPMessageRef)aRequest
    method:(NSString *)requestMethod
    url:(NSURL *)requestURL
    headerFields:(NSDictionary *)requestHeaderFields
{
    if ([requestURL.path isEqualToString:@"/"])
    {
        return YES;
    }
    
    return NO;
}
```

然后，`AppTextFileResponse` 通过将 App 保存的文本文件作为响应体写入，同步处理整个响应（在从 `startResponse` 方法返回之前）。

```objc
- (void)startResponse
{
    NSData *fileData =
        [NSData dataWithContentsOfFile:[AppTextFileResponse pathForFile]];

    CFHTTPMessageRef response =
        CFHTTPMessageCreateResponse(
            kCFAllocatorDefault, 200, NULL, kCFHTTPVersion1_1);
    CFHTTPMessageSetHeaderFieldValue(
        response, (CFStringRef)@"Content-Type", (CFStringRef)@"text/plain");
    CFHTTPMessageSetHeaderFieldValue(
        response, (CFStringRef)@"Connection", (CFStringRef)@"close");
    CFHTTPMessageSetHeaderFieldValue(
        response,
        (CFStringRef)@"Content-Length",
        (CFStringRef)[NSString stringWithFormat:@"%ld", [fileData length]]);
    CFDataRef headerData = CFHTTPMessageCopySerializedMessage(response);

    @try
    {
        [fileHandle writeData:(NSData *)headerData];
        [fileHandle writeData:fileData];
    }
    @catch (NSException *exception)
    {
        // Ignore the exception, it normally just means the client
        // closed the connection from the other end.
    }
    @finally
    {
        CFRelease(headerData);
        [server closeHandler:self];
    }
}
```

`[server closeHandler:self];` 调用告诉服务器将这个 `HTTPResponseHandler` 从活动处理器集合中移除。当服务器移除这个处理器时，它会调用 `endReponse`（这就是我们关闭连接的地方——因为这个处理器不支持 `keep-alive`）。

## 未实现的工作

此实现中未处理的最大任务是解析 HTTP 请求体。

原因是通用的 HTTP 请求体解决方案非常复杂。请求体的大小可能由 `Content-Length` 头部指定，但不一定——因此很难知道请求体在哪里结束。请求体也可能以大约十几种不同的 `Transfer-Encoding` 进行编码，包括 `chunk`、`quoted-printable`、`base64`、`gzip`——每种都需要不同的处理。

然而，我从未需要实现一个通用的解决方案。通常最容易的方法是确定你的具体需求是什么，然后根据这些需求处理 HTTP 请求体。你可以通过重写 `-[HTTPRequestHandler receiveIncomingDataNotification:]` 来处理请求体。默认实现会忽略在 HTTP 请求头部之后收到的所有数据。

> **数据处理注意事项**：在第一次调用 `-[HTTPRequestHandler receiveIncomingDataNotification:]` 方法时，HTTP 请求体的初始字节可能已经通过后台从 `fileHandle` 中读取出来并附加到了作为实例（instance）变量的 `request` 中。如果你需要读取请求体，要么继续读取到 `request` 对象中，要么记得包含这些初始数据。

另一个未处理的任务是 Keep-Alive 连接。这些也需要在 `-[HTTPRequestHandler receiveIncomingDataNotification:]` 中处理，并且我在该方法上留下了一大段注释，说明了所涉及的内容。事实上，可能更简单的方法是为每个响应将 `Connection` 头部字段设置为 `close`，以告知客户端你不会处理 Keep-Alive（参见上面的 `startResponse` 代码示例）。

`HTTPReseponseHandler` 的优先级并没有考虑请求的 `Content-Type`。如果这对你来说很重要，你可能需要更改 `+[HTTPResponseHandler handlerClassForRequest:method:url:headerFields:]` 选择其处理器的方式。

最后，这个服务器不处理 SSL/TLS。它旨在用于本地网络传输，在这些网络中，网络本身相对安全。如果你要在开放的互联网上进行传输并希望建立安全连接，那么在套接字层面有很多东西需要修改和管理。你可以自己尝试，但如果安全性真的很重要，你可能不应该冒险编写自己的服务器——如果可以安排，请使用成熟的、支持 TLS 的 HTTP 服务器，并在你的 App 中只处理客户端。在 Cocoa 中，客户端安全性非常容易实现——它在 `CFReadStream` 和 `NSURLConnection` 中是自动且透明的。

## 结论

> [下载示例 App TextTransfer.zip](https://www.cocoawithlove.com/assets/objc-era/TextTransfer.zip) (45kB)，其中包含 `HTTPServer` 和 `HTTPResponseHandler` 类。

主流 HTTP 服务器是庞大复杂的软件，但这并不意味着 HTTP 服务器必然庞大复杂——这里的核心实现只有两个类，却灵活且可配置。

当然，最终的结果不打算用作完整的 Web 服务器解决方案，但它应该非常适合作为一个通信门户，集成到你自定义的 iPhone 或 Mac App 中。
