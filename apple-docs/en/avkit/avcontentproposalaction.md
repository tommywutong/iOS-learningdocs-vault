---
title: AVContentProposalAction
framework: AVKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcontentproposalaction
source_url: 'https://developer.apple.com/documentation/avkit/avcontentproposalaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontentproposalaction.json'
content_hash: 'sha256:baf78e6016cf73a0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVContentProposalAction

<sub>Enumeration</sub>

Constant that indicate the action a user takes when dismissing a content proposal.

<sub>tvOS</sub>

```swift
enum AVContentProposalAction
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an action

- [init(rawValue:)](<avcontentproposalaction/init(rawvalue_).md>)

### Actions

- [AVContentProposalActionAccept](avcontentproposalaction/accept.md) — The user accepted the content proposal.
- [AVContentProposalActionReject](avcontentproposalaction/reject.md) — The user rejected the content proposal.
- [AVContentProposalActionDefer](avcontentproposalaction/defer.md) — The user deferred the content proposal.

## See Also

### Dismissing the Proposal

- [- dismissContentProposalForAction:animated:completion:](<avcontentproposalviewcontroller/dismisscontentproposal(for_animated_completion_).md>) — Dismisses the current content proposal.
