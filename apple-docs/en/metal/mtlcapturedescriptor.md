---
title: MTLCaptureDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcapturedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlcapturedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcapturedescriptor.json'
content_hash: 'sha256:60435cc3d23c54c9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCaptureDescriptor

<sub>Class</sub>

A configuration for a Metal capture session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLCaptureDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Setting capture parameters

- [captureObject](mtlcapturedescriptor/captureobject.md) — The instance whose contents should be captured.
- [destination](mtlcapturedescriptor/destination.md) — The destination for any captured command data.
- [outputURL](mtlcapturedescriptor/outputurl.md) — A URL for a file to write the capture data into.

## See Also

### Frame capture

- [MTLCaptureManager](mtlcapturemanager.md) — An instance you use to capture Metal command data in your app.
- [MTLCaptureDestination](mtlcapturedestination.md) — The kinds of destinations for captured command data.
- [MTLCaptureScope](mtlcapturescope.md) — A type that can programmatically customize a GPU frame capture.
