---
title: 'Friday Q&A 2017-08-25: Swift Error Handling Implementation'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2017-08-25-swift-error-handling-implementation.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:57f2928a2130625b'
translated: false
---

> 原文：[Friday Q&A 2017-08-25: Swift Error Handling Implementation](https://www.mikeash.com/pyblog/friday-qa-2017-08-25-swift-error-handling-implementation.html)　·　mikeash.com Friday Q&A

Posted at 2017-08-25 13:13 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Corporate Training, NYC Workshop, and Book Update](https://www.mikeash.com/pyblog/corporate-training-nyc-workshop-and-book-update.html)  
Previous article: [Friday Q&A 2017-08-11: Swift.Unmanaged](https://www.mikeash.com/pyblog/friday-qa-2017-08-11-swiftunmanaged.html)  
Tags: [assembly](https://www.mikeash.com/pyblog/?tag=assembly) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2017-08-25: Swift Error Handling Implementation

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Korean (translation by pilgwon)](https://pilgwon.github.io/blog/2017/09/03/Swift-Error-Handling-Implementation.html).

**Semantics**  
Let's start with a quick refresher on how Swift errors work at the language level.

Any Swift function can be decorated with a `throws` keyword, which indicates that it can throw an error:

```
    func getStringMightFail() throws -> String { ...
```

To actually throw an error from such a function, use the `throw` keyword with a value that conforms to the `Error` protocol:

```
        throw MyError.brainNotFound
```

When calling a `throws` function, you must include the `try` keyword:

```
    let string = try getStringMightFail()
```

The `try` keyword doesn't do anything, but is a required marker to indicate that the function might throw an error. The call must be in a context where throwing an error is allowed, either in a `throws` function, or in a `do` block with a `catch` handler.

To write a `catch` handler, place the `try` call in a `do` block, and add a `catch` block:

```
    do {
        let string = try getStringMightFail()
        ...
    } catch {
        print("Got an error: \(error)")
    }
```

When an error is thrown, execution jumps to the `catch` block. The value that was thrown is available in `error`. You can get fancy with type checking and conditions and multiple `catch` clauses, but these are the basics. For more information about all the details, see the [Error Handling](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/ErrorHandling.html) section of [The Swift Programming Language](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/index.html).

That's what it does. How does it work?

**Implementation**  
To find out how it works, I wrote some dummy code with error handling that I could disassemble:

```
    struct MyError: Error {
        var x: Int
        var y: Int
        var z: Int
    }

    func Thrower(x: Int, y: Int, z: Int) throws -> Int {
        throw MyError(x: x, y: y, z: z)
    }

    func Catcher(f: (Int, Int, Int) throws -> Int) {
        do {
            let x = try f(1, 2, 3)
            print("Received \(x)")
        } catch {
            print("Caught \(error)")
        }
    }
```

Of course, now that Swift is open source, I could just go look at the compiler code and see what it does. But that's no fun, and this is easier.

It turns out that Swift 3 and Swift 4 do it differently. I'll briefly discuss Swift 3, then look a bit deeper at Swift 4, since that's up and coming.

Swift 3 works by essentially automating Objective-C's `NSError` convention. The compiler inserts an extra, hidden parameter which is essentially `Error *`, or `NSError **`. Throwing an error consists of writing the error object to the pointer passed in that parameter. The caller allocates some stack space and passes its address in that parameter. On return, it checks to see if that space now contains an error. If it does, it jumps to the `catch` block.

Swift 4 gets a little fancier. The basic idea is the same, but instead of a normal extra parameter, a special register is reserved for the error return. Here's what the relevant assembly code in `Thrower` looks like:

```
    call       imp___stubs__swift_allocError
    mov        qword [rdx], rbx
    mov        qword [rdx+8], r15
    mov        qword [rdx+0x10], r14
    mov        r12, rax
```

This calls into the Swift runtime to allocate a new error, fills it out with the relevant values, and then places the pointer into `r12`. It then returns to the caller. The relevant code in `Catcher` looks like this:

```
    call       r14
    mov        r15, rax
    test       r12, r12
    je         loc_100002cec
```

It makes the call, then checks if `r12` contains anything. If it does, it jumps to the `catch` block. The technique on ARM64 is almost the same, with the `x21` register serving as the error pointer.

Internally, it looks a lot like returning a `Result` type, or otherwise returning some sort of error code. The `throws` function returns the thrown error to the caller in a special place. The caller checks that place for an error, and jumps to the error handling code if so. The generated code looks similar to Objective-C code using an `NSError **` parameter, and in fact Swift 3's version of it is identical.

**Comparison With Exceptions**  
Swift is careful never to use the word "exception" when discussing its error handling system, but it looks a lot like exceptions in other languages. How does its implementation compare? There are a lot of languages out there with exceptions, and many of them do things differently, but the natural comparison is C++. Objective-C exceptions (which do exist, although pretty much nobody uses them) use C++'s exceptions mechanism on the modern runtime.

A full exploration of how C++ exceptions work could fill a book, so we'll have to settle for a brief description.

C++ code that calls throwing functions (which is the default for C++ functions) produces assembly exactly as if it called non-throwing functions. Which is to say, it passes in parameters and retrieves return values and gives no thought to the possibility of exceptions.

How can this possibly work? In addition to generating the no-exceptions code, the compiler also generates a table with information about how (and whether) the code handles exceptions and how to safely unwind the stack to exit out of the function in the event that an exception is thrown.

When some function throws an exception, it walks up the stack, looking up each function's information and using that to unwind the stack to the next function, until it either finds an exception handler or runs off the end. If it finds an exception handler, it transfers control to that handler which then runs the code in the `catch` block.

For more information about how C++ exceptions work, see [C++ ABI for Itanium: Exception Handling](https://itanium-cxx-abi.github.io/cxx-abi/abi-eh.html).

This system is called "zero-cost" exception handling. The term "zero-cost" refers to what happens when no exceptions are ever thrown. Because that code is compiled exactly as it would be without exceptions, there's no runtime overhead for supporting exceptions. Calling potentially-throwing functions is just as fast as calling functions that don't throw, and adding `try` blocks to your code doesn't result in any additional work done at runtime.

When an exception _is_ thrown, the concept of "zero-cost" goes out the window. Unwinding the stack using the tables is an expensive process and takes a substantial amount of time. The system is designed around the idea that exceptions are thrown rarely, and performance in the case where no exceptions are ever thrown is more important. This assumption is likely to be true in almost all code.

Compared to this, Swift's system is extremely simple. It makes no attempt to generate the same code for `throws` and non-`throws` functions. Instead, every call to a `throws` function is followed by a check to see if an error was returned, and a jump to the appropriate error handling code if so. These checks aren't free, although they should be pretty cheap.

The tradeoff makes a lot of sense for Swift. Swift errors look a lot like C++ exceptions, but in practice they're used differently. Nearly any C++ call can potentially throw, and even basic stuff like the `new` operator will throw to indicate an error. Explicitly checking for a thrown exception after every call would add a lot of extra checks. In contrast, few Swift calls are marked `throws` in typical codebases, so the cost of explicit checks is low.

**Conclusion**  
Swift's error handling invites comparison with exceptions in other languages, such as C++. C++'s exception handling is extremely complicated internally, but Swift takes a different approach. Instead of unwind tables to achieve "zero-cost" in the common case, Swift returns thrown errors in a special register, and the caller checks that register to see if an error has been thrown. This adds a bit of overhead when errors aren't thrown, but avoids making things enormously complicated the way C++ does. It would take serious effort to write Swift code where the overhead from error handling makes any noticeable difference.

That's it for today! Come back again for more excitement, fun, and horror. As I have occasionally mentioned before, Friday Q&A is driven by reader suggestions. As always, if you have a topic you'd like to see covered here, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
