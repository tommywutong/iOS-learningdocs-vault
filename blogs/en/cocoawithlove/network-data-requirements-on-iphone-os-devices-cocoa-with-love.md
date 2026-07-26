---
title: 'Network data requirements on iPhone OS devices | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/04/network-data-requirements-on-iphone-os.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:5850a3c623ffe15e'
translated: false
---

> 原文：[Network data requirements on iPhone OS devices | Cocoa with Love](https://www.cocoawithlove.com/2010/04/network-data-requirements-on-iphone-os.html)　·　Cocoa with Love (Matt Gallagher)

If your iPhone OS application makes heavy use of the network, there are a few extra settings your application will require to ensure the network works correctly and Apple will approve your application. These requirements are not always obvious (some are documented, others are only implied in documentation). I thought I'd share them so that you can avoid network dropouts and unnecessary App Store rejections.

## Info.plist settings

If your iPhone/iPad/iPod Touch application uses a WiFi network connection at all, you should enable `UIRequiresPersistentWiFi` (Application uses Wi-Fi) in your application's Info.plist. Without this setting, the device will put its WiFi connection to sleep after 5-30 minutes.

I've mentioned this setting in a [previous post](https://www.cocoawithlove.com/2009/08/control-and-configuration-of.html) but I feel it is worth repeating since it is an easy flag to overlook and it leads to unexpected network dropouts if it isn't set.

There are other Info.plist settings, including the `UIRequireDeviceCapabilities` (Required device capabilities) value "wifi" which you can enable if you choose but it does not appear to have any effect at this time.

## Reachability

If your application runs on WiFi only or 3G only, then you are required to test this and present an error to the user if the wrong network is in use. This is a usability requirement that Apple enforces and your application will be rejected if it isn't followed.

Apple provide the [Reachability sample application](http://developer.apple.com/iphone/library/samplecode/Reachability/Introduction/Intro.html) to show how you can test for network availability. Internally, this class uses the `SCNetworkReachability` API but it's much easier to borrow the entire `Reachability` class from this example program and invoke:

```objc
if ([[Reachability reachabilityForLocalWiFi] currentReachabilityStatus] == ReachableViaWiFi)
{
    // perform action that requires a local WiFi connection
}
else
{
    // give a message that local WiFi is required
}
```

A quick warning about this: the WiFi connection can take 10 seconds or more to wake up after the device is woken up from sleep. If WiFi is not available, you may want to set a timer and try again for the next 5-10 seconds before presenting an error.

## 3G data throttling

If your application uses continuous data over 3G, you are required to throttle this data, rather than perpetually use the maximum available.

What do I mean by this?

As an example: I wrote an application for a client that downloaded music tracks to the phone and then played these tracks from the locally stored cache. The download of the track was not speed limited and Apple initially rejected the application for making excessive use of 3G.

This guideline is somewhat fuzzy. Apple did not give a specific data rate to which the application should limit itself. I do wonder if they didn't realize that the audio wasn't actually streaming but a progressive download.

In any case, throttling the download at 128kbps allowed the application to be approved.

How do you throttle a download? With an `NSURLConnection`, you can't.

I used the following crude but easy to implement approach. First, I switched from `NSURLConnection` to a `CFReadStream`. Then, in the `ReadStreamCallback`, I tracked the data downloaded over a small time window and if data downloaded exceeded the allowance for that window, simply removed the `CFReadStreamRef` from the run loop and scheduled a timer to put it back at the end of the windowed allowance period:

```objc
CFReadStreamUnscheduleFromRunLoop(
    downloadStream,
    CFRunLoopGetCurrent(),
    kCFRunLoopCommonModes);

NSTimeInterval delay =
    THROTTLE_WINDOW_DURATION * 
    (totalDataDownloaded - startOfThrottleWindow) / THROTTLE_WINDOW_QUOTA;
throttleTimer =
    [NSTimer
        scheduledTimerWithTimeInterval:delay
        target:self
        selector:@selector(continueDownload)
        userInfo:nil
        repeats:NO];
```

and in the implementation of `continueDownload` I used `CFReadStreamScheduleWithRunLoop` to reschedule the download again.

By removing the `CFReadStreamRef` from the run loop, it doesn't get processed and the connection is throttled. Put it back into the run loop when it's under quota again.

## Progressive download limit for 3G video

This limitation is pretty simple: if you are playing an MP4/MOV downloaded from a 3G network, it must be shorter than 10 minutes and a lower data rate than 5MB in 5 minutes (that's about 192kbps). Apple have started rejecting applications that significantly exceed these quoted limits.

The answer is that you are expected to convert any such application over to the new HTTP video streaming approach which can offer a more responsive performance over 3G.

## HTTP streaming video 64kbps stream

On the topic of HTTP streaming video, Apple have also added a new requirement that any HTTP video streaming that is intended for use over 3G must offer one stream quality that is 64kbps or less.

Apple suggest that you offer an audio-only stream quality to satisfy this requirement. Personally, I think that 4 frames per second is still better than none if you can find a way to squeeze in the video too. The iPhone doesn't like to play video at frame rates lower than about 2.5fps so you can't go much lower than this.

## Conclusion

There are a lot of little quirks to using a mobile, low power or 3G network device and these quirks won't always appear during testing on the simulator or during brief test runs on your office WiFi.

Apple have also added a lot of limits to how you can use 3G. None of this is really heavy-handed on their part — it appears they really are just trying to make sure that 3G connected applications will work in real-world situations — but it does create a collection of extra requirements you need to satisfy.

I hope some of these points are helpful. Every example on this page represents a point that I've had to fix in an application (sometimes during beta but sometimes during App Store submission or after release to customers). The sooner the better — it's always best to know _before_ you start.
