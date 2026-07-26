---
title: 'finishLoading(with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetresourceloadingrequest/finishloading(with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/finishloading(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingrequest/finishloading%28with%3A%29.json'
content_hash: 'sha256:a2262c2902a86032'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingRequest](../avassetresourceloadingrequest.md)

# finishLoading(with:)

<sub>Instance Method</sub>

Causes the receiver to handle the failure to load a resource for which a resource loader’s delegate took responsibility.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func finishLoading(with error: (any Error)?)
```

## Parameters

- `error` — An error object indicating the reason for the failure.

## Discussion

When a resource loader’s delegate takes responsibility for loading a resource, it calls this method when a failure occurred when loading the resource. This method marks the loading request as finished and notifies the resource loader object that the resource could not be loaded.

## See Also

### Reporting the result of the request

- [response](response.md) — The URL response for the loading request.
- [- finishLoading](<finishloading().md>) — Causes the receiver to treat the processing of the request as complete.
- [cancelled](iscancelled.md) — A Boolean value that indicates whether the request has been cancelled.
- [finished](isfinished.md) — A Boolean value that indicates whether loading of the resource has finished.
- [- finishLoadingWithResponse:data:redirect:](<finishloading(with_data_redirect_).md>) — Causes the receiver to finish loading a resource for which a resource loader’s delegate took responsibility . _(deprecated)_
