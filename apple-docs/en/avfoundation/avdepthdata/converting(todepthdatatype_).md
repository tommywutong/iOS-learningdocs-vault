---
title: 'converting(toDepthDataType:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avdepthdata/converting(todepthdatatype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avdepthdata/converting(todepthdatatype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdepthdata/converting%28todepthdatatype%3A%29.json'
content_hash: 'sha256:81aec9ab3a92bf47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDepthData](../avdepthdata.md)

# converting(toDepthDataType:)

<sub>Instance Method</sub>

Returns a derivative depth data object by converting the depth data map to the specified data type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func converting(toDepthDataType depthDataType: OSType) -> Self
```

## Parameters

- `depthDataType` — The data type to convert to. This value must be one of the formats present in the [availableDepthDataTypes](availabledepthdatatypes-472g0.md) array.

## Return Value

A new, converted depth data object.

## Discussion

This method raises an exception if you pass an invalid `depthDataType` value.

## See Also

### Transforming and processing

- [- depthDataByApplyingExifOrientation:](<applyingexiforientation(__).md>) — Returns a derivative depth data object by mirroring or rotating it to the specified orientation.
- [availableDepthDataTypes](availabledepthdatatypes-3ifx1.md) — The list of depth data formats to which you can convert this depth data.
- [- depthDataByReplacingDepthDataMapWithPixelBuffer:error:](<replacingdepthdatamap(with_).md>) — Returns a derivative depth data object by replacing the depth data map.
