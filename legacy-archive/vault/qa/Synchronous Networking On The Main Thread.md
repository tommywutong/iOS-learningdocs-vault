---
title: Synchronous Networking On The Main Thread
apple_id: DTS40010599
resource_type: QA
platform: iOS
topic: null
technology: null
published: '2010-12-23'
source_url: https://developer.apple.com/library/archive/qa/qa1693/_index.html
archived_at: '2026-07-27T06:57:02.096294Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1693

# Synchronous Networking On The Main Thread

## Q:  On iTunes Connect I see lots of crash reports saying that the app "failed to launch/suspend/resume/terminate in time", with the backtrace pointing to networking code. What's going on here?

A: On iTunes Connect I see lots of crash reports saying that the app "failed to launch/suspend/resume/terminate in time", with the backtrace pointing to networking code. What's going on here?

These are watchdog timeout crash reports, which you can recognise by the infamous "ate bad food" (`0x8badf00d`) exception code, as shown in Listing 1.

__Listing 1__  Watchdog timeout crash report

```
Exception Type: 00000020 Exception Codes: 0x8badf00d
```

The most common cause for watchdog timeout crashes in a network application is synchronous networking on the main thread. There are four contributing factors here:

1. synchronous networking — This is where you make a network request and block waiting for the response.
2. main thread — Synchronous networking is less than ideal in general, but it causes specific problems if you do it on the main thread. Remember that the main thread is responsible for running the user interface. If you block the main thread for any significant amount of time, the user interface becomes unacceptably unresponsive.
3. long timeouts — If the network just goes away (for example, the user is on a train which goes into a tunnel), any pending network request won't fail until some timeout has expired. Most network timeouts are measured in minutes, meaning that a blocked synchronous network request on the main thread can keep the user interface unresponsive for minutes at a time.

   Trying to avoid this problem by reducing the network timeout is not a good idea. In some situations it can take many seconds for a network request to succeed, and if you always time out early then you'll never make any progress at all.
4. watchdog — In order to keep the user interface responsive, iOS includes a watchdog mechanism. If your application fails to respond to certain user interface events (launch, suspend, resume, terminate) in time, the watchdog will kill your application and generate a watchdog timeout crash report. The amount of time the watchdog gives you is not formally documented, but it's always less than a network timeout.

One tricky aspect of this problem is that it's highly dependent on the network environment. If you always test your application in your office, where network connectivity is good, you'll never see this type of crash. However, once you start deploying your application to end users—who will run it in all sorts of network environments—crashes like this will become common.

__Warning:__ To summarize, if you make synchronous networking calls on the main thread, your application will suffer from watchdog timeout crashes when it's deployed to a wide range of users.

Given a watchdog timeout crash report, you can find the problematic code by looking at the backtrace of the main thread (thread 0). Listing 2 is a typical example.

__Listing 2__  Bad app, no biscuit

```
Thread 0: 0   libSystem.B.dylib 0x00001668 mach_msg_trap + 20 1   libSystem.B.dylib 0x00003734 mach_msg + 44 2   CoreFoundation    0x0002296e CFRunLoopRunSpecific + 1150 3   CoreFoundation    0x000224da CFRunLoopRunInMode + 42 4   CFNetwork         0x0002b118 CFURLConnectionSendSynchronousRequest + 244 5   Foundation        0x000a45a2 +[NSURLConnection sendSynchronousRequest:returningResponse[…] 6   MyBadApp          0x000063f6 0x1000 + 21494 7   MyBadApp          0x0000630a 0x1000 + 21258 8   MyBadApp          0x00006ada 0x1000 + 23258 9   MyBadApp          0x00003618 0x1000 + 9752 10  MyBadApp          0x0000351e 0x1000 + 9502 11  MyBadApp          0x00003874 0x1000 + 10356 12  UIKit             0x00068568 -[UIViewController viewWillMoveToWindow:] + 76 13  UIKit             0x0000988a -[UIView(Hierarchy) _willMoveToWindow:withAncestorView:] + 126 14  UIKit             0x00005e6e -[UIView(Internal) _addSubview:positioned:relativeTo:] + 222 15  UIKit             0x00005d80 -[UIView(Hierarchy) addSubview:] + 16 16  MyBadApp          0x000028d2 0x1000 + 6354 17  UIKit             0x00003e58 -[UIApplication _performInitializationWithURL:payload:] + 336 18  UIKit             0x00003b22 -[UIApplication _runWithURL:payload:launchOrientation:] + 394 19  UIKit             0x0004f8c4 -[UIApplication handleEvent:withNewEvent:] + 1336 20  UIKit             0x0004f242 -[UIApplication sendEvent:] + 38 21  UIKit             0x0004ec8c _UIApplicationHandleEvent + 4772 22  GraphicsServices  0x00003b2c PurpleEventCallback + 660 23  CoreFoundation    0x00022d96 CFRunLoopRunSpecific + 2214 24  CoreFoundation    0x000224da CFRunLoopRunInMode + 42 25  UIKit             0x0000340a -[UIApplication _run] + 342 26  UIKit             0x00001954 UIApplicationMain + 636 27  MyBadApp          0x00002828 0x1000 + 6184 28  MyBadApp          0x000027f8 0x1000 + 6136
```

Looking at frames 5 and 6, you can see that the application has made a synchronous networking call (`+[NSURLConnection sendSynchronousRequest:returningResponse:error:]`) which has blocked waiting for the network, thereby invoking the ire of the watchdog.

Once you've confirmed that this problem is related to your networking code, there are two common solutions:

- asynchronous networking — The best solution to this problem is to run your networking code asynchronously. Asynchronous networking code has a number of advantages, not least of which is that it lets you access the network safely without having to worry about threads.
- synchronous networking on a secondary thread — If it's prohibitively difficult to run your networking code asynchronously (perhaps you're working with a large portable code base that assumes synchronous networking), you can avoid the watchdog by running your synchronous code on a secondary thread.

There are numerous examples of how to run networking code asynchronously, including:

- [Sample Code 'SimpleURLConnections'](https://developer.apple.com/samplecode/SimpleURLConnections/index.html)
- [Sample Code 'SimpleFTPSample'](https://developer.apple.com/samplecode/SimpleFTPSample/index.html)
- [Sample Code 'SimpleNetworkStreams'](https://developer.apple.com/samplecode/SimpleNetworkStreams/index.html)
- [Sample Code 'SeismicXML'](https://developer.apple.com/samplecode/SeismicXML/index.html)
- [Sample Code 'LinkedImageFetcher'](https://developer.apple.com/samplecode/LinkedImageFetcher/index.html)

In addition, the following resources illustrate one nice technique for managing asynchronous networking, namely, using NSOperation to encapsulate each network request:

- [Technical Note TN2109, 'Simple and Reliable Threading with NSOperation'](https://developer.apple.com/technotes/tn2009/tn2109.html)
- [Sample Code 'ListAdder'](https://developer.apple.com/samplecode/ListAdder/index.html)
- [Sample Code 'MVCNetworking'](https://developer.apple.com/samplecode/MVCNetworking/index.html)

Finally, it's important to realize that synchronous networking can be hidden behind abstraction layers that mask the danger. For example, if you call `-[NSXMLParser -initWithContentsOfURL:]` with an "http" or "https" URL, NSXMLParser will download the contents of that URL synchronously. That's mighty convenient, but if you do it on the main thread you run the risk of being killed by the watchdog. A better option is to download the contents of the URL to a file asynchronously, and then call `-[NSXMLParser -initWithContentsOfURL:]` with a "file" URL. The same applies to numerous other "WithContentsOfURL" routines, like `+[NSString stringWithContentsOfURL:encoding:error:]`, `-[NSDictionary initWithContentsOfURL:]`, and so on.

Other common examples of hidden synchronous networking include:

- BSD DNS APIs — Traditional BSD DNS routines, like `gethostbyname` and `gethostbyaddr`, are never safe to call on the main thread. More modern routines like `getnameinfo` and `getaddrinfo` are only safe if you are working exclusively with IP addresses and not DNS names (that is, you specify `AI_NUMERICHOST` and `NI_NUMERICHOST`, respectively). If you must resolve a DNS address manually, use an asynchronous API like CFHost or `<dns_sd.h>`. Better yet, if you plan to connect to a server by name, use an asynchronous API that resolves and connects in one hit (see [Technical Q&A QA1652, 'Using NSStreams For A TCP Connection Without NSHost'](https://developer.apple.com/qa/qa2009/qa1652.html) for an example of this).
- reachability — The System Configuration framework reachability API (`<SystemConfiguration/SCNetworkReachability.h>`) operates synchronously by default. Thus, seemingly innocuous routines like `SCNetworkReachabilityGetFlags` can get you killed by the watchdog. If you're using the reachability API, you should use it asynchronously. This involves using the `SCNetworkReachabilityScheduleWithRunLoop` routine to schedule your reachability queries on the run loop. [Sample Code 'Reachability'](https://developer.apple.com/samplecode/Reachability/index.html) shows an example of this.

For more information about this problem and its solutions, and a high-level introduction to networking on iOS in general, you can [watch](https://developer.apple.com/videos/wwdc/2010/) WWDC 2010 presentation, "Network Apps for iPhone OS", part 1 and 2 (sessions 207 and 208).

For more information on iOS crash reports in general, see [Technical Note TN2151, 'Understanding and Analyzing iPhone OS Application Crash Reports'](https://developer.apple.com/technotes/tn2008/tn2151.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-12-23 | New document that describes the perils of doing synchronous networking on the main thread. |
