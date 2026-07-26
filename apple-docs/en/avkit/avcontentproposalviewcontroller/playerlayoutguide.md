---
title: playerLayoutGuide
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcontentproposalviewcontroller/playerlayoutguide
source_url: 'https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/playerlayoutguide'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontentproposalviewcontroller/playerlayoutguide.json'
content_hash: 'sha256:773081d1d3b94a35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVContentProposalViewController](../avcontentproposalviewcontroller.md)

# playerLayoutGuide

<sub>Instance Property</sub>

A layout guide that tracks the size and location of the player view.

<sub>tvOS</sub>

```swift
var playerLayoutGuide: UILayoutGuide { get }
```

## Discussion

The view controller can constrain its views using the anchors of the player layout guide, which has the same size and position as the player view. The layout guide is always relative to the current [preferredPlayerViewFrame](preferredplayerviewframe.md) property value.

## See Also

### Configuring the Proposal

- [contentProposal](contentproposal.md) — A prosal of content to play.
- [AVContentProposal](../avcontentproposal.md) — An object that describes the content to propose playing after the current item finishes.
- [dateOfAutomaticAcceptance](dateofautomaticacceptance.md) — The date that the system automatically accepts a proposal if the user doesn’t intervene.
- [preferredPlayerViewFrame](preferredplayerviewframe.md) — The preferred presentation frame of the player view while the content proposal is active.
