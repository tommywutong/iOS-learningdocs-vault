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
doc_path: '/documentation/uikit/uiaccessibility/converttoscreencoordinates(_:in:)-6dx4a'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/converttoscreencoordinates(_:in:)-6dx4a'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/converttoscreencoordinates%28_%3Ain%3A%29-6dx4a.json'
content_hash: 'sha256:b8efc1b23ddb1fc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# convertToScreenCoordinates(_:in:)

<sub>Type Method</sub>

Converts the specified path object to screen coordinates and returns a new path object with the results.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor static func convertToScreenCoordinates(_ path: UIBezierPath, in view: UIView) -> UIBezierPath
```

## Parameters

- `path` — The path object that you want to convert. The coordinate values used to create this path object should be relative to the coordinate system of the specified `view`. This parameter must not be `nil`.

- `view` — The view whose coordinate system was used to define the path. This parameter must not be `nil`.

## Return Value

A new path object that has the same shape as `path` but whose points are specified in screen coordinates.

## Discussion

This function adjusts the points of the path you provide to values that the accessibility system can use. You can use it to convert path objects in use by your app’s user interface before handing them to the accessibility system.

## See Also

### Conversions

- [UIAccessibilityConvertFrameToScreenCoordinates](<converttoscreencoordinates(__in_)-9ziiu.md>) — Converts the specified rectangle from view coordinates to screen coordinates.
