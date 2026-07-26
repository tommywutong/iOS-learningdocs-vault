---
title: 'deletionRanges(for:direction:destination:allowsDecomposition:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselectionnavigation/deletionranges(for:direction:destination:allowsdecomposition:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectionnavigation/deletionranges(for:direction:destination:allowsdecomposition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectionnavigation/deletionranges%28for%3Adirection%3Adestination%3Aallowsdecomposition%3A%29.json'
content_hash: 'sha256:c1424cc8b366ec7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionNavigation](../nstextselectionnavigation.md)

# deletionRanges(for:direction:destination:allowsDecomposition:)

<sub>Instance Method</sub>

Returns the ranges for deleting the text based on the current selection and movement arguments.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func deletionRanges(for textSelection: NSTextSelection, direction: NSTextSelectionNavigation.Direction, destination: NSTextSelectionNavigation.Destination, allowsDecomposition: Bool) -> [NSTextRange]
```

## Parameters

- `textSelection` — The text selection.

- `direction` — The [Direction](direction.md) to consider when calculating the deletion ranges.

- `destination` — The [Destination](destination.md) that describes the scope of the text selection to consider when calculating the deletion ranges.

- `allowsDecomposition` — A Boolean value that determines if this method operates on composite characters which may be present depending on the characteristics of the script used by `textSelection`.

## Return Value

An array of text ranges to delete.

## Discussion

The selection after deletion contains a zero-length range starting at the location of the first range returned. The framework ignores the destination when `textSelection` has a non-empty selection. The `allowsDecomposition` parameter only applies to the [NSTextSelectionNavigationDirectionBackward](direction/backward.md) direction and [NSTextSelectionNavigationDestinationCharacter](destination/character.md) with a zero-length selection.
