---
title: 'setMetadataObjectsDelegate(_:queue:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturemetadataoutput/setmetadataobjectsdelegate(_:queue:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/setmetadataobjectsdelegate(_:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemetadataoutput/setmetadataobjectsdelegate%28_%3Aqueue%3A%29.json'
content_hash: 'sha256:d6501dc0210dac4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMetadataOutput](../avcapturemetadataoutput.md)

# setMetadataObjectsDelegate(_:queue:)

<sub>Instance Method</sub>

Sets the delegate and dispatch queue to use handle callbacks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func setMetadataObjectsDelegate(_ objectsDelegate: (any AVCaptureMetadataOutputObjectsDelegate)?, queue objectsCallbackQueue: dispatch_queue_t?)
```

## Parameters

- `objectsDelegate` — The delegate object to notify when new metadata objects become available. This object must conform to the [AVCaptureMetadataOutputObjectsDelegate](../avcapturemetadataoutputobjectsdelegate.md) protocol.

- `objectsCallbackQueue` — The dispatch queue on which to execute the delegate’s methods. This queue must be a serial queue to ensure that metadata objects are delivered in the order in which they were received. If the `objectsDelegate` parameter is `nil`, you may specify `nil` for this parameter too; otherwise, you must specify a valid dispatch queue.

## Discussion

When new metadata objects are captured from the receiver’s connection, they are vended to the delegate object. All delegate methods are executed on the dispatch queue specified in the `objectsCallbackQueue` parameter. To ensure that metadata objects are processed in a timely manner and not dropped, you should specify a dispatch queue dedicated to processing the objects or that is otherwise not busy.

## See Also

### Receiving captured metadata objects

- [metadataObjectsDelegate](metadataobjectsdelegate.md) — The delegate of the capture metadata output object.
- [metadataObjectsCallbackQueue](metadataobjectscallbackqueue.md) — The dispatch queue on which to execute the delegate’s methods.
- [AVCaptureMetadataOutputObjectsDelegate](../avcapturemetadataoutputobjectsdelegate.md) — Methods for receiving metadata produced by a metadata capture output.
