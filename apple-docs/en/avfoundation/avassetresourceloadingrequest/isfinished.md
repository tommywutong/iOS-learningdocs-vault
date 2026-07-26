---
title: isFinished
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingrequest/isfinished
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/isfinished'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingrequest/isfinished.json'
content_hash: 'sha256:ecf9a3d019312482'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingRequest](../avassetresourceloadingrequest.md)

# isFinished

<sub>Instance Property</sub>

A Boolean value that indicates whether loading of the resource has finished.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isFinished: Bool { get }
```

## Discussion

The value of this property is [false](../../swift/false.md) initially. The value changes to [true](../../swift/true.md) when the delegate object handling the request calls the [- finishLoadingWithResponse:data:redirect:](<finishloading(with_data_redirect_).md>) or [- finishLoadingWithError:](<finishloading(with_).md>) method.

## See Also

### Reporting the result of the request

- [response](response.md) — The URL response for the loading request.
- [- finishLoading](<finishloading().md>) — Causes the receiver to treat the processing of the request as complete.
- [cancelled](iscancelled.md) — A Boolean value that indicates whether the request has been cancelled.
- [- finishLoadingWithError:](<finishloading(with_).md>) — Causes the receiver to handle the failure to load a resource for which a resource loader’s delegate took responsibility.
- [- finishLoadingWithResponse:data:redirect:](<finishloading(with_data_redirect_).md>) — Causes the receiver to finish loading a resource for which a resource loader’s delegate took responsibility . _(deprecated)_
