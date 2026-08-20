---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/ImageStackType.html
archived_at: '2026-07-18T02:27:00.736805Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Image Stack Type

A set of layered images combined to enable parallax. For more information on layered images and parallax, see [Creating Parallax Artwork](../../General/App%20Programming%20Guide%20for%20tvOS/CreatingParallaxArtwork.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbrfvbuqmjz) in the _[App Programming Guide for tvOS](https://developer.apple.com/library/archive/documentation/General/Conceptual/AppleTV_PG/index.html#//apple_ref/doc/uid/TP40015241)_ and [Layered Images](https://developer.apple.com/tvos/human-interface-guidelines/icons-and-images/#layered-images) in the [Apple TV Human Interface Guidelines](https://developer.apple.com/tvos/human-interface-guidelines/).

### Extension

`.imagestack`

### Folder Contents

Image stack layers.

### Contents.json File (Required)

Metadata and a list of the image stack layers (Table 19-1).

__Table 19-1__Image stack tags

| Key | Type | Description |
| --- | --- | --- |
| `info` | Dictionary | Metadata for the author and format version of the asset catalog. |
| `author` | String | Use your bundle ID. |
| `version` | Number | The format version of the asset catalog. Use `1`. |
| `layers` | Array of dictionaries | The layers in the image stack. |
| `filename` | String | The name of the asset catalog folder containing the layer. |
| `properties` | Dictionary | Properties for the image stack. |
| `canvasSize` | Dictionary | The canvas size for the image stack.  Defaults to the size of the background layer if the tag is not included. |
| `width` | Number | The width of the image stack canvas in pixels. |
| `height` | Number | The height of the image stack canvas in pixels. |

### Sample Contents.json Files

### Simple Image Stack

1. `{`
2. `"layers" : [`
3. `{`
4. `"filename" : "Foreground.imagestacklayer"`
5. `},`
6. `{`
7. `"filename" : "Llama.imagestacklayer"`
8. `},`
9. `{`
10. `"filename" : "Background.imagestacklayer"`
11. `}`
12. `],`
13. `"info" : {`
14. `"author" : "com.developerName",`
15. `"version" : 1`
16. `}`
17. `}`

### Image Stack with Canvas Size

1. `{`
2. `"layers" : [`
3. `{`
4. `"filename" : "Foreground.imagestacklayer"`
5. `},`
6. `{`
7. `"filename" : "Llama.imagestacklayer"`
8. `},`
9. `{`
10. `"filename" : "Background.imagestacklayer"`
11. `}`
12. `],`
13. `"info" : {`
14. `"author" : "com.developerName",`
15. `"version" : 1`
16. `},`
17. `"properties" : {`
18. `"canvasSize" : {`
19. `"width" : 2048`
20. `"height" : 1365`
21. `}`
22. `}`
23. `}`

[Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi)

[Image Stack Layer Type](ImageStackLayerType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnbsfvjvomi)
