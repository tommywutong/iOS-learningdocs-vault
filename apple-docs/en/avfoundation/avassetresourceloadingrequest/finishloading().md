---
title: finishLoading()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingrequest/finishloading()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/finishloading()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingrequest/finishloading%28%29.json'
content_hash: 'sha256:f7233b94944d42ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingRequest](../avassetresourceloadingrequest.md)

# finishLoading()

<sub>Instance Method</sub>

Causes the receiver to treat the processing of the request as complete.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func finishLoading()
```

## Discussion

If a [dataRequest](datarequest.md) is present and the resource does not contain the full extent of the data that has been requested according to the values of the [requestedOffset](../avassetresourceloadingdatarequest/requestedoffset.md) and [requestedLength](../avassetresourceloadingdatarequest/requestedlength.md) properties of the request, invoke `finishLoading` after providing as much of the requested data as the resource contains.

## See Also

### Reporting the result of the request

- [response](response.md) — The URL response for the loading request.
- [cancelled](iscancelled.md) — A Boolean value that indicates whether the request has been cancelled.
- [- finishLoadingWithError:](<finishloading(with_).md>) — Causes the receiver to handle the failure to load a resource for which a resource loader’s delegate took responsibility.
- [finished](isfinished.md) — A Boolean value that indicates whether loading of the resource has finished.
- [- finishLoadingWithResponse:data:redirect:](<finishloading(with_data_redirect_).md>) — Causes the receiver to finish loading a resource for which a resource loader’s delegate took responsibility . _(deprecated)_
