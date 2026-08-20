---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/StickerPack.html
archived_at: '2026-07-18T02:27:22.805439Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Sticker Pack Type

A pack of custom stickers for messaging.

### Extension

`.stickerpack`

### Folder Contents

Folders with stickers and sticker sequences.

### Contents.json File

Metadata, sticker size, and folder names for the stickers and sticker sequences. For values, see (Table 27-1).

__Table 27-1__Sticker pack tags

| Key | Type | Description |
| --- | --- | --- |
| `info` | Dictionary | Versioning information for the asset catalog. |
| `author` | String | The application that authored the asset catalog. |
| `version` | Number | The version of the asset catalog. |
| `properties` | Dictionary | Properties for the sticker pack. |
| `grid-size` | String | The size of the stickers and sticker sequences in the pack. For the values, see [grid-size](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjsfvjvomy) below. |
| `stickers` | Array of dictionaries | The stickers and sticker sequences in the sticker pack. |
| `filename` | String | The name of a folder containing a sticker or sticker sequence. |

### Values for Enumerated Tags

### grid-size

The size of the images in the stickers or sticker sequences in the pack. Values are shown in (Table 27-2).

__Table 27-2__`grid-size` values

| Value | Description |
| --- | --- |
| `small` | The recommended size for small stickers is `100x100` points at `3x` resolution. |
| `regular` | The recommended size for small stickers is `136x136` points at `3x` resolution. |
| `large` | The recommended size for small stickers is `206x206` points at `3x` resolution. |

### Sample Contents.json File

1. `{`
2. `"properties" : {`
3. `"grid-space" : "regular"`
4. `},`
5. `"stickers" : [`
6. `{`
7. `"filename" : "llamaHaloSticker.sticker"`
8. `},`
9. `"filename" : "llamaJumping.stickersequence"`
10. `},`
11. `"filename" : "llamaKnows.sticker"`
12. `}`
13. `],`
14. `"info" : {`
15. `"author" : "com.developerName",`
16. `"version" : 1`
17. `}`
18. `}`

[Sticker Type](Sticker.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjufvjvomi)

[Sticker Sequence Type](StickerFilmStrip.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjtfvjvomi)
