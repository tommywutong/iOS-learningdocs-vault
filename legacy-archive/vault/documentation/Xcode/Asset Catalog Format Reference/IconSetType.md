---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/IconSetType.html
archived_at: '2026-07-18T02:26:56.393784Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Icon Set Type

A set of OS X icons in the `.iconset` format.

### Extension

`.iconset`

### Folder Contents

`.png` files for the icons. Each file has a name of the form:

`icon_<width>x<height>[@2x].png`

- `width` is the width of the icon in pixels.
- `height` is the height of the icon in pixels.
- `@2x` is optional and specifies that the icon is for Retina displays.

For example, a fully specified OS X icon set contains the following files:

- `icon_16x16.png`
- `icon_16x16@2x.png`
- `icon_32x32.png`
- `icon_32x32@2x.png`
- `icon_128x128.png`
- `icon_128x128@2x.png`
- `icon_256x256.png`
- `icon_256x256@2x.png`
- `icon_512x512.png`
- `icon_512x512@2x.png`

For more information on OS X icons, see Icon and Image Design.

[Group Type](GroupType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrrfvjvomi)

[Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi)
