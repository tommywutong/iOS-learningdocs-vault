---
title: createPath()
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkoverlaypathrenderer/createpath()
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/createpath()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathrenderer/createpath%28%29.json'
content_hash: 'sha256:a0f2bbb513aaea9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathRenderer](../mkoverlaypathrenderer.md)

# createPath()

<sub>Instance Method</sub>

Creates the path for the overlay.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func createPath()
```

## Discussion

The default implementation of this method does nothing. Subclasses can override it and use it to create the [CGPath](../../coregraphics/cgpath.md) data type the subclass uses for drawing. After creating the path, your implementation needs to assign it to the [path](path.md) property.

## See Also

### Creating and managing the path

- [path](path.md) — The path representing the overlay’s shape.
- [- invalidatePath](<invalidatepath().md>) — Updates the path associated with the overlay renderer.
