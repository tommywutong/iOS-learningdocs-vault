---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/MIPMapType.html
archived_at: '2026-07-18T02:27:13.812690Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Mipmap Type

A series of images at different resolutions for the same texture.

### Extension

`.mipmapset`

### Folder Contents

Images for each resolution of the texture.

### Contents.json File

Metadata and level mapping information for the mipmap is show in (Table 23-1).

__Table 23-1__Mipmap tags

| Key | Type | Description |
| --- | --- | --- |
| `info` | Dictionary | Versioning information for the asset catalog. |
| `author` | String | The application that authored the asset catalog. |
| `version` | Number | The version of the asset catalog. |
| `properties` | Dictionary | Properties for the mipmap atlas. |
| `level-mode` | String | How the images levels in the mipmap apply to the texture.  For the values, see [level-mode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjxfvjvona) below. |
| `levels` | Array of dictionaries | The different levels of resolutions for the mipmap. |
| `display-gamut` | Slot component | The color gamut of the device display. For the values, see [display-gamut](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomzv) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `filename` | String | The `HEIF`, `.png` or `.jpg` file for the image. |
| `idiom` | Slot Component | The idiom of the icon. For the values, see [idiom](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomq) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `mipmap-level` | String | The mipmap texture level for the image. For the values, see [mipmap-level](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjxfvjvoni) below. |

### Values for Enumerated Tags

### display-gamut

See [display-gamut](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomzv) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### level-mode

How the images levels in the mipmap apply to the texture. For the values, see (Table 23-2).

__Table 23-2__`level-mode` values

| Value | Description |
| --- | --- |
| Tag not included | Metal generates all the mipmap levels from the base image. |
| `none` | Metal does not generate mipmap levels from the base image. |
| `all` | Metal generates all the mipmap levels from the base image. |
| `fixed` | Metal generates all the mipmap levels between the base image and the maximum mipmap level provided in [mipmap-level](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjxfvjvoni). |

### mipmap-level

The level for an image in the mipmap. For the values, see (Table 23-3).

__Table 23-3__`mipmap-level` values

| Value | Description |
| --- | --- |
| `base` | The base level image of the mip map. |
| `mipmap-level-[1…16]` | The image for a numbered level of the mip map.  For example, for the level three mipmap, set the key to `mipmap-level-3`. |

### Sample Contents.json File

1. `{`
2. `"properties" : {`
3. `"level-mode" : base`
4. `},`
5. `"levels" : [`
6. `{`
7. `"filename" : "WalkingLlamaBase.png",`
8. `"mipmap-level" : "base"`
9. `}`
10. `],`
11. `"info" : {`
12. `"author" : "com.developerName",`
13. `"version" : 1`
14. `}`
15. `}`

[Messages Extension Icon Type](MessagesIconType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjyfvjvomq)

[Named Color Type](Named_Color.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjzfvjvomi)
