---
title: RunApplicationEventLoop and Thread Manager
apple_id: DTS10001613
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-10-10'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1061.html
archived_at: '2026-07-18T02:38:06.256738Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Process Management](https://developer.apple.com/referencelibrary/Carbon/idxProcessManagement-date.html)

|  |
| --- |
| Technical Q&A QA1061RunApplicationEventLoop and Thread Manager |

|  |  |  |
| --- | --- | --- |
| ---   Q: I want to change my Carbon application to use `RunApplicationEventLoop`. My application uses cooperative (Thead Manager) threads and there's no obvious place to call `YieldToAnyThread` (r. 2729795). Should I use a Carbon timer to yield to my cooperative threads?  A: No. Using a timer is not the best solution because it limits the amount of processing that your cooperative threads can do. The right thing to do depends on whether your threads are compute-bound or I/O-bound. I'll explain each case in turn.  For compute-bound cooperative threads the simplest thing to do is to write your own equivalent of `RunApplicationEventLoop` that includes a call to `YieldToAnyThread`. The core code for `RunApplicationEventLoop` is shown in Listing 3-10 of [Inside Carbon: Handling Carbon Events](https://developer.apple.com/documentation/Carbon/pdf/HandlingCarbEvents.pdf). I've included a version of this code in Listing 1. The `EventLoopEventHandler` routine is the actual event loop code. The remainder of Listing 1 implements a trick to ensure that the standard handlers are installed while `EventLoopEventHandler` executes; see the comments in the code for an explanation of what it does and why.     |  | | --- | | ``` extern SInt32 gNumberOfRunningThreads;     // This variable must be maintained by your thread scheduling     // code to accurately reflect the number of threads that are     // ready and need time for computation.  static EventHandlerUPP gQuitEventHandlerUPP;   // -> QuitEventHandler  static pascal OSStatus QuitEventHandler(EventHandlerCallRef inHandlerCallRef,                                         EventRef inEvent, void *inUserData)     // This event handler is used to override the kEventClassApplication/     // kEventAppQuit event while inside our event loop (EventLoopEventHandler).     // It simply calls through to the next handler and, if that handler returns     // noErr (indicating that the application is doing to quit), it sets     // a Boolean to tell our event loop to quit as well. {     OSStatus err;      MoreAssertQ(inUserData != nil);      MoreAssertQ( GetEventClass( inEvent ) == kEventClassApplication );     MoreAssertQ( GetEventKind ( inEvent ) == kEventAppQuit );      err = CallNextEventHandler(inHandlerCallRef, inEvent);     if (err == noErr) {         *((Boolean *) inUserData) = true;     }      return err; }  static EventHandlerUPP gEventLoopEventHandlerUPP;   // -> EventLoopEventHandler  static pascal OSStatus EventLoopEventHandler(EventHandlerCallRef inHandlerCallRef,                                              EventRef inEvent, void *inUserData)     // This code contains the standard Carbon event dispatch loop,     // as per "Inside Macintosh: Handling Carbon Events", Listing 3-10,     // except:     //     // o this loop supports yielding to cooperative threads based on the     //   application maintaining the gNumberOfRunningThreads global     //   variable, and     //     // o it also works around a problem with the Inside Macintosh code     //   which unexpectedly quits when run on traditional Mac OS 9.     //     // See RunApplicationEventLoopWithCooperativeThreadSupport for     // an explanation of why this is inside a Carbon event handler.     //     // The code in Inside Mac has a problem in that it quits the     // event loop when ReceiveNextEvent returns an error.  This is     // wrong because ReceiveNextEvent can return eventLoopQuitErr     // when you call WakeUpProcess on traditional Mac OS.  So, rather     // than relying on an error from ReceiveNextEvent, this routine tracks     // whether the application is really quitting by installing a     // customer handler for the kEventClassApplication/kEventAppQuit     // Carbon event.  All the custom handler does is call through     // to the previous handler and, if it returns noErr (which indicates     // the application is quitting, it sets quitNow so that our event     // loop quits.     //     // Note that this approach continues to support QuitApplicationEventLoop,     // which is a simple wrapper that just posts a kEventClassApplication/     // kEventAppQuit event to the event loop. {     OSStatus        err;     OSStatus        junk;     EventHandlerRef installedHandler;     EventTargetRef  theTarget;     EventRef        theEvent;     EventTimeout    timeToWaitForEvent;     Boolean         quitNow;     static const EventTypeSpec eventSpec = {kEventClassApplication, kEventAppQuit};      quitNow = false;      MoreAssertQ(gQuitEventHandlerUPP != nil);      // Install our override on the kEventClassApplication, kEventAppQuit event.      err = InstallEventHandler(GetApplicationEventTarget(), gQuitEventHandlerUPP,                               1, &eventSpec, &quitNow, &installedHandler);     if (err == noErr) {          // Run our event loop until quitNow is set.          theTarget = GetEventDispatcherTarget();         do {             if (gNumberOfRunningThreads == 0) {                 timeToWaitForEvent = kEventDurationForever;             } else {                 timeToWaitForEvent = kEventDurationNoWait;             }             err = ReceiveNextEvent(0, NULL, timeToWaitForEvent,                                    true, &theEvent);             if (err == noErr) {                 (void) SendEventToEventTarget(theEvent, theTarget);                 ReleaseEvent(theEvent);             }             if (gNumberOfRunningThreads > 0) {                 (void) YieldToAnyThread();             }         } while ( ! quitNow );          // Clean up.          junk = RemoveEventHandler(installedHandler);         MoreAssertQ(junk == noErr);     }      // So we can tell when our event loop quit.      SysBeep(10);      return err; }  static void RunApplicationEventLoopWithCooperativeThreadSupport(void)     // A reimplementation of RunApplicationEventLoop that supports     // yielding time to cooperative threads.  It relies on the     // rest of your application to maintain a global variable,     // gNumberOfRunningThreads, that reflects the number of threads     // that are ready to run. {     static const EventTypeSpec eventSpec = {'KWIN', 'KWIN' };     OSStatus        err;     OSStatus        junk;     EventTargetRef  appTarget;     EventHandlerRef installedHandler;     EventRef        dummyEvent;      dummyEvent = nil;      // Create a UPP for EventLoopEventHandler and QuitEventHandler     // (if we haven't already done so).      err = noErr;     if (gEventLoopEventHandlerUPP == nil) {         gEventLoopEventHandlerUPP = NewEventHandlerUPP(EventLoopEventHandler);     }     if (gQuitEventHandlerUPP == nil) {         gQuitEventHandlerUPP = NewEventHandlerUPP(QuitEventHandler);     }     if (gEventLoopEventHandlerUPP == nil || gQuitEventHandlerUPP == nil) {         err = memFullErr;     }      // Install EventLoopEventHandler, create a dummy event and post it,     // and then call RunApplicationEventLoop.  The rationale for this     // is as follows:  We want to unravel RunApplicationEventLoop so     // that we can can yield to cooperative threads.  In fact, the     // core code for RunApplicationEventLoop is pretty easy (you     // can see it above in EventLoopEventHandler).  However, if you     // just execute this code you miss out on all the standard event     // handlers.  These are relatively easy to reproduce (handling     // the quit event and so on), but doing so is a pain because     // a) it requires a bunch boilerplate code, and b) if Apple     // extends the list of standard event handlers, your application     // wouldn't benefit.  So, we execute our event loop from within     // a Carbon event handler that we cause to be executed by     // explicitly posting an event to our event loop.  Thus, the     // standard event handlers are installed while our event loop runs.      if (err == noErr) {         err = InstallEventHandler(GetApplicationEventTarget(), gEventLoopEventHandlerUPP,                                   1, &eventSpec, nil, &installedHandler);         if (err == noErr) {             err = MacCreateEvent(nil, 'KWIN', 'KWIN', GetCurrentEventTime(),                                   kEventAttributeNone, &dummyEvent);             if (err == noErr) {                 err = PostEventToQueue(GetMainEventQueue(), dummyEvent,                                   kEventPriorityHigh);             }             if (err == noErr) {                 RunApplicationEventLoop();             }              junk = RemoveEventHandler(installedHandler);             MoreAssertQ(junk == noErr);         }     }      // Clean up.      if (dummyEvent != nil) {         ReleaseEvent(dummyEvent);     } ``` | | __Listing 1__. `RunApplicationEventLoopWithCooperativeThreadSupport` |   The `timeToWaitForEvent` variable is a key part of `EventLoopEventHandler`. If there are no active cooperative threads, `timeToWaitForEvent` is set to `kEventDurationForever` which means that `ReceiveNextEvent` will block your process until some event arrives (or a timer fires). On the other hand, if there are active cooperative threads then `timeToWaitForEvent` is set to `kEventDurationNoWait` and `ReceiveNextEvent` will return immediately with no event, and your cooperative threads will get an appropriately large fraction of the CPU.  Note: Of course, if your cooperative threads are compute-bound you probably want to switch to one of the preemptive threading APIs to take advantage of the second processor on dual processor computers. However, for the sake of this discussion I'll assume that you're looking for the simplest solution.  The approach described above falls down for I/O-bound threads for two reasons.   - Determining `gNumberOfRunningThreads`   becomes difficult as threads start and stop waiting for   I/O. - Cooperative threads always have a high scheduling   latency, which makes them incompatible with fast I/O   (without using excessive memory or CPU). For a further   discussion of this point, see the documentation that   comes with the [OTMP](https://developer.apple.com/samplecode/Sample_Code/Networking/OTMP.htm)   DTS sample.   The solution to this conundrum is to turn your I/O-bound cooperative threads into preemptive threads (MP tasks for Mac OS 9 and Mac OS X, or pthreads for Mac OS X only). A significant amount of the I/O subsystem can be called from preemptive threads, even on Mac OS 9. DTS Technote 2006 [MP-Safe Routines](https://developer.apple.com/library/archive/technotes/tn/tn2006.html) lists the preemptive-safe routines that are available on both Mac OS 9 and Mac OS X.  If a particular I/O subsystem is not callable from preemptive threads on Mac OS 9, it may be possible to construct glue for calling it. A good example of this is the "OTMP" DTS sample (see the URL above).     ---  [Oct 10 2001] |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---

---
