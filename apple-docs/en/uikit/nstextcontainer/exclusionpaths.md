---
title: exclusionPaths
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontainer/exclusionpaths
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontainer/exclusionpaths'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontainer/exclusionpaths.json'
content_hash: 'sha256:f92e25ebe398055f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContainer](../nstextcontainer.md)

# exclusionPaths

<sub>Instance Property</sub>

An array of path objects that represents the regions where text doesn’t display in the text container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var exclusionPaths: [UIBezierPath] { get set }
```

## Discussion

The default value of this property is an empty array. Depending on the platform, you can assign an array of [NSBezierPath](../../appkit/nsbezierpath.md) or [UIBezierPath](../uibezierpath.md) objects to exclude text from one or more regions in the text container’s bounds. When the layout manager proposes a line fragment rectangle intersecting one of the regions defined by the exclusion paths, the text container returns an adjusted line fragment rectangle excluding that region.

## See Also

### Related Documentation

- [- lineFragmentRectForProposedRect:atIndex:writingDirection:remainingRect:](<linefragmentrect(forproposedrect_at_writingdirection_remaining_).md>) — Returns the bounds of a line fragment rectangle inside the text container for the proposed rectangle.

### Defining the container shape

- [size](size.md) — The size of the text container’s bounding rectangle.
- [lineBreakMode](linebreakmode.md) — The behavior of the last line inside the text container.
- [widthTracksTextView](widthtrackstextview.md) — A Boolean that controls whether the text container adjusts the width of its bounding rectangle when its text view resizes.
- [heightTracksTextView](heighttrackstextview.md) — A Boolean that controls whether the text container adjusts the height of its bounding rectangle when its text view resizes.
