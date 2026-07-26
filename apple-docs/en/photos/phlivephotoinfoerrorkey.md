---
title: PHLivePhotoInfoErrorKey
framework: Photos
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotoinfoerrorkey
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoinfoerrorkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoinfoerrorkey.json'
content_hash: 'sha256:83685f60d0735bea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHLivePhotoInfoErrorKey

<sub>Global Variable</sub>

An error that occurred while attempting to load the requested Live Photo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let PHLivePhotoInfoErrorKey: String
```

## Discussion

The [+ requestLivePhotoWithResourceFileURLs:placeholderImage:targetSize:contentMode:resultHandler:](<phlivephoto/request(withresourcefileurls_placeholderimage_targetsize_contentmode_resulthandler_).md>) method validates that the files and their metadata can be loaded as a Live Photo. If Photos cannot load a Live Photo from the specified files, the `result` parameter in your result handler block is `nil`, and this key in the `info` dictionary contains an `NSError` object describing the error.

## See Also

### Constants

- [PHLivePhotoInfoIsDegradedKey](phlivephotoinfoisdegradedkey.md) — A Boolean (`NSNumber`) value indicating whether the result Live Photo is a low-quality substitute for the requested Live Photo.
- [PHLivePhotoInfoCancelledKey](phlivephotoinfocancelledkey.md) — A Boolean (`NSNumber`) value indicating whether the Live Photo loading request was canceled.
