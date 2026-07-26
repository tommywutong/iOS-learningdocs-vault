---
title: NSTextSelectionNavigation
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextselectionnavigation
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectionnavigation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectionnavigation.json'
content_hash: 'sha256:20ce924aa043c830'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextSelectionNavigation

<sub>Class</sub>

An interface you use to expose methods for obtaining results from actions performed on text selections.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class NSTextSelectionNavigation
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a selection navigation

- [- initWithDataSource:](<nstextselectionnavigation/init(datasource_).md>) — Creates a new object using the text selection data source you provide.

### Selection characteristics

- [allowsNonContiguousRanges](nstextselectionnavigation/allowsnoncontiguousranges.md) — Determines if the instance could produce selections with multiple noncontiguous selections.
- [rotatesCoordinateSystemForLayoutOrientation](nstextselectionnavigation/rotatescoordinatesystemforlayoutorientation.md) — Determines if the framework rotates the coordinate system to match the layout orientation.
- [Modifier](nstextselectionnavigation/modifier.md) — Values that describe how the framework handles different kinds of selection modifiers.
- [Destination](nstextselectionnavigation/destination.md) — Values that affect how the framework handles navigation across different textual boundaries during a selection.
- [Direction](nstextselectionnavigation/direction.md) — Values that describe the direction of a selection.
- [- textSelectionForSelectionGranularity:enclosingPoint:inContainerAtLocation:](<nstextselectionnavigation/textselection(for_enclosing_incontainerat_).md>) — Returns a text selection that expands to the nearest boundaries for selection granularity and an enclosing point you specify.

### Accessing the data source

- [textSelectionDataSource](nstextselectionnavigation/textselectiondatasource.md) — The data source associated with this selection navigation.
- [NSTextSelectionDataSource](nstextselectiondatasource.md) — A set of methods that objects implement to provide data for, and manage text selections.

### Working with text selections

- [- textSelectionForSelectionGranularity:enclosingTextSelection:](<nstextselectionnavigation/textselection(for_enclosing_).md>) — Returns a text selection expanded to the nearest boundaries for the selection granularity and enclosing text selection text ranges you specify.
- [- textSelectionsInteractingAtPoint:inContainerAtLocation:anchors:modifiers:selecting:bounds:](<nstextselectionnavigation/textselections(interactingat_incontainerat_anchors_modifiers_selecting_bounds_).md>) — Returns an array of text selections produced by a tap or click at the point you specify.
- [- destinationSelectionForTextSelection:direction:destination:extending:confined:](<nstextselectionnavigation/destinationselection(for_direction_destination_extending_confined_).md>) — Returns a new selection that results from applying the navigation operations you specify to the text selection you provide.

### Controlling cache behavior

- [- flushLayoutCache](<nstextselectionnavigation/flushlayoutcache().md>) — Flushes cached layout information.

### Finding the insertion point

- [- resolvedInsertionLocationForTextSelection:writingDirection:](<nstextselectionnavigation/resolvedinsertionlocation(for_writingdirection_).md>) — Returns the location for inserting the next input depending on the state of the current and secondary selections.

### Specifying deletion ranges

- [- deletionRangesForTextSelection:direction:destination:allowsDecomposition:](<nstextselectionnavigation/deletionranges(for_direction_destination_allowsdecomposition_).md>) — Returns the ranges for deleting the text based on the current selection and movement arguments.

## See Also

### Location and selection

- [NSTextRange](nstextrange.md) — A class that represents a contiguous range between two locations inside document contents.
- [NSTextSelection](nstextselection.md) — A class that represents a single logical selection context that corresponds to an insertion point.
- [NSTextLocation](nstextlocation.md) — An interface you implement that represents an abstract location inside your document’s content.
