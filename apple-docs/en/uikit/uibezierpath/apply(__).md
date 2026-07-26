---
title: 'apply(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibezierpath/apply(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/apply(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/apply%28_%3A%29.json'
content_hash: 'sha256:daad4165c263aec2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# apply(_:)

<sub>Instance Method</sub>

Transforms all points in the path using the specified affine transform matrix.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func apply(_ transform: CGAffineTransform)
```

## Parameters

- `transform` — The transform matrix to apply to the path.

## Discussion

This method applies the specified transform to the path’s points immediately. The modifications made to the path object are permanent. If you do not want to permanently modify a path object, you should consider applying the transform to a copy.
