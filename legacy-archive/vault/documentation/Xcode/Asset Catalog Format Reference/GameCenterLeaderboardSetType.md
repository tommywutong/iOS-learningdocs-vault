---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/GameCenterLeaderboardSetType.html
archived_at: '2026-07-18T02:26:54.209535Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## GameCenter Leaderboard Set Type

The image stacks for a named GameCenter leaderboard set.

Identifiers are created by combining the value of the `ASSETCATALOG​_⁠COMPILER​_⁠LEADERBOARD​_⁠SET​_⁠IDENTIFIER​_⁠PREFIX` build setting and the name of the leaderboard set.

### Extension

`.gcleaderboardset`

### Folder Contents

Image stacks.

### Contents.json File (Optional)

Contains metadata (Table 15-1).

__Table 15-1__GameCenter leaderboard set tags

| Key | Type | Description |
| --- | --- | --- |
| `info` | Dictionary | Metadata for the author and format version of the asset catalog. |
| `author` | String | Use your bundle ID. |
| `version` | Number | The format version of the asset catalog. Use `1`. |

### Sample Contents.json File

1. `{`
2. `"info" : {`
3. `"author" : "com.developerName",`
4. `"version" : 1`
5. `}`
6. `}`

[GameCenter Leaderboard Type](GameCenterLeaderboardType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzzfvjvomi)

[Group Type](GroupType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrrfvjvomi)
