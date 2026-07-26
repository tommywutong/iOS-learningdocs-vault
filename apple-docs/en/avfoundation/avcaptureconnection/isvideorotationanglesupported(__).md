---
title: 'isVideoRotationAngleSupported(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureconnection/isvideorotationanglesupported(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideorotationanglesupported(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/isvideorotationanglesupported%28_%3A%29.json'
content_hash: 'sha256:cdcb4cff84637c2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# isVideoRotationAngleSupported(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the connection supports a rotation angle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func isVideoRotationAngleSupported(_ videoRotationAngle: CGFloat) -> Bool
```

## Parameters

- `videoRotationAngle` — A rotation angle in degrees.

## See Also

### Rotating a video

- [videoRotationAngle](videorotationangle.md) — A rotation angle the connection applies to a video flowing through it.
