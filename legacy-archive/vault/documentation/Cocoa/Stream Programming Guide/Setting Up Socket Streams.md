---
title: 流编程指南
apple_id: 10000188i
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Streams/Articles/NetworkStreams.html
archived_at: '2026-07-15T07:19:26.700600Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [流编程指南](Introduction%20to%20Stream%20Programming%20Guide%20for%20Cocoa.md)


[下一页](Document%20Revision%20History.md)[上一页](Handling%20Stream%20Errors.md)

# 设置套接字流

你可以使用 CFStream API 建立套接字（socket）连接，并用由此创建的流对象（一个或多个）向远程主机（host）发送数据、从远程主机接收数据。你还可以为该连接配置安全特性。

在 iOS 上，NSStream 类不支持连接到远程主机。不过 CFStream _确实_支持这一行为，而且在你用 CFStream API 创建好流之后，可以利用 CFStream 与 NSStream 之间的免费桥接（toll-free bridge），把 CFStream 转换为 NSStream。只需调用 [CFStreamCreatePairWithSocketToHost](https://developer.apple.com/documentation/corefoundation/1539739-cfstreamcreatepairwithsockettoho) 函数，传入主机名和端口（port）号，就能得到针对该主机的 `CFReadStreamRef` 和 `CFWriteStreamRef`。随后你可以把这些对象转换为 NSInputStream 和 NSOutputStream，继续后面的操作。

清单 1 演示了 [CFStreamCreatePairWithSocketToHost](https://developer.apple.com/documentation/corefoundation/1539739-cfstreamcreatepairwithsockettoho) 的用法。这个例子同时创建了一个 `CFReadStreamRef` 对象和一个 `CFWriteStreamRef` 对象。如果你只想得到其中一个，只需把不需要的那个对象对应的参数指定为 `NULL`。

__清单 1__  设置网络套接字流

```objc
- (IBAction)searchForSite:(id)sender
{
    NSString *urlStr = [sender stringValue];
    if (![urlStr isEqualToString:@""]) {
        NSURL *website = [NSURL URLWithString:urlStr];
        if (!website) {
            NSLog(@"%@ is not a valid URL");
            return;
        }

        CFReadStreamRef readStream;
        CFWriteStreamRef writeStream;
        CFStreamCreatePairWithSocketToHost(NULL, (CFStringRef)[website host], 80, &readStream, &writeStream);

        NSInputStream *inputStream = (__bridge_transfer NSInputStream *)readStream;
        NSOutputStream *outputStream = (__bridge_transfer NSOutputStream *)writeStream;
        [inputStream setDelegate:self];
        [outputStream setDelegate:self];
        [inputStream scheduleInRunLoop:[NSRunLoop currentRunLoop] forMode:NSDefaultRunLoopMode];
        [outputStream scheduleInRunLoop:[NSRunLoop currentRunLoop] forMode:NSDefaultRunLoopMode];
        [inputStream open];
        [outputStream open];

        /* 保存对输入流和输出流的引用，
           以免它们被销毁…… */
        ...
    }
}
```

如果你传入的参数无效，请求的 `CFReadStreamRef` 和 `CFWriteStreamRef` 对象中会有一个或两个为 `NULL`。把 CFStream 转换为 NSStream 之后，像平常一样设置[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)（delegate）、把流调度到运行循环（run loop）上并打开流。委托应当开始收到流事件消息（`stream:handleEvent:`）。更多信息请参阅[从输入流读取](Reading%20From%20Input%20Streams.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3tglkcineuuscbi5ca)和[向输出流写入](Writing%20To%20Output%20Streams.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3tilkciffegqkcijbq)。

在打开流对象之前，你可能想为这条通往远程主机（例如一台 HTTPS 服务器）的连接设置安全特性和其他特性。`NSStream` 定义了从两个方面影响 TCP/IP 套接字连接安全性的属性：

- 安全套接字层（SSL）。

  一种安全协议，它使用数字证书为 TCP/IP 连接提供数据加密、服务器身份验证、消息完整性，以及（可选的）客户端身份验证。
- SOCKS 代理服务器。

  一种在 TCP/IP 连接上位于客户端应用程序与真实服务器之间的服务器。它拦截发往真实服务器的请求，如果无法从最近请求过的文件缓存中满足这些请求，就把它们转发给真实服务器。SOCKS 代理服务器有助于提升网络性能，也可用于过滤请求。

对于 SSL 安全性，`NSStream` 定义了各种安全级别属性（例如 `NSStreamSocketSecurityLevelSSLv2`）。你可以用键 `NSStreamSocketSecurityLevelKey` 向流对象发送 `setProperty:forKey:` 来设置这些属性，如下面这条示例消息所示：

```objc
[inputStream setProperty:NSStreamSocketSecurityLevelTLSv1 forKey:NSStreamSocketSecurityLevelKey];
```

你必须在打开流之前设置该属性。流一旦打开，就会执行一次握手协议，以确定连接另一端使用的 SSL 安全级别。如果该安全级别与你指定的属性不兼容，流对象会产生一个错误事件。不过，如果你请求的是协商式安全级别（`NSStreamSocketSecurityLevelNegotiatedSSL`），最终的安全级别会是连接双方都能实现的最高级别。即便如此，如果你在远程主机并不安全的情况下尝试设置 SSL 安全级别，仍会产生错误。

要为某条连接配置 SOCKS 代理服务器，你需要构造一个字典，其中的键形如 `NSStreamSOCKSProxy`_Name_`Key`（例如 `NSStreamSOCKSProxyHostKey`）。每个键的值就是 _Name_ 所指代的那项 SOCKS 代理设置。然后使用 `setProperty:forKey:`，把这个字典设置为 `NSStreamSOCKSProxyConfigurationKey` 的值。

如果你要打开的是通往某台 HTTP 服务器（也就是某个网站）的连接，那么可能需要通过发送一个 HTTP 请求来向该服务器发起一次事务。发出该请求的合适时机，是 `NSOutputStream` 对象的委托通过 `stream:handleEvent:` 消息收到 `NSStreamEventHasSpaceAvailable` 事件的时候。清单 2 展示了委托创建一个 HTTP GET 请求并把它写入输出流，随后立即关闭流对象。

__清单 2__  发起 HTTP GET 请求

```objc
- (void)stream:(NSStream *)stream handleEvent:(NSStreamEvent)eventCode {
    NSLog(@"stream:handleEvent: is invoked...");

    switch(eventCode) {
        case NSStreamEventHasSpaceAvailable:
        {
            if (stream == oStream) {
                NSString * str = [NSString stringWithFormat:
                    @"GET / HTTP/1.0\r\n\r\n"];
                const uint8_t * rawstring =
                    (const uint8_t *)[str UTF8String];
                [oStream write:rawstring maxLength:strlen(rawstring)];
                [oStream close];
            }
            break;
        }
        // 后续代码……
    }
}
```


要进一步了解如何在网络编程中使用流，请阅读 _[网络概述](../../Networking%20Internet%20Web/Networking%20Overview/About%20Networking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrq)_。

[下一页](Document%20Revision%20History.md)[上一页](Handling%20Stream%20Errors.md)

