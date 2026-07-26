---
title: wantsImmediatePresentation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiupdatelink/wantsimmediatepresentation
source_url: 'https://developer.apple.com/documentation/uikit/uiupdatelink/wantsimmediatepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdatelink/wantsimmediatepresentation.json'
content_hash: 'sha256:cf21352c5ce209bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateLink](../uiupdatelink.md)

# wantsImmediatePresentation

<sub>Instance Property</sub>

A Boolean value that determines whether the UI update link requests immediate frame presentation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var wantsImmediatePresentation: Bool { get set }
```

## Discussion

By default, the value of this property is [false](../../swift/false.md).

When the value of this property is [true](../../swift/true.md), the system requests immediate rendering of the display frame after the last [CATransaction](../../quartzcore/catransaction.md) commit for the current UI update. Opting in to this behavior can help reduce latency between input and display because the rendered display frame presents one frame duration sooner. This behavior is primarily useful for pencil-drawing apps where low input-to-display latency is critical for an optimal user experience.

> [!important] Important
> If you opt in to this behavior, keep the complexity of the code you submit to the render server to a minimum. When an app requests immediate frame presentation, but doesn’t keep rendering complexity minimal, frames don’t submit for presentation in time. Dropped frames cause hitches and provide a suboptimal user experience. If you request immediate presentation, make sure to profile your app thoroughly. For more information, read [Understanding user interface responsiveness](../../xcode/understanding-user-interface-responsiveness.md).

## See Also

### Configuring preferences

- [requiresContinuousUpdates](requirescontinuousupdates.md) — A Boolean value that determines whether the UI update link needs continuous UI updates.
- [wantsLowLatencyEventDispatch](wantslowlatencyeventdispatch.md) — A Boolean value that determines whether the UI update link requests dispatch of low-latency eligible events.
- [preferredFrameRateRange](preferredframeraterange.md) — The range of frame rates the UI update link prefers.
