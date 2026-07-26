---
title: contentTimeForTransition
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcontentproposal/contenttimefortransition
source_url: 'https://developer.apple.com/documentation/avkit/avcontentproposal/contenttimefortransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontentproposal/contenttimefortransition.json'
content_hash: 'sha256:b044fe04d6c180c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVContentProposal](../avcontentproposal.md)

# contentTimeForTransition

<sub>Instance Property</sub>

The time within the timeline of the current player item when the content proposal presentation should begin.

<sub>tvOS</sub>

```swift
var contentTimeForTransition: CMTime { get }
```

## Discussion

The time value commonly marks the beginning of the end credits in a television show or movie. For other content, this may be at the very end of the video. The default value, [indefinite](../../coremedia/cmtime/indefinite.md), indicates that the transition should occur at the very end of the current player item’s end time; this is equivalent to using the duration of the asset.

## See Also

### Configuring the Content Proposal

- [title](title.md) — The title of the proposed content.
- [previewImage](previewimage.md) — The preview image of the proposed item.
- [metadata](metadata.md) — Optional custom metadata associated with the proposed item.
- [automaticAcceptanceInterval](automaticacceptanceinterval.md) — The interval between the time playback ends and automatic acceptance of this content proposal.
- [URL](url.md) — The URL of the proposed content.
