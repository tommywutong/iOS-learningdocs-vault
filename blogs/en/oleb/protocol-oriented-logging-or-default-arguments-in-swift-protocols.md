---
title: 'Protocol-Oriented Logging, or: Default Arguments in Swift Protocols'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/05/default-arguments-in-protocols/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:67b600f8b34491ed'
translated: false
---

> 原文：[Protocol-Oriented Logging, or: Default Arguments in Swift Protocols](https://oleb.net/blog/2016/05/default-arguments-in-protocols/)　·　Ole Begemann

# Protocol-Oriented Logging, or: Default Arguments in Swift Protocols

**Swift 2.2 doesn’t permit default arguments in protocol declarations. This is a problem if you want to abstract your app’s logging code with a protocol because default arguments are used to pass the source location to the log function. However, you _can_ use default arguments in protocol extensions, and that enables a workaround.**

A typical [log](https://en.wikipedia.org/wiki/Logfile) message should include the source location (filename, line number, and possibly function name) of the log event. Swift provides the `#file`, `#line`, `#column`, and `#function` [debug identifiers](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Expressions.html#//apple_ref/doc/uid/TP40014097-CH32-ID390) for this purpose. At compile time, the parser will expand these placeholders to string or integer literals that describe the current source location. Since it would be incredibly repetitive if we had to include these arguments in every single call of a log function, they are usually passed as default arguments. This works because the compiler is smart enough to expand the debug identifiers to the [call site](https://en.wikipedia.org/wiki/Call_site) location when they are evaluated in a default argument list. Take the [`assert`](http://swiftdoc.org/v2.2/func/assert/#func-assert_-bool_-string-file_-staticstring-line_-uint) function from the standard library [as an example](https://developer.apple.com/swift/blog/?id=15). It is declared like this:

```
func assert(
    @autoclosure condition: () -> Bool,
    @autoclosure _ message: () -> String = default,
    file: StaticString = #file,
    line: UInt = #line)
```

The third and fourth arguments expand to the caller’s source location by default. (If you’re wondering about the [`@autoclosure`](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Closures.html#//apple_ref/doc/uid/TP40014097-CH11-ID543) attribute, it wraps an expression in a closure, effectively delaying the evaluation of the expression from the call site to the function body without requiring the caller to use an explicit closure expression. `assert` uses it to perform the evaluation of the condition (which could potentially be expensive or have side effects) only in debug builds, and the evaluation of the message only if the assertion fails.)

# A simple, global log function

You can use the same approach to write a `log` function that takes a log message and a log level. Its interface and implementation could look like this:

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
    // Use `print` for logging.
    // We don’t care about `logLevel` at the moment.
    print("\(logLevel) – \(file):\(line) – \(function) – \(message())")
}
```

You could argue either way whether `message` should be an `@autoclosure` here. The attribute provides no benefit in this simple example because the message is evaluated in any case. We will change that in the next step, however.

# A concrete type

Instead of the global `log` function, let’s create a type named `PrintLogger` that is initialized with a minimum log level. It will only log events whose log level is at least as severe as the minimum. `LogLevel` needs to be `Comparable` for this, which is why I declared it to store an `Int` raw value above:

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

You would use `PrintLogger` like this:

```
let logger = PrintLogger(
    minimumLogLevel: .warning)
logger.log(.error, "This is an error log")
    // gets logged
logger.log(.debug, "This is a debug log")
    // does nothing
```

# A protocol with default arguments

Next, I’d like to create a `Logger` protocol as an abstraction for `PrintLogger`. This would allow me to later replace the simple logging using `print` statements with a more sophisticated implementation that logs to a file or sends logs to a server. However, I hit a roadblock here because Swift doesn’t allow default arguments in protocol declarations. This does not compile:

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

So I would have to omit the default arguments to make the protocol compile. That doesn’t seem to be a problem at first. `PrintLogger` can adopt the protocol with an empty extension — its existing implementation already fulfills the requirements. And using the logger through a variable of type `logger: PrintLogger` works as before.

The problem becomes apparent if you try to use the logger through a variable of the protocol type, `logger2: Logger`, as you would in code that is not supposed to know about the concrete implementation:

```
let logger2: Logger = PrintLogger(
    minimumLogLevel: .warning)
logger2.log(.error, "An error occurred")
    // error: Missing argument in call
logger2.log(.error, "An error occurred",
    file: #file, line: #line, function: #function)
    // works but 😱
```

`logger2` only knows about a `log` method with five required arguments, so you would have to specify all of them every single time. Yuck!

## Move the default arguments into a protocol extension

The solution is to declare two versions of the `log` method: one, with no default arguments, in the protocol declaration, as before. I named this method `writeLogEntry`. Two, in a protocol extension on `Logger`, this time including the default arguments (which is permitted). I kept the name `log` for this method because it is supposed to be the public interface of the protocol.

Now, the implementation of `log` consists of a single line: it calls through to `writeLogEntry`, passing all of its arguments and thereby the source location it received from its caller through the default arguments. `writeLogEntry` on the other hand is the method that adopters of the protocol must implement to perform the actual logging. This is the complete protocol:

```
protocol Logger {
    /// Writes a log entry. Types that
    /// conform to `Logger` must implement
    /// this to perform their work.
    ///
    /// - Important: Clients of `Logger`
    ///   should never call this method.
    ///   Always call `log(_:,_:)`.
    func writeLogEntry(
        logLevel: LogLevel,
        @autoclosure _ message: () -> String,
        file: StaticString,
        line: Int,
        function: StaticString)
}

extension Logger {
    /// The public API for `Logger`. Calls
    /// `writeLogEntry(_:,_:,file:,line:,function:)`.
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

In the parlance of [session 408](https://developer.apple.com/videos/play/wwdc2015/408/), `writeLogEntry` is a _protocol requirement_ and hence a _customization point_ for the protocol, whereas `log` is not backed by a requirement and statically dispatched. This is what we want. The only task of the `log` method is to immediately forward to `writeLogEntry`, which contains the actual logic. Types that implement `Logger` have no reason to override `log`.

This is the complete `PrintLogger` type, adopting the protocol:

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

Now you can use the protocol as expected:

```
let logger3: Logger = PrintLogger(
    minimumLogLevel: .verbose)
logger3.log(.error, "An error occurred") // 🎉
```

## API visibility to clients

One downside of this approach is that it is not easily possible to clearly indicate the purpose of the `log` and `writeLogEntry` to users of the protocol through [access control](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/AccessControl.html). Ideally, clients using the protocol should not see the `writeLogEntry` method, whereas adopters may see both `log` and `writeLogEntry`. You can only model this with `public`, `internal`, and `private` if you don’t want to give clients the possibility to create their own types that adopt `Logger`. The alternative is to rely on documentation comments.
