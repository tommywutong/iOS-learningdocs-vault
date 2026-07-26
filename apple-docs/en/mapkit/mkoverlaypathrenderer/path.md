---
title: path
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkoverlaypathrenderer/path
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/path'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathrenderer/path.json'
content_hash: 'sha256:ffae445cb5388058'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathRenderer](../mkoverlaypathrenderer.md)

# path

<sub>Instance Property</sub>

The path representing the overlay’s shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var path: CGPath! { get set }
```

## Discussion

Getting the value of this property causes the method to create the path (using the [- createPath](<createpath().md>) method) if it doesn’t already exist. You can assign a path object to this property explicitly. When assigning a new path object to this property, the overlay renderer stores a strong reference to the path you provide.

## See Also

### Creating and managing the path

- [- createPath](<createpath().md>) — Creates the path for the overlay.
- [- invalidatePath](<invalidatepath().md>) — Updates the path associated with the overlay renderer.
