---
title: 'What''s new in MetricKit'
session_id: 10081
collection: wwdc2020
year: 2020
duration: '13:45'
topics: [Developer Tools]
group: G · 调试、崩溃与 Instruments
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2020/10081/'
content_hash: 'sha256:299ba5da331bddad'
translated: false
---

# What's new in MetricKit

<sub>WWDC2020 · 13:45 · Developer Tools</sub>

Quickly detect power and performance regressions and troubleshoot app issues when you adopt MetricKit. Discover the latest trackable...

> [!note] 归档理由
> MetricKit：线上性能与崩溃数据的采集

## Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10081/3/7AC69CDE-C614-4237-9C10-93A3B67C923E/wwdc2020_10081_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10081/3/7AC69CDE-C614-4237-9C10-93A3B67C923E/wwdc2020_10081_sd.mp4?dl=1)
- [Diagnose Power and Performance regressions in your app](https://developer.apple.com/videos/play/wwdc2021/10087)
- [Triage TestFlight crashes in Xcode Organizer](https://developer.apple.com/videos/play/wwdc2021/10203)
- [Ultimate application performance survival guide](https://developer.apple.com/videos/play/wwdc2021/10181)
- [Understand and eliminate hangs from your app](https://developer.apple.com/videos/play/wwdc2021/10258)
- [Diagnose performance issues with the Xcode Organizer](https://developer.apple.com/videos/play/wwdc2020/10076)
- [Eliminate animation hitches with XCTest](https://developer.apple.com/videos/play/wwdc2020/10077)
- [Identify trends with the Power and Performance API](https://developer.apple.com/videos/play/wwdc2020/10057)
- [Using MetricKit](https://developer.apple.com/videos/play/wwdc2020/10081/?time=131)
- [Adopting MetricKit Diagnostics](https://developer.apple.com/videos/play/wwdc2020/10081/?time=494)

## Transcript

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

Hello and welcome to WWDC.

Hi, everyone. My name is Phil Azar. And I'm a software engineer on the Power and Performance Tools team. Today I'm delighted to be able to share with you what's new in MetricKit on iOS 14. Your apps are a pivotal part of the software experience, and your apps are being used more than ever before. When your app is great for battery life and has good performance, it delights your users and contributes to the overall health of the software experience. Our team is committed to providing you powerful tools to improve the battery life and performance footprint of your application. Last year we introduced a number of these tools to help you do this, including MetricKit, an on-device framework for collecting battery life and performance metrics.

Today I'm excited to share with you what's coming in the next version of MetricKit. We'll start with a quick recap on how to use MetricKit. Then, we'll move into a discussion of some powerful new metrics and diagnostics, followed by a deep dive into those new interfaces. Then, we'll wrap up with a quick summary.

Let's get started with some review on how to use MetricKit today.

MetricKit as a framework was designed from the ground up to provide you data in phases of the development cycle where you typically do not have direct access to the users or devices that are running your app.

These phases include during an external beta like TestFlight or once you've shipped to the App Store.

This means, for you as a developer, MetricKit is a powerful tool when leveraged in these phases, as it provides you real access to performance data about your application from a large audience and can help you find trends and patterns in performance regressions. In order to use MetricKit, you need to follow three easy steps. The first is to link and import the MetricKit framework into your code.

The second step is to instantiate a shared instance of what we call the MetricManager, which is a class that serves as your point of contact with the framework.

Finally, you need to implement a provided subscriber delegate protocol to start receiving metrics from the framework.

Here's an example of the previous steps in code. For this example, we've implemented a custom class called MySubscriber to help keep your code clean.

After we link the MetricKit framework, we'll conform this new class to our subscriber protocol, instantiate an instance of our shared MetricManager and add a reference to the new custom class to the manager.

We recommend you remove that reference to the custom class on deinitialization.

Once you've done that, the final step is to implement the didReceive protocol method. This will allow you to receive metric payloads.

Let's review how the system aggregates and deliver these payloads to your application through MetricKit.

Over the course of the day, the operating system is passively aggregating performance data for your app as it is used. This data is anonymized and designed to protect user privacy.

At the end of the day, that data is bundled into a 24-hour payload which we know as the MetricKit payload. Metric payloads are strongly typed by the MetricKit interface.

Let's take a look into what sorts of data that payload contains. MetricKit payloads contain a wide variety of data, including launch times, CPU time, memory and more. Here, we've taken a MetricKit payload and converted it to a human-readable format.

This makes it easier for us to see that the data is split up into three types of aggregation-- cumulative, averaged and bucketized data.

Post-process, this data is extremely useful in identifying performance regressions build-to-build in your application and can be used in conjunction with local context to tackle challenging problems. In some areas, however, the metrics we have today may not be enough to fully characterize a regression.

Let's take a look at a common example of this-- our launch performance data.

We see here that the number of cold launches, i.e. when our app is being launched from scratch with no resources in memory, far exceeds the number of resumes.

In a typically well-performing app, we would expect our resumes to be much more prevalent than our launches. Something seems to be amiss here. Another common case is our cumulative CPU time.

Notice how our cumulative CPU time is far smaller than our cumulative foreground time.

This might seem like a good thing, but it isn't clear if this level of work is indicative of a performance regression or improvement because the CPU time is bound by clock frequency.

As developers, our first instinct might be to quantify this more precisely. And as it stands right now, that's not a straightforward problem.

There's a clear area for growth here. We need more details to dig deeper into these problems. This year, with MetricKit 2.0, we're going to be providing you some new metrics that we think will help you dig deeper into these common problem cases. Our team has worked hard to expand a subset of metrics to provide further clarity into application workload, performance and stability.

These include CPU instructions, scroll hitches and application exits. Let's start by reviewing CPU instructions first.

CPU instructions in MetricKit are a new addition to the MXCPUMetric class.

This metric summarizes daily cumulative instructions retired by your application.

CPU instructions are an absolute metric for the work that your application does on the CPU. It is both hardware and frequency independent.

This is going to enable you to more precisely quantify the total workload of your application. Next up, let's talk about scroll hitches. Scroll hitches are a new metric we're providing you this year to help you give insights into your application's graphical performance. A scroll hitch is when a rendered frame does not end up on screen at its expected time during scrolling.

This usually causes frames to be dropped, causing a user-perceptible interruption of animation smoothness.

In MetricKit, we'll be providing you a ratio of time that your application spends hitching to the time spent scrolling with UIScrollViews.

To dive deeper into the technical details of hitches, I encourage you to watch our talk this year covering scroll hitches and how to measure them using XCTest metrics.

Last but not least, we have application exit reasons.

This year, we're providing metrics around application exits and terminations. You'll receive a daily summary of reasons and counts of why your application exited in both the foreground and the background.

We think this is going to be helpful in assisting you track down common problems associated with app launch and using background runtime frameworks.

For a deeper dive into how you can leverage these metrics and employ best practices, I encourage you to watch our talk on app terminations this year, entitled "Why Did My App Get Killed?" And so those are our new metrics this year. We think they're gonna provide you an extra degree of certainty when looking for regressions in your MetricKit data.

Let's look back at our metric payload more closely and focus on one area where we still weren't able to determine what's going on.

In our application hang duration histogram, we see some entries that are alarming and could be a serious interruption in your user's experience.

As it stands right now, this is definitely a regression. But we can't determine the root cause from metrics alone.

We need some additional diagnostic data, like a backtrace at the time of the hang, to figure out what happened.

That brings us to our next big feature this year for MetricKit that's going to help you get to the bottom of another class of regressions-- MetricKit diagnostics.

MetricKit 2.0 is going to be providing a new interface that enables you access to targeted diagnostic information.

This diagnostic information is actionable for various types of regressions, including hangs, crashes, disk write exceptions and CPU exceptions.

To start receiving diagnostics in MetricKit 2.0, all you need to do is implement a new MetricManagerSubscriber protocol method. That's it! This new protocol looks almost identical to last year's didReceive metric payloads delegate method, and we expect that many of you will be able to use the same pipelines you've already built for MetricKit.

This protocol, however, doesn't just look the same. It also functions the same.

Semantically, MetricKit diagnostics functions almost identically to MetricKit metrics.

If we take another look at our timeline from earlier, as your app is used throughout the day, in addition to metrics, the MetricKit system will now passively collect diagnostic information about regressions that occur during use. Then, the system bundles them into a parallel daily diagnostic payload that can be used alongside your daily metric payload. Now, when you see a regression in a metric like hangs, you'll be able to reference, if present, the associated diagnostic payload that came at the same time as the metric payload.

This diagnostic payload effectively maps one-to-one to its companion metric payload.

Let's switch gears and take a deeper look into this new interface and get familiar with its capabilities. The new diagnostic interface mirrors the old metric interface insofar that we have a few new base classes-- MXDiagnostic, the base class that all diagnostics inherit from, MXDiagnosticPayload, the carrier class which contains all diagnostics at the end of the day, and MXCallStackTree, a new data class that encapsulates regression time backtraces for off-device use.

MXDiagnostics, which are contained within MXDiagnosticPayloads, contain metadata of the application at the time a regression occurred, such as the specific build version and diagnostic-specific data.

Diagnostic-specific data is a unique subset of data for each diagnostic subclass that we're providing this year.

One part that's consistent across all of them, however, is MXCallStackTree.

MXCallStackTree is a new data class that we're providing that encapsulates backtraces at the time a regression occurs.

These backtraces are unsymbolicated and designed for off-device processing. And they're going to provide you a rich set of information that will help you diagnose and capture the essence of regressions.

Here's an example of what these call stack trees look like after they've been converted to a human-readable JSON.

We can see that everything needed to symbolicate individual frames with a tool like ATOS is present. That includes binary information, such as the UUID, offset and name, and the frame address.

These new call stack tree data structures are highly portable and can be found in other performance tools we're shipping this year. To learn more, I encourage you to watch our talk on the new Power and Performance API.

As we said earlier, we're shipping a set of four new subclasses of MXDiagnostic this year-- hangs, CPU exceptions, disk write exceptions and crashes. Let's take a look at the unique data contained within each of these new diagnostic subclasses now, starting with hangs. Hangs are regressions that occur when your application is unresponsive to user input for long periods of time.

This is due to your application's main thread being blocked or busy.

Hang diagnostics provided through the MetricKit interface are gonna be providing you the time the application's main thread was unresponsive and the backtraces of the main thread.

Next up is CPU exceptions, or energy logs as they're called in the Xcode Organizer. These diagnostics are going to contain CPU time consumed, total time sampled during the high CPU usage and the backtraces of the threads consuming CPU time.

CPU exception diagnostics used in conjunction with metric payloads can be extremely useful in identifying regressions that may not be easy to reproduce.

Next, we have disk writes. Disk write exception diagnostics are fairly similar to CPU exception diagnostics.

Each diagnostic will contain the total number of writes caused that generated the exception and a backtrace of the threads causing excessive writes. These diagnostics are generated whenever a one-gigabyte daily threshold is breached by your application.

Last but not least, we have crash diagnostics. This year, we're excited to share that MetricKit is going to be providing you a diagnostic for application crashes.

Each time your application crashes, an MXCrashDiagnostic containing the exception information, termination reason, virtual memory region information, in the case of a bad access crash, and the backtrace will be provided to you via the MetricKit diagnostics interface.

And that wraps up MetricKit diagnostics, a powerful new tool for you to get to the root cause of regressions in real customer use cases. Let's wrap up with a summary of what we talked about today.

MetricKit 2.0 is packed with new features that are going to help you take your optimization efforts to the next level. We're providing new metrics for you to dive deeper into understanding regressions that occur in your customer and beta populations. We're also providing you targeted diagnostics to enable you to catch harder-to-reproduce regressions in those populations.

And finally, we're doing this all at very little cost to you by providing these new features through easy-to-implement interfaces and existing interfaces.

We have a ton of great new content this year and useful older content that I encourage you to check out. Thanks again for tuning in, and enjoy the rest of your WWDC 2020.
