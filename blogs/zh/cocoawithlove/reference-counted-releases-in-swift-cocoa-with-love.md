---
title: Swift 中的引用计数释放 | Cocoa with Love
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/resources-releases-reentrancy.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:e80586f586112409'
translated: true
---

> 原文：[Reference counted releases in Swift | Cocoa with Love](https://www.cocoawithlove.com/blog/resources-releases-reentrancy.html)　·　Cocoa with Love (Matt Gallagher)

几周前我[发布了](https://www.cocoawithlove.com/blog/cwlsignal.html)我的 [CwlSignal 项目](https://github.com/mattgallagher/CwlSignal)。自那以后，陆续有人问到我在那段代码里非常规地使用 Swift `withExtendedLifetime` 是怎么回事。

为了把这件事说清楚，我想先简略看一下 Swift 编译器是在**什么时候**选择释放引用计数对象的。这个题目很棘手，因为《The Swift Programming Language》过于高层，不会给出细节，而 Swift 仓库里的其他文档有时又不够完整。

既然文档指望不上，我转而细查 Swift 编译器，试图搞清楚它究竟有哪些优化会重新排列 release 指令的顺序。基于观察到行为，我会谈谈在哪些情形下对象会被释放、你可能需要怎样保持对象存活，以及如何用不同的方式组织代码来帮助编译器做好它的工作。

最后再绕回到 `withExtendedLifetime`，先讨论它的**设计**用意，再说我为什么把它用在了一个非常规的地方。

## 作用域生命周期

在 C++ 和某些其他语言里，可以保证所有“左值”（赋给变量的值）存活时间与声明该变量的作用域一样长。C++ 作用域锁这类构造就是建立在一条原则之上的：

```cpp
std::unique_lock<std::mutex> lock(this->mutex);
doSomeInternalWork();
```

因为 `lock` 一定会活到作用域结束，它的析构函数（会替我们解锁 mutex）就会在工作函数执行完了才运行，从而保证这部分工作被 mutex 保护着。

如果用 Swift 写同样的代码，看起来可能是这样：

```swift
let lock = ScopedLock(self.mutex)
self.doSomeInternalWork()
```

这样写确实能工作，但恐怕并不适合在 Swift 里推行这种做法。

不适合的原因是：Swift 的自动引用计数（Automatic Reference Counting，ARC）并不保证作用域变量——比如这里的 `lock`——会存活满整个作用域。ARC 只保证作用域变量存活到它们的最后一次**使用点**——而 `lock` 其实根本没被**使用过**，它仅仅是被赋值；于是按照 ARC 最宽松的解释，`lock` 可能**立刻**就被释放了。

可我也说了，在目前的 Swift 编译器版本下，这段 Swift 代码确实能工作。这只是巧合吗？未来会变吗？我们到底可以抱什么期望？

我们试着通过代码示例来探个究竟。

## 短于整个作用域的声明周期

想看到被 ARC 缩短生命周期比整个作用域还短的变量，可以看一个 Objective-C 例子：

```objc
First *f = [[First alloc] init];
consumesAnyObject(f)

Second *s = [[Second alloc] init];
consumesAnyObject(s)
```

`consumesAnyObject` 将它的参数声明为 `ns_consumed`（这等价于 Swift 默认以所有权传递参数的行为）。

最终的结果是，`f` 的生命周期在第一次调用 `consumesAnyObject` 时就结束了，并且在这行调用之后立即被释放——在作用域中途。这就是自动引用计数可以干出来的事，也是不能把 ARC 当成 C++ 作用域锁那种必须靠作用域保命的东西来依赖的原因。

那 Swift 会不会这样？不会，起码在现在的 3.0.2 版本里不会。等价代码里，`f` 和 `s` 都是在调用**第二次** `consumesAnyObject` 之后才释放的：

```swift
let f = First();
consumesAnyObject(f)

let s = Second();
consumesAnyObject(s)
```

## 延长 ARC 生命周期

不过，假想一下我们确实碰上了生命周期会半路结束的情况。我们可以用 Swift 函数 `withExtendedLifetime` 来应对。它能让我们明确表达：希望这个对象活过随后的一系列调用：

```swift
let lock = ScopedLock(self.mutex)
withExtendedLifetime(lock) {
   self.doSomeInternalWork();
}
```

可是我在 Swift 里压根找不到必须这样做的例子，那 `withExtendedLifetime` 是不是基本就是个摆设？

至此，我们看到的信息似乎自相矛盾。

一方面：

- ARC 只把生命周期保证到**最后一次使用**
- Objective-C 的 ARC 规则会让生命周期在任何“消费”传入对象的调用之后立即终止
- Swift 提供了 `withExtendedLifetime`，看起来就是因为的确有“延长”生命周期的需要

另一方面：

- 在 Swift 里好像根本找不到必须去延长生命周期的明显场景；无论是 Debug 编译还是 Release 编译，所有生命周期看上去都会撑到作用域末尾。

这些怎么才说得通，确凿的答案又在哪里？

遗憾的是，文档帮不上太大忙。[The Swift Programming Language](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/AutomaticReferenceCounting.html) 对这个题目讲得太上层，根本不能完全解释 Swift 自动引用计数底层的规则。[ARCOptimization.rst 文档](https://github.com/apple/swift/blob/master/docs/ARCOptimization.rst) 满是很显眼、听起来很有用的段落标题，后面跟着一句“TODO: Fill this in”，根本没讨论生命周期可能在什么时候缩短。 Clang 的 [Automatic Reference Counting](http://clang.llvm.org/docs/AutomaticReferenceCounting.html) 文档篇幅大得多，但正如我已经证明的，Swift 看起来用的是另一套略微不同的规则。

## 从 Swift 编译器看 release

我们试着直接从 Swift 编译器入手，搞清楚究竟是怎么回事。

Swift 里的 release 是由 Swift 中的“SILGen”（Swift 中间语言生成器）代码生成的。任意语句的 SIL 生成都可以为“右值”（被使用但没有赋给变量的值）产生 release，而本文大部分关注的“左值”的 release，发生在 `SILGenFunction::emitEpilogBB` 对所在基本块调用的 `emitCleanups` 中，这个逻辑位于 [SILGenEpilog.cpp](https://github.com/apple/swift/blob/master/lib/SILGen/SILGenEpilog.cpp) 文件。

也就是说，“左值”被留到所在块的收尾（epilog）阶段，以 LIFO 顺序清扫。这表明 Swift**确实**和 C++ 以及其他作用域生命周期语言行为一致。

但这不是全部故事。

如果你在打开优化的情况下编译（"-O"，也就是 Release 编译），那么后续 SIL 优化器会把来自 `createLateReleaseHoisting` 的 `SILTransform` 应用到代码上，这部分逻辑定义在 [ARCCodeMotion.cpp](https://github.com/apple/swift/blob/master/lib/SILOptimizer/Transforms/ARCCodeMotion.cpp)。它会扫描 release——包括处在收尾阶段的那些——然后尽量把它们向前挪到函数中最早可以释放的位置。

于是，在优化开启时，“左值”就会被尽早释放，理论上可以前移到函数内更早的地方。

但同样，这也不是全部故事。我们得定义“尽早”。实际上 release 只能前移越过那些不“阻挡”它的指令。什么会阻挡 release 前移？几乎什么都挡。

翻看 [ARCAnalysis.cpp](https://github.com/apple/swift/blob/master/lib/SILOptimizer/Analysis/ARCAnalysis.cpp) 里的 `mayHaveSymmetricInterference`，release 不能向前跨过以下几种情况：

1. 对该对象地址的内存访问
2. 对与该对象关联的内存图中任何内容的内存访问
3. 在对象 `deinit` 函数中访问过的任意地址的内存访问
4. 对与在对象 `deinit` 函数中访问过的任意地址关联的内存图中任何内容的内存访问
5. 与该对象、它的内存图或它的 `deinit` 函数之间何种交互行为无法完全确定的任何函数

最后一条杀伤力最大：在基础指令之外，函数的某些侧面几乎总有一些确定不了的东西。

这些要求极大地限制了 `ARCCodeMotion` 能做的事情。绝大多数时候，收尾阶段的 release 根本不会挪动。当然，你能理解为什么要设这些限制：优化器不应当在会引发可观测影响的情况下，去改动“release”指令的顺序。

## 哎呀，一个~~Bug~~（更正：Swift 3.0.x 中的惊人行为）

> **更新**：根据几位 Swift 开发者的反馈，本节描述的行为虽然让人惊掉下巴，但并没有被当作一个 bug。详见下一节的讨论。

在此之前，我查看的都是 Swift 仓库 `master` 分支上的代码。当前的 Xcode 版本 8.2.1 内置的是 Swift 3.0.2。不幸的是，这个版本用的 release 优化代码比 `master` 上老得多，并且里面有一些~~严重 bug~~（更正：严重地让人意外的行为）。

来看下面这个例子：

```swift
func test1() {
   let f = First()
   let s = Second()
}
```

这个函数里，Swift 会先释放 `s`，再释放 `f`（遵循 LIFO，也就是栈的顺序）。这是**预期**行为。

但是，如果 `First`、`Second` 以及一个叫 `something` 且接受 `Any` 参数（必须是一个存在类型才会触发这个 bug）的函数存在却不能内联（可能是因为不在当前编译单元），那么下面这段代码：

```swift
func test2() {
   let f = First()
   something(f)
   let s = Second()
}
```

**可以观察到**先释放 `f`，后释放 `s`（打破 LIFO 顺序）。注意，`f` 还是在收尾阶段释放，还在 `let s = Second()` 这一行之后；唯一的变化是编译器把两个 release 指令调换了顺序。

改变 release 顺序能糟糕到什么程度？糟糕到死锁的程度；这种重排序能导致相当夸张的次序改变，严重影响执行顺序。

看看我遇到过的最糟糕的一个场景：

```swift
func perform(data: UserData) {
   something(data)
   do {
      let resource = MutexLockedResource()
      resource.doSomethingElse()
   }
}
```

在这个结构中，`data` 参数在 `resource` 存活期间（也就是在互斥锁里面）被释放了。如果 `data` 没有被其他地方持有，而 `UserData` 的 `deinit` 又试图重新去获取那个 `MutexLockedResource`，这就可能死锁。

这看起来像是个拼凑出来的例子，但我在实际中确实碰到了多次死锁和其他执行顺序问题，逼着我一一绕开，每次都是因为父作用域的变量被诡异地重排了 `deinit` 调用顺序，从而在子作用域变量存活期间被释放。这种问题很难绕开，因为它完全出乎意料，而且 Swift 又没提供任何办法强制规定 `deinit` 的先后顺序。

值得庆幸的是，新的 ARC 优化器 `ARCCodeMotion` 看起来修复了这个问题和其他问题。它目前已经进了 Swift 3.1 分支，所以大概率会随这个版本一起交付。根据我的测试，换成新的 `ARCCodeMotion` 变换之后，本节描述的这些 release 重排序问题一个也没有出现。

## 更新：来自几位 Swift 开发者的细节

Swift 团队的开发者 Joe Groff [写道](https://twitter.com/jckarter/status/814522857325608960)：

> **jckarter**: @cocoawithlove Swift 的语义和 ObjC 一样。现在编译器没有缩短生命周期，并不代表以后不会。

所以我们应该预期未来生命周期的确会缩短，就像前面那个 Objective-C 例子。知道这点就好办了；`withExtendedLifetime` 会变得有用！

另一位 Swift 团队开发者 Michael Gottesman 也[写道](https://twitter.com/gottesmang/status/814561037865271296)：

> **gottesmang**: @s_tolksdorf @jckarter @cocoawithlove 我们在 Swift 文档里确实讨论过这个。看这里：[github.com/apple/swift/bl…](https://github.com/apple/swift/blob/master/docs/ARCOptimization.rst#deinit-model)

我前面贴过这份文档的链接，我也确实读过了。但显然我当时没吃透那一节。那里确实说在重排 release 顺序时，不会考虑 `deinit` 方法中的“干扰”，因此各个 `deinit` 调用在相对顺序上可以任意重排。

看起来我设想的差不多就是这种情况。“哎呀，一个 Bug”那节的例子 1 其实不算是 bug。

> **jckarter**: @cocoawithlove deinit 顺序重排不是 bug。你不应该依赖局部变量按 LIFO 顺序释放。

这一点在 Michael Gottesman 给的那份文档里已经蕴含了，不过我[回了一条](https://twitter.com/cocoawithlove/status/814733718568898560)说，我觉得“哎呀，一个 Bug”那节的例子 2 还是**应该**算个 bug——尽管它和例子 1 源于同一种机制。

> **cocoawithlove**: @jckarter 不保证 LIFO deinit 我可以接受，但一条准则：没在子作用域中使用的对象，它的释放要么在子作用域前，要么在子作用域后，不能插在中间。

Twitter 这种媒介很难把观点讲得很清楚，所以我在这里展开说。为什么我觉得第二个例子比第一个更让人难接受：因为一个来自父作用域、且在子作用域中根本没有用到的对象，它的副作用不应该与子作用域的副作用交织在一起——即便这些副作用只是释放所引发的副作用，而且子作用域只是一个本来没用的 `do` 作用域。

我们把 `do` 作用域移到子函数里，看看会怎样：

```swift
func perform(data: UserData) {
   something(data)
   completelySeparateChildFunction()
}
```

在这段代码里，在当前 Swift 3.0.2 编译时，如果 `completelySeparateChildFunction` 被内联，`data` 参数会在完全属于 `completelySeparateChildFunction` 内部的互斥锁区间内被释放。这是一种潜在的、由把我们自己的代码跟完全看不见的代码交织在一起所引发的死锁。即使我们知道 `completelySeparateChildFunction` 做了什么，Swift 也没给我们的 `perform` 函数任何手段来阻止这种串扰（目前唯一可行的阻止办法就是把 `completelySeparateChildFunction` 标记为 `@inline(never)`）。

父作用域和子作用域之间副作用的串扰，对最小惊讶原则的违背实在太严重。在代码结构上，两者**明显**是分开的，它们不该发生串扰，除非我们**显式地**让它们串扰。

## `withExtendedLifetime` 的常规用法

我给出过下面这个例子，然后说 `withExtendedLifetime` 基本上没用。

```swift
let lock = ScopedLock(self.mutex)
withExtendedLifetime(lock) {
   self.doSomeInternalWork();
}
```

在 Swift 真的开始提早终止生命周期之前（见上一节），Swift 确实没有逼着我们非要用什么手段来让 `lock` 活得够久（虽然具备安全意识的程序员还是应该用一下 `withExtendedLifetime`）。

但有一个场景是 Swift 确实逼着我们处理的，那就是右值。下面这种写法**严格来说**就是少不了的 `withExtendedLifetime` 用法：

```swift
withExtendedLifetime(ScopedLock(self.mutex)) {
   self.doSomeInternalWork();
}
```

不过我实际很少这么用 `withExtendedLifetime`。前提是你得有一个带副作用、而且副作用还得影响到闭包范围内代码的右值对象，并且该对象的 `deinit` 还不能有严格的顺序要求，否则就会撞上前两节讨论的那种惊人行为。这种条件组合在现代开发中不太常见。

不过，这里有一条可操作的提示：对于引用计数的对象，编译器通常不会把左值和右值之间的差异优化掉。引用计数的右值通常比引用计数的左值更精准、也更高效，因为右值的 release 会在紧接着的下一条非 release 语句之前发生。如果在 `withExtendedLifetime` 调用与外围作用域结束之间还有别的语句，右值会在这些语句之前被释放，而左值通常在之后才释放。

记住这一点：如果你并没有必要把一个对象赋给某个参数，那就最好别赋值。

## `withExtendedLifetime` 的非常规用途

可见 `withExtendedLifetime` 的常规用法真的不多。但我还是用它的，只是用法偏非常规一些。

CwlSignal 项目里有一个常见需求：把用户提供的数据的释放推迟到互斥锁释放之后再做（这样用户提供数据上哪怕有 `deinit` 也不会因为重入互斥锁造成死锁）。这在 CwlSignal 中通过类似下面的代码完成：

```swift
deferredWork.append { withExtendedLifetime(data) {} }
```

`deferredWork` 变量只是一个里面存有闭包的列表，这些闭包会在互斥锁退出后运行。而这里追加的闭包其实不需要做任何事，只需要捕获 `data` 的值就够。可我并没有真的一字不干，而是去调用了 `withExtendedLifetime`。

也可以试着真就一字不干。我们还是得告诉 Swift 想在闭包里捕获 `data` 变量，这可以通过捕获列表做到：

```swift
deferredWork.append { [data] in }
```

但编译器会警告：

```
warning: Capture "data" was never used
```

所以我用 `withExtendedLifetime` 来告诉编译器：“别急，我在用它。”

还有类似的“死存储”场景。CwlSignal 项目里有一个函数大致长这样：

```swift
public static func never() -> Signal<T> {
   var input: SignalInput<T>? = nil
   return Signal<T>.generate { i in
      input = i
   }
}
```

这段闭包里代码的唯一目的，就是持有收到的任何 `i`，好让 `i` 活到和这个闭包一样长。做法就是把 `i` 存到可变的、被捕获的 `input` 变量里。

逻辑都通，可编译器偏偏把 `input = i` 看作一次死存储。

```
warning: variable 'input' was written to, but never read
```

但在这里，保持对象存活本身就是一次“使用”，所以这个死存储是我们**想要的**。为了把这点向编译器说清楚，我用 `withExtendedLifetime(input) {}` 来给编译器一个让它可以解释成“使用了这个值”的东西。

```swift
public static func never() -> Signal<T> {
   var input: SignalInput<T>? = nil
   return Signal<T>.generate { i in
      input = i
      withExtendedLifetime(input) {}
   }
}
```

这么用 `withExtendedLifetime` 的理由是：它实际上什么事也不干，可它传递给编译器的信息——“我在这里用到了这个变量”——可以消除那些说变量没被使用的警告。既然我做这次死存储就是为了操作生命周期，那么用 `withExtendedLifetime` 在语义上也勉强沾边，尽管这不是它的常规用法。

## 结论

Swift 目前对 release 重排的做法还是相当保守的。Swift 开发者也指出，现在是这样，不代表以后也一直这样——他们显然**打算**让作用域中途的释放比现在发生得更频繁。这最终会让 Swift 的 release 排序更接近 Objective-C 的做法。

我通过简要的代码分析去确认在当前 Swift 版本（截至包含 Swift 3.1 预发布分支）里，release 指令究竟可能在什么情况下被重排。真相是，现阶段 release 很少被大范围重排。由于编译器对内存图和可达性了解有限，收尾阶段的 release 大多还是留在收尾阶段。即便偶尔被重排，影响也通常是**完全**不可察觉的。

`withExtendedLifetime` 函数有其设计用法——把一个对象的生命周期延长到一个相对较窄的闭包作用域上。鉴于 Swift 现在高度保守的行为，它最明确的用场是用于右值，以及当你对一个没有别处保持持有的对象使用 `withUnsafePointer` 的时候。更注重安全的用户不妨在更广泛的上下文里也这么用，因为将来 Swift 是可能逼迫你就范的。

不过，我通常把 `withExtendedLifetime` 当作一个用来消除编译器警告的工具，用在我只为了执行所有权转移而没有其他语义目的的场合。这个函数除了一次私有的 `_fixLifetime` 调用外没有别的效果（后者仅仅是强迫 SIL 层把对象保持存活），所以我觉得它很适合承担这个角色。

### 展望未来……

关于 CwlSignal 项目的代码，我还有更多想聊的。下一篇文章会介绍一个方便的实用工具——你可以独立于 CwlSignal 使用，用来处理来自 Objective-C 的一小段麻烦遗产。
