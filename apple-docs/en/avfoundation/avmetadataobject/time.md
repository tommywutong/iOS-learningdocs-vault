---
title: time
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 10.10+, tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadataobject/time
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataobject/time'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataobject/time.json'
content_hash: 'sha256:e9b1d5d5b17b19ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataObject](../avmetadataobject.md)

# time

<sub>Instance Property</sub>

The media time value associated with the metadata object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var time: CMTime { get }
```

## Discussion

For captured media, this property represents the time when the metadata was captured. For metadata originating from a sample buffer ([CMSampleBuffer](../../coremedia/cmsamplebuffer.md)), the time is the sample buffer’s presentation time. If there is no valid time value associated with the metadata, this property should contain [invalid](../../coremedia/cmtime/invalid.md).

## See Also

### Inspecting the metadata

- [bounds](bounds.md) — The bounding rectangle associated with the metadata.
- [duration](duration.md) — The duration of the media associated with this metadata object.
- [type](type.md) — The type of metadata that this object provides.
- [ObjectType](objecttype.md) — Constants that identify metadata object types.
- [fixedFocus](isfixedfocus.md) — A BOOL indicating whether this metadata object represents a fixed focus.
- [cinematicVideoFocusMode](cinematicvideofocusmode.md) — The current focus mode when an object is detected during a Cinematic Video recording.
- [groupID](groupid.md) — An identifier associated with a metadata object used to group it with other metadata objects belonging to a common parent.
- [objectID](objectid.md) — A unique identifier for each detected object type (face, body, hands, heads and salient objects) in a collection.
