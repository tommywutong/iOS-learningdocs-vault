---
title: preferredDisplayCriteria
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 11.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avdisplaymanager/preferreddisplaycriteria
source_url: 'https://developer.apple.com/documentation/avkit/avdisplaymanager/preferreddisplaycriteria'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avdisplaymanager/preferreddisplaycriteria.json'
content_hash: 'sha256:5cb0d29014cf3d5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVDisplayManager](../avdisplaymanager.md)

# preferredDisplayCriteria

<sub>Instance Property</sub>

A hint for the TV to set the display mode to best match the currently playing content’s display criteria.

<sub>tvOS, visionOS</sub>

```swift
@NSCopying var preferredDisplayCriteria: AVDisplayCriteria? { get set }
```

## Discussion

The display manager uses the preferred display criteria only when user settings allow. Set this property to `nil` to allow the system to guide you to a display mode that’s suitable for a wide range of video and nonvideo content.

## See Also

### Matching a Video’s Native Display Mode

- [displayCriteriaMatchingEnabled](isdisplaycriteriamatchingenabled.md) — A Boolean value that indicates whether the user has enabled display critera matching.
- [displayModeSwitchInProgress](isdisplaymodeswitchinprogress.md) — A Boolean value that indicates whether a display mode switch is in progress.
