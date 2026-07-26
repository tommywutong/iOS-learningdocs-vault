---
title: 'resolvedInsertionLocation(for:writingDirection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselectionnavigation/resolvedinsertionlocation(for:writingdirection:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectionnavigation/resolvedinsertionlocation(for:writingdirection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectionnavigation/resolvedinsertionlocation%28for%3Awritingdirection%3A%29.json'
content_hash: 'sha256:2754ebcc2287ca7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionNavigation](../nstextselectionnavigation.md)

# resolvedInsertionLocation(for:writingDirection:)

<sub>Instance Method</sub>

Returns the location for inserting the next input depending on the state of the current and secondary selections.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func resolvedInsertionLocation(for textSelection: NSTextSelection, writingDirection: NSTextSelectionNavigation.WritingDirection) -> (any NSTextLocation)?
```

## Parameters

- `textSelection` — The text selection.

- `writingDirection` — The [WritingDirection](writingdirection.md) direction.

## Return Value

Returns an `NSTextLocation` when the `textSelection.isLogical = false AND` `secondarySelectionLocation != nil`. Otherwise, returns nil.
