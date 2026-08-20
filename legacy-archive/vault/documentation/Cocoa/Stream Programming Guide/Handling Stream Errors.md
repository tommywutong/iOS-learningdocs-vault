---
title: 流编程指南
apple_id: 10000188i
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Streams/Articles/HandlingStreamError.html
archived_at: '2026-07-15T07:19:26.174339Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [流编程指南](Introduction%20to%20Stream%20Programming%20Guide%20for%20Cocoa.md)


[下一页](Setting%20Up%20Socket%20Streams.md)[上一页](Polling%20Versus%20Run-Loop%20Scheduling.md)

# 处理流错误

偶尔——尤其是在使用套接字（socket）时——流会遇到错误，导致无法继续处理流数据。一般来说，错误意味着流的某一端缺失了某样东西，比如远程主机（host）崩溃，或者正在传输的文件被删除。大多数错误发生时，流的使用方除了把错误报告给用户之外能做的事情很少。虽然已报告错误的流对象在关闭之前仍可被查询状态，但它无法再用于读写操作。

`NSStream` 和 `NSOutputStream` 类通过以下几种方式告知你发生了错误：

- 如果流对象被调度到运行循环（run loop）上，该对象会在 `stream:handleEvent:` [消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)中向它的[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)（delegate）上报一个 `NSStreamEventErrorOccurred` 事件（event）。
- 使用方可以随时向流对象发送 `streamStatus` 消息，看它是否返回 `NSStreamStatusError`。
- 如果你向 `NSOutputStream` 对象发送 `write:maxLength:` 来写入数据而它返回 -1，说明发生了写入错误。

一旦确定某个流对象遇到了错误，你可以向该对象发送 `streamError` 消息，以获取关于该错误的更多信息（以 `NSError` 对象的形式）。接下来，把该错误告知用户。清单 1 展示了一个被调度到运行循环上的流对象，其委托可以如何处理错误。

__清单 1__  处理流错误

```objc
- (void)stream:(NSStream *)stream handleEvent:(NSStreamEvent)eventCode {
    NSLog(@"stream:handleEvent: is invoked...");

    switch(eventCode) {
        case NSStreamEventErrorOccurred:
        {
            NSError *theError = [stream streamError];
            NSAlert *theAlert = [[NSAlert alloc] init];
            [theAlert setMessageText:@"Error reading stream!"];
            [theAlert setInformativeText:[NSString stringWithFormat:@"Error %i: %@",
                [theError code], [theError localizedDescription]]];
            [theAlert addButtonWithTitle:@"OK"];
            [theAlert beginSheetModalForWindow:[NSApp mainWindow]
                modalDelegate:self
                didEndSelector:@selector(alertDidEnd:returnCode:contextInfo:)
                contextInfo:nil];
            [stream close];
            [stream release];
            break;
        }
        // 后续代码……
    }
}
```

[下一页](Setting%20Up%20Socket%20Streams.md)[上一页](Polling%20Versus%20Run-Loop%20Scheduling.md)

