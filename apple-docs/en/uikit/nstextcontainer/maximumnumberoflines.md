---
title: maximumNumberOfLines
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontainer/maximumnumberoflines
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontainer/maximumnumberoflines'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontainer/maximumnumberoflines.json'
content_hash: 'sha256:72f54d88291d90e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContainer](../nstextcontainer.md)

# maximumNumberOfLines

<sub>Instance Property</sub>

The maximum number of lines that the text container can store.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var maximumNumberOfLines: Int { get set }
```

## Discussion

The layout manager uses the value of this property to determine the maximum number of lines associated with the text container. The default value of this property is `0`, which indicates that there is no limit.

## See Also

### Constraining text layout

- [lineFragmentPadding](linefragmentpadding.md) — The value for the text inset within line fragment rectangles.
- [- lineFragmentRectForProposedRect:atIndex:writingDirection:remainingRect:](<linefragmentrect(forproposedrect_at_writingdirection_remaining_).md>) — Returns the bounds of a line fragment rectangle inside the text container for the proposed rectangle.
- [simpleRectangularTextContainer](issimplerectangulartextcontainer.md) — A Boolean that indicates whether the text container’s region is a rectangle with no holes or gaps, and whose edges are parallel to the text view’s coordinate system axes.
