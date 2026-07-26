---
title: 'playerViewController(_:shouldPresent:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 10.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:shouldpresent:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:shouldpresent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller%28_%3Ashouldpresent%3A%29.json'
content_hash: 'sha256:3859b53c4543d594'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewController(_:shouldPresent:)

<sub>Instance Method</sub>

Asks the delegate whether the player view controller presents a content proposal.

<sub>tvOS</sub>

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, shouldPresent proposal: AVContentProposal) -> Bool
```

## Parameters

- `playerViewController` — The player view controller.

- `proposal` — The content proposal to present.

## Return Value

`true` if the player view controller should propose the content; otherwise `false`.

## See Also

### Responding to Content Proposals

- [- playerViewController:didAcceptContentProposal:](<playerviewcontroller(__didaccept_).md>) — Tells the delegate when the user accepts the proposed content.
- [- playerViewController:didRejectContentProposal:](<playerviewcontroller(__didreject_).md>) — Tells the delegate when the user rejects the proposed content.
