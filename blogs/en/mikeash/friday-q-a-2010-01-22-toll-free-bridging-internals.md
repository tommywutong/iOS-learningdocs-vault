---
title: 'Friday Q&A 2010-01-22: Toll Free Bridging Internals'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-01-22-toll-free-bridging-internals.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e6d8f95860645c7c'
translated: false
---

> 原文：[Friday Q&A 2010-01-22: Toll Free Bridging Internals](https://www.mikeash.com/pyblog/friday-qa-2010-01-22-toll-free-bridging-internals.html)　·　mikeash.com Friday Q&A

Posted at 2010-01-22 16:57 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-01-29: Method Replacement for Fun and Profit](https://www.mikeash.com/pyblog/friday-qa-2010-01-29-method-replacement-for-fun-and-profit.html)  
Previous article: [Friday Q&A 2010-01-15: Stack and Heap Objects in Objective-C](https://www.mikeash.com/pyblog/friday-qa-2010-01-15-stack-and-heap-objects-in-objective-c.html)  
Tags: [bridging](https://www.mikeash.com/pyblog/?tag=bridging) [corefoundation](https://www.mikeash.com/pyblog/?tag=corefoundation) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2010-01-22: Toll Free Bridging Internals

by [Mike Ash](https://www.mikeash.com/)

**What It Is**  
 I hope that everyone reading this already knows what toll-free bridging, but if you don't, here's a summary.

Toll-free bridging, or TFB for short, is a mechanism which allows certain Objective-C classes to be interchangeable with certain CoreFoundation classes. For example, `NSString` and `CFString` are bridged, which means that you can treat any `NSString` as if it were a `CFString` and vice versa. Example:

```
    CFStringRef cfStr = SomeFunctionThatReturnsCFString();
    NSUInteger length = [(NSString *)cfStr length];
    
    NSString *nsStr = [self someString];
    CFIndex length = CFStringGetLength((CFStringRef)nsStr);
```

Most (but not all!) classes which exist in both Cocoa and CoreFoundation are bridged in this way. A bridged class will mention the bridging in its documentation.

**Bridging From CF to ObjC**  
 The way that classes are bridged from CoreFoundation to Objective-C (how a `CFString` can act like an `NSString`) is fairly straightforward.

Every bridged class is actually a class cluster, which means that the public class is abstract, and core functionality is implemented in private subclasses. The CoreFoundation class is given a memory layout that matches one of these private subclasses, which is built just for the job of being the Objective-C counterpart to the CoreFoundation class. Other Objective-C classes may also exist independent of this. From the outside, they all look and work the same, because they all share the same interface.

To put it concretely, look at `NSString`. `NSString` is an abstract class. Every time you create one, you actually get an instance of one of its subclasses.

One of those subclasses is `NSCFString`. This is the direct counterpart to `CFString`. The first field of a `CFString` is an `isa` pointer which points to the `NSCFString` class, which allows it to function as an Objective-C object.

`NSCFString` implements methods to work properly as an `NSString`. There are two ways that it can do this. One way is to implement every method as a stub which just calls through to its CoreFoundation counterpart. Another way is to implement every method to match what its CoreFoundation counterpart does. In reality, the code is probably a mix of the two.

For this direction, the mechanism of bridging is so simple it's almost not there at all. `CFString` objects just happen to be instances of `NSCFString`, which is a subclass of `NSString`, and which implements the methods needed to act like one. Many of those implementations just happen to call through to CoreFoundation to get their work done.

**Bridging from ObjC to CF**  
 Bridging in the opposite direction gets a bit more complicated. This is because any given instance of a TFB Objective-C class could be an instance of any number of classes, even custom classes created within the application. Just write a subclass of `NSString` and you have such a custom class. And yet these custom classes still work transparently with CoreFoundation function calls. You can call `CFStringGetLength` on an instance of your custom `NSString` subclass and it will invoke your `-length` method and return the result to the caller.

As it turns out, there's no particular magic to make this work. It's just pure brute force. The implementation of `CFStringGetLength` looks like this:

```
    CFIndex CFStringGetLength(CFStringRef str) {
        CF_OBJC_FUNCDISPATCH0(__kCFStringTypeID, CFIndex, str, "length");
    
        __CFAssertIsString(str);
        return __CFStrLength(str);
    }
```

The first line is an ugly macro that hides the secret to how TFB works on this side of things. It checks the

of the object to see if it matches

. If it doesn't, then it's not a "real"

, but just some other Objective-C class. In that case, the CoreFoundation code doesn't know how to look up the length, so it just sends the

message to the object and returns the result. This is how custom subclasses work. If it

a "real"

, then it simply calls

which does the actual work of looking up the length of the string within the

structure, and returns that value.

In short: every CoreFoundation function for a TFB class first checks to see if the object being passed in is a "real" CoreFoundation object or a pure Objective-C class. If it's pure Objective-C, it simply calls through to the Objective-C side, and it's done. Otherwise, it proceeds normally. This is why I said it's pure brute force: every single function call has one of these checks at the top in order to make TFB work.

This implementation has an interesting consequence. Consider for a moment what would happen if you messed up and passed, say, a `CFArray` to `CFStringGetLength`. The `isa` check would show that it's not an `NSCFString`, so it would go for the Objective-C dispatch. The end result is that you get an error like this:

```
    -[NSCFArray length]: unrecognized selector sent to instance 0x100108e50
```

That's an Objective-C error coming from pure CoreFoundation code!

**Bridging Basic Behavior**  
 That's how classes which are explicitly bridged work. But there's one more interesting aspect to TFB: basic behaviors shared by all objects are also bridged for all classes. In essence, `NSObject` is bridged to `CFType`. As one of the most common examples, it's possible to `CFRetain` any Objective-C object, and `retain` any CoreFoundation object. Just like the other bridging, if you've overridden `retain` in your Objective-C code, `CFRetain` will call that override. This works not only for memory management, but for any `CFType` function, like `CFCopyDescription`, and for any `NSObject` method, like `performSelector:withObject:afterDelay:`.

For the bridging to Objective-C, the first field of any CoreFoundation object points to an Objective-C class. For bridged classes it points to the Objective-C counterpart class, and for non-bridged classes it points to a special `__NSCFType` class. All of these classes are subclasses of `NSObject` (most of them indirectly), so naturally they inherit all of their behavior. For methods which map to CoreFoundation counterparts, these classes simply override them and call through to the CoreFoundation side as necessary.

For bridging to CoreFoundation, the mechanism is just like the specific bridging. The first line of `CFRetain` and all the other `CFType` functions checks to see if the object is a "real" CoreFoundation object or if it's some random Objective-C class. If it's a "real" CF object, then it does its normal job. Otherwise, it dispatches through to Objective-C and lets that side of things handle all the work.

**Creating Bridged Classes**  
 I hope the title of this section didn't get anybody's hopes up, because the simple answer to this is: you can't. Now that we know how bridging works, it should be obvious why. You can't bridge an existing, unbridged CoreFoundation class because it requires massive cooperation on the CoreFoundation side. Every single function call needs to have a line at the top which checks the class of the object being passed in and dispatches to Objective-C if necessary, and you can't add that if it's not already there. And you can't create a new bridged CoreFoundation class because you can't create new CoreFoundation classes, period. That's capability that Apple keeps for itself, and doesn't expose to the outside world. (And really, would you want to pepper class checks into every function you write? Just write a pure Objective-C class, it's simpler and prettier.)

**Conclusion**  
 Now you know the basics of how toll-free bridging works. If you're interested in the deeper technical details of just what the dispatching code looks like and how it works, check out [ridiculous_fish's article on bridging](http://ridiculousfish.com/blog/archives/2006/09/09/bridge/).

That brings this week's edition to a close, but come back next week for yet another one. Friday Q&A is, of course, driven by user submissions. If you have an idea you would like to see covered in this space, [send it in](https://www.mikeash.com/pyblog/href)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
