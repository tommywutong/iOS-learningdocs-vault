---
title: PHLivePhotoInfoCancelledKey
framework: Photos
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotoinfocancelledkey
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoinfocancelledkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoinfocancelledkey.json'
content_hash: 'sha256:fef726c86768ab1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHLivePhotoInfoCancelledKey

<sub>Global Variable</sub>

A Boolean (`NSNumber`) value indicating whether the Live Photo loading request was canceled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let PHLivePhotoInfoCancelledKey: String
```

## Discussion

If you call the [+ cancelLivePhotoRequestWithRequestID:](<phlivephoto/cancelrequest(withrequestid_).md>) method to cancel a request, Photos calls your result handler block with a `true` value for this key.

## See Also

### Constants

- [PHLivePhotoInfoErrorKey](phlivephotoinfoerrorkey.md) — An error that occurred while attempting to load the requested Live Photo.
- [PHLivePhotoInfoIsDegradedKey](phlivephotoinfoisdegradedkey.md) — A Boolean (`NSNumber`) value indicating whether the result Live Photo is a low-quality substitute for the requested Live Photo.
