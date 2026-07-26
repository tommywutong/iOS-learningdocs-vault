---
title: 'Friday Q&A 2009-05-22: Objective-C Class Loading and Initialization'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-05-22-objective-c-class-loading-and-initialization.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:995965bbab35039c'
translated: false
---

> 原文：[Friday Q&A 2009-05-22: Objective-C Class Loading and Initialization](https://www.mikeash.com/pyblog/friday-qa-2009-05-22-objective-c-class-loading-and-initialization.html)　·　mikeash.com Friday Q&A

Posted at 2009-05-23 00:37 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-06-05: Introduction to Valgrind](https://www.mikeash.com/pyblog/friday-qa-2009-06-05-introduction-to-valgrind.html)  
Previous article: [Use NSOperationQueue](https://www.mikeash.com/pyblog/use-nsoperationqueue.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2009-05-22: Objective-C Class Loading and Initialization

by [Mike Ash](https://www.mikeash.com/)

How classes actually get loaded into memory in Objective-C aren't anything that you, the programmer, need to worry about most of the time. It's a bunch of complicated stuff that's handled by the runtime linker and is long done before your code ever starts to run.

For most classes, that's all you need to worry about. But some classes need to do more, and actually run some code in order to perform some kind of setup. A class may need to initialize a global table, cache values from user defaults, or do any number of other tasks.

The Objective-C runtime uses two methods to provide this functionality: `+initialize` and `+load`.

**+load**  
 `+load` is invoked as the class is actually loaded, if it implements the method. This happens very early on. If you implement `+load` in an application or in a framework that an application links to, `+load` will run before `main()`. If you implement `+load` in a loadable bundle, then it runs during the bundle loading process.

Using `+load` can be tricky because it runs so early. Obviously some classes need to be loaded before others, so you can't be sure that your other classes have had `+load` invoked yet. Worse than this, C++ static initializers in your app (or framework or plugin) won't have run yet, so if you run any code that relies on that it will likely crash. The good news is that frameworks you link to are guaranteed to be fully loaded by this point, so it's safe to use framework classes. Your superclasses are also guaranteed to be fully loaded, so they are safe to use as well. Keep in mind that there's no autorelease pool present at loading time (usually) so you'll need to wrap your code in one if you're calling into Objective-C stuff.

An interesting feature of `+load` is that it's special-cased by the runtime to be invoked in categories which implement it as well as the main class. This means that if you implement `+load` in a class and in a category on that class, both will be called. This probably goes against everything you know about how categories work, but that's because `+load` is not a normal method. This feature means that `+load` is an excellent place to do evil things like method swizzling.

**+initialize**  
 The `+initialize` method is invoked in a more sane environment and is usually a better place to put code than `+load`. `+initialize` is interesting because it's invoked lazily and may not be invoked at all. When a class first loads, `+initialize` is not called. When a message is sent to a class, the runtime first checks to see if `+initialize` has been called yet. If not, it calls it before proceeding with the message send. Conceptually, you can think of it as working like this:

```
    id objc_msgSend(id self, SEL _cmd, ...)
    {
        if(!self->class->initialized)
            [self->class initialize];
        ...send the message...
    }
```

It is of course considerably more complex than that due to thread safety and many other fun things, but that's the basic idea. `+initialize` happens once per class, and it happens the first time a message is sent to that class. Like `+load`, `+initialize` is always sent to all of a class's superclasses before it's sent to the class itself.

This makes `+initialize` safer to use because it's usually called in a much more forgiving environment. Obviously the environment depends on exactly when that first message send happens, but it's virtually certain to at least be after your call to `NSApplicationMain()`.

Because `+initialize` runs lazily, it's obviously not a good place to put code to register a class that otherwise wouldn't get used. For example, NSValueTransformer or NSURLProtocol subclasses can't use `+initialize` to register themselves with their superclasses, because you set up a chicken-and-egg situation.

This makes it a good place to do virtually everything else as far as class loading goes, though. The fact that it runs in a much more forgiving environment means you can be much freer with the code you write, and the fact that it runs lazily means that you don't waste resources setting your class up until your class actually gets used.

There's one more trick to `+initialize`. In my pseudocode above I wrote that the runtime does `[self->class initialize]`. This implies that normal Objective-C dispatch semantics apply, and that if the class doesn't implement it, the superclass's `+initialize` will run instead. That's exactly what happens. Because of this, you should always write your `+initialize` method to look like this:

```
   + (void)initialize
    {
        if(self == [WhateverClass class])
        {
            ...perform initialization...
        }
    }
```

Without that extra check, your initializations could run twice if you ever have a subclass that doesn't implement its own `+initialize` method. This is not just a theoretical concern, even if you don't write any subclasses. Apple's Key-Value Observing [creates dynamic subclasses](http://www.mikeash.com/?page=pyblog/friday-qa-2009-01-23.html) which don't override `+initialize`.

**Conclusion**  
 Objective-C offers two ways to automatically run class-setup code. The `+load` method is guaranteed to run very early, as soon as a class is loaded, and is useful for code that must also run very early. This also makes it dangerous, as it's not a very friendly environment to run it.

The `+initialize` method is much nicer for most setup tasks, because it runs lazily and in a nice environment. You can do pretty much anything you want from here, as long as it doesn't need to happen until some external entity messages your class.

That wraps up Friday Q&A for this week. Come back next week for another exciting edition. As always, [e-mail](mailto:mike@mikeash.com) your suggestions or post them below. Without your valuable contribution of ideas, Friday Q&A can't operate, so send yours in today!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-05-22-objective-c-class-loading-and-initialization.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
