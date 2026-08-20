---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/GroupType.html
archived_at: '2026-07-18T02:26:55.266932Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Group Type

A group of named assets and other named groups, including nested groups.

### Extension

None. No period (.) can appear in the name of the group.

### Folder Contents

Any asset type except catalog.

### Contents.json File (Optional)

Metadata and on-demand resource tags (Table 16-1).

__Table 16-1__Group tags

| Key | Type | Description |
| --- | --- | --- |
| `info` | Dictionary | Metadata for the author and format version of the asset catalog. |
| `author` | String | Use your bundle ID. |
| `version` | Number | The format version of the asset catalog. Use `1`. |
| `properties` | Dictionary | Properties for the group. |
| `on-demand-resource-tags` | Array of strings | The on-demand resource tags for all the assets in the group folder. |
| `provides-namespace` | Boolean | Use the group name as a namespace element for accessing any of the contents.  For more information, see [Unique Asset Names](FolderStructure.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmztfvjvona). |

### Sample Contents.json File

1. `{`
2. `"info" : {`
3. `"author" : "com.developerName",`
4. `"version" : 1`
5. `},`
6. `"properties" : {`
7. `"on-demand-resources : [`
8. `"level-1"`
9. `]`
10. `}`
11. `}`

[GameCenter Leaderboard Set Type](GameCenterLeaderboardSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnbqfvjvomi)

[Icon Set Type](IconSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrufvjvomi)
