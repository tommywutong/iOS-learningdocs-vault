---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/GameCenterDashboardImagesetType.html
archived_at: '2026-07-18T02:26:52.620858Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## GameCenter Dashboard Image Set Type

The graphical image files for a GameCenter dashboard logo.

### Extension

`.gcdashboardimage`

### Folder Contents

Image sets.

### Contents.json File (Optional)

Contains metadata (Table 13-1).

__Table 13-1__GameCenter dashboard tags

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

[Data Set Type](DataSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrtfvjvomi)

[GameCenter Leaderboard Type](GameCenterLeaderboardType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzzfvjvomi)
