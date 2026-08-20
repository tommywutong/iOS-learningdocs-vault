---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/ImageSetType.html
archived_at: '2026-07-18T02:26:58.286718Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Image Set Type

The graphical image files for a named image asset used for instances of `UIImage` and `NSImage`.

### Extension

`.imageset`

### Folder Contents

`.avci`, `.heic`, `.heif`, `.png`, `.jpg`, and `.pdf` files.

### Contents.json File (Required)

Metadata, on-demand resource tags, App Slicing properties, and attributes for the individual resource files (Table 18-1).

__Table 18-1__Image set tags

| Key | Type | Description |
| --- | --- | --- |
| `info` | Dictionary | Versioning information for the asset catalog. |
| `author` | String | The application that authored the asset catalog. |
| `version` | Number | The version of the asset catalog. |
| `properties` | Dictionary | Properties for the image set. |
| `on-demand-resource-tags` | Array of strings | The on-demand resource tags for the image set. |
| `preserves-vector-representation` | Boolean | Set to `true` to preserve the vector information for a PDF file. |
| `images` | Array of dictionaries | The images in the image set. |
| `color-space` | Slot component | The color space for the item. For the values, see [color-space](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvoni) below. |
| `compression-type` | Slot component | The compression used on the item. For the values, see [compression-type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomrz) below. |
| `display-gamut` | Slot component | The color gamut of the device display. For the values, see [display-gamut](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomzv) below. |
| `filename` | String | The `HEIF`, `.png`, `.jpg`, or `.pdf` file for the image. |
| `graphics-feature-set` | Slot component | The graphics features required for the image. For the values, see [graphics-feature-set](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomru) below. |
| `idiom` | Slot component | The device type for the image. For the values, see [idiom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomq) below. |
| `language-direction` | String | The horizontal display direction for the image. For the values, see [language-direction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomzs) below. |
| `memory` | Slot component | The memory required by the data item. For the values, see [memory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomrv) below. |
| `scale` | Slot component | The scale of the image. For the values, see [scale](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomy) below. |
| `screen-width` | Slot component | The Apple Watch screen width for the image. For the values, see [screen-width](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomjt) below. |
| `template-rendering-intent` | String | Specifies if the image is a template for use with visual effects such as replacing colors. For the values, see [template-rendering-intent](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomzt) below. |
| `width-class` | Slot component | The size class for the width of the image. For the values, see [width-class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomjv) below. |
| `height-class` | Slot component | The size class for the height of the image. For the values, see [height-class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomjx) below. |
| `unassigned` | Boolean | Used by Xcode. |
| `alignment-insets` | Dictionary | The insets for [alignmentRectInsets](https://developer.apple.com/documentation/uikit/uiimage/1624139-alignmentrectinsets) in [UIImage](https://developer.apple.com/documentation/uikit/uiimage) or for [alignmentRect](https://developer.apple.com/documentation/appkit/nsimage/1519905-alignmentrect) in [NSImage](https://developer.apple.com/documentation/appkit/nsimage). The inset tag can be omitted. |
| `top` | Number | The top inset in pixels. |
| `bottom` | Number | The bottom inset in pixels. |
| `left` | Number | The left inset in pixels. |
| `right` | Number | The right inset in pixels. |
| `resizing` | Dictionary | The attributes for a resizable image. Only included with resizable images. |
| `mode` | Enum | The resizing mode of the image. For the values, see [resizing mode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomjz) below. |
| `center` | Dictionary | Used for resizing the image. |
| `mode` | Enum | The center resizing mode for the image. For the values, see [center mode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomrr) below. |
| `width` | Number | The width in pixels of the rectangle for the resizable area of the image.  Only valid for modes of `3-part-horizontal` and `9-part`. |
| `height` | Number | The height in pixels of the rectangle for the resizable area of the image.  Only valid for modes of `3-part-vertical` and `9-part`. |
| `cap-insets` | Dictionary | The inset from the edges of the image to the resizable area. |
| `top` | Number | The height in pixels of the non-resizable slice on the top of the image. |
| `bottom` | Number | The height in pixels of the non-resizable slice on the bottom of the image. |
| `left` | Number | The width in pixels of the non-resizable slice on the left of the image. |
| `right` | Number | The width in pixels of the non-resizable slice on the right of the image. |

### Values for Enumerated Tags

### color-space

The color space for the image (Table 18-2).

__Table 18-2__`color-space` values

| Value | Description |
| --- | --- |
| Tag not included | The image uses the standard sRGB color space. |
| `srgb` | The image uses the standard sRGB color space. |
| `display-p3` | The image uses a wide gamut color space. |

### compression-type

The type of compression used for the item (Table 18-3).

__Table 18-3__`compression-type` values

| Value | Description |
| --- | --- |
| Tag not included | The compression type inherits from the parent.  The type is set to lossless compression if there is no parent. |
| `automatic` | The image uses an automatic lossy compression. |
| `gpu-optimized-best` | The image uses a lossy GPU compression format optimized for quality. |
| `gpu-optimized-smallest` | The image uses a lossy GPU compression format optimized for memory size. |
| `lossless` | The image uses lossless compression.  This is the default if the `compresson-type` tag is not included. |
| `lossy` | The image uses basic lossy compression. |

### display-gamut

The color gamut for the device display (Table 18-4).

__Table 18-4__`display-gamut` values

| Value | Description |
| --- | --- |
| Tag not included | The image uses the standard sRGB color space. |
| `sRGB` | The image uses the standard sRGB color space. |
| `display-P3` | The image uses a wide gamut color space. |

### graphics-feature-set

The graphics feature set required for the item. The values correspond to values in the [MTLFeatureSet](https://developer.apple.com/documentation/metal/mtlfeatureset) enumerated type. The keys are based on the iOS types. tvOS uses the GPU and OS revision level equivalent keys. For example, `metal2v3` corresponds to [MTLFeatureSet_iOS_GPUFamily2_v3](https://developer.apple.com/documentation/metal/mtlfeatureset/ios_gpufamily2_v3) on iOS and to [MTLFeatureSet_tvOS_GPUFamily1_v2](https://developer.apple.com/documentation/metal/mtlfeatureset/tvos_gpufamily1_v2) on tvOS.

For values, see (Table 18-5).

__Table 18-5__`graphics-feature-set` values

| Value | Description |
| --- | --- |
| Tag not included | The item works with any device that has at least OpenGL ES 2.0. |
| `metal1v2` | The item requires features in [MTLFeatureSet_iOS_GPUFamily1_v2](https://developer.apple.com/documentation/metal/mtlfeatureset/mtlfeatureset_ios_gpufamily1_v2). |
| `metal1v3` | The item features in [MTLFeatureSet_iOS_GPUFamily1_v3](https://developer.apple.com/documentation/metal/mtlfeatureset/ios_gpufamily1_v3). |
| `metal2v2` | The item requires features in [MTLFeatureSet_iOS_GPUFamily2_v2](https://developer.apple.com/documentation/metal/mtlfeatureset/ios_gpufamily2_v2) and [MTLFeatureSet_tvOS_GPUFamily1_v1](https://developer.apple.com/documentation/metal/mtlfeatureset/tvos_gpufamily1_v1). |
| `metal2v3` | The item requires features in [MTLFeatureSet_iOS_GPUFamily2_v3](https://developer.apple.com/documentation/metal/mtlfeatureset/ios_gpufamily2_v3) and [MTLFeatureSet_tvOS_GPUFamily1_v2](https://developer.apple.com/documentation/metal/mtlfeatureset/tvos_gpufamily1_v2). |
| `metal3v1` | The item requires features in [MTLFeatureSet_iOS_GPUFamily3_v1](https://developer.apple.com/documentation/metal/mtlfeatureset/mtlfeatureset_ios_gpufamily3_v1). |
| `metal3v2` | The item requires features in [MTLFeatureSet_iOS_GPUFamily3_v2](https://developer.apple.com/documentation/metal/mtlfeatureset/mtlfeatureset_ios_gpufamily3_v2). |
| `metal4v1` | The item requires features in [iOS_GPUFamily4_v1](https://developer.apple.com/documentation/metal/mtlfeatureset/ios_gpufamily4_v1). |

### idiom

The device family (Table 18-6).

__Table 18-6__`idiom` values

| Value | Description |
| --- | --- |
| `appLauncher` | An image shown app launcher on watchOS |
| `companionSettings` | An image for the Apple Watch Settings app |
| `ios-marketing` | An image for the App Store icon |
| `iphone` | The image is for iPhone devices. |
| `ipad` | The image is for iPad devices. |
| `mac` | The image is for Mac computers. |
| `notificationCenter` | An image for the notification center on watchOS. |
| `quickLook` | An image used for a long look on watchOS. |
| `tv` | The image is for Apple TV. |
| `universal` | The image works on any device and platform. |
| `watch` | The image is for the Apple Watch devices. |
| `watch-marketing` | An image for the App Store icon. |
| Tag not included | Same as specifying `universal`. |

### language-direction

The horizontal display direction of the image for left-to-right and right-to-left languages. (Table 18-7).

__Table 18-7__`language-direction` values

| Value | Description |
| --- | --- |
| Tag not included | The image has a fixed horizontal orientation and will display in the same direction. |
| `left-to-right` | The image is used for display in left-to-right languages.  The image is mirrored in right-to-left languages unless a right-to-left version of the image is provided. |
| `right-to-left` | The image is used for display in right-to-left languages.  The image is mirrored in left-to-right languages unless a left-to-right version of the image is provided. |

### memory

The minimum device memory configuration required by the data item (Table 18-8).

__Table 18-8__`memory` values

| Value | Description |
| --- | --- |
| Tag not included | The data item works on any device. |
| `1GB` | The device needs at least a 1GB memory configuration. |
| `2GB` | The device needs at least a 2GB memory configuration. |
| `3GB` | The device needs at least a 3GB memory configuration. |
| `4GB` | The device needs at least a 4GB device memory configuration. |

### scale

The targeted display scale for the image (Table 18-9).

__Table 18-9__`scale` values

| Value | Description |
| --- | --- |
| Tag not included | The image is for any display scale and should point to a `.pdf` file. |
| `1x` | Targeted for unscaled displays. |
| `2x` | Targeted for Retina displays. |
| `3x` | Targeted for Retina displays with higher density such as those on the iPhone 6 Plus. |

### screen-width

The screen width for the Apple Watch (Table 18-10).

__Table 18-10__`screen-width` values

| Value | Description |
| --- | --- |
| Tag not included | The image is for any Apple Watch screen. |
| `<=145` | Screen width for the 42mm Apple Watch screen. |
| `>145` | Screen width for the 38mm Apple Watch screen. |

### template-rendering-intent

Indicates if the image is a renderable image or is a template for. (Table 18-11).

__Table 18-11__`template-rendering-intent` values

| Value | Description |
| --- | --- |
| Tag not included | If the name of the image ends in "Template", use the image as a template, otherwise render it as the original image. |
| `original` | Render as the original image. |
| `template` | Use the image as a template for visual effects such as replacing colors. |

### width-class

The size class for the image width (Table 18-12).

__Table 18-12__`width-class` values

| Value | Description |
| --- | --- |
| Tag not included | The image width is for the `any` size class. |
| `compact` | The image width is for the `compact` size class. |
| `regular` | The image width is for the `regular` size class. |

### height-class

The size class for the image height (Table 18-13).

__Table 18-13__`height-class` values

| Value | Description |
| --- | --- |
| Tag not included | The image height is for the `any` size class. |
| `compact` | The image height is for the `compact` size class. |
| `regular` | The image height is for the `regular` size class. |

### resizing mode

The mode for a sliced resizable image (Table 18-14).

__Table 18-14__`resizing mode` values

| Value | Description |
| --- | --- |
| Tag not included | The entire image is resized. |
| `3-part-horizontal` | The image is divided into three horizontal parts. The outer portions are fixed-width. The central portion resizes in the horizontal dimension. |
| `3-part-vertical` | The image is divided into three vertical parts. The outer portions are fixed-height. The central portion resizes in the vertical dimension. |
| `9-part` | The image is divided into nine parts. There is a central area that resizes in the horizontal and vertical dimensions, fixed-width vertical caps at the left and right of the central area, fixed-height caps at the top and bottom of the central area, and four fixed-size corner parts. |

### center mode

The resizing mode of the central area of a resizing image (Table 18-15).

__Table 18-15__`center mode` values

| Value | Description |
| --- | --- |
| Tag not included |  |
| `tile` | The central area is tiled to fill the available size. |
| `stretch` | The central area is stretched to fill the available size. |

### Sample Contents.json File

1. `{`
2. `"images" : [`
3. `{`
4. `"idiom" : "universal",`
5. `"scale" : "1x"`
6. `},`
7. `{`
8. `"graphics-feature-set" : "metal1v2",`
9. `"idiom" : "universal",`
10. `"filename" : "Llama.png"`
11. `"scale" : "2x"`
12. `},`
13. `{`
14. `"graphics-feature-set" : "metal2v2",`
15. `"idiom" : "universal",`
16. `"memory" : "2GB",`
17. `"scale" : "3x"`
18. `}`
19. `],`
20. `"info" : {`
21. `"author" : "com.developerName",`
22. `"version" : 1`
23. `},`
24. `"properties" : {`
25. `"on-demand-resources : [`
26. `"llama",`
27. `"mountain"`
28. `]`
29. `}`
30. `}`

[Icon Set Type](IconSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrufvjvomi)

[Image Stack Type](ImageStackType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnbrfvjvomi)
