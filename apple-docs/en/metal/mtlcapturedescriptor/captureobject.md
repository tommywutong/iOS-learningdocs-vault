---
title: captureObject
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcapturedescriptor/captureobject
source_url: 'https://developer.apple.com/documentation/metal/mtlcapturedescriptor/captureobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcapturedescriptor/captureobject.json'
content_hash: 'sha256:0d5d46cfdb620c08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCaptureDescriptor](../mtlcapturedescriptor.md)

# captureObject

<sub>Instance Property</sub>

The instance whose contents should be captured.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var captureObject: Any? { get set }
```

## Discussion

The default value is `nil`, but you need to set an instance before using this descriptor to start a capture session.

The behavior of the capture session depends on the kind of instance being captured:

- Specify an [MTLDevice](../mtldevice.md) instance to capture commands in command buffers created on any command queues created by the device instance.
- Specify an [MTLCommandQueue](../mtlcommandqueue.md) instance to capture commands in command buffers created by a specific command queue.
- Specify an [MTLCaptureScope](../mtlcapturescope.md) instance to indirectly define which commands are captured.

## See Also

### Setting capture parameters

- [destination](destination.md) — The destination for any captured command data.
- [outputURL](outputurl.md) — A URL for a file to write the capture data into.
