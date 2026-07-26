---
title: 'cancelRequest(withRequestID:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phlivephoto/cancelrequest(withrequestid:)'
source_url: 'https://developer.apple.com/documentation/photos/phlivephoto/cancelrequest(withrequestid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephoto/cancelrequest%28withrequestid%3A%29.json'
content_hash: 'sha256:1acfa204ce83066a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHLivePhoto](../phlivephoto.md)

# cancelRequest(withRequestID:)

<sub>Type Method</sub>

Cancels an asynchronous request

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func cancelRequest(withRequestID requestID: PHLivePhotoRequestID)
```

## Parameters

- `requestID` — The numeric identifier of the request to be canceled.

## Discussion

When you use the [+ requestLivePhotoWithResourceFileURLs:placeholderImage:targetSize:contentMode:resultHandler:](<request(withresourcefileurls_placeholderimage_targetsize_contentmode_resulthandler_).md>) method to asynchronously load a Live Photo from resource files, the method returns a numeric identifier for the request. To cancel the request before it completes, provide the identifier when calling the [+ cancelLivePhotoRequestWithRequestID:](<cancelrequest(withrequestid_).md>) method.

## See Also

### Loading a Live Photo from Data Files

- [+ requestLivePhotoWithResourceFileURLs:placeholderImage:targetSize:contentMode:resultHandler:](<request(withresourcefileurls_placeholderimage_targetsize_contentmode_resulthandler_).md>) — Asynchronously loads a Live Photo from the specified resource files.
