---
title: Reducing power usage when capturing media
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/reducing-power-usage-when-capturing-media
source_url: 'https://developer.apple.com/documentation/xcode/reducing-power-usage-when-capturing-media'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/reducing-power-usage-when-capturing-media.json'
content_hash: 'sha256:38a061ec481f7e3a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Performance and metrics](performance-and-metrics.md) · [Reducing your app’s battery use](reducing-your-app-s-battery-use.md)

# Reducing power usage when capturing media

<sub>Article</sub>

Optimize device camera power usage by stopping sessions when not needed and choosing appropriate video formats.

## Overview

Device cameras draw a lot of power when they’re in use. To minimize the amount of time your app uses the device camera, run an [AVCaptureSession](../avfoundation/avcapturesession.md) only while your app is using the captured data, and call [stopRunning()](<../avfoundation/avcapturesession/stoprunning().md>) at the earliest opportunity. For example, stop the capture session if your app’s camera view is covered by other content, so that the device stops capturing the camera stream when someone can’t see it.

Because capturing higher-quality images consumes more power, set the capture device’s [activeFormat](../avfoundation/avcapturedevice/activeformat.md) to the format with the lowest image quality that supports your app’s features. Confirm that the [isVideoBinned](../avfoundation/avcapturedevice/format/isvideobinned.md) property is `true` for the format you use, as pixel binning also increases the power efficiency.

## See Also

### Graphics and sound

- [Improving your app’s rendering efficiency](improving-your-app-s-rendering-efficiency.md) — Optimize view updates by minimizing unnecessary redraws and using efficient update strategies.
