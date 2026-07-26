---
title: isDisplayCriteriaMatchingEnabled
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 11.3+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avdisplaymanager/isdisplaycriteriamatchingenabled
source_url: 'https://developer.apple.com/documentation/avkit/avdisplaymanager/isdisplaycriteriamatchingenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avdisplaymanager/isdisplaycriteriamatchingenabled.json'
content_hash: 'sha256:605fcf3864b6df2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVDisplayManager](../avdisplaymanager.md)

# isDisplayCriteriaMatchingEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the user has enabled display critera matching.

<sub>tvOS, visionOS</sub>

```swift
var isDisplayCriteriaMatchingEnabled: Bool { get }
```

## Discussion

This value reflects the user’s current Match Content settings, which they set in the Settings app under Video and Audio \> Match Content.

## See Also

### Matching a Video’s Native Display Mode

- [preferredDisplayCriteria](preferreddisplaycriteria.md) — A hint for the TV to set the display mode to best match the currently playing content’s display criteria.
- [displayModeSwitchInProgress](isdisplaymodeswitchinprogress.md) — A Boolean value that indicates whether a display mode switch is in progress.
