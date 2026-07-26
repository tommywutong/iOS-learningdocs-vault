---
title: path
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkoverlaypathview/path
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathview/path'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathview/path.json'
content_hash: 'sha256:ab85d3cb65ffb4ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathView](../mkoverlaypathview.md)

# path

<sub>Instance Property</sub>

The current path to use when drawing the overlay.

> [!warning] Deprecated
> Use an [MKOverlayPathRenderer](../mkoverlaypathrenderer.md) object instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property CGPathRef path;
```

## Discussion

Getting the value of this property causes the path to be created (using the [createPath](createpath.md) method) if it does not already exist. You can also assign a path object to this property explicitly.

When assigning a new path object to this property, the receiver retains the path you specify.

## See Also

### Creating and managing the path

- [createPath](createpath.md) — Creates the path for the overlay. _(deprecated)_
- [invalidatePath](invalidatepath.md) — Releases the path associated with the receiver. _(deprecated)_
