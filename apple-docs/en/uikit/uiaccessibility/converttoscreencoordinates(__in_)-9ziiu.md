---
title: 'convertToScreenCoordinates(_:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibility/converttoscreencoordinates(_:in:)-9ziiu'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/converttoscreencoordinates(_:in:)-9ziiu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/converttoscreencoordinates%28_%3Ain%3A%29-9ziiu.json'
content_hash: 'sha256:c6fbd0fa2c6ed73f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# convertToScreenCoordinates(_:in:)

<sub>Type Method</sub>

Converts the specified rectangle from view coordinates to screen coordinates.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor static func convertToScreenCoordinates(_ rect: CGRect, in view: UIView) -> CGRect
```

## Parameters

- `rect` — A rectangle specified in the coordinate system of the specified `view`.

- `view` — The view that contains the specified rectangle. This parameter must not be `nil`.

## Return Value

The rectangle in screen coordinates.

## Discussion

Use this function to convert accessibility frame rectangles to screen coordinates.

## See Also

### Conversions

- [UIAccessibilityConvertPathToScreenCoordinates](<converttoscreencoordinates(__in_)-6dx4a.md>) — Converts the specified path object to screen coordinates and returns a new path object with the results.
