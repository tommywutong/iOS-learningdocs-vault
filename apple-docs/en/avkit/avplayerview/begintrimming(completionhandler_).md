---
title: 'beginTrimming(completionHandler:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerview/begintrimming(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/begintrimming(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/begintrimming%28completionhandler%3A%29.json'
content_hash: 'sha256:b63f81b00a297544'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# beginTrimming(completionHandler:)

<sub>Instance Method</sub>

Puts the player view into trimming mode.

<sub>macOS</sub>

```swift
func beginTrimming(completionHandler handler: (@Sendable (AVPlayerViewTrimResult) -> Void)? = nil)
```

<sub>macOS</sub>

```swift
func beginTrimming() async -> AVPlayerViewTrimResult
```

## Parameters

- `handler` — The callback the system invokes when the user selects the Trim or Cancel button in the trimming UI. The result passed to the closure indicates whether the user clicked the Trim or Cancel button.

## Discussion

An example implementation of the handler block is as follows:

```swift
@IBAction func beginTrimming(_ sender: AnyObject) {
    playerView.beginTrimming { result in
        if result == .okButton {
            // user selected Trim button (AVPlayerViewTrimResult.okButton)...
        } else {
            // user selected Cancel button (AVPlayerViewTrimResult.cancelButton)...
        }
    }
}
```

This method blocks until the user selects either the Trim or the Cancel button.

## See Also

### Trimming media

- [canBeginTrimming](canbegintrimming.md) — A Boolean value that indicates whether the player view can begin trimming.
- [AVPlayerViewTrimResult](../avplayerviewtrimresult.md) — Constants that specify an action a user takes when trimming media in a player view.
