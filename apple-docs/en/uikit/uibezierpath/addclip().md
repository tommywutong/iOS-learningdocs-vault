---
title: addClip()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibezierpath/addclip()
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/addclip()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/addclip%28%29.json'
content_hash: 'sha256:11b89343050fa96f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# addClip()

<sub>Instance Method</sub>

Uses the clipping path of the current graphics context to intersect the region that the path encloses, and makes the resulting shape the current clipping path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func addClip()
```

## Discussion

This method modifies the visible drawing area of the current graphics context. After calling it, subsequent drawing operations result in rendered content only if they occur within the fill area of the specified path.

> [!important] Important
> If you need to remove the clipping region to perform subsequent drawing operations, you must save the current graphics state (using the [saveGState()](<../../coregraphics/cgcontext/savegstate().md>) function) before calling this method. When you no longer need the clipping region, you can then restore the previous drawing properties and clipping region using the [restoreGState()](<../../coregraphics/cgcontext/restoregstate().md>) function.

The [usesEvenOddFillRule](usesevenoddfillrule.md) property is used to determine whether the even-odd or non-zero rule is used to determine the area enclosed by the path.
