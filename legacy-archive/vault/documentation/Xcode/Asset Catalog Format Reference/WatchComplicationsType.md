---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/WatchComplicationsType.html
archived_at: '2026-07-18T02:27:23.220283Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Watch Complications Type

The image sets for the required watch complication placeholder images. For information on watch complications, see [Complication Essentials](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/ComplicationEssentials.html#//apple_ref/doc/uid/TP40014969-CH27) in _[App Programming Guide for watchOS](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)_.

### Extension

`.complicationset`

### Folder Contents

Image sets for each of the required watch complication types.

### Contents.json File (Required)

Metadata and attributes for each required complication type (Table 30-1).

__Table 30-1__Data set tags

| Key | Type | Description |
| --- | --- | --- |
| `info` | Dictionary | Versioning information for the asset catalog. |
| `author` | String | The application that authored the asset catalog. |
| `version` | Number | The version of the asset catalog. |
| `assets` | Array | The image sets for each required complication type. |
| `idiom` | Slot component | The device idiom of the watch complication image set. It must be set to `"watch"`. |
| `filename` | String | The name of the asset catalog folder containing the image set for the complication. |
| `role` | Slot component | The role of the required complication. For the values, see [role](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzufvjvony) below. |

### Values for Enumerated Tags

### role

The type of complication (Table 30-2).

__Table 30-2__`role` values

| Value | Description |
| --- | --- |
| `circular` | The image set for a small circular complication. |
| `modular` | The image set for a small modular complication. |
| `utilitarian` | The image set for a small utilitarian complication. |

### Sample Contents.json File

1. `{`
2. `"assets" : [`
3. `{`
4. `"idiom" : "watch",`
5. `"filename" : "MyCircularComplication.imageset",`
6. `"role" : "circular"`
7. `},`
8. `{`
9. `"idiom" : "watch",`
10. `"filename" : "MyModularComplication.imageset",`
11. `"role" : "modular"`
12. `},`
13. `{`
14. `"idiom" : "watch",`
15. `"filename" : "MyUtilitarianComplication.imageset",`
16. `"role" : "utilitarian"`
17. `}`
18. `],`
19. `"info" : {`
20. `"author" : "com.developerName",`
21. `"version" : 1`
22. `]`
23. `}`
24. `}`

[Texture Type](2DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvomi)

[LSR Format Overview](LSRFormatOverview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnbufvjvomi)
