---
title: trackingID
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifacefeature/trackingid-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/cifacefeature/trackingid-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifacefeature/trackingid-swift.property.json'
content_hash: 'sha256:35c2cc9dfdf8bec0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFaceFeature](../cifacefeature.md)

# trackingID

<sub>Instance Property</sub>

The tracking identifier of the face object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var trackingID: Int32 { get }
```

## Discussion

Core Image provides a tracking identifier for faces it detects in a video stream, which you can use to identify when a CIFaceFeature objects detected in one video frame is the same face detected in a previous video frame.

This identifier persists only as long as a face is in the frame and is not associated with a specific face. In other words, if a face moves out of the video frame and comes back into the frame later, another ID is assigned. (Core Image detects faces, but does not recognize specific faces.)

## See Also

### Tracking Distinct Faces in Video

- [hasTrackingID](hastrackingid-swift.property.md) — A Boolean value that indicates whether the face object has a tracking ID.
- [hasTrackingFrameCount](hastrackingframecount-swift.property.md) — A Boolean value that indicates the face object has a tracking frame count.
- [trackingFrameCount](trackingframecount-swift.property.md) — The tracking frame count of the face.
