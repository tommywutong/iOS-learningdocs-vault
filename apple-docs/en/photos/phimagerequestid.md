---
title: PHImageRequestID
framework: Photos
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestid
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestid.json'
content_hash: 'sha256:ed4b92a32c899400'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHImageRequestID

<sub>Type Alias</sub>

A numeric identifier for an asynchronous image request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias PHImageRequestID = Int32
```

## Discussion

Pass this identifier to the [- cancelImageRequest:](<phimagemanager/cancelimagerequest(__).md>) method if you need to cancel a request before it completes.

## See Also

### Canceling a Request

- [- cancelImageRequest:](<phimagemanager/cancelimagerequest(__).md>) — Cancels an asynchronous request
- [PHInvalidImageRequestID](phinvalidimagerequestid.md) — A special value provided for asynchronous image requests that cannot be canceled.
