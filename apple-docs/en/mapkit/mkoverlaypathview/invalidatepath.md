---
title: invalidatePath
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（7.0 起废弃）, iPadOS 4.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkoverlaypathview/invalidatepath
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlaypathview/invalidatepath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlaypathview/invalidatepath.json'
content_hash: 'sha256:9d5b7283eb29b3b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayPathView](../mkoverlaypathview.md)

# invalidatePath

<sub>Instance Method</sub>

Releases the path associated with the receiver.

> [!warning] Deprecated
> Use an [MKOverlayPathRenderer](../mkoverlaypathrenderer.md) object instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) invalidatePath;
```

## Discussion

You can call this method at any time where a change in the path information would require you to recreate the path. This method sets the [path](path.md) property to `nil`, which causes the cached path to be released.

## See Also

### Creating and managing the path

- [path](path.md) — The current path to use when drawing the overlay. _(deprecated)_
- [createPath](createpath.md) — Creates the path for the overlay. _(deprecated)_
