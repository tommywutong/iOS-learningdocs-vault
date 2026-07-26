---
title: PHLivePhotoRequestID
framework: Photos
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotorequestid
source_url: 'https://developer.apple.com/documentation/photos/phlivephotorequestid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotorequestid.json'
content_hash: 'sha256:3af2f3503c032187'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHLivePhotoRequestID

<sub>Type Alias</sub>

A numeric identifier for an asynchronous Live Photo loading request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias PHLivePhotoRequestID = Int32
```

## Discussion

Pass this identifier to the [+ cancelLivePhotoRequestWithRequestID:](<phlivephoto/cancelrequest(withrequestid_).md>) method if you need to cancel a request before it completes.

## See Also

### Constants

- [Image Request Identifiers](../photokit/image-request-identifiers.md) — Special values for the Live Photo request ID that are returned by asynchronous requests.
- [Result Handler Info Dictionary Keys](../photokit/result-handler-info-dictionary-keys.md) — Info describing an attempt to load a Live Photo.
