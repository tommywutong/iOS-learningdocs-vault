---
title: commandQueue
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcapturescope/commandqueue
source_url: 'https://developer.apple.com/documentation/metal/mtlcapturescope/commandqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcapturescope/commandqueue.json'
content_hash: 'sha256:f69e4316f6ec3fd9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCaptureScope](../mtlcapturescope.md)

# commandQueue

<sub>Instance Property</sub>

The command queue that this capture scope uses to limit which commands are recorded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var commandQueue: (any MTLCommandQueue)? { get }
```

## Discussion

This value is only available if you created the capture scope by calling the [- newCaptureScopeWithCommandQueue:](<../mtlcapturemanager/makecapturescope(commandqueue_)-1rozd.md>) method. Otherwise, the value is `nil`.

## See Also

### Identifying the capture scope

- [label](label.md) — A string that helps you identify the capture scope.
- [device](device.md) — The device object from which you created the capture scope.
