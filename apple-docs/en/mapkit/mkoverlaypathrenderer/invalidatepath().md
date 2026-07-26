---
title: invalidatePath()
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkoverlaypathrenderer/invalidatepath()
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/invalidatepath()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathrenderer/invalidatepath%28%29.json'
content_hash: 'sha256:a95d4eefffd09254'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathRenderer](../mkoverlaypathrenderer.md)

# invalidatePath()

<sub>Instance Method</sub>

Updates the path associated with the overlay renderer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func invalidatePath()
```

## Discussion

Call this method when a change in the path information would require you to recreate the overlay’s path. This method sets the [path](path.md) property to `nil` and tells the overlay renderer to redisplay its contents.

## See Also

### Creating and managing the path

- [path](path.md) — The path representing the overlay’s shape.
- [- createPath](<createpath().md>) — Creates the path for the overlay.
