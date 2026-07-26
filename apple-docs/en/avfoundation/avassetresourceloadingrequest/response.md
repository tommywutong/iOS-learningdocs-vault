---
title: response
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingrequest/response
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/response'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingrequest/response.json'
content_hash: 'sha256:886debb48410e491'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingRequest](../avassetresourceloadingrequest.md)

# response

<sub>Instance Property</sub>

The URL response for the loading request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var response: URLResponse? { get set }
```

## Discussion

The value of this property is an instance of [URLResponse](../../foundation/urlresponse.md), indicating a response to the loading request. If no response is needed, the value of this property is `nil`.

## See Also

### Reporting the result of the request

- [- finishLoading](<finishloading().md>) — Causes the receiver to treat the processing of the request as complete.
- [cancelled](iscancelled.md) — A Boolean value that indicates whether the request has been cancelled.
- [- finishLoadingWithError:](<finishloading(with_).md>) — Causes the receiver to handle the failure to load a resource for which a resource loader’s delegate took responsibility.
- [finished](isfinished.md) — A Boolean value that indicates whether loading of the resource has finished.
- [- finishLoadingWithResponse:data:redirect:](<finishloading(with_data_redirect_).md>) — Causes the receiver to finish loading a resource for which a resource loader’s delegate took responsibility . _(deprecated)_
