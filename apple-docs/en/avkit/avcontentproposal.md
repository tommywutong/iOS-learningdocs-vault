---
title: AVContentProposal
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [tvOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcontentproposal
source_url: 'https://developer.apple.com/documentation/avkit/avcontentproposal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontentproposal.json'
content_hash: 'sha256:d162e0eb22c897b8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVContentProposal

<sub>Class</sub>

An object that describes the content to propose playing after the current item finishes.

<sub>tvOS</sub>

```swift
class AVContentProposal
```

## Overview

A content proposal object models the data about the proposed content such as its title, preview image, presentation time, and content URL. You make a content proposal eligible for presentation by setting it as the [nextContentProposal](../avfoundation/avplayeritem/nextcontentproposal.md) of the current [AVPlayerItem](../avfoundation/avplayeritem.md).

```swift
let proposal = AVContentProposal(contentTimeForTransition: time,
                                 title: title,
                                 previewImage: image)
// Set the proposal as the nextContentProposal of the current player item
currentPlayerItem.nextContentProposal = proposal
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Content Proposal

- [- initWithContentTimeForTransition:title:previewImage:](<avcontentproposal/init(contenttimefortransition_title_previewimage_).md>) — Creates a new content proposal with the specified transition time, title, and preview image.

### Configuring the Content Proposal

- [contentTimeForTransition](avcontentproposal/contenttimefortransition.md) — The time within the timeline of the current player item when the content proposal presentation should begin.
- [title](avcontentproposal/title.md) — The title of the proposed content.
- [previewImage](avcontentproposal/previewimage.md) — The preview image of the proposed item.
- [metadata](avcontentproposal/metadata.md) — Optional custom metadata associated with the proposed item.
- [automaticAcceptanceInterval](avcontentproposal/automaticacceptanceinterval.md) — The interval between the time playback ends and automatic acceptance of this content proposal.
- [URL](avcontentproposal/url.md) — The URL of the proposed content.

## See Also

### Configuring the Proposal

- [contentProposal](avcontentproposalviewcontroller/contentproposal.md) — A prosal of content to play.
- [dateOfAutomaticAcceptance](avcontentproposalviewcontroller/dateofautomaticacceptance.md) — The date that the system automatically accepts a proposal if the user doesn’t intervene.
- [playerLayoutGuide](avcontentproposalviewcontroller/playerlayoutguide.md) — A layout guide that tracks the size and location of the player view.
- [preferredPlayerViewFrame](avcontentproposalviewcontroller/preferredplayerviewframe.md) — The preferred presentation frame of the player view while the content proposal is active.
