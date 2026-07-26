---
title: objectID
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadataobject/objectid
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataobject/objectid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataobject/objectid.json'
content_hash: 'sha256:d25dd2af792b4953'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataObject](../avmetadataobject.md)

# objectID

<sub>Instance Property</sub>

A unique identifier for each detected object type (face, body, hands, heads and salient objects) in a collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var objectID: Int { get }
```

## Discussion

Defaults to a value of -1 when invalid or not available. When used in conjunction with an [AVCaptureMetadataOutput](../avcapturemetadataoutput.md), each newly detected object that enters the scene is assigned a unique identifier. [objectID](objectid.md)s are never re-used as objects leave the picture and new ones enter. Objects that leave the picture and then re-enter are assigned a new [objectID](objectid.md).

## See Also

### Inspecting the metadata

- [bounds](bounds.md) — The bounding rectangle associated with the metadata.
- [duration](duration.md) — The duration of the media associated with this metadata object.
- [time](time.md) — The media time value associated with the metadata object.
- [type](type.md) — The type of metadata that this object provides.
- [ObjectType](objecttype.md) — Constants that identify metadata object types.
- [fixedFocus](isfixedfocus.md) — A BOOL indicating whether this metadata object represents a fixed focus.
- [cinematicVideoFocusMode](cinematicvideofocusmode.md) — The current focus mode when an object is detected during a Cinematic Video recording.
- [groupID](groupid.md) — An identifier associated with a metadata object used to group it with other metadata objects belonging to a common parent.
