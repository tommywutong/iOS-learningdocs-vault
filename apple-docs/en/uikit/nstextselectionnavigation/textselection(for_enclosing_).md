---
title: 'textSelection(for:enclosing:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselectionnavigation/textselection(for:enclosing:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectionnavigation/textselection(for:enclosing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectionnavigation/textselection%28for%3Aenclosing%3A%29.json'
content_hash: 'sha256:a00dd7e43e92931d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionNavigation](../nstextselectionnavigation.md)

# textSelection(for:enclosing:)

<sub>Instance Method</sub>

Returns a text selection expanded to the nearest boundaries for the selection granularity and enclosing text selection text ranges you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textSelection(for selectionGranularity: NSTextSelection.Granularity, enclosing textSelection: NSTextSelection) -> NSTextSelection
```

## Parameters

- `selectionGranularity` — One of the available [Granularity](../nstextselection/granularity-swift.enum.md) options.

- `textSelection` — The text selection that describes the text range of interest.

## Return Value

A new text selection.

## See Also

### Working with text selections

- [- textSelectionsInteractingAtPoint:inContainerAtLocation:anchors:modifiers:selecting:bounds:](<textselections(interactingat_incontainerat_anchors_modifiers_selecting_bounds_).md>) — Returns an array of text selections produced by a tap or click at the point you specify.
- [- destinationSelectionForTextSelection:direction:destination:extending:confined:](<destinationselection(for_direction_destination_extending_confined_).md>) — Returns a new selection that results from applying the navigation operations you specify to the text selection you provide.
