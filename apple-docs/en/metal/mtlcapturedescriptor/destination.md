---
title: destination
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcapturedescriptor/destination
source_url: 'https://developer.apple.com/documentation/metal/mtlcapturedescriptor/destination'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcapturedescriptor/destination.json'
content_hash: 'sha256:07e77c9618556504'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCaptureDescriptor](../mtlcapturedescriptor.md)

# destination

<sub>Instance Property</sub>

The destination for any captured command data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var destination: MTLCaptureDestination { get set }
```

## Discussion

The default value is [MTLCaptureDestinationDeveloperTools](../mtlcapturedestination/developertools.md).

## See Also

### Setting capture parameters

- [captureObject](captureobject.md) — The instance whose contents should be captured.
- [outputURL](outputurl.md) — A URL for a file to write the capture data into.
