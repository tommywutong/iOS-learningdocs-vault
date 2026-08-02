---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/SpriteAtlasType.html
archived_at: '2026-07-18T02:27:19.633481Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Sprite Atlas Type

A named sprite atlas created from the image sets contained in the folder. The sprite atlas can be loaded using the [textureNamed:](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427375-texturenamed) method of [SKTextureAtlas](https://developer.apple.com/documentation/spritekit/sktextureatlas). Individual images can be loaded using [imageNamed:](https://developer.apple.com/documentation/uikit/uiimage/1624146-imagenamed) in iOS 9 and later.

### Extension

`.spriteatlas`

### Folder Contents

Image sets for each sprite in the atlas.

### Contents.json File (Optional)

Metadata, on-demand resource tags, App Slicing properties, and properties for the sprite atlas (Table 25-1).

__Table 25-1__Sprite atlas tags

| Key | Type | Description |
| --- | --- | --- |
| `info` | Dictionary | Versioning information for the asset catalog. |
| `author` | String | The application that authored the asset catalog. |
| `version` | Number | The version of the asset catalog. |
| `properties` | Dictionary | Properties for the sprite atlas. |
| `compression-type` | Slot component | The compression used on the item. For the values, see [compression-type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomrz) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `provides-namespace` | Boolean | Use the name of the atlas as a path element for accessing any sprites.  The name of the atlas is the portion of the folder name before `.spriteatlas`. |
| `on-demand-resource-tags` | Array of strings | The on-demand resource tags for the sprite atlas. |

### Sample Contents.json File

1. `{`
2. `"properties" : {`
3. `"provides-namespace" : true`
4. `},`
5. `"info" : {`
6. `"author" : "com.developerName",`
7. `"version" : 1`
8. `}`
9. `}`

[Named Color Type](Named_Color.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjzfvjvomi)

[Sticker Type](Sticker.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjufvjvomi)
