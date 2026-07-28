---
title: 提供高滚动性能
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2015/06/25/ios/delivering-high-scroll-performance/'
original_language: en
published: 2015-06-25
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:21cfda2120c0e64c'
translated: true
---

> 原文：[Delivering high scroll performance](https://engineering.fb.com/2015/06/25/ios/delivering-high-scroll-performance/)　·　Meta Engineering — iOS

为使用我们 iOS App 的用户提供最佳体验是 Facebook 的目标之一。这个目标的一部分是确保动态消息（News Feed）的滚动流畅，但在一个包含高度可变内容的复杂滚动视图（Scroll View）中，目前 iOS 上还没有好方法能识别丢帧会来自哪里。我们开发了一种在实践中非常有效的识别策略，帮助我们维持高滚动性能。我们将在本文中详细介绍其工作原理。

## 在设备上测量滚动性能

大多数性能工作的第一步是测量和检测。[Apple 的 Instruments 应用](https://developer.apple.com/library/mac/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/Introduction/Introduction.html)允许你测量 App 的帧率，但很难模拟 App 在实际使用中发生的所有交互。另一种方法是直接在设备上测量滚动性能。

我们使用 [Apple 的 CADisplayLink API](https://developer.apple.com/library/prerelease/ios/documentation/QuartzCore/Reference/CADisplayLink_ClassRef/index.html) 来测量设备帧率。每次渲染一帧时，我们都测量其所花费的时间。如果超过六十分之一秒（16.6 毫秒），则表明丢帧，滚动出现了卡顿。

```clike
[CADisplayLink displayLinkWithTarget:self selector:@selector(_update)];
[_displayLink addToRunLoop:[NSRunLoop mainRunLoop] forMode:NSRunLoopCommonModes];
```

## 发现并修复性能衰退

与视频游戏不同，Facebook App 对 GPU 的消耗并不高。它主要显示文本和图像，因此大多数丢帧来自 CPU。为了保持稳定的 CPU 性能，我们希望确保组成动态消息中一条内容渲染的所有操作在 16.6 毫秒内完成。实际上，渲染一帧由多个步骤组成，在丢帧之前，App 通常只有 8 到 10 毫秒的主线程（Main Thread）处理时间，而不是完整的 16.6 毫秒。

因此，了解主线程在 CPU 上的时间都花在了哪里，有助于提供最佳的滚动体验。可以使用 [Time Profiler](https://developer.apple.com/library/mac/documentation/AnalysisTools/Reference/Instruments_User_Reference/TimeProfilerInstrument/TimeProfilerInstrument.html) 来评估主线程的时间花费，但重新创建丢帧时的确切设备条件可能很困难。

另一种方法是让 App 在运行时收集数据，以帮助识别丢帧最可能的原因。从某种意义上说，这就是 App 如何分析自身。一种实现方式是使用信号。产生的数据可能会有干扰，但它允许你在沙盒环境中获取分析数据。这在 iOS 上使用 Instruments 和 DTrace 等标准工具进行传统分析时是不可能的。

## 信号与设备端分析

要了解一个线程在做什么，我们通过向它发送一个信号并注册该信号的回调来挂起它。

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

信号安全的操作非常有限。例如，内存分配就不是，因此我们在信号处理器（Signal Handler）中唯一做的事情就是捕获当前的调用栈（Backtrace）。

## 触发信号

![](https://engineering.fb.com/wp-content/uploads/2015/06/GEMHrgAsxl4bJ1oFABQauyIAAAAAbj0JAAAB.jpg)

一旦信号捕获就位，我们需要一个触发信号的机制。它不能从主线程发送，因为那是我们试图跟踪的线程。GCD 是管理执行流程的一个优秀抽象。然而，分发源（Dispatch Source）作为提供执行代码块的标准机制，缺乏每 10 毫秒执行一次所需的精度。NSThread 提供了必要的粒度。

当主线程有很多工作时，它很可能会丢帧，此时主线程会被分配最多的执行时间。不幸的是，这意味着我们的信号发送线程很可能会一直等到主线程繁忙结束，从而错过使用高峰期。为了解决这个问题，我们给信号发送线程设置了比主线程更高的优先级。这确保了即使主线程处于最大利用率时，我们也能捕获到调用栈。

```clike
_trackerThread = [[NSThread alloc] initWithTarget:[self class] selector:@selector(_trackerLoop) object:nil];    
_trackerThread.threadPriority = 1.0;
[_trackerThread start];
```

与性能测量常见的情况一样，测量行为本身会影响 App，并可能带来额外的性能影响。在 iPhone 4S 上捕获调用栈大约需要 1 微秒，而当你只有 16 毫秒时，这已经相当多了。此外，挂起主线程（以触发信号）的行为会导致线程间更多的上下文切换，并可能拖慢整个 App。

因此，选择一个理想的采样策略并仅在绝对必要时进行测量非常重要。在我们的案例中，我们对采样时机做了一系列优化。一个简单的例子是仅在用户滚动时触发信号。另一个改进是我们仅在员工使用的内部版本上进行测量，这样测量就不会影响到我们的生产环境 App。

## 上报与符号化

一旦捕获到调用栈，我们会在设备上聚合它们，然后批量发送到服务器。当然，调用栈是不可读的——它是一堆地址——需要进行符号化（Symbolication），对此已有多种工具可用。[Apple atos API](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/atos.1.html )、[Google Breakpad](https://code.google.com/p/google-breakpad/) 和 [Facebook 的 atosl](https://github.com/facebook/atosl) 就是几个例子。符号化之后，我们会在一个数据可视化工具中聚合这些轨迹，以识别需要集中优化系统的哪些部分，并随着我们持续改进滚动性能来防止性能衰退。

以下是一个示例，显示了 Facebook App 两个版本的 CPU 消耗：

![](https://engineering.fb.com/wp-content/uploads/2015/06/GGAGrgAVKr5KcV4BAGcCw2IAAAAAbj0JAAAB.jpg)

## 尝试一下

这个策略让我们能够在大量性能衰退影响到生产环境之前就检测到它们。我们将此实现的示例放到了 [GitHub](https://gist.github.com/clementgenzmer/4ff6c51224089cc65e9b) 上。希望你会觉得它在你自己的项目中也有用！
