---
title: '8 个令人困惑的 Objective-C 警告和错误 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/04/8-confusing-objective-c-warnings-and.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:d8ee76d486e249d7'
translated: true
---

> 原文：[8 Confusing Objective-C Warnings and Errors | Cocoa with Love](https://www.cocoawithlove.com/2009/04/8-confusing-objective-c-warnings-and.html)　·　Cocoa with Love (Matt Gallagher)

Objective-C 独特的语法带来了独特的犯错方式。在这篇文章中，我列举了当你在 Objective-C 语法中犯错或可能犯错时，GCC 输出的编译器警告和错误，并告诉你如何修复。

## 每个警告都是错误

Objective-C 允许很多与方法调用相关的潜在致命问题仅以警告形式通过。这是因为方法查找系统是动态的，从编译器的角度来看，你*可能*在运行时提供解决方案。

为了使 Objective-C 中这种过度宽松的情况更安全，你应该把每个警告都当作潜在的致命错误。这意味着你应该在构建设置中开启 `GCC_TREAT_WARNINGS_AS_ERRORS`（`-Werror`），这样就能捕获这些问题并修复，而不是让程序继续运行直到运行时崩溃。

每个警告都有消除它的方法。这些没有警告的做法无一例外地代表了更好的设计。我会告诉你如何修复这里列出的每一个警告/错误。

## 1. 错误嵌套的方法括号

```objc
/path/file.m:15: error: syntax error before 'autorelease'
```

（其中 `autorelease` 可以是任何方法中的第一个词）

或

```objc
/path/file.m:15: error: syntax error before ';' token
```

这是本列表中仅有的两个语法错误——我的理由是，尽管问题本身很明显且发生频率很高，但 GCC 给出的错误提示却含糊不清，无法揭示其内在问题。

第一个错误的意思是“你在之前某处缺少了一个左括号”。第二个错误的意思是“你在分号之前缺少了一个右括号”。

如果 GCC 能给出类似“括号不匹配”的错误并指向不匹配的括号，那就太好了。Apple [暗示](http://clang.llvm.org/diagnostics.html)未来的基于 clang 的编译器可能会做到这一点，但目前，你只能看到这些简短的错误信息。

## 2. 试图使用前向类

```objc
/path/file.m:22: warning: receiver 'Test' is a forward class and corresponding @interface may not exist
```

这是一个简单的错误，但很多人（尤其是那些习惯于声明和实现不分离的语言的人）会感到困惑，因为他们可能不确定“前向类（forward class）”是什么。

我想借此机会告诉你：如果你不知道什么是[前向声明（forward declaration）](http://en.wikipedia.org/wiki/Forward_declaration)，或者从未使用过 `@class`，你需要[阅读相关文档](http://developer.apple.com/DOCUMENTATION/Cocoa/Conceptual/ObjectiveC/Articles/ocDefiningClasses.html)。简而言之：`@class` 前向声明告诉编译器某个名字是一个类，但避免导入整个声明（这会在头文件中产生不希望的交叉依赖）。

> **基本规则：**在*头*文件中，永远不要 `#import` 来自同一框架/应用中的其他类（除了父类）——始终使用 `@class` 前向定义。类的 `#import` 应该始终放在*实现*（.m）文件中。对于其他框架的 `#import`（比如 `#import <Cocoa/Cocoa.h>`）是可以的。

这个警告的原因是未能遵循上述基本规则的第二部分：你需要在实现文件中 `#import` 实际的类定义。

旧版本的 GCC（4.0 之前）并不总是给出这个警告。结果就是你可能不小心使用了不存在的类（导致运行时崩溃）。这个警告是一个很大的改进。

## 3. 递归头文件

```objc
/path/file.h:13: warning: duplicate interface declaration for class 'Test'
/path/file.h:15: error: redefinition of 'struct Test'
```

有两种方式会导致这个错误。第一种比较普通：你声明了两个同名的类——这不是 Objective-C 特有的问题。

第二种是：你使用了 `#include` 而不是 `#import` 来导入头文件声明。当连续出现几十（甚至几百）次这个错误时尤其容易识别，特别是如果还伴随着：

```objc
/path/file.h:9:35: error: #include nested too deeply
```

Objective-C 期望所有头文件都使用 `#import` 导入，它可以防止递归包含，因此文件不像标准 C 中那样防护重复包含。

解决方法：始终使用 `#import` 来导入头文件声明（不要听 Richard Stallman 对 `#import` 关键字的批评——他……与众不同）。

## 4. 接口未被导入

```objc
/path/file.m:26: warning: no '-blah' method found
/path/file.m:26: warning: (Messages without a matching method signature
/path/file.m:26: warning: will be assumed to return 'id' and accept
/path/file.m:26: warning: '...' as arguments.)
```

普通的原因是，确实不存在 `blah` 方法（你只是输错了方法名）。

然而，即使方法*确实存在*，Objective-C 也有一些方式会导致这个错误。

- 定义 `-blah` 的类可能不在已导入的类集合中。当你试图调用 `-blah` 的对象被声明为 `id`，或者该类只有前向声明时，就会发生这种情况。
- 你导入了基类，但该方法是声明在一个 `@category` 上，而这个分类没有被导入。

无论哪种情况，解决方法都是找到定义该方法的头文件并 `#import` 它。

还有一种情况也可能导致这个错误：在编译时根本没有该方法的实现。这又可以进一步分为两种情况：

- 运行时处理方法，与特定类有明确关联。例如：Core Data 中 `NSManagedObject` 属性的存取方法。对于这样的方法，你应该在一个分类中声明该方法（即使编译时不会有实现），并导入这个分类。
- 运行时处理方法，没有明确的类关联。为了突出这种运行时和非同寻常的情况，你应该使用 `[object performSelector:@selector(weirdRuntimeMethod)]`，而不是写 `[object weirdRuntimeMethod]` 导致编译器警告。

## 5. 多个不兼容的方法

```objc
/path/file.m:24: warning: multiple methods named '-setStringValue:' found
```

通常，如果存在多个匹配给定名称的方法，Objective-C 不会抱怨（它假设运行时查找能解决），因此这个警告出现时可能会让人惊讶。

这种类型的问题发生在有多个声明具有相同方法名，但方法的参数大小不同时（例如，一个声明期望 32 位 long 参数，另一个声明期望 64 位 long 参数）。这很重要，因为参数大小是在编译时确定的（运行时查找无法改变）。

解决方法是通过将对象转换为精确的类来告诉编译器哪个方法是正确的方法。例如：

```objc
[(NSXMLNode *)myObject setStringValue:@"value"];
```

或

```objc
NSXMLNode *myXMLNodeObject = myObject;
[myXMLNodeObject setStringValue:@"value"];
```

这两种方法产生相同的编译结果。

## 6. 访问错误类型上的属性

```objc
/path/file.m:23: error: request for member 'value' in something not a structure or union
```

在标准 C 代码中使用 `struct` 或 `union` 时可能会产生这个错误，就像错误报告所说的。

在 Objective-C 2.0 中，访问类上的 Objective-C 2.0 属性且编译器找不到该属性时也会发生这个错误。

如果发生这个错误并且你输入的属性名是正确的，那么你可能需要将对象转换为正确的类。例如，如果 `value` 是 `MyClass` 的一个属性：

```objc
id value = ((MyClass *)object).value;
```

或

```objc
MyClass *myClassObject = object;
id value = myClassObject.value;
```

和之前一样，这两种解法是等价的。

这个错误的另一个可能原因是 `MyClass` 没有被正确导入，所以请务必也检查这一点。

## 7. 赋值时的隐式向下转型

```objc
/path/file.m:22: warning: initialization from distinct Objective-C type
```

这个错误的常见原因是你试图将方法的返回值赋给一个不相关的对象类型。这就是一个错误，你需要修复它。

比较棘手的情况是隐式向下转型（implicit downcast）。我的意思是：方法返回了一个父类（比如 `NSObject`），但你知道它实际上是一个子类（比如 `MyClass`）。

在这种情况下，你必须显式转换：

```objc
MyClass *myClassObject = (MyClass *)[someObject getObject];
```

C++ 有 `dynamic_cast` 运算符来处理这种操作，它会验证 `myClassObject` 确实是一个 `MyClass` 对象。在 Objective-C 中，如果你关心运行时类型，应该使用：

```objc
NSAssert([myClassObject isKindOfClass:[MyClass class]],
    @"Return value is not of type MyClass as expected.");
```

如果你经常这样做，可以使用你自己的 `AssertCast` 宏来简化这个操作。

有两种情况允许隐式转换：

- 向上转型（即 `NSObject *myObject = myClassObject;` 是允许的）
- 从 `id` 到任何类型的隐式转换（`id` 是通用对象，可以隐式转换或作为任何类型使用）

这个错误也可能发生在赋值实际上是向上转型但源类只有前向声明的情况下——因此如果声明未被导入，你可能也需要导入它。

## 8. 参数的隐式向下转型

```objc
/path/file.m:24: warning: passing argument 1 of 'test:' from distinct Objective-C type
```

其原因和解决办法与赋值时的向下转型相同。正确地进行类型转换并适当地导入声明。

我知道，这个警告看起来像是第 7 条的重复，但这是一个编程博客：我必须有 8 个条目。在我的脑子里，我把它们都存储在一个索引从 0 到 7 的数组里。

## 结论

永远不要满足于代码中的警告。始终努力去理解 GCC 为什么会发出警告，并修复你的代码。你的代码会更容易理解，并且在运行时也会更安全。
