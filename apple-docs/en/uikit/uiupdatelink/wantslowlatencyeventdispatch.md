---
title: wantsLowLatencyEventDispatch
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiupdatelink/wantslowlatencyeventdispatch
source_url: 'https://developer.apple.com/documentation/uikit/uiupdatelink/wantslowlatencyeventdispatch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdatelink/wantslowlatencyeventdispatch.json'
content_hash: 'sha256:f410333dce9faf24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateLink](../uiupdatelink.md)

# wantsLowLatencyEventDispatch

<sub>Instance Property</sub>

A Boolean value that determines whether the UI update link requests dispatch of low-latency eligible events.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var wantsLowLatencyEventDispatch: Bool { get set }
```

## Discussion

By default, the value of this property is [false](../../swift/false.md), which means dispatch for events that are eligible for low-latency is off.

Set the value to [true](../../swift/true.md) to request dispatch of low-latency eligible events. Only pencil events are low-latency eligible, so this behavior is primarily useful for pencil-drawing or writing apps.

Low-latency eligible events dispatch in the middle of a UI update. This timing gives an app half the amount of time to handle them as standard events. Check the value of [completionDeadlineTime](../uiupdateinfo/completiondeadlinetime.md) for the precise completion deadline time.

> [!important] Important
> If you opt in to this behavior, keep the complexity of the code you use to handle these events to a minimum. When an app requests low-latency event dispatch, but doesn’t optimize event-handling code, frames don’t submit for presentation in time. Dropped frames cause hitches and provide a suboptimal user experience. If you request dispatch of low-latency eligible events, make sure to profile your app thoroughly. For more information, read [Understanding user interface responsiveness](../../xcode/understanding-user-interface-responsiveness.md).

## See Also

### Configuring preferences

- [requiresContinuousUpdates](requirescontinuousupdates.md) — A Boolean value that determines whether the UI update link needs continuous UI updates.
- [wantsImmediatePresentation](wantsimmediatepresentation.md) — A Boolean value that determines whether the UI update link requests immediate frame presentation.
- [preferredFrameRateRange](preferredframeraterange.md) — The range of frame rates the UI update link prefers.
