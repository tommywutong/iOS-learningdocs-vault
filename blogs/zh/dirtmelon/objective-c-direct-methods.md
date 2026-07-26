---
title: Objective-C Direct Methods
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/objective-c-direct-methods/'
original_language: zh
published: 2021-06-22
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c2703b9f26c5d04b'
translated: n/a
---

> 原文：[Objective-C Direct Methods](https://dirtmelon.github.io/posts/objective-c-direct-methods/)　·　dirtmelon

## Objective-C Direct Methods

[Clang 13 documentation](https://clang.llvm.org/docs/AttributeReference.html#objc-direct)

commit :

[Implement **attribute**((objc_direct)), **attribute**((objc_direct_me… · llvm/llvm-project@d4e1ba3](https://github.com/llvm/llvm-project/commit/d4e1ba3fa9dfec2613bdcc7db0b58dea490c56b1)

Clang 13 新增了 `objc_direct` 声明，对应的 Xcode 版本为 12 。使用 `objc_direct` 标记的 Objective-C 方法为直接派发方法。 `direct` 方法在调用时类似于静态方法，降低了一定的性能损耗，但是也牺牲了 Objective-C 的一些特性。

`direct` 方法的消息发送会像 C 函数那样直接调用实现，没有走 Objective-C 的消息发送流程。这里速度会比较快和有可能进行函数内联，这同时意味着方法不能够被重写或者动态替换。因此 `direct` 方法不会出现在 `class` 的方法列表中，可以减少代码段的大小。虽然说 `direct` 方法会当做 C 函数来进行静态调用，但是它仍然遵循以下 Objective-C 语义：

- 如果接收者为 `nil` ，则不会进行任何处理和返回方法返回值中对应的 `zero` 值；
- 调用 `direct` 方法也会触发 `class` 的初始化，包括调用 `+initiablize` 方法；
- 保留方法选择器的隐式参数 `_cmd` ，但是如果 `_cmd` 参数没有在方法中进行调用，那么实现中将不会保留对 `_cmd` 的引用，以减少代码段的大小。

同时不支持以下操作：

- 在 `protocol` 中声明 `direct` 方法；
- 在子类重写 `direct` 方法；
- 在子类中重写非 `direct` 方法，同时定义为 `direct` ；
- 相同的方法在不同的类接口中对 `direct` 的声明不一致；
- 在 `interface` 和 `implement` 中对 `direct` 的声明不一致；
- 不可以通过 `@selector` 和方法名来获取 `direct` 方法的 `SEL` 。

`class` 的 `interface` 包括了 `class` 的 `@interface` block ，extensions ， categories ，protocol 和父类的 `interface` 。

Objective-C 属性也支持声明为 `direct` 属性，在没有显示声明 `getter` 和 `setter` 的前提下，会默认声明为 `direct` 。

如果需要批量声明，可以使用 `objc_direct_members` 声明。可以在 `@interface` 或者 `@implementation` 中进行声明，对应的 `.m` 中的方法都会被设为 `direct` 。当 `objc_direct_members` 放置在 `@interface` 时，只有出现在 `@interface` 的方法会设置为 `direct` ，这包括了属性的隐式方法声明。

如果在 `@implementation` 中进行声明，除了已在其它 `@interface` 声明为 `non-direct` 的方法，其它方法都会声明为 `direct` 。

如果没办法保证外部调用会如何处理方法，那么比较保守的策略就是只处理 `.m` 里的私有方法和属性。

[Pierre H. 🔥🌸 on Twitter: “About objc_direct, a thread.I should have probably anticipated that people would raise eyebrows and spent more time explaining the point in the LLVM commit, so here it is… https://t.co/zgnaKD6n4A / Twitter”](https://twitter.com/pedantcoder/status/1197269246289444864)

这条推下面详细说明了 Objective-C 消息发送机制带来的损耗，主要包括以下四方面：

- 代码段大小，由于需要查找方法指针 `IMP` ，所以需要传递 `sekf` 和 `_cmd` 参数。每次调用会带来额外 8 字节的消耗，由于 `objc_msgSend` 的调用非常频繁，所以 8 字节叠加后占比非常大。在 CloudKit 中，这两个指令占了 `__text` 段 10.7% 的大小；
- 优化阻碍，为了更强的动态性和 ARC 等特性， Objective-C 要求编译器做出巨大的保护性编程。拒绝内联是比较明显的一个问题，还有的是在获取可读的 `integer` 属性时也会带来影响，ARC 会插入 `objc_retain()/objc_releas()` 方法包围属性的 `getter` 方法；
- 静态元数据，每个 Objective-C 的方法都会增加 150-250 字节大小。

    - 类的方法列表中会增加 24 字节；
    - 方法的 `type` 字符串超过 60 字节，如果不使用 `NSInvocation` 则没有不需要该字符串；
    - 方法的选择器平均为 20+ 字节。
- 运行时元数据，为了加快消息发送的速度，运行时会创建 `IMP` 缓存，即使是一些只调用一次的方法，也会带进程带来负担，同时由于运行时初始化时需要重定位指针，也会对启动性能带来影响。

[Objective-C Direct Methods](https://nshipster.com/direct/)

大多数情况下， `direct` 方法其实不会带来明显的性能收益， `objc_msgSend` 的处理速度其实非常快，这得益于极其侵略的缓存策略，广泛的底层优化以及现代处理器的进步。在存量代码比较多的情况下，把方法改写为 `direct` 会减少一定的代码段大小。

[Direct Calls with Objective-C](https://pspdfkit.com/blog/2020/improving-performance-via-objc-direct/)

性能相关数据：

PSPDFKit 替换了 3717 个方法，减少了 700 KB ，平均每个方法减少了 200 字节。

建议只在内部属性或者方法中使用，在公开的属性或者方法中使用时，如果有新开启 `direct` ，上层有调用相关接口的二进制库都需要重新编译。†
