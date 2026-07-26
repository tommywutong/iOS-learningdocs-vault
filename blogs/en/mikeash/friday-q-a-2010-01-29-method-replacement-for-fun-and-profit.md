---
title: 'Friday Q&A 2010-01-29: Method Replacement for Fun and Profit'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-01-29-method-replacement-for-fun-and-profit.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6daafc048ee16cd6'
translated: false
---

> 原文：[Friday Q&A 2010-01-29: Method Replacement for Fun and Profit](https://www.mikeash.com/pyblog/friday-qa-2010-01-29-method-replacement-for-fun-and-profit.html)　·　mikeash.com Friday Q&A

Posted at 2010-01-29 19:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-02-05: Error Returns with Continuation Passing Style](https://www.mikeash.com/pyblog/friday-qa-2010-02-05-error-returns-with-continuation-passing-style.html)  
Previous article: [Friday Q&A 2010-01-22: Toll Free Bridging Internals](https://www.mikeash.com/pyblog/friday-qa-2010-01-22-toll-free-bridging-internals.html)  
Tags: [evil](https://www.mikeash.com/pyblog/?tag=evil) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [override](https://www.mikeash.com/pyblog/?tag=override) [swizzling](https://www.mikeash.com/pyblog/?tag=swizzling)

Friday Q&A 2010-01-29: Method Replacement for Fun and Profit

by [Mike Ash](https://www.mikeash.com/)

**Overriding Methods**  
 Overriding methods is a common task in just about any object oriented language. Most of the time you do this by subclassing, a time-honored technique. You subclass, you implement the method in the subclass, you instantiate the subclass when necessary, and instances of the subclass use the overridden method. Everybody knows how to do this.

Sometimes, though, you need to override methods that are in objects whose instantiation you don't control. Subclassing doesn't suffice in that case, because you can't make that code instantiate your subclass. Your method override sits there, twiddling its thumbs, accomplishing nothing.

**Posing**  
 Posing is an interesting technique but, alas, is now obsolete, since Apple no longer supports it in the "new" (64-bit and iPhone) Objective-C runtime. With posing, you subclass, then pose the subclass as its superclass. The runtime does some magic and suddenly the subclass is used everywhere, and method overrides become useful again. Since this is no longer supported, I won't go into details.

**Categories**  
 Using a category, you can easily override a method in an existing class:

```
    @implementation NSView (MyOverride)
    
    - (void)drawRect: (NSRect)r
    {
        // this runs instead of the normal -[NSView drawRect:]
        [[NSColor blueColor] set];
        NSRectFill(r);
    }
    
    @end
```

However, this really only works if you want to override a method implemented in a superclass of the class you're targeting. When the method in question exists in the class where you want to override it, using a category to perform the override results in two problems:

1. It's impossible to call through to the original implementation of the method. The new implementation replaces the original, which is simply lost. Most overrides want to add functionality, not completely replace it, but it's not possible with a category.
2. The class in question could implement the method in question in a category too, and the runtime doesn't guarantee which implementation "wins" when two categories contain methods with the same name.

**Swizzling**  
 Using a technique called method swizzling, you can replace an existing method from a category without the uncertainty of who "wins", and while preserving the ability to call through to the old method. The secret is to give the override a different method name, then swap them using runtime functions.

First, you implement the override with a different name:

```
    @implementation NSView (MyOverride)
    
    - (void)override_drawRect: (NSRect)r
    {
        // call through to the original, really
        [self override_drawRect: r];
        
        [[NSColor blueColor] set];
        NSRectFill(r);
    }
    
    @end
```

Notice how calling through to the original is done by calling the _same_ method, in what looks like a recursive call. This works because the method gets swapped with the original implementation. At runtime, the method called `override_drawRect:` is actually the _original_!

To swap the method, you need a bit of code to move the new implementation in and the old implementation out:

```
    void MethodSwizzle(Class c, SEL origSEL, SEL overrideSEL)
    {
        Method origMethod = class_getInstanceMethod(c, origSEL);
        Method overrideMethod = class_getInstanceMethod(c, overrideSEL);
```

To be completely general, this code has to handle two cases. The first case is when the method to be overridden is _not_ implemented in the class in question, but rather in a superclass. The second case is when the method in question does exist in the class itself. These two cases need to be handled a bit differently.

For the case where the method only exists in a superclass, the first step is to add a new method to this class, using the override as the implementation. Once that's done, then the override method is replaced with the original one.

The step of adding the new method can also double as a check to see which case is actually present. The runtime function `class_addMethod` will fail if the method already exists, and so can be used for the check:

```
        if(class_addMethod(c, origSEL, method_getImplementation(overrideMethod), method_getTypeEncoding(overrideMethod)))
        {
```

If the add succeeded, then replace the override method with the original, completing the (conceptual) swap:

```
            class_replaceMethod(c, overrideSEL, method_getImplementation(origMethod), method_getTypeEncoding(origMethod));
        }
```

If the add failed, then it's the second case; both methods exist in the class in question. For that case, the runtime provides a handy function called method_exchangeImplementations which just swaps the two methods in place:

```
        else
        {
            method_exchangeImplementations(origMethod, overrideMethod);
        }
    }
```

You'll notice that the `method_exchangeImplementations` call just uses the two methods that the code already fetched, and you might wonder why it can't just go straight to that and skip all of the annoying stuff in the middle.

The reason the code needs the two cases is because `class_getInstanceMethod` will actually return the `Method` for the _superclass_ if that's where the implementation lies. Replacing that implementation will replace the method for the wrong class!

As a concrete example, imagine replacing `-[NSView description]`. If `NSView` doesn't implement `-description` (which is probable) then you'll get `NSObject`'s `Method` instead. If you called `method_exchangeImplementations` on that `Method`, you'd replace the `-description` method on `NSObject` with your own code, which is not what you want to do!

(When that's the case, a simple category method would work just fine, so this code wouldn't be needed. The problem is that you can't know whether a class overrides a method from its superclass or not, and that could even change from one OS release to the next, so you have to assume that the class may implement the method itself, and write code that can handle that.)

Finally we just need to make sure that this code actually gets called when the program starts up. This is easily done by adding a `+load` method to the `MyOverride` category:

```
    + (void)load
    {
        MethodSwizzle(self, @selector(drawRect:), @selector(override_drawRect:));
    }
```

**Direct Override**  
 This is a bit complicated, though. The swizzling concept is a little weird, and especially the way that you call through to the original implementation tends to bend the mind a bit. It's a pretty standard technique, but I want to propose a way that I believe is a little simpler, both in terms of being easier to understand and easier to implement.

It turns out that there's no need to preserve the method-ness of the original method. The dynamic dispatch involved in `[self override_drawRect: r]` is completely unnecessary. We know which implementation we want right from the start.

Instead of moving the original method into a new one, just move its implementation into a global function pointer:

```
    void (*gOrigDrawRect)(id, SEL, NSRect);
```

Then in `+load` you can fill that global with the original implementation

```
    + (void)load
    {
        Method origMethod = class_getInstanceMethod(self, @selector(drawRect:));
        gOrigDrawRect = (void *)method_getImplementation(origMethod);
```

(I like to cast to `void *` for these things just because it's so much easier to type than long, weird function pointer types, and thanks to the magic of C, the `void *` gets implicitly converted to the right pointer type anyway.)

Next, replace the original. Like before, there are two cases to worry about, so I'll first add the method, then replace the existing one if it turns out that there is one:

```
        if(!class_addMethod(self, @selector(drawRect:), (IMP)OverrideDrawRect, method_getTypeEncoding(origMethod)))
            method_setImplementation(origMethod, (IMP)OverrideDrawRect);
    }
```

Finally, implement the override. Unlike before, it's now a function, not a method:

```
    static void OverrideDrawRect(NSView *self, SEL _cmd, NSRect r)
    {
        gOrigDrawRect(self, _cmd, r);
        [[NSColor blueColor] set];
        NSRectFill(r);
    }
```

A bit uglier, certainly, but I think it's simpler and easier to follow.

**The Obligatory Warning**  
 Overriding methods on classes you don't own is a dangerous business. Your override could cause problems by breaking the assumptions of the class in question. Avoid it if it's at all possible. If you must do it, code your override with extreme care.

**Conclusion**  
 That's it for this week. Now you know the full spectrum of method override possibilities in Objective-C, including one variation that I haven't seen discussed much elsewhere. Use this power for good, not for evil!

Come back in seven days for the next edition. Until then, [keep sending in your suggestions for topics](mailto:mike@mikeash.com). Friday Q&A is powered by reader submissions, so if you have an idea for a topic to cover here, send it in!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-01-29-method-replacement-for-fun-and-profit.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
