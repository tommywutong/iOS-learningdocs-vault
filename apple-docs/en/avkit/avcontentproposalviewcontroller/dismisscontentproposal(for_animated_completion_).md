---
title: 'dismissContentProposal(for:animated:completion:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avcontentproposalviewcontroller/dismisscontentproposal(for:animated:completion:)'
source_url: 'https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller/dismisscontentproposal(for:animated:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontentproposalviewcontroller/dismisscontentproposal%28for%3Aanimated%3Acompletion%3A%29.json'
content_hash: 'sha256:2d7480dead9bc872'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVContentProposalViewController](../avcontentproposalviewcontroller.md)

# dismissContentProposal(for:animated:completion:)

<sub>Instance Method</sub>

Dismisses the current content proposal.

<sub>tvOS</sub>

```swift
func dismissContentProposal(for action: AVContentProposalAction, animated: Bool, completion block: (() -> Void)? = nil)
```

<sub>tvOS</sub>

```swift
func dismissContentProposal(for action: AVContentProposalAction, animated: Bool) async
```

## Parameters

- `action` — A content proposal action that indicates whether the user accepted, rejected, or deferred the content proposal.

- `animated` — A Boolean value that indicates whether the content proposal dismisses in an animated manner.

- `block` — An optional callback that the system calls when its hidden the conten proposal.

## Discussion

Call this method to indicate the user action when leaving this proposal.

## See Also

### Dismissing the Proposal

- [AVContentProposalAction](../avcontentproposalaction.md) — Constant that indicate the action a user takes when dismissing a content proposal.
