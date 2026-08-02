---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/2DTextureType.html
archived_at: '2026-07-18T02:26:39.192377Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Texture Type

A 2D texture.

### Extension

`.textureset`

### Folder Contents

Mipmaps for the different trait configurations. For information on the mipmap type, see [Mipmap Type](MIPMapType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjxfvjvomi).

### Contents.json File

Metadata, on-demand resource tags, texture information, and properties for the texture are shown in (Table 29-1).

__Table 29-1__Texture tags

| Key | Type | Description |
| --- | --- | --- |
| `info` | Dictionary | Versioning information for the asset catalog. |
| `author` | String | The application that authored the asset catalog. |
| `version` | Number | The version of the asset catalog. |
| `properties` | Dictionary | Properties for the texture. |
| `interpretation` | String | Interpret the file as an image or as data. For the values, see [interpretation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvonq) below. |
| `on-demand-resource-tags` | Array of strings | The on-demand resource tags for the texture. |
| `origin` | String | The origin of the coordinate system. For the values, see [origin](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvooa) below. |
| `textures` | Array of dictionaries | The mipmap sets for each trait combination. |
| `color-space` | Slot component | The color space for the data item. For the values, see [color-space](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvoni) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `display-gamut` | Slot component | The color gamut of the device display. For the values, see [display-gamut](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomzv) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `filename` | String | The name of the folder containing the mipmap for the trait variation.  For information on the mipmap type, see [Mipmap Type](MIPMapType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjxfvjvomi). |
| `graphics-feature-set` | Slot component | The graphics features required for the item. For the values, see [graphics-feature-set](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomru) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `idiom` | Slot component | The device type for the image. For the values, see [idiom](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomq) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `memory` | Slot component | The memory required by the data item. For the values, see [memory](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomrv) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `pixel-format` | String | The format of the pixels in the image. For the values, see [pixel-format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvony) below. |
| `scale` | Slot Component | The scale of the image. For the values, see [scale](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomy) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |

### Values for Enumerated Tags

### color-space

See [color-space](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvoni) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### display-gamut

See [display-gamut](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomzv) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### graphics-feature-set

See [graphics-feature-set](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomru) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### idiom

See [idiom](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomq) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### interpretation

How to interpret the contents of the file (Table 29-2).

__Table 29-2__`interpretation` values

| Value | Description |
| --- | --- |
| Tag not included | The contents of the file are an image. |
| `colors` | The contents of the file are an image. |
| `data` | The contents of the file are data such as a normal map. |

### memory

See [memory](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomrv) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### origin

The origin of the image coordinate system. Values are shown in (Table 29-3).

__Table 29-3__`origin` values

| Value | Description |
| --- | --- |
| Tag not included | The coordinate system originates at the top-left. |
| `bottom-left` | The coordinate system originates at the bottom-left. |

### pixel-format

The pixel format for a texture. Values are shown in (Table 29-4).

__Table 29-4__`pixel-format` values

| Value | Description |
| --- | --- |
| Tag not included | Format is determined automatically. |
| `r-8-unorm` | The pixels are in normalized 8-bit red format. |
| `rg-8-unorm` | The pixels are in normalized 8-bit red, green format. |
| `rgba-8-unorm` | The pixels are in normalized 8-bit RGB alpha format. |
| `rgba-8-unorm-sRGB` | The pixels are in normalized 8-bit RGB alpha format for the sRGB color space. |
| `r-16-float` | The pixels are in 16-bit floating point red format. |
| `rg-16-float` | The pixels are in 16-bit floating point red, green format. |
| `rgba-16-float` | The pixels are in 16-bit floating point RGB alpha format. |
| `rbg-10-extended-range-sRGB` | The pixels are in 10-bit extended range sRGB format. |
| `astc-4x4` | The pixels are in ASTC 4x4 RGB alpha format. |
| `astc-4x4-sRGB` | The pixels are in ASTC 4x4 sRGB format. |
| `astc-8x8` | The pixels are in ASTC 8x8 RGB alpha format. |
| `astc-8x8-sRGB` | The pixels are in ASTC 8x8 sRGB format. |

### scale

See [scale](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomy) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### Sample Contents.json File

1. `{`
2. `"properties" : {`
3. `"interpretation" : "colors"`
4. `},`
5. `"textures" : [`
6. `{`
7. `"filename" : "HighFidelityLlama.mipmapset",`
8. `"idiom" : "Universal",`
9. `"memory" : "4GB",`
10. `"pixel-format" : "rbg-10-extended-range-sRGB"`
11. `},`
12. `{`
13. `"filename" : "LowFidelityLlama.mipmapset",`
14. `"idiom" : "Universal",`
15. `"memory" : "1GB",`
16. `"pixel-format" : "rgba-8-unorm"`
17. `}`
18. `]`
19. `"info" : {`
20. `"author" : "com.developerName",`
21. `"version" : 1`
22. `}`
23. `}`

[Sticker Sequence Type](StickerFilmStrip.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjtfvjvomi)

[Watch Complications Type](WatchComplicationsType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzufvjvomi)
