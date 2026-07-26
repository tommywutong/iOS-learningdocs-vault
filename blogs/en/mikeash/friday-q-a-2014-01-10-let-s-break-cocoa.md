---
title: 'Friday Q&A 2014-01-10: Let''s Break Cocoa'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-01-10-lets-break-cocoa.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e5ca28f01bf7e230'
translated: false
---

> 原文：[Friday Q&A 2014-01-10: Let's Break Cocoa](https://www.mikeash.com/pyblog/friday-qa-2014-01-10-lets-break-cocoa.html)　·　mikeash.com Friday Q&A

Posted at 2014-01-10 14:58 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2014-01-24: Introduction to libclang](https://www.mikeash.com/pyblog/friday-qa-2014-01-24-introduction-to-libclang.html)  
Previous article: [Friday Q&A 2013-12-06: Network Protocol Design](https://www.mikeash.com/pyblog/friday-qa-2013-12-06-network-protocol-design.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbreak](https://www.mikeash.com/pyblog/?tag=letsbreak)

Friday Q&A 2014-01-10: Let's Break Cocoa

by [Mike Ash](https://www.mikeash.com/)

**Strings With Embedded NULs**  
The NUL character, which is `0` in ASCII and Unicode, is an unusual beast. When working with C strings, it's not treated as a character at all, but rather it's used to signal the end of the string. In other contexts, it's treated the same as other characters.

This has interesting consequences when you cross between C strings and other contexts. `NSString` objects, for example, have no problem with NUL characters:

```
    NSString *s = @"abc\0def";
```

We can print this in the debugger, if we're careful:

```
    (lldb) p (void)[[NSFileHandle fileHandleWithStandardOutput] writeData: [s dataUsingEncoding: 5]]
    abcdef
```

However, the more typical ways to display this string end up treating it as a C string at some point. Because the '\\0' character in the middle signals the end of a C string, the string effectively gets truncated when converted:

```
    (lldb) po s
    abc
    (lldb) p (void)NSLog(s)
    LetsBreakCocoa[16689:303] abc
```

The original string still contains the expected number of characters:

```
    (lldb) p [s length]
    (unsigned long long) $1 = 7
```

Trying to manipulate this string can get _really_ confusing:

```
    (lldb) po [s stringByAppendingPathExtension: @"txt"]
    abc
```

If you didn't know that `s` contained a NUL in the middle, this sort of behavior might convince you that something has gone seriously wrong with your brain.

You don't normally encounter the NUL character, but it's possible to run into it if you're loading data from external sources. `-initWithData:encoding:` will happily read in zero bytes and produce NUL characters in the resulting `NSString`.

**Circular Containers**  
This is an array:

```
    NSMutableArray *a = [NSMutableArray array];
```

This is an array that contains another array:

```
    NSMutableArray *a = [NSMutableArray array];
    NSMutableArray *b = [NSMutableArray array];
    [a addObject: b];
```

So far, so good. This is an array that contains itself:

```
    NSMutableArray *a = [NSMutableArray array];
    [a addObject: a];
```

What does this look like?

```
    NSLog(@"%@", a);
```

Oh, that's what it looks like:

```
    (lldb) bt
    * thread #1: tid = 0x43eca, 0x00007fff8952815a CoreFoundation`-[NSArray descriptionWithLocale:indent:] + 154, queue = 'com.apple.main-thread, stop reason = EXC_BAD_ACCESS (code=2, address=0x7fff5f3ffff8)
                    frame #0: 0x00007fff8952815a CoreFoundation`-[NSArray descriptionWithLocale:indent:] + 154
                    frame #1: 0x00007fff895282da CoreFoundation`-[NSArray descriptionWithLocale:indent:] + 538
                    frame #2: 0x00007fff895282da CoreFoundation`-[NSArray descriptionWithLocale:indent:] + 538
                    frame #3: 0x00007fff895282da CoreFoundation`-[NSArray descriptionWithLocale:indent:] + 538
                    frame #4: 0x00007fff895282da CoreFoundation`-[NSArray descriptionWithLocale:indent:] + 538
                    frame #5: 0x00007fff895282da CoreFoundation`-[NSArray descriptionWithLocale:indent:] + 538
                    frame #6: 0x00007fff895282da CoreFoundation`-[NSArray descriptionWithLocale:indent:] + 538
                    frame #7: 0x00007fff895282da CoreFoundation`-[NSArray descriptionWithLocale:indent:] + 538
                    frame #8: 0x00007fff895282da CoreFoundation`-[NSArray descriptionWithLocale:indent:] + 538
                    frame #9: 0x00007fff895282da CoreFoundation`-[NSArray descriptionWithLocale:indent:] + 538
                    frame #10: 0x00007fff895282da CoreFoundation`-[NSArray descriptionWithLocale:indent:] + 538
                    frame #11: 0x00007fff895282da CoreFoundation`-[NSArray descriptionWithLocale:indent:] + 538
```

There are a few thousand stack frames that I omitted. The `description` method isn't smart enough to deal with recursive containers, so it keeps trying to follow the "tree" down to the end, and eventually blows up.

We can compare it for equality with itself:

```
    NSLog(@"%d", [a isEqual: a]);
```

This just says `YES`. Let's construct a second structurally identical array and compare with that:

```
    NSMutableArray *b = [NSMutableArray array];
    [b addObject: b];
    NSLog(@"%d", [a isEqual: b]);
```

Oops:

```
    (lldb) bt
    * thread #1: tid = 0x4412a, 0x00007fff8946a8d7 CoreFoundation`-[NSArray isEqualToArray:] + 103, queue = 'com.apple.main-thread, stop reason = EXC_BAD_ACCESS (code=2, address=0x7fff5f3fff28)
                    frame #0: 0x00007fff8946a8d7 CoreFoundation`-[NSArray isEqualToArray:] + 103
                    frame #1: 0x00007fff8946f6b7 CoreFoundation`-[NSArray isEqual:] + 71
                    frame #2: 0x00007fff8946aa07 CoreFoundation`-[NSArray isEqualToArray:] + 407
                    frame #3: 0x00007fff8946f6b7 CoreFoundation`-[NSArray isEqual:] + 71
                    frame #4: 0x00007fff8946aa07 CoreFoundation`-[NSArray isEqualToArray:] + 407
                    frame #5: 0x00007fff8946f6b7 CoreFoundation`-[NSArray isEqual:] + 71
                    frame #6: 0x00007fff8946aa07 CoreFoundation`-[NSArray isEqualToArray:] + 407
                    frame #7: 0x00007fff8946f6b7 CoreFoundation`-[NSArray isEqual:] + 71
                    frame #8: 0x00007fff8946aa07 CoreFoundation`-[NSArray isEqualToArray:] + 407
                    frame #9: 0x00007fff8946f6b7 CoreFoundation`-[NSArray isEqual:] + 71
```

Equality checking doesn't know how to deal with recursive containers either.

**Circular Views**  
You can do the same sort of thing with `NSView` instances:

```
    NSWindow *win = [self window];
    NSView *a = [[NSView alloc] initWithFrame: NSMakeRect(0, 0, 1, 1)];
    [a addSubview: a];
    [[win contentView] addSubview: a];
```

To make this break, all you have to do is attempt to show the window. You don't even have to try to print a description or compare it for equality like that. When trying to show the window, the app will just crash trying to chase down to the bottom of the view hierarchy:

```
    (lldb) bt
    * thread #1: tid = 0x458bf, 0x00007fff8c972528 AppKit`NSViewGetVisibleRect + 130, queue = 'com.apple.main-thread, stop reason = EXC_BAD_ACCESS (code=2, address=0x7fff5f3ffff8)
                    frame #0: 0x00007fff8c972528 AppKit`NSViewGetVisibleRect + 130
                    frame #1: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #2: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #3: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #4: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #5: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #6: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #7: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #8: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #9: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #10: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #11: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #12: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #13: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #14: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #15: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #16: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #17: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #18: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #19: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
                    frame #20: 0x00007fff8c9725c6 AppKit`NSViewGetVisibleRect + 288
```

**Hash Abuse**  
Let's create a small class whose instances are always equal to each other, but whose hash values are not:

```
    @interface AlwaysEqual : NSObject @end
    @implementation AlwaysEqual

    - (BOOL)isEqual: (id)object { return YES; }
    - (NSUInteger)hash { return random(); }

    @end
```

This is, of course, a serious breach of Cocoa's requirement that `hash` always return the same value for objects that are considered equal. Of course, this isn't strictly enforced, so the above will still compile and run just fine.

Let's start adding instances to an `NSMutableSet`:

```
    NSMutableSet *set = [NSMutableSet set];
    for(;;)
    {
        AlwaysEqual *obj = [[AlwaysEqual alloc] init];
        [set addObject: obj];
        NSLog(@"%@", set);
    }
```

This produces an amusing log:

```
    LetsBreakCocoa[17069:303] {(
                    <AlwaysEqual: 0x61000001ed70>
    )}
    LetsBreakCocoa[17069:303] {(
                    <AlwaysEqual: 0x61000001ec40>,
                    <AlwaysEqual: 0x61000001ed70>
    )}
    LetsBreakCocoa[17069:303] {(
                    <AlwaysEqual: 0x61000001ec40>,
                    <AlwaysEqual: 0x61000001ed70>
    )}
    LetsBreakCocoa[17069:303] {(
                    <AlwaysEqual: 0x61000001ec40>,
                    <AlwaysEqual: 0x61000001ed70>,
                    <AlwaysEqual: 0x61000001f930>
    )}
    LetsBreakCocoa[17069:303] {(
                    <AlwaysEqual: 0x61000001ec40>,
                    <AlwaysEqual: 0x61000001ed70>,
                    <AlwaysEqual: 0x61000001f930>
    )}
    LetsBreakCocoa[17069:303] {(
                    <AlwaysEqual: 0x61000001ec40>,
                    <AlwaysEqual: 0x61000001ed70>,
                    <AlwaysEqual: 0x61000001f930>
    )}
```

It's not exactly the same every run, but the overall pattern looks like this. `addObject:` generally adds a new object at first, then becomes less likely to succeed as more objects are added, topping out around three objects. This set now contains three supposedly identical objects, when it should never contain more than one. This is why you must always override `hash` when you override `isEqual:`.

**Selector Abuse**  
Selectors are a special data type used by the runtime to represent method names. They're essentially uniqued strings, although they aren't strictly required to be strings. In the current Objective-C runtime, they _are_ strings, and while you should never rely on that fact, it can be fun to take advantage of it to break things.

Here's a quick example:

```
    SEL sel = (SEL)"";
    [NSObject performSelector: sel];
```

This compiles and runs, and produces a really confusing error at runtime:

```
    LetsBreakCocoa[17192:303] *** NSForwarding: warning: selector (0x100001f86) for message '' does not match selector known to Objective C runtime (0x6100000181f0)-- abort
    LetsBreakCocoa[17192:303] +[NSObject ]: unrecognized selector sent to class 0x7fff75570810
```

By creating selectors from strange strings, you can produce really odd errors:

```
    SEL sel = (SEL)"]: unrecognized selector sent to class 0x7fff75570810";
    [NSObject performSelector: sel];

    LetsBreakCocoa[17262:303] +[NSObject ]: unrecognized selector sent to class 0x7fff75570810]: unrecognized selector sent to class 0x7fff75570810
```

You can even make it look like `NSObject` has stopped responding to completely normal messages:

```
    SEL sel = (SEL)"alloc";
    [NSObject performSelector: sel];

    LetsBreakCocoa[46958:303] *** NSForwarding: warning: selector (0x100001f77) for message 'alloc' does not match selector known to Objective C runtime (0x7fff8d38d879)-- abort
    LetsBreakCocoa[46958:303] +[NSObject alloc]: unrecognized selector sent to class 0x7fff75570810
```

This, of course, isn't the real `alloc` selector, but a fake selector that happens to point to a string that contains `"alloc"`. The runtime still prints it as `alloc`, though.

**Fake Objects**  
It's been getting more complicated in recent years, but an Objective-C object is still _usually_ a blob of memory where the first chunk points to the object's class. With that in mind, let's build a fake object:

```
    id obj = (__bridge id)(void *)&(Class){ [NSObject class] };
```

These fake objects totally work, too:

```
    NSMutableArray *array = [NSMutableArray array];
    for(int i = 0; i < 10; i++)
    {
        id obj = (__bridge id)(void *)&(Class){ [NSObject class] };
        [array addObject: obj];
    }
    NSLog(@"%@", array);
```

This works and logs this output:

```
    LetsBreakCocoa[17543:303] (
        "<NSObject: 0x7fff5fbfe760>",
        "<NSObject: 0x7fff5fbfe760>",
        "<NSObject: 0x7fff5fbfe760>",
        "<NSObject: 0x7fff5fbfe760>",
        "<NSObject: 0x7fff5fbfe760>",
        "<NSObject: 0x7fff5fbfe760>",
        "<NSObject: 0x7fff5fbfe760>",
        "<NSObject: 0x7fff5fbfe760>",
        "<NSObject: 0x7fff5fbfe760>",
        "<NSObject: 0x7fff5fbfe760>"
    )
```

Oops, it looks like every fake object ended up at the same address. Still worked, though. Well, until you exit the method and the autorelease pool tries to clean up:

```
    (lldb) bt
    * thread #1: tid = 0x46790, 0x00007fff8b3d55c9 libobjc.A.dylib`realizeClass(objc_class*) + 156, queue = 'com.apple.main-thread, stop reason = EXC_BAD_ACCESS (code=1, address=0x7fff00006000)
        frame #0: 0x00007fff8b3d55c9 libobjc.A.dylib`realizeClass(objc_class*) + 156
        frame #1: 0x00007fff8b3d820c libobjc.A.dylib`lookUpImpOrForward + 98
        frame #2: 0x00007fff8b3cb169 libobjc.A.dylib`objc_msgSend + 233
        frame #3: 0x00007fff8940186f CoreFoundation`CFRelease + 591
        frame #4: 0x00007fff89414ad9 CoreFoundation`-[__NSArrayM dealloc] + 185
        frame #5: 0x00007fff8b3cd65a libobjc.A.dylib`(anonymous namespace)::AutoreleasePoolPage::pop(void*) + 502
        frame #6: 0x00007fff89420d72 CoreFoundation`_CFAutoreleasePoolPop + 50
        frame #7: 0x00007fff8551ada7 Foundation`-[NSAutoreleasePool drain] + 147
```

Since those fake objects aren't properly allocated at all, things go seriously wrong once the autorelease pool tries to manipulate them after this method returns and the memory gets overwritten.

**Key-Value Coding**  
Here's an array of classes:

```
    NSArray *classes = @[
        [NSObject class],
        [NSString class],
        [NSView class]
    ];
    NSLog(@"%@", classes);
    LetsBreakCocoa[17726:303] (
        NSObject,
        NSString,
        NSView
    )
```

Here's an array of instances of those classes:

```
    NSArray *instances = [classes valueForKeyPath: @"alloc.init.autorelease"];
    NSLog(@"%@", instances);
    LetsBreakCocoa[17726:303] (
        "<NSObject: 0x61000000a600>",
        "",
        "<NSView: 0x610000136bc0>"
    )
```

Key-value coding isn't meant to be used like this at all, but it works just fine even so.

**Caller Inspection**  
The compiler builtin `__builtin_return_address` will give you the address of the code that called you:

```
    void *addr = __builtin_return_address(0);
```

From that, we can get information about the caller, including its name:

```
    Dl_info info;
    dladdr(addr, &info);
    NSString *callerName = [NSString stringWithUTF8String: info.dli_sname];
```

With this, we can do some seriously nefarious stuff, like behaving completely differently depending on what called a certain method:

```
    @interface CallerInspection : NSObject @end
    @implementation CallerInspection

    - (void)method
    {
        void *addr = __builtin_return_address(0);
        Dl_info info;
        dladdr(addr, &info);
        NSString *callerName = [NSString stringWithUTF8String: info.dli_sname];
        if([callerName isEqualToString: @"__CFNOTIFICATIONCENTER_IS_CALLING_OUT_TO_AN_OBSERVER__"])
            NSLog(@"Do some notification stuff");
        else
            NSLog(@"Do some regular stuff");
    }

    @end
```

Here's some code to test it:

```
    id obj = [[CallerInspection alloc] init];
    [[NSNotificationCenter defaultCenter] addObserver: obj selector: @selector(method) name: @"notification" object: obj];
    [[NSNotificationCenter defaultCenter] postNotificationName: @"notification" object: obj];
    [obj method];

    LetsBreakCocoa[47427:303] Do some notification stuff
    LetsBreakCocoa[47427:303] Do some regular stuff
```

Of course, this is completely unreliable, because `__CFNOTIFICATIONCENTER_IS_CALLING_OUT_TO_AN_OBSERVER__` is an internal Apple symbol and could easily change in the future.

**Dealloc Swizzle**  
Let's swizzle out `-[NSObject dealloc]` with a method that doesn't do anything. We need to get a little tricky to obtain `@selector(dealloc)` under ARC, since it won't let us write that directly:

```
    Method m = class_getInstanceMethod([NSObject class], sel_getUid("dealloc"));
    method_setImplementation(m, imp_implementationWithBlock(^{}));
```

Now we can sit back and admire the chaos this causes:

```
    for(;;)
        @autoreleasepool {
            [[NSObject alloc] init];
        }
```

Swizzling `dealloc` causes this perfectly reasonable code to leak like crazy, since objects can't actually be destroyed anymore.

**Conclusion**  
Breaking Cocoa in new and interesting ways can provide endless entertainment. Some of these manifest in real-world code as well. My first encounter with an embedded NUL in an `NSString` was a long and painful debugging session. Others are just fun and mildly educational.

That's it for today! Come back next time for more fun and games. Friday Q&A is driven by reader suggestions, as always, so if you have something you'd like to see discussed here, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
