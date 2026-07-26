---
title: 'cancelImageRequest(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phimagemanager/cancelimagerequest(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phimagemanager/cancelimagerequest(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagemanager/cancelimagerequest%28_%3A%29.json'
content_hash: 'sha256:71c02d2ef7a09ed8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageManager](../phimagemanager.md)

# cancelImageRequest(_:)

<sub>Instance Method</sub>

Cancels an asynchronous request

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func cancelImageRequest(_ requestID: PHImageRequestID)
```

## Parameters

- `requestID` — The numeric identifier of the request to be canceled.

## Discussion

When you perform an asynchronous request for image data using the [- requestImageForAsset:targetSize:contentMode:options:resultHandler:](<requestimage(for_targetsize_contentmode_options_resulthandler_).md>) method, or for a video object using one of the methods listed in Requesting Video Objects, the image manager returns a numeric identifier for the request. To cancel the request before it completes, provide this identifier when calling the [- cancelImageRequest:](<cancelimagerequest(__).md>) method.

## See Also

### Canceling a Request

- [PHImageRequestID](../phimagerequestid.md) — A numeric identifier for an asynchronous image request.
- [PHInvalidImageRequestID](../phinvalidimagerequestid.md) — A special value provided for asynchronous image requests that cannot be canceled.
