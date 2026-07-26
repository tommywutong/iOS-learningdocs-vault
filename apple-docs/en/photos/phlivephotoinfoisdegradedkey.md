---
title: PHLivePhotoInfoIsDegradedKey
framework: Photos
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotoinfoisdegradedkey
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoinfoisdegradedkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoinfoisdegradedkey.json'
content_hash: 'sha256:5e332d90103f135f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHLivePhotoInfoIsDegradedKey

<sub>Global Variable</sub>

A Boolean (`NSNumber`) value indicating whether the result Live Photo is a low-quality substitute for the requested Live Photo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let PHLivePhotoInfoIsDegradedKey: String
```

## Discussion

If `true`, the `result` parameter of your `resultHandler` block contains a still or low-quality Live Photo, and Photos will call your result handler block again to provide the full motion and sound content of the Live Photo. If `false`, Photos has provided all possible data and will not call your result handler again.

## See Also

### Constants

- [PHLivePhotoInfoErrorKey](phlivephotoinfoerrorkey.md) — An error that occurred while attempting to load the requested Live Photo.
- [PHLivePhotoInfoCancelledKey](phlivephotoinfocancelledkey.md) — A Boolean (`NSNumber`) value indicating whether the Live Photo loading request was canceled.
