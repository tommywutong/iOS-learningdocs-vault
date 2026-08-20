---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/AppIconType.html
archived_at: '2026-07-18T02:26:42.536158Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## App Icon Type

The source images for the different sizes and resolutions of your iOS and watchOS app icons.

### Extension

`.appiconset`

### Folder Contents

`.png` files for the icons.

### Contents.json File (Required)

Metadata and attributes for the individual icon files (Table 6-1).

__Table 6-1__App icon tags

| Key | Type | Description |
| --- | --- | --- |
| `info` | Dictionary | Metadata for the author and format version of the asset catalog. |
| `author` | String | Use your bundle ID. |
| `version` | Number | The format version of the asset catalog. Use `1`. |
| `properties` | Dictionary | Properties associated with the app icon. `properties` is an optional key. |
| `pre-rendered` | Boolean | Backward compatibility for iOS 6.0 indicating if the icon includes the mask and shine effect.  `pre-rendered` is an optional key. |
| `images` | Array | Each element identifies one variant of the icon. |
| `filename` | String | The name of the `.png` file containing the image. |
| `display-gamut` | Slot component | The color gamut of the device display. For the values, see [display-gamut](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomzv) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `idiom` | Slot Component | The idiom of the icon. For the values, see [idiom](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomq) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `size` | Slot Component | One of the sizes that matches the idiom for the icon. If the size is not valid, the image is ignored.  For the values, see [size](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrsfvjvooa) below. |
| `scale` | Slot Component | The scale of the icon. For the values, see [scale](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomy) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `subtype` | Slot Component | The scale of the icon. For the values, see [scale](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomy) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi). |
| `role` | Slot Component | The role of the icon in a watch app. For the values, see [role](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrsfvjvomjr) below. |
| `unassigned` | Boolean | Used by Xcode. |
| `matching-style` | Enum | The type of matching for the system to use to find the referenced file. The only valid value is `fully-qualified-name`. |

### Values for Enumerated Tags

### display-gamut

See [display-gamut](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomzv) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### idiom

See [idiom](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomq) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### size

The size of the app icon in points. Also see [Points Versus Pixels](../../Windows%20Views/View%20Programming%20Guide%20for%20iOS/View%20and%20Window%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbtfvbuqmrnknltcni) (Table 6-2).

__Table 6-2__`size` values

| Value | Description |
| --- | --- |
| `16x16` | An OS X icon. |
| `20x20` | An iPhone or iPad notification icon. |
| `24x24` | A 38mm Apple Watch notification center icon. |
| `27.5x27.5` | A 42mm Apple Watch notification center icon. |
| `29x29` | An iPhone or iPad settings icon for iOS 7 or later.  An Apple Watch companion settings icon. |
| `32x32` | An OS X icon. |
| `40x40` | An iPhone or iPad Spotlight search results icon on iOS 7 or later.  The main Apple Watch app icon. |
| `44x44` | An Apple Watch long-look notification icon. |
| `60x60` | The main iPhone app icon for iOS 7 or later. |
| `76x76` | The main iPad app icon for iOS 7 or later. |
| `83.5x83.5` | The main iPad Pro app icon. |
| `86x86` | A 38mm Apple Watch short-look notification icon. |
| `98x98` | A 42mm Apple Watch short-look notification icon. |
| `128x128` | An OS X icon. |
| `256x256` | An OS X icon. |
| `512x512` | An OS X icon. |
| `1024x1024` | The App Store icon. |

### scale

See [scale](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomy) in [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi).

### subtype

The type of Apple Watch when there is more than one icon size for a role.

__Table 6-3__`subtype` values

| Value | Description |
| --- | --- |
| Tag not included | The icon is not for Apple Watch. |
| `38mm` | The icon is for a 38mm Apple Watch. |
| `42mm` | The icon is for a 42mm Apple Watch. |

### role

The role for an Apple Watch icon (Table 6-4).

__Table 6-4__`role` values

| Value | Description |
| --- | --- |
| Tag not included | The icon is not for Apple Watch. |
| `notificationCenter` | The icon is used in the notification center. |
| `companionSettings` | The icon is used in settings. |
| `appLauncher` | The icon is used in the app launcher. |
| `longLook` | The icon is used for a long-look notification. |
| `quickLook` | The icon is used for a short-look notification. |

### Sample Contents.json File

1. `{`
2. `"images" : [`
3. `{`
4. `"filename" : "my-iphone-app",`
5. `"idiom" : "iphone",`
6. `"size" : "60x60",`
7. `"scale" : "2x",`
8. `},`
9. `…`
10. `],`
11. `"info" : {`
12. `"author" : "com.developerName",`
13. `"version" : 1`
14. `}`
15. `}`

[Types Overview](AssetTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzqfvjvomi)

[AR Reference Image](AR_Reference_Image.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnrqfvjvomi)
