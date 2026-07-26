---
title: 'replacingDepthDataMap(with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avdepthdata/replacingdepthdatamap(with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avdepthdata/replacingdepthdatamap(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdepthdata/replacingdepthdatamap%28with%3A%29.json'
content_hash: 'sha256:20148357009b9098'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDepthData](../avdepthdata.md)

# replacingDepthDataMap(with:)

<sub>Instance Method</sub>

Returns a derivative depth data object by replacing the depth data map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func replacingDepthDataMap(with pixelBuffer: CVPixelBuffer) throws -> Self
```

## Parameters

- `pixelBuffer` — A pixel buffer containing depth or disparity information in a compatible format.

## Return Value

A new depth data object containing the pixel buffer.

## Discussion

If you apply simple transforms to media containing depth data, you can use the [- depthDataByApplyingExifOrientation:](<applyingexiforientation(__).md>) method to apply parallel transforms to the corresponding depth data. More complex transforms and edits require creating a derivative depth map reflecting whatever edits you make to the corresponding image. In such cases, use this [- depthDataByReplacingDepthDataMapWithPixelBuffer:error:](<replacingdepthdatamap(with_).md>) method to create a derivative depth data object.

> [!note] Note
> This method cannot ensure correspondence between an arbitrarily edited depth map and the camera parameters that generated the initial depth map, so the new depth data object’s [cameraCalibrationData](cameracalibrationdata.md) property is always `nil`.

## See Also

### Transforming and processing

- [- depthDataByApplyingExifOrientation:](<applyingexiforientation(__).md>) — Returns a derivative depth data object by mirroring or rotating it to the specified orientation.
- [- depthDataByConvertingToDepthDataType:](<converting(todepthdatatype_).md>) — Returns a derivative depth data object by converting the depth data map to the specified data type.
- [availableDepthDataTypes](availabledepthdatatypes-3ifx1.md) — The list of depth data formats to which you can convert this depth data.
