---
title: Swift 中的运行时多态
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2024/04/Run-time-Polymorphism-in-Swift/'
original_language: en
published: 2024-04-06
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9937df14dd40ba8a'
translated: true
---

> 原文：[Run-time Polymorphism in Swift](https://belkadan.com/blog/2024/04/Run-time-Polymorphism-in-Swift/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Online Communication](https://belkadan.com/blog/2024/01/Online-Communication/)

[XZ Gon' Give It To Ya](https://belkadan.com/blog/2024/04/XZ-Gon-Give-It-To-Ya/) »

« [GitMounter](https://belkadan.com/blog/2023/11/GitMounter/?tag=swift)

« [Default Arguments and Label-based Overloading](https://belkadan.com/blog/2022/04/Default-Arguments-and-Label-based-Overloading/?tag=programming-languages)

## [Run-time Polymorphism in Swift](#)

这些年在论坛上被问过好几次了，但我一直没有正式写下来，所以这次就写一篇：**在 Swift 里获得运行时多态（run-time polymorphism）只有三种方式。**嗯，三种半。

我说的*运行时多态*是什么意思？我指的是一次函数/方法调用（或者变量、下标访问），在每次调用发生时都（有可能）执行不同的代码。这跟绝大多数其他函数调用形成对比：当你调用 Array 的 `append` 时，被调用的永远是同一个方法。

那么，获得这种行为的三种、抱歉，三种半方式是什么？

- [调用一个函数值](#calling-a-function-value)（闭包）
- [调用一个类成员](#calling-a-class-member)
- [调用一个协议要求](#calling-a-protocol-requirement)
- [手动测试一个值的类型](#manually-testing-the-type-of-a-value)

### 调用一个函数值

这一种算是很显然的。如果你在调用一个回调，它可以是任何匹配该函数类型的东西，取决于它来自哪里。

### 调用一个类成员

非 `final` 类上的非 `final` 方法可能在子类中被重写，所以调用类方法会基于 `self` 的运行时类型做动态派发。这是最为人熟知的、面向对象意义上的「多态」，通常不会让人觉得意外。

注意「类方法」这个说法有点含糊：这条规则同时适用于实例方法和类型级方法（以及属性、下标、`required` 初始化方法）。不过在类里，`static` 等价于 `class` 加 `final`，所以这种情况下不会有任何动态派发。

实际上还有一个类成员被动态派发的地方，就是便利初始化方法这个非常特殊的场景。便利初始化方法*内部*对 `self.init` 的调用是动态派发的，这也是为什么便利初始化方法只有在你提供了超类所有非便利初始化方法时才会被继承。这是一个从 Objective-C 里的模式变成 Swift 语言特性的例子，说实话，[也许它带来的复杂度超出了我们真正需要的程度](https://github.com/apple/swift/blob/swift-5.10-RELEASE/docs/InitializerProblems.rst)。

### 调用一个协议要求

这一种也不算太意外；毕竟协议存在的全部意义就是提供一套由具体类型实现的通用 API。可能让人意外的是，在协议的扩展中添加的成员*不会*参与这种行为。仔细想想的话，支持这一点就意味着*在运行时*程序必须查看某个具体类型可能拥有的所有方法，看看有没有哪个匹配这个扩展方法。如果匹配了不止一个，运行时系统就得执行*重载决议*。而如果结果是有歧义的呢？所以答案是不行，扩展方法要么在编译期被直接选中，要么在编译期被直接跳过；它们会不会被调用完全由静态类型信息决定，而不是运行时多态。

### 手动测试一个值的类型

这一种其实不太能算数，但把它列在这里是因为有时候它确实是解决问题的最佳答案。Swift 并不提供完美的[参数化多态性（parametricity）](https://www.seas.upenn.edu/~cis1940/spring13/lectures/05-type-classes.html)；你随时可以用 `is` 和 `as?` 表达式，或者 `is` 和 `as` 模式，尝试向下转换/转换成更具体的类型：

```
if firstPet is Cat, let secondPet = secondPet as? Dog { /* … */ }
```

```
switch thirdPet {
case is Cat:
  /* … */
case let thirdPet as Dog:
  /* … */
default:
  break
}
```

这样做是不是个好主意，一部分取决于权衡取舍，一部分取决于品味，但 Swift 确实允许这么做。

### 题外话：泛型呢？

泛型是个强大而灵活的工具，但一般来说，它们带来的运行时多态并不比 `any` 类型（曾经叫「协议组合类型」）更多。这经常会把习惯了 C++ 模板的人搞糊涂，因为在 C++ 里，重载决议是基于满足泛型约束的*具体*类型来做的，而不是基于*泛型*类型本身。Swift 没有选择那个方案，主要有两个原因：一是这会让在编译期诊断问题变得困难得多；二是这意味着泛型的整个函数体都必须对调用者可见（这样它们才能把具体类型代入进去）。这对优化有利，但对库的演进不利。你可以把 Swift 的模型理解成「调用哪个重载，是根据调用点所在位置已知的信息来决定的，而在这个例子里，调用点是在一个带有特定约束的泛型函数内部」。

我不知道有哪些其他现代语言拥有像 C++ 那样的模板，但在*单态化（monomorphization）*——也就是为每个具体类型生成一份单独的代码副本——和*多态（polymorphic）*泛型——也就是用单一份代码通过动态派发来处理多种不同类型——之间，仍然存在一个选择。^[1](#fn:optimizer) 不同语言在这个问题上采取了不同的做法：

| 语言 | 泛型是… | 泛型类型是… | 重载决议基于… |
|---|---|---|---|
| C++ | 单态化的 | 展开成具体类型 | 具体类型（所以叫「模板」） |
| Rust | 单态化的 | 展开成具体类型 | 约束 |
| Swift | 多态的 | 展开成具体类型（但有时是间接的） | 约束 |
| Java | 多态的 | 被「擦除」为其约束 | 约束 |
| Objective-C | 多态的 | 被「擦除」为其约束 | 何谓重载^[2](#fn:objc) |

现在（在 Swift 和 Rust 里）确实*有*办法获得类似 C++ 的行为：宏。但 Swift 的宏*完全*是句法层面的，而且必须显式调用，所以它们并不天然适合像 C++ 模板那样的用法，至少目前还不行。所以有时候这就是「3.5」这个解法登场的地方：在泛型方法体内做一次动态转换，起到某种「特化」的作用，尽管它确实会带来运行时的检查开销。

### 要点回顾

那么让我再重申一遍：开头列出的三种半特性，是 Swift 里*唯一*的运行时多态形式。现在如果有人问「我怎样才能让任意不同的参数类型产生不同的行为」，你就知道答案了：写一个协议。（或者，如果它们已经在你拥有的类层次结构里，就借助基类。）如果有人问「为什么这次方法调用没有选中更特化的那个重载」，你也知道答案了：泛型不是模板，重载决议只基于泛型约束来做，他们可能需要写一个协议。而如果有人问「嘿，我怎样才能让我的协议扩展方法可以被重写」，你同样知道答案：你得再写*另一个*协议（并且可能需要从原来的类型向下转换到它）。

……听着，「面向协议编程」这个说法可能有点像个流行语，但我们可不是开玩笑的！协议就是你在值类型上实现运行时多态、乃至多态本身的工具。用它们！

1. 优化会模糊这些区分。C++ 或 Rust 代码可能会生成同一个函数的许多份副本，但随后如果它们在机器码层面行为相同，就会被优化回一个函数，或者至少把函数中共同的部分*外提（outline）*出来以节省代码体积。和内联一样，这通常取决于启发式规则和其他设置，如今仍然是一个活跃的研究领域（至少几年前是这样）。反过来，虽然 Swift 在形式上对泛型函数的每个版本都只使用同一份定义，但它有时会针对特定的具体类型对它们进行*特化*，以性能换取代码体积。[↩︎](#fnref:optimizer)
2. 我这是在开玩笑，但实际上 Objective-C *确实*关心对泛型方法调用做*一些*类型检查，以便得到正确的调用约定。你不能在一个地方把某个方法声明成返回 `float`，在另一个地方又声明成返回 `id`，所以如果你尝试调用一个完全不在参数约束范围内的方法，编译器是会报错的。

  我这里还偷偷夹带了一下 Rust 的重载。Rust *确实*有重载，尽管它装作没有：不同的 trait 可以声明同名方法，而调用者在两个 trait 都成立时，必须手动消除歧义。[↩︎](#fnref:objc)

本文发布于 [2024](https://belkadan.com/blog/2024) 年 [4](https://belkadan.com/blog/2024/04) 月 06 日，归类于 [技术](https://belkadan.com/blog/technical)。标签：[Swift](https://belkadan.com/blog/tags/swift)、[编程语言](https://belkadan.com/blog/tags/programming-languages)
