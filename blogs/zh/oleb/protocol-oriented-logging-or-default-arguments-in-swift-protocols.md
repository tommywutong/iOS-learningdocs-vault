---
title: 面向协议的日志，或者说 Swift 协议中的默认参数
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/05/default-arguments-in-protocols/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:67b600f8b34491ed'
translated: true
---

> 原文：[Protocol-Oriented Logging, or: Default Arguments in Swift Protocols](https://oleb.net/blog/2016/05/default-arguments-in-protocols/)　·　Ole Begemann

# 面向协议的日志，或者说 Swift 协议中的默认参数

**Swift 2.2 不允许在协议声明中使用默认参数。如果你想通过一个协议来抽象你的 App 的日志记录代码，这就会成为一个问题，因为默认参数正被用来向日志函数传递源代码位置。不过，你_可以_在协议扩展（protocol extension）中使用默认参数，而这也就提供了一种变通方案。**

一个典型的[日志](https://en.wikipedia.org/wiki/Logfile)消息应当包含日志事件的源代码位置（文件名、行号，以及可能的函数名）。Swift 为此提供了 `#file`、`#line`、`#column` 和 `#function` 这些[调试标识符](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Expressions.html#//apple_ref/doc/uid/TP40014097-CH32-ID390)。在编译时，解析器会将这些占位符展开为描述当前源代码位置的字符串或整数字面量。如果每次调用日志函数都要包含这些参数，那将极其繁琐，因此它们通常作为默认参数传递。这样做的可行性在于，编译器足够智能，能在默认参数列表中求值时将这些调试标识符展开为[调用点](https://en.wikipedia.org/wiki/Call_site)位置。以标准库中的 [`assert`](http://swiftdoc.org/v2.2/func/assert/#func-assert_-bool_-string-file_-staticstring-line_-uint) 函数[为例](https://developer.apple.com/swift/blog/?id=15)，它的声明如下：

```
func assert(
    @autoclosure condition: () -> Bool,
    @autoclosure _ message: () -> String = default,
    file: StaticString = #file,
    line: UInt = #line)
```

第三和第四个参数默认展开为调用方的源代码位置。（如果你对 [`@autoclosure`](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Closures.html#//apple_ref/doc/uid/TP40014097-CH11-ID543) 特性（attribute）感到好奇，它可以将一个表达式包装在闭包（closure）中，有效延迟表达式的求值——从调用点推迟到函数体内，而不需要调用方显式使用闭包表达式。`assert` 用它来仅在调试构建中求值条件（条件可能开销较大或有副作用），并且仅在断言失败时求值消息。）

# 一个简单的全局日志函数

你可以用同样的方式编写一个 `log` 函数，它接受一条日志消息和一个日志级别。其接口和实现可以如下所示：

```
enum LogLevel: Int {
    case verbose = 1
    case debug = 2
    case info = 3
    case warning = 4
    case error = 5
}

func log(
    logLevel: LogLevel,
    @autoclosure _ message: () -> String,
    file: StaticString = #file,
    line: Int = #line,
    function: StaticString = #function)
{
    // 使用 `print` 进行日志记录。
    // 目前我们不关心`logLevel`。
    print("\(logLevel) – \(file):\(line) – \(function) – \(message())")
}
```

对于 `message` 是否应该是 `@autoclosure`，你可以有不同看法。在这个简单的示例中，该特性没有任何好处，因为无论何种情况消息都会被求值。不过，我们在下一步会对此进行修改。

# 一个具体类型

与其使用全局的 `log` 函数，不如创建一个名为 `PrintLogger` 的类型，它用一个最低日志级别来初始化。它只会记录日志级别至少达到该最低严重级别的事件。为此，`LogLevel` 需要遵循 `Comparable`，这也是我上面将其声明为存储 `Int` 原始值的原因：

```
extension LogLevel: Comparable {}

func <(lhs: LogLevel, rhs: LogLevel) -> Bool {
    return lhs.rawValue < rhs.rawValue
}

struct PrintLogger {
    let minimumLogLevel: LogLevel

    func log(
        logLevel: LogLevel,
        @autoclosure _ message: () -> String,
        file: StaticString = #file,
        line: Int = #line,
        function: StaticString = #function)
    {
        if logLevel >= minimumLogLevel {
            print("\(logLevel) – \(file):\(line) – \(function) – \(message())")
        }
    }
}
```

你可以像这样使用 `PrintLogger`：

```
let logger = PrintLogger(
    minimumLogLevel: .warning)
logger.log(.error, "This is an error log")
    // 被记录
logger.log(.debug, "This is a debug log")
    // 什么都不做
```

# 一个包含默认参数的协议

接下来，我想创建一个 `Logger` 协议作为 `PrintLogger` 的抽象。这将允许我以后将使用 `print` 语句的简单日志记录替换为更复杂的实现，例如记录到文件或将日志发送到服务器。然而，我在这里遇到了阻碍，因为 Swift 不允许在协议声明中使用默认参数。以下代码无法编译：

```
protocol Logger {
    func log(
        logLevel: LogLevel,
        @autoclosure _ message: () -> String,
        file: StaticString = #file,
        line: Int = #line,
        function: StaticString = #function)
    // error: Default argument not permitted
    // in a protocol method
}
```

因此，我必须省略默认参数才能让协议编译通过。这起初似乎不是问题。`PrintLogger` 可以通过一个空的扩展来遵循该协议——它现有的实现已经满足了要求。并且通过 `logger: PrintLogger` 类型的变量来使用日志记录器的功能也一如既往。

问题在当你试图通过协议类型的变量 `logger2: Logger` 来使用日志记录器时变得明显，就像在那些不应该了解具体实现的代码中那样：

```
let logger2: Logger = PrintLogger(
    minimumLogLevel: .warning)
logger2.log(.error, "An error occurred")
    // error: Missing argument in call
logger2.log(.error, "An error occurred",
    file: #file, line: #line, function: #function)
    // 可以工作，但是 😱
```

`logger2` 只知道一个有五个必需参数的 `log` 方法，因此你每次调用都得指定所有这些参数。真糟糕！

## 将默认参数移到协议扩展中

解决方案是声明 `log` 方法的两个版本：一个，没有默认参数，照旧放在协议声明中。我将此方法命名为 `writeLogEntry`。第二个，放在 `Logger` 的协议扩展（protocol extension）中，这次包含默认参数（这是允许的）。这个方法我保留了 `log` 这个名字，因为它应该是协议的公开接口。

现在，`log` 的实现只有一行：它调用 `writeLogEntry`，传递它的所有参数，从而也传递了它通过默认参数从调用方那里收到的源代码位置。另一方面，`writeLogEntry` 是协议遵循者必须实现以执行实际日志记录的方法。这是完整的协议：

```
protocol Logger {
    /// 写入一条日志条目。遵循
    /// `Logger` 的类型必须实现
    /// 此方法来完成其工作。
    ///
    /// - Important: `Logger` 的客户端
    ///   不应调用此方法。
    ///   始终调用 `log(_:,_:)`。
    func writeLogEntry(
        logLevel: LogLevel,
        @autoclosure _ message: () -> String,
        file: StaticString,
        line: Int,
        function: StaticString)
}

extension Logger {
    /// `Logger` 的公开 API。调用
    /// `writeLogEntry(_:,_:,file:,line:,function:)`。
    func log(
        logLevel: LogLevel,
        @autoclosure _ message: () -> String,
        file: StaticString = #file,
        line: Int = #line,
        function: StaticString = #function)
    {
        writeLogEntry(logLevel, message,
            file: file, line: line,
            function: function)
    }
}
```

用 [session 408](https://developer.apple.com/videos/play/wwdc2015/408/) 的话来说，`writeLogEntry` 是一个_协议要求_，因此是该协议的一个_自定义点_，而 `log` 则并非由协议要求所支持，而是静态派发的。这正是我们想要的。`log` 方法的唯一任务是立即转发给包含实际逻辑的 `writeLogEntry`。实现 `Logger` 的类型没有理由重写 `log`。

这是完整的遵循了协议的 `PrintLogger` 类型：

```
struct PrintLogger {
    let minimumLogLevel: LogLevel
}

extension PrintLogger: Logger {
    func writeLogEntry(
        logLevel: LogLevel,
        @autoclosure _ message: () -> String,
        file: StaticString,
        line: Int,
        function: StaticString)
    {
        if logLevel >= minimumLogLevel {
            print("\(logLevel) – \(file):\(line) – \(function) – \(message())")
        }
    }
}
```

现在你可以按预期使用该协议了：

```
let logger3: Logger = PrintLogger(
    minimumLogLevel: .verbose)
logger3.log(.error, "An error occurred") // 🎉
```

## 对客户端的 API 可见性

这种方法的一个缺点是，很难通过[访问控制](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/AccessControl.html)向协议的使用者清晰地表明 `log` 和 `writeLogEntry` 的目的。理想情况下，使用该协议的客户端不应该看到 `writeLogEntry` 方法，而协议的遵循者则可能同时看到 `log` 和 `writeLogEntry`。如果你不希望让客户端能够创建自己的遵循 `Logger` 的类型，那么你只能通过 `public`、`internal` 和 `private` 来模拟它。另一种选择是依赖文档注释。
