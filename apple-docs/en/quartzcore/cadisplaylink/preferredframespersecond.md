---
title: preferredFramesPerSecond
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+（27.0 起废弃）, iPadOS 10.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 10.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/quartzcore/cadisplaylink/preferredframespersecond
source_url: 'https://developer.apple.com/documentation/quartzcore/cadisplaylink/preferredframespersecond'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cadisplaylink/preferredframespersecond.json'
content_hash: 'sha256:b0b499d8b25a8516'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CADisplayLink](../cadisplaylink.md)

# preferredFramesPerSecond

<sub>Instance Property</sub>

A frequency your app prefers for frame updates, affecting how often the system invokes your delegate’s callback.

> [!warning] Deprecated
> Use [preferredFrameRateRange](preferredframeraterange.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredFramesPerSecond: Int { get set }
```

## Discussion

The display link makes a best attempt to invoke your app’s callback at the frequency value you set to this property. However, the system also takes into account the device’s hardware capabilities and the other tasks your game or app is running.

> [!important] Important
> Choose a frame rate that your app can consistently maintain.

In iOS 15 and later, the system can change the available range of frame rates because it factors in system policies and a person’s preferences. For example, Low Power Mode, critical thermal state, and accessibility settings can affect the system’s frame rate.

The system typically provides a consistent frame rate by choosing one that’s a factor of the display’s maximum refresh rate. For example, a display link could invoke your callback 60 times per second for a display with a refresh rate of 60 hertz. However, the display link could invoke your callback less frequently, such as 30, 20, or 15 times per second, by setting a smaller value.

> [!note] Note
> The property defaults to `0`, which is equivalent to the display’s maximum refresh rate, such as a [UIScreen](../../uikit/uiscreen.md) instance’s [maximumFramesPerSecond](../../uikit/uiscreen/maximumframespersecond.md) property.

For more information, see [Optimizing iPhone and iPad apps to support ProMotion displays](../optimizing-iphone-and-ipad-apps-to-support-promotion-displays.md).

## See Also

### Configuring a Display Link

- [duration](duration.md) — The time interval between screen refresh updates.
- [preferredFrameRateRange](preferredframeraterange.md) — A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.
- [paused](ispaused.md) — A Boolean value that indicates whether the system suspends the display link’s notifications to the target.
- [timestamp](timestamp.md) — The time interval that represents when the last frame displayed.
- [targetTimestamp](targettimestamp.md) — The time interval that represents when the next frame displays.
- [frameInterval](frameinterval.md) — The number of frames that must pass before the display link notifies the target again. _(deprecated)_
