---
title: 高级内存管理编程指南
apple_id: 10000011i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Performance
technology: Foundation
published: '2012-07-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmAutoreleasePools.html
archived_at: '2026-07-15T07:16:40.623772Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [高级内存管理编程指南](About%20Memory%20Management.md)


[下一页](Document%20Revision%20History.md)[上一页](Practical%20Memory%20Management.md)

# 使用自动释放池块

自动释放池块（autorelease pool block）提供了一种机制，让你可以放弃某个对象的所有权，同时又避免它被立即释放（例如从方法中返回一个对象时）。通常你不需要创建自己的自动释放池块，但在某些情况下你必须这么做，或者这么做会更有好处。

自动释放池块用 `@autoreleasepool` 标记，如下例所示：

```objc
@autoreleasepool {
    // 创建自动释放对象的代码。
}
```

在自动释放池块结束时，块内收到过 `autorelease` 消息的对象都会收到一条 `release` 消息——对象在块内每收到一次 `autorelease` 消息，就会相应地收到一条 `release` 消息。

和其他任何代码块一样，自动释放池块也可以嵌套：

```objc
@autoreleasepool {
    // . . .
    @autoreleasepool {
        // . . .
    }
    . . .
}
```

（通常你不会看到完全像上面这样的代码；典型的情形是，某个源文件中位于自动释放池块内的代码调用了另一个源文件中的代码，而后者又包含在另一个自动释放池块里。）对于某条给定的 `autorelease` 消息，与之对应的 `release` 消息会在发送该 `autorelease` 消息时所处的那个自动释放池块结束时发出。

Cocoa 始终期望代码在自动释放池块内执行，否则自动释放的对象得不到释放，你的应用程序就会泄漏内存。（如果你在自动释放池块之外发送 `autorelease` 消息，Cocoa 会记录一条相应的错误信息。）AppKit 和 UIKit 框架会把每一次事件循环迭代（例如一次鼠标按下事件或一次点按）都放在一个自动释放池块内处理。因此你通常不必自己创建自动释放池块，甚至看不到创建它的代码。不过，在以下三种场合你可能会用到自己的自动释放池块：

- 如果你编写的程序不是基于 UI 框架的，例如命令行工具。
- 如果你写了一个会创建大量临时对象的循环。

  你可以在循环内部使用一个自动释放池块，在下一次迭代开始之前处置掉这些对象。在循环中使用自动释放池块有助于降低应用程序的内存占用峰值。
- 如果你派生了一个次级线程。

  线程一开始执行，你就必须创建自己的自动释放池块；否则你的应用程序会泄漏对象。（详见[自动释放池块与线程](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga2doljrga2dcobxgy)。）

许多程序都会创建被自动释放的临时对象。这些对象会一直增加程序的内存占用，直到块结束为止。在很多情况下，让临时对象累积到当前事件循环迭代结束并不会带来过多开销；但在某些情况下，你可能会创建大量临时对象，它们会显著增加内存占用，而你希望更快地把它们处置掉。在后一类情况下，你可以创建自己的自动释放池块。在块结束时，这些临时对象会被释放，通常也就随之被销毁，从而降低程序的内存占用。

下面的例子展示了如何在 `for` 循环中使用一个局部的自动释放池块。


```objc
NSArray *urls = <# An array of file URLs #>;
for (NSURL *url in urls) {

    @autoreleasepool {
        NSError *error;
        NSString *fileContents = [NSString stringWithContentsOfURL:url
                                         encoding:NSUTF8StringEncoding error:&error];
        /* 处理这个字符串，过程中会创建并自动释放更多对象。 */
    }
}
```

这个 `for` 循环一次处理一个文件。任何在自动释放池块内收到过 `autorelease` 消息的对象（例如 `fileContents`）都会在块结束时被释放。

在自动释放池块结束之后，你应当把块内被自动释放过的任何对象都视为“已被处置”。不要再向该对象发送消息，也不要把它返回给你这个方法的调用者。如果你必须在自动释放池块之外使用某个临时对象，可以在块内向该对象发送 `retain` 消息，然后在块之后再向它发送 `autorelease`，如下例所示：

```objc
– (id)findMatchingObject:(id)anObject {

    id match;
    while (match == nil) {
        @autoreleasepool {

            /* 执行一次会创建大量临时对象的搜索。 */
            match = [self expensiveSearchForObject:anObject];

            if (match != nil) {
                [match retain]; /* 把 match 保住。 */
            }
        }
    }

    return [match autorelease];   /* 放掉 match 并把它返回。 */
}
```

在自动释放池块内向 `match` 发送 `retain`、并在自动释放池块之后向它发送 `autorelease`，延长了 `match` 的生命期，使它可以在循环之外接收消息，并被返回给 `findMatchingObject:` 的调用者。

Cocoa 应用程序中的每个线程都维护着自己的一个自动释放池块栈。如果你编写的是仅使用 Foundation 的程序，或者你分离出了一个线程，就需要创建自己的自动释放池块。

如果你的应用程序或线程是长期运行的，并且可能产生大量自动释放的对象，你就应该使用自动释放池块（就像 AppKit 和 UIKit 在主线程上所做的那样）；否则自动释放的对象会不断累积，你的内存占用也会持续增长。如果你分离出的线程不调用 Cocoa，那就不需要使用自动释放池块。

[下一页](Document%20Revision%20History.md)[上一页](Practical%20Memory%20Management.md)

