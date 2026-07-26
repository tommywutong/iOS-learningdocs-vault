---
title: PHImageResultIsDegradedKey
framework: Photos
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimageresultisdegradedkey
source_url: 'https://developer.apple.com/documentation/photos/phimageresultisdegradedkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimageresultisdegradedkey.json'
content_hash: 'sha256:ab154ae942d67c58'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHImageResultIsDegradedKey

<sub>Global Variable</sub>

A key whose value indicates whether the result image is a low-quality substitute for the requested image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let PHImageResultIsDegradedKey: String
```

## Discussion

This key provides information about an image loading result in the `resultHandler` block for methods listed in Requesting Images. The corresponding value is an `NSNumber` object containing a Boolean value.If `true`, the `result` parameter of your `resultHandler` block contains a low-quality image because Photos could not yet provide a higher-quality image. Depending on your settings in the [PHImageRequestOptions](phimagerequestoptions.md) object that you provided with the request, Photos may call your result handler block again to provide a higher-quality image.

## See Also

### Constants

- [PHImageResultIsInCloudKey](phimageresultisincloudkey.md) — A key whose value indicates whether photo asset data is stored on the local device or must be downloaded from iCloud.
- [PHImageResultRequestIDKey](phimageresultrequestidkey.md) — A key whose value is a unique identifier for the image request.
- [PHImageCancelledKey](phimagecancelledkey.md) — A key whose value indicates whether the image request was canceled.
- [PHImageErrorKey](phimageerrorkey.md) — A key whose value is an error that occurred when Photos attempted to load the image.
