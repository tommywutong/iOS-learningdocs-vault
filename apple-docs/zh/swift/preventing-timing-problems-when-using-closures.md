---
title: 防止使用闭包时出现时序问题
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/preventing-timing-problems-when-using-closures
source_url: 'https://developer.apple.com/documentation/swift/preventing-timing-problems-when-using-closures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/preventing-timing-problems-when-using-closures.json'
content_hash: 'sha256:23cda789700bb9df'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Swift](../swift.md)

# 防止使用闭包时出现时序问题

<sub>文章</sub>

了解对你的闭包发起的不同 API 调用会如何影响你的 App。

## 概述

你在 Swift 里用到的许多 API 都会把一个闭包——或者说以实例形式传递的函数——作为参数。因为闭包里可能包含与 App 多个部分交互的代码，所以理解你传给的这些 API 会以哪些不同方式调用闭包就很重要。你传给 API 的闭包既可能被同步调用（立即调用），也可能被异步调用（在之后的某个时刻调用）。它们可能被调用一次、多次，也可能一次都不被调用。

> [!important] 重要
> 对闭包何时被调用做出错误假设，可能导致数据不一致和 App 崩溃。

### 了解同步调用和异步调用的结果

当你把一个闭包传给某个 API 时，要考虑这个闭包相对于你 App 里其他代码，_什么时候_会被调用。在同步 API 里，调用闭包的结果会在你传入闭包后立即可用。在异步 API 里，结果要到之后的某个时刻才可用；这种差异既会影响你_在_闭包内部写代码的方式，也会影响_跟在_闭包之后的那部分代码的写法。

下面的示例定义了两个函数，`now(_:)` 和 `later(_:)`。这两个函数的调用方式是一样的：用一个尾随闭包，不传其他参数。`now(_:)` 和 `later(_:)` 都会接受一个闭包并调用它，但 `later(_:)` 会先等待几秒钟，然后才调用它的闭包。

```swift
import Dispatch
let queue = DispatchQueue(label: "com.example.queue")

func now(_ closure: () -> Void) {
    closure()
}

func later(_ closure: @escaping () -> Void) {
    queue.asyncAfter(deadline: .now() + 2) {
        closure()
    }
}
```

`now(_:)` 和 `later(_:)` 这两个函数，代表了你会在 App 框架里那些接受闭包的方法中遇到的两大类最常见的 API：像 `now(_:)` 这样的同步 API，以及像 `later(_:)` 这样的异步 API。

因为调用闭包可能会改变你 App 的局部状态和全局状态，所以你在传入闭包之后那几行代码里写的内容，需要仔细考虑这个闭包_何时_被调用。哪怕只是打印一串字母这么简单的事，也会受到闭包调用时机的影响：

```swift
later {
    print("A") // 最终会打印 "A"
}
print("B") // 立即打印 "B"

now {
    print("C") // 立即打印 "C"
}
print("D") // 立即打印 "D"

// 如果你在终端里运行这段代码，防止程序立即退出。
let semaphore = DispatchSemaphore(value: 0).wait(timeout: .now() + 10)
```

运行上面示例里的代码，通常会按 `B` → `C` → `D` → `A` 的顺序打印这些字母。尽管打印 `A` 的那一行在代码里排在最前面，但它在输出里的顺序却排在最后。这种顺序上的差异，是由 `now(_:)` 和 `later(_:)` 这两个函数的定义方式造成的。如果你写的代码依赖某个特定的执行顺序，你就需要知道每个函数是怎样调用它的闭包的。

> [!note] 注意
> `A` 相对于其他字母被打印的顺序并没有保证。在典型的系统条件下，它通常会被最后打印，但如果不在线程之间做更细致的同步，你就不应该编写依赖异步调用相对于同步代码的顺序的代码。

在使用接受闭包的 API 时，你会经常需要考虑这种基于时序的执行问题。在很多情况下，对你的 App 来说只有一种调用顺序是正确的，所以仔细想清楚在使用这些 API 的情况下你 App 的状态会是什么样，这一点很重要。可以借助 API 名称、参数名称以及文档，来判断一个 API 是同步的还是异步的。

一个常见的时序错误，是指望异步调用的结果能在发起调用的同步代码里就绪。例如，上面的 `later(_:)` 方法就类似于 [URLSession](../foundation/urlsession.md) 类的 [dataTask(with:completionHandler:)](<../foundation/urlsession/datatask(with_completionhandler_)-52wk8.md>) 方法，这个方法同样是异步的。你应该避免的一种时序场景是：在你 App 的 [viewDidLoad()](<../uikit/uiviewcontroller/viewdidload().md>) 方法里调用 [dataTask(with:completionHandler:)](<../foundation/urlsession/datatask(with_completionhandler_)-52wk8.md>) 方法，然后试图在你作为完成处理程序传入的闭包外部使用其结果。

### 不要在会被多次调用的闭包里写只应执行一次的改动

如果你要把一个闭包传给一个可能会多次调用它的 API，就不要在其中写那些只打算对外部状态做一次性改动的代码。

下面的示例创建了一个 [FileHandle](../foundation/filehandle.md)，以及一个要写入该句柄所指向文件的数据行数组：

```swift
import Foundation

let file = FileHandle(forWritingAtPath: "/dev/null")!
let lines = ["x,y", "1,1", "2,4", "3,9", "4,16"]
```

要把每一行都写入文件，可以把一个闭包传给 [forEach(_:)](<array/foreach(__).md>) 方法：

```swift
lines.forEach { line in
    file.write("\(line)\n".data(using: .utf8)!)
}
```

在用完 [FileHandle](../foundation/filehandle.md) 之后，要用 [closeFile()](<../foundation/filehandle/closefile().md>) 把它关闭。调用 [closeFile()](<../foundation/filehandle/closefile().md>) 的正确位置是在闭包外部：

```swift
lines.forEach { line in
    file.write("\(line)\n".data(using: .utf8)!)
}

file.closeFile()
```

如果你误解了 [closeFile()](<../foundation/filehandle/closefile().md>) 的要求，你可能会把这个调用放在闭包内部。这样做会导致你的 App 崩溃：

```swift
lines.forEach { line in
    file.write("\(line)\n".data(using: .utf8)!)
    file.closeFile() // 错误
}
```

### 不要把关键代码放进可能不会被调用的闭包里

如果你传给某个 API 的闭包有可能不会被调用，就不要把对你 App 继续运行至关重要的代码放进这个闭包。

下面的示例定义了一个 `Lottery` 枚举，它会随机选出一个中奖号码，如果猜中了正确的号码，就调用一个完成处理程序：

```swift
enum Lottery {
    static var lotteryWinHandler: (() -> Void)?

    @discardableResult static func pickWinner(guess: Int) -> Bool {
        print("Running the lottery.")
        if guess == Int.random(in: 0 ..< 100_000_000), let winHandler = lotteryWinHandler {
            winHandler()
            return true
        }

        return false
    }
}
```

编写依赖完成处理程序一定会被调用的代码是危险的。没有任何保证能确保随机猜测一定正确，所以像还账单这样安排在中彩票之后执行的重要操作，可能永远都不会发生。

```swift
func payBills() {
    amountOwed = 0
}

var amountOwed = 25
let myLuckyNumber = 42

Lottery.lotteryWinHandler = {
    print("Congratulations!")
    payBills()
}

// 你有 10 次中奖机会。
for _ in 1...10 {
    Lottery.pickWinner(guess: myLuckyNumber)
}

if amountOwed > 0 {
    fatalError("You need to pay your bills before proceeding.")
}

// 只有中了彩票，写在这一行之后的代码才会运行。
```

## 另请参阅

### 数据流与控制流

- [在你的 App 里维护状态](maintaining-state-in-your-apps.md) — 使用枚举来捕获并跟踪你 App 的状态。
