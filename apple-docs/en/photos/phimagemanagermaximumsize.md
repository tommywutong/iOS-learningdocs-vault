---
title: PHImageManagerMaximumSize
framework: Photos
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagemanagermaximumsize
source_url: 'https://developer.apple.com/documentation/photos/phimagemanagermaximumsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagemanagermaximumsize.json'
content_hash: 'sha256:1faf1584a9ea0ce4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHImageManagerMaximumSize

<sub>Global Variable</sub>

A special value for requesting original image data or the largest rendered image available. .

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let PHImageManagerMaximumSize: CGSize
```

## Discussion

When you use the [PHImageManagerMaximumSize](phimagemanagermaximumsize.md) option, Photos provides the largest image available for the asset without scaling or cropping. (That is, it ignores the [resizeMode](phimagerequestoptions/resizemode.md) option.)

## See Also

### Requesting Images

- [- requestImageForAsset:targetSize:contentMode:options:resultHandler:](<phimagemanager/requestimage(for_targetsize_contentmode_options_resulthandler_).md>) — Requests an image representation for the specified asset.
- [- requestImageDataAndOrientationForAsset:options:resultHandler:](<phimagemanager/requestimagedataandorientation(for_options_resulthandler_).md>) — Requests the largest represented image as data bytes and EXIF orientation for the specified asset.
