---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/AR_Resource_Group.html
archived_at: '2026-07-18T02:26:41.027702Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## AR Resource Group

A set of [ARReferenceImage](https://developer.apple.com/documentation/arkit/arreferenceimage)s loaded by [referenceImages(inGroupNamed:bundle:)](https://developer.apple.com/documentation/arkit/arreferenceimage/2948910-referenceimagesingroupnamed).

### Extension

`.arresourcegroup`

### Folder Contents

A set of unique [AR Reference Image](AR_Reference_Image.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnrqfvjvomi) items.

### Contents.json File (Required)

Metadata, on-demand resource tags, and a list of the AR Reference Images (Table 8-1.)

__Table 8-1__AR resource group tags

| Key | Type | Description |
| --- | --- | --- |
| info | Dictionary | Metadata for the author and format version of the asset catalog. |
| `author` | String | Use your bundle ID. |
| `version` | Number | The format version of the asset catalog. Use `1`. |
| `properties` | Dictionary | Properties for the image set. |
| `on-demand-resource-tags` | Array of strings | The on-demand resource tags for the resource group. |
| resources | Array | The reference images contained in the group. |
| `filename` | String | The name of the asset catalog folder containing an `ARReferenceImage`. |

### Sample Contents.json File

1. `{`
2. `"resources" : [`
3. `{`
4. `"filename" : "Reference image 1.arreferenceimage"`
5. `},`
6. `{`
7. `"filename" : "Another reference image.arreferenceimage"`
8. `},`
9. `…`
10. `],`
11. `"properties" : {`
12. `"on-demand-resources : [`
13. `"llama",`
14. `"mountain"`
15. `]`
16. `},`
17. `"info" : {`
18. `"author" : "com.developerName",`
19. `"version" : 1`
20. `}`
21. `}`

[AR Reference Image](AR_Reference_Image.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnrqfvjvomi)

[Brand Assets Type](BrandAssetsType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzxfvjvomi)
