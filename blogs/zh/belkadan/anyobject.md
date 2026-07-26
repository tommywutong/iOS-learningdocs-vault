---
title: AnyObject
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2024/07/AnyObject/'
original_language: en
published: 2024-07-02
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:67a612dc4c63b324'
translated: true
---

> 原文：[AnyObject](https://belkadan.com/blog/2024/07/AnyObject/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [XZ Gon' Give It To Ya](https://belkadan.com/blog/2024/04/XZ-Gon-Give-It-To-Ya/)

[The Shell is a Program](https://belkadan.com/blog/2024/12/The-Shell-is-a-Program/) »

« [Swift 中的运行时多态](https://belkadan.com/blog/2024/04/Run-time-Polymorphism-in-Swift/?tag=swift)

## [AnyObject](#)

AnyObject 什么时候不是 AnyObject？当它是一个协议类型的时候。

Swift 有一个叫 AnyObject 的类型，它代表一个引用计数的对象，没有任何可用的操作。^[1](#fn:objc) 这听起来不太有用，但有时候你只是想借助这个对象的生命周期（一种动态版的 RAII），另一些时候你打算把它向下转换成一个具体类型。

AnyObject 也可以用作泛型约束。如果你用 `T: AnyObject`，就能保证 T 具有那种单一对象引用的表示形式。这让你可以像预期的那样持有对 T 的 `weak` 和 `unowned` 引用。

你也可以把 AnyObject 用作协议上的约束：`protocol MyDelegate: AnyObject`。这样一来，实现者就已知具有引用语义，通过 `T: MyDelegate`，你同样可以持有对 T 的弱引用。你甚至可以持有对 `any MyDelegate` 的弱引用，从而允许在不同类型的委托之间切换。

不过你可能会碰到的一个情况是，`any MyDelegate` 本身并不是 AnyObject。

（什么？）

如果你试图把 `any MyDelegate` 当作 `T: AnyObject` 来用，你会发现编译器对此并不满意。尽管每一个具体的 MyDelegate 类型都是合法的 AnyObject 类型，`any MyDelegate` 本身却不是。为什么不是？因为它携带的信息比一个单纯的对象引用要多：它还带有一个「witness table」指针，这是协议一致性在运行时的表示。这就是协议类型（`any` 类型）在 Swift 里的*工作方式*：它们既有普通的值——按大小决定是内联存储还是外部存储——又额外带有那个塞满了方法指针的 witness table。当你通过一个 `any` 类型调用协议方法时，运行时的代码会去查这张给定的表，取出该方法对应的实现，然后把值那部分当作 `self` 来调用它。^[2](#fn:extension)

但是等等，Objective-C 从来没有这个问题！`id <MyDelegate>` 类型占用的存储不会超过一个单一对象引用！但那是因为 ObjC 协议并不是表示成方法表；它们只是承诺实现的类*拥有*带有特定名字的方法。所以协议的「表」和一个类*所有*方法的「表」其实是同一张——代价是方法名（选择器）要共用一个命名空间，还有 App 启动和方法调用时的一点额外开销。而这张表是存在类型里的，每个对象都知道自己的类型，所以值上不需要附带第二个指针。

（这是个好的取舍吗？这是个大问题，牵涉的东西远不止协议类型的表示方式本身。也许改天再谈。）

所以这就是为什么 Swift 里受类约束的协议类型，比 ObjC 里的要稍微没那么方便一点点。你依然可以把值转换成 AnyObject，依然可以对它们持有弱引用或 unowned 引用，依然可以相信它们的拷贝和移动成本是固定的。你也依然可以把该协议用作约束，获得所有同样的效果。但你不能把两者混在一起用，因为 `any MyDelegate` 本身并不具备 `AnyObject` 的表示形式。

1. [在 Apple 的操作系统上，这其实是个谎言](https://belkadan.com/blog/2021/08/Swift-Regret-AnyObject-Dispatch/)，但我还是鼓励大家都当它是真的。[↩︎](#fnref:objc)
2. 这也是为什么协议扩展里定义的方法是静态解析的：它们不在那张表里。而且由于模块是分开编译的，把它们放进表里也可能根本*做不到*。所以这里只有一条规则，那就是只有协议的要求会被[动态派发](https://belkadan.com/blog/2024/04/Run-time-Polymorphism-in-Swift/)。[↩︎](#fnref:extension)

本文发布于 [2024](https://belkadan.com/blog/2024) 年 [7](https://belkadan.com/blog/2024/07) 月 02 日，归类于 [技术](https://belkadan.com/blog/technical)。标签：[Swift](https://belkadan.com/blog/tags/swift)
