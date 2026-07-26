---
title: 'applyingExifOrientation(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avdepthdata/applyingexiforientation(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avdepthdata/applyingexiforientation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdepthdata/applyingexiforientation%28_%3A%29.json'
content_hash: 'sha256:bef3f7e34beaf52f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDepthData](../avdepthdata.md)

# applyingExifOrientation(_:)

<sub>Instance Method</sub>

Returns a derivative depth data object by mirroring or rotating it to the specified orientation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func applyingExifOrientation(_ exifOrientation: CGImagePropertyOrientation) -> Self
```

## Parameters

- `exifOrientation` — The image orientation to apply to the depth data map.

## Return Value

A new, transformed depth data object.

## Discussion

When applying simple 90-degree rotation or mirroring edits to media containing depth data, you may use this method to create a derivative copy of the depth in which the specified orientation is applied to both the underlying pixel map data and the camera calibration data. This method throws an exception if you pass an unrecognized `exifOrientation` value.

A depth data object does not contain orientation metadata; this method assumes the data is in the default [CGImagePropertyOrientation.up](../../imageio/cgimagepropertyorientation/up.md) orientation and applies the transformation necessary to produce the orientation you specify.

## See Also

### Transforming and processing

- [- depthDataByConvertingToDepthDataType:](<converting(todepthdatatype_).md>) — Returns a derivative depth data object by converting the depth data map to the specified data type.
- [availableDepthDataTypes](availabledepthdatatypes-3ifx1.md) — The list of depth data formats to which you can convert this depth data.
- [- depthDataByReplacingDepthDataMapWithPixelBuffer:error:](<replacingdepthdatamap(with_).md>) — Returns a derivative depth data object by replacing the depth data map.
