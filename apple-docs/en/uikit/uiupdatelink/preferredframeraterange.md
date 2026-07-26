---
title: preferredFrameRateRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiupdatelink/preferredframeraterange
source_url: 'https://developer.apple.com/documentation/uikit/uiupdatelink/preferredframeraterange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdatelink/preferredframeraterange.json'
content_hash: 'sha256:0ed98a681ef44973'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateLink](../uiupdatelink.md)

# preferredFrameRateRange

<sub>Instance Property</sub>

The range of frame rates the UI update link prefers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredFrameRateRange: CAFrameRateRange { get set }
```

## Discussion

By default, the value of this property is [default](../../quartzcore/caframeraterange/default.md), which doesn’t request any specific frame rate range.

## See Also

### Configuring preferences

- [requiresContinuousUpdates](requirescontinuousupdates.md) — A Boolean value that determines whether the UI update link needs continuous UI updates.
- [wantsLowLatencyEventDispatch](wantslowlatencyeventdispatch.md) — A Boolean value that determines whether the UI update link requests dispatch of low-latency eligible events.
- [wantsImmediatePresentation](wantsimmediatepresentation.md) — A Boolean value that determines whether the UI update link requests immediate frame presentation.
