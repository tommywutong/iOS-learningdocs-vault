---
title: 'finishLoading(with:data:redirect:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+（10.15 起废弃）, tvOS 9.0+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetresourceloadingrequest/finishloading(with:data:redirect:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/finishloading(with:data:redirect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingrequest/finishloading%28with%3Adata%3Aredirect%3A%29.json'
content_hash: 'sha256:19aed937de338e76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingRequest](../avassetresourceloadingrequest.md)

# finishLoading(with:data:redirect:)

<sub>Instance Method</sub>

Causes the receiver to finish loading a resource for which a resource loader’s delegate took responsibility .

> [!warning] Deprecated
> This method is deprecated. Use the following methods and properties instead: the [response](response.md) property to provide the response object, the [redirect](redirect.md) property when redirecting a request, invoking the [dataRequest](datarequest.md) instance’s[- respondWithData:](<../avassetresourceloadingdatarequest/respond(with_).md>) method to provide data, and the [- finishLoading](<finishloading().md>) method to indicate that loading is finished.

<sub>macOS, tvOS</sub>

```swift
func finishLoading(with response: URLResponse?, data: Data?, redirect: URLRequest?)
```

## Parameters

- `response` — The response object for the requested resource. Use the request object in the receiver’s [request](request.md) property to get information about the requested resource.

- `data` — The data of the resource. If no data is available, specify `nil`.

- `redirect` — When redirecting a resource request, use this parameter to specify the corresponding [NSURLRequest](../../foundation/nsurlrequest.md) object. If you are handling the request and not redirecting it, specify `nil`.

## Discussion

When a resource loader’s delegate takes responsibility for loading a resource, it calls this method to indicate that the resource was loaded successfully. This method marks the loading request as finished and returns the provided data back to the resource loader object for processing.

## See Also

### Reporting the result of the request

- [response](response.md) — The URL response for the loading request.
- [- finishLoading](<finishloading().md>) — Causes the receiver to treat the processing of the request as complete.
- [cancelled](iscancelled.md) — A Boolean value that indicates whether the request has been cancelled.
- [- finishLoadingWithError:](<finishloading(with_).md>) — Causes the receiver to handle the failure to load a resource for which a resource loader’s delegate took responsibility.
- [finished](isfinished.md) — A Boolean value that indicates whether loading of the resource has finished.
