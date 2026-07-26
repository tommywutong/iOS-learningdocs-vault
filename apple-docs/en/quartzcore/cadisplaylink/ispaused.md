---
title: isPaused
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, macOS 14.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cadisplaylink/ispaused
source_url: 'https://developer.apple.com/documentation/quartzcore/cadisplaylink/ispaused'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cadisplaylink/ispaused.json'
content_hash: 'sha256:b8ffc691bb7da245'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CADisplayLink](../cadisplaylink.md)

# isPaused

<sub>Instance Property</sub>

A Boolean value that indicates whether the system suspends the display link’s notifications to the target.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isPaused: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md). If [true](../../swift/true.md), the display link doesn’t send notifications to the target.

This property is thread safe, so you can set it from a thread separate to the one in which the display link runs.

## See Also

### Configuring a Display Link

- [duration](duration.md) — The time interval between screen refresh updates.
- [preferredFrameRateRange](preferredframeraterange.md) — A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.
- [preferredFramesPerSecond](preferredframespersecond.md) — A frequency your app prefers for frame updates, affecting how often the system invokes your delegate’s callback. _(deprecated)_
- [timestamp](timestamp.md) — The time interval that represents when the last frame displayed.
- [targetTimestamp](targettimestamp.md) — The time interval that represents when the next frame displays.
- [frameInterval](frameinterval.md) — The number of frames that must pass before the display link notifies the target again. _(deprecated)_
