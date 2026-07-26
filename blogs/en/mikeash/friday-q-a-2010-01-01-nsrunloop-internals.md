---
title: 'Friday Q&A 2010-01-01: NSRunLoop Internals'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-01-01-nsrunloop-internals.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d2940c3a0a7f6b16'
translated: false
---

> 原文：[Friday Q&A 2010-01-01: NSRunLoop Internals](https://www.mikeash.com/pyblog/friday-qa-2010-01-01-nsrunloop-internals.html)　·　mikeash.com Friday Q&A

Posted at 2010-01-01 10:43 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-01-08: NSNotificationQueue](https://www.mikeash.com/pyblog/friday-qa-2010-01-08-nsnotificationqueue.html)  
Previous article: [Friday Q&A 2009-12-18: Highlights From a Year of Friday Q&A](https://www.mikeash.com/pyblog/friday-qa-2009-12-18-highlights-from-a-year-of-friday-qa.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [runloop](https://www.mikeash.com/pyblog/?tag=runloop)

Friday Q&A 2010-01-01: NSRunLoop Internals

by [Mike Ash](https://www.mikeash.com/)

If you want to understand something as thoroughly as possible, you should build one yourself. That's a little too much for a blog post, so rather than build a complete implementation of `NSRunLoop`, I'm going to take the second-best route and plan out the key features of its internals in pseudocode.

**CoreFoundation**  
 On the Mac, `NSRunLoop` sits on top of its CoreFoundation equivalent, `CFRunLoop`. Most of the smarts are there, and the Cocoa side of things is mostly a wrapper. For this discussion, I am going to ignore this layering, and examine `NSRunLoop` as a single, standalone entity. From this perspective, `CFRunLoop` can be considered to be an implementation detail.

**Autorelease Pools**  
 One of the basic things that `NSRunLoop` does in manage autorelease pools, both for itself and for any code that it calls. Since autorelease pools are fairly straightforward compared to the rest, and will just serve to clutter things up, I will ignore this aspect of `NSRunLoop`'s functionality.

**Fundamentals**  
 Most of the mysteriousness in `NSRunLoop` is in its various `run` methods. What goes on in there? How does it all work?

The `-run` method is pretty simple, since the documentation describes it in terms of `-runMode:beforeDate:`:

If no input sources or timers are attached to the run loop, this method exits immediately; otherwise, it runs the receiver in the NSDefaultRunLoopMode by repeatedly invoking runMode:beforeDate:.

Its implementation must therefore look something pretty close to:

```
    - (void)run
    {
        while([self hasSourcesOrTimers])
            [self runMode: NSDefaultRunLoopMode beforeDate: [NSDate distantFuture]];
    }
```

The `-runUntilDate:` method is similar:

If no input sources or timers are attached to the run loop, this method exits immediately; otherwise, it runs the receiver in the NSDefaultRunLoopMode by repeatedly invoking runMode:beforeDate: until the specified expiration date.

Its implementation would then be like this:

```
    - (void)runUntilDate: (NSDate *)limitDate
    {
        while([self hasSourcesOrTimers])
        {
            [self runMode: NSDefaultRunLoopMode beforeDate: limitDate];
            
            // check limitDate at the end of the loop to ensure that
            // the runloop always runs at least once
            if([limitDate timeIntervalSinceNow] < 0)
                break;
        }
    }
```

That was easy enough. How about `-runMode:beforeDate:`, then? Well, that's where all the complication lies.

**Input Sources**  
 As described in [Apple's Run Loops programming guide](http://developer.apple.com/mac/library/documentation/Cocoa/Conceptual/Multithreading/RunLoopManagement/RunLoopManagement.html), a run loop contains two types of sources: inputs and timers. An input source is basically some kind of external signal from outside the runloop itself.

In Mac OS X, input sources are mach ports. While things like NSFileHandle and CFFileDescriptor may give the appearance of connecting non-mach-port things into the runloop, this is actually fake! They monitor their file descriptor sources on a dedicated thread, then signal back to the runloop over a mach port.

(This may have changed in 10.6, which now has APIs which are capable of monitoring both mach ports and file descriptors at the same time. However, the fundamental fact remains that mach ports are the major input source used on OS X.)

Most people's eyes glaze over when they hear about mach ports. They're not very well known, nor well documented. And personally, I don't know them all that well myself. Because of this, I'm going to explore an alternate `NSRunLoop` which uses file descriptors as its input sources instead. The fundamentals are the same, and file descriptors are more readily understandable to most people.

Quick refresher: what is a file descriptor, or FD for short? An FD is an object (not in the Objective-C sense, but in the conceptual sense) which you can either read from, write to, or both read and write. An FD can have data available for reading, space available for writing, or neither. This particular state of an FD can change over time. For example, imagine an FD which represents a socket communicating with another application. When that other application writes to the socket, the FD in your application will have data available for reading. If that FD is an input source for a run loop, that run loop will wake up and process that source. Likewise, if the other application reads from the socket, the FD in your application will have space available for writing, and this will also wake up the run loop and process that source. This is one of the fundamental tasks of a run loop.

A run loop needs to monitor multiple input sources at a time. There are several APIs for doing this on OS X, but the one I'm going to use here is `select(2)`.

I won't go into details on how to use `select` (pseudocode, remember?), but the basics are pretty easy: you give it three sets of FDs, which you want to monitor for reading, writing, and errors. It then returns whenever there's activity, and the three sets contain those FDs which have had that sort of activity on them.

Thus, we can see the first pass at how `-runMode:beforeDate:` would work. I'm going to simplify things a bit further and ignore the fact that `select` takes three different sets of FDs, and just use one. The idea is just that we're interested in activity on these input sources.

And remember, I'm doing pseudocode, so don't expect this to look 100% like real Objective-C.

The first thing is to check if there are any sources. According to the documentation, this method immediately returns `NO` if not:

```
    - (BOOL)runMode: (NSString *)mode beforeDate: (NSDate *)limitDate
    {
        if(![self hasSourcesOrTimers])
            return NO;
```

Next, create an empty FD set:

```
        fd_set fdset;
        FD_ZERO(&fdset);
```

Then, set each input source's FD within the set. I assume that the input source class has a `-fileDescriptor` method that returns the FD it wants to monitor:

```
        for(inputSource in [self inputSources])
            FD_SET([inputSource fileDescriptor], &fdset);
```

Now call `select`. Remember, to simplify, I'm pretending that it only takes one file descriptor set rather than three. I'm also ignoring all error checking:

```
        select(fdset, NULL);
```

Once it returns, check each input source to see if it's ready for processing now. I iterate over a copy of the input sources because the code that the input source executes may modify the set of input sources:

```
        for(inputSource in [[[self inputSources] copy] autorelease])
            if(FD_ISSET([inputSource fileDescrptor], &fdset))
                [inputSource fileDescriptorIsReady];
```

The documentation states that this method returns `YES` the runloop was run in any way, so that's the last thing to do here:

```
        return YES;
    }
```

**Modes**  
 So far so good, but it has a way to go. This method completely ignores its parameters! First, we'll look at the `mode` parameter.

Just what is the `mode` parameter, anyway? A mode is essentially a grouping of input and timer sources. Different sources are active in different modes. `NSRunLoop` has `NSDefaultRunLoopMode`, which as the name would expect is where most sources are added. In Cocoa, you also have secondary modes like `NSEventTrackingRunLoopMode`, which is used when the mouse is held down on a control. By switching to this mode, sources which were only added to the default mode will not fire, which prevents unwanted code from running while the user is in the middle of making a menu selection or moving a slider. Sources which need to fire during event tracking can be added to that mode. Sources which need to fire in both circumstances can be added to both.

You can then imagine `NSRunLoop` containing an instance variable for input sources like this:

```
    NSMutableDictionary *_inputSources; // maps modes to NSMutableSets
```

`NSRunLoop`'s method to add an input source is called `-addPort:forMode:`, and its implementation would then look like this:

```
    - (void)addPort: (NSPort *)aPort forMode: (NSString *)mode
    {
        NSMutableSet *sourcesSet = [_inputSources objectForKey: mode];
        if(!sourcesSet)
        {
            // this is the first time anything has used this mode
            // so create a new set for it
            sourcesSet = [NSMutableSet set];
            [_inputSources setObject: sourcesSet forKey: mode];
        }
        [sourcesSet addObject: aPort];
    }
```

Similarly for the removal method:

```
    - (void)removePort: (NSPort *)aPort forMode: (NSString *)mode
    {
        NSMutableSet *sourcesSet = [_inputSources objectForKey: mode];
        [sourcesSet removeObject: aPort];
        
        // this isn't strictly necessary, but keeps us from leaking
        // sets if the caller uses a lot of one-time "throwaway" modes
        // (which it probably never would)
        if(![sourcesSet count])
            [_inputSources removeObjectForKey: mode];
    }
```

And then the run method needs to be changed to match:

```
    - (BOOL)runMode: (NSString *)mode beforeDate: (NSDate *)limitDate
    {
        if(![self hasSourcesOrTimersForMode: mode])
            return NO;
        
        fd_set fdset;
        FD_ZERO(&fdset);
        
        for(inputSource in [_inputSources objectForKey: mode])
            FD_SET([inputSource fileDescriptor], &fdset);
        
        select(fdset, NULL);
        
        for(inputSource in [[[_inputSources objectForKey: mode] copy] autorelease])
            if(FD_ISSET([inputSource fileDescrptor], &fdset))
                [inputSource fileDescriptorIsReady];
        
        return YES;
    }
```

**Timeout**  
 This code still ignores one parameter, `limitDate`. The purpose of this parameter is to force the method to return even if no input sources were ready. It functions as a timeout. To make this work, the code simply computes the timeout and passes it as the last parameter to `select` (which in reality requires a more complicated timeout structure, not just an `NSTimeInterval`, but remember, pseudocode!):

```
     - (BOOL)runMode: (NSString *)mode beforeDate: (NSDate *)limitDate
    {
        if(![self hasSourcesOrTimersForMode: mode])
            return NO;
        
        fd_set fdset;
        FD_ZERO(&fdset);
        
        for(inputSource in [_inputSources objectForKey: mode])
            FD_SET([inputSource fileDescriptor], &fdset);
        
        NSTimeInterval timeout = [limitDate timeIntervalSinceNow];
        select(fdset, timeout);
        
        // if the timeout was hit, there may not be
        // any active input sources, but this loop
        // will simply do nothing if that's the case
        for(inputSource in [[[_inputSources objectForKey: mode] copy] autorelease])
            if(FD_ISSET([inputSource fileDescrptor], &fdset))
                [inputSource fileDescriptorIsReady];
        
        return YES;
    }
```

**Timer Sources**  
 This implementation deals with input sources and the timeout parameter well enough, but completely ignores timers.

As with input sources, I'll assume an instance variable which holds timers. And like input sources, timers are grouped into modes:

```
    NSMutableDictionary *_timerSources; // maps modes to NSMutableSets
```

I'll skip over the implementation of `-addTimer:forMode:`, as it should be pretty obvious and is basically identical to `-addPort:forMode:`.

Adding timer support to the above code is relatively straightforward. The list of timers can be consulted to find the one that fires earliest. If that time is earlier than `limitDate`, then it gets to be the timeout instead of `limitDate`. After `select` runs, check the list of timers to see if any of them are ready to fire, and fire the ones that are.

There's one wrinkle, which is that a timer firing does _not_ make `-runMode:beforeDate:` return. If a timer fires, it should be processed, and then control should return back to `select`. This continues until an input source fires. If an input source does fire, the method still needs to check the list of timers and fire any that are ready, because otherwise a busy input source could prevent timers from ever running.

Given all of that, here's what the code looks like with timer support:

```
     - (BOOL)runMode: (NSString *)mode beforeDate: (NSDate *)limitDate
    {
        if(![self hasSourcesOrTimersForMode: mode])
            return NO;
        
        // with timer support, this code has to loop until an input
        // source fires
        BOOL didFireInputSource = NO;
        while(!didFireInputSource)
        {
            fd_set fdset;
            FD_ZERO(&fdset);
            
            for(inputSource in [_inputSources objectForKey: mode])
                FD_SET([inputSource fileDescriptor], &fdset);
            
            // the timeout needs to be set from the limitDate
            // and from the list of timers
            // start with the limitDate
            NSTimeInterval timeout = [limitDate timeIntervalSinceNow];
            
            // now run through the list of timers and set the
            // timeout to the smallest one found in them and
            // in the limitDate
            for(timer in [_timerSources objectForKey: mode])
                timeout = MIN(timeout, [[timer fireDate] timeIntervalSinceNow]);
            
            // now run select
            select(fdset, timeout);
            
            // process input sources first (this choice is arbitrary)
            for(inputSource in [[[_inputSources objectForKey: mode] copy] autorelease])
                if(FD_ISSET([inputSource fileDescrptor], &fdset))
                {
                    didFireInputSource = YES;
                    [inputSource fileDescriptorIsReady];
                }
            
            // now process timers
            // responsibility for updating fireDate for repeating timers
            // and for removing the timer from the runloop for non-repeating timers
            // rests in the timer class, not in the runloop
            for(timer in [[[_timerSources objectForKey: mode] copy] autorelease])
                if([[timer fireDate] timeIntervalSinceNow] <= 0)
                    [timer fire];
            
            // see if we timed out, if so, abort!
            // this is checked at the end to ensure that timers and inputs are
            // always processed at least once before returning
            if([limitDate timeIntervalSinceNow] < 0)
                break;
        }
        return YES;
    }
```

And that covers all of the necessary functionality. The final code is pretty straightforward and understandable.

**Conclusion**  
 What does this exercise tell us? We have to be careful not to take _too_ much away from this pseudocode, as there's no guarantee that it matches Apple's. In fact, I know of one case that recently bit me where it does not: Apple's implementation will only fire _one_ pending timer for each pass through the run loop, even if multiple timers are ready to fire, whereas this code will fire all pending timers once before returning. And of course there's the major difference that Apple's code uses mach ports, not file descriptors, although their semantics are similar.

Despite this problem, a lot can be learned from this sort of exercise. For example, run loop modes are a common point of confusion among Cocoa programmers, and writing all of this stuff out helps to make it clear just what a mode is and how it works.

It can also inform speculation about the implementation of other parts of Cocoa. For example, we can deduce how the `-performSelector:withObject:afterDelay:` method works on the inside. Since a run loop only handles sources and timers, it must use one of those two. Since it activates after a delay, it must use a timer. Watching how it behaves in the debugger will confirm this to be correct. As another example, we can conclude that `-performSelectorOnMainThread:withObject:waitUntilDone:` must use a mach port, since it can't manipulate a timer on the main thread from a secondary thread. (`NSRunLoop` is not thread safe.)

All in all, this kind of technique is really useful in general. I don't usually take it as far as writing out detailed pseudocode like this, but thinking about _how_ some Apple code might be implemented can really help further understanding of how it works and what the documentation says, as well as what it implies but does not say directly. You have to be careful to ensure that your conclusions are ultimately based on documentation and real-world constraints, and not the peculiarities of your particular idea of how it might work, but that just takes a bit of care.

It's also helpful just to demystify a class. It's easy to get into magical thinking, where you see a class as being incomprehensible and elevated above the mortal plane. The fact is, while the particular implementations of some of these classes can be pretty sophisticated (the `CFRunLoop` source will make your eyes bleed), the basics of what they do and how they do it are usually very straightforward. For 99.9% of the APIs in Cocoa, they aren't there because they're doing something amazing that you could never achieve, but rather they simply exist to save you the time and trouble of having to write it all yourself.

That's it for this week. Check back in seven days for another exciting edition. Until then, [keep sending in your ideas for topics](mailto:mike@mikeash.com). Friday Q&A is reader-driven, and the more topic ideas I get, the better this series will become.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-01-01-nsrunloop-internals.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
