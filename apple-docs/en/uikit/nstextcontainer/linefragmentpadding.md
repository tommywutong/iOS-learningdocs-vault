---
title: lineFragmentPadding
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontainer/linefragmentpadding
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontainer/linefragmentpadding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontainer/linefragmentpadding.json'
content_hash: 'sha256:1f196c129819610d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContainer](../nstextcontainer.md)

# lineFragmentPadding

<sub>Instance Property</sub>

The value for the text inset within line fragment rectangles.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var lineFragmentPadding: CGFloat { get set }
```

## Discussion

The padding appears at the beginning and end of the line fragment rectangles. The layout manager uses this value to determine the layout width. The default value of this property is `5.0`.

Line fragment padding is not designed to express text margins. Instead, you should use insets on your text view, adjust the paragraph margin attributes, or change the position of the text view within its superview.

## See Also

### Related Documentation

- [- lineFragmentRectForProposedRect:atIndex:writingDirection:remainingRect:](<linefragmentrect(forproposedrect_at_writingdirection_remaining_).md>) — Returns the bounds of a line fragment rectangle inside the text container for the proposed rectangle.

### Constraining text layout

- [maximumNumberOfLines](maximumnumberoflines.md) — The maximum number of lines that the text container can store.
- [- lineFragmentRectForProposedRect:atIndex:writingDirection:remainingRect:](<linefragmentrect(forproposedrect_at_writingdirection_remaining_).md>) — Returns the bounds of a line fragment rectangle inside the text container for the proposed rectangle.
- [simpleRectangularTextContainer](issimplerectangulartextcontainer.md) — A Boolean that indicates whether the text container’s region is a rectangle with no holes or gaps, and whose edges are parallel to the text view’s coordinate system axes.
