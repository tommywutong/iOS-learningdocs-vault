---
title: '速度测试：NSManagedObject ObjC-2.0 访问器 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/06/speed-test-nsmanagedobject-objc-20.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:2b6d577fe73b593b'
translated: true
---

> 原文：[Speed test: NSManagedObject ObjC-2.0 accessors | Cocoa with Love](https://www.cocoawithlove.com/2008/06/speed-test-nsmanagedobject-objc-20.html)　·　Cocoa with Love (Matt Gallagher)

在 Leopard 中对 NSManagedObject 属性的三种访问方式进行的一次快速相对性能测试。

## Mac OS X Snow Leopard？我还没跟上 10.5！

如果你整个星期都昏迷不醒，你可能没注意到 Apple 在周一宣布了 Mac OS X 的下一个重大更新 [Snow Leopard](http://www.apple.com/macosx/snowleopard)。它计划于「明年某个时候」发布，这意味着我确实应该完成对当前 Mac OS X 版本代码的更新。

作为这项工作的一部分，我正在评估是否应该重构一些旧有的 pre-Leopard 代码，改用 Leopard 引入的新 NSManagedObject 访问器。

如果你不明白我在说什么，让我给你看看这个……

```objc
// 设置 NSManagedObject 字符串值的旧方式
[object setValue:value forKey:@"stringValue"];

// 设置 NSManagedObject 字符串值的自定义访问器方式
[object setStringValue:value];

// 设置 NSManagedObject 字符串值的新替代语法
object.stringValue = value;
```

在「旧」方法中，NSManagedObject 必须执行字符串比较才能确定 NSManagedObject 的实体（entity）描述中哪个属性（property）对应于提供的「key」。它还必须确定是否存在自定义的 `getter` 和 `setter` 方法，并且可能需要调用它们。

「自定义访问器」方法消除了字符串比较和方法查找，但在 Leopard 之前，你必须显式地自己编写这些方法——这是一项耗时到足以阻碍使用的工作。在 Leopard 中，你只需要声明这些方法，就能免费获得实现。

「新」方法实际上只是通过 Objective-C 2.0 属性（property）使用 Leopard 自动生成的自定义访问器方法，但只需要 `property` 声明（工作量比方法声明又少了一点）。

由于在 Tiger 下「自定义访问器」方法需要额外的开发工作，我大部分 pre-Leopard 代码都使用旧的 KVC 方法。我在乎吗？我应该更新代码吗？

## 给我数据

真正的问题是：这能带来多大差异？我有很多使用「旧」方法的代码。改用其他两种方法之一，我能看到多大的提升？

是时候写一些测试代码了：

```objc
    for (int i = 0; i < 10000; i++)
    {
        for (NSManagedObject *object in objects)
        {
            #if LEOPARD_OBJC_2_ACCESSORS
                NSString *value = object.stringValue;
                object.stringValue = value;
            #elif CUSTOM_METHOD_ACCESSORS
                NSString *value = [object stringValue];
                [object setStringValue:value];
            #else // 键值编码（Key Value Coding）访问器
                NSString *value = [object valueForKey:@"stringValue"];
                [object setValue:value forKey:@"stringValue"];
            #endif
        }
    }
```

我的测试数据是一组 1000 个实体，其 `stringValue` 设置为 `Entity number %d`（其中 `%d` 为 0001 到 1000）。所有数据都已预取（prefaulted）。我所做的只是访问一个字符串值，并将其重新设置为相同的值，重复 1000 万次。

性能表现如下：

| 访问方式 | 耗时 |
|---|---|
| Objective-C 2.0 访问器 | 16.6701 秒 |
| 自定义方法访问器 | 16.7978 秒 |
| 键值编码访问器 | 31.6373 秒 |

* 结果在双 2Ghz PPC G5 上生成（仅支持 Intel 的 Snow Leopard 让他想哭）

## 结论

Leopard 自动生成的访问器所需时间仅为键值编码方法的一半——这是一个显著的改进。「Objective-C 2.0 访问器」和「自定义方法访问器」之间没有实际区别，因此这仅仅是风格偏好和头文件声明的问题。

旧的键值编码方法仍有其用途，特别是在运行时选择的键路径（key path）方面。它也是唯一完全不需要头文件或声明的方法（尽管这可能导致运行时错误）。但除此之外，我确实应该做一些重构。
