---
title: Delivering high scroll performance
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2015/06/25/ios/delivering-high-scroll-performance/'
original_language: en
published: 2015-06-25
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:21cfda2120c0e64c'
translated: false
---

> 原文：[Delivering high scroll performance](https://engineering.fb.com/2015/06/25/ios/delivering-high-scroll-performance/)　·　Meta Engineering — iOS

Delivering the best experience to people using our iOS app is one of our goals at Facebook. Part of this goal is to make sure the News Feed scrolls smoothly, but in a complicated scroll view with highly variable content, there is currently no good way on iOS to identify where frame drops will come from. We’ve developed an identification strategy that works very well in practice and assists us with maintaining high scroll performance. We’ll detail how it works in this post.

## Measuring scroll performance on device

The first step in most performance work is measurement and instrumentation. [Apple’s Instruments app](https://developer.apple.com/library/mac/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/Introduction/Introduction.html) allows you to measure the frame rate of your app, but it is difficult to simulate all the interactions that occur when the app is in use. Another approach would be to measure the scroll performance directly on a device.

We measure the on-device frame rate using [Apple’s CADisplayLink API](https://developer.apple.com/library/prerelease/ios/documentation/QuartzCore/Reference/CADisplayLink_ClassRef/index.html). Each time a frame is rendered, we measure the time it took. If it took more than one-sixtieth of a second (16.6 ms), a frame was dropped and the scrolling stuttered.

```clike
[CADisplayLink displayLinkWithTarget:self selector:@selector(_update)];
[_displayLink addToRunLoop:[NSRunLoop mainRunLoop] forMode:NSRunLoopCommonModes];
```

## Finding and fixing regressions

Unlike a video game, the Facebook app is not very GPU-intensive. It displays mostly text and images, and thus most frame drops come from the CPU. To maintain solid CPU performance, we want to make sure that all the operations that compose the rendering for a story in News Feed are performed in less than 16.6 milliseconds. In practice, rendering a frame is composed of multiple steps, and an app typically has only 8 to 10 ms of main thread processing before dropping a frame, not the full 16.6 ms.

Knowing where the main thread is spending time on the CPU, then, is helpful to delivering the best scrolling experience. It is possible to use the [Time Profiler](https://developer.apple.com/library/mac/documentation/AnalysisTools/Reference/Instruments_User_Reference/TimeProfilerInstrument/TimeProfilerInstrument.html)to evaluate where the main thread is spending time, but it can be difficult to re-create the exact conditions the device was in when the frame was dropped.

Another approach is for the app to gather data while running to help identify the most likely cause of a frame drop. This is, in a way, how the app can profile itself. One way to do this is through the use of signals. The resulting data can be noisy, but it allows you to get profiling data in a sandboxed environment. It is impossible with traditional profiling on iOS with standard tools like Instruments and DTrace.

## Signals and on-device profiling

To understand what a thread is doing, we suspend it by sending a signal to it and having a callback registered for the signal.

```clike
static void _callstack_signal_handler(int signr, siginfo_t *info, void *secret) {
  callstack_size = backtrace(callstacks, 128);
}

struct sigaction sa;
sigfillset(&sa.sa_mask);
sa.sa_flags = SA_SIGINFO;
sa.sa_sigaction = _callstack_signal_handler;
sigaction(SIGPROF, &sa, NULL);
```

The operations that are signal-safe are pretty limited. Memory allocation, for instance, is not, so the only thing that we do in the signal handler is capture the current backtrace.

## Firing the signal

![](https://engineering.fb.com/wp-content/uploads/2015/06/GEMHrgAsxl4bJ1oFABQauyIAAAAAbj0JAAAB.jpg)

Once the signal capturing is in place, we need a mechanism to fire the signal. It can’t be sent from the main thread, since that is the thread we are trying to track. GCD is a great abstraction for managing flow of executions. However, dispatch sources, the standard mechanism for supplying blocks of execution, lack the resolution to be executed as often as every 10 ms. NSThread offers the necessary granularity.

When the main thread has a lot of work, and thus is likely to drop a frame, it will be given the most time to execute. Unfortunately, this means that our signaling thread is likely to be woken up until the main thread winds down and we miss the moment of heavy use. To work around this problem, we give the signal-firing thread a priority that is higher than the main thread. This ensures that we can capture a backtrace even when the main thread is at maximum utilization.

```clike
_trackerThread = [[NSThread alloc] initWithTarget:[self class] selector:@selector(_trackerLoop) object:nil];    
_trackerThread.threadPriority = 1.0;
[_trackerThread start];
```

As is common with performance measurement, the act of measuring affects the app and can have additional performance implications of its own. Capturing the backtrace on an iPhone 4S takes roughly 1 microsecond, and when you have only 16 milliseconds, that’s quite a bit. Also, the act of suspending the main thread (to fire the signal) generates more context switching between threads and can slow down the app as a whole.

Thus, it is important to choose an ideal sampling policy and measure only when absolutely needed. In our case, we made a number of optimizations to when we sample. One straightforward example was to fire the signal only when the user is scrolling. Another change we made was to measure on only internal builds that employees use so that the measurement would not affect our production app.

## Reporting and symbolication

Once the backtrace is captured, we aggregate them on the device and send them to the server in batches. The backtrace is, of course, unreadable — a collection of addresses — and needs to be symbolicated, for which there are a number of tools already available. [Apple atos API](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/atos.1.html ), [Google Breakpad](https://code.google.com/p/google-breakpad/), and [Facebook’s atosl](https://github.com/facebook/atosl) are a few examples. After symbolication, we aggregate the traces in a data-visualization tool to identify the parts of the system on which to focus our efforts and prevent regressions as we continue to improve our scroll performance.

Here is an example showing the CPU consumption of two versions of the Facebook app:

![](https://engineering.fb.com/wp-content/uploads/2015/06/GGAGrgAVKr5KcV4BAGcCw2IAAAAAbj0JAAAB.jpg)

## Try it out

This strategy has allowed us to detect a very large number of regressions before they hit production. We put a sample of this implementation on [GitHub](https://gist.github.com/clementgenzmer/4ff6c51224089cc65e9b). We hope you will find it useful in projects of your own!
