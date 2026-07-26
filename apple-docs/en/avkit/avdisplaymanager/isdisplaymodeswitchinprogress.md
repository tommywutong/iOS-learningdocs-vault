---
title: isDisplayModeSwitchInProgress
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 11.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avdisplaymanager/isdisplaymodeswitchinprogress
source_url: 'https://developer.apple.com/documentation/avkit/avdisplaymanager/isdisplaymodeswitchinprogress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avdisplaymanager/isdisplaymodeswitchinprogress.json'
content_hash: 'sha256:7287a1881a43b272'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVDisplayManager](../avdisplaymanager.md)

# isDisplayModeSwitchInProgress

<sub>Instance Property</sub>

A Boolean value that indicates whether a display mode switch is in progress.

<sub>tvOS</sub>

```swift
var isDisplayModeSwitchInProgress: Bool { get }
```

## Discussion

While this property value is `true`, your app should behave as if the display is currently changing modes, and may be temporarily blank. The accuracy of this property value depends on the TV hardware and the nature of the mode switch. When displaying temporary content or user interface elements, such as hints or tips, leave them visible for longer than the mode switch takes, to ensure the user sees them.

This property is key-value observable.

## See Also

### Matching a Video’s Native Display Mode

- [preferredDisplayCriteria](preferreddisplaycriteria.md) — A hint for the TV to set the display mode to best match the currently playing content’s display criteria.
- [displayCriteriaMatchingEnabled](isdisplaycriteriamatchingenabled.md) — A Boolean value that indicates whether the user has enabled display critera matching.
