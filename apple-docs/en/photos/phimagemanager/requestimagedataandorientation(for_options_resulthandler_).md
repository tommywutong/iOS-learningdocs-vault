---
title: 'requestImageDataAndOrientation(for:options:resultHandler:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phimagemanager/requestimagedataandorientation(for:options:resulthandler:)'
source_url: 'https://developer.apple.com/documentation/photos/phimagemanager/requestimagedataandorientation(for:options:resulthandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagemanager/requestimagedataandorientation%28for%3Aoptions%3Aresulthandler%3A%29.json'
content_hash: 'sha256:a66dcca765e99cf9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageManager](../phimagemanager.md)

# requestImageDataAndOrientation(for:options:resultHandler:)

<sub>Instance Method</sub>

Requests the largest represented image as data bytes and EXIF orientation for the specified asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func requestImageDataAndOrientation(for asset: PHAsset, options: PHImageRequestOptions?, resultHandler: @escaping (Data?, String?, CGImagePropertyOrientation, [AnyHashable : Any]?) -> Void) -> PHImageRequestID
```

## Parameters

- `asset` — The asset for which to load image data.

- `options` — Options specifying how Photos should handle the request, format the requested image, and notify your app of progress or errors. If [PHImageRequestOptionsVersionCurrent](../phimagerequestoptionsversion/current.md) is requested and the asset has adjustments, the largest rendered image data is returned. In all other cases, the original image data is returned. For further details, see [PHImageRequestOptions](../phimagerequestoptions.md).

- `resultHandler` — A block called, exactly once, when image loading is complete, providing the requested image or information about the status of the request. The block takes the following parameters: - **imageData** — The requested image. - **dataUTI** — The uniform type identifier for the image. - **orientation** — The EXIF orientation for the image, as a [CGImagePropertyOrientation](../../imageio/cgimagepropertyorientation.md). For iOS or tvOS, convert this orientation to a [UIImage.Orientation](../../uikit/uiimage/orientation.md). - **info** — A dictionary providing information about the status of the request. See [Image Result Info Keys](../../photokit/image-result-info-keys.md) for possible keys and values.

## Return Value

A numeric identifier for the request. If you need to cancel the request before it completes, pass this identifier to the [- cancelImageRequest:](<cancelimagerequest(__).md>) method.

## Discussion

When you call this method, Photos loads the largest available representation of the image asset, then calls your `resultHandler` block to provide the requested data. Depending on the options you specify and the current state of the asset, Photos may download asset data from the network.

By default, this method executes asynchronously. If you call it from a background thread, you may change the [synchronous](../phimagerequestoptions/issynchronous.md) property of the `options` parameter to `true` to block the calling thread until either the requested image is ready or an error occurs, at which time Photos calls your result handler. This method ignores the [deliveryMode](../phimagerequestoptions/deliverymode.md) option—Photos calls your result handler block exactly once.

If the [version](../phimagerequestoptions/version.md) option is set to [PHImageRequestOptionsVersionCurrent](../phimagerequestoptionsversion/current.md), Photos provides rendered image data, including the results of any edits that have been made to the asset content. Otherwise, Photos provides the originally captured image data for the asset.

## See Also

### Requesting Images

- [- requestImageForAsset:targetSize:contentMode:options:resultHandler:](<requestimage(for_targetsize_contentmode_options_resulthandler_).md>) — Requests an image representation for the specified asset.
- [PHImageManagerMaximumSize](../phimagemanagermaximumsize.md) — A special value for requesting original image data or the largest rendered image available. .
