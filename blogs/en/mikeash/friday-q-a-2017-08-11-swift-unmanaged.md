---
title: 'Friday Q&A 2017-08-11: Swift.Unmanaged'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2017-08-11-swiftunmanaged.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1ef6629159353547'
translated: false
---

> 原文：[Friday Q&A 2017-08-11: Swift.Unmanaged](https://www.mikeash.com/pyblog/friday-qa-2017-08-11-swiftunmanaged.html)　·　mikeash.com Friday Q&A

Posted at 2017-08-11 13:14 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2017-08-25: Swift Error Handling Implementation](https://www.mikeash.com/pyblog/friday-qa-2017-08-25-swift-error-handling-implementation.html)  
Previous article: [Friday Q&A 2017-07-28: A Binary Coder for Swift](https://www.mikeash.com/pyblog/friday-qa-2017-07-28-a-binary-coder-for-swift.html)  
Tags: [c](https://www.mikeash.com/pyblog/?tag=c) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2017-08-11: Swift.Unmanaged

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Estonian (translation by Johanne Teerink)](https://www.autonvaraosatpro.fi/blogi/2018/02/26/2-12/).

**Overview**  
Getting Swift references into and out of the world of C encompasses two separate tasks.

The first task is converting a reference into the raw bytes for a `void *`, or converting the raw bytes of a `void *` back to a reference. Since Swift references are implemented as pointers, this is straightforward. It's really just a matter of getting the type system to cooperate. You can do this with `unsafeBitCast`, although I strongly recommend against it. If these details ever changed, you'd be in trouble, whereas `Unmanaged` will continue to work.

The second task is making Swift's memory management work with a pointer that Swift can't see. Swift's ARC memory management requires the compiler to manage references to each object so that it can insert the appropriate retain and release calls. Once the pointer gets passed into C, it can no longer do this. Instead, you must manually tell the system how to handle memory management at each stage. `Unmanaged` provides the facilities to do this.

`Unmanaged` wraps a reference to an object. It is possible to keep `Unmanaged` values around long-term, but you typically use it as a brief, temporary stop on the way to or from a raw pointer.

**From Swift to C**  
To pass a reference from Swift to C, you must create an `Unmanaged` value from that reference, then ask it for a raw pointer. There are two ways to create an `Unmanaged` value from a Swift reference. To figure out which one you need, you must figure out your memory management requirements.

Using `Unmanaged.passRetained(obj)` will perform an unbalanced retain on the object. This effectively confers ownership on whatever C API you're passing the pointer to. It must be balanced with a release at a later point, or the object will leak.

Using `Unmanaged.passUnretained(obj)` will leave the object's retain count unchanged. This does not confer any ownership on the C API you pass the pointer to. This is suitable when passing to a C API which takes ownership internally (for example, passing an object into a `CFArray` which will retain it) and when passing to a C API which uses the value immediately but doesn't hold onto it long-term. If you pass such a value to a C API that holds the pointer long-term and doesn't take ownership, your object may be deallocated prematurely resulting in a crash or worse.

Once you have the `Unmanaged` value, you can obtain a raw pointer from it using the `toOpaque` method. Since you already decided how memory management needs to be handled, there's only one call here, and no decisions to make at this point.

Here's an example of how you'd get a raw pointer with ownership:

```
    let ptr = Unmanaged.passRetained(obj).toOpaque()
    FunctionCall(ptr)
```

And here's an example without ownership:

```
    let ptr = Unmanaged.passUnretained(obj).toOpaque()
    FunctionCall(ptr)
```

In both cases, `ptr` is an `UnsafeMutableRawPointer` which is Swift's equivalent to C's `void *`, and can be passed into C APIs.

**From C to Swift**  
To retrieve a reference from C into Swift code, you create an `Unmanaged` value from the raw pointer, then take a reference from it. There are two ways to take a reference: one which consumes an unbalanced retain, and once which performs no memory management.

To create the `Unmanaged` value, use `fromOpaque`. Unlike `passRetained` and `passUnretained`, you must specify the generic type for `Unmanaged` when using `fromOpaque` so that the compiler knows which class you're expecting to receive.

Once you have the `Unmanaged` value, you can get a reference out of it. Using `takeRetainedValue` will perform an unbalanced release, which will balance an unbalanced retain previously performed with `passRetained`, or by C code which confers ownership on your code. Using `takeUnretainedValue` will obtain the object reference without performing any retain or release.

Here's an example of getting a reference from a pointer while performing an unbalanced release:

```
    let obj = Unmanaged<MyClass>.fromOpaque(ptr).takeRetainedValue()
    obj.method()
```

And without a retain or release:

```
    let obj = Unmanaged<MyClass>.fromOpaque(ptr).takeUnretainedValue()
    obj.method()
```

**Patterns**  
It's possible to use `Umanaged` in a one-sided way, with C APIs which take a pointer and do stuff with it, or which return a pointer. But the most common way to use `Unmanaged` is with C APIs which pass around a context pointer. In this situation, you control both sides, and you need to figure out your memory management to avoid crashing or leaking. How you do that will depend on what you're doing. There are a few fundamental patterns to use.

**Synchronous Callback**  
Some APIs call you back immediately with your context pointer, completing all of their work before they return. In this case, you can pass the object unretained, and take it unretained. For example, here's some code that calls `CFArrayApplyFunction` and calls a method on `self` for each element in the array:

```
    let context = Unmanaged.passUnretained(self).toOpaque()
    let range = CFRangeMake(0, CFArrayGetCount(array))
    CFArrayApplyFunction(array, range, { element, context in
        let innerSelf = Unmanaged<MyClass>.fromOpaque(context!).takeUnretainedValue()
        innerSelf.method(element)
    }, context)
```

Because the function runs immediately, and we know that `self` will stay alive for the duration, we don't need to do any memory management on it.

**Asynchronous One-Shot Callback**  
Some APIs perform a single callback later on, for example to inform you that some task has completed. In this case, you want to retain going in, and release in the callback. Here's an example using `CFHost` to perform asynchronous DNS resolution. As a bonus, this code also contains a one-sided use of `Unmanaged` to retrieve the return value of `CFHostCreateWithName`.

It starts by creating the host. `CFHostCreateWithName` returns an `Unmanaged`, presumably because it hasn't had any curated bridging done to it. Since it returns a value that we own, we use `takeRetainedValue()` on it to get the underlying value out:

```
    let host = CFHostCreateWithName(nil, "mikeash.com" as CFString).takeRetainedValue()
```

We need a context to pass to the host object. We'll ignore all fields of this context except `info`, which is the raw pointer where we'll put the pointer to `self`:

```
    var context = CFHostClientContext()
    context.info = Unmanaged.passRetained(self).toOpaque()
```

We'll set the callback using `CFHostSetClient`:

```
    CFHostSetClient(host, { host, typeInfo, error, info in
```

Here, we retrieve `self` passed through `info` by using `Unmanaged` again. Since we passed it retained, we use `takeRetainedValue` here to balance it out. We can then use the resulting reference.

```
        let innerSelf = Unmanaged<MyClass>.fromOpaque(info!).takeRetainedValue()
        innerSelf.resolved(host)
    }, &context)
```

This code starts the asynchronous resolution process:

```
    CFHostScheduleWithRunLoop(host, CFRunLoopGetCurrent(), CFRunLoopMode.commonModes.rawValue)
    CFHostStartInfoResolution(host, .addresses, nil)
```

**Asynchronous Multi-Shot Callback**  
Finally, some APIs take a callback which they invoke many times later on. To handle this, you need to retain going in to ensure that the object stays alive. You must _not_ release in the callback, since the first callback would destroy the object and leave subsequent callbacks with a pointer to junk. Instead, you must release the value later on, when all of the callbacks are done. Typically the API will provide a separate destruction callback to handle this.

Here's an example using `CFRunLoopTimer` to perform a task once per second. It starts by creating a context and filling out the `info` field like above:

```
    var context = CFRunLoopTimerContext()
    context.info = Unmanaged.passRetained(self).toOpaque()
```

This example also fills out the context's `release` field. In the `release` callback, it uses `fromOpaque` to get an `Unmanaged` for the `info` pointer, and then calls `release` to balance the retain:

```
    context.release = { Unmanaged<MyClass>.fromOpaque($0!).release() }
```

It then creates the timer and passes a callback:

```
    let timer = CFRunLoopTimerCreate(nil, 0, 1, 0, 0, { timer, info in
```

It retrieves `self` using `Unmanaged`. It uses `takeUnretainedValue` here, since we don't want to modify the object's retain count:

```
        let innerSelf = Unmanaged<MyClass>.fromOpaque(info!).takeUnretainedValue()
        innerSelf.doStuff()
    }, &context)
```

Finally, it adds the timer to the runloop so the timer will fire:

```
    CFRunLoopAddTimer(CFRunLoopGetCurrent(), timer, CFRunLoopMode.commonModes)
```

**Miscellaneous Functionality**  
Most of what you need from `Unmanaged` can be done using `fromOpaque`, `passRetained`, `passUnretained`, `takeRetainedValue`, `takeUnretainedValue`, and `toOpaque`. However, `Unmanaged` also exposes methods for performing memory management directly on objects without the window dressing of passing or taking values. We saw that briefly in the previous example with the call to `release`. `Unmanaged` provides three plain memory management calls:

- `retain`
- `release`
- `autorelease`

These all do exactly what their names indicate. It's rare to need these, aside from `release` to balance retains as shown above, but they're there if you do.

**Conclusion**  
One of Swift's great strengths is the smoothness with which it interoperates with C code. The `Unmanaged` API is a key component of that. Unfortunately, it requires the programmer to make memory management decisions as pointers move in and out of Swift, but that's an inherent part of the job it does. Once you have the memory management figured out, it's mostly straightforward to use.

That wraps things up for now. Come back soon for more programming-related mystery goo. Until then, Friday Q&A is driven by reader ideas, so if you have a topic you'd like to see covered, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
