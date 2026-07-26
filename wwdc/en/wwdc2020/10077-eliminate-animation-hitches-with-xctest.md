---
title: Eliminate animation hitches with XCTest
session_id: 10077
collection: wwdc2020
year: 2020
duration: '13:45'
topics: [Developer Tools]
group: D · 响应性、hang/hitch 与渲染循环（RunLoop 的现代替身）
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2020/10077/'
content_hash: 'sha256:a7baa8aee390a78f'
translated: false
---

# Eliminate animation hitches with XCTest

<sub>WWDC2020 · 13:45 · Developer Tools</sub>

Animations can dramatically enhance the user experience of your app, provide a sense of direct manipulation, and help people to better...

> [!note] 归档理由
> 用 XCTest 把动画卡顿变成可回归的指标

## Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10077/2/B3286370-EF32-46C5-AF96-8EF51A8EB971/wwdc2020_10077_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10077/2/B3286370-EF32-46C5-AF96-8EF51A8EB971/wwdc2020_10077_sd.mp4?dl=1)
- [Ultimate application performance survival guide](https://developer.apple.com/videos/play/wwdc2021/10181)
- [Diagnose performance issues with the Xcode Organizer](https://developer.apple.com/videos/play/wwdc2020/10076)
- [Handle interruptions and alerts in UI tests](https://developer.apple.com/videos/play/wwdc2020/10220)
- [Identify trends with the Power and Performance API](https://developer.apple.com/videos/play/wwdc2020/10057)
- [Triage test failures with XCTIssue](https://developer.apple.com/videos/play/wwdc2020/10687)
- [What's new in MetricKit](https://developer.apple.com/videos/play/wwdc2020/10081)
- [XCTSkip your tests](https://developer.apple.com/videos/play/wwdc2020/10164)
- [Create an animation os_signpost interval](https://developer.apple.com/videos/play/wwdc2020/10077/?time=395)
- [Use a UIKit instrumented animation os_signpost interval](https://developer.apple.com/videos/play/wwdc2020/10077/?time=415)
- [Measure scrolling animation performance using a Performance XCTest](https://developer.apple.com/videos/play/wwdc2020/10077/?time=432)
- [Reset the application state between runs](https://developer.apple.com/videos/play/wwdc2020/10077/?time=482)

## Transcript

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

Hello and welcome to WWDC.

Hi, everyone. My name is Tanuja Mohan, and I'm a software engineer on the Power and Performance team at Apple. Animations are an important part in our application's customer experience. Animations can be subtle, such as when we tap on the back button to navigate from one screen to another, or they can be the main focus of a gesture, such as when we scroll up or down on an application. We want these gestures to produce smooth responses since it's noticeable when a navigation takes too long or a scroll appears to jitter.

We call these user perceptible jitters "hitches." A hitch is any time that a frame appears on the screen later than expected. This is distracting to your users and is detrimental to the perceived quality of your application. Let's zoom in on the individual frames of our application to see what is really going on. The first three frames are displayed as expected. We have a gradual movement of the list, perfectly matching the movement of our finger.

But then frame three remains on the screen. The application no longer appears to track the movement of your finger.

Then, when frame four is displayed to screen, the list makes a sudden large jump back to your finger. This is not what we expect and what we want to avoid. To understand what is happening here, we first need to understand how frames are displayed to the screen. Frames on iPhones and iPads are usually expected to update at 60 hertz, giving a cadence of 16.67 milliseconds for each frame. On iPad Pro, we can expect 120 hertz updates, or a cadence of 8.33 milliseconds. This cadence is represented by VSYNCs, which are when the screen determines whether to swap a frame onto the display or not. We see a hitch when a frame misses its expected VSYNC. The severity of a hitch is measured by how late the frame is to appear on-screen.

In this example, frame four is 16.67 milliseconds late.

There are two ways we can quantify hitches.

Hitch time is the time in milliseconds that a frame is late to display on-screen. We prefer to express hitch ratio, milliseconds per second, which is the total hitch time in milliseconds over some other duration of time in seconds. For example, over the duration of a test. This sounds complicated. Why don't we just say dropped frames and measure frames per second? Frames per second is an absolute target that is easily skewed. If your test contains any resting time during the execution of an animation, then fps is useless since we did not expect any frames to be swapped during the resting period.

And we often intentionally do not target the maximum fps. Maybe a game only wants to run at 30 fps, or a video at 24 fps. For power and performance reasons, the hands on the Clock app icon only run at ten fps.

Hitch time's target is always zero and is reliable even with these considerations. But hitch time is not always comparable. Total hitch time for a one-second test cannot be compared to that over a ten-second test.

By normalizing hitch ratio as milliseconds of hitches per second of test duration, we get a metric that is both comparable across different tests and can be used as an approximation for the end user impact. For end user impact, these are the target hitch ratios we recommend and use in our tools.

A hitch ratio of less than five milliseconds per second is good user experience. In the five-to-ten millisecond per second range, users will start to notice hitches, and these hitches should be investigated.

At ten milliseconds per second or more, hitches are quite distracting to the user, and we should take immediate action to resolve them. In iOS 14, you can track hitches in both your development and production workflows using our suite of tools. The XCTest framework allows you to collect hitch and animation data directly in unit and UI tests, while MetricKit and Xcode Organizer give you access to performance metrics from your customers. In this portion of the talk, we're going to focus on the development workflow of catching hitches using Performance XCTests. If you wanna learn how you can view hitches in your production workflow, check out the separate talks we have for MetricKit and Xcode Organizer this year at WWDC 2020 as well. In Xcode 11, we introduced XCTMetrics. These metrics specify what part of the system you want to measure in your test. The XCTMetrics we have available today allow you to test around clock time, CPU utilization, memory use, os_signposts, storage, and with Xcode 12, we have a separate metric to measure application launch times. We also have a template for you to write your own custom metrics.

In this talk, we will focus on the XCTOSSignpostMetric, which is the XCTMetric used to do animation performance testing.

Starting with Xcode 11, you can use the XCTOSSignpostMetric to measure the duration of the os_signpost interval. Now, with Xcode 12, when using an animation os_signpost interval, you will receive not just duration, but also three hitch related metrics, frame rate, and frame count.

You may already be familiar with frame rate and frame count. These two values measure the frequency and number of frames displayed to the screen respectively.

And now you are also familiar with hitches. You can now track how many hitches occur in the tested code block, what the total duration is we spent hitching in our test, and the ratio of this total time hitching over the duration of the measured code block.

To collect these metrics, you first need to instrument your code to emit an os_signpost interval. There are three ways you can do this, and we will refer to them as non-animation intervals-- intervals that only return back duration, and animation intervals-- intervals that return back the additional animation metrics. With Xcode 11, you could only instrument a non-animation os_signpost interval using the "begin" and "end" interfaces. This would just return back duration.

Now, in Xcode 12, to specify an animation os_signpost interval, all you need to do is use the animationBegin interface instead. With just this one change, you can convert any of your existing instrumentation to emit animation intervals instead and receive back the animation metrics mentioned earlier.

Aside from using a custom interval, you can use one of the predefined UIKit instrumented intervals for testing around navigation transitions and scrolling. These are sub-metrics provided on the XCTOSSignpostMetric class. Let's take a look at an example of writing a test using one of these sub-metrics. Here I have a performance XCTest that is going to launch my application, tap on the "Meal Planner" cell, and swipe up on the foodCollection view to scroll down.

In this test, I'm specifying that I want to measure the scrollDeceleration sub-metric.

In the body of the measure block, I'm swiping up, and now with Xcode 12, you can customize the velocity of the scroll.

This test looks good so far, but there is an improvement we can make. Remember by default a measure block is run five times to collect performance measurements. Meaning that in the current implementation, we are going to swipe up five times back-to-back and will most likely be swiping over different content in each iteration.

To avoid this, we want to reset the application state between runs. We can do this by using the XCTMeasureOptions to let our measure block know that we are going to manually stop our measurement collection. Then, pass this into our measure block, call stopMeasuring, and then reset our application state. Now that we have our test written, we wanna run it. But before we do so, we first wanna modify some settings on our test scheme to eliminate their impact on our performance measurements. We first wanna make sure we use a separate test scheme for our Performance XCTests.

Then, we wanna select the release build configuration and disable the debugger.

We also wanna disable automatic screenshot collection and turn off code coverage.

And finally, we wanna turn off all diagnostic options. These are the options listed under Runtime Sanitization, Runtime API Checking, and Memory Management. Now we can run our Performance XCTest and view our results in the report UI. In the drop-down, we can see our new animation metrics. Let's select the Hitch Time Ratio metric.

We see that we collected measurements for five iterations...

and we got an average of 1.2 milliseconds per second for our hitch time ratio.

As a next step, we could set this average value of 1.2 milliseconds per second as our baseline, so that any future runs of this test would be compared to this baseline value.

Let's take a look at an example of how you might encounter a hitch in your code base and how you can use a Performance XCTest to prevent it from shipping to your customers.

Let's say I'm an app developer at a meal planner company that wants to support online orders and deliveries. So far, I've implemented a view that lists the different menu items available.

As a next step, I wanna make my food appealing by including images of what the different dishes look like. Before I dive into writing this new feature, I wanna measure my current animation performance, so I can use it as a baseline to compare for after I add the feature.

I've set up a separate test scheme for my performance test and have configured the settings to what we talked about earlier. I can now write my test.

As we saw before, I'm going to launch my application, tap on the "Meal Planner" cell, and measure my scrolling animation performance.

I've already pre-ran this test, so let's take a look at our measurements.

It looks like we have zero hitches and our animations are performing as expected. Let's go ahead and add in our new feature.

First, I'm gonna set my image view to contain the images I've already pre-included in my project.

Second, I'm gonna scale these images so that they fit well in my application.

Now we can go ahead and rerun our performance test.

Note that when using the XCTOSSignpostMetric, the measure block will listen for when your instrumented os_signpost interval is emitted within the code block and collect metrics only for the code executed within this interval. Another thing to note is that a measure block supports listening for multiple distinct os_signpost intervals. For example, you could listen for both the scrollDeceleration and scrollDragging os_signpost intervals within the same block of code that calls swipe up. Let's skip ahead to the completion of this test.

It looks like we have an increase in the number of hitches and we should immediately investigate.

It looks like our issue is here in our scaleAspectFit call. We are redrawing the image on the main thread which is responsible for rendering the rest of the UI. We are using the CPU, which creates new pixels and allocates memory.

We can reduce this impact by using Core Animation's setContentMode which will hand off redrawing these images to the GPU. This allows us to use the existing image pixels, reducing the amount of work we do on the main thread.

We can rerun our Performance XCTest again to see if this resolves the issue.

We can confirm that our animation metrics now report back zero hitches and our performance is back to what we expect.

Using our Performance XCTest, we were able to see that our new feature caused a regression, giving us a chance to fix it, and that now our feature is ready to reach our customers.

Let's recap what we've talked about. We learned that a hitch occurs any time a frame appears on the screen later than expected. And we can quantify these hitches using the recommended good, warning and critical categories.

We then learned that we can catch hitches in our development workflow using Performance XCTest. We can do this by using a UIKit or custom animation os_signpost interval. We also talked about best practices, which include resetting our application content between iterations and configuring our scheme settings to prevent inaccuracies. With this knowledge, you are now ready to prevent hitches in your code base and provide smooth animation experiences to your customers. Thank you for listening, and we hope you have a great rest of your conference.
