---
title: bounds
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 10.10+, tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadataobject/bounds
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataobject/bounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataobject/bounds.json'
content_hash: 'sha256:229ebf37a85d15a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataObject](../avmetadataobject.md)

# bounds

<sub>Instance Property</sub>

The bounding rectangle associated with the metadata.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var bounds: CGRect { get }
```

## Discussion

The bounding rectangle is specified relative to the picture or video of the corresponding media. The rectangle’s origin is always specified in the top-left corner, and the x and y axis extend down and to the right.

If the metadata has no bounding rectangle, the value of this property should be [CGRectZero](../../coregraphics/cgrectzero.md).

For video content, the bounding rectangle may be expressed using scalar values in the range 0.0 to 1.0. Scalar values remain meaningful even when the original video has been scaled down.

## See Also

### Inspecting the metadata

- [duration](duration.md) — The duration of the media associated with this metadata object.
- [time](time.md) — The media time value associated with the metadata object.
- [type](type.md) — The type of metadata that this object provides.
- [ObjectType](objecttype.md) — Constants that identify metadata object types.
- [fixedFocus](isfixedfocus.md) — A BOOL indicating whether this metadata object represents a fixed focus.
- [cinematicVideoFocusMode](cinematicvideofocusmode.md) — The current focus mode when an object is detected during a Cinematic Video recording.
- [groupID](groupid.md) — An identifier associated with a metadata object used to group it with other metadata objects belonging to a common parent.
- [objectID](objectid.md) — A unique identifier for each detected object type (face, body, hands, heads and salient objects) in a collection.
