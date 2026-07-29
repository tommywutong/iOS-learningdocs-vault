---
title: 可选非逃逸闭包
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/10/optional-non-escaping-closures/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:33b136b6ed072caa'
translated: true
---

> 原文：[Optional Non-Escaping Closures](https://oleb.net/blog/2016/10/optional-non-escaping-closures/)　·　Ole Begemann

# 可选非逃逸闭包

Swift 区分了 _逃逸_（escaping）闭包和 _非逃逸_（non-escaping）闭包。[逃逸闭包](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/Closures.html) 是指（可能）在传入的函数返回 _之后_ 才被调用的闭包——也就是说，闭包 _逃逸_ 了作为参数传入的函数的范围。

逃逸闭包通常与异步控制流（asynchronous control flow）相关联，例如以下场景：

- 一个函数启动一个后台任务（background task）并立即返回，通过完成处理程序（completion handler）报告后台任务的结果。
- 一个视图类（view class）将闭包存储在属性（property）中，作为按钮点击事件的事件处理程序（event handler）。每当用户点击按钮时，该类都会调用该闭包。该闭包逃逸了属性设置器（property setter）。
- 你使用 [`DispatchQueue.async`](https://developer.apple.com/reference/dispatch/dispatchqueue/2016098-async) 将一个任务（task）调度到调度队列（dispatch queue）上异步执行。该任务闭包的生命周期超过了 `async` 调用。

与之对比的是 [`DispatchQueue.sync`](https://developer.apple.com/reference/dispatch/dispatchqueue/2016081-sync)，它会等待任务闭包执行完毕后才返回——闭包永远不会逃逸。对于 [`map`](https://developer.apple.com/reference/swift/sequence/1641748-map) 和标准库中其他常见的序列（Sequence）和集合（Collection）算法也是如此。

# 为什么区分逃逸闭包和非逃逸闭包很重要？

简而言之，是为了内存管理。一个闭包会强引用（strong reference）它所捕获的每个对象——如果在闭包内访问了 `self` 的任何属性（property）或实例方法（instance method），这还包括 `self`，因为这些都隐式携带了一个 `self` 参数。

这样做很容易无意中引入[引用循环](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/AutomaticReferenceCounting.html#//apple_ref/doc/uid/TP40014097-CH20-ID56)，因此编译器要求你在闭包内部显式地引用 `self`。这迫使你去思考潜在的引用循环，并使用[捕获列表](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/AutomaticReferenceCounting.html#//apple_ref/doc/uid/TP40014097-CH20-ID56)手动解决它们。

然而，非逃逸闭包不可能创建引用循环——编译器可以保证在函数返回时，该闭包已经释放了它捕获的所有对象。因此，编译器只要求对 _逃逸_ 闭包显式引用 `self`。这使得非逃逸闭包用起来要方便得多。

非逃逸闭包的另一个好处是编译器可以进行更积极的性能优化。例如，当闭包的生命周期已知时，编译器可以省略一些 retain 和 release 调用。此外，如果闭包是非逃逸的，闭包上下文的内存可以保存在栈（stack）上而不是堆（heap）上——不过我不确定当前 Swift 编译器是否会执行此优化（一个[2016年3月尚未解决的 bug 报告](https://bugs.swift.org/browse/SR-904)表明它不会）。

# 闭包默认是非逃逸的……

从 Swift 3 开始，非逃逸闭包[现在已成为默认](https://github.com/apple/swift-evolution/blob/master/proposals/0103-make-noescape-default.md)。如果希望允许闭包参数逃逸，需要在类型上添加 `@escaping` 注解。例如，以下是 `DispatchQueue.async`（逃逸）和 `DispatchQueue.sync`（非逃逸）的声明：

```
class DispatchQueue {
    ...
    func async(/* other params omitted */, execute work: @escaping () -> Void)
    func sync<T>(execute work: () throws -> T) rethrows -> T
}
```

在 Swift 3 之前，情况正好相反：逃逸是默认行为，而你需要添加 `@noescape` 来覆盖它。新的行为更好，因为它默认是安全的：函数参数现在必须显式注解才能指示存在引用循环的可能性。因此，`@escaping` 注解充当了对使用该函数的开发者的警告。

# ……但仅限于直接函数参数

非逃逸默认规则有一个问题：它只适用于 _直接参数位置_（immediate function parameter position）的闭包，即任何具有函数类型的函数参数。其他所有闭包都是逃逸的。

## 直接参数位置是什么意思？

让我们看一些例子。最简单的情况是类似 `map` 的函数：一个接受直接闭包参数的函数。正如我们所见，该闭包是非逃逸的（我省略了 `map` 真实签名中的一些细节，它们对本讨论不重要）：

```
func map<T>(_ transform: (Iterator.Element) -> T) -> [T]
```

### 函数类型的变量始终是逃逸的

与之对比的是一个具有函数类型的变量或属性（property）。它自动就是逃逸的，即使没有显式注解也是如此（实际上，添加显式的 `@escaping` 反而是错误）。这很有道理，因为给一个变量赋值会隐式地让该值逃逸到变量的作用域中，这对于非逃逸闭包来说是不允许的。然而，令人困惑的是，一个裸的、没有注解的函数类型在参数列表中的含义与在其他地方不同。

### 可选闭包始终是逃逸的

更令人惊讶的是，那些 _作为_ 参数使用，但被包装在其他类型（例如元组（tuple）、枚举 case（enum case）或可选值（optional））中的闭包也是逃逸的。因为在这种情况下，闭包不再是 _直接_ 参数，它会自动变成逃逸的。因此，在 Swift 3.0 中，你无法编写一个函数，其参数既是可选的又是非逃逸的。考虑以下人为构造的例子：`transform` 函数接受一个整数 `n` 和一个可选的转换函数 `f`。它返回 `f(n)`，或者如果 `f` 是 `nil` 则返回 `n`：

```
/// 将 `f` 应用于 `n` 并返回结果。
/// 如果 `f` 为 nil，则返回 `n` 不变。
func transform(_ n: Int, with f: ((Int) -> Int)?) -> Int {
    guard let f = f else { return n }
    return f(n)
}
```

在这里，函数 `f` 是逃逸的，因为 `((Int) -> Int)?` 是 `Optional<(Int) -> Int>` 的简写，也就是说，函数类型不处于 _直接_ 参数位置。这是不理想的，因为没有任何理由说明 `f` 在这里不应该是非逃逸的。

### 用默认实现替换可选参数

Swift 团队[已经意识到这个限制](https://bugs.swift.org/browse/SR-2444)，并计划在未来的版本中修复它。在此之前，了解这一点很重要。目前没有办法强制一个可选闭包成为非逃逸，但在许多情况下，你可以通过为闭包提供默认值来避免让参数成为可选的。在我们的例子中，默认值是恒等函数（identity function），它只是原封不动地返回参数：

```
/// 如果省略了 `f`，则使用默认实现
func transform(_ n: Int, with f: (Int) -> Int = { $0 }) -> Int {
    return f(n)
}
```

### 使用重载提供可选和非逃逸两个变体

如果无法提供默认值，Michael Ilseman 建议[使用重载作为变通方法](https://forums.swift.org/t/escaping-may-only-be-applied-to-parameters-of-function-type/4017/9)——你可以编写该函数的两个变体，一个带有可选（逃逸）函数参数，另一个带有非可选、非逃逸参数：

```
// 重载 1：可选，逃逸
func transform(_ n: Int, with f: ((Int) -> Int)?) -> Int {
    print("Using optional overload")
    guard let f = f else { return n }
    return f(n)
}

// 重载 2：非可选，非逃逸
func transform(_ input: Int, with f: (Int) -> Int) -> Int {
    print("Using non-optional overload")
    return f(input)
}
```

我添加了一些 print 语句来演示调用的是哪个函数。让我们用各种参数来测试一下。毫不意外，如果你传递 `nil`，类型检查器会选择第一个重载，因为它是唯一与输入兼容的：

```
transform(10, with: nil) // → 10
// 使用可选重载
```

如果你传递一个具有可选函数类型的变量，情况也是如此：

```
let f: ((Int) -> Int)? = { $0 * 2 }
transform(10, with: f) // → 20
// 使用可选重载
```

即使变量是非可选类型，Swift 仍然会选择第一个重载。这是因为存储在变量中的函数会自动逃逸，因此与期望非逃逸参数的第二个重载不兼容：

```
let g: (Int) -> Int = { $0 * 2 }
transform(10, with: g) // → 20
// 使用可选重载
```

但是，当你传递一个闭包表达式，即一个函数字面量（function literal）作为参数时，情况就不同了。现在，第二个、非逃逸的重载会被选中：

```
transform(10) { $0 * 2 } // → 20
// 使用非可选重载
```

由于使用字面量闭包表达式调用高阶函数非常常见，这使得你在大多数情况下可以走快乐路径（即非逃逸，无需考虑引用循环），同时仍然可以选择传递 `nil`。如果你决定走这条路，请确保记录为什么需要这两个重载。

### 类型别名始终是逃逸的

最后需要注意的一点是，在 Swift 3.0 中，你不能在类型别名（typealias）上添加逃逸或非逃逸注解。并且，如果你在函数声明中对函数类型使用了类型别名，那么该参数总是被认为逃逸的。针对[这个 bug](https://bugs.swift.org/browse/SR-2316) 的修复已经包含在 master 分支中，并且应该是下一个版本的一部分。
