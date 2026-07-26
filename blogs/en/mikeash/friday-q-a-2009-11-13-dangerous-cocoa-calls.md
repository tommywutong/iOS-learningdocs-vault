---
title: 'Friday Q&A 2009-11-13: Dangerous Cocoa Calls'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-11-13-dangerous-cocoa-calls.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d15c4393926bb459'
translated: false
---

> 原文：[Friday Q&A 2009-11-13: Dangerous Cocoa Calls](https://www.mikeash.com/pyblog/friday-qa-2009-11-13-dangerous-cocoa-calls.html)　·　mikeash.com Friday Q&A

Posted at 2009-11-13 20:38 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Deconstructing Apple's Copyright and Trademark Guidelines](https://www.mikeash.com/pyblog/deconstructing-apples-copyright-and-trademark-guidelines.html)  
Previous article: [Friday Q&A 2009-11-06: Linking and Install Names](https://www.mikeash.com/pyblog/friday-qa-2009-11-06-linking-and-install-names.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [dangerous](https://www.mikeash.com/pyblog/?tag=dangerous) [threading](https://www.mikeash.com/pyblog/?tag=threading)

Friday Q&A 2009-11-13: Dangerous Cocoa Calls

by [Mike Ash](https://www.mikeash.com/)

First, let me clarify what I mean by a dangerous call. I don't mean something that is obviously dangerous, like `-[NSFileManager removeFileAtPath:handler:]`. That call is dangerous because you could use it to wipe the user's entire hard drive, but it's not interesting, because it's obvious that it can do this. Instead, I'm going to cover calls which are _subtly_ dangerous, things which you might easily use in an innocent manner, only to discover later that bad things can occur.

Without further ado, here are my dangerous calls:

**`-[NSTask launch]`**  
 This call is dangerous because it throws exceptions when it fails, and it can fail for completely mundane problems, like trying to execute a file that doesn't have the executable bit set. Because the Cocoa tradition is to only throw exceptions for programmer errors, this can cause trouble for the unwary programmer who doesn't wrap this in a `@try` block.

**`-[NSTask waitUntilExit]`**  
 This one looks tremendously innocent. The problem is that, if the task is still running, it will run the runloop to wait for the task to exit. Even that would not be a problem, except that _it runs the runloop in the default mode_. Because of this, all timers, callbacks, etc., that are installed in the default mode will continue to run, but will be running in a context they did not expect. This call looks like a simple blocking call, but it can potentially lead to the invocation of random timers or other callbacks. This in turn can easily lead to deadlocks or data corruption.

**`+[NSTimer scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:]`**  
 This returns a timer whose memory management is difficult to get right. Many people simply stash the return value in an instance variable. This is legitimate, because the runloop is documented to retain the timer. However, the runloop will release it as soon as it's invalidated, which will happen once a non-repeating timer fires, and also upon explicit invalidation. It's easy to get this wrong and end up with a dangling reference, and a lot of code has this problem. To make things even more fun, the timer retains its target, so if you retain the timer, you're likely to set up a retain cycle.

**`NSHost`**  
 Yes, this entire class is dangerous, and should not be used. Why? It's an unfortunate confluence of two otherwise unrelated properties of the class.

The first property is that `NSHost` has a blocking API. It accesses network resources, and as such any call to it can take an indefinite amount of time. This is fine by itself.

The second property is that `NSHost` returns shared objects, but `NSHost` is not thread safe. This means that [it can only be safely used on the main thread](https://www.mikeash.com/pyblog/friday-qa-2009-01-09.html).

Put the two together, and you have a class which can block any time you use it, but which can only be used on the main thread. Since it's unacceptable to indefinitely block the main thread of an application, this basically means that you can't use `NSHost`.

**`NSBundle`**  
 This one has half of the problems of `NSHost`. `NSBundle` returns shared objects, but is not thread safe, so it's main-thread only. It's still safe to use from the main thread. The reason I mark it as dangerous is because the fact that it's unsafe to use from secondary threads is not really documented, but rather has to be inferred from the fact that it's not thread safe and the fact that the instances are shared, and it can be tempting to use it from other threads.

**`-[NSBundle unload]`**  
 Because it's very easy to make references to memory within a bundle's code (e.g. by creating instances of an Objective-C class defined within the bundle, or by referring to literal strings defined within the bundle), and extremely difficult to make sure that all such references are gone, it's generally not safe to unload code on Mac OS X. If any such dangling references remain, your application will crash.

**`-[NSImage imageNamed:]`, followed by mutation**  
 This call is very convenient, but it returns a shared object. A lot of code will make this call, and then immediately start resizing or drawing into the object that it returns. This can mess up the shared image for any other code that uses it. If you're going to modify the image, then you need to copy it first, but this isn't immediately obvious.

**`-[NSDate timeIntervalSinceReferenceDate]` used for elapsed time**  
 How many of you have written code like this?

```
    BOOL success;
    NSTimeInterval start = [NSDate timeIntervalSinceReferenceDate];
    do
        success = [self trySomething];
    while(!success && [NSDate timeIntervalSinceReferenceDate] - start <= kTimeoutInterval);
```

I'm guilty of it myself. It's a pretty natural way to write a timeout loop. There are many other circumstances where you might use this sort of thing too, not with an explicit loop, but in something more asynchronous.

So what's the problem? `-timeIntervalSinceReferenceDate` uses the system clock, _which can be changed!_ Imagine that your program enters this loop, but before it can exit it, the system clock is set back by a day. Your timeout has now gone up to a day! Or imagine the opposite, that the system clock is suddenly set forward. Your timeout will suddenly become zero.

Mac OS X tries to make time adjustments smooth. For example, if the NTP client discovers that your clock is a few seconds out of whack, it will gradually pull it back in rather than making the adjustment all at once. However, sudden adjustments are still possible, even if rare, and your code should be robust against them. Even the gradual adjustments will cause your timeouts to change duration, albeit not by a huge amount.

The bad news is that Cocoa doesn't make it easy to do this right. You want to use a consistent, non-adjustable for elapsed time, but Cocoa has no APIs for such a thing. The OS does, so you just have to drop down a level.

My preferred API for this task is `mach_absolute_time`. However, this returns a value that's in terms of arbitrary timebase units, not something comfortable like seconds or nanoseconds. It's not hard to convert, but requires some work. Apple has [two examples of how to convert the return value into something sensible](http://developer.apple.com/mac/library/qa/qa2004/qa1398.html).

Two other reasonable alternatives are the Carbon calls `Microseconds` and `UpTime`.

**Distributed Objects**  
 I've [said it before](https://www.mikeash.com/pyblog/friday-qa-2009-02-20-the-good-and-bad-of-distributed-objects.html), but Distributed Objects need special care and attention. The trouble is that DO looks like a completely transparent way to access objects in other processes, but it doesn't entirely succeed at this. It can still be a good way to do IPC, but it requires more care than you might think from reading through the documentation on it. For details on why that's so, [my original post on the subject](https://www.mikeash.com/pyblog/friday-qa-2009-02-20-the-good-and-bad-of-distributed-objects.html) covers it all.

**Conclusion**  
 No, that's not a dangerous Cocoa call, it just means that we're done for the week. Come back in seven days for another exciting edition. In the meanwhile, [keep those topic suggestions flowing](mailto:mike@mikeash.com). Friday Q&A is driven by your ideas, so if you'd like to see a topic covered here, let me know.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
