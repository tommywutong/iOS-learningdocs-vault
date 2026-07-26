---
title: 'init(cvPixelBuffer:properties:options:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+（27.0 起废弃）, iPadOS 10.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.12+（27.0 起废弃）, tvOS 10.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/cifilter-swift.class/init(cvpixelbuffer:properties:options:)-69695'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/init(cvpixelbuffer:properties:options:)-69695'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/init%28cvpixelbuffer%3Aproperties%3Aoptions%3A%29-69695.json'
content_hash: 'sha256:fa65f80a1524f099'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# init(cvPixelBuffer:properties:options:)

<sub>Initializer</sub>

Returns a CIFilter that will in turn return a properly processed CIImage as “outputImage”.

> [!warning] Deprecated
> Use new CIRAWFilter class instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init!(cvPixelBuffer pixelBuffer: CVPixelBuffer!, properties: [AnyHashable : Any]!, options: [CIRAWFilterOption : Any]! = [:])
```

## Discussion

Note that when using this initializer, you should pass in a CVPixelBufferRef with one of the following Raw pixel format types kCVPixelFormatType_14Bayer_GRBG, kCVPixelFormatType_14Bayer_RGGB, kCVPixelFormatType_14Bayer_BGGR, kCVPixelFormatType_14Bayer_GBRG as well as the root properties attachment from the CMSampleBufferRef.
