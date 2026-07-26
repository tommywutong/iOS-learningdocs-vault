---
title: 'playerViewController(_:didAccept:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 10.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:didaccept:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:didaccept:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller%28_%3Adidaccept%3A%29.json'
content_hash: 'sha256:595bae580f29900d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewController(_:didAccept:)

<sub>Instance Method</sub>

Tells the delegate when the user accepts the proposed content.

<sub>tvOS</sub>

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, didAccept proposal: AVContentProposal)
```

## Parameters

- `playerViewController` — The player view controller.

- `proposal` — The content proposal.

## Discussion

Implement this method to replace the player’s current player item with a player item for the proposed content.

## See Also

### Responding to Content Proposals

- [- playerViewController:shouldPresentContentProposal:](<playerviewcontroller(__shouldpresent_).md>) — Asks the delegate whether the player view controller presents a content proposal.
- [- playerViewController:didRejectContentProposal:](<playerviewcontroller(__didreject_).md>) — Tells the delegate when the user rejects the proposed content.
