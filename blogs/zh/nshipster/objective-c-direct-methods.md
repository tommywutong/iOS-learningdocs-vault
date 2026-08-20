---
title: Objective-C 直接方法
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/direct/'
original_language: en
published: 2019-12-16
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:e187e6c924ca6a42'
translated: true
---

> 原文：[Objective-C Direct Methods](https://nshipster.com/direct/)　·　NSHipster (Mattt)

# [Objective-C Direct Methods](https://nshipster.com/direct/)

作者：[Mattt](https://nshipster.com/authors/mattt/)　2019 年 12 月 16 日

当 Objective-C 迎来新特性时，很难让人兴奋起来。如今，这类改进都是为了服务 Swift 互操作性（interoperability），而不是对语言本身的投入（可见 [nullability](https://developer.apple.com/swift/blog/?id=25) 和 [lightweight generics](https://developer.apple.com/documentation/swift/imported_c_and_objective-c_apis/using_imported_lightweight_generics_in_swift)）。

因此，当得知 [Clang 近期合入的一个补丁](https://reviews.llvm.org/D69991)为 Objective-C 方法增加了直接派发（direct dispatch）机制时，还是令人惊讶的。

这一语言新特性的起源尚不清楚；我们唯一能依据的是一个 Apple 内部的 [Radar 编号](https://nshipster.com/bug-reporting/)（[`2684889`](rdar://2684889)），除了它的年代相对久远（根据我们的估计，大约在本世纪初）之外，并没有告诉我们太多信息。幸运的是，该特性[已落地](https://github.com/llvm/llvm-project/commit/d4e1ba3fa9dfec2613bdcc7db0b58dea490c56b1)，并附带了足够的文档和测试覆盖，足以让我们很好地了解其工作原理。（感谢实现者 Pierre Habouzit、审核经理 John McCall 以及其他 LLVM 贡献者）。

本周的 NSHipster，我们将借此机会回顾 Objective-C 的方法派发（method dispatching），并尝试理解这一语言新特性对未来代码库的潜在影响。

---

要理解直接方法（direct methods）的意义，你需要了解一些关于 Objective-C 运行时（runtime）的知识。但让我们在讨论开始之前先退一步，追溯到面向对象编程（OOP）本身的起源：

## 面向对象编程

Alan Kay 在 1960 年代末创造了术语“面向对象编程”。在 Adele Goldberg、Dan Ingalls 以及他在 Xerox PARC 的其他同事的帮助下，Kay 在 70 年代通过创建 Smalltalk 编程语言将这一想法付诸实践。

在 80 年代，Brad Cox 和 Tom Love 开始着手开发 Objective-C 的第一个版本，这是一种旨在将 Smalltalk 的面向对象范式（paradigm）实现在 C 语言的坚实基础上。通过 90 年代一系列偶然的事件，这门语言最终成为了 NeXT 的官方语言，后来又成为了 Apple 的官方语言。

对于我们这些在 iPhone 时代开始学习 Objective-C 的人来说，这门语言常常被视为另一种 Apple 专有技术——是该公司[“非我发明”](https://en.wikipedia.org/wiki/Not_invented_here)（NIH）文化产生的无数晦涩副产品之一。然而，Objective-C 不仅仅是“一种面向对象的 C”，它是最原始的面向对象语言之一，在 OOP 血脉上与任何其他语言同样纯正。

那么，OOP 意味着什么？这是个好问题。90 年代的炒作周期已经使得这个术语几乎毫无意义。然而，就我们今天的目的而言，让我们聚焦于 Alan Kay 在 1998 年写下的一段话：

> 我很抱歉很久以前为这个主题创造了“对象”一词，因为它让很多人关注了次要的概念。主要的概念是“消息传递”……\> [Alan Kay](https://wiki.c2.com/?AlanKayOnMessaging)

## 动态派发与 Objective-C Runtime

在 Objective-C 中，程序由一组通过传递消息来相互交互的对象组成，消息进而调用方法或函数。这种消息传递的动作由方括号语法表示：

```
[someObject aMethod:withAnArgument];
```

当 Objective-C 代码被编译时，消息发送被转换为对一个名为 [`objc_msgSend`](https://developer.apple.com/documentation/objectivec/1456712-objc_msgsend) 的函数的调用（字面意思是“向某个对象发送一条带参数的消息”）。

```
objc_msgSend(object, @selector(message), withAnArgument);
```

- 第一个参数是接收者（receiver）（对于实例方法（instance method）是 `self`）
- 第二个参数是 `_cmd`：选择器（selector），即方法的名称
- 任何方法参数都作为附加的函数参数传递

`objc_msgSend` 负责确定调用哪个底层实现（implementation）来响应此消息，这一过程称为方法派发（method dispatch）。

在 Objective-C 中，每个类（`Class`）维护一个派发表（dispatch table）来解析运行时发送的消息。派发表中的每个条目都是一个方法（`Method`），它将选择器（`SEL`）与对应的实现（`IMP`）关联起来，`IMP` 是一个指向 C 函数的指针。当一个对象收到一条消息时，它会查询其类的派发表。如果能够找到该选择器的实现，则调用关联的函数。否则，该对象会查询其超类（superclass）的派发表。这个过程沿着继承链一直向上，直到找到匹配项，或者根类（`NSObject`）判定该选择器无法识别。

如果你认为所有这些间接层听起来工作量很大……从某种意义上说，你是对的！

如果你的代码中有一条热路径（hot path），一个被频繁调用的开销较大的方法，你可以想象避免所有这些间接层会带来一些好处。为此，一些开发者使用 C 函数来绕过动态派发。

## 使用 C 函数的直接派发

正如我们在 `objc_msgSend` 中看到的，任何方法调用都可以通过将隐式的 `self` 作为第一个参数传递，用等效的函数来表示。

例如，考虑以下带有传统动态派发方法的 Objective-C 类的声明。

```
@interface MyClass: NSObject
- (void)dynamicMethod;
@end
```

如果开发者想要在 `MyClass` 上实现某些功能，而不经过整套消息发送流程，他们可以声明一个以 `MyClass` 实例作为参数的静态 C 函数。

```
static void directFunction(MyClass *__unsafe_unretained object);
```

以下展示了每种方法在调用点的表现形式：

```
MyClass *object = [[[MyClass] alloc] init];

// 动态派发
[object dynamicMethod];

// 直接派发
directFunction(object);
```

## 直接方法

直接方法具有传统方法的外观和感觉，但行为类似于 C 函数。当直接方法被调用时，它会直接调用其底层实现，而不经过 `objc_msgSend`。

借助这个新的 LLVM 补丁，你现在有一种方法可以注解（annotate）Objective-C 方法，选择性地避免参与动态派发。

### objc_direct、@property(direct) 和 objc_direct_members

要使一个实例方法（instance method）或类方法（class method）变为直接方法，你可以使用 `objc_direct` [Clang 特性（attribute）](https://nshipster.com/__attribute__/)来标记它。同样，Objective-C 属性（property）的方法可以通过使用 `direct` 属性特性来声明为直接方法。

```
@interface MyClass: NSObject
@property(nonatomic) BOOL dynamicProperty;
@property(nonatomic, direct) BOOL directProperty;

- (void)dynamicMethod;
- (void)directMethod __attribute__((objc_direct));
@end
```

当一个分类（category）或类扩展（class extension）的 `@interface` 被注解为 `objc_direct_members` 特性时，其中包含的所有方法和属性声明都被视为直接方法，除非之前已被该类声明过。

```
__attribute__((objc_direct_members))
@interface MyClass ()
@property (nonatomic) BOOL directExtensionProperty;
- (void)directExtensionMethod;
@end
```

用 `objc_direct_members` 注解 `@implementation` 有类似的效果，会导致之前未声明的成员被视为直接方法，包括属性合成（property synthesis）产生的隐式方法。

```
__attribute__((objc_direct_members))
@implementation MyClass
- (BOOL)directProperty {…}
- (void)dynamicMethod {…}
- (void)directMethod {…}
- (void)directExtensionMethod {…}
- (void)directImplementationMethod {…}
@end
```

将这些注解应用到我们之前的例子中，我们可以看到直接方法和动态方法在调用点上是无法区分的：

```
MyClass *object = [[[MyClass] alloc] init];

// 动态派发
[object dynamicMethod];

// 直接派发
[object directMethod];
```

---

对于我们这些注重性能的开发者来说，直接方法似乎是一个绝对好用的特性。但这里有个转折：

**在大多数情况下，将方法设为直接方法可能不会有明显的性能优势。**

事实证明，[`objc_msgSend` 快得出奇](https://www.mikeash.com/pyblog/friday-qa-2016-04-15-performance-comparisons-of-common-operations-2016-edition.html)。得益于激进的缓存、广泛的底层优化以及现代处理器的内在性能特性，`objc_msgSend` 的开销极低。

我们早已过了 iPhone 硬件可以被合理描述为资源受限环境的时代。因此，除非 Apple 正在准备一个新的嵌入式平台（_[AR 眼镜，有人吗？](http://appleinsider.com/articles/17/01/09/rumor-apple-working-with-carl-zeiss-on-ar-glasses-to-debut-in-2018)_），否则对于 Apple 在 2019 年实现 Objective-C 直接方法的最合理解释，源于性能之外的其他因素。

## 隐藏动机

当一个 Objective-C 方法被标记为直接方法时，它的实现具有隐藏的可见性（hidden visibility）。也就是说，直接方法只能在同一个模块（module）内被调用（_说得严谨些，是[链接单元（linkage unit）](https://clang.llvm.org/docs/LTOVisibility.html)）。它甚至不会出现在 Objective-C 运行时（runtime）中。

隐藏的可见性有两个直接优势：

- 更小的二进制体积
- 无法从外部调用

由于没有外部可见性，也无法通过 Objective-C 运行时（runtime）动态调用它们，因此直接方法本质上是私有方法（private methods）。

虽然隐藏的可见性可以被 Apple 用来防止方法调配（swizzling）和私有 API 的使用，但这似乎不是主要动机。

[据实现该特性的 Pierre 所说](https://twitter.com/pedantcoder/status/1197269246289444864)，这种优化的主要好处是代码体积的减小。据报道，未使用的 Objective-C 元数据（metadata）的重量可能占编译后二进制文件 `__text` 段的 5 – 10%。

---

你可以想象，从现在到明年的开发者大会，几位工程师可能会遍历 SDK 框架中的每一个，将私有方法注解为 `objc_direct`，将私有类注解为 `objc_direct_members`，作为一种渐进式收紧其 SDK 的轻量级方法。

如果这是真的，那么我们对新的 Objective-C 特性持怀疑态度也许正好。当它们不是为了服务 Swift 时，就是为了服务 Apple。尽管 Objective-C 在编程史和 Apple 自身中占有重要地位，但我们很难不将其视为——历史。
