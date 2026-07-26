---
title: preferredPlayerViewFrame
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcontentproposalviewcontroller/preferredplayerviewframe
source_url: 'https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/preferredplayerviewframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontentproposalviewcontroller/preferredplayerviewframe.json'
content_hash: 'sha256:12efcc887672c3af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVContentProposalViewController](../avcontentproposalviewcontroller.md)

# preferredPlayerViewFrame

<sub>Instance Property</sub>

The preferred presentation frame of the player view while the content proposal is active.

<sub>tvOS</sub>

```swift
var preferredPlayerViewFrame: CGRect { get }
```

## Discussion

This value defaults to a rectangle that represents the entire screen bounds, but custom view controllers may return a smaller rectangle, or [zero](../../corefoundation/cgrect/zero.md) to hide the player view completely. If you return a rectangle smaller that the full-screen bounds, the player view animates its frame to its new size and position.

## See Also

### Configuring the Proposal

- [contentProposal](contentproposal.md) — A prosal of content to play.
- [AVContentProposal](../avcontentproposal.md) — An object that describes the content to propose playing after the current item finishes.
- [dateOfAutomaticAcceptance](dateofautomaticacceptance.md) — The date that the system automatically accepts a proposal if the user doesn’t intervene.
- [playerLayoutGuide](playerlayoutguide.md) — A layout guide that tracks the size and location of the player view.
