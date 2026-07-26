---
title: 'Friday Q&A 2011-08-19: Namespaced Constants and Functions'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-08-19-namespaced-constants-and-functions.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9e78bb7b41d7c583'
translated: false
---

> 原文：[Friday Q&A 2011-08-19: Namespaced Constants and Functions](https://www.mikeash.com/pyblog/friday-qa-2011-08-19-namespaced-constants-and-functions.html)　·　mikeash.com Friday Q&A

Posted at 2011-08-19 14:40 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2011-09-02: Let's Build NSAutoreleasePool](https://www.mikeash.com/pyblog/friday-qa-2011-09-02-lets-build-nsautoreleasepool.html)  
Previous article: [See Me Speak at Voices That Matter in Boston](https://www.mikeash.com/pyblog/see-me-speak-at-voices-that-matter-in-boston.html)  
Tags: [c](https://www.mikeash.com/pyblog/?tag=c) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2011-08-19: Namespaced Constants and Functions

by [Mike Ash](https://www.mikeash.com/)

**Traditional Constants**  
There are three standard techniques for creating constants in C: `#define`, `const` global variables, and `enum`.

The use of `#define` is straightforward. Simply create a macro with the name and value you want to use:

```
    #define MAAnswerToTheQuestion 42
    #define MAThingDidChangeNotification @"MAThingDidChangeNotification"
```

The main downside to this approach is that it doesn't interact nicely with the debugger. Since `#define` is a preprocessor construct, the debugger doesn't see `MAAnswerToTheQuestion`, just `42`, so trying to get it to print the value of `MAAnswerToTheQuestion` won't work. It's also a bit ugly, and you can get into some serious trouble if you forget to parenthesize a more complicated expression like `#define MAAnswerToTheQuestion 40 + 2`.

Global variable constants are a little more complex, but should be familiar since they're the same as a regular global variable, just with the `const` keyword added. This follows a more typical C pattern of a declaration in the header, then a definition in the implementation file. The header looks like this:

```
    extern const int MAAnswerToTheQuestion;
    extern NSString * const MAThingDidChangeNotification;
```

Note the odd position of the `const` keyword in the second one. Writing the more natural type of `const NSString *` won't have the intended effect. That declares a pointer to a `const NSString`, when what we want is a `const` pointer to a regular `NSString`.

The definition in the implementation file is much the same, minus the 'extern' and with an initializer:

```
    const int MAAnswerToTheQuestion = 42;
    NSString * const MAThingDidChangeNotification = @"MAThingDidChangeNotification";
```

This technique is a little more wordy but works more like you might expect it to. The symbols will be visible to the debugger and won't have strange interactions with the preprocessor.

The `enum` technique only works for integers, but can be nice for them:

```
    enum MAConstants
    {
        MAAnswerToTheQuestion = 42,
        MAMusketeers = 3,
        MACircumferenceOfEarth = 199211 // in furlongs
    };
```

This ends up being reasonably nice, but is somewhat unnatural for constants which aren't part of a single group, as `enums` are typically used.

**Namespaced Constants**  
Like other global symbols in Objective-C, it's normal to prefix constants with the name of the class that they're associated with or other pertinent info. This not only helps organize the constants and tell the reader where they're from, but also prevents inadvertent naming conflicts between two constants with a similar purpose from different sections of the program.

As an example, let's imagine a class called `MANotifyingArray` which posts notifications when its contents are altered. The names of these notifications are declared as string constants, along with some `userInfo` keys for more information:

```
    const NSString * MANotifyingArrayDidAddObjectNotification;
    const NSString * MANotifyingArrayDidChangeObjectNotification;
    const NSString * MANotifyingArrayDidRemoveObjectNotification;

    // userInfo key pointing to NSNumber
    const NSString * MANotifyingArrayIndexChangedKey;

    // userInfo key containing the changed object
    const NSString * MANotifyingArrayObjectChangedKey;
```

And then the implementation file would have pretty much the same thing again, slightly different. This is really verbose and ugly, and there's a ton of repetition.

I do a fair bit of Python programming as well, and in Python I can stuff constants into a class to reduce redundancy while preserving organization and preventing conflicts. The above might look like this in Python:

```
    class MANotifyingArray:
        class notifications:
            didAddObject = 'didAddObject'
            didChangeObject = 'didChangeObject'
            didRemoveObject = 'didRemoveObject'

            class keys:
                indexChanged = 'indexChanged'
                objectChanged = 'objectChanged'
```

These values could then be accessed by writing code like `MANotifyingArray.notifications.didAddObject` or `MANotifyingArray.notifications.keys.indexChanged`. This is much easier to read and write and also gives us a nice hierarchy.

Wouldn't it be nice if we could do this in Objective-C as well? It turns out that we can, or very nearly.

It's not possible to use a class for this purpose as the Python example does, but we can use a struct. The notifications above would look like this:

```
    // in the header
    extern const struct MANotifyingArrayNotificationsStruct
    {
        NSString *didAddObject;
        NSString *didChangeObject;
        NSString *didRemoveObject;
    } MANotifyingArrayNotifications;

    // in the implementation
    const struct MANotifyingArrayNotificationsStruct MANotifyingArrayNotifications = {
        .didAddObject = @"didAddObject",
        .didChangeObject = @"didChangeObject",
        .didRemoveObject = @"didRemoveObject"
    };
```

The `.didAddObject = ...` syntax is a new feature of C99 which allows explicitly initializing individual fields of a struct. It's not strictly necessary here, but it makes this code considerably more clear.

These constants can then be accessed by writing code like `MANotifyingArrayNotifications.didAddObject`. How nice!

We can go further and even replicate the nested hierarchy of the Python version. Here's what the code looks like with that added in:

```
    // in the header
    extern const struct MANotifyingArrayNotifications
    {
        NSString *didAddObject;
        NSString *didChangeObject;
        NSString *didRemoveObject;
        struct
        {
            NSString *indexChanged;
            NSString *objectChanged;
        } keys;
    } MANotifyingArrayNotifications;

    // in the implementation
    const struct MANotifyingArrayNotifications MANotifyingArrayNotifications = {
        .didAddObject = @"didAddObject",
        .didChangeObject = @"didChangeObject",
        .didRemoveObject = @"didRemoveObject",
        .keys = {
            .indexChanged = @"indexChanged",
            .objectChanged = @"objectChanged"
        }
    };
```

The nested constants can then be accessed just as you would expect, with `NSNotifyingArrayNotifications.keys.indexChanged` and similar.

Overall, this ends up working nicely. A great deal of the redundancy of the standard global variable approach is eliminated, and the constants are placed in a hierarchy that's easy to understand.

It's certainly not perfect. There's substantial redundancy in having to declare a separate `struct` type in addition to the variable. However, the pros substantially outweigh the cons in my view.

**Namespaced Functions**  
But wait, there's more! The same basic technique can be used to create namespaced functions as well. Plain functions aren't found as often in typical Cocoa/Objective-C code, but they still show up. Cocoa itself contains many helpful functions like `NSSelectorFromString`, `NSPointInRect`, and the ubiquitous `NSLog`.

We can use the same basic struct technique to namespace these functions. The struct will contain function pointers, and then when initializing the struct, we'll just have to implement the function privately and then point the function pointer at the real function.

For an example, let's make a few extra utility functions for `NSRect`:

```
    extern const struct MARectUtils
    {
        NSPoint (*topLeft)(NSRect r);
        NSPoint (*topRight)(NSRect r);
        NSPoint (*bottomLeft)(NSRect r);
        NSPoint (*bottomRight)(NSRect r);
    } MARectUtils;
```

For the implementation, we'll write these as normal, `static` functions, and then finally initialize the struct with them:

```
    static NSPoint topLeft(NSRect r)
    {
        return r.origin;
    }

    static NSPoint topRight(NSRect r)
    {
        return NSMakePoint(NSMaxX(r), NSMinY(r));
    }

    static NSPoint bottomLeft(NSRect r)
    {
        return NSMakePoint(NSMinX(r), NSMaxY(r));
    }

    static NSPoint bottomRight(NSRect r)
    {
        return NSMakePoint(NSMaxX(r), NSMaxY(r));
    }

    const struct MARectUtils MARectUtils = {
        .topLeft = topLeft,
        .topRight = topRight,
        .bottomLeft = bottomLeft,
        .bottomRight = bottomRight
    };
```

Code can call these functions like this:

```
    NSPoint corner = MARectUtils.bottomRight([self frame]);
```

Just like with constants, this provides nice grouping and categorization for these functions.

**Conclusion**  
Namespacing constants and functions in C is an unusual technique, and likely to frighten people who aren't comfortable seeing new things. However, I believe it could make code cleaner and easier to understand, and in any case is worth some consideration.

That wraps things up for today. Come back in two weeks for the next one. As always, Friday Q&A is driven by reader ideas, so if you have a topic that you would like to see covered here, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
