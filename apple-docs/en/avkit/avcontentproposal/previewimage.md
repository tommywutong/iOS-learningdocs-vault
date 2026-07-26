---
title: previewImage
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcontentproposal/previewimage
source_url: 'https://developer.apple.com/documentation/avkit/avcontentproposal/previewimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontentproposal/previewimage.json'
content_hash: 'sha256:4ee69ecc4deb7b41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVContentProposal](../avcontentproposal.md)

# previewImage

<sub>Instance Property</sub>

The preview image of the proposed item.

<sub>tvOS</sub>

```swift
var previewImage: UIImage? { get }
```

## Discussion

The preview image you provide should typically be a frame from the proposed video, not the poster artwork.

## See Also

### Configuring the Content Proposal

- [contentTimeForTransition](contenttimefortransition.md) — The time within the timeline of the current player item when the content proposal presentation should begin.
- [title](title.md) — The title of the proposed content.
- [metadata](metadata.md) — Optional custom metadata associated with the proposed item.
- [automaticAcceptanceInterval](automaticacceptanceinterval.md) — The interval between the time playback ends and automatic acceptance of this content proposal.
- [URL](url.md) — The URL of the proposed content.
