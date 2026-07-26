---
title: duration
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, macOS 14.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cadisplaylink/duration
source_url: 'https://developer.apple.com/documentation/quartzcore/cadisplaylink/duration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cadisplaylink/duration.json'
content_hash: 'sha256:e200c165bdf1e6c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CADisplayLink](../cadisplaylink.md)

# duration

<sub>Instance Property</sub>

The time interval between screen refresh updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var duration: CFTimeInterval { get }
```

## Discussion

This value is in an undefined state until the system calls the target’s selector at least once.

You calculate the expected amount of time your app has to render each frame by using [targetTimestamp](targettimestamp.md)-[timestamp](timestamp.md). Use [targetTimestamp](targettimestamp.md)-[CACurrentMediaTime](<../cacurrentmediatime().md>) to calculate the actual amount of time.

## See Also

### Configuring a Display Link

- [preferredFrameRateRange](preferredframeraterange.md) — A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.
- [preferredFramesPerSecond](preferredframespersecond.md) — A frequency your app prefers for frame updates, affecting how often the system invokes your delegate’s callback. _(deprecated)_
- [paused](ispaused.md) — A Boolean value that indicates whether the system suspends the display link’s notifications to the target.
- [timestamp](timestamp.md) — The time interval that represents when the last frame displayed.
- [targetTimestamp](targettimestamp.md) — The time interval that represents when the next frame displays.
- [frameInterval](frameinterval.md) — The number of frames that must pass before the display link notifies the target again. _(deprecated)_
