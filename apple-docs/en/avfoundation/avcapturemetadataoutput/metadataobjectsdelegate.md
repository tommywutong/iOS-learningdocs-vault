---
title: metadataObjectsDelegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemetadataoutput/metadataobjectsdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/metadataobjectsdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemetadataoutput/metadataobjectsdelegate.json'
content_hash: 'sha256:c96a5f413f552ac8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMetadataOutput](../avcapturemetadataoutput.md)

# metadataObjectsDelegate

<sub>Instance Property</sub>

The delegate of the capture metadata output object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var metadataObjectsDelegate: (any AVCaptureMetadataOutputObjectsDelegate)? { get }
```

## Discussion

The delegate object must conform to the [AVCaptureMetadataOutputObjectsDelegate](../avcapturemetadataoutputobjectsdelegate.md) protocol. The object in this property is used to process all metadata objects captured from the capture metadata output object’s connection.

To set the delegate object, you must use the [- setMetadataObjectsDelegate:queue:](<setmetadataobjectsdelegate(__queue_).md>) method.

## See Also

### Receiving captured metadata objects

- [- setMetadataObjectsDelegate:queue:](<setmetadataobjectsdelegate(__queue_).md>) — Sets the delegate and dispatch queue to use handle callbacks.
- [metadataObjectsCallbackQueue](metadataobjectscallbackqueue.md) — The dispatch queue on which to execute the delegate’s methods.
- [AVCaptureMetadataOutputObjectsDelegate](../avcapturemetadataoutputobjectsdelegate.md) — Methods for receiving metadata produced by a metadata capture output.
