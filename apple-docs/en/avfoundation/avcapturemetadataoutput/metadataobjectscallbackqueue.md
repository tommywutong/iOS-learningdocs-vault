---
title: metadataObjectsCallbackQueue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemetadataoutput/metadataobjectscallbackqueue
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/metadataobjectscallbackqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemetadataoutput/metadataobjectscallbackqueue.json'
content_hash: 'sha256:9aa96b055853598a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMetadataOutput](../avcapturemetadataoutput.md)

# metadataObjectsCallbackQueue

<sub>Instance Property</sub>

The dispatch queue on which to execute the delegate’s methods.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var metadataObjectsCallbackQueue: dispatch_queue_t? { get }
```

## Discussion

To set the dispatch queue, you must use the [- setMetadataObjectsDelegate:queue:](<setmetadataobjectsdelegate(__queue_).md>) method.

## See Also

### Receiving captured metadata objects

- [- setMetadataObjectsDelegate:queue:](<setmetadataobjectsdelegate(__queue_).md>) — Sets the delegate and dispatch queue to use handle callbacks.
- [metadataObjectsDelegate](metadataobjectsdelegate.md) — The delegate of the capture metadata output object.
- [AVCaptureMetadataOutputObjectsDelegate](../avcapturemetadataoutputobjectsdelegate.md) — Methods for receiving metadata produced by a metadata capture output.
