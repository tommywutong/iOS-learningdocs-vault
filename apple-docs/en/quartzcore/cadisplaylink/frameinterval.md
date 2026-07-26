---
title: frameInterval
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.1+（10.0 起废弃）, iPadOS 3.1+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（10.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/quartzcore/cadisplaylink/frameinterval
source_url: 'https://developer.apple.com/documentation/quartzcore/cadisplaylink/frameinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cadisplaylink/frameinterval.json'
content_hash: 'sha256:9f357e5d58d68cb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CADisplayLink](../cadisplaylink.md)

# frameInterval

<sub>Instance Property</sub>

The number of frames that must pass before the display link notifies the target again.

> [!warning] Deprecated
> Use [preferredFramesPerSecond](preferredframespersecond.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var frameInterval: Int { get set }
```

## Discussion

The default value is `1`, which results in the system notifying your app at the refresh rate of the display. If you set the value to a value greater than `1`, the display link notifies your app at a fraction of the native refresh rate. For example, setting the interval to `2` causes the display link to fire every other frame, providing half the frame rate.

Setting this value to less than `1` results in undefined behavior and is a programmer error.

## See Also

### Configuring a Display Link

- [duration](duration.md) — The time interval between screen refresh updates.
- [preferredFrameRateRange](preferredframeraterange.md) — A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.
- [preferredFramesPerSecond](preferredframespersecond.md) — A frequency your app prefers for frame updates, affecting how often the system invokes your delegate’s callback. _(deprecated)_
- [paused](ispaused.md) — A Boolean value that indicates whether the system suspends the display link’s notifications to the target.
- [timestamp](timestamp.md) — The time interval that represents when the last frame displayed.
- [targetTimestamp](targettimestamp.md) — The time interval that represents when the next frame displays.
