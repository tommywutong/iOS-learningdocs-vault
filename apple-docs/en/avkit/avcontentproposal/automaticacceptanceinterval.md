---
title: automaticAcceptanceInterval
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcontentproposal/automaticacceptanceinterval
source_url: 'https://developer.apple.com/documentation/avkit/avcontentproposal/automaticacceptanceinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontentproposal/automaticacceptanceinterval.json'
content_hash: 'sha256:ce704bb4d6803594'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVContentProposal](../avcontentproposal.md)

# automaticAcceptanceInterval

<sub>Instance Property</sub>

The interval between the time playback ends and automatic acceptance of this content proposal.

<sub>tvOS</sub>

```swift
var automaticAcceptanceInterval: TimeInterval { get set }
```

## Discussion

The content proposal displays a countdown timer to reflect this value. Set this value to [nan](../../swift/double/nan.md) to disable the default, which is automatic acceptance.

## See Also

### Configuring the Content Proposal

- [contentTimeForTransition](contenttimefortransition.md) — The time within the timeline of the current player item when the content proposal presentation should begin.
- [title](title.md) — The title of the proposed content.
- [previewImage](previewimage.md) — The preview image of the proposed item.
- [metadata](metadata.md) — Optional custom metadata associated with the proposed item.
- [URL](url.md) — The URL of the proposed content.
