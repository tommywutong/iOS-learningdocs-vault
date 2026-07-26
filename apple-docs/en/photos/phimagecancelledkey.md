---
title: PHImageCancelledKey
framework: Photos
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagecancelledkey
source_url: 'https://developer.apple.com/documentation/photos/phimagecancelledkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagecancelledkey.json'
content_hash: 'sha256:2465e3ca7ead779f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHImageCancelledKey

<sub>Global Variable</sub>

A key whose value indicates whether the image request was canceled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let PHImageCancelledKey: String
```

## Discussion

This key provides information about an image loading result in the `resultHandler` block for methods listed in Requesting Images. The corresponding value is an `NSNumber` object containing a Boolean value.If you call the [- cancelImageRequest:](<phimagemanager/cancelimagerequest(__).md>) method to cancel a request, Photos calls your result handler block with the value `true` for this key.

## See Also

### Constants

- [PHImageResultIsInCloudKey](phimageresultisincloudkey.md) — A key whose value indicates whether photo asset data is stored on the local device or must be downloaded from iCloud.
- [PHImageResultIsDegradedKey](phimageresultisdegradedkey.md) — A key whose value indicates whether the result image is a low-quality substitute for the requested image.
- [PHImageResultRequestIDKey](phimageresultrequestidkey.md) — A key whose value is a unique identifier for the image request.
- [PHImageErrorKey](phimageerrorkey.md) — A key whose value is an error that occurred when Photos attempted to load the image.
