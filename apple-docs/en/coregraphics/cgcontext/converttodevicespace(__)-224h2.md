---
title: 'convertToDeviceSpace(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/converttodevicespace(_:)-224h2'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/converttodevicespace(_:)-224h2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/converttodevicespace%28_%3A%29-224h2.json'
content_hash: 'sha256:0a5ad3cc465dc063'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# convertToDeviceSpace(_:)

<sub>Instance Method</sub>

Returns a size that is transformed from user space coordinates to device space coordinates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func convertToDeviceSpace(_ size: CGSize) -> CGSize
```

## Parameters

- `size` — The size, in user space coordinates, to transform.

## Return Value

The size in device space coordinates.

## See Also

### Converting Between Coordinate Spaces

- [CGContextGetUserSpaceToDeviceSpaceTransform](userspacetodevicespacetransform.md) — Returns an affine transform that maps user space coordinates to device space coordinates.
- [CGContextConvertPointToDeviceSpace](<converttodevicespace(__)-53m7u.md>) — Returns a point that is transformed from user space coordinates to device space coordinates.
- [CGContextConvertPointToUserSpace](<converttouserspace(__)-3mtg3.md>) — Returns a point that is transformed from device space coordinates to user space coordinates.
- [CGContextConvertRectToDeviceSpace](<converttodevicespace(__)-91x5g.md>) — Returns a rectangle that is transformed from user space coordinate to device space coordinates.
- [CGContextConvertRectToUserSpace](<converttouserspace(__)-1hk5r.md>) — Returns a rectangle that is transformed from device space coordinate to user space coordinates.
- [CGContextConvertSizeToUserSpace](<converttouserspace(__)-693ur.md>) — Returns a size that is transformed from device space coordinates to user space coordinates.
