---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/AssetTypes.html
archived_at: '2026-07-18T02:26:43.680353Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Types Overview

The folders in asset catalogs represent the overall asset catalog, groups of assets and other groups, and several different types of assets. Some of the asset types in a catalog work only with selected Apple platforms.

### Content Types

The type of content represented by a folder is encoded in the extension for the name of the folder. For example, a folder named `PosingLlamas.imageset` has a type of `imageset`.

Table 5-1 lists the content types, folder name extension, and a brief description of each type.

> [!IMPORTANT]
> 

__Table 5-1__Content types

| Folder type | Extension | Description |
| --- | --- | --- |
| [App Icon Type](AppIconType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrsfvjvomi) | `.appiconset` | The various sizes of the icon for an iOS or watchOS app.    Children are `.png` files. |
| [AR Reference Image](AR_Reference_Image.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnrqfvjvomi) | `.arimageset` | An image file for an [ARReferenceImage](https://developer.apple.com/documentation/arkit/arreferenceimage). Supported file formats include HEIF (High Efficiency Image Format), JPEG, PNG, and TIFF. |
| [AR Resource Group](AR_Resource_Group.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnrrfvjvomi) | `.arresourcegroup` | A group of reference images for ARKit.    Children are AR Reference Image folders. |
| [Brand Assets Type](BrandAssetsType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzxfvjvomi) | `.brandassets` | The layered app icons and top shelf image for your app.    Children are image stacks and image sets. |
| [Catalog Type](CatalogType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrqfvjvomi) | `.xcassets` | The top level folder for the asset catalog.    Children are any valid asset type except Catalog. |
| [Cube Texture Type](3DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjrfvjvomi) | `.cubetextureset` | A 3D texture mapped onto a cube.    Children are `.mipmapset` folders. |
| [Data Set Type](DataSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrtfvjvomi) | `.dataset` | Used to include arbitrary app data.    Children are files in any format except binary executable code. |
| [GameCenter Dashboard Image Set Type](GameCenterDashboardImagesetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzyfvjvomi) | `.gcdashboardimage` | Images for the logos in a GameCenter dashboard.    Children are image sets. |
| [GameCenter Leaderboard Type](GameCenterLeaderboardType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzzfvjvomi) | `.gcleaderboard` | Background image stack for a GameCenter leaderboard.    Children are image stacks. |
| [GameCenter Leaderboard Set Type](GameCenterLeaderboardSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnbqfvjvomi) | `.gcleaderboardset` | Background image stack for a GameCenter leaderboard set.    Children are image stacks. |
| [Group Type](GroupType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrrfvjvomi) | _None_.  No period (.) can appear in the name of the group. | A group of other elements.    Children are any valid asset type except Catalog. |
| [Icon Set Type](IconSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrufvjvomi) | `.iconset` | A replica of the `.iconset` format for OS X apps.    Children are `.png` files. |
| [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi) | `.imageset` | An image used for `UIImage`, `NSImage`, user interface controls, and other objects using images.    Children are `HEIF`(High Efficiency Image Format), `.png`, `.jpg`, `.pdf` files. |
| [Image Stack Type](ImageStackType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnbrfvjvomi) | `.imagestack` | A set of layered images combined to enable parallax.    Children are image stack layers. |
| [Image Stack Layer Type](ImageStackLayerType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnbsfvjvomi) | `.imagestacklayer` | A layer in an image stack.    Children are image sets. |
| [Launch Image Type](LaunchImageType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrwfvjvomi) | `.launchimage` | Support for app launch images.    Children are `.png` files. |
| [Mipmap Type](MIPMapType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjxfvjvomi) | `.mipmapset` | An optimized set of texture images at different resolutions.    Children are files for the different resolutions. |
| [Named Color Type](Named_Color.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjzfvjvomi) | `.colorset` | A named color. The name of the color can be used anywhere in an Xcode project. |
| [Sprite Atlas Type](SpriteAtlasType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrxfvjvomi) | `.spriteatlas` | The image sets used for an `SKTextureAtlas` class.    Children are image set asset folders. |
| [Sticker Type](Sticker.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjufvjvomi) | `.sticker` | A sticker for a sticker pack.    Child is the image for the sticker. |
| [Sticker Pack Type](StickerPack.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjsfvjvomi) | `.stickerpack` | A pack of stickers for messaging.    Children are `.stickersequence` and `.sticker` folders. |
| [Sticker Sequence Type](StickerFilmStrip.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjtfvjvomi) | `.stickersequence` | A set of images for an animated sticker.    Children are the images for the animation. |
| [Texture Type](2DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvomi) | `.textureset` | A 2D texture.    Children are `.mipmapset` folders. |
| [Watch Complications Type](WatchComplicationsType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzufvjvomi) | `.complicationset` | The image sets used for the different types of watch complications.    Children are image set folders. |

### Contents.json File

The `Contents.json` file specifies metadata for the asset catalog, attributes for a folder type, and attributes for asset files. Table 5-2 shows whether a `Contents.json` file is required, optional, or not used for each folder type.

__Table 5-2__`Contents.json` file required

| Folder type | `Contents.json` |
| --- | --- |
| [App Icon Type](AppIconType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrsfvjvomi) | Required |
| [Brand Assets Type](BrandAssetsType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzxfvjvomi) | Required |
| [Catalog Type](CatalogType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrqfvjvomi) | Optional |
| [Cube Texture Type](3DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjrfvjvomi) | Required |
| [Data Set Type](DataSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrtfvjvomi) | Required |
| [GameCenter Dashboard Image Set Type](GameCenterDashboardImagesetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzyfvjvomi) | Optional |
| [GameCenter Leaderboard Type](GameCenterLeaderboardType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzzfvjvomi) | Optional |
| [GameCenter Leaderboard Set Type](GameCenterLeaderboardSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnbqfvjvomi) | Optional |
| [Group Type](GroupType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrrfvjvomi) | Optional |
| [Icon Set Type](IconSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrufvjvomi) | None |
| [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi) | Required |
| [Image Stack Type](ImageStackType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnbrfvjvomi) | Required |
| [Image Stack Layer Type](ImageStackLayerType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnbsfvjvomi) | Optional |
| [Launch Image Type](LaunchImageType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrwfvjvomi) | Required |
| [Mipmap Type](MIPMapType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjxfvjvomi) | Required |
| [Sprite Atlas Type](SpriteAtlasType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrxfvjvomi) | Optional |
| [Sticker Type](Sticker.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjufvjvomi) | Required |
| [Sticker Pack Type](StickerPack.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjsfvjvomi) | Required |
| [Sticker Sequence Type](StickerFilmStrip.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjtfvjvomi) | Required |
| [Texture Type](2DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvomi) | Required |
| [Watch Complications Type](WatchComplicationsType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzufvjvomi) | Required |

### Platform Types

Table 5-3 shows the valid platforms for each folder type.

__Table 5-3__Folder type platforms

| Element | iOS | OS X | tvOS | watchOS |
| --- | --- | --- | --- | --- |
| [App Icon Type](AppIconType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrsfvjvomi) | ✓ | – | – | ✓ |
| [Brand Assets Type](BrandAssetsType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzxfvjvomi) | – | – | ✓ | – |
| [Catalog Type](CatalogType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrqfvjvomi) | ✓ | ✓ | ✓ | ✓ |
| [Cube Texture Type](3DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjrfvjvomi) | ✓ | ✓ | ✓ | ✓ |
| [Data Set Type](DataSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrtfvjvomi) | ✓ | ✓ | ✓ | ✓ |
| [GameCenter Dashboard Image Set Type](GameCenterDashboardImagesetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzyfvjvomi) | – | – | ✓ | – |
| [GameCenter Leaderboard Type](GameCenterLeaderboardType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzzfvjvomi) | – | – | ✓ | – |
| [GameCenter Leaderboard Set Type](GameCenterLeaderboardSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnbqfvjvomi) | – | – | ✓ | – |
| [Group Type](GroupType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrrfvjvomi) | ✓ | ✓ | ✓ | ✓ |
| [Icon Set Type](IconSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrufvjvomi) | – | ✓ | – | – |
| [Image Set Type](ImageSetType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrvfvjvomi) | ✓ | ✓ | ✓ | ✓ |
| [Image Stack Type](ImageStackType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnbrfvjvomi) | – | – | ✓ | – |
| [Image Stack Layer Type](ImageStackLayerType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnbsfvjvomi) | – | – | ✓ | – |
| [Launch Image Type](LaunchImageType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrwfvjvomi) | ✓ | – | ✓ | – |
| [Mipmap Type](MIPMapType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjxfvjvomi) | ✓ | ✓ | ✓ | – |
| [Sprite Atlas Type](SpriteAtlasType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrxfvjvomi) | ✓ | ✓ | ✓ | – |
| [Sticker Type](Sticker.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjufvjvomi) | ✓ | ✓ | ✓ | ✓ |
| [Sticker Pack Type](StickerPack.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjsfvjvomi) | ✓ | ✓ | ✓ | ✓ |
| [Sticker Sequence Type](StickerFilmStrip.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjtfvjvomi) | ✓ | ✓ | ✓ | ✓ |
| [Texture Type](2DTextureType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnjvfvjvomi) | ✓ | ✓ | ✓ | ✓ |
| [Watch Complications Type](WatchComplicationsType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzufvjvomi) | – | – | – | ✓ |

[Adding Asset Catalogs to Projects](AddingAssetCatalogstoXcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzvfvjvomi)

[App Icon Type](AppIconType.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmrsfvjvomi)
