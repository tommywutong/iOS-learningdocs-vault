---
title: calibratedLatency
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/calibratedlatency
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/calibratedlatency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/calibratedlatency.json'
content_hash: 'sha256:591ef419df728787'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# calibratedLatency

<sub>Instance Property</sub>

The user-calibrated latency for the current screen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var calibratedLatency: CFTimeInterval { get }
```

## Discussion

Use this property when you need to manually synchronize video playback with custom audio. For example, you might correlate this value with the [latency](../../audiotoolbox/auaudiounit/latency.md) property of a Core Audio unit when writing custom video-playback software. The value of this property is `0` until the user explicitly calibrates their display.
