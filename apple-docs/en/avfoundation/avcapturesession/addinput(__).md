---
title: 'addInput(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesession/addinput(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/addinput(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/addinput%28_%3A%29.json'
content_hash: 'sha256:9a02594b227eb0f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# addInput(_:)

<sub>Instance Method</sub>

Adds a capture input to the session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addInput(_ input: AVCaptureInput)
```

## Parameters

- `input` — An input to add to the session.

## Discussion

It’s only valid to call this method if [- canAddInput:](<canaddinput(__).md>) returns [true](../../swift/true.md).

You can invoke this method while the session is running.

## See Also

### Configuring inputs

- [inputs](inputs.md) — The inputs that provide media data to a capture session.
- [- canAddInput:](<canaddinput(__).md>) — Determines whether you can add an input to a session.
- [- removeInput:](<removeinput(__).md>) — Removes an input from the session.
