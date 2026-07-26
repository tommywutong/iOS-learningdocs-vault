---
title: dateOfAutomaticAcceptance
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcontentproposalviewcontroller/dateofautomaticacceptance
source_url: 'https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/dateofautomaticacceptance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontentproposalviewcontroller/dateofautomaticacceptance.json'
content_hash: 'sha256:d3958c052cce8b72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVContentProposalViewController](../avcontentproposalviewcontroller.md)

# dateOfAutomaticAcceptance

<sub>Instance Property</sub>

The date that the system automatically accepts a proposal if the user doesn’t intervene.

<sub>tvOS</sub>

```swift
var dateOfAutomaticAcceptance: Date? { get set }
```

## Discussion

The system schedules the proposal when you present it, and may unschedule it if the user cancels automatic acceptance, manually accepts, or otherwise dismisses the proposal.

Set this property to `nil` to cancel automatic acceptance.

## See Also

### Configuring the Proposal

- [contentProposal](contentproposal.md) — A prosal of content to play.
- [AVContentProposal](../avcontentproposal.md) — An object that describes the content to propose playing after the current item finishes.
- [playerLayoutGuide](playerlayoutguide.md) — A layout guide that tracks the size and location of the player view.
- [preferredPlayerViewFrame](preferredplayerviewframe.md) — The preferred presentation frame of the player view while the content proposal is active.
