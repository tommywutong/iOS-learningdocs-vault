---
title: 'textSelections(interactingAt:inContainerAt:anchors:modifiers:selecting:bounds:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselectionnavigation/textselections(interactingat:incontainerat:anchors:modifiers:selecting:bounds:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectionnavigation/textselections(interactingat:incontainerat:anchors:modifiers:selecting:bounds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectionnavigation/textselections%28interactingat%3Aincontainerat%3Aanchors%3Amodifiers%3Aselecting%3Abounds%3A%29.json'
content_hash: 'sha256:4687f905cba2e7c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionNavigation](../nstextselectionnavigation.md)

# textSelections(interactingAt:inContainerAt:anchors:modifiers:selecting:bounds:)

<sub>Instance Method</sub>

Returns an array of text selections produced by a tap or click at the point you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textSelections(interactingAt point: CGPoint, inContainerAt containerLocation: any NSTextLocation, anchors: [NSTextSelection], modifiers: NSTextSelectionNavigation.Modifier, selecting: Bool, bounds: CGRect) -> [NSTextSelection]
```

## Parameters

- `point` — A `CGPoint` that represents the location of the tap or click.

- `containerLocation` — A `NSTextLocation that describes the contasiner location`.

- `anchors` — An array of `NSTextSelection` objects.

- `modifiers` — One or more [Modifier](modifier.md) options.

- `selecting` — A Boolean value that indicates if the selection is in drag session.

- `bounds` — A `CGRect` that defines the view area in the container’s coordinate system that can interact with events.

## Return Value

An array of text selections.

## See Also

### Working with text selections

- [- textSelectionForSelectionGranularity:enclosingTextSelection:](<textselection(for_enclosing_).md>) — Returns a text selection expanded to the nearest boundaries for the selection granularity and enclosing text selection text ranges you specify.
- [- destinationSelectionForTextSelection:direction:destination:extending:confined:](<destinationselection(for_direction_destination_extending_confined_).md>) — Returns a new selection that results from applying the navigation operations you specify to the text selection you provide.
