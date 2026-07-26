---
title: canBeginTrimming
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerview/canbegintrimming
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/canbegintrimming'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/canbegintrimming.json'
content_hash: 'sha256:76e17b838c596fcd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# canBeginTrimming

<sub>Instance Property</sub>

A Boolean value that indicates whether the player view can begin trimming.

<sub>macOS</sub>

```swift
var canBeginTrimming: Bool { get }
```

## Discussion

Before calling [- beginTrimmingWithCompletionHandler:](<begintrimming(completionhandler_).md>), check the value of this property to determine whether the player view and current media support trimming. This property value is `false` if the current controls style doesn’t support trimming, the media is content protected, or when playing HTTP Live Streaming media.

If you’re presenting a menu item to initiate trimming, a good place to perform this check is in the [validateUserInterfaceItem(_:)](<../../appkit/nsdocument/validateuserinterfaceitem(__).md>) method of [NSDocument](../../appkit/nsdocument.md):

```swift
override func validateUserInterfaceItem(_ item: NSValidatedUserInterfaceItem) -> Bool {
    if item.action == #selector(beginTrimming) {
        return playerView.canBeginTrimming
    }
    return super.validateUserInterfaceItem(item)
}
```

## See Also

### Trimming media

- [- beginTrimmingWithCompletionHandler:](<begintrimming(completionhandler_).md>) — Puts the player view into trimming mode.
- [AVPlayerViewTrimResult](../avplayerviewtrimresult.md) — Constants that specify an action a user takes when trimming media in a player view.
