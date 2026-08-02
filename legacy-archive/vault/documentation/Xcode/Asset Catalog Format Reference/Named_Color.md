---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/Named_Color.html
archived_at: '2026-07-18T02:27:18.651400Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Named Color Type

The definition for a named color that can be used anywhere you can use a color in your project.

### Extension

`.colorset`

### Folder Contents

The `Contents.json` file.

### Contents.json File (Required)

Metadata and attributes for the individual colors for the named color (Table 24-1).

__Table 24-1__Named color tags

| Key | Type | Description |
| --- | --- | --- |
| `info` | Dictionary | Metadata for the author and format version of the asset catalog. |
| `author` | String | Use your bundle ID. |
| `version` | Number | The format version of the asset catalog. Use `1`. |
| `colors` | Array | Each element identifies one variant of the color. |
| `display-gamut` | Slot component | The color gamut of the device display. For the values, see [display-gamut](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomzv) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `idiom` | Slot Component | The idiom of the icon. For the values, see [idiom](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomq) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `color` | Dictionary | One of the sizes that matches the idiom for the icon. If the size is not valid, the image is ignored.  For the values, see [size](AppIconType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrsfvjvooa) below. |
| `color-space` | Slot Component | The color space for the data item. For the values, see [color-space](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvoni) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `components` | Dictionary | The RGBA color components for the named color. |
| `red` | Number | The red component of the custom color specified as a number from `0` to `1`. |
| `green` | Number | The green component of the custom color specified as a number from `0` to `1`. |
| `blue` | Number | The blue component of the custom color specified as a number from `0` to `1`. |
| `alpha` | Number | The transparency of the custom color specified as a number from `0` to `1`. |

### Values for Enumerated Tags

### color-space

See [color-space](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvoni) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### display-gamut

See [display-gamut](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomzv) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### idiom

See [idiom](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomq) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### Sample Contents.json File

1. `{`
2. `"colors" : [`
3. `{`
4. `"idiom" : "universal",`
5. `"display-gamut" : "sRGB",`
6. `"color" : {`
7. `"components" : {`
8. `"red" : 0.5,`
9. `"green" : 0.5,`
10. `"blue" : 0.5,`
11. `"alpha" : 1`
12. `},`
13. `"color-space" : "srgb"`
14. `},`
15. `},`
16. `{`
17. `"idiom" : "universal",`
18. `"display-gamut" : "display-P3",`
19. `"color" : {`
20. `"components" : {`
21. `"red" : 0.5,`
22. `"green" : 0.5,`
23. `"blue" : 0.5,`
24. `"alpha" : 1`
25. `},`
26. `"color-space" : "display-p3"`
27. `},`
28. `},`
29. `…`
30. `],`
31. `"info" : {`
32. `"author" : "com.developerName",`
33. `"version" : 1`
34. `}`
35. `}`

[Mipmap Type](MIPMapType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjxfvjvomi)

[Sprite Atlas Type](SpriteAtlasType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrxfvjvomi)
