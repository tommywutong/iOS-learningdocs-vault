---
title: 'Friday Q&A 2016-03-04: Swift Asserts'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2016-03-04-swift-asserts.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0f4385d81f788be5'
translated: false
---

> 原文：[Friday Q&A 2016-03-04: Swift Asserts](https://www.mikeash.com/pyblog/friday-qa-2016-03-04-swift-asserts.html)　·　mikeash.com Friday Q&A

Posted at 2016-03-04 14:30 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2016-04-15: Performance Comparisons of Common Operations, 2016 Edition](https://www.mikeash.com/pyblog/friday-qa-2016-04-15-performance-comparisons-of-common-operations-2016-edition.html)  
Previous article: [Friday Q&A 2016-02-19: What Is the Secure Enclave?](https://www.mikeash.com/pyblog/friday-qa-2016-02-19-what-is-the-secure-enclave.html)  
Tags: [assert](https://www.mikeash.com/pyblog/?tag=assert) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2016-03-04: Swift Asserts

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Chinese (translation by SwiftGG)](http://swift.gg/2016/05/11/friday-qa-2016-03-04-swift-asserts/) and [Lithuanian (translation by Giedrius Sadauskas)](http://crowfer.com/swift-teigia/).

I'm not going to spend much time discussing what asserts are in general or where to use them. This article just looks at what's available in Swift and some details of their implementations. If you want to read about how best to use asserts in your code, see my previous article [Proper Use of Asserts](https://www.mikeash.com/pyblog/friday-qa-2013-05-03-proper-use-of-asserts.html).

**APIs**  
There are two primary assert functions in the Swift standard library.

The first is creatively named `assert`. You call it with an expression that's supposed to be true, like so:

```
    assert(x >= 0) // x can't be negative here
```

It optionally takes a message that will be printed as part of the failure if the expression is false:

```
    assert(x >= 0, "x can't be negative here")
```

`assert` only functions in non-optimized builds. When optimizations are enabled, the entire thing is compiled out. This is useful for asserting conditions that are so expensive to compute that they would slow down your release builds too much, but which are still useful and important to check when debugging.

Some people prefer to only have asserts in debug builds, under the theory that it's good to have checks when debugging, but it's best not to crash the app out in the real world with real users. However, the error is present regardless of the presence of the assert that checks for it, and if it's not caught right away it's just going to cause havoc down the road. It's much better to fail quickly and obviously when it's practical to do so. That brings us to the next function.

The `precondition` function is much like `assert`. Calling it looks the same:

```
    precondition(x >= 0) // x can't be negative here
    precondition(x >= 0, "x can't be negative here")
```

The difference is that it performs the check even in optimized builds. This makes it a much better choice for most assertion checks, as long as the check is sufficiently fast.

While `precondition` remains active in a normal optimized build, it is _not_ active in an "unchecked" optimized build. Unchecked builds are done by specifying `-Ounchecked` at the command line. These not only remove `precondition` calls, but also important things like array bounds checks. This is really dangerous, so this option should probably not be used unless you really, really need the performance and there's no other way to achieve it.

One interesting note about unchecked builds is that, while the `precondition` check is removed, the optimizer will also assume that the condition is always true and use that to optimize the following code. For the above examples, the generated code will no longer check to see if `x` is negative, but it will compile the code that comes after with the assumption that `x` is always zero or greater. The same is true of `assert`.

Each of these functions has a variant without the conditional, which always signals a failure when called. These two variants are `assertionFailure` and `preconditionFailure`. This is useful when the condition you're asserting doesn't fit nicely within the call. For example:

```
    guard case .Thingy(let value) = someEnum else {
        preconditionFailure("This code should only be called with a Thingy.")
    }
```

The behavior under optimization is similar to the ones with conditions. `assertionFailure` is compiled out when optimizations are enabled. `preconditionFailure` remains in optimized builds, but is removed in unchecked optimized builds. In unchecked builds, the optimizer will assume that these functions can never be reached, and will generate code based on that assumption.

Finally, there's `fatalError`. This function always signals a failure and halts the program, regardless of the optimization level, even in unchecked builds.

**Logging Caller Info**  
When you hit an assertion failure, you get a message like this:

```
    precondition failed: x must be greater than zero: file test.swift, line 6
```

How does it get the file and line information?

In C, we'd write `assert` as a macro and use the magic `__FILE__` and `__LINE__` identifiers to get the info:

```
    #define assert(condition) do { \
            if(!(condition)) { \
                fprintf(stderr, "Assertion failed %s in file %s line %d\n", #condition, __FILE__, __LINE__); \
                abort(); \
            } \
        }
```

These end up being the caller's file and line, because the macro is expanded there. Swift doesn't have macros, so how does it work?

This works in Swift by using default argument values. There are magic identifiers which can be used as the default value for an argument. If the caller doesn't provide an explicit value, then the default value expands to the call location's file and line. Currently, these magic identifiers are `__FILE__` and `__LINE__`, but in the next Swift release they're changing to `#file` and `#line` for better consistency with the rest of the language.

To see this in action, we can look at the definition of `assert`:

```
    public func assert(
      @autoclosure condition: () -> Bool,
      @autoclosure _ message: () -> String = String(),
      file: StaticString = #file, line: UInt = #line
    )
```

Normally, you call `assert` and only pass one or two arguments. The `file` and `line` arguments are left as the default, which means that the caller's information is passed in.

You're not _required_ to leave the default values. You can pass in other values if you prefer. You could do this to, for example, lie:

```
    assert(false, "Guess where!", file: "not here", line: 42)
```

This produces:

```
    assertion failed: Guess where!: file not here, line 42
```

For a more practical use, this allows you to write wrappers that preserve the original call site's information. For example:

```
    func assertWrapper(
        @autoclosure condition: () -> Bool,
        @autoclosure _ message: () -> String = String(),
        file: StaticString = #file, line: UInt = #line
    ) {
        if !condition() {
            print("Oh no!")
        }
        assert(condition, message, file: file, line: line)
    }
```

There is one missing piece from the Swift version of `assert`. In the simple C version above, the expression for the failed assertion is printed by using `#condition` to get a stringified version of that parameter. Unfortunately, there is no equivalent in Swift, so while Swift can print the file and line number where the failure occurred, it's not able to print the expression that was supposed to be true.

**Autoclosures**  
These functions use the `@autoclosure` attribute on the `condition` and `message` arguments. Why is that?

First, a quick recap in case you're not familiar with what `@autoclosure` does. The `@autoclosure` argument can be applied to an argument of function type which takes no parameters. At the call site, the caller provides an expression for that argument. This expression is then implicitly wrapped in a function, and that function is passed in as the parameter. Here's an example:

```
    func f(@autoclosure value: () -> Int) {
        print(value())
    }

    f(42)
```

This is equivalent to:

```
    func f(value: () -> Int) {
        print(value())
    }

    f({ 42 })
```

What's the point of passing in an expression as a function? It allows the callee to control when that expression is evaluated. For example, consider the boolean and operator. We could implement this to take two `Bool` parameters:

```
    func &&(a: Bool, b: Bool) -> Bool {
        if a {
            if b {
                return true
            }
        }
        return false
    }
```

This works fine for some things:

```
    x > 3 && x < 10
```

However, it's wasteful if the right-hand side operand is expensive to compute:

```
    x > 3 && expensiveFunction(x) < 10
```

It can be downright crashy if we assume the right-hand side doesn't execute when the left-hand side is false:

```
    optional != nil && optional!.value > 3
```

Like C, Swift's `&&` operator short-circuits. That means that if the left-hand side is false, the right-hand side is never even evaluated. That makes this expression safe with Swift's implementation, but not with ours. `@autoclosure` lets the function control when the expression is evaluated, to ensure that it's only evaluated when the left-hand side is true:

```
    func &&(a: Bool, @autoclosure b: () -> Bool) -> Bool {
        if a {
            if b() {
                return true
            }
        }
        return false
    }
```

Now the semantics match Swift's semantics, because when `a` is false then `b` is never called.

How does this apply to the asserts? It's all about performance. The assert's message may be expensive to compute. Imagine:

```
    assert(widget.valid, "Widget wasn't valid: \(widget.dump())")
```

You don't want to compute that big string every time through, even when the widget is valid and nothing is going to be printed. By using `@autoclosure` for the message argument, `assert` can avoid evaluating the `message` expression unless the assert actually fails.

The condition itself is also an `@autoclosure`. Why? Because `assert` doesn't check the condition in optimized builds. If it doesn't check the condition, there's no point in even evaluating it. Using `@autoclosure` means that this doesn't slow down optimized builds:

```
    assert(superExpensiveFunction())
```

All of the functions in this API use `@autoclosure` to ensure that the parameters aren't evaluated unless they really need to be. For some reason, even `fatalError` uses it, even though `fatalError` executes unconditionally.

**Code Removal**  
These functions are removed from the generated code depending on how your code is compiled. They exist in the Swift standard library, not your code, and the standard library was compiled long before your code was. How does that work?

In C, it's all about the macros. Macros just exist in the header, so their code is compiled at the call site. Even if they're conceptually part of a library, they're actually just dumped straight into your own code. That means they can check for the existence of a `DEBUG` macro or similar, and produce no code when it's not set. For example:

```
    #if DEBUG
    #define assert(condition) do { \
            if(!(condition)) { \
                fprintf(stderr, "Assertion failed %s in file %s line %d\n", #condition, __FILE__, __LINE__); \
                abort(); \
            } \
        }
    #else
    #define assert(condition) (void)0
    #endif
```

And again, Swift doesn't have macros, so how does this work?

If you [look at the definition of these functions in the standard library](https://github.com/apple/swift/blob/0619e57a61f27f721e273ab6f808ac81011aeb2c/stdlib/public/core/Assert.swift), you'll see that they're all annotated with `@_transparent`. This attribute makes the function a little bit macro-like. Every call is inlined at the call site rather than emitted as a call to a separate function. When you write `precondition(...)` in Swift code, the body of the standard library `precondition` function gets pulled into your code and treated as if you had copy/pasted it in yourself. That means that it gets compiled under the same conditions as the rest of your code, and the optimizer is able to see all the way into the function body. It can see that nothing happens in `assert` when optimizations are enabled and remove the entire thing.

The standard library is a separate library. How can functions from a separate library be inlined into your own code? Coming from a C universe where libraries consist of compiled object code, this makes no sense.

The Swift standard library is provided as a `.swiftmodule` file, which is a completely different beast from a `.dylib` or `.a` file. A `.swiftmodule` file contains declarations for everything in the module, but it can also contain full implementations. To quote [the module format documentation](https://github.com/apple/swift/blob/cf8baedee2b09c9dd2d9c5519bf61629d1f6ebc8/docs/Serialization.rst):

> The SIL block contains SIL-level implementations that can be imported into a client's SILModule context.

That means that the full bodies of the various `assert` functions are saved, in an intermediate form, into the standard library module. Those bodies are then available to be inlined wherever you call them. Since they're inlined, they have access to the context in which they're compiled, and the optimizer can remove them entirely when it's warranted.

**Conclusion**  
Swift provides a nice set of assert functions. The `assert` function and its companion `assertionFailure` are only active in non-optimized builds. This can be useful for checking conditions that are slow to compute, but should usually be avoided. The `precondition` and `preconditionFailure` functions are active in normal optimized builds as well.

These functions use the `@autoclosure` attribute on their `condition` and `message` parameters, which allows them to control when those parameters are evaluated. This prevents custom assert messages from being evaluated every time an assertion is checked, and it prevents assertion conditions from being evaluated when the assertion is disabled in optimized builds.

The assert functions are part of the standard library, but their use of the `@_transparent` attribute causes the generated intermediate code to be emitted into the module file. When they're called, the entire body is inlined at the call site, which allows the optimizer to remove the call entirely when it's appropriate.

That's it for today! I hope knowing what's going on might encourage you to use more asserts in your code. They can help a lot by making problems show themselves immediately and obviously, rather than causing subtle symptoms long after the initial problem occurred. Come back next time for more exciting ideas. Until then, Friday Q&A is driven by reader ideas, so if you have a topic you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
