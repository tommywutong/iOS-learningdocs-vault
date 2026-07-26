---
title: requestsAllDataToEndOfResource
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingdatarequest/requestsalldatatoendofresource
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/requestsalldatatoendofresource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingdatarequest/requestsalldatatoendofresource.json'
content_hash: 'sha256:1efdf091beaa2b45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingDataRequest](../avassetresourceloadingdatarequest.md)

# requestsAllDataToEndOfResource

<sub>Instance Property</sub>

A Boolean value that indicates the entire remaining length of the resource from the offest to the end of the resource is being requested.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requestsAllDataToEndOfResource: Bool { get }
```

## Discussion

When this property is true, you should disregard the value of requestedLength and incrementally provide as much data, starting from the requested offset, as the resource contains. Continue until all available data was successfully loaded, the request was cancelled, or an error occurs.

## See Also

### Providing data to a request

- [- respondWithData:](<respond(with_).md>) — Provides data to the loading request.
- [requestedLength](requestedlength.md) — The length, in bytes, of the data requested.
- [requestedOffset](requestedoffset.md) — The position within the resource of the first byte requested.
- [currentOffset](currentoffset.md) — The position within the resource of the next byte.
