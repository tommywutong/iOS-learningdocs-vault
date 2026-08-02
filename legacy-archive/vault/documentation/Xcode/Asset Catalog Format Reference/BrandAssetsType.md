---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/BrandAssetsType.html
archived_at: '2026-07-18T02:26:44.223737Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Brand Assets Type

The brand assets used for your app in the main TV interface and in the App Store. There are three elements in the brand asset:

- __App store icon.__ A layered image used in the App Store.
- __App icon.__ A layered image used to represent your app on the Home screen.
- __Top shelf image.__ An image displayed when your app is selected in the Apple TV App Launcher.

The icons are image stacks, and the top shelf image is an image set. For information in sizes see the [Apple TV Human Interface Guidelines](https://developer.apple.com/tvos/human-interface-guidelines/icons-and-images/image-size-and-resolution/).

### Extension

`.brandassets`

### Folder Contents

Image stacks and image sets.

### Contents.json File (Required)

Metadata and attributes for the individual icon and top shelf elements (Table 9-1).

__Table 9-1__Brand asset tags

| Key | Type | Description |
| --- | --- | --- |
| `info` | Dictionary | Metadata for the author and format version of the asset catalog. |
| `author` | String | Use your bundle ID. |
| `version` | Number | The format version of the asset catalog. Use `1`. |
| `assets` | Array of dictionaries | The icon and top shelf elements in the brand. |
| `idiom` | String | The platform for the element.  The value must be `"tv"`. |
| `filename` | String | The name of the asset catalog folder containing the branding element. |
| `role` | String | The role of the element. See [role](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzxfvjvony) below. |
| `size` | String | The horizontal and vertical size of the element.  The form is `"<horizontal-size>x<vertical-size>"`. |

### Values for Enumerated Tags

### role

The role of the element in the brand (Table 9-2).

__Table 9-2__`role` values

| Value | Description |
| --- | --- |
| `primary-app-icon` | The main icon for the app. The primary icon can have multiple sizes. |
| `top-shelf-image` | An image for the top shelf. |
| `top-shelf-image-wide` | A banner image for the top shelf. |

### Sample Contents.json File

1. `{`
2. `"assets" : [`
3. `{`
4. `"size" : "1280x768",`
5. `"idiom" : "tv",`
6. `"filename" : "App Icon - Large.imagestack",`
7. `"role" : "primary-app-icon"`
8. `},`
9. `{`
10. `"size" : "400x240",`
11. `"idiom" : "tv",`
12. `"filename" : "App Icon - Small.imagestack",`
13. `"role" : "primary-app-icon"`
14. `},`
15. `{`
16. `"size" : "1920x720",`
17. `"idiom" : "tv",`
18. `"filename" : "Top Shelf Image.imageset",`
19. `"role" : "top-shelf-image"`
20. `},`
21. `],`
22. `"info" : {`
23. `"author" : "com.developerName",`
24. `"version" : 1`
25. `}`
26. `}`

[AR Resource Group](AR_Resource_Group.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnrrfvjvomi)

[Catalog Type](CatalogType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrqfvjvomi)
