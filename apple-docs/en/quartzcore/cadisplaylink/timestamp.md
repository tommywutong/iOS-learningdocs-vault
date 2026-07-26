---
title: timestamp
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, macOS 14.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cadisplaylink/timestamp
source_url: 'https://developer.apple.com/documentation/quartzcore/cadisplaylink/timestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cadisplaylink/timestamp.json'
content_hash: 'sha256:a81e80f4503d5906'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CADisplayLink](../cadisplaylink.md)

# timestamp

<sub>Instance Property</sub>

The time interval that represents when the last frame displayed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var timestamp: CFTimeInterval { get }
```

## Discussion

If you need to calculate what to display next, use [targetTimestamp](targettimestamp.md) instead.

## See Also

### Configuring a Display Link

- [duration](duration.md) — The time interval between screen refresh updates.
- [preferredFrameRateRange](preferredframeraterange.md) — A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.
- [preferredFramesPerSecond](preferredframespersecond.md) — A frequency your app prefers for frame updates, affecting how often the system invokes your delegate’s callback. _(deprecated)_
- [paused](ispaused.md) — A Boolean value that indicates whether the system suspends the display link’s notifications to the target.
- [targetTimestamp](targettimestamp.md) — The time interval that represents when the next frame displays.
- [frameInterval](frameinterval.md) — The number of frames that must pass before the display link notifies the target again. _(deprecated)_
