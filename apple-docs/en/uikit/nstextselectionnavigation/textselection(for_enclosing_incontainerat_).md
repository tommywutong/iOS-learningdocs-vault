---
title: 'textSelection(for:enclosing:inContainerAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselectionnavigation/textselection(for:enclosing:incontainerat:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectionnavigation/textselection(for:enclosing:incontainerat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectionnavigation/textselection%28for%3Aenclosing%3Aincontainerat%3A%29.json'
content_hash: 'sha256:ab99a026c71306df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionNavigation](../nstextselectionnavigation.md)

# textSelection(for:enclosing:inContainerAt:)

<sub>Instance Method</sub>

Returns a text selection that expands to the nearest boundaries for selection granularity and an enclosing point you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textSelection(for selectionGranularity: NSTextSelection.Granularity, enclosing point: CGPoint, inContainerAt location: any NSTextLocation) -> NSTextSelection?
```

## Parameters

- `selectionGranularity` — One of the available [Granularity](../nstextselection/granularity-swift.enum.md) options.

- `point` — The point that encloses the text.

- `location` — An [NSTextLocation](../nstextlocation.md) that describes the container.

## Return Value

A new `NSTextSelection`, or `nil` if the text selection is not found.

## See Also

### Selection characteristics

- [allowsNonContiguousRanges](allowsnoncontiguousranges.md) — Determines if the instance could produce selections with multiple noncontiguous selections.
- [rotatesCoordinateSystemForLayoutOrientation](rotatescoordinatesystemforlayoutorientation.md) — Determines if the framework rotates the coordinate system to match the layout orientation.
- [Modifier](modifier.md) — Values that describe how the framework handles different kinds of selection modifiers.
- [Destination](destination.md) — Values that affect how the framework handles navigation across different textual boundaries during a selection.
- [Direction](direction.md) — Values that describe the direction of a selection.
