---
title: 'Friday Q&A 2015-06-19: The Best of What''s New in Swift'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-06-19-the-best-of-whats-new-in-swift.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ada76489a0c996b2'
translated: false
---

> 原文：[Friday Q&A 2015-06-19: The Best of What's New in Swift](https://www.mikeash.com/pyblog/friday-qa-2015-06-19-the-best-of-whats-new-in-swift.html)　·　mikeash.com Friday Q&A

Posted at 2015-06-19 13:12 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2015-07-03: Address Sanitizer](https://www.mikeash.com/pyblog/friday-qa-2015-07-03-address-sanitizer.html)  
Previous article: [I Do Not Agree To Your Terms](https://www.mikeash.com/pyblog/i-do-not-agree-to-your-terms.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2015-06-19: The Best of What's New in Swift

by [Mike Ash](https://www.mikeash.com/)

**Function Pointers**  
This is my favorite new Swift feature by far. It's a relatively small but important feature that closes the last big hole remaining in Swift's bridging to C.

Previously, Swift treated C function pointer types as opaque types. If something returned a function pointer, you could obtain the value. If something accepted a function pointer as a parameter, you could pass that value. But there was no way to call a function pointer, and more importantly no way to create one that referred to your Swift code. You got a `CFunctionPointer` value that you could use for almost nothing. The only reasonable way to interact with these APIs was to write C or Objective-C APIs that wrapped them.

The terrible world of `CFunctionPointer` is gone in Swift 2. Instead, Swift function types have trifurcated into variants. Any Swift function type can optionally be annotated with a `@convention` specifier which says what kind of function it is. The `swift` convention is the default and indicates a normal Swift function. The `block` convention indicates an Objective-C block type. These were automatically bridged, and still are, but now the typing is more explicit. Finally, the `c` convention indicates a C function pointer. Function types annotated with `@convention(c)` still behave mostly normally, so you can call them and pass them as usual.

I said "mostly" above because C function pointers have significant limitations which are necessarily reflected in Swift. Specifically, C function pointers are pure pointers to code, with no associated data. Swift functions often have implicit associated data, such as methods in an object, or closures which capture values from the enclosing scope. Because of this mismatch, only global Swift functions or nested or anonymous functions with no captured data can be passed as `@convention(c)` parameters.

Here's an example of this new feature at work:

```
    atexit({ print("Goodbye!") })
```

This will print "Goodbye!" when the program exits.

To illustrate the limitations, this code will not work (unless placed at the global scope):

```
    let x = 42
    atexit({ print("The answer is \(x)") })
```

The compiler complains: "A C function pointer cannot be formed from a closure that captures context."

This limitation is only to be expected, and is what we've always had to deal with in C anyway. Despite that, this is still extremely useful and lets us use a common class of C APIs which were basically off limits from Swift before.

**Protocol Extensions**  
This is my favorite new Swift feature by far. Protocol extensions allow protocols to contain method implementations, not just method declarations. This is a feature I've wanted in Objective-C for ages, and I'm glad to see it show up even if it took a new language.

Previously, in both Objective-C and Swift, protocols contained only method declarations. They were pure interface definitions, just a list of things for conforming types to implement. With protocol extensions in Swift 2, protocols can now contain method _implementations_ as well as declarations.

Often there's some functionality that can apply to all types that conform to a certain interface. For example, all collections can support the concept of mapping over the collection to create a new one. With the old style of protocols, there were two ways to give all collections this capability. You could either put the method in the protocol and require each conforming type to implement it, or you could write a global function that works on values of the protocol type.

Cocoa mostly went with the former solution. Although they're not formally part of any protocol, the various Cocoa collections tend to have similar functionality such as `enumerateObjectsUsingBlock:` which each one implements separately.

Swift previously went with the latter solution. Global functions like `map` operated on any `CollectionType`. This allows for a nice shared implementation, but awkward syntax and no ability to override the implementation to specialize it for a particular type.

With protocol extensions, there's a third option that's far superior. `map` can be implemented in an extension on the `CollectionType` protocol. All types which conform to `CollectionType` then automatically get an implementation of a `map` method for free.

As an example, here's a simple reimplementation of `map':

```
    extension CollectionType {
        func myMap<U>(f: Self.Generator.Element -> U) -> [U] {
            var result: [U] = []
            for elt in self {
                result.append(f(elt))
            }
            return result
        }
    }

    [1, 2, 3, 4].myMap({ $0 * 2 })
    // This produces [2, 4, 6, 8]
```

This previously could have been done as an extension on `Array`, but then would only be available on `Array`. With a protocol extension, it also applies to `Set` and `ArraySlice` and every other implementation of `CollectionType` without any additional effort.

One really interesting feature of Swift protocol extensions is that they can be given type constraints. For example, you might want to implement a `max` property. But `max` doesn't conceptually work with all collections, only collections of objects that have some sort of ordering. That's not a problem! Just add a requirement to the extension that the collection elements must be `Comparable`:

```
    extension CollectionType where Self.Generator.Element: Comparable {
        var max: Self.Generator.Element {
            var best = self[self.startIndex]
            for elt in self {
                if elt > best {
                    best = elt
                }
            }
            return best
        }
    }

    Set([5, 4, 3, 2, 1]).max
    // This produces 5

    [NSObject(), NSObject()].max
    // This produces an error, as NSObject is not Comparable
```

There's one wrinkle with protocol extensions, which is a subtle but important distinction which determines whether protocol extension methods are subject to dynamic dispatch.

A method in a protocol extension _may_ also be declared in the protocol itself, or it may exist solely in the extension. Methods which exist solely in the extension are _not_ dynamically dispatched and cannot be overridden. Methods which are also declared in the protocol itself are dynamically dispatched and can be overridden. This is a bit difficult to explain, here's an example:

```
    protocol P {
        func a()
    }

    extension P {
        func a() {
            print("default implementation of A")
        }

        func b() {
            print("default implementation of B")
        }
    }

    struct S: P {
        func a() {
            print("specialized implementation of A")
        }

        func b() {
            print("specialized implementation of B")
        }
    }

    let p: P = S()
    p.a()
    p.b()
```

This will print "specialized implementation of A" followed by "default implementation of B." Although the `struct` contains an implementation of `b`, it does not override the protocol's `b`, because the main protocol doesn't contain a declaration of `b`. The distinction is ultimately between methods in the protocol which _happen to have_ a default implementation, and method implementations that are attached to the protocol.

This is a bit of a weird spot with protocol extensions and I'm hoping that Apple will improve upon this somehow as the beta cycle proceeds. As it stands, it's not a big problem, just something to be aware of.

(My brief and modest proposal for a fix: borrow the `final` keyword to indicate "no dynamic dispatch" on protocol extension messages.)

I believe protocol extensions may also be Apple's answer to the question of optional protocol methods. Pure Swift protocols couldn't, and still can't, contain optional methods. We're used to having optional methods in Objective-C protocols for things like delegates:

```
    @protocol MyClassDelegate
    @optional

    - (BOOL)shouldDoThingOne;
    - (BOOL)shouldDoThingTwo

    @end
```

The users of the protocol would then check `respondsToSelector:` before invoking these methods. Pure Swift has no equivalent:

```
    protocol MyClassDelegate {
        func shouldDoThingOne() -> Bool
        func shouldDoThingTwo() -> Bool
    }
```

Previously, anything that implemented this protocol was required to implement these methods. This conflicts with Cocoa's notion of a delegate as being able to provide _optional_ customizations, with sensible default behaviors. With protocol extensions in Swift 2, the sensible default behaviors can now be provided in the protocol itself:

```
    extension MyClassDelegate {
        func shouldDoThingOne() -> Bool {
            // Thing one is harmless and should almost always be done
            return true
        }

        func shouldDoThingTwo() -> Bool {
            // Thing two is a menace and should not be done without careful consideration
            return false
        }
    }
```

This provides the same ultimate functionality as `@optional` in Objective-C, but without requiring runtime checks.

**Error Handling**  
This is my favorite new Swift feature by far. Many people despaired when Swift showed up with no support for exceptions. Yet this despair was somewhat abstract, since Objective-C doesn't really support exceptions either. The syntax, compiler, and runtime support for exceptions is there, but writing code that can tolerate exceptions being thrown through it is hard, and most people don't do it. ARC drove this point home when it arrived, as ARC's own generated code isn't exception safe by default.

Because of this state of affairs, Objective-C _de facto_ only uses exceptions to signal programming errors. There are a handful of, uh, exceptions to this, but Cocoa code generally uses exceptions only to signal assertion failures. Third-party code typically follows along. Which is kind of weird, since the whole idea with exceptions is that you can catch them and continue execution, but doing that after an assertion failure is a really, really bad idea.

Since exceptions can't really be used to signal recoverable errors in Objective-C in practice, Cocoa adopted the `NSError **` convention, where any method that can signal an error takes an extra `NSError **` parameter and uses that to return information about the failure. This works, but it turns the code into a terrible slog because the `NSError **` interface just isn't very nice.

It also encourages ignoring errors, since by convention these parameters accept `NULL` to mean "I don't care about the error, don't give it to me." I can't tell you how many times I've seen fellow programmers scratching their head over why some piece of code won't work, and they're passing `NULL` for the error parameter. The computer is trying to tell you what's going wrong, if you'd just listen!

Swift 2 introduces an error handling facility that attempts to find a middle ground between the two techniques. Syntactically, it resembles exceptions. Semantically, it's more like `NSError **`. The result is unusual but looks pretty good.

Let's look at an example. Writing a file to disk is a common operation that can fail. In Cocoa, it looks like this:

```
    NSError *error;
    BOOL success = [data writeToFile: path options: options error: &error];
    if(!success) {
        // respond to the error somehow
        return;
    }
    // proceed normally
```

In a world where Cocoa used exceptions to signal these kinds of errors, this code would look something like:

```
    @try {
        [data writeToFile: path options: options];
        // proceed normally
    } @catch(NSError *error) {
        // respond to the error somehow
    }
```

In Swift 2, you write:

```
    do {
        try data.writeToFile(path, options: options)
        // proceed normally
    } catch {
        // respond to the error somehow
    }
```

This is superficially similar to the code with exceptions, but there are some important differences in Swift's approach.

Swift errors are checked by the compiler. This is similar to languages like Java where the possibility of throwing exceptions is part of a method's type signature. It's radically different from Objective-C and a lot of other languages where anything and everything can potentially throw an exception.

When exceptions are completely unchecked, that means that either every bit of code has to be written with the possibility that an exception will be thrown through it, or you have to know from other sources (documentation, reading the source code) which methods can throw and which can't. With the Swift approach, if you forget that `writeToFile` throws, the compiler will tell you. With the Objective-C approach, your code will compile and run and work just fine until the write fails someday, at which point you suddenly find yourself working as a 19th century Cockney bootblack, pondering the meaning of "undefined behavior" in between shining Victorians' shoes.

One feature of Swift error handling that is unique (as far as I know) is that the `try` keyword is required for _each statement_ that can throw. With Java-style checked exceptions, the only requirement is that a throwing method either exist within a method that can throw the appropriate type, or within a suitable `try` block. To illustrate the difference, consider these two pieces of hypothetical code:

```
    // Java style
    try {
        String name = textField.value();
        Data nameBytes = name.getBytes("UTF-8");
        nameBytes.writeToFile(path);
        proceedWithName(name);
    } catch(IOException exception) {
        ...
    }

    // Swift style
    do {
        let name = textField.value
        let nameBytes = name.dataUsingEncoding(NSUTF8StringEncoding)!
        try nameBytes.writeToFile(path, options: [])
        proceedWithName(name)
    } catch {
        ...
    }
```

Quick, which calls in the first version can throw? There's no way to know unless you know (or look up) the interface for every call used in the `try` block. Now, which calls in the second version can throw? That's easy: the `writeToFile` call.

You might say that it's pretty obvious what throws just from looking at the calls. But maybe `proceedWithName` can also produce an error and throw. Compare:

```
    // Java style
    try {
        String name = textField.value();
        Data nameBytes = name.getBytes("UTF-8");
        nameBytes.writeToFile(path);
        proceedWithName(name);
    } catch(IOException exception) {
        ...
    }

    // Swift style
    do {
        let name = textField.value
        let nameBytes = name.dataUsingEncoding(NSUTF8StringEncoding)!
        try nameBytes.writeToFile(path, options: [])
        try proceedWithName(name)
    } catch {
        ...
    }
```

The Java version doesn't change, while the Swift one shows that there are now two calls that can potentially fail.

In Java, you'd typically want to put as few things into the `try` block as possible, just to make it obvious which bits can throw and which bits are incidental. In Swift, you don't have to worry about it, since each throwing statement is clearly marked.

This becomes even more significant when an entire method is marked as `throws`. With Java-style checked exceptions, once you've declared that some method `throws IOException` then potentially anything within it could throw that type. With Swift, a method marked as `throws` still needs to annotate each potentially-throwing call with `try`, so it's still obvious.

Another nice difference from Java is a built-in "really, this can't fail" mechanism, in the form of `try!` Sometimes there's a method that can fail only in some circumstances, and you _know_ that it can't fail the way you're using it. The `getBytes` call above is a good example of this in Java: it `throws UnsupportedEncodingException` but it's guaranteed never to throw with UTF-8. The call needs a dummy `try` wrapper even though you know it can't fail. In Swift, you can use `try!` to accomplish this, which is both clearer and shorter. This fits nicely with the `!` suffix for unwrapping optionals that you know cannot be `nil`, as used with `dataUsingEncoding` above, and the `as!` operator for downcasts you know will succeed.

An interesting contrast with Java is that while Swift errors are checked, only the fact that an error can be thrown is checked. When a Java method is annotated with `throws`, you specify the types that can be thrown. The caller then knows that it only needs to check for those types, and the compiler typechecks everything accordingly. Swift only annotates `throws` with no type information. This type information is useful in Java but can also be annoyingly restrictive when nesting `throws` calls. It will be interesting to see how it works out in Swift.

**Guard Statements**  
This is my favorite new Swift feature by far. It's small and simple nearly to the point of being redundant, but it can make code much nicer to read and write.

The `guard` statement is essentialy an inverse `if` statement. In an `if` statement you write:

```
    if condition {
        // true branch
    } else {
        // false branch
    }
```

With `guard`, the true branch pops out to the upper level after the false branch:

```
    guard condition else {
        // false branch
    }
    // true branch
```

Note that the false branch _must_ terminate execution within the enclosing scope somehow, such as by returning a value or throwing an error. You're guaranteed that the code in the true branch only executes in the case where the condition is true.

This makes `guard` a natural way to check non-fatal preconditions without running into the "pyramid of doom" that comes with multiple nested `if` statements, and without inverting conditions. For example, here's a typical pyramid:

```
    let fd1 = open(...)
    if fd1 >= 0 {
        let fd2 = open(...)
        if fd2 >= 0 {
            // use fd1 and fd2 here
            close(fd2)
        } else {
            // handle fd2 error
        }
        close(fd1)
    } else {
        // handle fd1 error
    }
```

This is pretty ugly, and as you stack them up it just gets worse. The primary code gets indented a lot and the error handling code gets exiled to a distant land far from the origin of the failure it's supposed to handle. We can avoid that by inverting the conditions:

```
    let fd1 = open(...)
    if fd1 == -1 {
        // handle fd1 error
        return
    }

    let fd2 = open(...)
    if fd2 == -1 {
        // handle fd2 error
        close(fd1)
        return
    }

    // use fd1 and fd2 here
    close(fd1)
    close(fd2)
```

This is decent, but it's a bit annoying that the conditions are now flipped to check for the error case rather than the good case. Worse is the fact that if you forget a `return` statement, the compiler doesn't care and your code will happily continue executing after the error case. `guard` solves both of these problems:

```
    let fd1 = open(...)
    guard fd1 >= 0 else {
        // handle fd1 error
        return
    }

    let fd2 = open(...)
    guard fd2 >= 0 else {
        // handle fd2 error
        close(fd1)
        return
    }

    // use fd1 and fd2 here
    close(fd1)
    close(fd2)
```

Better! This reads more clearly and I get more help from the compiler. But it's not that special, so why is it my favorite? It's because, like an `if` statement, `guard` statements can contain variable declarations and check for `nil`. Unlike `if` statements, the declared variables are available in the scope that contains the `guard` statement, not just within the statement's own scope. To illustrate, let's look an an optionals version of the above example, first with the pyramid of doom:

```
    if let file1 = Open(...) {
        if let file2 = Open(...) {
            // use file1 and file2
            file2.close()
        } else {
            // handle file2 error
        }
        file1.close()
    } else {
        // handle file1 error
    }
```

Let's invert the conditionals like before:

```
    if !let file1 =
```

Oops! You can't invert a `let`. Let's try again:

```
    let file1 = Open(...)
    if file1 == nil {
        // handle file1 error
        return
    }

    let file2 = Open(...)
    if file2 == nil {
        // handle file2 error
        file1.close()
```

Oops! The optional isn't unwrapped anymore. We'll have to do that separately. Let's try again:

```
    let file1Optional = Open(...)
    if file1Optional == nil {
        // handle file1 error
        return
    }
    let file1 = file1Optional!

    let file2Optional = Open(...)
    if file2Optional == nil {
        // handle file2 error
        file1.close()
        return
    }
    let file2 = file2Optional!

    // use file1 and file2 here
    file1.close()
    file2.close()
```

Got it. That's an unpleasant mess, though. `guard` makes it nice:

```
    guard let file1 = Open(...) else {
        // handle file1 error
        return
    }
    guard let file2 = Open(...) else {
        // handle file2 error
        file1.close()
        return
    }

    // use file1 and file2 here
    file1.close()
    file2.close()
```

Much better! The only really annoying thing here is the repetition of `file1.close()` and the fact that the cleanup code is so far away from the initialization code, which brings us to....

**Defer Statements**  
This is my favorite new Swift feature by far. The `defer` statement is much like the `finally` statement in many other languages, except it doesn't have to be bundled with a `try` statement, and you can put it just about anywhere you want. You write `defer { ... }` and the code in that block will be executed when control leaves the enclosing scope, whether it left by running off the end, or hitting a `return` statement, or throwing an error.

This lets you put cleanup code next to the stuff it cleans up, instead of at the end. For example:

```
    let tmpMemory = malloc(...)
    defer { free(tmpMemory) }

    // use tmpMemory here
```

It goes well with `guard` so that creation, error handling, and cleanup can all live together. Here's the above example using `defer`:

```
    guard let file1 = Open(...) else {
        // handle file1 error
        return
    }
    defer { file1.close() }

    guard let file2 = Open(...) else {
        // handle file2 error
        return
    }
    defer { file2.close() }

    // use file1 and file2 here
    // no need for cleanup at the end, it's already done
```

Note that the `defer` for `file1` handles both the normal case and the case where `file2` failed. This eliminates the repetition from the previous example, and also helps ensure we don't forget cleanup on any branch. Since error handling code is often untested, failing to clean up in the event of an error can be a common problem, and `defer` ensures that can't happen.

**Conclusion**  
This is my favorite article about new Swift features by far. Swift 2 looks like a great upgrade to Swift, addressing a lot of deficiencies and adding some great improvements.

That's it for today. Come back next time for more new and exciting stuff. Friday Q&A is driven by reader ideas, so if you have something you'd like to see covered, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2015-06-19-the-best-of-whats-new-in-swift.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
