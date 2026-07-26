---
title: outputs
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/outputs
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/outputs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/outputs.json'
content_hash: 'sha256:d9228f7ab271fb68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# outputs

<sub>Instance Property</sub>

The output destinations to which a captures session sends its data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var outputs: [AVCaptureOutput] { get }
```

## Discussion

You add new outputs to a capture session by calling its [- addOutput:](<addoutput(__).md>) method.

## See Also

### Configuring outputs

- [- canAddOutput:](<canaddoutput(__).md>) — Determines whether you can add an output to a session.
- [- addOutput:](<addoutput(__).md>) — Adds an output to the capture session.
- [- removeOutput:](<removeoutput(__).md>) — Removes an output from a capture session.
