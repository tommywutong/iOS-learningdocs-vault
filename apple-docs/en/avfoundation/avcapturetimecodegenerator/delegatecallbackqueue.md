---
title: delegateCallbackQueue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecodegenerator/delegatecallbackqueue
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/delegatecallbackqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegenerator/delegatecallbackqueue.json'
content_hash: 'sha256:de52f49adf407bd7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md)

# delegateCallbackQueue

<sub>Instance Property</sub>

The dispatch queue on which delegate callbacks are invoked.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var delegateCallbackQueue: dispatch_queue_t? { get }
```

## Discussion

Provides the queue set in [- setDelegate:queue:](<setdelegate(__queue_).md>). If no delegate is assigned, this property is `nil`.

## See Also

### Handling delegate callbacks

- [delegate](delegate.md) — The delegate that receives timecode updates from the timecode generator.
