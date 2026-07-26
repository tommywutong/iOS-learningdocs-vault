---
title: contentProposal
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcontentproposalviewcontroller/contentproposal
source_url: 'https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/contentproposal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontentproposalviewcontroller/contentproposal.json'
content_hash: 'sha256:9846edf479ecd6fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVContentProposalViewController](../avcontentproposalviewcontroller.md)

# contentProposal

<sub>Instance Property</sub>

A prosal of content to play.

<sub>tvOS</sub>

```swift
var contentProposal: AVContentProposal? { get }
```

## Discussion

The associated player view controller sets this property value.

## See Also

### Configuring the Proposal

- [AVContentProposal](../avcontentproposal.md) — An object that describes the content to propose playing after the current item finishes.
- [dateOfAutomaticAcceptance](dateofautomaticacceptance.md) — The date that the system automatically accepts a proposal if the user doesn’t intervene.
- [playerLayoutGuide](playerlayoutguide.md) — A layout guide that tracks the size and location of the player view.
- [preferredPlayerViewFrame](preferredplayerviewframe.md) — The preferred presentation frame of the player view while the content proposal is active.
