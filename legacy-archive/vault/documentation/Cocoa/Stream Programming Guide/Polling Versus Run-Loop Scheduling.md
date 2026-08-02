---
title: 流编程指南
apple_id: 10000188i
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Streams/Articles/PollingVersusRunloop.html
archived_at: '2026-07-15T07:19:27.181338Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [流编程指南](Introduction%20to%20Stream%20Programming%20Guide%20for%20Cocoa.md)


[下一页](Handling%20Stream%20Errors.md)[上一页](Writing%20To%20Output%20Streams.md)

# 轮询与运行循环调度

流处理中一个潜在的问题是阻塞。正在向流写入或从流读取的线程，可能不得不无限期地等待——分别等待流上出现可放入字节的空间，或等待流上出现可读取的字节。实际上，这个线程完全受制于流，而这可能给应用程序带来麻烦。对套接字（socket）流来说，阻塞尤其容易成为问题，因为它们依赖远程主机（host）的响应。

在 Cocoa 流中，你有两种处理流事件（event）的方式：

- _运行循环调度_。你把流对象调度到运行循环（run loop）上，这样只有在不太可能发生阻塞时，委托（delegate）才会收到上报流相关事件的[消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)。对读写操作而言，相关的 `NSStreamEvent` 常量是 `NSStreamHasBytesAvailable` 和 `NSStreamHasSpaceAvailable`。
- _轮询_。在一个只有到达流末尾或发生错误时才会跳出的闭环里，你不断询问流对象：（对读取流）是否有字节可读，或者（对写入流）是否有空间可写。相关的方法是 `hasBytesAvailable`（NSInputStream）和 `hasSpaceAvailable`（NSOutputStream）。

运行循环调度几乎总是优于轮询，这也正是[从输入流读取](Reading%20From%20Input%20Streams.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3tglkcineuuscbi5ca)和[向输出流写入](Writing%20To%20Output%20Streams.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3tilkciffegqkcijbq)中的代码示例清一色使用运行循环的原因。采用轮询时，你的程序被锁死在一个紧凑的循环里，苦等一个未必马上到来的流事件。采用运行循环调度时，你的程序可以去做别的事情，因为它知道一旦有流事件需要处理就会收到通知。而且，运行循环让你不必自己管理状态，效率也比轮询更高。轮询还很耗 CPU；你的处理时间本可以用来做别的事。

话虽如此，在某些场景下轮询仍是可行的选择。例如，如果你在移植遗留代码，可能会选择使用轮询，因为它更契合遗留代码中的线程模型。清单 1 展示了一个用轮询方式向输出流写入数据的方法。

__清单 1__  使用轮询向输出流写入数据

```objc
- (void)createNewFile {
    oStream = [[NSOutputStream alloc] initToMemory];
    [oStream open];
    uint8_t *readBytes = (uint8_t *)[data mutableBytes];
    uint8_t buf[1024];
    int len = 1024;

    while (1) {
        if (len == 0) break;
        if ( [oStream hasSpaceAvailable] ) {
        (void)strncpy(buf, readBytes, len);
        readBytes += len;
        if ([oStream write:(const uint8_t *)buf maxLength:len] == -1) {
            [self handleError:[oStream streamError]];
            break;
        }
        [bytesWritten setIntValue:[bytesWritten intValue]+len];
        len = (([data length] - [bytesWritten intValue] >= 1024) ? 1024 :
            [data length] - [bytesWritten intValue]);
        }
    }
    NSData *newData = [oStream propertyForKey:
        NSStreamDataWrittenToMemoryStreamKey];
    if (!newData) {
        NSLog(@"No data written to memory!");
    } else {
        [self processData:newData];
    }
    [oStream close];
    [oStream release];
    oStream = nil;
}
```

需要指出的是，轮询和运行循环调度这两种方式都不是防止阻塞的万全之策。如果 NSInputStream 的 `hasBytesAvailable` 方法或 NSOutputStream 的 `hasSpaceAvailable` 方法返回 `NO`，那么在这两种情形下都意味着流确实没有可用的字节或空间。然而，如果这两个方法中的任何一个返回 `YES`，它既可能意味着确实有可用的字节或空间，_也_可能意味着唯一的确认办法就是尝试一次读取或写入操作（而这可能导致短暂的阻塞）。`NSStreamEventHasBytesAvailable` 和 `NSStreamEventHasSpaceAvailable` 这两个流事件具有完全相同的语义。

[下一页](Handling%20Stream%20Errors.md)[上一页](Writing%20To%20Output%20Streams.md)

