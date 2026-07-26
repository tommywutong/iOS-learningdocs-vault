---
title: 'addOutput(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesession/addoutput(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/addoutput(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/addoutput%28_%3A%29.json'
content_hash: 'sha256:b2a46e3f672e1626'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# addOutput(_:)

<sub>Instance Method</sub>

Adds an output to the capture session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addOutput(_ output: AVCaptureOutput)
```

## Parameters

- `output` — An output to add to the session.

## Discussion

You can only add an output to a session using this method if [- canAddOutput:](<canaddoutput(__).md>) returns [true](../../swift/true.md).

You can invoke this method while the session is running.

## See Also

### Configuring outputs

- [outputs](outputs.md) — The output destinations to which a captures session sends its data.
- [- canAddOutput:](<canaddoutput(__).md>) — Determines whether you can add an output to a session.
- [- removeOutput:](<removeoutput(__).md>) — Removes an output from a capture session.
