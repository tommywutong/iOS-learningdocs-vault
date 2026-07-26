---
title: requestedOffset
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingdatarequest/requestedoffset
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/requestedoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingdatarequest/requestedoffset.json'
content_hash: 'sha256:5650b79ca3aae92d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingDataRequest](../avassetresourceloadingdatarequest.md)

# requestedOffset

<sub>Instance Property</sub>

The position within the resource of the first byte requested.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requestedOffset: Int64 { get }
```

## Discussion

When all of the requested bytes that can be provided have been loaded—including the possible [contentInformationRequest](../avassetresourceloadingrequest/contentinformationrequest.md) data in the [AVAssetResourceLoadingRequest](../avassetresourceloadingrequest.md) instance that contains the receiver—the delegate should respond by invoking [- finishLoading](<../avassetresourceloadingrequest/finishloading().md>).

If the `requestedOffset` value is beyond the content length of the resource, the [AVAssetResourceLoadingRequest](../avassetresourceloadingrequest.md) instance is sent a [- finishLoading](<../avassetresourceloadingrequest/finishloading().md>) message without any prior invocations of [- respondWithData:](<respond(with_).md>).

## See Also

### Providing data to a request

- [- respondWithData:](<respond(with_).md>) — Provides data to the loading request.
- [requestedLength](requestedlength.md) — The length, in bytes, of the data requested.
- [currentOffset](currentoffset.md) — The position within the resource of the next byte.
- [requestsAllDataToEndOfResource](requestsalldatatoendofresource.md) — A Boolean value that indicates the entire remaining length of the resource from the offest to the end of the resource is being requested.
