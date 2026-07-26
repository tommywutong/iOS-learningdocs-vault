---
title: url
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcontentproposal/url
source_url: 'https://developer.apple.com/documentation/avkit/avcontentproposal/url'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontentproposal/url.json'
content_hash: 'sha256:bd7574d50fc6e219'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVContentProposal](../avcontentproposal.md)

# url

<sub>Instance Property</sub>

The URL of the proposed content.

<sub>tvOS</sub>

```swift
var url: URL? { get set }
```

## Discussion

Use this property value to initialize a new [AVPlayerItem](../../avfoundation/avplayeritem.md) to play when the user accepts the content proposal. If the value of this property is `nil`, the [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md) must handle the content proposal acceptance.

## See Also

### Configuring the Content Proposal

- [contentTimeForTransition](contenttimefortransition.md) — The time within the timeline of the current player item when the content proposal presentation should begin.
- [title](title.md) — The title of the proposed content.
- [previewImage](previewimage.md) — The preview image of the proposed item.
- [metadata](metadata.md) — Optional custom metadata associated with the proposed item.
- [automaticAcceptanceInterval](automaticacceptanceinterval.md) — The interval between the time playback ends and automatic acceptance of this content proposal.
