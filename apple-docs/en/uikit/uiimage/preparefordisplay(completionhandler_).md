---
title: 'prepareForDisplay(completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/preparefordisplay(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/preparefordisplay(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/preparefordisplay%28completionhandler%3A%29.json'
content_hash: 'sha256:4e3bccfc4455185d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# prepareForDisplay(completionHandler:)

<sub>Instance Method</sub>

Decodes an image asynchronously and provides a new one for display in views and animations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func prepareForDisplay(completionHandler: @escaping @Sendable (UIImage?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func byPreparingForDisplay() async -> UIImage?
```

## Parameters

- `completionHandler` — The closure to call when the function finishes preparing the image. This completion handler takes one parameter: - **`image`** — A new version of the image object for display. If the system can’t decode the image, the parameter value is `nil.`

## Discussion

The Animation Hitches [instrument](https://help.apple.com/instruments/mac/current/) measures system performance for multiple stages of preparing views for display. It can show you the exact cause of an animation hitch, which appears to the user as an interruption or jump in an animation that should be smooth. If Animation Hitches indicates that decoding an image takes too long and causes hitches, use this method to move the decoding work to the background.

This method creates a new image object and passes it to the completion handler. The new image is ready for efficient display by an image view. Assign the image this method creates to the [image](../uilistcontentconfiguration-swift.struct/image.md) property of an image view. If [UIImageView](../uiimageview.md) can render the image without decoding, this method passes the completion handler a valid image without further processing. If the system can’t decode the image, such as an image created from a [CIImage](../../coreimage/ciimage.md), the method passes `nil` to the completion handler`.`

UIKit doesn’t associate the prepared image with the original, or with any related variants from an asset catalog. If your app environment dynamically changes display traits, listen for changes in the trait environment and prepare new images when the environment changes.

```swift
func collectionView(_ collectionView: UICollectionView, prefetchItemsAt indexPaths: [IndexPath]) {
    for path in indexPaths {
        let item = models[path.item]
        if preparedImageCache.object(forKey: item.id) == nil {
            item.loadAsset()
            item.image.prepareForDisplay { [weak preparedImageCache] preparedImage in
                if let preparedImage = preparedImage {
                    preparedImageCache?.setObject(preparedImage, forKey: item.id)
                }
            }
        }
    }
}
```

## See Also

### Loading images for display

- [- imageByPreparingForDisplay](<preparingfordisplay().md>) — Decodes an image synchronously and provides a new one for display in views and animations.
- [- imageByPreparingThumbnailOfSize:](<preparingthumbnail(of_).md>) — Returns a new thumbnail image at the specified size.
- [- prepareThumbnailOfSize:completionHandler:](<preparethumbnail(of_completionhandler_).md>) — Creates a thumbnail image at the specified size asynchronously on a background thread.
