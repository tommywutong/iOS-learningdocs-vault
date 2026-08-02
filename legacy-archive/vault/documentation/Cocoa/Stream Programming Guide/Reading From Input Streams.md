---
title: 流编程指南
apple_id: 10000188i
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Streams/Articles/ReadingInputStreams.html
archived_at: '2026-07-15T07:19:27.737090Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [流编程指南](Introduction%20to%20Stream%20Programming%20Guide%20for%20Cocoa.md)


[下一页](Writing%20To%20Output%20Streams.md)[上一页](Cocoa%20Streams.md)

# 从输入流读取

在 Cocoa 中，从一个 `NSInputStream` 实例读取数据包含以下几个步骤：

1. 从某个数据来源[创建并初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)一个 `NSInputStream` 实例。
2. 把流对象调度到运行循环（run loop）上，并打开流。
3. 处理流对象上报给其委托（delegate）的事件（event）。
4. 当没有更多数据可读时，[释放](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27)该流对象。

下面的讨论会更详细地介绍每一个步骤。

要开始使用 `NSInputStream` 对象，你必须先拥有（必要时先定位到）该流的数据来源。数据来源可以是文件、`NSData` 对象或网络套接字（socket）。

NSInputStream 的初始化方法和[工厂方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)允许你基于一个 NSData 对象或文件创建并初始化实例。清单 1 展示了一个基于文件创建的 NSInputStream 实例。

__清单 1__  创建并初始化 NSInputStream 对象

```objc
- (void)setUpStreamForFile:(NSString *)path {
    // iStream 是 NSInputStream 类型的实例变量
    iStream = [[NSInputStream alloc] initWithFileAtPath:path];
    [iStream setDelegate:self];
    [iStream scheduleInRunLoop:[NSRunLoop currentRunLoop]
        forMode:NSDefaultRunLoopMode];
    [iStream open];
}
```

如这个例子所示，创建对象之后你应当设置委托（多数情况下设为 `self`）。当 NSInputStream 对象被调度到运行循环上、并且有与流相关的事件需要上报时（例如流上有字节可读），委托就会收到该对象发来的 `stream:handleEvent:` [消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)。

在打开流、开始数据流传输之前，向流对象发送 `scheduleInRunLoop:forMode:` 消息，把它调度到某个运行循环上以接收流事件。这样做可以帮助委托在流上无数据可读时避免阻塞。如果数据流传输发生在另一个线程上，务必把流对象调度到那个线程的运行循环上。你绝不应该从持有该流所属运行循环的线程之外的线程去访问一个已被调度的流。最后，向 `NSInputStream` 实例发送 `open` 消息，开始从输入来源传输数据。

在向流对象发送 `open` 之后，你可以用下面这些消息了解它的状态、是否有字节可读，以及任何错误的具体情况：

- `streamStatus`
- `hasBytesAvailable`
- `streamError`

返回的状态是一个 `NSStreamStatus` 常量，表示流正在打开、正在读取、已到流末尾等等。返回的错误是一个 `NSError` 对象，其中封装了所发生错误的相关信息。（关于 `NSStreamStatus` 和其他流相关类型的说明，请参阅 NSStream 的参考文档。）

更重要的是，流对象一旦打开，就会持续向其委托发送 `stream:handleEvent:` 消息，直到遇到流的末尾。这些消息带有一个 `NSStreamEvent` 常量参数，用于指明事件类型。对 `NSInputStream` 对象而言，最常见的事件类型是 `NSStreamEventOpenCompleted`、`NSStreamEventHasBytesAvailable` 和 `NSStreamEventEndEncountered`。委托通常最关心 `NSStreamEventHasBytesAvailable` 事件。清单 2 展示了处理这类事件的一种不错的做法。

__清单 2__  处理“有字节可读”事件

```objc
- (void)stream:(NSStream *)stream handleEvent:(NSStreamEvent)eventCode {
    switch(eventCode) {
        case NSStreamEventHasBytesAvailable:
        {
            if(!_data) {
                _data = [[NSMutableData data] retain];
            }
            uint8_t buf[1024];
            NSInteger len = 0;
            len = [(NSInputStream *)stream read:buf maxLength:1024];
            if(len) {
                [_data appendBytes:(const void *)buf length:len];
                // bytesRead 是 NSNumber 类型的实例变量。
                [bytesRead setIntValue:[bytesRead intValue]+len];
            } else {
                NSLog(@"no buffer!");
            }
            break;
        }
        // 后续代码
```

在这份 `stream:handleEvent:` 实现中，委托使用一个 switch 语句来判别传入的 `NSStreamEvent` 常量。如果该常量是 `NSStreamEventHasBytesAvailable`，委托首先按需惰性创建一个 `NSMutableData` 对象（`_data`）来保存取到的字节。接着它声明一个特定大小的缓冲区（本例中为 1024 字节），并调用流对象的 `read:maxLength:` 方法，用指定数量的字节填充这个缓冲区。如果读取操作成功从流中取到了字节，委托就把这些字节追加到 `NSMutableData` 对象中。

一次该读取多少字节，并没有硬性准则。虽然在一个事件中读完流里的全部数据是有可能的，但这取决于流的长度（即其中的字节数）以及内核的行为，包括设备和套接字的特性。最好的做法是选用一个合理的缓冲区大小，比如 512 字节、1 KB（如上面的例子）或一个页面大小（4 KB）。

当 `NSInputStream` 对象在处理流时遇到错误，它会停止传输数据，并通过 `NSStreamEventErrorOccurred` 通知其委托。委托应当在它的 `stream:handleEvent:` 方法中处理该错误，具体做法见[处理流错误](Handling%20Stream%20Errors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3tmlkcineuircgjbda)。

当 `NSInputStream` 对象到达流的末尾时，它会在 `stream:handleEvent:` 消息中向委托发送 `NSStreamEventEndEncountered` 事件。委托应当以准备该对象时的相反顺序来释放它。换句话说，它应当先关闭流对象，把它从运行循环中移除，最后释放它。清单 3 给出了一个可行的做法示例。

__清单 3__  关闭并释放 NSInputStream 对象

```objc
- (void)stream:(NSStream *)stream handleEvent:(NSStreamEvent)eventCode
{
    switch(eventCode) {
        case NSStreamEventEndEncountered:
        {
            [stream close];
            [stream removeFromRunLoop:[NSRunLoop currentRunLoop]
                forMode:NSDefaultRunLoopMode];
            [stream release];
            stream = nil; // stream 是实例变量，所以重新初始化它
            break;
        }
        // 后续代码……
    }
}
```

[下一页](Writing%20To%20Output%20Streams.md)[上一页](Cocoa%20Streams.md)

