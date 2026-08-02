---
title: Cocoa 编码规范
apple_id: 10000146i
resource_type: Guide
platform: watchOS|iOS|macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CodingGuidelines/Articles/NamingBasics.html
archived_at: '2026-07-15T07:13:26.779901Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Cocoa 编码规范](Introduction%20to%20Coding%20Guidelines%20for%20Cocoa.md)


[下一页](Naming%20Methods.md)[上一页](Introduction%20to%20Coding%20Guidelines%20for%20Cocoa.md)

# 代码命名基础

在设计面向对象的软件库时，类、方法、函数、常量以及编程接口中其他元素的命名往往是被忽视的一环。本节讨论 [Cocoa](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Cocoa.html#//apple_ref/doc/uid/TP40008195-CH9) 接口中大多数元素通用的若干命名[规范](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/CodingConventions.html#//apple_ref/doc/uid/TP40008195-CH53)。

_清晰性_

- 名称既清晰又简短当然最好，但不能为了简短而牺牲清晰：

| 代码 | 说明 |
| --- | --- |
| `insertObject:atIndex:` | 好。 |
| `insert:at:` | 不清晰；插入的是什么？“at”又指什么？ |
| `removeObjectAtIndex:` | 好。 |
| `removeObject:` | 好，因为它移除的正是参数所指的对象。 |
| `remove:` | 不清晰；移除的是什么？ |
- 一般来说，不要缩写名称。哪怕拼出来很长，也要完整拼写：

| 代码 | 说明 |
| --- | --- |
| `destinationSelection` | 好。 |
| `destSel` | 不清晰。 |
| `setBackgroundColor:` | 好。 |
| `setBkgdColor:` | 不清晰。 |

  你可能觉得某个缩写（abbreviation）人尽皆知，但事实未必如此，尤其当读到你的方法名或函数名的开发者来自不同的文化和语言背景时。
- 不过，确实有少数缩写极为常见且沿用已久，你可以继续使用它们；参见[可接受的缩写与首字母缩略词](Acceptable%20Abbreviations%20and%20Acronyms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dklkcineuqq2hifcq)。

- 避免 API 名称有歧义，比如可以有多种解读方式的方法名。

| 代码 | 说明 |
| --- | --- |
| `sendPort` | 它是发送这个 port，还是返回一个 port？ |
| `displayName` | 它是显示某个名称，还是返回接收者在用户界面中的标题？ |

_一致性_

- 在整个 Cocoa 编程接口中尽量保持名称用法一致。拿不准时，可以浏览现有的头文件或参考文档，看看先例是怎么做的。
- 当一个类的方法需要利用多态时，一致性尤为重要。不同类中做同一件事的方法应当取相同的名字。

| 代码 | 说明 |
| --- | --- |
| `- (NSInteger)tag` | 在 `NSView`、`NSCell`、`NSControl` 中均有定义。 |
| `- (void)setStringValue:(NSString *)` | 在多个 Cocoa 类中均有定义。 |

另请参阅[方法参数](Naming%20Methods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4deljrgaydcobwgu)。

_不要自我指涉_

- 名称不应该自我指涉。

| 代码 | 说明 |
| --- | --- |
| `NSString` | 可以。 |
| `NSStringObject` | 自我指涉。 |
- 掩码类常量（因而可以通过按位运算组合）是这条规则的例外，[通知](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35)名称常量也是例外。

| 代码 | 说明 |
| --- | --- |
| `NSUnderlineByWordMask` | 可以。 |
| `NSTableViewColumnDidMoveNotification` | 可以。 |

前缀（prefix）是编程接口中名称的重要组成部分，它用来区分软件的不同功能领域。这些软件通常打包在一个[框架](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56)中，或者（像 Foundation 和 Application Kit 那样）打包在若干紧密相关的框架中。前缀可以防止第三方开发者定义的符号与 Apple 定义的符号发生冲突（也能防止 Apple 自家框架之间的符号冲突）。

- 前缀有规定的格式：由两到三个大写字母组成，不使用下划线，也不使用“子前缀”。以下是一些例子：

| 前缀 | Cocoa 框架 |
| --- | --- |
| NS | Foundation |
| NS | Application Kit |
| AB | Address Book |
| IB | Interface Builder |
- 命名类、[协议](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45)、函数、常量和 `typedef` 结构体时要使用前缀。命名方法时_不要_使用前缀；方法存在于定义它的类所创建的命名空间中。此外，结构体的字段名也不要加前缀。

命名 API 元素时，请遵循几条简单的排版约定：

- 对于由多个单词组成的名称，不要用标点符号作为名称的一部分或作为分隔符（下划线、连字符等）；而应把每个单词的首字母大写，然后把这些单词连写在一起（例如 `runTheWordsTogether`）——这就是所谓的驼峰式（camel case）。不过要注意以下几点限定：

  - 对于方法名，以小写字母开头，内嵌单词的首字母大写。不要使用前缀。

```objc
fileExistsAtPath:isDirectory:
```

    这条准则的例外是以知名首字母缩略词（acronym）开头的方法名，例如 `TIFFRepresentation`（`NSImage`）。
  - 对于函数名和常量名，使用与相关类相同的前缀，并把内嵌单词的首字母大写。

```objc
NSRunAlertPanel
NSCellDisabled
```
- 避免在_方法_名中用下划线作为表示私有的前缀（用下划线作为_实例变量_名的前缀是允许的）。Apple 保留了这一约定的使用权。第三方若使用它，可能导致命名空间冲突；他们可能在不知情的情况下用自己的方法[覆写](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MethodOverriding.html#//apple_ref/doc/uid/TP40008195-CH57)了一个已有的私有方法，后果不堪设想。关于私有 API 应遵循的约定，参见[私有方法](Naming%20Methods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4deljrgaydgobshe)。

类名中应当包含一个名词，清楚地表明这个类（或该类的对象）代表什么或者做什么。类名还应带有恰当的前缀（参见[前缀](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dcljrgaydemrsgy)）。Foundation 和应用程序框架中这样的例子比比皆是，比如 `NSString`、`NSDate`、`NSScanner`、`NSApplication`、`UIApplication`、`NSButton` 和 `UIButton`。

[协议](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45)应当按照它所归拢的行为来命名：

- 大多数_协议_归拢的是一组彼此相关、但不与某个特定类关联的方法。这类协议的命名应当让人不会把协议误认为类。常见的做法是使用动名词（“...ing”）形式：

| 代码 | 说明 |
| --- | --- |
| `NSLocking` | 好。 |
| `NSLock` | 不好（看起来像个类名）。 |
- 有些协议归拢了一批互不相关的方法（而不是拆成几个独立的小协议）。这类协议往往与某个类关联，该类是这个协议的主要体现。这种情况下，惯例是让协议与类同名。

  [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intf/NSObject) 协议就是这类协议的一个例子。这个协议归拢的方法可以用来查询任意对象在类层次中的位置、让它调用特定方法、以及增减它的引用计数。由于 [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject) 类是这些方法的主要体现，该协议便以这个类命名。

头文件（header file）的命名方式很重要，因为你采用的约定表明了文件里装的是什么内容：

- _声明单独的类或协议_。如果某个类或协议不属于任何一组，就把它的声明放在一个单独的文件里，文件名即该类或协议的名称。

| 头文件 | 声明内容 |
| --- | --- |
| `NSLocale.h` | `NSLocale` 类。 |
- _声明相关的类和协议_。对于一组相关的声明（类、分类和协议），把这些声明放在一个以主类、[分类](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Category.html#//apple_ref/doc/uid/TP40008195-CH5)或[协议](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45)命名的文件中。

| 头文件 | 声明内容 |
| --- | --- |
| `NSString.h` | `NSString` 和 `NSMutableString` 类。 |
| `NSLock.h` | `NSLocking` 协议，以及 `NSLock`、`NSConditionLock` 和 `NSRecursiveLock` 类。 |
- _包含框架头文件_。每个框架都应当有一个以框架命名的头文件，它包含该框架所有的公开头文件。

| 头文件 | 框架 |
| --- | --- |
| `Foundation.h` | `Foundation.framework`。 |
- _为另一个框架中的类添加 API_。如果你在一个框架中为另一个框架中的类声明了分类方法，就在原类名后面追加“Additions”；Application Kit 的 `NSBundleAdditions.h` 头文件就是一例。
- _相关的函数和数据类型_。如果你有一组相关的函数、常量、结构体和其他数据类型，就把它们放在一个命名恰当的头文件里，比如 `NSGraphics.h`（Application Kit）。

[下一页](Naming%20Methods.md)[上一页](Introduction%20to%20Coding%20Guidelines%20for%20Cocoa.md)

