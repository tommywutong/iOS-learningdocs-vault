---
title: 'playerViewController(_:didSelect:in:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 9.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:didselect:in:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:didselect:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller%28_%3Adidselect%3Ain%3A%29.json'
content_hash: 'sha256:4ab8105aeb4e89cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewController(_:didSelect:in:)

<sub>Instance Method</sub>

Tells the delegate when the user selects a media option from a media selection group.

<sub>tvOS</sub>

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, didSelect mediaSelectionOption: AVMediaSelectionOption?, in mediaSelectionGroup: AVMediaSelectionGroup)
```

## Parameters

- `playerViewController` — The player view controller.

- `mediaSelectionOption` — The user’s selected media option, which may be `nil`.

- `mediaSelectionGroup` — The media selection group in which the selected media option exists.
