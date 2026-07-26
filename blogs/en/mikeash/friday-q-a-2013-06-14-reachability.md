---
title: 'Friday Q&A 2013-06-14: Reachability'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-06-14-reachability.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:06ad7e470af14de1'
translated: false
---

> 原文：[Friday Q&A 2013-06-14: Reachability](https://www.mikeash.com/pyblog/friday-qa-2013-06-14-reachability.html)　·　mikeash.com Friday Q&A

Posted at 2013-06-14 13:49 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2013-06-28: Anatomy of a Compiler Bug](https://www.mikeash.com/pyblog/friday-qa-2013-06-28-anatomy-of-a-compiler-bug.html)  
Previous article: [Friday Q&A 2013-05-31: C Quiz](https://www.mikeash.com/pyblog/friday-qa-2013-05-31-c-quiz.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [networking](https://www.mikeash.com/pyblog/?tag=networking) [reachability](https://www.mikeash.com/pyblog/?tag=reachability)

Friday Q&A 2013-06-14: Reachability

by [Mike Ash](https://www.mikeash.com/)

**Concept**  
Reachability allows your app to find out whether a remote server is potentially reachable. In short, it tells you whether or not the computer (or iDevice) has a network connection. It also keeps track of the status of the various network connections, and can notify you when they appear or disappear.

Imagine you start an iPhone app in a tunnel with no cell service. It tries to load data, but it fails. It gives you a weird error. You leave the tunnel, but the app is still showing the error. You tap the reload button, hoping that it was just the loss of signal that caused the problem, and it loads.

Now imagine the same scenario, but with an app that uses the reachability API. It notices that there is no internet connection, and doesn't try to load data in the first place. It instead displays an informative message about requiring internet access. Once you leave the tunnel and obtain a signal again, the app automatically loads its data without any intervention, and you go on to use the app.

The second scenario is a lot nicer, and doesn't take too much additional effort to add.

**Limitations**  
Network reachability isn't a panacea and cannot substitute for robust error handling in your networking code.

In particular, the reachability API only accounts for the local environment. If your computer is connected to a Wi-Fi access point, but that access point's internet connection is down, reachability will tell you that _yes_, you have a network connection. From its perspective, you do. Similarly, you may have a working internet connection, but the target server itself may be offline, or experiencing errors, or slow to respond. Again, reachability will just say _yes_, you have a connection.

Finally, any pattern where you check for permission and then execute a request is inherently subject to race conditions. Reachability may say that the network connection is up, but then network disconnects before your code makes the actual network request.

All of this is to say that your code must be _correct_ in the absence of reachability, but adopting reachability can greatly enhance usability.

**The API**  
The reachability API is located in the `SystemConfiguration` framework and is called `SCNetworkReachability`. It can be found in the documentation under that name. It's a CoreFoundation-like API, so you'll need to do some C.

The basic lifecycle when using the API is this:

1. Create a reachability object with a given remote host.
2. Set a callback so it can notify you when things change3
3. Schedule the reachability object on a runloop or dispatch queue.
4. If desired, query the reachability object directly.
5. When done, tear down the object.

**Creation**  
You create a reachability object using the `SCNetworkReachabilityCreateWithName` call. It takes a hostname in C string format. You can conveniently extract the hostname from a NSURL instance, or hardcode a string, or obtain a hostname any other way that makes sense:

```
    NSURL *url = ...;
    NSString *host = [url host];
    SCNetworkReachabilityRef reachabilityRef = SCNetworkReachabilityCreateWithName(NULL, [host UF8String]);
```

**Callback**  
You set a callback on the reachability object using `SCNetworkReachabilitySetCallback`. This takes a context structure and a C function. Since raw C functions are a little annoying to deal with when the rest of your code is Objective-C, I'll go ahead and write a quick trampoline function to bridge the call over to a block.

The C callback gets three parameters: the reachability object, the new reachability flags, and an info pointer. The reachability object is already accessible, and the info pointer will contain the block, so the block itself will just take the new reachability flags. Here's an example block:

```
    void (^callbackBlock)(SCNetworkReachabilityFlags) = ^(SCNetworkReachabilityFlags flags) {
        BOOL reachable = (flags & kSCNetworkReachabilityFlagsReachable) != 0;
        NSLog(@"The network is currently %@", reachable ? @"reachable" : @"unreachable");
    };
```

Next, set up a context structure. It has five fields, a `version`, which is always `0`, an `info` pointer, a `retain` and `release` call, and a `copyDescription` call. We'll only use `version`, `info`, and `release`. The `info` pointer will point to the block above, and the `release` call will just call `CFRelease` to release the block. The `CFBridgingRetain` call is used to get ARC to be happy with the type conversion, and to handle memory management correctly:

```
    SCNetworkReachabilityContext context = {
        .version = 0,
        .info = (void *)CFBridgingRetain(callbackBlock),
        .release = CFRelease
    };
```

For non-ARC code, the `info` line can simply be changed to copy the block:

```
        .info = [callbackBlock copy],
```

The actual callback function will just extract the block from `info` and call it:

```
    static void ReachabilityCallback(SCNetworkReachabilityRef reachabilityRef, SCNetworkReachabilityFlags flags, void *info)
    {
        void (^callbackBlock)(SCNEtworkReachabilityFlags) = (__bridge id)info;
        callbackBlock(flags);
    }
```

With everything in place, set the callback:

```
    SCNetworkReachabilitySetCallback(reachabilityRef, ReachabilityCallback, &context);
```

**Scheduling**  
In order to provide notifications, the reachability object must be scheduled on a runloop or dispatch queue. The callback will be invoked on the specified runloop or queue.

To receive callbacks in the main thread, just schedule the object on the main runloop:

```
    SCNetworkReachabilityScheduleWithRunLoop(reachabilityRef, CFRunLoopGetMain(), kCFRunLoopDefaultMode);
```

Or you can do the same thing with the main dispatch queue:

```
    SCNetworkReachabilitySetDispatchQueue(reachabilityRef, dispatch_queue_get_main());
```

If you don't want your callbacks tied to the main thread, you could instead pass in a custom dispatch queue or a global queue.

**Flags**  
When your callback is invoked, it will receive the new reachability flags. You can also query the flags at any time directly:

```
    SCNetworkReachabilityFlags flags = 0;
    bool success = SCNetworkReachabilityGetFlags(reachabilityRef, &flags);
    if(!success) // error getting flags!
```

There are quite a few potential flags. What do you look at?

The most useful one is the `kSCNetworkReachabilityFlagsReachable` flag. This flag is set when the destination appears to be reachable, which is usually what you're after.

There are a bunch of informative flags which can tell you about the nature of the reachability described, for example if a connection isn't currently present but will be initiated on demand. See the documentation for a full list and description.

One particularly pertinent flag for iOS development is the `kSCNetworkReachabilityFlagsIsWWAN` flag. This is set when the target is reachable over the device's cellular connection. You can use this flag to make informed decisions about what sort of data to download, to accommodate the typically slow and expensive nature of these connections.

Note that if you have traffic that absolutely must not be sent over the cellular connection, checking for `kSCNetworkReachabilityFlagsIsWWAN` is not 100% reliable. The system may think that the destination is reachable through other means, but then later lose that connection and try the cellular network instead. If you need to absolutely prevent this, you can use the `setAllowsCellularAccess:` method on `NSMutableURLRequest`.

**Cleanup**  
When done with a reachability object, first unschedule it from the runloop, or clear the dispatch queue:

```
    // runloop
    SCNetworkReachabilityUnscheduleFromRunLoop(reachabilityRef, CFRunLoopGetMain(), kCFRunLoopDefaultMode);

    // dispatch queue
    SCNetworkReachabilitySetDispatchQueue(reachabilityRef, NULL);
```

Finally, release the object:

```
    CFRelease(reachabilityRef);
```

That's it!

**Conclusion**  
The reachability API is a valuable tool for making a networked app easier and nicer to use. By checking reachability status when making a request, you can provide better error reporting to the user. By watching for reachability changes, you can automatically retry a network request once the user regains connectivity.

That wraps up today's article. Come back soon for the next exciting adventure. Until then, in case you hadn't already heard, Friday Q&A is driven by reader suggestions, so if you have a suggestion for a topic to cover, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
