---
title: delegateQueue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloader/delegatequeue
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloader/delegatequeue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloader/delegatequeue.json'
content_hash: 'sha256:47657f1315744281'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoader](../avassetresourceloader.md)

# delegateQueue

<sub>Instance Property</sub>

The dispatch queue to use when handling resource requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var delegateQueue: dispatch_queue_t? { get }
```

## Discussion

Resource requests are processed synchronously on the specified dispatch queue.

## See Also

### Accessing the delegate

- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the delegate and dispatch queue to use with the resource loader.
- [delegate](delegate.md) — The delegate object to use when handling resource requests.
- [AVAssetResourceLoaderDelegate](../avassetresourceloaderdelegate.md) — Methods you can implement to handle resource-loading requests coming from a URL asset.
