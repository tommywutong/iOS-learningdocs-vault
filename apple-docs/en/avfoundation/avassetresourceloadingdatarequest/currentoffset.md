---
title: currentOffset
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingdatarequest/currentoffset
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/currentoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingdatarequest/currentoffset.json'
content_hash: 'sha256:a65cc783f05e8294'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingDataRequest](../avassetresourceloadingdatarequest.md)

# currentOffset

<sub>Instance Property</sub>

The position within the resource of the next byte.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var currentOffset: Int64 { get }
```

## Discussion

When incrementally loading data you should begin loading at this offset, returning the data by invoking the [- respondWithData:](<respond(with_).md>) method. Bytes previous to this value have already been provided.

## See Also

### Providing data to a request

- [- respondWithData:](<respond(with_).md>) — Provides data to the loading request.
- [requestedLength](requestedlength.md) — The length, in bytes, of the data requested.
- [requestedOffset](requestedoffset.md) — The position within the resource of the first byte requested.
- [requestsAllDataToEndOfResource](requestsalldatatoendofresource.md) — A Boolean value that indicates the entire remaining length of the resource from the offest to the end of the resource is being requested.
