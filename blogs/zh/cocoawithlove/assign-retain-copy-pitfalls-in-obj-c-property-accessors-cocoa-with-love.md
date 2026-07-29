---
title: 'Assign, retain, copy：Obj-C 属性访问器中的陷阱 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/06/assign-retain-copy-pitfalls-in-obj-c.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:f9e7e2f8c212bc57'
translated: true
---

> 原文：[Assign, retain, copy: pitfalls in Obj-C property accessors | Cocoa with Love](https://www.cocoawithlove.com/2010/06/assign-retain-copy-pitfalls-in-obj-c.html)　·　Cocoa with Love (Matt Gallagher)

在这篇文章中，我将探讨如果 getter 或 setter 方法选择了错误的内存管理模式可能会引发的一些非常微妙的问题，并在此过程中解释为什么 `NSDictionary` 会拷贝（copy）其键而不是简单地保留（retain）它们。

> **本文范围**：在这篇文章中，我将讨论 Objective-C 访问器方法中的基本内存和可变性考虑。如果你对访问器方法中的原子性（atomicity）和线程安全问题感兴趣，请阅读我早先的文章 [内存与线程安全的自定义属性方法](https://www.cocoawithlove.com/2009/10/memory-and-thread-safe-custom-property.html)。本文仅关注非原子（non-atomic）访问器。

## 为什么要实现你自己的访问器？

如果你了解 Objective-C 的属性（properties），你可能已经在问：“为什么要自己实现访问器？”对于简单的访问器，你可以（而且很应该）使用合成的 `@property` 访问器，而不用担心其实现。写这篇文章的原因是，你常常需要自己实现访问器方法，以便在 get 或 set 动作上附加一些额外的行为，所以你总是需要知道访问器应该如何工作。

## 你已经知道的那种模式：assign 模式

既然你在读这篇博客，大概可以假设你已经知道基本的 assign 访问器长什么样：

```objc
- (SomeVariable)someValue
{
    return someValue;
}
```

而 setter 方法看起来是这样：

```objc
- (void)setSomeValue:(SomeVariable)aSomeVariableValue
{
    someValue = aSomeVariableValue;
}
```

对于大多数非对象数据，这就足够了。这就是你在非原子 `assign` 合成的 `@property` 中得到的实现。

## Retain：首次出现问题的机会

如果你在 Objective-C 中处理 retain/release 对象，你的对象会在 setter 没有 retain 它时变得无效，因此 setter 必须处理这个问题。

在 setter 中处理 `retain` 和 `release` 问题最彻底、最通用的方式是这样的：

```objc
- (void)setSomeInstance:(SomeClass *)aSomeInstanceValue
{
    if (someInstance == aSomeInstanceValue)
    {
        return;
    }
    SomeClass *oldValue = someInstance;
    someInstance = [aSomeInstanceValue retain];
    [oldValue release];
}
```

这显然比简单的赋值复杂得多。

最突出的地方是占据了这段代码最后三行的奇怪的 `retain`/`release` 舞蹈。我们这样做是为了避免 `aSomeInstanceValue` 和 `someInstance` 指向同一个对象时可能产生的问题。想象一下这种情况：

```objc
- (void)setSomeInstance:(SomeClass *)aSomeInstanceValue
{
    [someInstance release]; // <-- original value is released
    someInstance = [aSomeInstanceValue retain];
}
```

如果 `aSomeInstanceValue` 和 `someInstance` 是同一个对象，那么第一行可能会在第二行 retain 它之前就释放了底层的对象——这意味着当它再次被 retain 时，该对象已经被销毁，变得无效了。

你会注意到我们使用 C 的相等运算符来比较这两个对象，而不是 `isEqual:` 方法。通常，这不是个好主意（Objective-C 对象即使不指向内存中的同一位置，也可能是“相等的”），但在这种情况下，我们特别关心内存位置（以及引用计数）相同的情况。这个比较对于防止过早释放来说并非严格必要（因为 `retain` 发生在 `release` 之前），但它是一种优化和安全措施。

但实际上，写所有这些代码都有点痛苦：比较、烦人的临时变量以及所有东西的仔细排序。在实践中，我们通常使用一个更短的 setter 方法版本，它基本上一样好，而且写起来肯定容易得多：

```objc
- (void)setSomeInstance:(SomeClass *)aSomeInstanceValue
{
    [someInstance autorelease];
    someInstance = [aSomeInstanceValue retain];
}
```

在这种情况下，我们不关心比较优化，而是使用自动释放池（autorelease pool）来临时持有原始值，而不是使用我们自己的栈变量。

这个方法具有与 `retain`/`release` 舞蹈相同的安全性，但需要一个自动释放池，并且在 `someInstance` 和 `aSomeInstanceValue` 实际上是同一个对象时，性能会稍微差一点。实际上，在 Cocoa 应用程序中几乎总是有一个自动释放池，而且性能差异更多是理论上的而不是实际存在的（你很难构造一个能显示出差异的测试程序），除非你开始创建 copy setter（见下文）。

> **并非所有 Objective-C setter 都应该 retain**：在某些情况下，接受 Objective-C 对象的 setter 方法不应该 retain 其参数。具体来说：层次结构中的对象通常不应该 retain 它们的父对象。更多关于此主题的信息，请查看 [避免保留循环的规则](https://www.cocoawithlove.com/2009/07/rules-to-avoid-retain-cycles.html)。

## Retain 访问模式的另一半

实际上，即使你忘记了在访问器方法中进行 `if (newInstance == oldInstance) return;` 检查，即使你真的将当前值传递给了一个 setter 方法，你也极不可能看到问题。

即使你犯了错误，通常也很安全的原因是，你传递给方法的参数通常在其他地方还有一个引用计数被持有。

具体来说：你在栈上访问的大多数对象，都有一个由栈上的自动释放池或堆中某个生命周期更长的对象持有的自动释放的引用计数。

从理论上讲，你可以通过为 retained 对象实现这样的 getter 方法来促进这个思路：

```objc
- (SomeClass *)someInstance
{
    return [[someInstance retain] autorelease];
}
```

这将确保，如果你的对象被这样使用：

```objc
SomeClass *stackInstance = [anObject someInstance];
[anObject release]; // anObject releases its someInstance ivar in its dealloc method
[stackInstance doSomething];
```

那么在 `stackInstance` 上调用 `doSomething` 时，`stackInstance` 变量仍然有效。

不过一般来说，我不在非原子 getter 方法中费心做这个。

为什么不做？速度、冗余和常识。

虽然 retain 然后 autorelease 一个东西并不算巨大的开销，但对于 get 访问器方法来说，通常根本不需要。使用 get 访问器的程序员应该理解，其生命周期与源对象绑定。

但是，在返回值不明显是 getter 方法的情况下，你可能想使用这个模式。例如：

```objc
@implementation ThisClassIsReallyJustAString

- (NSString *)description
{
    return [[internalValue retain] autorelease];
}

@end
```

`description` 方法（返回一个对象的 `NSString` 表示）通常不会直接返回实例变量，所以一般不认为它是一个访问器方法。在这种情况下，它被实现为访问器，但由于期望 description 是一个生成的值，我们需要 retain 和 autorelease 返回的值。

任何从方法中返回的实例变量，如果该方法不显然是访问器方法，都应该总是通过 `retain`/`autorelease`，因为其生命周期与源对象生命周期的绑定关系并不明显。

## Copy 访问器

`retain` 访问器存在的原因很明显——你不希望在值被设置在对象上时它被释放。

Objective-C 中最后一种访问器模式——copy 访问器——存在的原因则不那么广为人知，但仍然很重要。

当 setter 参数可能是可变的（mutable），但你不能让属性的内部状态在无警告的情况下改变时，你应该使用 copy 访问器。考虑下面的例子：

```objc
NSMutableString *mutableString = [NSMutableString stringWithString:@"initial value"];
[someObject setStringValue:mutableString];
[mutableString setString:@"different value"];
```

在这种情况中，如果 `setStringValue:` 方法遵循了 `retain` 模式，那么下一行调用的 `setString:` 方法就会在未通知 `someObject` 的情况下改变这个属性的内部值。

有时，你不关心属性的内部状态是否会在无警告的情况下改变。然而，如果你确实关心属性的内部状态是否会改变，那么你就会想使用 `copy` setter。

非原子 copy setter 的实现如你想象的那么简单：

```objc
- (void)setStringValue:(NSString *)aString
{
    if (stringValue == aString)
    {
        return;
    }
    NSString *oldValue = stringValue;
    stringValue = [aString copy];
    [oldValue release];
}
```

> **更正**：我之前说过 copy 不需要相等比较（因为我错误地声称 `copy` 总会确保你得到一个不同的内存块）。我当然错了。正如评论中立即指出的那样：`copy` 并不总是返回一个拷贝；对于不可变（immutable）对象，`copy` 可以返回**同一个**对象。我忘记了这一点，尽管我确实写过这样工作的 copy setter（参见 [SynthesizeSingleton 代码](https://www.cocoawithlove.com/2008/11/singletons-appdelegates-and-top-level.html)）。结果是，我们仍然需要这个比较来确保将属性设置为相同的值不会引起与之前 retain 模式相同的潜在释放问题。我有没有说过搞砸属性访问器是可能的？

这最终解释了为什么 `NSDictionary` 会拷贝它的键。

`NSDictionary` 将所有值对象存储在与每个对应键对象的 `hash` 方法结果相对应的位置。

如果键对象以一种导致 `hash` 方法结果改变的方式发生了变化，那么 `NSDictionary` 就无法再找到对应的值对象了。

键对象不是通过 `NSDictionary` 上的属性访问器设置的，但效果是一样的：使用 copy 模式是为了确保外部对象不能在无警告的情况下改变字典的内部状态。

当然，遵循 copy 模式的属性的缺点就是速度。对于几 KB 大小的对象来说，这通常不是问题，但超过那个点，你就需要考虑 copy 是否是所涉及资源的正确模式。

## 结论

Getter 和 setter 方法通常被认为是实现起来最简单的方法。但你可以看到，即使是这种非常简单的类型的方法，也存在一些微妙的出错方式。

总的来说，这篇文章比我通常的文章简单得多，但这并不意味着它只适用于初级的 Objective-C 开发者。有经验的程序员也远不能免于在这个领域犯错。Getter 和 setter 方法的一些潜在问题非常罕见，你可能从没见过问题（即使你的代码在做一些不安全的事情），所以在这个领域，从经验中学习可能需要时间。

当然，如果你的访问器方法不需要任何定制，你应该直接使用合成的 `@property` 实现。这将避免引入错误的任何可能性。
