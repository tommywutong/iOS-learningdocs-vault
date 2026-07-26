---
title: createPath
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkoverlaypathview/createpath
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathview/createpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathview/createpath.json'
content_hash: 'sha256:74218fb5b17352c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathView](../mkoverlaypathview.md)

# createPath

<sub>Instance Method</sub>

Creates the path for the overlay.

> [!warning] Deprecated
> Use an [MKOverlayPathRenderer](../mkoverlaypathrenderer.md) object instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) createPath;
```

## Discussion

The default implementation of this method does nothing. Subclasses should override it and use it to create the [CGPath](../../coregraphics/cgpath.md) data type to be used for drawing. After creating the path, your implementation should then assign it to the [path](path.md) property.

## See Also

### Creating and managing the path

- [path](path.md) — The current path to use when drawing the overlay. _(deprecated)_
- [invalidatePath](invalidatepath.md) — Releases the path associated with the receiver. _(deprecated)_
