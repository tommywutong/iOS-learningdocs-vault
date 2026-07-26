---
title: 'removeOutput(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesession/removeoutput(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/removeoutput(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/removeoutput%28_%3A%29.json'
content_hash: 'sha256:4e0ae6f9d496d650'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# removeOutput(_:)

<sub>Instance Method</sub>

Removes an output from a capture session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeOutput(_ output: AVCaptureOutput)
```

## Parameters

- `output` — An output to remove from the capture session.

## Discussion

You can call this method while the session is running.

## See Also

### Configuring outputs

- [outputs](outputs.md) — The output destinations to which a captures session sends its data.
- [- canAddOutput:](<canaddoutput(__).md>) — Determines whether you can add an output to a session.
- [- addOutput:](<addoutput(__).md>) — Adds an output to the capture session.
