---
title: PHImageResultRequestIDKey
framework: Photos
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimageresultrequestidkey
source_url: 'https://developer.apple.com/documentation/photos/phimageresultrequestidkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimageresultrequestidkey.json'
content_hash: 'sha256:7dda02649034aa1d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHImageResultRequestIDKey

<sub>Global Variable</sub>

A key whose value is a unique identifier for the image request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let PHImageResultRequestIDKey: String
```

## Discussion

This key provides information about an image loading result in the `resultHandler` block for methods listed in Requesting Images. The corresponding value is an `NSNumber` object containing an integer value.This identifier matches that returned when making a request. You can use it with the [- cancelImageRequest:](<phimagemanager/cancelimagerequest(__).md>) method to cancel requests with pending results that are no longer needed.

## See Also

### Constants

- [PHImageResultIsInCloudKey](phimageresultisincloudkey.md) — A key whose value indicates whether photo asset data is stored on the local device or must be downloaded from iCloud.
- [PHImageResultIsDegradedKey](phimageresultisdegradedkey.md) — A key whose value indicates whether the result image is a low-quality substitute for the requested image.
- [PHImageCancelledKey](phimagecancelledkey.md) — A key whose value indicates whether the image request was canceled.
- [PHImageErrorKey](phimageerrorkey.md) — A key whose value is an error that occurred when Photos attempted to load the image.
