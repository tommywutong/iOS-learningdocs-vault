---
title: Adjusting the movie brightness
apple_id: DTS10003407
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2004-09-16'
source_url: https://developer.apple.com/library/archive/qa/qa1382/_index.html
archived_at: '2026-07-18T02:30:29.293468Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1382

# Adjusting the movie brightness

## Q:  I'd like to change the brightness of a movie during playback, just as I can in QuickTime Player using the brightness control. Is there an API to do this?

A: I'd like to change the brightness of a movie during playback, just as I can in QuickTime Player using the brightness control. Is there an API to do this?

The QuickTime Player makes use of a private, custom filter to adjust movie brightness during playback. The way it works is each movie frame is first rendered offscreen and the filter is applied to the frame. The modified frame is then copied back to the screen for display.

You can use a similar technique in your application with the QuickTime Brightness & Contrast Filter Effect (`kBrightnessContrastImageFilterType` ='`brco`'). Simply step through each frame of the movie, draw the frame to an offscreen buffer and apply the Brightness & Contrast Filter Effect. Finally, copy the modified image to the screen.

The [Sample Code 'qtshoweffect'](https://developer.apple.com/samplecode/qtshoweffect/index.html) demonstrates this technique for effects in general, and the [Sample Code 'QTEffects Explode'](https://developer.apple.com/samplecode/QTEffects_Explode/index.html) shows how to build and run an effect without presenting the effects dialog first. For more information about the QuickTime Effects, check the [QuickTime Video and Effects Documentation](https://developer.apple.com/documentation/QuickTime/RM/EffectsTransitions/Effects/index.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-09-16 | New document that demonstrates how to adjust the brightness of a movie for playback. |

