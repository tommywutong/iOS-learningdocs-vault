---
title: 'setDelegate(_:queue:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetresourceloader/setdelegate(_:queue:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloader/setdelegate(_:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloader/setdelegate%28_%3Aqueue%3A%29.json'
content_hash: 'sha256:f2554f77898b6240'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoader](../avassetresourceloader.md)

# setDelegate(_:queue:)

<sub>Instance Method</sub>

Sets the delegate and dispatch queue to use with the resource loader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setDelegate(_ delegate: (any AVAssetResourceLoaderDelegate)?, queue delegateQueue: dispatch_queue_t?)
```

## Parameters

- `delegate` — The delegate object to query when handling resource requests. You may specify `nil` if you want to clear the delegate object. The resource loader does not store a strong reference to the delegate object.

- `delegateQueue` — The dispatch queue on which to execute resource requests. If the `delegate` parameter is not `nil`, this parameter must also not be `nil` and must contain a valid dispatch queue. However, if `delegate` is `nil`, this parameter may also be `nil`. The resource loader maintains a strong reference to the dispatch queue you specify.

## Discussion

You use this method to specify the object to use when handling resource requests and the dispatch queue on which to process those requests. Resource requests are processed synchronously on the dispatch queue you provide.

## See Also

### Accessing the delegate

- [delegate](delegate.md) — The delegate object to use when handling resource requests.
- [AVAssetResourceLoaderDelegate](../avassetresourceloaderdelegate.md) — Methods you can implement to handle resource-loading requests coming from a URL asset.
- [delegateQueue](delegatequeue.md) — The dispatch queue to use when handling resource requests.
