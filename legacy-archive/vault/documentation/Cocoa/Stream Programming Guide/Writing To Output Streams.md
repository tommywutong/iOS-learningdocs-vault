---
title: 流编程指南
apple_id: 10000188i
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Streams/Articles/WritingOutputStreams.html
archived_at: '2026-07-15T07:19:28.206144Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [流编程指南](Introduction%20to%20Stream%20Programming%20Guide%20for%20Cocoa.md)


[下一页](Polling%20Versus%20Run-Loop%20Scheduling.md)[上一页](Reading%20From%20Input%20Streams.md)

# 向输出流写入

使用 `NSOutputStream` 实例向输出流写入数据需要以下几个步骤：

1. 用一个存放所写数据的容器[创建并初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)一个 `NSOutputStream` 实例。同时设置[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)（delegate）。
2. 把流对象调度到运行循环（run loop）上，并打开流。
3. 处理流对象上报给其委托的事件（event）。
4. 如果流对象已把数据写入内存，可以请求 `NSStreamDataWrittenToMemoryStreamKey` 属性来获取这些数据。
5. 当没有更多数据要写时，[释放](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27)该流对象。

下面的讨论会更详细地介绍每一个步骤。

要开始使用 `NSOutputStream` 对象，你必须为写入流的数据指定一个去向。输出流对象的去向可以是文件、C 缓冲区（buffer）、应用程序内存或网络套接字（socket）。

`NSOutputStream` 的初始化方法和[工厂方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)允许你基于文件、缓冲区或内存创建并初始化实例。清单 1 展示了如何创建一个把数据写入应用程序内存的 `NSOutputStream` 实例。

__清单 1__  创建并初始化写入内存的 NSOutputStream 对象

```objc
- (void)createOutputStream {
    NSLog(@"Creating and opening NSOutputStream...");
    // oStream 是一个实例变量
    oStream = [[NSOutputStream alloc] initToMemory];
    [oStream setDelegate:self];
    [oStream scheduleInRunLoop:[NSRunLoop currentRunLoop]
        forMode:NSDefaultRunLoopMode];
    [oStream open];
}
```

如清单 1 中的代码所示，创建对象之后你应当设置委托（多数情况下设为 `self`）。当 `NSOutputStream` 对象有与流相关的事件需要上报时（例如流中有空间可容纳字节），委托就会收到该对象发来的 `stream:handleEvent:` [消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)。

在打开流、开始数据流传输之前，向流对象发送 `scheduleInRunLoop:forMode:` 消息，把它调度到某个运行循环上以接收流事件。这样做可以帮助委托在流无法再接收更多字节时避免阻塞。如果数据流传输发生在另一个线程上，务必把流对象调度到那个线程的运行循环上。你绝不应该从持有该流所属运行循环的线程之外的线程去访问一个已被调度的流。最后，向 `NSOutputStream` 实例发送 `open` 消息，开始向输出容器传输数据。

在向流对象发送 `open` 之后，你可以用下面这些消息了解它的状态、是否有空间可写入数据，以及任何错误的具体情况：

- `streamStatus`
- `hasSpaceAvailable`
- `streamError`

返回的状态是一个 `NSStreamStatus` 常量，表示流正在打开、正在写入、已到流末尾等等。返回的错误是一个 `NSError` 对象，其中封装了所发生错误的相关信息。（关于 `NSStreamStatus` 和其他流相关类型的说明，请参阅 NSStream 的参考文档。）

更重要的是，流对象一旦打开，就会持续向其委托发送 `stream:handleEvent:` 消息（只要委托继续往流上放字节），直到遇到流的末尾。这些消息带有一个 `NSStreamEvent` 常量参数，用于指明事件类型。对 `NSOutputStream` 对象而言，最常见的事件类型是 `NSStreamEventOpenCompleted`、`NSStreamEventHasSpaceAvailable` 和 `NSStreamEventEndEncountered`。委托通常最关心 `NSStreamEventHasSpaceAvailable` 事件。清单 2 展示了处理这类事件时可以采用的一种做法。

__清单 2__  处理“有空间可用”事件

```objc
- (void)stream:(NSStream *)stream handleEvent:(NSStreamEvent)eventCode
{
    switch(eventCode) {
        case NSStreamEventHasSpaceAvailable:
        {
            uint8_t *readBytes = (uint8_t *)[_data mutableBytes];
            readBytes += byteIndex; // 用于移动指针的实例变量
            int data_len = [_data length];
            unsigned int len = ((data_len - byteIndex >= 1024) ?
                1024 : (data_len-byteIndex));
            uint8_t buf[len];
            (void)memcpy(buf, readBytes, len);
            len = [stream write:(const uint8_t *)buf maxLength:len];
            byteIndex += len;
            break;
        }
        // 后续代码……
    }
}
```

在这份 `stream:handleEvent:` 实现中，委托使用一个 switch 语句来判别传入的 `NSStreamEvent` 常量。如果该常量是 `NSStreamEventHasSpaceAvailable`，委托就取出 `NSMutableData` 对象（`_data`）所持有的字节，并把指针推进到本次写入操作的位置。接着它确定这次写入操作的字节容量（1024 字节，或者剩余待写的字节数），声明一个该大小的缓冲区，并把相应数量的数据复制到缓冲区中。然后委托调用输出流对象的 `write:maxLength:` 方法，把缓冲区的内容放到输出流上。最后，它推进那个用于移动 `readBytes` 指针的索引，为下一次操作做准备。

如果委托收到了 `NSStreamEventHasSpaceAvailable` 事件却没有向流写入任何内容，那么在 `NSOutputStream` 对象接收到更多字节之前，它不会再从运行循环收到后续的“有空间可用”事件。等到那时，运行循环才会重新开始投递有空间可用事件。如果你的实现中可能出现这种情形，可以让委托在收到 `NSStreamEventHasSpaceAvailable` 事件却_没有_向流写入时设置一个标志。之后当程序有更多字节要写时，就可以检查这个标志，如果已设置，则直接向输出流实例写入。

一次该写入多少字节，并没有硬性准则。虽然在一个事件中把全部数据写入流是有可能的，但这取决于外部因素，比如内核的行为以及设备和套接字的特性。最好的做法是选用一个合理的缓冲区大小，比如 512 字节、1 KB（如上面的例子）或一个页面大小（4 KB）。

当 `NSOutputStream` 对象在向流写入时遇到错误，它会停止传输数据，并通过 `NSStreamEventErrorOccurred` 通知其委托。委托应当在它的 `stream:handleEvent:` 方法中处理该错误，具体做法见[处理流错误](Handling%20Stream%20Errors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3tmlkcineuircgjbda)。

当 `NSOutputStream` 对象结束向输出流写入数据时，它会在 `stream:handleEvent:` 消息中向委托发送 `NSStreamEventEndEncountered` 事件。此时委托应当以准备该对象时的相反顺序来释放这个流对象。换句话说，它应当先关闭流对象，把它从运行循环中移除，最后释放它。此外，如果 `NSOutputStream` 对象的去向是应用程序内存（也就是说，你是用 `initToMemory` 或工厂方法 `outputStreamToMemory` 创建的实例），你现在可能还想取回保存在内存中的数据。清单 3 演示了如何完成所有这些事情。

__清单 3__  关闭并释放 NSInputStream 对象

```objc
- (void)stream:(NSStream *)stream handleEvent:(NSStreamEvent)eventCode
{
    switch(eventCode) {
        case NSStreamEventEndEncountered:
        {
            NSData *newData = [oStream propertyForKey:
                NSStreamDataWrittenToMemoryStreamKey];
            if (!newData) {
                NSLog(@"No data written to memory!");
            } else {
                [self processData:newData];
            }
            [stream close];
            [stream removeFromRunLoop:[NSRunLoop currentRunLoop]
                forMode:NSDefaultRunLoopMode];
            [stream release];
            oStream = nil; // oStream 是实例变量
            break;
        }
        // 后续代码……
    }
}
```

要取得写入内存的流数据，可以向 `NSOutputStream` 对象发送 `propertyForKey:` 消息，并指定 `NSStreamDataWrittenToMemoryStreamKey` 作为键。流对象会在一个 `NSData` 对象中返回这些数据。

[下一页](Polling%20Versus%20Run-Loop%20Scheduling.md)[上一页](Reading%20From%20Input%20Streams.md)

