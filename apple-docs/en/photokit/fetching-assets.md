---
title: Fetching Assets
framework: Photos
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photokit/fetching-assets
source_url: 'https://developer.apple.com/documentation/photokit/fetching-assets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photokit/fetching-assets.json'
content_hash: 'sha256:5d4c1856c54ab43f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotoKit](../photokit.md) · [Photos](../photos.md) · [PHAsset](../photos/phasset.md)

# Fetching Assets

<sub>Article</sub>

Retrieve asset metadata or request full asset content.

## Overview

You fetch assets to begin working with them. Use the class methods listed in Fetching Assets to retrieve one or more [PHAsset](../photos/phasset.md) instances representing the assets you want to display or edit. For example, to fetch all the assets in an asset collection (such as an album or moment), use the [+ fetchAssetsInAssetCollection:options:](<../photos/phasset/fetchassets(in_options_).md>) method. Each fetch method takes a [PHFetchOptions](../photos/phfetchoptions.md) parameter that you use to specify the assets to retrieve and how to sort them.

> [!important] Important
> Accessing or modifying the Photos library requires explicit authorization from the user. The first time you call one of the methods listed in Fetching Assets, Photos automatically prompts the user for authorization. Alternatively, you can use the [PHPhotoLibrary](../photos/phphotolibrary.md) [+ requestAuthorization:](<../photos/phphotolibrary/requestauthorization(__).md>) method to prompt the user at a time of your choosing. For more information, see `Requesting Authorization to Access Photos`.

## See Also

### Fetching Assets

- [+ fetchAssetsInAssetCollection:options:](<../photos/phasset/fetchassets(in_options_).md>) — Retrieves assets from the specified asset collection.
- [+ fetchAssetsWithMediaType:options:](<../photos/phasset/fetchassets(with_options_).md>) — Retrieves assets with the specified media type.
- [+ fetchAssetsWithLocalIdentifiers:options:](<../photos/phasset/fetchassets(withlocalidentifiers_options_).md>) — Retrieves assets with the specified local-device-specific unique identifiers.
- [+ fetchKeyAssetsInAssetCollection:options:](<../photos/phasset/fetchkeyassets(in_options_).md>) — Retrieves assets marked as key assets in the specified asset collection.
- [+ fetchAssetsWithOptions:](<../photos/phasset/fetchassets(with_).md>) — Retrieves all assets matching the specified options.
- [+ fetchAssetsWithBurstIdentifier:options:](<../photos/phasset/fetchassets(withburstidentifier_options_).md>) — Retrieves assets with the specified burst photo sequence identifier.
- [+ fetchAssetsWithALAssetURLs:options:](<../photos/phasset/fetchassets(withalasseturls_options_).md>) — Retrieves assets using URLs provided by the Assets Library framework. _(deprecated)_
