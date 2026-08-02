---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/StickerFilmStrip.html
archived_at: '2026-07-18T02:27:22.071300Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Sticker Sequence Type

An animated sticker for a sticker pack. The sticker uses a series of images to generate the animation.

### Extension

`.stickersequence`

### Folder Contents

An image for each frame of the sequence.

### Contents.json File

Metadata, animation information, accessibility text, and filenames for the sticker sequence. For values, see (Table 28-1).

__Table 28-1__Sticker sequence tags

| Key | Type | Description |
| --- | --- | --- |
| `info` | Dictionary | Versioning information for the asset catalog. |
| `author` | String | The application that authored the asset catalog. |
| `version` | Number | The version of the asset catalog. |
| `properties` | Dictionary | Properties for the sprite atlas. |
| `accessibility-label` | String | A custom string used by Voice Over. The sticker name is used if no string is provided. |
| `duration` | Number | Determines the length of the animation cycle as a fixed duration or as a number of frames per second.  The interpretation is controlled by the `duration-type` key. |
| `duration-type` | String | Determines how the number for `duration` is used. For the values, see [duration-type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjtfvjvooa) below. |
| `repetitions` | Number | The number of times the animation repeats in addition to the initial animation.  Use `0` for continuous animation. |
| `frames` | Array of dictionaries | The array of frames in the animation. The order of the animation is the same as the order of the array. |
| `filename` | String | The name of the image file containing the sticker for a frame. |

### Values for Enumerated Tags

### duration-type

The type of duration. The value determines how the `duration` key is used. Values are shown in (Table 28-2).

__Table 28-2__`duration-type` values

| Value | Description |
| --- | --- |
| `fixed` | `duration` is the number of seconds for one animation cycle. |
| `fps` | `duration` is the target frame rate for the animation. |

### Sample Contents.json File

1. `{`
2. `"properties" : {`
3. `"accessibility-label" : "The llama is winking at you.",`
4. `"repetions" : 0,`
5. `"duration-type" : "fps",`
6. `"duration" : 15`
7. `},`
8. `"frames" : [`
9. `{`
10. `"filename" : "001_llamaWink.png"`
11. `},`
12. `{`
13. `"filename" : "002_llamaWink.png"`
14. `},`
15. `…`
16. `{`
17. `"filename" : "015_llamaWink.png"`
18. `}`
19. `],`
20. `"info" : {`
21. `"author" : "com.developerName",`
22. `"version" : 1`
23. `}`
24. `}`

[Sticker Pack Type](StickerPack.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjsfvjvomi)

[Texture Type](2DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvomi)
