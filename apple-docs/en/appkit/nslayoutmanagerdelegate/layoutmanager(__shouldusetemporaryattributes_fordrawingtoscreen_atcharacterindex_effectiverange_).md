---
title: 'layoutManager(_:shouldUseTemporaryAttributes:forDrawingToScreen:atCharacterIndex:effectiveRange:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanagerdelegate/layoutmanager(_:shouldusetemporaryattributes:fordrawingtoscreen:atcharacterindex:effectiverange:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/layoutmanager(_:shouldusetemporaryattributes:fordrawingtoscreen:atcharacterindex:effectiverange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanagerdelegate/layoutmanager%28_%3Ashouldusetemporaryattributes%3Afordrawingtoscreen%3Aatcharacterindex%3Aeffectiverange%3A%29.json'
content_hash: 'sha256:bab4f3e98cb9f2b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManagerDelegate](../nslayoutmanagerdelegate.md)

# layoutManager(_:shouldUseTemporaryAttributes:forDrawingToScreen:atCharacterIndex:effectiveRange:)

<sub>Instance Method</sub>

Asks the delegate whether to use temporary attributes when drawing the text.

<sub>macOS</sub>

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, shouldUseTemporaryAttributes attrs: [NSAttributedString.Key : Any] = [:], forDrawingToScreen toScreen: Bool, atCharacterIndex charIndex: Int, effectiveRange effectiveCharRange: NSRangePointer?) -> [NSAttributedString.Key : Any]?
```

## Parameters

- `layoutManager` — The layout manager sending the message.

- `attrs` — The temporary attributes currently in effect for the given character range.

- `toScreen` — [true](../../swift/true.md) if the layout manager is drawing to the screen; otherwise, [false](../../swift/false.md).

- `charIndex` — Index of the first character in the range being drawn.

- `effectiveCharRange` — On input and output, the effective range to which the temporary attributes apply.

## Return Value

The temporary attributes for the layout manager to use, or `nil` if no temporary attributes are to be used.

## Discussion

The default behavior, if this method is not implemented, is to use temporary attributes only when drawing to the screen, so an implementation to match that behavior would return `attrs` if `toScreen` is [true](../../swift/true.md) and `nil` otherwise, without changing `effectiveCharRange`.
