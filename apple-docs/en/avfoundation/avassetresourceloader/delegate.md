---
title: delegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloader/delegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloader/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloader/delegate.json'
content_hash: 'sha256:22513f3eca343a12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoader](../avassetresourceloader.md)

# delegate

<sub>Instance Property</sub>

The delegate object to use when handling resource requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
weak var delegate: (any AVAssetResourceLoaderDelegate)? { get }
```

## Discussion

The delegate object is responsible for indicating whether or not it is able to handle a resource request. And for those requests it does handle, the delegate object must initiate the loading of the requested resource.

## See Also

### Accessing the delegate

- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the delegate and dispatch queue to use with the resource loader.
- [AVAssetResourceLoaderDelegate](../avassetresourceloaderdelegate.md) — Methods you can implement to handle resource-loading requests coming from a URL asset.
- [delegateQueue](delegatequeue.md) — The dispatch queue to use when handling resource requests.
