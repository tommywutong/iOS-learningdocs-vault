---
title: 大型数组的 Objective-C 对象备选分配方案 | Cocoa with Love
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/08/alternative-objective-c-object.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:685f9a1d65ba0785'
translated: true
---

> 原文：[Alternative Objective-C object allocation for large arrays | Cocoa with Love](https://www.cocoawithlove.com/2010/08/alternative-objective-c-object.html)　·　Cocoa with Love (Matt Gallagher)

在这篇文章中，我将向你展示如何在不使用标准实例（instance）分配流程（无论是 `+[NSObject alloc]` 还是 `class_createInstance()`）的情况下创建对象。我还会解释你为什么要这样做——自定义对象创建流程的优点和缺点。

## 对象分配简介

在探讨 Objective-C 对象分配时，首先要理解的是：什么是 Objective-C 对象？

答案相当简单：任何以 Objective-C `Class` 指针开头的数据块都可以被视为一个 Objective-C 对象。这个指针通常被称为 `isa` 指针，它使得这块内存可以被用于 Objective-C 的消息发送系统。

通常，Objective-C 对象是在 `+[NSObject alloc]` 或 `class_createInstance()` 的实现内部，通过 `malloc_zone_calloc` 在 malloc 堆上逐个分配的。这些分配方法会在对象分配后自动设置其 `isa` 指针。

## 备选对象分配

由于任何以 `isa` 指针开头的内存块都可以被视为对象，因此实际上有多种分配对象的方式。我将只考虑一种备选方案：malloc 一个大的连续数据块，将这个数据块视为 Objective-C 对象的 C 数组，并手动设置每个对象开头的 `isa` 指针。

这个方法相当简单。第一步，分配 C 数组（使用 `calloc` 以遵循 Objective-C 惯例）：

```objc
const NSInteger arrayLength = /* some array length */;
Class someClass = [SomeClass class];
NSInteger runtimeInstanceSize = class_getInstanceSize(someClass);
char *instanceArray = calloc(
    runtimeInstanceSize,
    arrayLength);
```

注意，我们使用的是实例（instance）的运行时大小，而不是编译时的值。这是因为如果某个超类（superclass）在运行时添加了额外的实例变量（instance variable），实例的大小可能会发生变化（参见我之前的文章 [关于 Dynamic Ivars](https://www.cocoawithlove.com/2010/03/dynamic-ivars-solving-fragile-base.html)）。如果你的类没有超类，或者你足够轻视以至于忽略这种可能性，那么你可以使用固定或编译时的大小值。

一旦数据块分配完成，我们需要设置所有的 `isa` 指针：

```objc
for (NSInteger instanceIndex = 0; instanceIndex < arrayLength; instanceIndex++)
{
    Class *currentInstanceIsa =
        (Class *)(instanceArray + (runtimeInstanceSize * instanceIndex));
    *currentInstanceIsa = someClass;
}
```

然后，如果愿意，你可以调用 `init` 方法或以其他方式初始化每个对象。

## 使用备选分配方案的理由

避免使用标准分配的原因通常是因为 `malloc_zone_calloc` 无法提供所需的内存效率或性能。

我之前已经探讨过 [malloc 在 Mac 上的工作原理](https://www.cocoawithlove.com/2010/05/look-at-how-malloc-works-on-mac.html)。那篇文章简要地提到了 malloc 的两个限制：

- malloc 分配存在“分配粒度”（不是该粒度倍数的对象会导致空间浪费）
- malloc 必须维护已分配对象的元数据，这会带来额外的内存开销

然而，malloc 最大的限制仅仅在于它对每次分配都施加了 per-object 的 CPU 开销。

最后，使用备选分配方案还有一个其他优点：它更底层。这并非在所有情况下都是优点——底层实现可能很繁琐且容易出错。但是，底层的 C 实现更容易与其他底层 C 实现结合，因此如果你的程序大部分已经是底层 C 实现，那么能够低层级地访问对象分配最终可能会成为一个优势。

## 备选对象分配的缺点

不应轻率地使用备选对象分配。首先，它给程序员增加了工作量，因此你需要确保付出的努力是值得的。

但它带来的最大问题是，单个对象无法在其所分配的更大数据块的生命周期之外被保留。为了解决这个问题，你必须要么

- 让包含这些对象的数据块具有全局生命周期（永不释放），例如单例或其他永久实例（instance）
- 仔细管理所有的 retain 和 release，以确保没有对象在包含它的数据块生命周期之外被保留
- 禁止 retain（使用一个会抛出异常的 retain 实现）。

只有当效率优势显著时，这种限制才是合理的。在 iPhone 上，对于数万个对象可能值得这么做；但在 Mac 上，你的数据块应该包含数十万个对象才值得费心。

## 一个例子：加载 "/usr/share/dict/words" 文件

为了说明如何使用备选分配，我将展示一个传统的 Objective-C 方法，用于将 "/usr/share/dict/words" 文件的内容读取、解析并存储为 `NSString` 数组。我将比较这种方法与备选分配方法所花费的时间和内存。

传统的 Objective-C 方法：

```objc
words = [[NSString
        stringWithContentsOfFile:@"/usr/share/dict/words"
        encoding:NSASCIIStringEncoding
        error:NULL]
    arrayBySeparatingIntoParagraphs];
```

这里的 `arrayBySeparatingIntoParagraphs` 是一个 `NSString` 分类（category）方法，它使用 `getParagraphStart:end:contentsEnd:forRange:` 将 `NSString` 分割成行。

备选方法使用自定义的 `NSString` 类，如上面“备选对象分配”部分所述进行分配。这个 `NSString` 存储一个固定长度为 24 字符的 ASCII 字符串（24 个字符是 words 文件中一行的最大长度）。字符串存储实际上不是一个 C 字符串；如果存储的字符串长度为 24 个字符，则没有空终止符。

```objc
@interface CustomAsciiString : NSString
{
    char value[CUSTOM_ASCII_STRING_LENGTH];
}
@end
```

分配本身发生在自定义 NSArray 子类（subclass）的 init 方法中。

```objc
@interface CustomAsciiStringArray : NSArray
{
    NSInteger count;
    char *stringArray;
}
@end
```

这个自定义数组子类用于提供与 `NSArray` 兼容的访问方式，以访问 `CustomAsciiString` 的 C 数组。

`CustomAsciiString` 的数组在这里实际上被引用为 `char*`，因为在编译时我们无法预知 `CustomAsciiString` 的分配大小，所以我们需要按字节（即 `char`）偏移来索引数组。

所有相关代码篇幅太长，无法在此包含，但你可以下载 [CustomObjectCreation.zip](https://www.cocoawithlove.com/assets/objc-era/CustomObjectCreation.zip) 获取完整代码。

## 结果

字典中共有 234936 个单词，最长 24 个字符，平均长度 9.6 个字符。

“传统” Objective-C 方法将文件加载、解析并存储到字符串数组 20 次，耗时 3.12 秒。最终迭代后的内存使用量（所有其他迭代均已释放）为 16.5 MB。

“备选分配”方法将文件加载、解析并存储到字符串数组 20 次，耗时 0.49 秒。最终迭代后的内存使用量为 8 MB。

最终结果：速度快了 6 倍，内存只用了一半。

## 这些数字背后方法论的潜在问题

基于这些数字，“备选分配”似乎速度快了 6 倍多，内存效率提高了 2 倍多。

然而，这并不是一个“同类比较”。

“备选分配”方法存储的是 ASCII 字符串（每个字符的大小是典型 `unichar` `NSString` 的一半）。然而，这很大程度上被以下事实所抵消：每个 ASCII 字符串的长度都是 24 个字符——这显著超过了字符串平均长度的两倍，因此这里分配的有效内存实际上更大。即使你将 ASCII 字符串长度加倍到 48 个字符，内存使用量也仅为 13.4 MB——仍然比传统分配方法少 20%。此外，“备选分配”方法还分配了一个固定的 250000 条目的数组（尽管只使用了 234936 个）。

每种方法使用的解析逻辑也截然不同。然而，这与我之前的陈述有关：底层分配有利于与底层解析和处理相结合。我没有试图使两种方法的解析更具可比性，因为我相信不同的解析方法与不同的分配方法是正确匹配的。

我本希望更好地解决的最大问题——但我真的不知道如何做——是简单地通过 `getrusage` 读取内存使用量并不是一种高度精确的方法来确定测试所使用的内存。`getrusage` 的结果会统计所有已分配的内存页面，无论它们是否真正在使用中。它也无法区分可能被运行时用于不同目的而分配的内存。由于测量内存的困难，我不得不假设 `getrusage` 是足够的，但数字中肯定存在误差范围。

## 结论

> 你可以下载 [CustomObjectCreation.zip](https://www.cocoawithlove.com/assets/objc-era/CustomObjectCreation.zip)（20kB），其中包含本文测试项目中使用的所有代码。

对于非常大的 Objective-C 对象数组，将它们自行分配到 C 风格的数组中肯定会更高效。它更快（大约快 6 倍）且内存效率更高（内存使用量降低 20% 到 60%）。

然而，你不应该对所有数组都这样做。这会引入大量额外代码——其中的任何部分都可能带来问题——并且会引入对象生命周期问题。但对于非常大的数组，其优势（尤其是在 CPU 或内存受限的场景下）可能值得付出这样的努力。
