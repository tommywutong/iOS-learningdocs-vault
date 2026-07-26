---
title: cinematicVideoFocusMode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadataobject/cinematicvideofocusmode
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataobject/cinematicvideofocusmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataobject/cinematicvideofocusmode.json'
content_hash: 'sha256:89dcdd91a2711fdc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataObject](../avmetadataobject.md)

# cinematicVideoFocusMode

<sub>Instance Property</sub>

The current focus mode when an object is detected during a Cinematic Video recording.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var cinematicVideoFocusMode: AVCaptureDevice.CinematicVideoFocusMode { get }
```

## Discussion

Default is [AVCaptureCinematicVideoFocusModeNone](../avcapturedevice/cinematicvideofocusmode/none.md).

## See Also

### Inspecting the metadata

- [bounds](bounds.md) — The bounding rectangle associated with the metadata.
- [duration](duration.md) — The duration of the media associated with this metadata object.
- [time](time.md) — The media time value associated with the metadata object.
- [type](type.md) — The type of metadata that this object provides.
- [ObjectType](objecttype.md) — Constants that identify metadata object types.
- [fixedFocus](isfixedfocus.md) — A BOOL indicating whether this metadata object represents a fixed focus.
- [groupID](groupid.md) — An identifier associated with a metadata object used to group it with other metadata objects belonging to a common parent.
- [objectID](objectid.md) — A unique identifier for each detected object type (face, body, hands, heads and salient objects) in a collection.
