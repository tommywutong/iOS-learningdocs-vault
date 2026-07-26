---
title: userSpaceToDeviceSpaceTransform
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontext/userspacetodevicespacetransform
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/userspacetodevicespacetransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/userspacetodevicespacetransform.json'
content_hash: 'sha256:8fe45f44f7cd7932'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# userSpaceToDeviceSpaceTransform

<sub>Instance Property</sub>

Returns an affine transform that maps user space coordinates to device space coordinates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var userSpaceToDeviceSpaceTransform: CGAffineTransform { get }
```

## See Also

### Converting Between Coordinate Spaces

- [CGContextConvertPointToDeviceSpace](<converttodevicespace(__)-53m7u.md>) — Returns a point that is transformed from user space coordinates to device space coordinates.
- [CGContextConvertPointToUserSpace](<converttouserspace(__)-3mtg3.md>) — Returns a point that is transformed from device space coordinates to user space coordinates.
- [CGContextConvertRectToDeviceSpace](<converttodevicespace(__)-91x5g.md>) — Returns a rectangle that is transformed from user space coordinate to device space coordinates.
- [CGContextConvertRectToUserSpace](<converttouserspace(__)-1hk5r.md>) — Returns a rectangle that is transformed from device space coordinate to user space coordinates.
- [CGContextConvertSizeToDeviceSpace](<converttodevicespace(__)-224h2.md>) — Returns a size that is transformed from user space coordinates to device space coordinates.
- [CGContextConvertSizeToUserSpace](<converttouserspace(__)-693ur.md>) — Returns a size that is transformed from device space coordinates to user space coordinates.
