---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/LaunchImageType.html
archived_at: '2026-07-18T02:27:13.033324Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Launch Image Type

Launch images contain the different sizes and resolutions for an app launch image. They are required for iOS 7.0 and earlier. New projects for iOS 8.0 and later default to using a launch screen storyboard.

### Extension

`.launchimage`

### Folder Contents

`.png` files.

### Contents.json File (Required)

Metadata and attributes for the individual resource files (Table 21-1).

__Table 21-1__Launch image tags

| Key | Type | Description |
| --- | --- | --- |
| `info` | Dictionary | Metadata for the author and format version of the asset catalog. |
| `author` | String | Use your bundle ID. |
| `version` | Number | The format version of the asset catalog. Use `1`. |
| `data` | Array of dictionaries | The launch images in the set. |
| `filename` | String | The `.png` file for the launch screen image. |
| `idiom` | Slot component | The device type for the launch image. For the values, see [idiom](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomq) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `orientation` | Slot component | The valid device orientations for the launch image. For the values, see [orientation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrwfvjvooa) below. |
| `scale` | Slot component | The scale of the launch image. For the values, see [scale](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomy) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `subtype` | Slot component | A subtype for the launch image. For the values, see [subtype](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrwfvjvomjr) below. |
| `minimum-system-version` | Slot component | The minimum system version for the launch image. For the values, see [minimum-system-version](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrwfvjvomjs) below. |
| `extent` | Slot component | The vertical extent of the launch image. For the values, see [extent](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrwfvjvomju) below. |

### Values for Enumerated Tags

### idiom

See [idiom](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomq) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### orientation

The device orientation for the launch image (Table 21-2).

__Table 21-2__`orientation` values

| Value | Description |
| --- | --- |
| `portrait` | The launch image is for a device in portrait orientation. |
| `landscape` | The launch image is for a device in landscape orientation. |

### scale

See [scale](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomy) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### subtype

The targeted iPhone screen height for the image (Table 21-3).

__Table 21-3__`subtype` values

| Value | Description |
| --- | --- |
| Tag not included | The image is for a 3.5-inch iPhone screen. |
| `retina4` | The image is for a 4-inch iPhone screen. |
| `667h` | The image is for a 4.7-inch iPhone screen. |
| `736h` | The image is for a 5.5-inch iPhone screen. |

### minimum-system-version

The minimum system version for the launch image (Table 21-4).

__Table 21-4__`minimum-system-version` values

| Value | Description |
| --- | --- |
| Tag not included | There is no minimum system version for the launch image. |
| `7.0` | The launch image is for iOS 7.0 or later. |
| `8.0` | The launch image is for iOS 8.0 or later. |
| `9.0` | The launch image is for iOS 9.0 or later. |

### extent

The extent of the image in the vertical dimension of the screen (Table 21-5).

__Table 21-5__`extent` values

| Value | Description |
| --- | --- |
| `to-status-bar` | The launch image extends from the bottom of the screen to the bottom of the status bar. |
| `full-screen`  `regular` (deprecated) | The launch image extends the full height of the screen. |

### Sample Contents.json File

1. `{`
2. `"images" : [`
3. `{`
4. `"filename" : "MyLaunchScreen-iPhone-portrait"`
5. `"orientation" : "portrait"`
6. `"idiom" : "iphone",`
7. `"extent" : "full-screen"`
8. `"minimum-system-version" : "8.0",`
9. `"scale" : "3x",`
10. `},`
11. `…`
12. `],`
13. `"info" : {`
14. `"author" : "com.developerName",`
15. `"version" : 1`
16. `}`
17. `}`

[Image Stack Layer Type](ImageStackLayerType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnbsfvjvomi)

[Messages Extension Icon Type](MessagesIconType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjyfvjvomq)
