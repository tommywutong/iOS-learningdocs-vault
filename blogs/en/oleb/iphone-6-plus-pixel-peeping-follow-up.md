---
title: iPhone 6 Plus Pixel Peeping Follow-Up
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/12/pixel-peeping-followup/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:7169278b6ccb9383'
translated: false
---

> 原文：[iPhone 6 Plus Pixel Peeping Follow-Up](https://oleb.net/blog/2014/12/pixel-peeping-followup/)　·　Ole Begemann

# iPhone 6 Plus Pixel Peeping Follow-Up

## A Closer Look at Display Zoom

After posting [iPhone 6 Plus Pixel Peeping](https://oleb.net/blog/2014/11/iphone-6-plus-screen/), several people asked if and how the results would change if Display Zoom was activated. So I did some more tests on the iPhone 6 Plus and also tested with an iPhone 6.

# UIKit/CoreGraphics Rendering

## iPhone 6 Plus

[Display Zoom](http://support.apple.com/en-us/HT203073) is a feature on the iPhone 6 and 6 Plus that allows users to trade screen space for a larger user interface. With Display Zoom enabled, an iPhone 6 Plus effectively [behaves as if it had the same logical resolution as the iPhone 6](http://www.paintcodeapp.com/news/ultimate-guide-to-iphone-resolutions) (375 × 667 points). Output is first rendered into a 1125 × 2001 pixel backing store (at 3× scale) and finally downsampled to fit the 1080 × 1920 pixel screen resolution.

My tests show that activating Display Zoom on the 6 Plus has no discernible negative or positive effect on output quality. The effective scale factor changes from one non-integral number (2.61 px/pt) to another (2.88 px/pt), resulting in a final image that is just as flawed on a per-pixel level as it was before.[1](#fn:1) I did not take any new close-up photos to back this up, but the line pattern in [my test app](https://github.com/ole/iphone-6-plus-rendering) looks essentially identical in both modes (with respect to image quality; the image becomes larger with Display Zoom activated, of course).

## iPhone 6

On the iPhone 6, Display Zoom reduces the logical screen size [from 375 × 667 to 320 × 568 points](http://www.paintcodeapp.com/news/ultimate-guide-to-iphone-resolutions) (the same as the iPhone 5 and 5s). The logical scale factor for rendering into the backing store remains at 2×. The backing store image measuring 640 × 1136 pixels is then upscaled by approximately 17% to the screen dimensions of 750 × 1334 pixels – the native scale factor is 2.34×.

The end result is a slightly blurry image which, unlike the ever-present-but-practically-invisible loss of image quality on the 6 Plus, looks clearly worse than the non-zoomed image at normal viewing distance. Especially text looks distinctly worse when Display Zoom is on. I’m not sure whether the lower-resolution screen on the iPhone 6 (326 ppi vs. 401 ppi) or the fact that upscaling is worse for image quality than downscaling is the major contributing factor here.

The line pattern in my test app also shows the image degradation very clearly. With Display Zoom off, the rendering is pixel-perfect. The result looks like [this photo I took of an iPhone 5 screen](https://oleb.net/media/iphone-5-test-pattern-photo-logical-and-native-pixels-PA220016.png). Turn Display Zoom on and lines start to bleed into neighboring pixels, resulting in an uneven pattern and overall darker image (like [this photo of an iPhone 6 Plus screen](https://oleb.net/media/iphone-6-plus-test-pattern-photo-logical-pixels-PA220021.png)).

# OpenGL Rendering

[We saw](https://oleb.net/blog/2014/11/iphone-6-plus-screen/#opengl) that on the 6 Plus iOS can bypass the final scaling step for OpenGL rendering. It turns out this also works when Display Zoom is activated, and applies to the iPhone 6 as well.

My test app, and any other app that uses OpenGL, renders identically regardless of the user’s Display Zoom setting. A `GLKView`’s default renderbuffer is always initialized to the device’s native pixel dimensions (1080 × 1920 px on the 6 Plus and 750 × 1334 px on the 6). If you want to render certain parts of your OpenGL scene (such as UI elements) larger when Display Zoom is activated, you should explicitly take the `GLKView`’s `contentScaleFactor` into account. On the iPhone 6, its value will be `2.0` with Display Zoom off and `2.34` when it is on.

On the iPhone 6, I also observed the same sudden loss in image quality that I saw on the 6 Plus when OpenGL content (rendered at native resolution) has to be mixed with UIKit content (rendered at logical resolution). See how the pattern becomes darker and irregular as soon as the blur overlay is shown in the video below:

<sub>iPhone 6 with Display Zoom enabled rendering the test pattern using OpenGL. Note that the pattern is crisp and pixel-perfect in the No Overlay and Alpha Overlay modes because the OpenGL renderbuffer uses native pixel dimensions even with Display Zoom on. (The moiré pattern is caused by the video recording. It looks perfect in real life.) Observe the loss in image quality when the Blur Overlay is activated: once the OpenGL view needs to be composited with another view, the scaling must kick in again. [Download the video](https://oleb.net/media/iphone-6-opengl-display-zoom.mp4).</sub>

# 1080p Video

[Again](https://oleb.net/blog/2014/11/iphone-6-plus-screen/#p-video), for full-screen 1080p video playback, the iPhone 6 Plus can skip the scaling stage and render directly at native resolution. Since full-screen video is not scaled differently when Display Zoom is activated, it would make sense to work identically under both settings, and that is indeed so.

I have never seen this effect in real-life examples, but the image quality in this video of a test pattern degrades very noticeably once we force the OS to engage the scaling stage by showing the toolbars:

<sub>iPhone 6 Plus with Display Zoom activated playing a 1080p video. The image quality deteriorates once the playback controls are shown because the scaling kicks in. This indicates that the scaling step is being bypassed when the player controls are not visible and the video is being rendered at its native 1080p resolution even in Display Zoom mode. [Download the video](https://oleb.net/media/iphone-6-plus-1080p-video-display-zoom.mp4).</sub>

Lastly, let me show you one observation I can’t explain. Playing the 1080p test video on an iPhone 6, the image also changes very noticeably whenever I show or hide the player controls (regardless of whether Display Zoom is on or off). It looks as though an additional scaling step is performed when the controls are shown, despite the fact that the video resolution doesn’t match the device’s native resolution, anyway. I don’t know what happens here.

<sub>iPhone 6 with Display Zoom disabled playing a 1080p video. I can’t explain why the image changes when the playback controls are hidden or shown. (The result is the same with Display Zoom enabled.) [Download the video](https://oleb.net/media/iphone-6-1080p-video-no-display-zoom.mp4).</sub>

1. You can use the `UIScreen.nativeScale` property to find out if Display Zoom is activated. It will report different values depending on the setting. In a standard UIKit app you should normally not need to use this information anywhere, however. [↩︎](#fnref:1)
