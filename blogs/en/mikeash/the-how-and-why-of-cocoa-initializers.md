---
title: The How and Why of Cocoa Initializers
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/the-how-and-why-of-cocoa-initializers.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3e6eb5c9306bde78'
translated: false
---

> 原文：[The How and Why of Cocoa Initializers](https://www.mikeash.com/pyblog/the-how-and-why-of-cocoa-initializers.html)　·　mikeash.com Friday Q&A

Posted at 2008-10-09 23:43 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Key-Value Observing Done Right](https://www.mikeash.com/pyblog/key-value-observing-done-right.html)  
Previous article: [It's a Poor Carpenter Who Blames His Tools or: Xcode Sucks Again](https://www.mikeash.com/pyblog/its-a-poor-carpenter-who-blames-his-tools-or-xcode-sucks-again.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [init](https://www.mikeash.com/pyblog/?tag=init) [initializer](https://www.mikeash.com/pyblog/?tag=initializer) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [super](https://www.mikeash.com/pyblog/?tag=super)

The How and Why of Cocoa Initializers

by [Mike Ash](https://www.mikeash.com/)

**How it must be done**  
 It should come as no surprise that the right way to write an initializer is the Apple Way, which should be familiar to everyone reading this:

```
- init {
    if((self = [super init])) {
        // set up instance variables and whatever else here
    }
    return self;
}
```

Minor variations are of course just fine, as long as they're equivalent. For example, some people like to check self for nil and then return nil immediately to avoid putting initialization in a separate block. Some people like to break out the assignment, then check just plain `self` in the if statement. These all do the same thing, so it's just a matter of taste.

**Call `super` or `self`?**  
 For the sake of completeness, I'll first cover a more obvious part of this method, the call to `[super init]`. If you're really new to Objective-C and came from a language like C++ or Java, this may puzzle you. It's here because Objective-C initializers are just plain methods like any other method. If you want the superclass initializer to be called, then you have to call it yourself. You also have a choice here, between calling `super` and calling `self`. Which one you use depends on circumstances. If you're not sure, you can apply one of these rules of thumb:

1. Call super if and only if the method name matches.
2. Call super if and only if you're implementing your class's [designated initializer](http://developer.apple.com/documentation/Cocoa/Conceptual/CocoaFundamentals/CocoaObjects/chapter_3_section_6.html#//apple_ref/doc/uid/TP40002974-CH4-SW3). (This rule is more accurate, but sometimes harder to apply.)

**Checking `nil`**  
 And again for the sake of completeness, some may wonder why the if statement is there at all. The reason is because your superclass may fail to initialize (for example, if the parameters weren't consistent) and the standard way to indicate this is to release the object and return `nil` from the initializer. If you continue initializing your state after this happens, you will crash. The if statement lets you fail gracefully if your superclass failed.

**The assignment**  
 Now on to the meat of the controversy. The above is fairly obvious and I doubt anyone will disagree with it. But that assignment to `self` is frequently disputed. Let's run through the myths one by one, from most obvious to least obvious.

**Myth:** The superclass initializer will only ever return nil or self.  
 **Fact:** Many Cocoa classes return a different pointer from their initializer.

**Myth:** Fine, but that only happens with class clusters, and only when you don't subclass them.  
 **Fact:** It's true that class clusters don't do this to their subclasses, but _other_ classes can and do.

**Myth:** But those other subclasses are things you would never want to subclass anyway, like NSColorPanel, or it only happens when you do something wrong, like subclass a singleton but fail to make that subclass the singleton.  
 **Fact:** These are indeed situations where it can happen, but it's not limited to these situations.

**Myth:** The superclass initializer has to return `self` because my initializer can only deal with instances of my class.  
 **Fact:** The superclass initializer could return a _different_ instance of your class.

**Myth:** It can't return a different instance because you're not allowed to re-initialize instances.  
 **Fact:** It's true about re-initialization, but it could allocate a _new_ instance.

**Myth:** But it has no reason to do that. It already _has_ a new instance right there.  
 **Fact:** It has a good reason to do that if it wants some _extra_ storage at the end, like if it created a dynamic subclass of your class and wants to use an instance of that subclass.

This is why the standard initializer pattern is the only one that works. Cocoa classes can _and do_ deallocate the original instance, then allocate a new instance of the same class (or a subclass) and return it from their initializers. This is admittedly rare, but it is legal and it does happen. And that, in a nutshell, is why the standard Apple initializer pattern is the only correct way.

**Conclusion**  
 To summarize, the superclass's initializer can return one of three things, and the standard Apple pattern deals with them all:

1. `self` (This is what you get the vast, vast majority of the time.)
2. `nil` (On failure.)
3. A new instance of your class (Rare but legitimate.)

Many people like to leave off the assignment and just check for nil. This works fine for cases 1 and 2 but will fail in very confusing ways for case 3.

There are actually a couple of other things that can potentially be returned:

1. An instance of a different class
2. An existing instance of your class

Case 4 only happens if you did something wrong, so it's not something you should be handling. Case 5 only happens if you either did something wrong, or if you subclassed a singleton. If you subclass a singleton then you should make sure your initializer can handle re-initializing the existing singleton instance. This is just good practice for singletons in general anyway.

(As an aside, the standard pattern is _not_ necessary if you subclass NSObject directly. This is because `-[NSObject init]` in documented to do nothing and always return self. However, using the principle that we should always write code that's robust to changes, in this case to changes in what class you inherit from, I very much recommend using the standard pattern even for direct NSObject subclasses.)

So there you have it. This is how to write your initializers, and why you should write them that way. I hope it's clear enough not to generate dispute, but if you must, comment away.

**References**

1. [re: self = [super init] debate.](http://www.cocoabuilder.com/archive/message/cocoa/2008/2/11/198591) - Ben Trumbull posts on [cocoa-dev](http://lists.apple.com/mailman/listinfo/cocoa-dev) to explain some key points on the subject.
2. [NSManagedObject Class Reference](http://developer.apple.com/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSManagedObject_Class/Reference/NSManagedObject.html#//apple_ref/occ/instm/NSManagedObject/initWithEntity:insertIntoManagedObjectContext:) - This class is an example of a class which returns a new, different instance of the class being initialized.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/the-how-and-why-of-cocoa-initializers.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
