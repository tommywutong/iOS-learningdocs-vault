---
title: 'destinationSelection(for:direction:destination:extending:confined:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselectionnavigation/destinationselection(for:direction:destination:extending:confined:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectionnavigation/destinationselection(for:direction:destination:extending:confined:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectionnavigation/destinationselection%28for%3Adirection%3Adestination%3Aextending%3Aconfined%3A%29.json'
content_hash: 'sha256:dbf024e96bae48e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionNavigation](../nstextselectionnavigation.md)

# destinationSelection(for:direction:destination:extending:confined:)

<sub>Instance Method</sub>

Returns a new selection that results from applying the navigation operations you specify to the text selection you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func destinationSelection(for textSelection: NSTextSelection, direction: NSTextSelectionNavigation.Direction, destination: NSTextSelectionNavigation.Destination, extending: Bool, confined: Bool) -> NSTextSelection?
```

## Parameters

- `textSelection` — The source selection.

- `direction` — One of the available [Direction](direction.md) directions.

- `destination` — One of the available [Destination](destination.md) destinations.

- `extending` — Whether this selection extends an existing selection.

- `confined` — Whether to confine movement to the existing selection.

## Return Value

A new [NSTextSelection](../nstextselection.md), or `nil` if the operation doesn’t produce a logically valid result.

## Discussion

If `confined` is `true`, confine any movement to the text element that the selection already lies within.

## See Also

### Working with text selections

- [- textSelectionForSelectionGranularity:enclosingTextSelection:](<textselection(for_enclosing_).md>) — Returns a text selection expanded to the nearest boundaries for the selection granularity and enclosing text selection text ranges you specify.
- [- textSelectionsInteractingAtPoint:inContainerAtLocation:anchors:modifiers:selecting:bounds:](<textselections(interactingat_incontainerat_anchors_modifiers_selecting_bounds_).md>) — Returns an array of text selections produced by a tap or click at the point you specify.
