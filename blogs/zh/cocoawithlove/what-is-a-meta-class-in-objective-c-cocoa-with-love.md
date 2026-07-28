---
title: '什么是 Objective-C 中的元类？ | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/01/what-is-meta-class-in-objective-c.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:75eafb2c3b532789'
translated: true
---

> 原文：[What is a meta-class in Objective-C? | Cocoa with Love](https://www.cocoawithlove.com/2010/01/what-is-meta-class-in-objective-c.html)　·　Cocoa with Love (Matt Gallagher)

在这篇文章中，我将探讨 Objective-C 中一个比较陌生的概念——元类（meta-class）。Objective-C 中的每个类都有其关联的元类，但由于你很少直接使用元类，它们可能仍然难以理解。我将首先介绍如何在运行时创建一个类。然后通过检查这个过程中创建的“类对”（class pair），来解释什么是元类，同时我也会更广泛地讨论在 Objective-C 中数据作为对象或类意味着什么。

## 在运行时创建一个类

下面的代码在运行时创建了一个 `NSError` 的新子类（subclass），并为其添加了一个方法：

```objc
Class newClass =
    objc_allocateClassPair([NSError class], "RuntimeErrorSubclass", 0);
class_addMethod(newClass, @selector(report), (IMP)ReportFunction, "v@:");
objc_registerClassPair(newClass);
```

添加的方法使用名为 `ReportFunction` 的函数作为其实现，该函数定义如下：

```objc
void ReportFunction(id self, SEL _cmd)
{
    NSLog(@"This object is %p.", self);
    NSLog(@"Class is %@, and super is %@.", [self class], [self superclass]);
    
    Class currentClass = [self class];
    for (int i = 1; i < 5; i++)
    {
        NSLog(@"Following the isa pointer %d times gives %p", i, currentClass);
        currentClass = object_getClass(currentClass);
    }

    NSLog(@"NSObject's class is %p", [NSObject class]);
    NSLog(@"NSObject's meta class is %p", object_getClass([NSObject class]));
}
```

表面上看起来很简单。在运行时创建一个类只需三个简单的步骤：

1. 为“类对”分配存储空间（使用 `objc_allocateClassPair`）。
2. 根据需要为类添加方法和实例变量（我已经用 `class_addMethod` 添加了一个方法）。
3. 注册这个类，以便它可以使用（使用 `objc_registerClassPair`）。

然而，直接的问题是：什么是“类对”？函数 `objc_allocateClassPair` 只返回一个值：类（class）。这对中的另一半在哪里？

我相信你已经猜到，这对中的另一半就是元类（这正是本文的标题），但为了解释它是什么以及为什么需要它，我将先介绍一些 Objective-C 中对象和类的背景知识。

## 一个数据结构需要什么才能成为对象？

每个对象都有一个类（class）。这是一个基本的面向对象概念，但在 Objective-C 中，它也是数据的基本组成部分。任何在正确位置拥有指向类指针的数据结构都可以被视为一个对象。

在 Objective-C 中，对象的类由其 `isa` 指针决定。`isa` 指针指向该对象的 Class。

事实上，Objective-C 中对象的基本定义是这样的：

```objc
typedef struct objc_object {
    Class isa;
} *id;
```

这意味着：任何以一个指向 `Class` 结构的指针开头的结构，都可以被当作一个 `objc_object` 来处理。

Objective-C 中对象最重要的特性是，你可以向它们发送消息：

```objc
[@"stringValue"
    writeToFile:@"/file.txt" atomically:YES encoding:NSUTF8StringEncoding error:NULL];
```

这之所以有效，是因为当你向一个 Objective-C 对象（比如这里的 `NSCFString`）发送消息时，运行时会跟随该对象的 `isa` 指针到达该对象的 `Class`（这里是 `NSCFString` 类）。`Class` 包含一个应用于该 `Class` 所有对象的 `Method` 列表，以及一个指向超类（`superclass`）的指针，用于查找继承的方法。运行时会在 `Class` 及其超类的 `Method` 列表中查找，找到与消息选择器（selector）匹配的方法（上述例子中是 `NSString` 的 `writeToFile:atomically:encoding:error`）。然后运行时会调用该方法的函数（`IMP`）。

关键在于，`Class` 定义了你可以向对象发送的消息。

## 什么是元类（meta-class）？

现在，你可能已经知道，Objective-C 中的一个 `Class` 本身也是一个对象。这意味着你可以向一个 `Class` 发送消息。

```objc
NSStringEncoding defaultStringEncoding = [NSString defaultStringEncoding];
```

在这个例子中，`defaultStringEncoding` 被发送给了 `NSString` 类。

这之所以有效，是因为 Objective-C 中的每个 `Class` 本身都是一个对象。这意味着 `Class` 结构必须以一个 `isa` 指针开头，以便与我上面展示的 `objc_object` 结构二进制兼容，并且结构中的下一个字段必须是一个指向超类（`superclass`）的指针（对于基类，则为 `nil`）。

[正如我上周展示的](https://www.cocoawithlove.com/2010/01/getting-subclasses-of-objective-c-class.html)，根据你运行的运行时版本，`Class` 的定义可能有几种不同的方式，但没错，它们都以一个 `isa` 字段开头，后面跟着一个 `superclass` 字段。

```objc
typedef struct objc_class *Class;
struct objc_class {
    Class isa;
    Class super_class;
    /* followed by runtime specific details... */
};
```

然而，为了让我们能够在 `Class` 上调用方法，`Class` 的 `isa` 指针本身必须指向一个 `Class` 结构，并且该 `Class` 结构必须包含我们可以在这个 Class 上调用的 `Method` 列表。

这就引出了元类的定义：元类是一个 `Class` 对象的类。

简单来说：

- 当你向一个对象发送消息时，会在该对象的类的方法列表中查找该消息。
- 当你向一个类发送消息时，会在该类的元类的方法列表中查找该消息。

元类是必不可少的，因为它存储了一个 `Class` 的类方法。每个 `Class` 都必须有一个唯一的元类，因为每个 `Class` 可能拥有唯一的类方法列表。

## 元类的类是什么？

元类，与 `Class` 一样，本身也是一个对象。这意味着你也可以在它上面调用方法。自然，这意味着它也必须有一个类。

所有元类都使用基类的元类（即继承层次结构中顶层 `Class` 的元类）作为它们的类。这意味着，对于所有继承自 `NSObject` 的类（大多数类），元类都以 `NSObject` 元类作为其类。

遵循所有元类都使用基类的元类作为其类这一规则，任何基元类都将是它自己的类（它们的 `isa` 指针指向自身）。这意味着 `NSObject` 元类上的 `isa` 指针指向它自己（它是它自己的实例）。

## 类和元类的继承

与 `Class` 通过其 `super_class` 指针指向超类的方式类似，元类也通过其自身的 `super_class` 指针指向该 `Class` 的 `super_class` 的元类。

另一个特别之处是，基类的元类将其 `super_class` 设置为基类本身。

这种继承层次结构的结果是，该层次结构中的所有实例、类和元类都继承自该层次结构的基类。

对于 `NSObject` 层次结构中的所有实例、类和元类，这意味着所有 `NSObject` 实例方法都是有效的。对于类和元类，所有 `NSObject` 类方法也同样是有效的。

所有这些用文字表述都相当令人困惑。[Greg Parker](http://www.sealiesoftware.com/blog/) 整理了一份[关于实例、类、元类及其超类的优秀示意图](http://www.sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html)，展示了它们是如何组合在一起的。

## 对此的实验验证

为了验证所有这些，让我们来看看本文开头给出的 `ReportFunction` 的输出。这个函数的目的是跟踪 `isa` 指针并记录它所发现的内容。

要运行 `ReportFunction`，我们需要创建一个动态创建类的实例，并在其上调用 `report` 方法。

```objc
id instanceOfNewClass =
    [[newClass alloc] initWithDomain:@"someDomain" code:0 userInfo:nil];
[instanceOfNewClass performSelector:@selector(report)];
[instanceOfNewClass release];
```

由于没有 `report` 方法的声明，我使用 `performSelector:` 来调用它，这样编译器不会给出警告。

`ReportFunction` 现在将遍历 `isa` 指针，并告诉我们哪些对象被用作类、元类以及元类的类。

> **获取对象的类：** `ReportFunction` 使用 `object_getClass` 来跟踪 `isa` 指针，因为 `isa` 指针是类的保护成员（你不能直接访问其他对象的 `isa` 指针）。`ReportFunction` 不使用 `class` 方法来做到这一点，因为在一个 `Class` 对象上调用 `class` 方法不会返回元类，而是再次返回该 `Class`（所以 `[NSString class]` 将返回 `NSString` 类，而不是 `NSString` 元类）。

这是程序运行时的输出（去除了 `NSLog` 前缀）：

```objc
This object is 0x10010c810.
Class is RuntimeErrorSubclass, and super is NSError.
Following the isa pointer 1 times gives 0x10010c600
Following the isa pointer 2 times gives 0x10010c630
Following the isa pointer 3 times gives 0x7fff71038480
Following the isa pointer 4 times gives 0x7fff71038480
NSObject's class is 0x7fff710384a8
NSObject's meta class is 0x7fff71038480
```

查看通过反复跟踪 `isa` 值所到达的地址：

- 对象是地址 `0x10010c810`。
- 类是地址 `0x10010c600`。
- 元类是地址 `0x10010c630`。
- 元类的类（即 `NSObject` 元类）是地址 `0x7fff71038480`。
- `NSObject` 元类的类就是它自己。

这些地址的值本身并不重要，只是它们展示了从类到元类再到 `NSObject` 元类的过程，正如我们所讨论的那样。

## 结论

元类是一个 `Class` 对象的类。每个 `Class` 都有自己唯一的元类（因为每个 `Class` 可以拥有自己唯一的方法列表）。这意味着，并非所有 `Class` 对象都属于同一个类。

元类将始终确保 `Class` 对象拥有层次结构中基类的所有实例方法和类方法，以及所有中间类的类方法。对于继承自 `NSObject` 的类，这意味着 `NSObject` 的所有实例方法和协议方法都在所有 `Class`（以及元类）对象上定义了。

所有元类本身都使用基类的元类（对于 `NSObject` 层次结构中的类来说是 `NSObject` 元类）作为它们的类，包括基元类，它是运行时中唯一自我定义的类。
