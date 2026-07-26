---
title: 'Friday Q&A 2010-11-19: Creating Classes at Runtime for Fun and Profit'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-11-19-creating-classes-at-runtime-for-fun-and-profit.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3a4193738af1db40'
translated: false
---

> 原文：[Friday Q&A 2010-11-19: Creating Classes at Runtime for Fun and Profit](https://www.mikeash.com/pyblog/friday-qa-2010-11-19-creating-classes-at-runtime-for-fun-and-profit.html)　·　mikeash.com Friday Q&A

Posted at 2010-11-19 17:53 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-12-03: Accessors, Memory Management, and Thread Safety](https://www.mikeash.com/pyblog/friday-qa-2010-12-03-accessors-memory-management-and-thread-safety.html)  
Previous article: [Summary of the Current State of my Publications](https://www.mikeash.com/pyblog/summary-of-the-current-state-of-my-publications.html)  
Tags: [fridayqa](https://www.mikeash.com/pyblog/?tag=fridayqa) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2010-11-19: Creating Classes at Runtime for Fun and Profit

by [Mike Ash](https://www.mikeash.com/)

**`MAObjCRuntime`**  
 In my last article, I avoided making use of [`MAObjCRuntime`](http://github.com/mikeash/MAObjCRuntime), my object-oriented wrapper around the Objective-C runtime, in order to show how to use the Objective-C runtime directly. Since I've already shown how to call the runtime directly, I'll be making use of `MAObjCRuntime` today in order to make the code simpler to read and write. If you're interested in doing things the old-fashioned way, the `MAObjCRuntime` calls translate pretty directly to runtime calls, it's just more verbose and less convenient.

While I think the calls will be pretty obvious, you may want to read [`MAObjCRuntime`](https://github.com/mikeash/MAObjCRuntime)'s readme to see how it works before continuing.

**Conditional Subclassing**  
 A common problem in Mac and iOS development is supporting multiple OS versions simultaneously. Often it's necessary to use a class that exists on newer versions, but avoid using it on older versions where it's not available. Normally this can be done by using calls like `NSClassFromString`. However, sometimes it's necessary to subclass one of these classes, and the normal technique of writing `@interface YourClass : ThisMightNotExist` doesn't work too well.

(It is possible to use the normal syntax by using weak linking to pull in the class which may not exist. Unfortunately, weak linking of Objective-C classes is not very mature yet, and you have to wait for it to work all the way back to the _earliest_ OS version that you support.)

By creating the subclass at runtime only if the superclass exists, you can make code that works properly in both cases without too much effort.

As an example, I'll show how to create a subclass of a hypothetical `NSFoo` class which might not exist at runtime. The subclass will override a single method from its superclass, `-bar`, to do nothing.

First, write the function that implements the `-bar` method. As you'll recall from last time, you just write a C function that takes `id self` and `SEL _cmd` as its first two parameters, with the other parameters and the return type as usual. Here's the simple do-nothing function:

```
    static void BarOverride(id self, SEL _cmd)
    {
    }
```

Now, a function to create the subclass. The first thing it does is use

to make the class.

```
    static Class CreateMyFoo(void)
    {
        Class NSFoo = NSClassFromString(@"NSFoo");
        if(!NSFoo)
            return nil;
        
        Class myFoo = [NSFoo rt_createSubclassNamed: @"MyFoo"];
```

Now to add the new

method. We first get the method from the superclass so I can borrow its type signature string, then create a new

and add it to the subclass:

```
        SEL sel = @selector(bar);
        RTMethod *nsBar = [NSFoo rt_methodForSelector: sel];
        RTMethod *myBar = [RTMethod methodWithSelector: sel implementation: (IMP)BarOverride signature: [nsBar signature]];
        [myFoo rt_addMethod: myBar];
```

That's it! Now just return the newly created class:

```
        return myFoo;
    }
```

To complete the code, we just need a simple wrapper function that creates the above class just once and stores it, then returns it on demand. (I'm using GCD for thread safety, which may defeat the purpose of compatibility with older OSes, but it can easily be replaced with another method.)

```
    static Class MyFoo(void)
    {
        static Class c = nil;
        static dispatch_once_t pred;
        dispatch_once(&pred, ^{
            c = CreateMyFoo();
        });
        
        return c;
    }
```

Because

returns

if

doesn't exist,

will also return

in that case. All the caller has to do to use

is something like this:

```
    Class myFoo = MyFoo();
    if(myFoo)
    {
        id foo = [[myFoo alloc] init];
        // ...
    }
```

It's very common to call

in an overridden method. Unfortunately, the

keyword isn't valid in a C function, even if you're using it to implement an Objective-C method.

It's still possible, and not too hard, but you have to be a little more roundabout. You need to manually retrieve the method pointer from the superclass, then directly call it. Here's what `BarOverride` would look like just calling through to `super`:

```
    static void BarOverride(id self, SEL _cmd)
    {
        Class superclass = NSClassFromString(@"NSFoo");
        void (*superIMP)(id, SEL) = (void *)[superclass instanceMethodForSelector: @selector(bar)];
        superIMP(self, _cmd);
    }
```

Simply calling through to

is not all that useful, but you can add your own code before and after the call to augment it.

**Example Subclass**  
 Here's a more realistic example that subclasses the hypothetical `NSMysteryView` to add custom drawing and event handling:

```
    static DrawRect(id self, SEL _cmd, NSRect rect)
    {
        // draw the original stuff, but on top of a black background
        [[NSColor blackColor] setFill];
        NSRectFill(rect);
        
        // black background is down, now draw the original
        Class superclass = NSClassFromString(@"NSMysteryView");
        void (*superIMP)(id, SEL, NSRect) = [superclass instanceMethodForSelector: @selector(drawRect:)];
        superIMP(self, _cmd, rect);
    }
    
    static MouseUp(id self, SEL _cmd, NSEvent *event)
    {
        // beep if the mouse is clicked in this view
        NSBeep();
    }
    
    // encapsulate code needed to override an existing method
    static void Override(Class c, SEL sel, void *fptr)
    {
        RTMethod *superMethod = [[c superclass] rt_methodForSelector: sel];
        RTMethod *newMethod = [RTMethod methodWithSelector: sel implementation: fptr signature: [superMethod signature]];
        [c rt_addMethod: newMethod];
    }
    
    static Class CreateMyMysteryView(void)
    {
        Class NSMysteryView = NSClassFromString(@"NSMysteryView");
        if(!NSMysteryView)
            return nil;
        
        Class c = [NSMysteryView rt_createSubclassNamed: @"MyMysteryView"];
        Override(c, @selector(drawRect:), DrawRect);
        Override(c, @selector(mouseUp:), MouseUp);
        
        return c;
    }
```

Sometimes you need to intercept a call to an arbitrary object without knowing in advance what it will be. By creating a subclass of the target's class at runtime, and then swizzling the class of the target object, you can accomplish this interception. Cocoa's

Key-Value Observing

does this, as does my own

`MAZeroingWeakRef`

. Here, I'll walk through how you can do this for yourself. For a simple example, I'll show a sort of light version of what

does by making code that simply observes when an object is deallocated by overriding its

method.

A quick note: none of the code that I'm going to show is thread safe, just to keep it simple. Since this is the sort of low-level code that you might want to use from multiple threads (especially since `dealloc` could happen on other threads), keep in mind that a more practical version would want to lock access to all of the shared data.

When the object is about to be destroyed, it will post a notification. Of course we'll want a constant to hold the notification name:

```
    NSString *MyObjectWillDeallocateNotification = @"MyObjectWillDeallocateNotification";
```

Now, we only want to create one subclass of any given class. If two objects of the same class are passed in to the system, they should both be swizzled to the same dynamic subclass, rather than creating two identical dynamic subclasses. To accomplish this, we'll keep a dictionary that maps from classes to subclasses. It's also useful to keep a set of the already-created subclasses:

```
    static NSMutableDictionary *gSubclassesDict;
    static NSMutableSet *gSubclasses;
```

Now, a small function to query the dictionary and either return what it contains, or call a function to create the subclass, insert it into the dictionary, and return that:

```
    static Class GetSubclassForClass(Class c)
    {
        Class subclass = [gSubclassesDict objectForKey: c];
        if(!subclass)
        {
            subclass = CreateSubclassForClass(c);
            [gSubclassesDict setObject: subclass forKey: c];
            [gSubclasses addObject: subclass];
        }
        return subclass;
    }
```

Before we can write

, we need to write a

override. All this override needs to do is post the notification and then call

. However, calling

is complicated because not only is this a dynamically allocated class, but one whose superclass isn't known at compile time. Thus we need to perform a search at runtime to find the correct superclass.

It is _not_ correct to simply use `[self superclass]` in this case. Although our dynamic subclass is _probably_ the very last class to be set, and so `[self superclass]` would _probably_ return the correct answer, it's not guaranteed. Some other piece of code (like KVO) could have pulled the same dynamic subclassing trick that we're pulling after we did it, which means their class would be at the bottom instead of our. To be truly robust, we have to search in a loop until we come across a class that has an entry in `gSubclassesDict`, and then that is the one where we need to send our `dealloc`.

Here's what the full `dealloc` override function looks like:

```
    static void Dealloc(id self, SEL _cmd)
    {
        [[NSNotificationCenter defaultCenter] postNotificationName: MyObjectWillDeallocateNotification object: self];
        
        Class c = [self rt_class];
        while(c && ![gSubclassesDict objectForKey: c])
            c = [c superclass];
        
        // if it wasn't found, something went horribly wrong
        assert(c);
        
        void (*superIMP)(id, SEL) = [c instanceMethodForSelector: @selector(dealloc)];
        superIMP(self, _cmd);
    }
```

Now we're ready to write

. There's nothing complex here, this looks just like the other subclass-creation code we've written:

```
    static Class CreateSubclassForClass(Class c)
    {
        // give the subclass a sensible name
        NSString *name = [NSString stringWithFormat: @"%@_MyDeallocNotifying", [class name]];
        Class subclass = [c rt_createSubclassNamed: name];
        
        // use the Override function from above
        Override(c, @selector(dealloc), Dealloc);
        
        return subclass;
    }
```

Finally, a function to transform an object to post this notification. We start out by checking to see if it's already been added by seeing if it has one of our subclasses in its hierarchy:

```
    void MakeObjectPostDeallocNotification(id obj)
    {
        Class c = [obj rt_class];
        while(c && ![gSubclasses containsObject: c])
            c = [c superclass];
        // if we found one, then nothing else to do
        if(c)
            return;
        
        // not yet set, grab the subclass
        c = GetSubclassForClass([obj rt_class]);
        // set the class of the object to the subclass
        [obj rt_setClass: c];
    }
```

That's it! You can now call

and then use

to listen for the notification.

**Caveats**  
 There are some gotchas to this technique. From easiest to hardest:

1. if a targeted object is archived, the archiver will record the custom subclass. When unarchiving, it will try to instantiate that custom subclass. Since these classes are created dynamically, that class may not exist yet, preventing the unarchiver from instantiating the object. To fix this, you can override

  in the subclass to return the superclass, so that the archiver records the correct class.
2. as I mentioned previously, KVO makes use of this same technique. Unfortunately, Apple's code does not tolerate having subclasses created beneath its own custom classes. To work around this, you can subclass the "real" class and then insert your new subclass into the class hierarchy between the KVO class and the "real" class.

  `MAZeroingWeakRef`

  shows how to do this, just search for "KVO".
3. due to how toll-free bridging is implemented, you cannot subclass the bridged classes, nor can you reliably intercept messages to them in other ways. Depending on exactly what you're doing, you may be able to

  use some really nasty hacks

  , but in general your best bet is to simply not try to mess with bridged classes.

Creating classes at runtime is a powerful technique. Today I've shown how you can use it to create subclasses of classes that you can't reference at compile time, and to dynamically create subclasses of arbitrary classes in order to intercept calls to them. This is the sort of thing you can use to blow a very large hole in your foot, but it can also let you do things that simply can't be done otherwise.

That's it for today. Come back in two weeks for another Friday Q&A. As always, if you have an idea for a topic that you would like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
