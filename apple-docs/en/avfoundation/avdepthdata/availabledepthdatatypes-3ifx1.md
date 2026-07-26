---
title: availableDepthDataTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdepthdata/availabledepthdatatypes-3ifx1
source_url: 'https://developer.apple.com/documentation/avfoundation/avdepthdata/availabledepthdatatypes-3ifx1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdepthdata/availabledepthdatatypes-3ifx1.json'
content_hash: 'sha256:ecd265d7cd0c72d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDepthData](../avdepthdata.md)

# availableDepthDataTypes

<sub>Instance Property</sub>

The list of depth data formats to which you can convert this depth data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@nonobjc var availableDepthDataTypes: [OSType] { get }
```

## Discussion

Use the [- depthDataByConvertingToDepthDataType:](<converting(todepthdatatype_).md>) method to obtain a converted depth data object using one of the types in this list.

## See Also

### Transforming and processing

- [- depthDataByApplyingExifOrientation:](<applyingexiforientation(__).md>) — Returns a derivative depth data object by mirroring or rotating it to the specified orientation.
- [- depthDataByConvertingToDepthDataType:](<converting(todepthdatatype_).md>) — Returns a derivative depth data object by converting the depth data map to the specified data type.
- [- depthDataByReplacingDepthDataMapWithPixelBuffer:error:](<replacingdepthdatamap(with_).md>) — Returns a derivative depth data object by replacing the depth data map.
