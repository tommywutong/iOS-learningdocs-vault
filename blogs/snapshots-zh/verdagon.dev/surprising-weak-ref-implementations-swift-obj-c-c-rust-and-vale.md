---
title: 令人惊讶的弱引用实现：Swift、Obj-C、C++、Rust 和 Vale
source_url: 'https://verdagon.dev/blog/surprising-weak-refs'
source_domain: verdagon.dev
source_group: single-site
original_language: en
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:1eaae12c3bd3915d'
plan_ref: 第二周：weak、属性关键字与 Block / Day 2｜weak 按“写入—读取—销毁”三段学（对应 W2-01～W2-06）
plan_week: 第二周：weak、属性关键字与 Block
plan_day: Day 2｜weak 按“写入—读取—销毁”三段学（对应 W2-01～W2-06）
container: '//div[contains(@class,''page-inner'')]'
container_source: map
---

> 原文：[Surprising Weak-Ref Implementations: Swift, Obj-C, C++, Rust, and Vale](https://verdagon.dev/blog/surprising-weak-refs)

# 令人惊讶的弱引用实现：Swift、Obj-C、C++、Rust 和 Vale

这些花招，就在我们眼皮底下！

2022 年 4 月 4 日 —— Evan Ovadia

“你没开玩笑吧？这……**太可怕了。**”——Alice（评价 Obj-C）。

“这太荒谬了！”——Ed（评价 Vale）。

“弱引用不只是一个索引，它是一种**心态。**”——Bob（评价 Rust）

弱引用是很 _古怪_ 的东西。

这篇文章汇集了各种语言为了实现弱引用而使用的那些神秘而晦涩的机制。

我们的任务是找到最适合 [Vale](https://vale.dev/) 的方法，要符合它**快速、内存安全且易于使用**的目标。

最后，我们创造了一种全新的方法！

## 它们 _应该_ 是什么样子的？

在大多数语言中，[0](#note0) 普通引用是“强”引用。只要存在至少一个指向某个对象的强引用，该对象就会保持存活。当最后一个强引用消失时，对象就会被释放。[1](#note1)

我们也可以有指向该对象的**弱**引用，它 _不会_ 让对象保持存活。在目标对象消亡后，它们看起来会是 nil。[2](#note2)

它们不仅有助于打破[引用计数循环](https://www.appypie.com/how-to-fix-strong-reference-cycle-swift)，还能用来了解某个东西在逻辑上是否仍然存在，从而影响我们程序的行为。如果你曾经在类中见过表示存活或已销毁的布尔值，那很可能就是一个适合使用弱引用的场景。

例如，我们可以在观察者中使用它：

vale

```vale
func handleClick(self &Button) {
  // 检查 self.clickObserverWeakRef 指向的对象是否仍存活。
  // 如果存活，就将其引用为 clickObserver。
  if clickObserver = self.clickObserverWeakRef.lock() {
    // 既然知道它存活，就调用它的 onClick。
    clickObserver.onClick();
  }
}
```

或者，一个魔法飞弹可以检查它的敌人是否仍然存在：

vale

```vale
func takeAction(self &Missile) {
  // 检查 self.enemyWeakRef 指向的敌人是否仍存活。
  // 如果存活，就将其引用为 enemy。
  if enemy = self.enemyWeakRef.lock() {
    // 既然知道它存活，就向它移动一步。
    self.position.goToward(enemy.position);
    if self.position == enemy.position {
      // 已到达敌人位置，爆炸！
      self.explode();
    }
  } else {
    // 敌人已经消失。就在当前位置爆炸！
    self.explode();
  }
}
```

这是一个相当有用的工具！而且它的底层原理也很简单。

_……除了_ 在 Objective-C 中。

## Objective-C 的全局弱指针追踪管理器 [3](#note3)

Objective-C 有一个受互斥锁保护的全局散列映射（hash map），追踪所有弱引用及它们所指向的对象。

具体来说：

- 当我们创建一个指向某个对象的新弱引用时，就在映射中添加一个条目。
- 当我们移除一个指向某个对象的弱引用时，就从映射中删除该条目。
- 当一个对象消亡时，它会查找该对象的所有条目……

出人意料的是，这种方法 _确实_ 有一些好处！

- 给定一个弱引用，检查它是否指向一个存活对象是 _极快的_。我们只需要检查该引用是否为 nil。
- 它没有 Swift 和 Rust 存在的“僵尸对象”问题；这种方法 _可能_ 比它们使用更少的内存。
- 在我们创建第一个弱引用之前，这种方法零开销。

但当然，它也有缺点：

- 创建和销毁弱引用 _极慢_。它需要获取全局锁并执行一些散列映射操作。
- 每个弱引用消耗 16B，有时更多。[4](#note4)

**附注**

（有趣的旁枝想法）

注 [–] 注 [+] 0 1 2 3 4

0

更具体地说，在 Python、Swift、Obj-C、C# 这类共享所有权语言中。

1

在像 Swift 这样的引用计数语言中，语言会立即注意到对象不再有强引用，并立即释放该对象。在像 Java 这样的追踪式垃圾回收语言中，解释器最终会注意到没有人指向这个对象，然后才释放它。

2

语言很少将它们直接设为 null。更常见的是，弱引用有某种方式知道目标对象是否仍然存活，从而它可以假装是 null。

3

来源：[Matt](https://stackoverflow.com/a/42847825)，[Mecki](https://stackoverflow.com/a/23689503)

4

我不确定，但如果全局映射是一个 unordered_map\<void*, vector\<void*\>*\> 散列映射（以 C++ 术语来说），负载因子为 0.5，那么为某个新对象创建第一个弱引用可能花费约 48B，而任何后续的弱引用将花费 16B。如果有人想深入研究，源代码可在[此仓库](https://github.com/apple-oss-distributions/objc4/tree/objc4-838.1)中找到，可能在 [objc-weak.h](https://github.com/apple-oss-distributions/objc4/blob/objc4-838.1/runtime/objc-weak.h) 附近。（感谢 [mayoff](https://www.reddit.com/r/vale/comments/tuokkq/surprising_weakref_implementations_swift_objc_c/i38ln6f/?context=3) 提供的线索！）

## Swift 的僵尸对象

更新：这个描述实际上已经过时了；本文描述的是它在 Swift 4 之前的工作方式。在 Swift 4 中，他们更新为使用“side tables”，请参阅 [Mike Ash 的文章](https://www.mikeash.com/pyblog/friday-qa-2017-09-22-swift-4-weak-references.html)了解相关描述。[5](#note5) 敬请期待第二部分，届时我们将讨论 side tables、“reference chaining”以及 Python 的方法！

当 Swift 没有因兼容性原因而采用 Objective-C 的方法时，它实际上采用了一种相当优雅的方式。[6](#note6)

一个 Swift 对象内部有两个计数器：

- 一个计数器，用于统计指向该对象的**强**引用数量。
- 一个计数器，用于统计指向该对象的**弱**引用数量。

还记得我们之前说过“当最后一个强引用消失时，对象就被释放”吗？**这对 Swift 来说不成立。**

假设一个对象有强引用和弱引用指向它。

当最后一个强引用消失时，对象会被**反初始化（deinitialized）**，但不会被释放。我喜欢把这个过程想象成将所有字段清零。[7](#note7)

对象还不会立即被释放；它处于一种“僵尸状态”，因为它没有可用的内容，但只要还有弱引用指向它，它就会保持存活。

如果我们问其中一个弱引用：“你是否指向一个存活对象？”，它会查看该对象并检查强引用计数是否为正数。如果是，则返回 true；如果为零，则返回 false。[8](#note8)

后来，当我们放弃最后一个弱引用时，弱引用计数变为零，对象才被释放；僵尸终于被销毁了。

Swift 的方法有一个很大的好处：

- 速度非常快，因为引用计数就在对象其他字段的旁边，这对缓存非常友好。[9](#note9)

和一些代价：

- 僵尸对象：即使最后一个强引用消失，整个对象的内存分配可能仍然存在。
- 有一定的内存开销（每个对象多一个计数器），即使我们从不使用弱引用，也要支付这个开销。
- 所有对象都必须独立地在堆上分配，我们永远无法对一个位于其他对象内存内部的对象持有弱引用。

Swift 的方法非常简单，我喜欢这一点。[10](#note10)

注 [–] 注 [+] 5 6 7 8 9 10

5

感谢 [electromaster666](https://www.reddit.com/r/swift/comments/tuoduj/surprising_weakref_implementations_swift_objc_c/i37d0u2/?context=3)、[mayoff](https://www.reddit.com/r/vale/comments/tuokkq/surprising_weakref_implementations_swift_objc_c/i38ln6f/?context=3) 和 [jaredgrubb](https://www.reddit.com/r/cpp/comments/tuohau/surprising_weakref_implementations_swift_objc_c/i3b94ws/?context=3) 指出这一点！

6

来源：[Mike Ash](https://mikeash.com/pyblog/friday-qa-2015-12-11-swift-weak-references.html)

7

这并不完全正确，它实际上不会改变内存，但这样想对理解很有帮助。

8

如果答案是 false，Swift 还会将该引用设为 _实际上的_ null，而不仅仅是让它指向一个僵尸对象，这样下次回答时可以更快，无需再次解引用。

9

这意味着计数器和字段位于同一缓存行（cache line），也就是说，如果我们要访问计数器，CPU 自然会将其附近的一些字段也带入缓存，从而加快后续访问速度。

10

尤其是与 Objective-C 的方法相比！

## C++ 的 weak_ptr

如果看内存布局，C++ 与 Swift 相似；在对象旁边，我们可以有一个强引用计数和一个弱引用计数。[11](#note11)

在 C++ 中，我们可以选择对象是否可以对其持有弱引用。一个 Spaceship 默认情况下没有任何计数器，但一个 shared_ptr\<Spaceship\> 会有。

我们可以从任何 shared_ptr\<Spaceship\> 创建一个弱引用，即 weak_ptr\<Spaceship\>。

这有好处：

- 只有在需要时，才选择支付计数器的 16B 开销。[12](#note12)

以及一个代价：

- 每个 weak_ptr 是 16B。[13](#note13)

以及一些古怪之处：

- 如果我们使用 make_shared 进行分配，对象及其控制结构共享同一个内存分配，会导致僵尸对象。[14](#note14)
- 如果我们有一个普通指针（Spaceship*），我们无法获得 weak_ptr\<Spaceship\>，除非 Spaceship 继承自 std::enable_shared_from_this。

注 [–] 注 [+] 11 12 13 14

11

如果我们使用 std::make_shared 就是这种情况。如果直接初始化 shared_ptr，那么计数器将在堆中的其他位置。

12

这是一个称为“零成本抽象（zero-cost abstraction）”的原则；如果不使用某个特性，它就不会花费我们任何空间或 CPU 时间。

13

weak_ptr 的典型实现存储两个指针：

- 指向控制块（control block）的指针；以及
- 构造它所用的 shared_ptr 的存储指针。

来源：[cppreference](https://en.cppreference.com/w/cpp/memory/weak_ptr)

14

[来源](https://dev.to/fenbf/how-a-weakptr-might-prevent-full-memory-cleanup-of-managed-object-i0i)

## Rust 的 Weak

Rust 的 Rc 和 Weak 基本上就是 C++ 的 shared_ptr 和 weak_ptr，有几个不同之处：

- Rust 的 Rc 总是将它的计数器放在对象旁边，而 C++ 允许我们将其放在一个单独的块中（如果我们想这样做的话）。
- 给定一个 &Spaceship，我们不能获取 Weak\<Spaceship\>。

我们在 Rust 中不常看到 Rc 和 Weak。相反，我们使用其他机制来模拟弱引用的行为。

## 隐藏于众目睽睽之下的弱引用

我们现在已经看到了几种不同的弱引用。然而，如果我们把视野放宽一些，就能看到很多行为与弱引用非常相似的东西。

弱引用基本上是一种东西，你可以用它来换取一个指向对象的常规引用（_如果该对象仍然存在的话_）。

当你这样想的时候，很多东西都是弱引用。

例如，一个包含文件名的字符串，比如 myfile.txt。我们可以用它来换取文件的内容（如果该文件仍然存在的话）：

vale

```vale
func main() {
  if contents = readFileAsString("myfile.txt") {
    // 文件存在！
    println(contents);
  } else {
    println("File doesn't exist!");
  }
}
```

或者，我们有一个整数 ID，可以用它在映射中查找一个 Spaceship：

vale

```vale
func printName(ships &HashMap<int, Spaceship>, ship_id int) {
  if ship = ships.get(ship_id) {
    println("Ship exists! {ship.name}")
  } else {
    println("Ship doesn't exist!");
  }
}
```

注意我们是先检查是否存在，然后再使用结果数据。就像弱引用一样！

我最喜欢的伪装成弱引用的是**世代索引（generational index）**，常用于 C++ 和 Rust 程序中。

## 世代索引

我们经常把对象存储在数组或向量中，比如 Vec\<Spaceship\>。[15](#note15) 当我们销毁一个 Spaceship 时，我们通常希望为另一个 Spaceship 重用它的位置。

有时，我们会记住一个 Spaceship 在 Vec 中的索引。稍后，我们可能想知道那个 Spaceship 是否还在那里，或者它是否已经被重用。方法如下！

在向量中的每个对象旁边，我们有一个整数：Vec\<(Spaceship, i64)\>。这个 i64 就是 Spaceship 的**当前世代号（current generation number）**。每次我们重用某个槽位时，就增加这个数字。

每当我们想要记住一个 Spaceship 的索引时，我们也会一并记住它当时的世代号。这就是**记住的世代号（remembered generation number）**。

为了方便起见，我们将索引和这个“记住的世代号”放在一个叫做 GenerationalIndex 的小结构体中：

```
struct GenerationalIndex {
  index: i64,
  remembered_generation: i64
}
struct Missile {
  enemy_ref: GenerationalIndex
}
```

现在，如果我们想知道那个 Spaceship 是否仍然存在，我们只需**将当前世代号与记住的世代号进行比较**，就像这样：

```
if enemies[missile.enemy_ref.index] == missile.enemy_ref.remembered_generation {
  // 敌人仍然存在！
  let enemy = &enemies[missile.enemy_ref.index];
  ...
}
```

就好像这个世代索引在说：

**“你好！我在寻找索引 7 的第 11 位居民，他们还在吗？”**

而索引 7 处的元素则回答：

**“不，抱歉，我是第 12 位居民，第 11 位居民已经不在了。”**

或者回答：

**“是的！就是我。你想访问我的哪个字段？”**

这就是世代索引。它就像一个弱引用！

然而，世代索引有一个缺点：要“解引用”它，我们需要访问包含它的 Vec（比如上面的 enemies Vec），通常通过参数传入。

这有时会很不方便：当我们添加一个新参数时，我们必须修改调用方来提供它，然后是调用方的调用方，再然后是调用方的调用方的调用方，这可能导致“重构冲击波”。这样做的次数太多会造成 API 的不稳定。

有时，为了克服这个缺点，我们放弃并将所有容器放入一个“上帝对象”中，并将其作为参数传递给代码库中的每个函数。

也许有更好的方法来解决这个缺点。请继续阅读！

## Vale 的世代引用

Vale 增加了类似世代索引的东西，我们称之为**世代引用（generational reference）**。

每个对象在内存中都有一个“当前世代号（current generation number）”放在它旁边。每当我们销毁一个对象时，就增加这个数字。[16](#note16)

要创建对该对象的弱引用，我们获取两样东西：

- 指向该对象的指针。[17](#note17)
- 对象当前的世代号。

……然后将它们组合在一起。

为了知道对象是否仍然存在，Vale 只需将对象的当前世代号与我们引用中记住的世代号进行比较。

与世代索引类似，就好像这个引用在说：

**“你好！我在寻找这所房子的第 11 位居民，他们还在吗？”**

而开门的人回答：

**“不，抱歉，我是这所房子的第 12 位居民，第 11 位居民已经不在了。”**

或者回答：

**“是的！就是我。你想访问我的哪个字段？”**

我们实现了世代引用，并发现它们[比引用计数至少快 2.3 倍！](https://verdagon.dev/blog/generational-references)

与其他弱引用方法相比，这有几个好处：

- 创建或销毁新的弱引用是零开销的，无需增加引用计数器。
- 它实现了[无惧 FFI（Fearless FFI）](https://vale.dev/fearless#safe-externs)；C 代码无法破坏 Vale 对象。[18](#note18)
- 它没有僵尸对象问题。
- 支持世代引用只需要每个分配增加 8B 的开销！

以及代价：

- 支持世代引用需要每个分配增加整整 8B 的开销。
- 可能需要一些虚拟内存操作才能将内存释放给操作系统。[19](#note19)
- 它只能用于堆分配，因为堆分配有稳定的地址。

我们预计普通的 Vale 程序会混合使用三种不同的方法：

- 对于堆分配，我们会使用世代引用。
- 当我们可以方便地访问容器时，我们会使用世代索引。
- 对于所有其他情况，我们会使用“增强型世代索引”，它也包含一个对容器的引用。

通过在标准库中提供所有这些方法，我们可以轻松地拥有快速的弱引用。这很好，因为 Vale 的目标是让速度和安全性变得前所未有的简单。

注 [–] 注 [+] 15 16 17 18 19

15

或者 C++ 的 std::vector\<Spaceship\>，或 Java 的 ArrayList\<Spaceship\>。

16

注意，我们不会立即对它调用 free() 释放给操作系统，因为我们需要那个世代号持续存在，以便与弱引用记住的世代号进行比较。稍后，我们会使用一些虚拟内存技术将物理内存释放回操作系统。了解更多请参阅 [Mesh](https://tiba-jrchang.medium.com/mesh-compacting-memory-management-for-c-c-applications-bc2a2cecc8cc)！

17

因为它不是索引，所以我们不需要访问任何容器！

18

像 Python 这样的引用计数方法会遭受此问题。我们将一个引用传递给 C 代码，C 代码必须手动记得增加/减少它。忘记这样做会破坏 Python 对象。而世代引用则不需要这种增加操作！

19

参见 [Mesh](https://tiba-jrchang.medium.com/mesh-compacting-memory-management-for-c-c-applications-bc2a2cecc8cc)，这是一种将多个虚拟地址合并到一个底层物理页面的算法。

## 结论

感谢阅读！在接下来的几周里，我将撰写关于如何用“自动借用检查器”增强世代引用的文章，所以请订阅我们的 [RSS 订阅源](https://verdagon.dev/rss.xml)、[Twitter](https://twitter.com/vale_pl) 或 [r/Vale](https://reddit.com/r/vale) 子版块，或者来 [Vale Discord](https://discord.gg/SNB8yGH) 逛逛。

- Evan Ovadia
