---
title: isCancelled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingrequest/iscancelled
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/iscancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingrequest/iscancelled.json'
content_hash: 'sha256:38932a91ab135c62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingRequest](../avassetresourceloadingrequest.md)

# isCancelled

<sub>Instance Property</sub>

A Boolean value that indicates whether the request has been cancelled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isCancelled: Bool { get }
```

## Discussion

[true](../../swift/true.md) when the resource loader cancels the loading of a request, just prior to sending the message [- resourceLoader:didCancelLoadingRequest:](<../avassetresourceloaderdelegate/resourceloader(__didcancel_)-3nl51.md>) to the delegate.

## See Also

### Reporting the result of the request

- [response](response.md) — The URL response for the loading request.
- [- finishLoading](<finishloading().md>) — Causes the receiver to treat the processing of the request as complete.
- [- finishLoadingWithError:](<finishloading(with_).md>) — Causes the receiver to handle the failure to load a resource for which a resource loader’s delegate took responsibility.
- [finished](isfinished.md) — A Boolean value that indicates whether loading of the resource has finished.
- [- finishLoadingWithResponse:data:redirect:](<finishloading(with_data_redirect_).md>) — Causes the receiver to finish loading a resource for which a resource loader’s delegate took responsibility . _(deprecated)_
