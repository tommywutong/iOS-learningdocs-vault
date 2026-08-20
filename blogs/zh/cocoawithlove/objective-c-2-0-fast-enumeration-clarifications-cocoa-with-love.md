---
title: 'Objective-C 2.0：快速枚举澄清 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/05/fast-enumeration-clarifications.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:512f5f074ad6b6f5'
translated: true
---

> 原文：[Objective-C 2.0: Fast enumeration clarifications | Cocoa with Love](https://www.cocoawithlove.com/2008/05/fast-enumeration-clarifications.html)　·　Cocoa with Love (Matt Gallagher)

Objective-C 2.0 中的快速枚举（fast enumeration）是一个双重好处的补充：它让代码既更好看，又运行更快。不过，它的文档中仍然有一些含糊或误导之处。以下是我发现的一些澄清说明。

## 你应该已经了解的内容

如果你从未听说过快速枚举，它是 Objective-C 2.0 中的一个新增特性，允许你将 Objective-C 1.0 对 NSSet（或其他集合）的枚举从：

```objc
NSSet *objectSet = &lt;#setaccess#&gt;;
NSEnumerator *enumerator = [objectSet objectEnumerator];
id setObject;
while ((setObject = [enumerator nextObject]) != nil)
{
    &lt;#!loopcontents#&gt;
}
```

改为：

```objc
for (id setObject in &lt;#setaccess#&gt;)
{
    &lt;#!loopcontents#&gt;
}
```

你的代码运行速度也会更快，因为内部实现减少了消息发送的开销，并提高了流水线化的潜力。

由此产生的语法更美观，并能更好地反映程序员的意图。更快、更美观，它就像是为极客们准备的一辆跑车（没有高昂的标价，也没有中年危机的笑话）。

## 文档澄清

### 如何逆向枚举？或者枚举字典的对象而不是键？

Apple 在整个 Cocoa 文档中都提到，你可以在 Mac OS X 10.5 中使用快速枚举代替 NSEnumerator。在 -[NSArray reverseObjectEnumerator] 的文档中，他们指出：“在 Mac OS X v10.5 及更高版本中，使用快速枚举协议（fast enumeration protocol）效率更高。”

这个说法可能有点令人困惑，因为快速枚举并不允许你选择枚举方向。但 Apple 在这里的意思是，你可以使用逆向的 NSEnumerator 对象本身来进行快速枚举。只需获取逆向对象枚举器，然后将它像集合一样传入即可。

如下所示：

```objc
for (id object in [someArray reverseObjectEnumerator])
```

最新可下载的 XCode 文档集仍然遗漏了 NSEnumerator 实际上实现了 NSFastEnumeration 这一事实。[developer.apple.com 上关于 NSEnumerator 的文档](http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Classes/NSEnumerator_Class/Reference/Reference.html) 最终修复了这一遗漏，并且它存在于 Mac OS X 10.5 的头文件中，因此上述代码实际上是有效的语法。

这将对任何返回 NSEnumerator 的方法有效，包括 NSDictionary 的 objectEnumerator。

### “collection”表达式代码是否会被重复调用？

在上面的例子中，你可能会担心 -[NSArray reverseObjectEnumerator] 是否会在循环的每次迭代中都运行——这可能会降低代码速度。在这个例子中情况并不严重，但如果你的代码如下所示呢：

```objc
for (id object in [someObject generateArrayInTimeConsumingCode])
```

在一个普通的 C for 循环中，你会期望 for 表达式在每次迭代时都被求值。[Objective-C 2.0 编程语言：快速枚举](http://developer.apple.com/documentation/Cocoa/Conceptual/ObjectiveC/Articles/chapter_7_section_1.html) 页面暗示它会在每次调用 `countByEnumeratingWithState:objects:count:`（即每几次迭代）时被求值。

通过使用一个实现了自己 `countByEnumeratingWithState:objects:count:` 的测试类，我能够确定以上两种情况**都不成立**。“collection”表达式只在 `for` 循环开始时被求值一次。这是最佳情况，因为你可以在“collection”表达式中安全地放置一个耗时函数，而不会影响循环的每次迭代性能。

### 返回的数据必须是对象指针（“id”）吗？

不是。编译器不会生成任何从返回数据中读取的代码，所以它并不关心。

即使枚举数据的指针被声明为：

```objc
id *itemsPtr;
```

你也可以返回任何你想返回的数据的数组，只要它被包含在一个指针大小的数组中。例如，指向结构体的指针是可以的，char 值也是可以的（前提是它们之间间隔 `sizeof(id)` 的距离）。

### 在 10.4 上快速枚举代码会怎样？

文档明确指出，快速枚举在 Mac OS X 10.4 上无法正常工作，如果你尝试编译，编译器会给出警告。

但这并不完全正确。

如果你针对 Mac OS X 10.5 SDK 库进行编译，但将最低所需操作系统设置为 Mac OS X 10.4，你会收到“for...in”构造不支持的警告。不过，在一定范围内，你可以忽略这些警告。

对于你自己的类的快速枚举，“for...in”构造在 10.4 下无需修改即可工作。

尝试在 10.4 下运行快速枚举代码存在两个潜在严重问题：

- Mac OS X 10.4 中的 Cocoa 类都没有实现 NSFastEnumeration 协议，因此你在 Mac OS X 10.4 下运行时，需要在运行时将你自己设计的 `countByEnumeratingWithState:objects:count:` 方法动态加载到这些类中。
- `objc_enumerationMutation` 函数在 10.4 下不存在，因此如果你在迭代时修改集合（mutate），你不会抛出异常，而是会崩溃。

显然，除非你有非常充分的理由，否则不应该这样做，但如果你愿意承担额外的努力，这个选项是存在的。
