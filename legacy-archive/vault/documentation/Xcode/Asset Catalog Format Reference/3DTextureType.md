---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/3DTextureType.html
archived_at: '2026-07-18T02:26:39.706347Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Cube Texture Type

A 3D cube mapped texture.

### Extension

`.cubetextureset`

### Folder Contents

Mipmaps for the different trait configurations of each of the six cube faces. For information on the mipmap type, see [Mipmap Type](MIPMapType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjxfvjvomi).

### Contents.json File

Metadata, on-demand resource tags, texture information, and properties for the cube texture are shown in (Table 11-1).

__Table 11-1__Cube texture tags

| Key | Type | Description |
| --- | --- | --- |
| `info` | Dictionary | Versioning information for the asset catalog. |
| `author` | String | The application that authored the asset catalog. |
| `version` | Number | The version of the asset catalog. |
| `properties` | Dictionary | Properties for the 2D texture. |
| `interpretation` | String | Interpret the file as an image or as data. For the values, see [interpretation](2DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvonq) in [Texture Type](2DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvomi). |
| `on-demand-resource-tags` | Array of strings | The on-demand resource tags for the 2D texture. |
| `origin` | String | The origin of the coordinate system. For the values, see [origin](2DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvooa) in [Texture Type](2DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvomi). |
| `textures` | Array of dictionaries | The mipmap sets for each trait combination.  The array must contain at least one texture for each of the 6 [cube-face](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjrfvjvona) values: x+, x-, y+, y-, z+, z-. |
| `color-space` | Slot component | The color space for the data item. For the values, see [color-space](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvoni) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `cube-face` | String | The cube face for the mipmap. For the values, see [cube-face](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjrfvjvona) below. |
| `display-gamut` | Slot component | The color gamut of the device display. For the values, see [display-gamut](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomzv) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `filename` | String | The name of the folder containing the mipmap for the trait variation.  For information on the mipmap type, see [Mipmap Type](MIPMapType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjxfvjvomi). |
| `graphics-feature-set` | Slot component | The graphics features required for the item. For the values, see [graphics-feature-set](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomru) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `idiom` | Slot component | The device type for the image. For the values, see [idiom](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomq) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `memory` | Slot component | The memory required by the data item. For the values, see [memory](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomrv) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `pixel-format` | String | The format of the pixels in the image. For the values, see [pixel-format](2DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvony) in [Texture Type](2DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvomi). |
| `scale` | Slot Component | The scale of the image. For the values, see [scale](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomy) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |

### Values for Enumerated Tags

### color-space

See [color-space](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvoni) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### cube-face

The name of the cube face as a string. Values are shown in (Table 11-2).

__Table 11-2__`cube-face` values

| Value | Description |
| --- | --- |
| `x-` | The cube face on the negative x axis. |
| `x+` | The cube face on the positive x axis. |
| `y-` | The cube face on the negative y axis. |
| `y+` | The cube face on the positive y axis. |
| `z-` | The cube face on the negative z axis. |
| `z+` | The cube face on the positive z axis. |

### display-gamut

See [display-gamut](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomzv) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### graphics-feature-set

See [graphics-feature-set](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomru) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### idiom

See [idiom](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomq) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### interpretation

See [interpretation](2DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvonq) in [Texture Type](2DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvomi).

### memory

See [memory](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomrv) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### origin

See [origin](2DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvooa) in [Texture Type](2DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvomi).

### pixel-format

See [pixel-format](2DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvony) in [Texture Type](2DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvomi).

### scale

See [scale](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomy) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### Sample Contents.json File

1. `{`
2. `"properties" : {`
3. `"interpretation" : "colors"`
4. `},`
5. `"textures" : [`
6. `{`
7. `"filename" : "LlamaFront.mipmapset",`
8. `"cube-face" : "x+",`
9. `"idiom" : "Universal",`
10. `"memory" : "4GB",`
11. `"pixel-format" : "rbg-10-extended-range-sRGB"`
12. `},`
13. `{`
14. `"filename" : "LlamaBack.mipmapset",`
15. `"cube-face" : "x-",`
16. `"idiom" : "Universal",`
17. `"memory" : "4GB",`
18. `"pixel-format" : "rbg-10-extended-range-sRGB"`
19. `},`
20. `{`
21. `"filename" : "LlamaLeft.mipmapset",`
22. `"cube-face" : "y+",`
23. `"idiom" : "Universal",`
24. `"memory" : "4GB",`
25. `"pixel-format" : "rbg-10-extended-range-sRGB"`
26. `},`
27. `{`
28. `"filename" : "LlamaRight.mipmapset",`
29. `"cube-face" : "y-",`
30. `"idiom" : "Universal",`
31. `"memory" : "4GB",`
32. `"pixel-format" : "rbg-10-extended-range-sRGB"`
33. `},`
34. `{`
35. `"filename" : "LlamaTop.mipmapset",`
36. `"cube-face" : "z+",`
37. `"idiom" : "Universal",`
38. `"memory" : "4GB",`
39. `"pixel-format" : "rbg-10-extended-range-sRGB"`
40. `},`
41. `{`
42. `"filename" : "LlamaBottom.mipmapset",`
43. `"cube-face" : "x+",`
44. `"idiom" : "Universal",`
45. `"memory" : "4GB",`
46. `"pixel-format" : "rbg-10-extended-range-sRGB"`
47. `},`
48. `{`
49. `"filename" : "LlamaFront.mipmapset",`
50. `"cube-face" : "z+",`
51. `"idiom" : "Universal",`
52. `"memory" : "4GB",`
53. `"pixel-format" : "rbg-10-extended-range-sRGB"`
54. `}`
55. `]`
56. `"info" : {`
57. `"author" : "com.developerName",`
58. `"version" : 1`
59. `}`
60. `}`

[Catalog Type](CatalogType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrqfvjvomi)

[Data Set Type](DataSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrtfvjvomi)
