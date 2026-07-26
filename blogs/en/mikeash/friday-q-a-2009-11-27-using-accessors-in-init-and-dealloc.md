---
title: 'Friday Q&A 2009-11-27: Using Accessors in Init and Dealloc'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-11-27-using-accessors-in-init-and-dealloc.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6e284c24b3e23ce5'
translated: false
---

> 原文：[Friday Q&A 2009-11-27: Using Accessors in Init and Dealloc](https://www.mikeash.com/pyblog/friday-qa-2009-11-27-using-accessors-in-init-and-dealloc.html)　·　mikeash.com Friday Q&A

Posted at 2009-11-27 16:32 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-12-04: Building Standalone iPhone Web Apps](https://www.mikeash.com/pyblog/friday-qa-2009-12-04-building-standalone-iphone-web-apps.html)  
Previous article: [Friday Q&A 2009-11-20: Probing Cocoa With PyObjC](https://www.mikeash.com/pyblog/friday-qa-2009-11-20-probing-cocoa-with-pyobjc.html)  
Tags: [accessors](https://www.mikeash.com/pyblog/?tag=accessors) [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2009-11-27: Using Accessors in Init and Dealloc

by [Mike Ash](https://www.mikeash.com/)

**Introduction**  
 There has been a change in the Cocoa community in the past few years, where the use of accessors in `init`/`dealloc` is frowned upon, recommend against, and outright considered to be wrong. It is much better, they say, to directly access instance variables instead. In other words, the recommendation is to write code like this:

```
    - (id)initWithWhatever: (id)whatever
    {
        if((self = [self init]))
        {
            _whatever = [whatever retain];
        }
        return self;
    }
    
    - (void)dealloc
    {
        [_whatever release];
        
        [super dealloc];
    }
```

The alternative is to use accessors, like this:

```
    - (id)initWithWhatever: (id)whatever
    {
        if((self = [self init]))
        {
            [self setWhatever: whatever];
        }
        return self;
    }
    
    - (void)dealloc
    {
        [self setWhatever: nil];
        
        [super dealloc];
    }
```

The pros of using accessors in

/

are pretty much the same as the pros of using them anywhere else. They decouple the code from your implementation, and in particular help you with memory management. How many times have you accidentally written code like this?

```
    - (id)init
    {
        _ivar = [NSArray arrayWithObjects:...];
        return self;
    }
```

I expect the answer will vary quite a bit (I haven't made this particular error in quite a long time) but using an accessor will make sure you don't make this mistake:

```
    - (id)init
    {
        [self setIvar: [NSArray arrayWithObjects:...]];
        return self;
    }
```

Furthermore, you might have ancillary state, like caches, summaries, etc. that need to be set up and torn down when the object value changes. Correct use of accessors can ensure that all of this happens as it needs to when the object is created and destroyed without duplicate code.

**Cons of Accessors**  
 The downside to using accessors in this way can be summed up in one short sentence: accessors can have side effects. Sometimes these side effects are undesirable for `init`/`dealloc`.

When writing a setter, it needs to behave correctly if you're going to call it from `init`/`dealloc`. This means dealing with a partially constructed object.

Worse, if you ever override a setter in a subclass, you need to write it to handle the case where the superclass is using that setter to initialize or destroy its ivars. For example, this bit of innocuous-looking code is potentially dangerous:

```
    - (void)setSomeObj: (id)obj
    {
        [anotherObj notifySomething];
        [super setSomeObj: obj];
    }
    
    - (void)dealloc
    {
        [anotherObj release];
        [super dealloc];
    }
```

If the superclass uses the accessor to destroy

, then the override will execute after

has already executed, causing the override to access a dangling reference to

, probably causing a nice crash.

It's not hard to fix this code to handle the situation gracefully. Simply assign `anotherObj = nil` after releasing it in `dealloc`, and everything works again. In general it's not difficult to make sure that your overrides behave properly, but if you're going to use accessors like this then you must remember to, and that is the difficult part.

**Key-Value Observing**  
 A topic which is frequently brought up in these discussions is key-value observing, because KVO is a common way for accessors to have side effects. Like other cases, if KVO side effects are triggered when the object is partially initialized or destroyed, and that code isn't written to tolerate such an object, bad things will occur. I personally think that it's mostly a red herring.

The reason it's mostly a red herring is because 99% of the time, KVO is not set up on an object until after it's already fully initialized, and is ceased before an object is destroyed. It is _conceivable_ for KVO to be used such that it activates earlier or terminates later, but it's unlikely in practice.

It's not possible for outside code to do anything with your object until it's fully initialized, unless your initializer itself is passing pointers around to outside objects. And likewise, it's not possible for outside code to keep a KVO reference to your object as it's executing its `dealloc` method, because it's too late for it to remove it, unless your `dealloc` triggers something that allows it to do so. Superclass code does execute in these timeframes, but superclass code is extremely unlikely to do anything to cause external objects to observe properties that the superclass itself doesn't even have.

**Conclusion**  
 Now you know the pros and cons; should you use accessors in `init` and `dealloc`? In my opinion, it can go either way. The advantages aren't generally that great. The downsides are minor. I don't use accessors for the vast majority of my instance variables, but there are certain cases where the advantages become significant because I'm doing something special with an ivar, and in that case I don't hesitate to let the accessors save me some headache.

That's it for this week. Come back next week for another round. If you have a topic you would like to see covered here, [send it in!](mailto:mike@mikeash.com) Friday Q&A is driven by your suggestions, and the more I receive, the better topics you get to read about.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
