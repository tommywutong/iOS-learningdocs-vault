---
title: 'Friday Q&A 2011-08-05: Method Signature Mismatches'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-08-05-method-signature-mismatches.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:039d36c0753909b5'
translated: false
---

> 原文：[Friday Q&A 2011-08-05: Method Signature Mismatches](https://www.mikeash.com/pyblog/friday-qa-2011-08-05-method-signature-mismatches.html)　·　mikeash.com Friday Q&A

Posted at 2011-08-05 14:45 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [See Me Speak at Voices That Matter in Boston](https://www.mikeash.com/pyblog/see-me-speak-at-voices-that-matter-in-boston.html)  
Previous article: [Friday Q&A 2011-07-22: Writing Unit Tests](https://www.mikeash.com/pyblog/friday-qa-2011-07-22-writing-unit-tests.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [vararg](https://www.mikeash.com/pyblog/?tag=vararg)

Friday Q&A 2011-08-05: Method Signature Mismatches

by [Mike Ash](https://www.mikeash.com/)

**Message Sending Recap**  
Whenever you write a `[obj foo]` message send in your code, the compiler internally translates it to a standard function call to this function:

```
    id objc_msgSend(id self, SEL op, ...);
```

There are a few variants of this, to handle things like struct returns and calls to `super`, but they all do essentially the same thing.

While the call itself is normal, this function is strange and unusual. When called, it uses the `self` and `SEL` parameters to look up the method that needs to be invoked. Once it finds the method, it jumps to it. It completely ignores all other arguments and the return value.

The prototype listed above is taken directly from Apple's `objc/runtime.h` header. It shows that the function takes an `id`, a `SEL`, and variable arguments after that, and that it returns `id`. This prototype is a lie. Because of the strange and unusual nature of this function, it actually has no fixed prototype. The correct prototype for `objc_msgSend` is whatever matches the prototype of the method that it will invoke. This is what's referred to as the "method signature". If the prototype used by the caller doesn't match the prototype used by the method itself, interesting things can happen.

If you're interested in more details about precisely how messaging and `objc_msgSend` work, see my previous article, [Objective-C Messaging](https://www.mikeash.com/pyblog/friday-qa-2009-03-20-objective-c-messaging.html).

**Method Signatures**  
Objective-C is a dynamically typed object-oriented language, so what's the big deal with method signatures having to match? You can pass an object of type A to code that expects type B, and as long as it behaves properly, everything still works.

Unfortunately, that's only half the story, specifically the "Objective" half. In the "C" half, none of the above is true. In that world, types are all static and not all that well enforced, and when you tell the compiler that something is of type A when it's really of type B, it believes you. If A and B lay things out differently in memory, or otherwise don't precisely match, havoc ensues.

A method signature is simply the types of the arguments and the return type. When you declare a method in your class's `@implementation`, it gives the compiler two key pieces of information. First, it declares the method's name so that users of the class know that a method by that name exists. Second, it declares the method's signature, so that callers know how to generate the correct code to call it.

It's not possible for the compiler to generate correct code without knowing the method signature. Consider the following fairly innocuous call:

```
    [foo doThing: 0];
```

Now consider these different declarations for that method:

```
    - (void)doThing: (double)x;
    - (void)doThing: (void *)x;
    - (void)doThing: (char)x;
```

In all three cases, you're passing an `int` which gets implicitly converted to a different type. That implicit conversion happens _at the call site_. If `doThing:` expects a `double` argument, then the argument _must_ be converted to a `double` before the call is even made. If the compiler doesn't know the argument type, it won't know that it needs to make the conversion. The result is that the caller will place an `int` in one place and the caller will fetch a `double` from a completely different place, resulting in nonsensical data.

**ABIs**  
What exactly happens in cases like this depends on the low-level details of how functions are called on the particular architecture you're running on. Those details are documented in the ABI, or application binary interface, of the architecture in question. The details will be completely different from one architecture to the next. For example, i386, x86-64, and ARM, all use completely different function calling conventions. For this article, I'll concentrate on ARM, as it's the cleanest of the bunch. The principles carry over to other architectures, even if the details don't.

The function calling conventions for ARM can be found starting on page 15 of the ABI, which is available here:

[`http://infocenter.arm.com/help/topic/com.arm.doc.ihi0042d/IHI0042D_aapcs.pdf`](http://infocenter.arm.com/help/topic/com.arm.doc.ihi0042d/IHI0042D_aapcs.pdf)

Many of the details aren't too important here, but some are key.

The first four arguments to a function are passed in registers `r0-r3`, which each hold 32 bits. If the function takes more than four arguments, additional arguments are passed by pushing them onto the stack. However, this assumes that the arguments are 32-bit data types. For 64-bit data types such as `long long` and `double`, the argument in question takes up two register (or two stack slots), and is additionally aligned to start in an even-numbered position.

Values are returned by storing them into `r0`. Again, this assumes a 32-bit data type. 64-bit data types, are returned in `r0` and `r1`. Structs which are larger than 32-bits are returned by having the caller allocate memory to store the return value, then passing an extra, hidden parameter to the function which contains the address of that memory.

The C standard also comes into play. When the compiler can't find a method signature at all, it assumes that the method signature takes `...` variable arguments. C specifies type promotions for variable arguments. Any integer type smaller than an `int` is promoted to an `int`, and arguments of type `float` are promoted to `double`.

**Consequences**  
Now we know how parameters are passed, but what does it _mean_?

The most common case for a method signature mismatch is when a declaration for the method isn't visible at all, and the compiler then assumes that it takes `...` variable arguments. This usually happens when forgetting to import the header which contains the declaration. As noted above, types get promoted when passed as variable arguments.

In the case of integer types, this is harmless, at least on ARM. All integer types up to `int` are passed in a single register or stack slot, and the caller will end up extracting the correct portion of the data.

In the case of floating point types, this causes a major problem if the method takes a `float`. The `float` will be promoted to a `double`, which takes up two registers or stack slots. Not only will the method only load half of the data (which won't make any sense on its own anyway), but all subsequent arguments will be shifted down by one, causing the method to fetch junk for all of them as well. If the `float` is an odd-numbered argument, the `double` will be pushed down even further in order to align it properly.

It can also cause a major problem if the caller passes a number that's of a different type than the method is expecting. C will do silent conversions between numeric types. Normally, if the method expects a `float` but the caller passes an `int`, the compiler silently converts the value to a `float` and everything is happy. However, if no method signature is available, the compiler will simply pass the `int`. The method will then try to interpret that bit pattern as a `float`, with nonsensical results. It gets worse if the two sides use data types of different sizes, like passing an `int` where a `double` is expected, or a `char` where a `long long` is expected. This will not only cause bad data to be extracted, but once again shift all of the other arguments down so they end up with bad data as well.

Finally, there can be problems with return type conflicts. When no declaration is present, the compiler assumes that the method returns `id`. If you're using the return value, then any conflict will become quickly obvious. If you treat the return value like an `int`, the compiler will give you an error about the mismatch.

Where it becomes a problem is when you don't use the return value. If the method returns a pointer or integer, then all is well. However, if the method returns a large struct, an extra hidden parameter will be inserted to hold the address of the caller's storage for the struct, which will end up shifting everything down and all of the parameters will contain garbage. If you're unlucky enough to have the method return, it will write its return value to whatever location is indicated by your first parameter, almost certainly not what you want. On some architectures, the `objc_msgSend_fpret` variant has to be used for some floating point types, and a mismatch here can lead to bizarre crashes later, as the CPU's floating point state goes bad.

(Note that, in general, there's no real guarantee made by the language that passing variable arguments will work at all when the method expects fixed arguments. It just so happens that it _usually_ works out on architectures you're likely to encounter.)

This situation also prevents the compiler from checking your code. Even if you only use data types which are safe, the compiler won't be able to yell at you if you accidentally pass an `NSNumber *` for a parameter that expects an `int`. This will result in the object's pointer value being interpreted as a number, which is not what you want. With a method signature available, the compiler will give you an error instead.

Less common is the case where there is a true method signature mismatch. This happens when the caller sees a different declaration than the method implementation. This requires two methods with identical names but different signatures to exist in the code. Such a conflict can happen when an object variable is declared to be of one type but the object stored in it is actually a different type. This can also happen when using a variable of type `id` and either the compiler only sees the wrong declaration or it sees both and chooses the wrong one. While the compiler will warn if it has to choose from multiple distinct declarations, the case where it only sees the wrong one is particularly nasty, as the compiler has _no_ indication that something is wrong, and therefore can't give any sort of warning.

Let's look at an example. Here are two methods, declared in two different classes:

```
    @interface Foo (MoreMethods)
    - (void)makeThingOfWidth: (int)width;
    @end

    @interface Bar (MoreMethods)
    - (void)makeThingOfWidth: (float)width;
    @end
```

These two methods have identical names but different signatures. If we write code which imports both of these headers, code which tries to use these methods on an `id` will run into trouble:

```
    id obj = ...;
    [obj makeThingOfWidth: 42]; // danger!
```

Depending on whether `obj` is a `Foo` or a `Bar`, and on which method signature the compiler decides to use, this could end up passing junk data into the method. Fortunately, the compiler will warn for this case.

More dangerous is code which only imports _one_ header, then ends up manipulating an instance of the other class:

```
    #import <Foo.h> // note: no Bar.h

    id obj = [otherObj getMeABar];
    [obj makeThingOfWidth: 42];
```

This is _guaranteed_ to go wrong, and the compiler _can't_ generate any errors or warnings about it because, as far as it can see, there's no potential problem.

In general, to avoid both this and the more benign case where multiple signatures are visible, I recommend trying to ensure that methods with different signatures also have different names whenever it's practical to do so. When that's not possible, using static types instead of `id` will either solve the problem or at least give an error or warning that something has gone wrong.

**Conclusion**  
Method signature mismatches can result in some truly weird behavior, from bizarre data showing up in method arguments to random-looking crashes that don't occur until long after the site of the mismatch.

Good Objective-C code should always build with no warnings, and this is an excellent example of why this is important. The compiler will warn for _nearly_ all situations that can lead to a method signature mismatch, and when it warns, the problem needs to be fixed in order to eliminate the warning.

In certain rare cases, a mismatch can happen with no warning generated. Fortunately, this is a difficult situation to get into and it's unlikely to happen by accident. However, because Objective-C deals so poorly with multiple methods which have the same name but different signatures, it's best to try to ensure that methods with different signatures also have different names.

That wraps things up for today. Come back in another two weeks for another Friday Q&A. As always, Friday Q&A is driven by you, the reader. If you have a suggestion for a topic that you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
