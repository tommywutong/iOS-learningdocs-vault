---
title: Improving your app’s rendering efficiency
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/improving-your-app-s-rendering-efficiency
source_url: 'https://developer.apple.com/documentation/xcode/improving-your-app-s-rendering-efficiency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/improving-your-app-s-rendering-efficiency.json'
content_hash: 'sha256:06e44120d331aa45'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Performance and metrics](performance-and-metrics.md) · [Reducing your app’s battery use](reducing-your-app-s-battery-use.md)

# Improving your app’s rendering efficiency

<sub>Article</sub>

Optimize view updates by minimizing unnecessary redraws and using efficient update strategies.

## Overview

Redrawing views unnecessarily, or performing complicated updates, can increase power consumption by the CPU and GPU. Additionally, inefficient view updates can contribute to hangs and hitches in your app, degrading a person’s experience when they use your app. For more information, see [Understanding user interface responsiveness](understanding-user-interface-responsiveness.md).

### Improve SwiftUI performance

Profile your app with the SwiftUI instrument to identify long-running view body updates and frequent view updates in your app, and reorganize your views to avoid these. For more information, see [Understanding and improving SwiftUI performance](understanding-and-improving-swiftui-performance.md).

### Limit the frame rate and duration of animations

Use animations to communicate changes and updates in your app, and pause or stop them when the update completes. For more information, see [Foundations \> Motion](https://developer.apple.com/design/human-interface-guidelines/motion) in the Human Interface Guidelines.

For situations where you need precise control over an animation’s behavior, use [Core Animation](../quartzcore.md) to provide hints to the system about the preferred frame rates for animations, and to control animation duration. Higher frame rates cause the system to use more power. For more information, see [Optimizing iPhone and iPad apps to support ProMotion displays](../quartzcore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays.md).

### Update views efficiently

Identify when your app updates regions of the screen by choosing Debug \> View Debugging \> Rendering \> Flash Updated Regions in Xcode while it’s running your app. Regions of your app’s display that flash — indicating a screen update — but that don’t noticably change visually indicate unnecessary screen use, and potentially unneccessary computations to prepare the update.

When you need to update a view, calculate the smallest region that needs updating and pass that to [setNeedsDisplay(_:)](<../uikit/uiview/setneedsdisplay(__).md>) (UIKit) or [setNeedsDisplay(_:)](<../appkit/nsview/setneedsdisplay(__).md>) (AppKit), so the system only updates the changed region. Avoid view layouts where updating one layer requires the system to redraw other overlapping layers.

Pay particular attention to the regions you update in views that appear under [Liquid Glass](../technologyoverviews/liquid-glass.md) effects, as the system performs additional calculations to update the Liquid Glass appearance when your app updates screen regions around the Liquid Glass effect.

### Minimize complex effects

When you adopt [Liquid Glass](../technologyoverviews/liquid-glass.md), use [GlassEffectContainer](../swiftui/glasseffectcontainer.md) to combine Liquid Glass effects in multiple views. For more information, see [Applying Liquid Glass to custom views](../swiftui/applying-liquid-glass-to-custom-views.md).

Be careful when grouping views that are spatially distant from each other, as it can cause unnecessary updates. For example, grouping two buttons that are at the top and bottom of the screen respectively means that any change in the middle of the screen causes the system to update both buttons. Use the Flash Updated Regions tool, described in [Update views efficiently](improving-your-app-s-rendering-efficiency.md#Update-views-efficiently) above, to assess screen updates due to [GlassEffectContainer](../swiftui/glasseffectcontainer.md) extents.

Prefer simple backgrounds — for example, solid colors — to complex effects like [UIVisualEffectView](../uikit/uivisualeffectview.md).

### Use recommended APIs for media playback

Where possible, use [AVPlayer](../avfoundation/avplayer.md) to play media assets, as it’s optimized to efficiently render audio and video. If you need to use lower-level APIs, measure your app’s power use, and choose the most efficient approach that supports your app’s features. For example, [AVSampleBufferDisplayLayer](../avfoundation/avsamplebufferdisplaylayer.md) typically uses less power to play a video than [CAMetalLayer](../quartzcore/cametallayer.md).

When you use [VTDecompressionSession](../videotoolbox/vtdecompressionsession-api-collection.md) to decode video frames that you display in an [AVSampleBufferDisplayLayer](../avfoundation/avsamplebufferdisplaylayer.md), pass [kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey](../corevideo/kcvpixelbufferiosurfacecoreanimationcompatibilitykey.md) as an image buffer attribute to [VTDecompressionSessionCreate(allocator:formatDescription:decoderSpecification:imageBufferAttributes:decompressionSessionOut:)](<../videotoolbox/vtdecompressionsessioncreate(allocator_formatdescription_decoderspecification_imagebufferattributes_decompressionsessionout_).md>) so that Video Toolbox chooses the most efficient pixel format:

```swift
_ = VTDecompressionSessionCreate(allocator: nil,
                                 formatDescription: formatDescription,
                                 decoderSpecification: nil,
                                 imageBufferAttributes: [kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey],
                                 decompressionSessionOut: &decompressionSession)
```

### Reduce average pixel luminance in your app

Brighter pixels use more power than darker pixels, so the lower the average pixel luminance of views in your app, the less energy the system uses powering the display. Support Dark Mode in your app and reduce the overall brightness of the display when someone enables this setting. For more information, see [Supporting Dark Mode in your interface](../uikit/supporting-dark-mode-in-your-interface.md).

Measure the average pixel luminance of views in your app using Power Profiler. For more information, see [Measuring your app’s power use with Power Profiler](measuring-your-app-s-power-use-with-power-profiler.md). Use [MXUnitAveragePixelLuminance](../metrickit/mxunitaveragepixelluminance.md) to gather metrics about the pixel luminosity.

## See Also

### Graphics and sound

- [Reducing power usage when capturing media](reducing-power-usage-when-capturing-media.md) — Optimize device camera power usage by stopping sessions when not needed and choosing appropriate video formats.
