---
title: 'Objective-C 弱类型的一大缺陷 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2011/06/big-weakness-of-objective-c-weak-typing.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:9ff630dd88d29c83'
translated: true
---

> 原文：[A big weakness in Objective-C's weak typing | Cocoa with Love](https://www.cocoawithlove.com/2011/06/big-weakness-of-objective-c-weak-typing.html)　·　Cocoa with Love (Matt Gallagher)

我们通常认为，在代码中向类型为“`id`”的变量发送任意消息都可以，Objective-C 的动态消息处理机制会保证这些调用在运行时正确工作。但在极少数情况下，这个假设是错误的。本文将讨论向“`id`”类型变量发送消息时需要注意的场景，以及一个因 Objective-C 语言本身的局限而需要用丑陋的绕行方案来避免严重 bug 的情况。

## 引言

我们通常认为，可以向一个“`id`”变量（或 `Class` 变量）发送任意消息。事实上，这正是“`id`”类型的真正用途：它是 Objective-C 中的“任意”类型，可以向它发送任何 Objective-C 消息。

我们在很多场合下使用这种特性，最常见的情况之一就是向 `NSArray` 中存储的对象发送消息：

```objc
NSString *description = [[someArray objectAtIndex:0] substringFromIndex:5];
```

在这段代码中，我们不需要先把 `objectAtIndex:` 调用的结果转型（cast）为 `NSString`，然后再发送 `substringFromIndex:` 消息——我们知道，只要索引 0 处的对象确实是一个能响应 `substringFromIndex:` 选择器（selector）的对象，就能正常工作。

> 本文讨论的是在 Objective-C 的两种“弱类型”（`id` 或 `Class`）上调用方法的情况。如果你在其上调用方法的变量被声明为其他类型（即使是 `id<SomeProtocol>` 也算作“其他类型”，可以避免本文讨论的问题），则本文不适用。

## 错误的假设

此处常见的错误假设是：编译器不需要知道任何类型信息。但实际上，即使方法查找发生在运行时，那也只能确保正确的方法被调用，却不足以保证参数也能正常工作。

编译器**一定**需要推断出所涉及方法签名（method signature）的_某些_信息。尽管编译器不一定需要知道 `id` 的类型，但它确实需要知道所有参数的字节长度以及任何返回值的显式类型。这是因为参数的编组（marshalling，即压入栈和弹出栈）是在编译时配置的。

不过，我们通常不需要为此做任何额外步骤。参数信息的获取方式如下：查看你要调用的方法名称，在导入的头文件中搜索与该方法名匹配的方法，然后从找到的第一个匹配方法中获取参数长度。

99.99% 的情况下，这样做没问题：即使你真正要调用的具体方法存在歧义，但由于 Objective-C 的方法名通常暗示了数据类型，匹配方法之间的参数也很可能是一样的，因此这类冲突不太可能导致签名上的差异。

但接下来就是那 0.01% 的情况……

## 灾难性失败

假设你有一个类 `MyClass`，它有一个名为 `currentPoint` 的实例方法（instance method），返回 `int`。你想从存储在数组中的一个对象上获取 `currentPoint`，因此使用了以下代码：

```objc
int result = [[someArray objectAtIndex:0] currentPoint];
```

当你运行代码时，你知道对数组中第一个对象调用 `currentPoint` 返回的值应该是 0（因为你把它设为了 0，并且在调试器（debugger）中可以看到它仍然是 0），但最终赋给 `result` 的值却是 2,147,483,647（或其他某种部分垃圾值）。

## 哪里出了问题？

实际运行中调用的是正确的方法。问题是编译器错误地编组了这次调用的参数，导致返回类型的数据被损坏。

编译器需要在消息发送之前正确地把参数压入栈，并使用正确的 `objc_msgSend` 变体来执行消息发送，以便之后取回返回值。正是这一步失败了。

编译器通过方法签名（它根据接收者的类型以及所有对该接收者有效的方法名来获取）来准备参数，并试图推断出你可能会调用哪个方法。因为接收者的类型（即 `objectAtIndex:` 的返回结果）只是 `id`，所以我们没有显式的类型信息，编译器会遍历所有已知的方法列表。

不幸的是，编译器没有匹配我们的 `MyClass` 方法，而是选择了 `NSBezierPath` 中名为 `currentPoint` 的方法，并按照该方法的签名准备了参数。`NSBezierPath` 方法返回的是一个 `NSPoint`，这是一个 `struct`，它处理返回值的方式与我们实际方法所用的 `int` 参数截然不同。这导致了我们的返回类型被破坏。

> 我在这里使用 `struct` 值返回类型作为例子，因为它最可能引发 bug，因为返回值为 struct 时，编译器会为消息调用生成 `objc_msgSend_stret`，而不是常规的 `objc_msgSend`。不过，如果非返回参数的字节长度不同，也可能产生问题，尤其是当冲突发生在浮点与非浮点参数之间，或 `struct` 与非 `struct` 参数之间时。

## 解决问题（大多数情况下）

最好的解决办法是为接收者添加额外的类型信息，这样方法名就只有一个可能的匹配了。

我们可以通过向接收者添加转型来实现：

```objc
int result = [(MyClass *)[someArray objectAtIndex:0] currentPoint];
```

对 `MyClass` 类型的接收者来说，`currentPoint` 只有一个匹配项，因此不会与 `NSBezierPath` 方法发生冲突，问题解决了。

## 为什么允许这种情况发生？为什么没有编译器错误？

从技术上讲，编译器有一个警告会提醒你这类问题。编译器警告“严格选择器匹配（Strict Selector Matching）”（即 -Wstrict-selector-match）会在你在 Objective-C 的两种弱类型（`id` 或 `Class`）上调用方法时，如果存在两个不同方法名之间的冲突，就会发出警告。

如果严格选择器匹配总是有效，并且我们可以一直启用它，那就太好了。Apple 没有默认启用它，要么是因为他们认为这个问题足够罕见而可以忽略，要么是承认了这个警告当前存在以下显著局限性：

1. **它会过度警告**。本质上，两个方法签名不同但完全兼容的方法之间存在冲突，我们没必要在意，但这个编译器警告仍然会出现。
2. 由于第（1）点，**Apple 自己的很多方法会引发虚假警告**。比如 `objectForKey:`、`count` 以及 `NSNotificationCenter` 和 `NSDistributedNotificationCenter` 中大多数方法的不同实现。这些虚假警告可能会迫使你大量转型那些实际上不会引发任何问题的方法调用。
3. **它不会警告你类方法和实例方法之间的冲突**。这一点有点荒谬，因为 `Class` 对象通常被当作泛型 `id` 来处理。
4. **如果你根本没有导入正确的定义，它也无能为力**。如果你没有导入正确方法的声明，却导入了另一个方法名相同、签名不同的方法的声明，那么我不确定编译器_能否_就这个问题发出警告。

## 转型无法解决问题的场景

假设在上述例子中，问题发生在两个_类方法_之间，而不是两个_实例方法_之间。

也就是说，冲突不是发生在 `-[NSBezierPath currentPoint]` 和 `-[MyClass currentPoint]` 之间，而是发生在 `+[NSBezierPath currentPoint]` 和 `+[MyClass currentPoint]` 之间。

对于实例方法，我们通过将接收者转型为所需的具体对象类型来解决；但当你的对象都是 `Class` 时，无法转型为具体的类。这是真的：你不能在 Objective-C 中对类进行转型。

我认为这是 Objective-C 的一个严重缺陷。它使得避免类方法名冲突的场景变得十分丑陋。如果你无法修改方法名，那么唯一的绕行方案如下所示：

```objc
int result = objc_msgSend([someArray objectAtIndex:0], @selector(currentPoint));
```

没错：我们需要完全绕过编译器，自己插入 `objc_msgSend` 调用。

然而，情况可能更糟，因为默认情况下 `objc_msgSend` 使用可变参数列表（variable argument list），如果你需要传递给 `objc_msgSend` 或从中接收的参数与可变参数列表的签名不兼容，那么你需要自己完整地转型 `objc_msgSend`，以确保参数正确传递：

```objc
SomeReturnType result =
    ((SomeReturnType(*)(id, SEL, float, short, WeirdStruct))objc_msgSend)
    (
        [someArray objectAtIndex:0],
        @selector(methodWithMultipleVariables:thatAreNot:varArgCompatible:),
        someFloat,
        someShort,
        someWeirdStruct
    );
```

而如果 `SomeReturnType` 是一个 struct，你需要改用 `objc_msgSend_stret`；对于浮点类型，则需要使用 `objc_msgSend_fpret`。

## 结论

我希望给出一个笼统的建议：在每个项目中，都在工作区（Workspace）/项目（Project）/目标（Target）设置中启用“严格选择器匹配”，但不幸的是，这个警告的局限性让这个建议很难实施。

每次你试图在类型为 `id` 的变量上使用 `objectForKey:`（或其他大量方法）时，来自 Apple 代码的虚假警告都会令人恼火，并且无谓地增加你的工作量。

这个警告并不能捕获所有问题，因为它不检查 `Class` 和 `id` 空间之间方法的冲突。因此，考虑到虚假警告的烦恼，认为可以忽略这个警告本身（只需在心里把这个潜在问题记住）这种说法，很可能也是站得住脚的。

这个警告本身应该在 GCC 和 Clang 中得到修复，使其足够可用，从而在所有情况下都保持开启。当冲突签名中的参数兼容时，它不应该给出警告。此外，当代码中的类型是 `id` 时，它也应该在 `Class` 和 `id` 之间进行交叉检查。

而 Objective-C 确实需要一种方式来声明一个具体的 `Class` 类型。即使是像 `@classtype(SomeClass)` 这样丑陋的语法也能解决问题，但我相信能找到更优雅的方式。

我见过有人争辩说，如果你需要一个具体的 `Class`，那说明你的设计很糟糕。我认为，方法名冲突引起的 bug 正属于这样一种场景：如果你无法重命名任一方法，就可能无法在不借助将 Class 转型为更具体类型的能力的情况下，干净利落地从设计层面绕开这个严重问题。

除了能让两个 `Class` 方法之间的冲突更优雅地解决之外，它还有助于解决另一个不相关的情况：方法需要接收一个 `Class` 对象作为参数，但该 `Class` 必须是某个特定类的子类（subclass）。
