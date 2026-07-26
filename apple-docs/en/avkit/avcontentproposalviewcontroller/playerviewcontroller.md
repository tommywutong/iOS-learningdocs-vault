---
title: playerViewController
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcontentproposalviewcontroller/playerviewcontroller
source_url: 'https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/playerviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontentproposalviewcontroller/playerviewcontroller.json'
content_hash: 'sha256:d7596b3bd3a3fbb0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVContentProposalViewController](../avcontentproposalviewcontroller.md)

# playerViewController

<sub>Instance Property</sub>

The player view controller that presents a content proposal.

<sub>tvOS</sub>

```swift
weak var playerViewController: AVPlayerViewController? { get }
```

## Discussion

The framework sets this property value during the presentation of the content proposal. It may be `nil` at other times.
