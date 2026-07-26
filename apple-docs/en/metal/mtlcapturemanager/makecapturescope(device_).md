---
title: 'makeCaptureScope(device:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcapturemanager/makecapturescope(device:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcapturemanager/makecapturescope(device:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcapturemanager/makecapturescope%28device%3A%29.json'
content_hash: 'sha256:0304cfdde7927440'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCaptureManager](../mtlcapturemanager.md)

# makeCaptureScope(device:)

<sub>Instance Method</sub>

Creates a capture scope for commands submitted to a specific device object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeCaptureScope(device: any MTLDevice) -> any MTLCaptureScope
```

## Parameters

- `device` — The device object whose commands you want to capture.

## Discussion

The capture scope captures commands in command buffers created on any command queues created by the device object.

## See Also

### Creating a capture scope

- [- newCaptureScopeWithCommandQueue:](<makecapturescope(commandqueue_)-1rozd.md>) — Creates a capture scope for commands submitted to a specific command queue.
- [defaultCaptureScope](defaultcapturescope.md) — The capture scope to use when a capture is initiated in Xcode.
