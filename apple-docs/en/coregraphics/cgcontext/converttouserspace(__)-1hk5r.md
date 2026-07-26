---
title: 'convertToUserSpace(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/converttouserspace(_:)-1hk5r'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/converttouserspace(_:)-1hk5r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/converttouserspace%28_%3A%29-1hk5r.json'
content_hash: 'sha256:58895530b9db3be8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# convertToUserSpace(_:)

<sub>Instance Method</sub>

Returns a rectangle that is transformed from device space coordinate to user space coordinates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func convertToUserSpace(_ rect: CGRect) -> CGRect
```

## Parameters

- `rect` — The rectangle, in device space coordinates, to transform.

## Return Value

The rectangle in user space coordinates.

## Discussion

In general, affine transforms do not preserve rectangles. As a result, this function returns the smallest rectangle that contains the transformed corner points of the rectangle.

## See Also

### Converting Between Coordinate Spaces

- [CGContextGetUserSpaceToDeviceSpaceTransform](userspacetodevicespacetransform.md) — Returns an affine transform that maps user space coordinates to device space coordinates.
- [CGContextConvertPointToDeviceSpace](<converttodevicespace(__)-53m7u.md>) — Returns a point that is transformed from user space coordinates to device space coordinates.
- [CGContextConvertPointToUserSpace](<converttouserspace(__)-3mtg3.md>) — Returns a point that is transformed from device space coordinates to user space coordinates.
- [CGContextConvertRectToDeviceSpace](<converttodevicespace(__)-91x5g.md>) — Returns a rectangle that is transformed from user space coordinate to device space coordinates.
- [CGContextConvertSizeToDeviceSpace](<converttodevicespace(__)-224h2.md>) — Returns a size that is transformed from user space coordinates to device space coordinates.
- [CGContextConvertSizeToUserSpace](<converttouserspace(__)-693ur.md>) — Returns a size that is transformed from device space coordinates to user space coordinates.
