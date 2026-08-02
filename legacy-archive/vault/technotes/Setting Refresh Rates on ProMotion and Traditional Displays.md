---
title: Setting Refresh Rates on ProMotion and Traditional Displays
apple_id: DTS40017657
resource_type: Technical Note
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: null
published: '2017-06-15'
source_url: https://developer.apple.com/library/archive/technotes/tn2460/_index.html
archived_at: '2026-07-27T06:57:05.486473Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2460

# Setting Refresh Rates on ProMotion and Traditional Displays

In this document we will provide detailed information on how to set the display refresh rate property on various view classes such as MTKView, SCNView and SKView. Setting refresh rate is supported in iOS 10, tvOS 10, and macOS 10.12 and later with Xcode 8.3.3.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrvg4wugsbrfvke4vcbi4yq)[How to enable an alternate refresh rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrvg4wugsbrfvke4vcbi4za)[Querying the maximum supported refresh rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrvg4wugsbrfvke4vcbi42a)[Setting a custom refresh rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrvg4wugsbrfvke4vcbi43a)[Use cases and considerations for custom refresh rates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrvg4wugsbrfvke4vcbi43q)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrvg4wvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

The sections that follow describe the steps required to determine a device's maximum refresh rate, how to use an alternate refresh rate and situations for which you would want to change the refresh rate from a default value.

[Back to Top](#)

## How to enable an alternate refresh rate

To enable alternate refresh rates, add the `CADisableMinimumFrameDuration` key, set as true (YES), to your App's Info.plist. Note that this will not be required in later releases of iOS, tvOS and macOS.

__Listing 1__  Info.plist feature flag

```
<key>CADisableMinimumFrameDuration</key>
<true/>
```

[Discussion in Introduction to Metal 2](https://developer.apple.com/videos/play/wwdc2017/601/?time=2135)

[Back to Top](#)

## Querying the maximum supported refresh rate

Once you opt in to supporting alternate refresh rates, you'll want to query your device for it's maximum supported refresh rate. This done via the `maximumFramesPerSecond` property of `UIScreen`.

__Listing 2__  Querying the maximumFramesPerSecond property

```
let maxFPS = UIScreen.maximumFramesPerSecond
```

See the API documentation for UIScreen's [maximumFramesPerSecond](https://developer.apple.com/documentation/uikit/uiscreen/2806814-maximumframespersecond) property for more information.

[Back to Top](#)

## Setting a custom refresh rate

After determining your device's maximum frames per second, you can set your preferred rate for the view class that you're using in your App. `GLKViewController` is an exception as the property is on a view controller instead of a view. There are several choices depending on the framework:

- CADisplaylink's [preferredFramesPerSecond](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1648421-preferredframespersecond) for UIKit if you are driving client side animations on your own
- MTKView's [preferredFramesPerSecond](https://developer.apple.com/documentation/metalkit/mtkview/1536027-preferredframespersecond) for MetalKit
- SCNView's [preferredFramesPerSecond](https://developer.apple.com/documentation/scenekit/scnview/1621205-preferredframespersecond) for SceneKit
- SKView's [preferredFramesPerSecond](https://developer.apple.com/documentation/spritekit/skview/1642773-preferredframespersecond) for SpriteKit
- GLKViewController's [preferredFramesPerSecond](https://developer.apple.com/documentation/glkit/glkviewcontroller/1620702-preferredframespersecond) for GLKit

The actual frame rate chosen by the system is usually a factor of the maximum refresh rate of the screen to provide a consistent frame rate. For example, if the maximum refresh rate of the screen is 60 frames per second, that is also the highest frame rate the [display link](https://developer.apple.com/documentation/quartzcore/cadisplaylink) sets as the actual frame rate; however, if you ask for a lower frame rate, the display link might choose 30, 20, or 15 frames per second (or another rate) as the actual frame rate. Consequently, it's important to consider `preferredFramesPerSecond` as a hint or heuristic and not a guarantee.

Your application should choose a frame rate that it can consistently maintain. The default value is 60 FPS. This means that `preferredFramesPerSecond` must be explicitly set to 120 FPS on a ProMotion display if that is desired.

Setting a refresh rate higher than necessary will increase overall system power consumption which can lead to a poor user experience.

You can verify your App's FPS using [Xcode's GPU report](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/debugging_with_xcode/chapters/special_debugging_workflows.html#//apple_ref/doc/uid/TP40015022-CH9-SW24) in the Debug navigator.

[Back to Top](#)

## Use cases and considerations for custom refresh rates

The typical motivation for choosing a custom frame rate, lower than the device's `maximumFramesPerSecond`, is to prevent frame stuttering where some frames appear on display longer than others. This stuttering makes it difficult to render animations smoothly. On devices with ProMotion displays the time between refresh intervals can be much smaller thereby helping to prevent stutter.

For UIKit based Apps this is handled automatically by presenting immediately to display as soon as content is ready to render. The same is true for SceneKit, SpriteKit and GLKit if you choose to drive the update based on your own pacing or event sources with `preferredFramesPerSecond`.

To get the best performance in UIKit make sure you invalidate your drawing based on the your incoming event changes such as touches, network events, etc. as quickly as possible. The resulting Core Animation transaction will be picked up with the next possible refresh of the display. Take care to invalidate only when necessary to reduce power consumption. See [WWDC 2015 session 233](https://developer.apple.com/videos/play/wwdc2015/233/), [WWDC 2016 session 220](https://developer.apple.com/videos/play/wwdc2016/220/), [Getting High Fidelity Input with Coalesced Touches](https://developer.apple.com/library/content/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/GettingHighFidelityInputwithCoalescedTouches.html#//apple_ref/doc/uid/TP40009541-CH17-SW1), and [Minimizing Latency with Predicted Touches](https://developer.apple.com/library/content/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/MinimizingLatencywithPredictedTouches.html#//apple_ref/doc/uid/TP40009541-CH18-SW1).

For Metal based Apps there are three choices for how to work with custom refresh rates:

- MTLDrawable's [present()](https://developer.apple.com/documentation/metal/mtldrawable/1470284-present) method
- MTLDrawable's [present(afterMinimumDuration:)](https://developer.apple.com/documentation/metal/mtldrawable/2806859-present) method
- MTLDrawable's [present(at:)](https://developer.apple.com/documentation/metal/mtldrawable/1470282-present) method

The first method `present()` is the default and behaves as discussed above. See [WWDC 2017 session 601](https://developer.apple.com/videos/play/wwdc2017/601/?time=2170).

`present(afterMinimumDuration:)` keeps a rendered image on display for a fixed amount of time. This time constraint provides the consistent frame rate that is desired, and is a noteworthy use case for 30FPS on traditional displays with a `maximumFramesPerSecond` value of 60. See [WWDC 2017 session 601](https://developer.apple.com/videos/play/wwdc2017/601/?time=2210).

Lastly, `present(at:)` allows for fully customized presentation timing which can render for exactly the time when the user is going to see it. Scheduling must happen accordingly using MTLDrawable's [presentedTime](https://developer.apple.com/documentation/metal/mtldrawable/2806855-presentedtime) property to get the system feedback required to adjust the timing. See [WWDC 2017 session 601](https://developer.apple.com/videos/play/wwdc2017/601/?time=2240).

__Listing 3__  Supporting custom animation timing

```
let targetTime = // project when intend to display this drawable

// render your scene into a command buffer for 'targetTime'
let drawable = metalLayer.nextDrawable()
commandBuffer.present(drawable, atTime: targetTime)

// after a frame or two...

let presentationDelay = drawable.presentedTime - targetTime
// examine presentationDelay and adjust future frame timing
```

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-06-15 | New document that shows how to detect and enable different refresh rates and the situations in which you'd want to do this. |
