---
title: 'Objective-C 内部探秘：类的架构'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/01/02/objc-class-arch'
original_language: en
published: 2023-01-02
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5f6e0907d814dbc4'
translated: true
---

> 原文：[Objective-C Internals: Class Architecture Objective-C has an unique class architecture where classes are objects. Its elegant design enables dynamic method dispatch for all object types through the us](https://alwaysprocessing.blog/2023/01/02/objc-class-arch)　·　Always Processing (Brian T. Kelley)

# Objective-C 内部探秘：类的架构

![两只黄色拉布拉多犬趴在放有铅笔、纸张和其他设计工具的工作台上。](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/bbda3229-a843-497b-efad-887288209a00/public)

Objective-C 拥有一种独特的类架构，其中类本身就是对象。这种优雅的设计通过编译器生成的元类（metaclass），使得所有对象类型都能实现动态方法派发（dynamic method dispatch）。

Objective-C 与许多流行语言一样，采用[基于类的风格](https://en.wikipedia.org/wiki/Class-based_programming)来实现[面向对象编程](https://en.wikipedia.org/wiki/Object-oriented_programming)。在讨论 Objective-C 的类架构时，我们将把焦点放在类的行为（方法和属性）上，而暂时搁置类的状态（即实例变量（instance variables），相关内容在[这篇文章](https://alwaysprocessing.blog/2023/03/12/objc-ivar-abi)中介绍）。

以下六行代码是探索 Objective-C 类架构所需的全部内容：

```
@interface MyObject: NSObject
+ (void)classMethod;
- (void)instanceMethod;
@end

MyObject *object = [[MyObject alloc] init];
```

## 方法派发

第 6 行实例化了 `MyObject` 类，并将新对象实例赋值给变量 `object`。这个新对象实例拥有自己的状态，并且能够响应消息（即方法调用），例如 `-instanceMethod` 和 `-init`。

Objective-C 对每次消息发送（即每次方法调用）都使用[动态派发](https://en.wikipedia.org/wiki/Dynamic_dispatch)^[[1](#_footnotedef_1)]。运行时通过实例的 `isa` 变量所引用的类对象（class object）中查找选择器（selector，即方法名），来找到方法的实现。（所有 Objective-C 对象的第一个实例变量都是 `isa` 指针，它由编译器自动插入并由运行时初始化。）

上一段中使用“类对象（class object）”一词是刻意的：在 Objective-C 中，类本身也是对象！这种巧妙的设计是“类方法（class method）”这一语言功能的基础（例如调用 `[NSObject alloc]` 或 `[MyObject classMethod]`）：它使得类方法可以完全多态化（即子类可以覆写类方法），并且消除了运行时在类方法和实例方法之间的任何区别（类方法和实例方法都是通过 `objc_msgSend` 来派发的）。

因为类是对象，所以它们同样拥有一个 `isa` 指针，这个指针指向的是**元类（metaclass）**。元类为类对象提供了从选择器到类方法实现（selector-to-class method implementation）的映射，其方式与类对象为类实例（即对象）提供从选择器到实例方法实现的映射完全相同。

## 继承

任何类或元类都只提供该类自身实现的方法所对应的选择器到方法实现的映射。在上面的代码示例中，`MyObject` 的类对象包含 `instanceMethod` 的映射，而 `MyObject` 的元类包含 `classMethod` 的映射。

`MyObject` 也能响应 `+alloc` 和 `-init`，这两个方法是在 `NSObject` 中实现的。每个类对象（包括每个元类）都有一个对其父类（superclass）的引用。在解析选择器时，如果类/元类对象没有定义映射，运行时就会在父类链中继续查找定义。（如果在父类链的末端仍未找到定义，运行时将抛出异常——尽管运行时也提供了用于处理这种情况的备选方案。）

## 架构图

下图展示了上述讨论的 Objective-C 类设计：

- `object` 实例拥有一个指向 `MyClass` 类对象的 `isa` 变量。
- `MyClass` 类对象拥有：
    - 一个指向 `MyClass` 元类的 `isa` 变量。
    - 一个指向 `NSObject` 类对象的 `super` 变量。
- `MyClass` 元类拥有：
    - 一个指向 `NSObject`（根对象）元类的 `isa` 变量。
    - 一个指向 `NSObject` 元类的 `super` 变量。

该图还展示了一些前文未提及的要点：

- 每个元类的 `isa` 变量都指向根对象的元类，包括根对象元类本身。`isa` 不为 `nil` 是合理的（对象必须有某种类型），但我并不确定为什么所有元类的类型都是根元类的类型，而不是由运行时提供的类型。不过，我认为这其实无关紧要，因为元类本身从不接收消息。
- 根元类的父类是根类对象。在为这张图做研究时，我对此感到惊讶。目前我并不清楚这个关联存在的理由——我曾以为它的父类会是 `nil`。

如果有人了解这些设计细节背后的原理，请随时联系我并告诉我！

---

[1](#_footnoteref_1). 从 [Xcode 11.x](https://pspdfkit.com/blog/2020/improving-performance-via-objc-direct/) 或 [Xcode 12](https://nshipster.com/direct/) 开始，Clang 增加了对直接（即[静态](https://en.wikipedia.org/wiki/Static_dispatch)）派发的支持。不过，我尚未能在 Xcode 发布说明或 WWDC 会议中找到任何关于此功能的参考资料。
