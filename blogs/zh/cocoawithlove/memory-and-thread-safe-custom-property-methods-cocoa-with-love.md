---
title: '自定义属性方法：内存与线程安全 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/10/memory-and-thread-safe-custom-property.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:aa9079f6824c40ea'
translated: true
---

> 原文：[Memory and thread-safe custom property methods | Cocoa with Love](https://www.cocoawithlove.com/2009/10/memory-and-thread-safe-custom-property.html)　·　Cocoa with Love (Matt Gallagher)

Objective-2.0 的属性（property）方法虽便捷，但若需重写属性（property）的实现——尤其是原子（atomic）、retain 或 copy 的对象型 setter 属性——若未严格遵循规则，可能会引入一些潜在的 bug。我会展示这些陷阱以及正确实现属性访问方法的方式。我还会展示一种直接调用隐藏运行时（runtime）函数的方法，让 Objective-C 为你安全地进行原子 get 和 set 操作。

## 隐式原子类型的自定义 getter 和 setter 方法

对于隐式原子类型，或无需内存管理的类型，Objective-C 中的自定义 getter 和 setter 方法非常简单。这些“简单”的情况包括：

- 基本值类型（`char`、`short`、`int`、`float`、`long`、`double` 等）。
- 在垃圾回收（garbage collected）环境中的 Objective-C 对象
- 赋值（assign，非 retain）指针

对于这些类型，自定义 getter 或 setter 方法很难出错。对于下列属性声明：

```objc
@property SomeAtomicType somePropertyVariable;
```

自定义的 getter 和 setter 只需写成这样：

```objc
- (SomeAtomicType)somePropertyVariable
{
    return somePropertyVariable;
}
- (void)setSomePropertyVariable:(SomeAtomicType)aValue
{
    somePropertyVariable = aValue;
}
```

## 非原子类型访问方法中的常见错误

非原子类型需要更谨慎。这些类型包括：

- 在手动管理内存（manually managed memory）环境中的 Objective-C 对象
- `struct` 及其他复合类型（compound type）

鉴于为原子类型编写自定义 getter 和 setter 方法如此简单，容易让人对这些类型的实现掉以轻心。然而，采用错误的方式可能会导致内存崩溃 bug，并缺乏适当的线程安全（thread safety）。

为了说明实现自定义 setter 方法时多么容易引入 bug，请看下面的属性声明：

```objc
@property NSString (copy) someString;
```

一个草率的 setter 实现可能是：

```objc
- (void)setSomeString:(NSString *)aString
{
    [someString release];
    someString = [aString copy];
}
```

这个实现实际上包含了两个 bug：

1. **此方法不是原子的**。
   `someString` 对象发生了两次改变：一次在 `release` 时，另一次在它被赋值为 copy 后对象的地址时。此方法 _不是_ 原子的，从而违背了声明（该声明省略了 `nonatomic` 关键字，因此要求原子性（atomicity））。
2. **赋值操作中包含潜在的内存释放 bug。**
   如果 `someString` 曾将自己赋值为自己，它会在 `copy` 之前 `release` 自身，导致可能使用一个已被 `release` 的变量。代码：`self.someString = someString;` 就是这种潜在问题的一个例子。

如果你曾经犯过这些错误，不必过于自责。在为本文做研究时，我花了一些时间查看 [clang](http://clang.llvm.org/) 合成的（synthesized）方法实现，并注意到[他们在需要原子方式（atomic manner）处理 struct 访问方法时，忘了这么做](http://llvm.org/svn/llvm-project/cfe/trunk/lib/CodeGen/CGObjC.cpp)。

## 非原子类型自定义访问方法的安全实现

为了解决第二个问题，[Apple 的 Declared Properties 文档](http://developer.apple.com/mac/library/documentation/Cocoa/Conceptual/ObjectiveC/Articles/ocProperties.html)建议你的 setter 方法应该像这样：

```objc
- (void)setSomeString:(NSString *)aString
{
    if (someString != aString)
    {
        [someString release];
        someString = [aString copy];
    }
}
```

这仅修复了内存问题，并未修复原子性问题。要处理原子性问题，唯一简单的方案是使用 `@synchronized` 区域：

```objc
- (void)setSomeString:(NSString *)aString
{
    @synchronized(self)
    {
        if (someString != aString)
        {
            [someString release];
            someString = [aString copy];
        }
    }
}
```

这种方法也适用于 `retain` 属性（只需将 `copy` 方法替换为 `retain`）。

为保持原子性，你还需要在 getter 方法中使用 `retain/autorelease` 模式并加锁：

```objc
- (NSString *)someString
{
    @synchronized(self)
    {
        id result = [someString retain];
    }
    return [result autorelease];
}
```

`@synchronized` 区域只需包裹 `retain` 操作，因为在它返回结果之前能阻止 setter 释放该值（`autorelease` 随后可在区域外安全进行）。

对于 `struct` 和其他复合数据类型，我们不需要 `retain` 或 `copy`，因此只需 `@synchronized` 区域：

```objc
- (NSRect)someRect
{
    @synchronized(self)
    {
        return someRect;
    }
}
- (void)setSomeRect:(NSRect)aRect
{
    @synchronized(self)
    {
        someRect = aRect;
    }
}
```

## 实现自定义访问方法的更快、更简短方式

上面列出的自定义访问方法有两个缺点：

- 需要精确编码以避免 bug。
- 在 `self` 上加 `@synchronized` 区域是粗粒度的（coarse-grained）且缓慢。

还有另一种实现这些方法的方式，不需要那么多谨慎的编码，并且使用更高效的锁：使用与 `synthesized` 方法相同的函数。

以下函数在 Objective-C 运行时中实现：

```objc
id objc_getProperty(id self, SEL _cmd, ptrdiff_t offset, BOOL atomic);
void objc_setProperty(id self, SEL _cmd, ptrdiff_t offset, id newValue, BOOL atomic,
    BOOL shouldCopy);
void objc_copyStruct(void *dest, const void *src, ptrdiff_t size, BOOL atomic,
    BOOL hasStrong);
```

虽然这些函数在运行时中实现了，但它们并未被声明，因此如果你想使用它们，必须自己声明（编译器随后会在编译时找到它们的定义）。

这些方法比在整个对象上使用 `@synchronized` 区域要快得多，因为（如其 [Apple 开源实现](http://www.opensource.apple.com/source/objc4/objc4-371.2/runtime/Accessors.subproj/objc-accessors.m)所示）它们使用细粒度的、仅针对实例变量（instance variable）的自旋锁（spin lock）来处理并发访问（不过 `objc_copyStruct` 函数由于界面设计上的混淆，使用了两个锁）。

声明这些函数后，你还可以声明以下便捷宏（macro）：

```objc
#define AtomicRetainedSetToFrom(dest, source) \
    objc_setProperty(self, _cmd, (ptrdiff_t)(&dest) - (ptrdiff_t)(self), source, YES, NO)
#define AtomicCopiedSetToFrom(dest, source) \
    objc_setProperty(self, _cmd, (ptrdiff_t)(&dest) - (ptrdiff_t)(self), source, YES, YES)
#define AtomicAutoreleasedGet(source) \
    objc_getProperty(self, _cmd, (ptrdiff_t)(&source) - (ptrdiff_t)(self), YES)
#define AtomicStructToFrom(dest, source) \
    objc_copyStruct(&dest, &source, sizeof(__typeof__(source)), YES, NO)
```

我喜欢包含 "To/From" 字样，以便记住 source 和 destination 参数的顺序。如果它们让你困扰，可以去掉。

使用这些宏，上面 `someString` 的 "copy" getter 和 setter 方法将变成：

```objc
- (NSString *)someString
{
    return AtomicAutoreleasedGet(someString);
}
- (void)setSomeString:(NSString *)aString
{
    AtomicCopiedSetToFrom(someString, aString);
}
```

而上面展示的 `someRect` 访问方法将变成：

```objc
- (NSRect)someRect
{
    NSRect result;
    AtomicStructToFrom(result, someRect);
    return result;
}
- (void)setSomeRect:(NSRect)aRect
{
    AtomicStructToFrom(someRect, aRect);
}
```

## 总结

我在这里展示的大多数访问方法都是原子的，但现实中，大多数 Objective-C 对象的访问方法被声明为 `nonatomic`。

即使你的属性被声明为 `nonatomic`，内存管理规则仍然适用。这些规则很重要，必须遵守，因为违反它们可能导致一些非常隐蔽且难以追踪的内存 bug。

我提供的宏都是针对原子属性的。对于非原子属性，样板赋值代码可能简单到足以记住。如果不确定，你也可以使用宏：

```objc
#define NonatomicRetainedSetToFrom(a, b) do{if(a!=b){[a release];a=[b retain];}}while(0)
#define NonatomicCopySetToFrom(a, b) do{if(a!=b){[a release];a=[b copy];}}while(0)
```

**更新：** 根据下面的评论，我意识到我未限定这些访问方法在何种情况下是线程安全的（thread-safe）。具体来说：

1. 这些 setter 方法仅在传递给它们的参数是不可变（immutable）时才是线程安全的。对于可变参数，你可能需要确保参数上的修改操作与属性的赋值操作之间的线程安全。
2. 原子访问方法仅在它们是访问实例变量的唯一方式时，才能为实例变量提供线程安全。如果需要非属性方式的访问，你必须确保属性访问方法与非属性访问方式之间的共享线程安全。
3. 对于我列出的“隐式原子”类型，原子赋值并不意味所有的 CPU/核心看到的是相同的内容（因为每个 CPU/核心可能有自己的值缓存）——它仅确保该值被完整设置，没有中断的可能。如果你需要所有 CPU/核心在特定时刻同步并看到相同的值，那么即使是“隐式原子”类型也可能需要 `volatile` 限定符，或者在赋值操作周围使用 `@synchronized` 区域来刷新缓存。
