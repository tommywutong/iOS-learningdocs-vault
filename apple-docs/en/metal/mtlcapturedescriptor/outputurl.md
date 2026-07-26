---
title: outputURL
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcapturedescriptor/outputurl
source_url: 'https://developer.apple.com/documentation/metal/mtlcapturedescriptor/outputurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcapturedescriptor/outputurl.json'
content_hash: 'sha256:e3a9db923c0edb31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCaptureDescriptor](../mtlcapturedescriptor.md)

# outputURL

<sub>Instance Property</sub>

A URL for a file to write the capture data into.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var outputURL: URL? { get set }
```

## Discussion

The default value is `nil`. If you set [destination](destination.md) to [MTLCaptureDestinationGPUTraceDocument](../mtlcapturedestination/gputracedocument.md), you need to set this property to where you want the file to be written to.

## See Also

### Setting capture parameters

- [captureObject](captureobject.md) — The instance whose contents should be captured.
- [destination](destination.md) — The destination for any captured command data.
