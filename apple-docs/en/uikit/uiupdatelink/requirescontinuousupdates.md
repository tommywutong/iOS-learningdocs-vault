---
title: requiresContinuousUpdates
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiupdatelink/requirescontinuousupdates
source_url: 'https://developer.apple.com/documentation/uikit/uiupdatelink/requirescontinuousupdates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdatelink/requirescontinuousupdates.json'
content_hash: 'sha256:ee76c3af2b3b7f15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateLink](../uiupdatelink.md)

# requiresContinuousUpdates

<sub>Instance Property</sub>

A Boolean value that determines whether the UI update link needs continuous UI updates.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var requiresContinuousUpdates: Bool { get set }
```

## Discussion

By default, the value of this property is [false](../../swift/false.md), which means the UI update link acts as a passive observer of UI updates. The system only calls its actions while producing a UI update in response to some kind of event, such as a gesture or layer change.

Set the value to [true](../../swift/true.md) to request that the system produces UI updates continuously. You might opt in to this behavior if you want your actions to run at consistent intervals regardless of other input to the system.

## See Also

### Configuring preferences

- [wantsLowLatencyEventDispatch](wantslowlatencyeventdispatch.md) — A Boolean value that determines whether the UI update link requests dispatch of low-latency eligible events.
- [wantsImmediatePresentation](wantsimmediatepresentation.md) — A Boolean value that determines whether the UI update link requests immediate frame presentation.
- [preferredFrameRateRange](preferredframeraterange.md) — The range of frame rates the UI update link prefers.
