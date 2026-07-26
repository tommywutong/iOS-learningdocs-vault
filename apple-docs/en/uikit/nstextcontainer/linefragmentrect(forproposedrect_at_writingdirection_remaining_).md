---
title: 'lineFragmentRect(forProposedRect:at:writingDirection:remaining:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextcontainer/linefragmentrect(forproposedrect:at:writingdirection:remaining:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontainer/linefragmentrect(forproposedrect:at:writingdirection:remaining:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontainer/linefragmentrect%28forproposedrect%3Aat%3Awritingdirection%3Aremaining%3A%29.json'
content_hash: 'sha256:1402c9175de04991'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContainer](../nstextcontainer.md)

# lineFragmentRect(forProposedRect:at:writingDirection:remaining:)

<sub>Instance Method</sub>

Returns the bounds of a line fragment rectangle inside the text container for the proposed rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func lineFragmentRect(forProposedRect proposedRect: CGRect, at characterIndex: Int, writingDirection baseWritingDirection: NSWritingDirection, remaining remainingRect: UnsafeMutablePointer<CGRect>?) -> CGRect
```

## Parameters

- `proposedRect` — A rectangle in which to lay out text proposed by the layout manager.

- `characterIndex` — The character location inside the text storage for the line fragment being processed.

- `baseWritingDirection` — The direction of advancement for line fragments inside a visual horizontal line. The values passed into the method are either [NSWritingDirectionLeftToRight](../nswritingdirection/lefttoright.md) or [NSWritingDirectionRightToLeft](../nswritingdirection/righttoleft.md).

- `remainingRect` — The remainder of the proposed rectangle that was excluded from returned rectangle. It can be passed in as the proposed rectangle for the next iteration.

## Discussion

The bounds of the line fragment rectangle are determined by the intersection of `proposedRect` and the text container’s bounding rectangle defined by its [NSTextContainer](../nstextcontainer.md) property. The regions defined by the [NSTextContainer](../nstextcontainer.md) property are excluded from the return value. It is possible that `proposedRect` can be divided into multiple line fragments due to exclusion paths. In that case, `remainingRect` returns the remainder that can be passed in as the proposed rectangle for the next iteration.

This method can be overridden by subclasses for further text container region customization.

## See Also

### Constraining text layout

- [maximumNumberOfLines](maximumnumberoflines.md) — The maximum number of lines that the text container can store.
- [lineFragmentPadding](linefragmentpadding.md) — The value for the text inset within line fragment rectangles.
- [simpleRectangularTextContainer](issimplerectangulartextcontainer.md) — A Boolean that indicates whether the text container’s region is a rectangle with no holes or gaps, and whose edges are parallel to the text view’s coordinate system axes.
