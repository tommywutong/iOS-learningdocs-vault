---
title: 'requestLivePhoto(for:targetSize:contentMode:options:resultHandler:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phimagemanager/requestlivephoto(for:targetsize:contentmode:options:resulthandler:)'
source_url: 'https://developer.apple.com/documentation/photos/phimagemanager/requestlivephoto(for:targetsize:contentmode:options:resulthandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagemanager/requestlivephoto%28for%3Atargetsize%3Acontentmode%3Aoptions%3Aresulthandler%3A%29.json'
content_hash: 'sha256:ca66cfac7fa6a4d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageManager](../phimagemanager.md)

# requestLivePhoto(for:targetSize:contentMode:options:resultHandler:)

<sub>Instance Method</sub>

Requests a Live Photo representation for the specified asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func requestLivePhoto(for asset: PHAsset, targetSize: CGSize, contentMode: PHImageContentMode, options: PHLivePhotoRequestOptions?, resultHandler: @escaping (PHLivePhoto?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID
```

## Parameters

- `asset` — The asset whose Live Photo data is to be loaded.

- `targetSize` — The target size of Live Photo to be returned.

- `contentMode` — An option for how to fit the image to the aspect ratio of the requested size. For details, see [PHImageContentMode](../phimagecontentmode.md).

- `options` — Options specifying how Photos should handle the request, format the requested image, and notify your app of progress or errors. For details, see [PHLivePhotoRequestOptions](../phlivephotorequestoptions.md).

- `resultHandler` — A block to be called when image loading is complete, providing the requested image or information about the status of the request. The block takes the following parameters: - **result** — The requested Live Photo object. - **info** — A dictionary providing information about the status of the request. See [Image Result Info Keys](../../photokit/image-result-info-keys.md) for possible keys and values.

## Return Value

A numeric identifier for the request. If you need to cancel the request before it completes, pass this identifier to the [- cancelImageRequest:](<cancelimagerequest(__).md>) method.

## Discussion

A Live Photo is a picture, taken with a supported device, that includes movement and sound from the moments just before and after its capture. Much like how a [UIImage](../../uikit/uiimage.md) object represents a ready-to-use form of an image, a [PHLivePhoto](../phlivephoto.md) object represents a Live Photo whose image, motion, and sound data are prepared for display. Use this method to request an asset’s Live Photo form; after Photos calls your `resultHandler` block to provide the Live Photo, you can display it using the [PHLivePhotoView](../../photosui/phlivephotoview.md) class.

> [!note] Note
> Use this method only when you plan to display the motion and sound content associated with a Live Photo. In contexts where you need only a still image for a Live Photo asset—for example, when loading thumbnails to display in a photo chooser interface—use the [- requestImageForAsset:targetSize:contentMode:options:resultHandler:](<requestimage(for_targetsize_contentmode_options_resulthandler_).md>) method instead.

When you call this method, Photos loads or generates a [PHLivePhoto](../phlivephoto.md) object for the asset at, or near, the size you specify. Next, it calls your `resultHandler` block to provide the requested image. To serve your request more quickly, Photos may provide an image that is slightly larger than the target size—either because such an image is already cached or because it can be generated more efficiently. Depending on the options you specify and the current state of the asset, Photos may download asset data from the network. This method always executes asynchronously.

Photos may call your result handler block more than once. Photos first calls the block to provide a low-quality image suitable for displaying temporarily while it prepares a high-quality image. (If low-quality image data is immediately available, the first call may occur before the method returns.) When the high-quality image is ready, Photos calls your result handler again to provide it. If the image manager has already cached the requested image at full quality, Photos calls your result handler only once. The [PHImageResultIsDegradedKey](../phimageresultisdegradedkey.md) key in the result handler’s `info` parameter indicates when Photos is providing a temporary low-quality image.
