---
title: 'objc_msgSend''s New Prototype'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/objc_msgsends-new-prototype.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2b3d5ad8166475f9'
translated: false
---

> 原文：[objc_msgSend's New Prototype](https://www.mikeash.com/pyblog/objc_msgsends-new-prototype.html)　·　mikeash.com Friday Q&A

Posted at 2019-10-11 12:09 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Previous article: [Friday Q&A 2018-06-29: Debugging with C-Reduce](https://www.mikeash.com/pyblog/friday-qa-2018-06-29-debugging-with-c-reduce.html)  
Tags: [objc](https://www.mikeash.com/pyblog/?tag=objc)

objc_msgSend's New Prototype

by [Mike Ash](https://www.mikeash.com/)

**The True Prototype**  
There's a big and surprisingly difficult question behind this: what is the _true_ prototype of `objc_msgSend`? That is to say, what parameters does it actually take, and what does it actually return? This question doesn't have a straightforward answer.

You may have heard that `objc_msgSend` is implemented in assembly because it's so commonly called that it needs every bit of performance it can get. This is true, but not entirely complete. It's not possible to implement it in C at _any_ speed.

The fast path of `objc_msgSend` does a few critical things:

1. Load the class of the object.
2. Look up the selector in that class's method cache.
3. Jump to the method implementation found in the cache.

From the perspective of the method implementation, it looks like the caller invoked it directly. Because `objc_msgSend` jumps straight to the method implementation without making a function call, it effectively disappears once its job is done. The implementation is careful not to disturb any of the registers that can be used to pass arguments to a function. The caller calls `objc_msgSend` _as if_ it was going to directly call the method implementation, passing all of the parameters in the same way it would for a direct function call. Once `objc_msgSend` looks up the implementation and jumps to it, those parameters are still exactly where the implementation expects them to be. When the implementation returns, it returns directly to the caller, and the return value is provided by the standard mechanism.

This answers the above question: the prototype of `objc_msgSend` is that of the method implementation it ends up calling.

But wait, isn't the whole point of dynamic method lookup and message sending that you don't know what method implementation you'll be calling? This is true! However, you do know what _type signature_ the implementation will have. The compiler can get this information from the declaration of the method in an `@interface` or `@protocol` block, and uses that to generate the appropriate parameter passing and return value fetching code. If you override a method, the compiler complains if you don't match the type signature. It's possible to work around this by hiding declarations or adding methods at runtime, and in that case you can end up with a type signature for a method implementation that doesn't match the call site. The behavior of such a call then depends on how those two type signatures match up at the ABI level, with anything from perfectly reasonable and correct behavior (if the ABIs match so all the parameters happen to line up) to complete nonsense (if they don't).

This hints at an answer to this article's question: the old prototype worked in some circumstances (when the ABIs matched) and failed strangely in others (when the ABIs didn't match). The new prototype never works unless you cast it to the appropriate type first. As long as you cast it to the correct type, it always works. The new way of doing things thus encourages doing things correctly and makes it harder to do things wrong.

**The Minimal Prototype**  
Although the prototype of `objc_msgSend` depends on the method implementation that will be called, there are two things that are common across all method implementations: the first parameter is always `id self`, and the second parameter is always `SEL _cmd`. The number and type of any additional parameters is unknown, as is the return type, but those two parameters are known. `objc_msgSend` needs these two pieces of information to perform its method dispatch work, so they always have to be in the same place for it to be able to find them.

We could write an approximate generalized prototype for `objc_msgSend` to represent this:

```
    ??? objc_msgSend(id self, SEL _cmd, ???)
```

Where `???` means that we don't know, and it depends on the particular method implementation that will be called. Of course, C has no way to represent a wildcard like this.

For the return value, we can try to pick something common. Since Objective-C is all about objects, it would make sense to assume the return value is `id`:

```
    id objc_msgSend(id self, SEL _cmd, ???)
```

This not only covers cases where the return value is an object, but also cases where it's `void` and some other cases where it's a different type but the value isn't used.

How about the parameters? C actually does have a way to indicate an arbitrary number of parameters of arbitrary types, in the form of variadic function prototypes. An ellipsis at the end of the parameter list means that a variable number of arbitrarily typed values follows:

```
    id objc_msgSend(id self, SEL _cmd, ...)
```

This is exactly what the prototype used to be before the recent change.

**ABI Mismatches**  
The pertinent question at runtime is whether the ABI at the call site matches the ABI of the method implementation. Which is to say, will the receiver retrieve the parameters from the same location and in the same format that the caller passes them? If the caller puts a parameter into `$rdx` then the implementation needs to retrieve that parameter from `$rdx`, otherwise havoc will ensue.

The minimal prototype may be able to express the concept of passing an arbitrary number of arbitrary types, but for it to actually work at runtime, it needs to use the same ABI as the method implementation. That implementation is almost certainly using a different prototype, and usually has a fixed number of arguments.

There is no guarantee that the ABI for a variadic function matches the ABI for a function with a fixed number of arguments. On some platforms, they match almost perfectly. On others, they don't match at all.

**Intel ABI**  
Let's look at a concrete example. macOS uses the standard [System V ABI for x86-64](https://www.uclibc.org/docs/psABI-x86_64.pdf). There is a ton of detail in the ABI, but we'll focus on the basics.

Parameters are passed in registers. Integer parameters are passed in registers `rdi`, `rsi`, `rdx`, `rcx`, `r8`, and `r9`, in that order. Floating point parameters are passed in the SSE registers `xmm0` through `xmm7`. When calling a variadic function, the register `al` is set to the number of SSE registers that were used to pass parameters. Integer return values are placed in `rax` and `rdx`, and floating-point return values are placed in `xmm0` and `xmm1`.

The ABI for variadic functions is almost identical to the ABI for normal functions. The one exception is passing the number of SSE registers used in `al`. However, this is harmless when using the variadic ABI to call a normal function, as the normal function will ignore the contents of `al`.

The C language messes things up a bit. C specifies that certain types get promoted to wider types when passed as a variadic argument. Integers smaller than `int` (such as `char` and `short`) get promoted to `int`, and `float` gets promoted to `double`. If your method signature includes one of these types, it's not possible for a caller to pass a parameter as that exact type if it's using a variadic prototype.

For integers, this doesn't actually matter. The integer gets stored in the bottom bits of the appropriate register, and the bits end up in the same place either way. However, it's catastrophic for `float`. Converting a smaller integer to an `int` just requires padding it out with extra bits. Converting `float` to `double` involves converting the value to a different structure altogether. The bits in a `float` don't line up with the corresponding bits in a `double`. If you try to use a variadic prototype to call a non-variadic function that takes a `float` parameter, that function will receive garbage.

To illustrate this problem, here's a quick example:

```
    // Use the old variadic prototype for objc_msgSend.
    #define OBJC_OLD_DISPATCH_PROTOTYPES 1

    #import <Foundation/Foundation.h>
    #import <objc/message.h>

    @interface Foo : NSObject @end
    @implementation Foo
    - (void)log: (float)x {
        printf("%f\n", x);
    }
    @end

    int main(int argc, char **argv) {
        id obj = [Foo new];
        [obj log: (float)M_PI];
        objc_msgSend(obj, @selector(log:), (float)M_PI);
    }
```

It produces this output:

```
    3.141593
    3370280550400.000000
```

As you can see, the value came through correctly when written as a message send, but got completely mangled when passed through an explicit call to `objc_msgSend`.

This can be remedied by casting `objc_msgSend` to have the right signature. Recall that `objc_msgSend`'s actual prototype is that of whatever method will end up being invoked, so the correct way to use it is to cast it to the corresponding function pointer type. This call works correctly:

```
    ((void (*)(id, SEL, float))objc_msgSend)(obj, @selector(log:), M_PI);
```

**ARM64 ABI**  
Let's look at another relevant example. iOS uses [a variation on the standard ABI for ARM64](https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/iPhoneOSABIReference/Articles/ARM64FunctionCallingConventions.html).

Integer parameters are passed in registers `x0` through `x7`. Floating point parameters are passed in `v0` through `v7`. Additional parameters are passed on the stack. Return values are placed in the same register or registers where they would be passed as parameters.

This is only true for normal parameters. Variadic parameters are never passed in registers. They are always passed on the stack, even when parameter registers are available.

There's no need for a careful analysis of how this will work out in practice. The ABIs are completely mismatched and a method called with an uncast `objc_msgSend` will receive garbage in its parameters.

**The New Prototype**  
The new prototype is short and sweet:

```
    void objc_msgSend(void);
```

This isn't correct at all. However, neither was the old prototype. This one is much more _obviously_ incorrect, and that's a good thing. The old prototype made it easy to to use it without casting it, and worked often enough that you could easily end up thinking everything was OK. When you hit the problematic cases, the bugs were very unclear.

This prototype doesn't even allow you to pass the two required parameters of `self` and `_cmd`. You can call it with no parameters at all, but it'll immediately crash and it should be pretty obvious about what went wrong. If you try to use it without casting, the compiler will complain, which is much better than weird broken parameter values.

Because it still has a function type, you can still cast it to a function pointer of the appropriate type and invoke it that way. This will work correctly as long as you get the types right.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/objc_msgsends-new-prototype.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
