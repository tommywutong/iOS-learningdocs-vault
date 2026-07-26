---
title: device
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcapturescope/device
source_url: 'https://developer.apple.com/documentation/metal/mtlcapturescope/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcapturescope/device.json'
content_hash: 'sha256:2baf1954bb29d996'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCaptureScope](../mtlcapturescope.md)

# device

<sub>Instance Property</sub>

The device object from which you created the capture scope.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var device: any MTLDevice { get }
```

## See Also

### Identifying the capture scope

- [label](label.md) — A string that helps you identify the capture scope.
- [commandQueue](commandqueue.md) — The command queue that this capture scope uses to limit which commands are recorded.
