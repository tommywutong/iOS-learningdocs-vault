---
title: 'respond(with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetresourceloadingdatarequest/respond(with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/respond(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingdatarequest/respond%28with%3A%29.json'
content_hash: 'sha256:6458889a97bc07e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingDataRequest](../avassetresourceloadingdatarequest.md)

# respond(with:)

<sub>Instance Method</sub>

Provides data to the loading request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func respond(with data: Data)
```

## Parameters

- `data` — An instance of NSData containing some or all of the requested bytes.

## Discussion

This method may be invoked multiple times on the same instance of `AVAssetResourceLoadingDataRequest` to provide the full range of requested data incrementally. Upon each invocation, the value of the [currentOffset](currentoffset.md) property is updated to match the amount of data provided.

## See Also

### Providing data to a request

- [requestedLength](requestedlength.md) — The length, in bytes, of the data requested.
- [requestedOffset](requestedoffset.md) — The position within the resource of the first byte requested.
- [currentOffset](currentoffset.md) — The position within the resource of the next byte.
- [requestsAllDataToEndOfResource](requestsalldatatoendofresource.md) — A Boolean value that indicates the entire remaining length of the resource from the offest to the end of the resource is being requested.
