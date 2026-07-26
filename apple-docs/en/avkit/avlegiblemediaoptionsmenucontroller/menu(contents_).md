---
title: 'menu(contents:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, visionOS 26.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avlegiblemediaoptionsmenucontroller/menu(contents:)'
source_url: 'https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/menu(contents:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avlegiblemediaoptionsmenucontroller/menu%28contents%3A%29.json'
content_hash: 'sha256:1c6d4d7c99850b25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVLegibleMediaOptionsMenuController](../avlegiblemediaoptionsmenucontroller.md)

# menu(contents:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func menu(contents: AVLegibleMediaOptionsMenuController.MenuContents = []) -> UIMenu?
```

<sub>macOS</sub>

```swift
func menu(contents: AVLegibleMediaOptionsMenuController.MenuContents = []) -> NSMenu?
```

## Parameters

- `contents` — A set of values from the AVLegibleMediaOptionsMenuContents

## Return Value

A NSMenu ready to be presented by the client, or nil if the menu cannot be built

## Discussion

Builds a legible options menu using the specified contents.

Returns nil if the requested menu type cannot be built due to missing content (e.g., requesting track selection without a player).

## See Also

### Managing the menu

- [menuState](menustate.md)
- [MenuContents](menucontents.md)
- [AVLegibleMediaOptionsMenuState](../avlegiblemediaoptionsmenustate.md)
- [StateChangeReason](statechangereason.md)
