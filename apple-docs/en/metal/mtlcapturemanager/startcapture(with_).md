---
title: 'startCapture(with:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcapturemanager/startcapture(with:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcapturemanager/startcapture(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcapturemanager/startcapture%28with%3A%29.json'
content_hash: 'sha256:a9c3a0bb5cb1494b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCaptureManager](../mtlcapturemanager.md)

# startCapture(with:)

<sub>Instance Method</sub>

Starts capturing any of your app’s Metal commands, with the capture session defined by a descriptor object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func startCapture(with descriptor: MTLCaptureDescriptor) throws
```

## Parameters

- `descriptor` — A description of the capture session to create.

## See Also

### Starting capture

- [- startCaptureWithDevice:](<startcapture(device_).md>) — Starts capturing any of your app’s Metal commands that are executed by the device object. _(deprecated)_
- [- startCaptureWithCommandQueue:](<startcapture(commandqueue_).md>) — Starts capturing any of your app’s Metal commands that are executed by the command queue. _(deprecated)_
- [- startCaptureWithScope:](<startcapture(scope_).md>) — Starts capturing any of your app’s Metal commands that are in the specified capture scope. _(deprecated)_
