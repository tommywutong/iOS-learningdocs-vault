---
title: 'Friday Q&A 2010-01-08: NSNotificationQueue'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-01-08-nsnotificationqueue.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:dc63e7cd3b735076'
translated: false
---

> 原文：[Friday Q&A 2010-01-08: NSNotificationQueue](https://www.mikeash.com/pyblog/friday-qa-2010-01-08-nsnotificationqueue.html)　·　mikeash.com Friday Q&A

Posted at 2010-01-08 07:21 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-01-15: Stack and Heap Objects in Objective-C](https://www.mikeash.com/pyblog/friday-qa-2010-01-15-stack-and-heap-objects-in-objective-c.html)  
Previous article: [Friday Q&A 2010-01-01: NSRunLoop Internals](https://www.mikeash.com/pyblog/friday-qa-2010-01-01-nsrunloop-internals.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [notifications](https://www.mikeash.com/pyblog/?tag=notifications)

Friday Q&A 2010-01-08: NSNotificationQueue

by [Mike Ash](https://www.mikeash.com/)

**Runloops**  
 `NSNotificationQueue` works in close concert with `NSRunLoop`. If you haven't already, it might be a good idea to read [my post from last week on NSRunLoop internals](https://www.mikeash.com/pyblog/friday-qa-2010-01-01-nsrunloop-internals.html).

**(No) Threading**  
 Many people, upon confronted with `NSNotificationQueue`, immediately think that it allows posting notifications across threads. (Well, I did, anyway.) In fact, `NSNotificationQueue` is completely unrelated to threads! Like `NSRunLoop`, there exists a single `NSNotificationQueue` per thread, and that per-thread instance can't be used from other threasd.

**So What _Is_ It?**  
 Simply put, the primary mission of `NSNotificationQueue` is to delay posting of a notification, and to allow coalescing of notifications.

**Delayed Notifications**  
 Sometimes you don't want to post a notification immediately. This is especially true if you want to coalesce multiple identical notifications; you can't do that unless you delay posting the first one. It can be useful for other scenarios as well, such as wanting to give calling code a chance to run before the notification's observers run. (In this respect, it's very similar to passing zero delay to `performSelector:withObject:afterDelay:` in order to have some code run at the next runloop cycle.)

`NSNotificationQueue` provides three posting styles for notifications:

```
    NSPostWhenIdle = 1,
    NSPostASAP = 2,
    NSPostNow = 3
```

Let's take them bottom to top.

`NSPostNow` is the easiest to understand. This has the same semantics as posting the notification directly to the `NSNotificationCenter`, in that the notification is posted immediately and observers are notified before control returns to the caller. The only reason to use this instead of `NSNotificationCenter` is because it can be used to coalesce previously enqueued notifications before posting.

`NSPostASAP` is much like a zero-delay timer. The notification is not posted immediately, but will be posted as soon as control returns to the runloop. The usage scenarios are much like for a zero-delay timer.

`NSPostWhenIdle` will wait until the runloop is idle, then post the notification. You can think of this as using a zero-delay timer with low priority. As long as the runloop has other work to do, the notification will not be posted. Once the runloop runs out of stuff to do, the notification will be posted. This is useful if you want to wait until your program has not only finished the currently executing code, but has nothing else to do. For example, imagine tracking mouse movement and performing an expensive update on the basis of that movement. Performing that update with every movement will make the program unresponsive, but you still want to update as often as possible within reason. Using `NSPostWhenIdle` will accomplish this. As long as more mouse movement events are pending, the notification will not be posted. If the user pauses for a moment, the runloop will clear out and the notification will be posted. If the user has a really fast computer, or the computation takes less time than expected, the runloop may have time to idle in between mouse moved events, and your update will then happen more frequently.

**Coalescing**  
 The real power of `NSNotificationQueue` is in coalescing. What does that mean?

When posting with `NSPostASAP` or `NSPostWhenIdle`, the notification is not posted immediately, but rather is queued. Coalescing means that if a notification is posted which matches one already in the queue, the two are merged, so that only a single notification is posted to observers.

This behavior can be really handy. Imagine a loop modifying a bunch of objects which posts notifications that cause other parts of the application to update their idea of the world. If they only need one notification at the end of all the modifications, coalescing will allow that other code to avoid a lot of needless computation that would occur if every modification caused a separate notification.

`NSNotificationQueue` provides three types of coalescing.

- `NSNotificationNoCoalescing` means that no coalescing is performed.
- `NSNotificationCoalescingOnName` means that coalescing is performed if two notifications share the same name.
- `NSNotificationCoalescingOnSender` means that coalescing is performed if two notifications share the same sender object.

These are bitwise flags, so you can combine them. Writing `NSNotificationCoalescingOnName | NSNotificationCoalescingOnSender` means that coalescing is performed if two notifications share both the same name and the same sender object. (Most of the time when coalescing, this is what you want, and it's what `-enqueueNotification:postingStyle:` implicitly uses.)

With coalescing, the semantics of `NSPostNow` make more sense. By using `NSPostNow` with `NSNotificationQueue`, any matching enqueued notifications will be coalesced with the one being posted before it's posted, essentially clearing them out and posting the coalesced notification earlier than would have otherwise happened.

These coalescing flags can also be used to remove notifications from the queue without posting them, using the `-dequeueNotificationsMatching:coalesceMask:` method.

**Examples**  
 `NSNotificationQueue` is pretty straightforward to use. Rather than standard code using `NSNotificationCenter`, you more or less drop in NSNotificationQueue. As a concrete example, imagine you have an `NSSlider` set to be "continuous", so that it sends its action message every time the mouse is moved, even while it's down:

```
    - (IBAction)sliderMoved: (id)sender
    {
        [self updateWithNewSliderValue: [sender doubleValue]];
```

But you also have some updates that you only want to run once the mouse has been released. Since the runloop is run in `NSEventTrackingRunLoopMode` while the mouse is down, you can just post a notification using `NSPostASAP` onto the `NSNotificationQueue`, and the notification will be posted only once the mouse is released. By coalescing, this code ensures that only one notification is posted when the mouse is released, even though this action message may be called many times:

```
        NSNotification *note = [NSNotification notificationWithName: SliderDoneMovingNotification object: self];
        [[NSNotificationQueue defaultQueue] enqueueNotification: note postingStyle: NSPostASAP];
```

Imagine that you also want to update a value while the slider is moving, but that this update is expensive to perform, so you want to keep the application responsive. Using `NSPostWhenIdle` and `NSEventTrackingRunLoopMode` will allow this:

```
        note = [NSNotification notificationWithName: ExpensiveSliderUpdate object: self];
        NSArray *modes = [NSArray arrayWithObject: NSEventTrackingRunLoopMode];
        [[NSNotificationQueue defaultQueue] enqueueNotification: note
                                                   postingStyle: NSPostWhenIdle
                                                   coalesceMask: NSNotificationCoalescingOnName | NSNotificationCoalescingOnSender
                                                   forModes: modes];
    }
```

To avoid a pending notification waiting around a long time if the mouse is immediately released after this code executes, you'll want to observe `SliderDoneMovingNotification` and remove `ExpensiveSliderUpdate` from the queue:

```
    - (void)sliderDoneMoving: (NSNotification *)note
    {
        NSNotification *note = [NSNotification notificationWithName: ExpensiveSliderUpdate object: self];
        [[NSNotificationQueue defaultQueue] dequeueNotificationsMatching: note
                                                            coalesceMask: NSNotificationCoalescingOnName | NSNotificationCoalescingOnSender];
    }
```

**Conclusion**  
`NSNotificationQueue` may not be well known in general, but now you know how it works, what it's good for, and have some ideas for how to put it to work.

That's it for this week. Come back next week for another exciting edition. (A warning: I'm going to be making a long trip not long before next Friday, and so there's some possibility that I'll miss next week's edition. In that event, my instructions to you, the reader, are to panic as thoroughly as possible until the following Friday.)

As always, Friday Q&A is driven by reader suggestions. If you have an idea for a topic to cover here, [please send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-01-08-nsnotificationqueue.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
