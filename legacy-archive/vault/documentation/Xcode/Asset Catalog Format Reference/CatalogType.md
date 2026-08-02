---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/CatalogType.html
archived_at: '2026-07-18T02:26:45.825358Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Catalog Type

The root level folder of an asset catalog. There can only be one of these in an asset catalog.

### Extension

`.xcassets`

### Folder Contents

Any asset type except catalog.

### Contents.json File (Optional)

Metadata relating to the catalog (Table 10-1).

__Table 10-1__Catalog tags

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

[Brand Assets Type](BrandAssetsType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzxfvjvomi)

[Cube Texture Type](3DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjrfvjvomi)
