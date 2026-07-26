---
title: PHAssetResourceDataRequestID
framework: Photos
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourcedatarequestid
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcedatarequestid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcedatarequestid.json'
content_hash: 'sha256:9ad525fb00c74c63'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetResourceDataRequestID

<sub>Type Alias</sub>

A numeric identifier for an asynchronous asset resource loading request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias PHAssetResourceDataRequestID = Int32
```

## Discussion

Pass this identifier to the [- cancelDataRequest:](<phassetresourcemanager/canceldatarequest(__).md>) method if you need to cancel a request before it completes.

## See Also

### Constants

- [Resource Loading Request Identifiers](../photokit/resource-loading-request-identifiers.md) — Special values for the [PHAssetResourceDataRequestID](phassetresourcedatarequestid.md) identifier that are returned by asynchronous requests.
