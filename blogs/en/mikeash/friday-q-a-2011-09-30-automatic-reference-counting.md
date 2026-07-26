---
title: 'Friday Q&A 2011-09-30: Automatic Reference Counting'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-09-30-automatic-reference-counting.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ffaae452d0e13d07'
translated: false
---

> 原文：[Friday Q&A 2011-09-30: Automatic Reference Counting](https://www.mikeash.com/pyblog/friday-qa-2011-09-30-automatic-reference-counting.html)　·　mikeash.com Friday Q&A

Posted at 2011-09-30 15:02 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2011-10-14: What's New in GCD](https://www.mikeash.com/pyblog/friday-qa-2011-10-14-whats-new-in-gcd.html)  
Previous article: [Friday Q&A 2011-09-16: Let's Build Reference Counting](https://www.mikeash.com/pyblog/friday-qa-2011-09-16-lets-build-reference-counting.html)  
Tags: [arc](https://www.mikeash.com/pyblog/?tag=arc) [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [memory](https://www.mikeash.com/pyblog/?tag=memory) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2011-09-30: Automatic Reference Counting

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Hungarian (translation by Szabolcs Csintalan)](http://fertlond.com/automatikus-referencia-szamlalas/).

**Conceptual**  
The [Clang static analyzer](https://www.mikeash.com/pyblog/friday-qa-2009-03-06-using-the-clang-static-analyzer.html) is a really useful tool for finding memory management errors in code. If you're like me, you've looked at the output of the analyzer and thought, "If you can spot the error, why can't you just _fix_ it for me too?"

That, in essence, is what ARC is. The memory management rules are baked into the compiler, but instead of using them to help the programmer find mistakes, it simply inserts the necessary calls on its own.

ARC occupies a middle ground between garbage collection and manual memory management. Like garbage collection, ARC frees the programmer from writing `retain`/`release`/`autorelease` calls. Unlike garbage collection, however, ARC does not deal with [retain cycles](https://www.mikeash.com/pyblog/friday-qa-2010-04-30-dealing-with-retain-cycles.html). Two objects with strong references to each other will never be collected under ARC, even if nothing else refers to them. Because of this, while ARC frees the programmer from dealing with _most_ memory management issues, the programmer still has to avoid or manually break cycles of strong references in the object graph.

When it comes to implementation specifics, there's another key difference between ARC and Apple's implementation of garbage collection: ARC is not an either/or proposition. With Apple's garbage collector, either the entire application runs under GC, or none of it does. This means that all Objective-C code in an application, including all of Apple's frameworks and all third-party libraries you might include, must be GC compatible for you to take advantage of GC. In contrast, ARC coexists peacefully with non-ARC manual memory managed code in the same application. This makes it possible to convert projects piecemeal without the massive compatibility and reliability problems that garbage collection ran into when it was first introduced.

**Xcode**  
ARC is available in Xcode 4.2, currently in beta, and only when compiling with Clang (a.k.a. "Apple LLVM compiler"). The setting is called, obviously enough, "Objective-C Automatic Reference Counting". Turn it on, and off you go.

If you're working on existing code, changing this setting will produce an enormous quantity of errors. ARC not only manages memory for you, but it forbids you from trying to do it yourself. It's illegal to manually send `retain`/`release`/`autorelease` when using ARC. Since normal non-ARC Cocoa code is littered with this stuff, you'll get a lot of errors.

Fortunately, Xcode offers a tool to convert existing code. Select Edit -\> Refactor... -\> Convert to Objective-C ARC... and Xcode will guide you through converting your code. Although there may be some situations where it needs help figuring out what to do, the process should be largely automatic.

**Basic Functionality**  
Cocoa memory management rules are fairly simple. In short:

1. ,

  ,

  , or

  an object, you must balance that with

  or

  .
2. or

  it. This must, of course, be balanced later.

These are highly suitable for automation. If you write this:

```
    Foo *foo = [[Foo alloc] init];
    [foo something];
    return;
```

The compiler can see the unbalanced `alloc`. The code is thus transformed:

```
    Foo *foo = [[Foo alloc] init];
    [foo something];
    [foo release];
    return;
```

In reality, the compiler does not insert a message send to `release`. Instead, it inserts a call to a special runtime function:

```
    Foo *foo = [[Foo alloc] init];
    [foo something];
    objc_release(foo);
    return;
```

This allows for some optimization. In the common case where `-release` is not overridden, the `objc_release` function can bypass Objective-C messaging, resulting in a bit of a speed gain.

This automation can make code safer. Most Cocoa programmers interpret "long-term" in rule #2 to mean objects stored in instance variables and similar places. We don't normally retain and release local temporary objects:

```
    Foo *foo = [self foo];
    [foo bar];
    [foo baz];
    [foo quux];
```

However, this can be dangerous:

```
    Foo *foo = [self foo];
    [foo bar];
    [foo baz];
    [self setFoo: newFoo];
    [foo quux]; // crash
```

The standard way to work around this is to have the `-foo` getter do a `retain`/`autorelease` before returning the value. This works, but can build up a lot of temporary objects leading to excessive memory usage. ARC, however, will be paranoid and insert extra calls here:

```
    Foo *foo = objc_retainAutoreleasedReturnValue([self foo]);
    [foo bar];
    [foo baz];
    [self setFoo: newFoo];
    [foo quux]; // fine
    objc_release(foo);
```

Likewise, even if you write a plain getter, ARC will make it safe as well:

```
    - (Foo *)foo
    {
        return objc_retainAutoreleaseReturnValue(_foo);
    }
```

But wait, this doesn't solve the problem of excessive temporary objects at all! We're still doing a `retain`/`autorelease` sequence in the getter, _and_ a `retain`/`release` combination in the calling code. This is considerably less efficient!

Not to worry. As I mentioned above, ARC emits these special calls instead of plain message sends for the purposes of optimization. In addition to simply making `retain` and `release` faster, these calls are able to eliminate certain operations altogether.

When `objc_retainAutoreleaseReturnValue` runs, it looks on the stack and grabs the return address from its caller. This allows it to see exactly what will happen after it finishes. When compiler optimizations are turned on, the call to `objc_retainAutoreleaseReturnValue` will be subject to tail-call optimization, and the return address will point to the call to `objc_retainAutoreleasedReturnValue`.

With this crazy return-address examination, the runtime is able to see that it's about to perform some redundant work. It therefore eliminates the `autorelease`, and sets a flag that tells the caller to eliminate its `retain`. The whole sequence ends up doing a single `retain` in the getter and a single `release` in the calling code, which is both completely safe and efficient.

Note that this optimization is fully compatible with non-ARC code. In the event that the getter doesn't use ARC, the flag won't be set and the caller will perform a full `retain`/`release` combination. In the event that the getter uses ARC but the caller does not, the getter will see that it's not returning to code that immediately calls the special runtime function, and will perform a full `retain`/`autorelease` combination. Some efficiency is lost, but correctness is preserved.

In addition to all of this, ARC also automatically creates or fills out a `-dealloc` method for all classes to release their instance variables. It's still possible to manually implement `-dealloc`, and it's necessary for classes which manage external resources, but it's no longer necessary (or possible) to manually release instance variables. ARC will even put the `[super dealloc]` at the end for you, so you don't have to. Previously, you might have written this:

```
    - (void)dealloc
    {
        [ivar1 release];
        [ivar2 release];
        free(buffer);

        [super dealloc];
    }
```

Now you can just write this:

```
    - (void)dealloc
    {
        free(buffer);
    }
```

In the event that your `-dealloc` method just releases instance variables, it can simply be eliminated altogether.

**Cycles and Weak References**  
ARC still requires the programmer to manually resolve reference cycles, and the best way to resolve reference cycles is typically to use weak references.

ARC provides zeroing weak references. These are weak references which not only don't keep the referenced object alive, but which also automatically become `nil` when the referenced object is destroyed. Zeroing weak references avoid the potential for dangling pointers and the associated crashes and mysterious behavior.

To make a zeroing weak variable, simply prefix its declaration with `__weak`. For example, here is a weak instance variable:

```
    @interface Foo : NSObject
    {
        __weak Bar *_weakBar;
    }
```

Likewise for local variables:

```
    __weak Foo *_weakFoo = [object foo];
```

You can then use it like any other variable, with the value automatically becoming `nil` when appropriate:

```
    [_weakBar doSomethingIfStillAlive];
```

Note, however, that a `__weak` variable can become `nil` at almost any time. Memory management is an inherently multithreaded activity, and a weakly referenced object could be destroyed on one thread while another thread is accessing it. Code like this is therefore not valid:

```
    if(_weakBar)
        [self mustNotBeNil: _weakBar];
```

Instead, store the object into a local strong reference and test that:

```
    Bar *bar = _weakBar;
    if(bar)
        [self mustNotBeNil: bar];
```

Because `bar` is a strong reference here, the object is guaranteed to stay alive (and the variable non-`nil`) throughout this code.

ARC's implementation of zeroing weak references requires close coordination between the Objective-C reference counting system and the zeroing weak reference system. This means that any class which overrides `retain` and `release` can't be the target of a zeroing weak reference. While this is uncommon, some Cocoa classes, like `NSWindow`, suffer from this limitation. Fortunately, if you hit one of these cases, you will know it immediately, as your program will crash with a message like this:

```
    objc[2478]: cannot form weak reference to instance (0x10360f000) of class NSWindow
```

If you really must make a weak reference to classes such as these, you can use the `__unsafe_unretained` qualifier in place of `__weak`. This creates a weak reference which is _not_ zeroing. You must ensure that you never use such a pointer (preferably by zeroing it out manually) after the object it points to has been destroyed. Be careful, as non-zeroing weak references are playing with fire.

While it's possible to build programs using ARC that run on Mac OS X 10.6 and iOS 4, zeroing weak references are not available on those OSes. All weak references must be `__unsafe_unretained` here. Because non-zeroing weak references are so dangerous, this limitation significantly decreases the attractiveness of ARC on those OSes in my view.

**Properties**  
Since properties are so tightly coupled to memory management, it makes sense that ARC would introduce some new behaviors there.

ARC introduces a few new ownership modifiers. Declaring a property as `strong` makes that property a strong reference. Declaring it as `weak` uses a zeroing weak reference. The `unsafe_unretained` modifier uses a non-zeroing weak reference. When `@synthesize` is used, the compiler creates an instance variable of the same storage type.

The existing modifiers of `assign`, `copy`, and `retain` still exist and work the same way they did before. Notably, `assign` creates a _non_-zeroing weak reference, so it should be avoided whenever possible.

Aside from the new modifiers, properties work just as they always have.

**Blocks**  
Blocks are Objective-C objects, and as such are also managed by ARC. Blocks have special memory management requirements, and ARC treats them accordingly. Block literals must be copied, not retained, which in practice means that it's best to copy rather than retain blocks everywhere. ARC follows this practice.

Additionally, ARC knows that block literals must be copied if they're used after the current scope returns. Non-ARC code needs to explicitly copy and autorelease returned blocks:

```
    return [[^{
        DoSomethingMagical();
    } copy] autorelease];
```

With ARC, this simply becomes:

```
    return ^{ DoSomethingMagical(); };
```

However, beware! ARC currently does not automatically copy a block literal that's converted to an `id`. So while this code is fine:

```
    dispatch_block_t function(void)
    {
        return ^{ DoSomethingMagical(); };
    }
```

This code is not:

```
    id function(void)
    {
        return ^{ DoSomethingMagical(); };
    }
```

It's easy to work around by simply copying the block, but it's something to be careful with:

```
    return [^{ DoSomethingMagical(); } copy];
```

Likewise, you need to explicitly copy blocks that you pass as `id` parameters:

```
    [myArray addObject: [^{ DoSomethingMagical(); } copy]];
```

Fortunately, it appears that this is just an edge case that fell through the cracks and is likely to be fixed soon. There's no problem with throwing in an extra manual copy if you're unsure.

Another significant change with ARC is the behavior of `__block` qualified variables. The `__block` qualifier allows a block to modify a captured variable:

```
    id x;
    __block id y;
    void (^block)(void) = ^{
        x = [NSString string]; // error
        y = [NSString string]; // works
    };
```

Without ARC, `__block` also has the side effect of not retaining its contents when it's captured by a block. Blocks will automatically retain and release any object pointers they capture, but `__block` pointers are special-cased and act as a weak pointer. It's become a common pattern to rely on this behavior by using `__block` to avoid retain cycles.

Under ARC, `__block` now retains its contents just like other captured object pointers. Code that uses `__block` to avoid retain cycles won't work anymore. Instead, use `__weak` as described above.

**Toll-Free Bridging**  
ARC only works on Objective-C types. CoreFoundation types still have to be managed manually by the programmer. Because there is ambiguity about ownership, ARC forbids standard casts between pointers to Objective-C objects and pointers of other types, including pointers to CoreFoundation objects. The following code, which is fairly typical under manual memory management, does not compile with ARC:

```
    id obj = (id)CFDictionaryGetValue(cfDict, key);
```

In order to make this compile again, you must tell ARC about the ownership semantics involved by using special casting annotations. These annotations are `__bridge`, `__bridge_retained`, and `__bridge_transfer`.

The simplest one to understand is `__bridge`. This is a direct conversion with no ownership consequences. ARC receives the value and then manages it normally. This is what we want for the above:

```
    id obj = (__bridge id)CFDictionaryGetValue(cfDict, key);
```

The other casting annotations transfer ownership to and from the ARC system. These can help ease the pain when bridging back and forth.

Here's an example of using bridging in a situation where the returned object needs to be released.

```
    NSString *value = (NSString *)CFPreferencesCopyAppValue(CFSTR("someKey"), CFSTR("com.company.someapp"));
    [self useValue: value];
    [value release];
```

If we move this to ARC by using `__bridge`, removing the `release`, and otherwise not making any changes, we end up with a leak:

```
    NSString *value = (__bridge NSString *)CFPreferencesCopyAppValue(CFSTR("someKey"), CFSTR("com.company.someapp"));
    [self useValue: value];
```

The `Copy` in this code needs to be balanced with a release. ARC will emit a `retain` when initializing `value`, then balance that with a `release` when `value` is no longer used. Since nothing balances the original `Copy`, that object is leaked.

We can work around this with a little extra code:

```
    CFStringRef valueCF = CFPreferencesCopyAppValue(CFSTR("someKey"), CFSTR("com.company.someapp"));
    NSString *value = (__bridge NSString *)valueCF;
    CFRelease(valueCF);

    [self useValue: value];
```

This is getting fairly verbose, though. Since the whole point of toll-free bridging is to be as painless as possible, and the whole point of ARC is to remove the need to write memory management code, it would be nice if this could be made more straightforward.

The `__bridge_transfer` annotation solves this problem. Rather than simply move a pointer value into ARC, it moves the value _and transfers ownership_. When `__bridge_transfer` is used in a cast, it tells ARC that this object is _already_ retained, and that ARC doesn't need to retain it again. Since ARC takes ownership, it will still release it when it's done. The net result is that everything works the way it's supposed to:

```
    NSString *value = (__bridge_transfer NSString *)CFPreferencesCopyAppValue(CFSTR("someKey"), CFSTR("com.company.someapp"));
    [self useValue: value];
```

Toll-free bridging works both ways. As before, ARC doesn't allow a standard cast to convert from an Objective-C object pointer to a CoreFoundation object pointer. This code won't compile under ARC:

```
    CFStringRef value = (CFStringRef)[self someString];
    UseCFStringValue(value);
```

Adding a `__bridge` to the cast makes it compile, but the resulting code is dangerous:

```
    CFStringRef value = (__bridge CFStringRef)[self someString];
    UseCFStringValue(value);
```

Since ARC doesn't manage the lifetime of `value`, it will release ownership of the object immediately, before it gets passed to `UseCFStringValue`, potentially causing a crash or other misbehavior. By using `__bridge_retained`, we can tell ARC to transfer ownership out of the system and into our hands. Since ownership is transferred, we're now responsible for releasing the object when done with it, just like with any other CF code:

```
    CFStringRef value = (__bridge_retained CFStringRef)[self someString];
    UseCFStringValue(value);
    CFRelease(value);
```

These cast annotations are useful outside of toll-free bridging as well. Any time you need to store an object pointer in storage that's not managed as an Objective-C object, they smooth the way. There are `void *` context pointers found in various places in Cocoa, and a prominent example is sheets. Without ARC:

```
    NSDictionary *contextDict = [NSDictionary dictionary...];
    [NSApp beginSheet: sheetWindow
       modalForWindow: mainWindow
        modalDelegate: self
       didEndSelector: @selector(sheetDidEnd:returnCode:contextInfo:)
          contextInfo: [contextDict retain]];

    - (void)sheetDidEnd: (NSWindow *)sheet returnCode: (NSInteger)code contextInfo: (void *)contextInfo
    {
        NSDictionary *contextDict = [(id)contextInfo autorelease];
        if(code == NSRunStoppedResponse)
            ...
    }
```

As before, this fails under ARC, because normal casts between object and non-object pointers are not allowed. However, using the cast modifiers, we can not only get ARC to allow it, but also get ARC to do the requisite memory management for us:

```
    NSDictionary *contextDict = [NSDictionary dictionary...];
    [NSApp beginSheet: sheetWindow
       modalForWindow: mainWindow
        modalDelegate: self
       didEndSelector: @selector(sheetDidEnd:returnCode:contextInfo:)
          contextInfo: (__bridge_retained void *)contextDict];

    - (void)sheetDidEnd: (NSWindow *)sheet returnCode: (NSInteger)code contextInfo: (void *)contextInfo
    {
        NSDictionary *contextDict = (__bridge_transfer NSDictionary *)contextInfo;
        if(code == NSRunStoppedResponse)
            ...
    }
```

To summarize:

- simply transfers a pointer between ARC and non-ARC with no transfer of ownership.
- moves a non-Objective-C pointer to Objective-C and also transfers ownership, such that ARC will release the value for you.
- moves an Objective-C pointer to a non-Objective-C pointer and also transfers ownership, such that you, the programmer, are responsible for later calling

  or otherwise releasing ownership of the object.

**Structs**  
Under ARC, structs and Objective-C object pointers pretty much don't mix. The problem is that there is no good way for the compiler to know when a particular struct is destroyed or copied, and thus no good place for the compiler to insert the necessary `retain` and `release` calls. Because it's such a difficult problem, and because putting object pointers in structs is so unusual anyway, ARC just gives up on the whole proposition. If you want to put an Objective-C object pointer in a struct, you _must_ qualify it with `__unsafe_unretained`, and deal with all of the problems and danger that this implies.

Because it's so uncommon to put Objective-C pointers into structs, it's likely that this won't be a problem for your code. If it is, your best bet is to change the struct into a lightweight Objective-C class instead. ARC will start managing memory for you and the problem goes away.

**Further Reading**  
While Apple's official documentation on ARC is still under wraps while Xcode 4.2 is in beta, a great deal of information about the system is available on the Clang site here: [http://clang.llvm.org/docs/AutomaticReferenceCounting.html](http://clang.llvm.org/docs/AutomaticReferenceCounting.html)

**Conclusion**  
Automatic reference counting substantially reduces the burden on the programmer for dealing with memory management. ARC is not a full garbage collector. It cannot detect retain cycles, and these must be dealt with and broken by the programmer. It still takes a lot of the grunt work out of writing Cocoa code, and the zeroing weak references that it provides are a powerful tool for dealing with cycles.

Things get trickier when it comes to CoreFoundation objects and toll-free bridging. ARC limits itself to dealing with Objective-C, so the programmer still needs to manage the CoreFoundation side manually. When converting between Objective-C and CoreFoundation pointers, the special `__bridge` cast modifiers need to be used to inform ARC about the memory management semantics of the conversion.

That wraps up today's exploration of Apple's latest programming language technology. Come back in two weeks for another fine word salad. Until then, keep watching the skies and [sending in your suggestions for topics](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
