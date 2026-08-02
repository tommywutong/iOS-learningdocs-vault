---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/Sticker.html
archived_at: '2026-07-18T02:27:20.644694Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Sticker Type

An individual sticker in a sticker pack.

### Extension

`.sticker`

### Folder Contents

An image for the sticker.

### Contents.json File

Metadata, accessibility text, and filename for a sticker. For values, see (Table 26-1).

__Table 26-1__Sticker tags

| Key | Type | Description |
| --- | --- | --- |
| `info` | Dictionary | Versioning information for the asset catalog. |
| `author` | String | The application that authored the asset catalog. |
| `version` | Number | The version of the asset catalog. |
| `properties` | Dictionary | Properties for the sprite atlas. |
| `accessibility-label` | String | A custom string used by Voice Over. The sticker name is used if no string is provided. |
| `filename` | String | The name of the image file containing the sticker. |

### Sample Contents.json File

1. `{`
2. `"properties" : {`
3. `"accessibility-label" : "The llama says hi.",`
4. `"filename" : "llamaKnows.png"`
5. `},`
6. `"info" : {`
7. `"author" : "com.developerName",`
8. `"version" : 1`
9. `}`
10. `}`

[Sprite Atlas Type](SpriteAtlasType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrxfvjvomi)

[Sticker Pack Type](StickerPack.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjsfvjvomi)
