---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/AR_Reference_Image.html
archived_at: '2026-07-18T02:26:40.310397Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## AR Reference Image

The image file for an [ARReferenceImage](https://developer.apple.com/documentation/arkit/arreferenceimage).

### Extension

`.arreferenceimage`

### Folder Contents

A `.heif` (High Efficiency Image Format), `.png`, `.jpg`, or `.tiff` file.

### Contents.json File (Required)

Metadata and attributes for the image (Table 7-1.)

__Table 7-1__AR reference image tags

| Key | Type | Description |
| --- | --- | --- |
| `info` | Dictionary | Metadata for the author and format version of the asset catalog. |
| `author` | String | Use your bundle ID. |
| `version` | Number | The format version of the asset catalog. Use `1`. |
| `images` | Array of one dictionary | The image file for the `ARReferenceImage`. |
| `filename` | String | The `.heif`, `.jpg`, `.png`, or `.tiff` file for the image. |
| `idiom` | Slot component | The device type for the image. For the values, see [idiom](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomq) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `properties` | Dictionary | Properties for the image. |
| `unit` | String | The unit type of the `width` property. For the values, see [unit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnrqfvjvomy) below. |
| `width` | Number | The physical width of the image. |

### Values for Enumerated Tags

### unit

An optional unit type used to convert the value of the `width` property to meters. Valid unit types are:

- `meters`
- `centimeters`
- `feet`
- `inches`
- `yards`

A value of `meters` is used if the tag is not specified.

### Sample Contents.json File

1. `{`
2. `"images" : [`
3. `{`
4. `"idiom" : "universal",`
5. `"filename" : "llama farm.heif"`
6. `}`
7. `],`
8. `"properties" : {`
9. `"width" : 33,`
10. `"units" : "inches"`
11. `},`
12. `"info" : {`
13. `"author" : "com.developerName",`
14. `"version" : 1`
15. `}`
16. `}`

[App Icon Type](AppIconType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrsfvjvomi)

[AR Resource Group](AR_Resource_Group.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnrrfvjvomi)
