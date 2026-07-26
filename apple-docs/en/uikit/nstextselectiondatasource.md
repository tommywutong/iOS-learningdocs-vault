---
title: NSTextSelectionDataSource
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextselectiondatasource
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectiondatasource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectiondatasource.json'
content_hash: 'sha256:cfcb00db50042a93'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextSelectionDataSource

<sub>Protocol</sub>

A set of methods that objects implement to provide data for, and manage text selections.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol NSTextSelectionDataSource : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [NSTextLayoutManager](nstextlayoutmanager.md)

## Topics

### Range of the selection

- [documentRange](nstextselectiondatasource/documentrange.md) — Returns the starting and ending locations for the document.

### Enumerating components of the selection

- [- enumerateCaretOffsetsInLineFragmentAtLocation:usingBlock:](<nstextselectiondatasource/enumeratecaretoffsetsinlinefragment(at_using_).md>) — Enumerates all the insertion point caret offsets from left to right in visual order.
- [- enumerateContainerBoundariesFromLocation:reverse:usingBlock:](<nstextselectiondatasource/enumeratecontainerboundaries(from_reverse_using_).md>) — Enumerates all the container boundaries starting from the location you specify.
- [- enumerateSubstringsFromLocation:options:usingBlock:](<nstextselectiondatasource/enumeratesubstrings(from_options_using_).md>) — Enumerates the textual segment boundaries starting at the location you specify.

### Finding specific content in the selection

- [- locationFromLocation:withOffset:](<nstextselectiondatasource/location(__offsetby_).md>) — Returns a new location using the location and offset you specify.
- [- lineFragmentRangeForPoint:inContainerAtLocation:](<nstextselectiondatasource/linefragmentrange(for_incontainerat_).md>) — Returns the range of the line fragment that contains the point you specify.
- [- offsetFromLocation:toLocation:](<nstextselectiondatasource/offset(from_to_).md>) — Returns the offset between the two locations you specify.
- [- textRangeForSelectionGranularity:enclosingLocation:](<nstextselectiondatasource/textrange(for_enclosing_).md>) — Returns a text range that corresponds to selection granularity of the enclosing location.

### Changing the characteristics of the selection

- [- baseWritingDirectionAtLocation:](<nstextselectiondatasource/basewritingdirection(at_).md>) — Returns the base writing direction at the location you specify.
- [WritingDirection](nstextselectionnavigation/writingdirection.md) — Values that describe the writing direction inside a text selection.
- [- textLayoutOrientationAtLocation:](<nstextselectiondatasource/textlayoutorientation(at_).md>) — Returns the layout orientation at the location you specify.
- [LayoutOrientation](nstextselectionnavigation/layoutorientation.md) — Values that describe the possible layout orientations.

### Instance Methods

- [- convertInteractionPoint:toContainerAtLocation:](<nstextselectiondatasource/convertinteractionpoint(__tocontainerat_).md>) — Converts an interaction point from display space into the text container’s coordinate system. _(beta)_

## See Also

### Accessing the data source

- [textSelectionDataSource](nstextselectionnavigation/textselectiondatasource.md) — The data source associated with this selection navigation.
