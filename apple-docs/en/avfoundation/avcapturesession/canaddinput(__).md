---
title: 'canAddInput(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesession/canaddinput(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/canaddinput(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/canaddinput%28_%3A%29.json'
content_hash: 'sha256:3638d3f6aff2ef74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# canAddInput(_:)

<sub>Instance Method</sub>

Determines whether you can add an input to a session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func canAddInput(_ input: AVCaptureInput) -> Bool
```

## Parameters

- `input` — An input to add to the session.

## Return Value

[true](../../swift/true.md) if you can add the input to the session; otherwise, [false](../../swift/false.md).

## Discussion

This method returns [false](../../swift/false.md) if you can’t add an input to a capture session. This occurs, for example, if you attempt to add the input to a session twice, or if the input already belongs to another capture session.

## See Also

### Configuring inputs

- [inputs](inputs.md) — The inputs that provide media data to a capture session.
- [- addInput:](<addinput(__).md>) — Adds a capture input to the session.
- [- removeInput:](<removeinput(__).md>) — Removes an input from the session.
