---
title: requestedLength
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingdatarequest/requestedlength
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/requestedlength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingdatarequest/requestedlength.json'
content_hash: 'sha256:c7a16e3127fee037'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingDataRequest](../avassetresourceloadingdatarequest.md)

# requestedLength

<sub>Instance Property</sub>

The length, in bytes, of the data requested.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requestedLength: Int { get }
```

## Discussion

If the content length of the resource is unknown, the sum of the [requestedLength](requestedlength.md) and [requestedOffset](requestedoffset.md) properties may be greater than the actual content length. When this situation occurs, an application must attempt to provide as much of the requested data beginning at the [requestedOffset](requestedoffset.md) property as the resource contains. The application must then invoke either the [AVAssetResourceLoadingRequest](../avassetresourceloadingrequest.md) instance’s [- finishLoading](<../avassetresourceloadingrequest/finishloading().md>) method upon success, or the [- finishLoadingWithError:](<../avassetresourceloadingrequest/finishloading(with_).md>) method if an error is encountered during the loading.

## See Also

### Providing data to a request

- [- respondWithData:](<respond(with_).md>) — Provides data to the loading request.
- [requestedOffset](requestedoffset.md) — The position within the resource of the first byte requested.
- [currentOffset](currentoffset.md) — The position within the resource of the next byte.
- [requestsAllDataToEndOfResource](requestsalldatatoendofresource.md) — A Boolean value that indicates the entire remaining length of the resource from the offest to the end of the resource is being requested.
