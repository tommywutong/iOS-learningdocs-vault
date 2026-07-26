---
title: 'playerViewController(_:didReject:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 10.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:didreject:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:didreject:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller%28_%3Adidreject%3A%29.json'
content_hash: 'sha256:c034bed1559619b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewController(_:didReject:)

<sub>Instance Method</sub>

Tells the delegate when the user rejects the proposed content.

<sub>tvOS</sub>

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, didReject proposal: AVContentProposal)
```

## Parameters

- `playerViewController` — The player view controller.

- `proposal` — The content proposal.

## See Also

### Responding to Content Proposals

- [- playerViewController:shouldPresentContentProposal:](<playerviewcontroller(__shouldpresent_).md>) — Asks the delegate whether the player view controller presents a content proposal.
- [- playerViewController:didAcceptContentProposal:](<playerviewcontroller(__didaccept_).md>) — Tells the delegate when the user accepts the proposed content.
