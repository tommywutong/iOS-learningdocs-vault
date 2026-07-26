---
title: 'makeCaptureScope(commandQueue:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcapturemanager/makecapturescope(commandqueue:)-1rozd'
source_url: 'https://developer.apple.com/documentation/metal/mtlcapturemanager/makecapturescope(commandqueue:)-1rozd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcapturemanager/makecapturescope%28commandqueue%3A%29-1rozd.json'
content_hash: 'sha256:01060b8a69403def'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCaptureManager](../mtlcapturemanager.md)

# makeCaptureScope(commandQueue:)

<sub>Instance Method</sub>

Creates a capture scope for commands submitted to a specific command queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeCaptureScope(commandQueue: any MTLCommandQueue) -> any MTLCaptureScope
```

## Parameters

- `commandQueue` — The command queue whose commands you want to capture.

## See Also

### Creating a capture scope

- [- newCaptureScopeWithDevice:](<makecapturescope(device_).md>) — Creates a capture scope for commands submitted to a specific device object.
- [defaultCaptureScope](defaultcapturescope.md) — The capture scope to use when a capture is initiated in Xcode.
