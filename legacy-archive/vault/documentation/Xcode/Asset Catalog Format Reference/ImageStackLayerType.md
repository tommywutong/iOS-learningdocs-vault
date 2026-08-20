---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/ImageStackLayerType.html
archived_at: '2026-07-18T02:26:59.728288Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Image Stack Layer Type

A layer in an image stack.

There are two types of image stack layers. _Embedded_ layers are the default and contain the image set for the layer. _Referenced_ layers contain a reference to an image set in the asset catalog.

### Extension

`.imagestacklayer`

### Folder Contents

An image set for the layer for embedded types.

A `Contents.json` for referenced types.

### Contents.json File

Optional for embedded image stack layers and contains metadata (Table 20-1).

Required for referenced image and contains the location of the referenced image stack inside the asset catalog.

__Table 20-1__Image stack layer tags

| Key | Type | Description |
| --- | --- | --- |
| `info` | Dictionary | Metadata for the author and format version of the asset catalog. |
| `author` | String | Use your bundle ID. |
| `version` | Number | The format version of the asset catalog. Use `1`. |
| `properties` | Dictionary | Properties for an image stack layer. |
| `content-reference` | Dictionary | The location of the referenced image set for the image stack layer. |
| `type` | String | The type of asset pointed to by the reference. Must be `image-set`. |
| `name` | String | The fully qualified name of the image set. For more information, see [Unique Asset Names](FolderStructure.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmztfvjvona). |
| `matching-style` | String | The kind of content reference. Must be `fully-qualified-name`. |
| `frame-size` | Dictionary | The size for the image stack layer.  Defaults to the size of the image stack canvas if the tag is not included. |
| `width` | Number | The width of the image stack layer in pixels. |
| `height` | Number | The height of the image stack layer in pixels. |
| `frame-center` | Dictionary | The position of the center of the image stack layer image on the image stack canvas.  Defaults to the center of the image stack canvas if the tag is not included.  The coordinate is in pixels from the top-left edge of the image stack canvas. |
| `x` | Number | The horizontal position of the center of the image stack layer. |
| `y` | Number | The vertical position of the image stack layer. |

### Sample Contents.json Files

### Simple Image Stack Layer

1. `{`
2. `"info" : {`
3. `"author" : "com.developerName",`
4. `"version" : 1`
5. `},`
6. `}`

### Image Stack Layer with Content Reference

1. `{`
2. `"properties" : {`
3. `"content-reference : {`
4. `"type" : "image-set",`
5. `"name" : "Llamas\/Front",`
6. `"matching-style" : "fully-qualified-name"`
7. `}`
8. `},`
9. `"info" : {`
10. `"author" : "com.developerName",`
11. `"version" : 1`
12. `},`
13. `}`

### Image Stack Layer with Size and Center

1. `{`
2. `"properties" : {`
3. `"frame-size : {`
4. `"width" : 364,`
5. `"height" : 548`
6. `},`
7. `"frame-center : {`
8. `"x" : 1500,`
9. `"y" : 700`
10. `}`
11. `},`
12. `"info" : {`
13. `"author" : "com.developerName",`
14. `"version" : 1`
15. `},`
16. `}`

[Image Stack Type](ImageStackType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnbrfvjvomi)

[Launch Image Type](LaunchImageType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrwfvjvomi)
