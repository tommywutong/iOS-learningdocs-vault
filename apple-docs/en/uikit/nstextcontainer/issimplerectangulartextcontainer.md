---
title: isSimpleRectangularTextContainer
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontainer/issimplerectangulartextcontainer
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontainer/issimplerectangulartextcontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontainer/issimplerectangulartextcontainer.json'
content_hash: 'sha256:065ff13ee46bb693'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContainer](../nstextcontainer.md)

# isSimpleRectangularTextContainer

<sub>Instance Property</sub>

A Boolean that indicates whether the text container’s region is a rectangle with no holes or gaps, and whose edges are parallel to the text view’s coordinate system axes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isSimpleRectangularTextContainer: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) when the text container’s region is a rectangle with no holes or gaps and the edges are parallel to the text view’s coordinate system axes. The default value of this property is [false](../../swift/false.md) when the [exclusionPaths](exclusionpaths.md) property contains one or more items, when the [maximumNumberOfLines](maximumnumberoflines.md) property is not zero, or when you override the [- lineFragmentRectForProposedRect:atIndex:writingDirection:remainingRect:](<linefragmentrect(forproposedrect_at_writingdirection_remaining_).md>) method. Otherwise, the default value is [true](../../swift/true.md).

## See Also

### Constraining text layout

- [maximumNumberOfLines](maximumnumberoflines.md) — The maximum number of lines that the text container can store.
- [lineFragmentPadding](linefragmentpadding.md) — The value for the text inset within line fragment rectangles.
- [- lineFragmentRectForProposedRect:atIndex:writingDirection:remainingRect:](<linefragmentrect(forproposedrect_at_writingdirection_remaining_).md>) — Returns the bounds of a line fragment rectangle inside the text container for the proposed rectangle.
