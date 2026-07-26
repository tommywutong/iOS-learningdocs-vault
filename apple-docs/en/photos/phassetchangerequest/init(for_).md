---
title: 'init(for:)'
framework: Photos
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetchangerequest/init(for:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetchangerequest/init(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetchangerequest/init%28for%3A%29.json'
content_hash: 'sha256:64c58fa7e0114494'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetChangeRequest](../phassetchangerequest.md)

# init(for:)

<sub>Initializer</sub>

Creates a request for modifying the specified asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(for asset: PHAsset)
```

## Parameters

- `asset` — The asset to be modified.

## Return Value

An asset change request.

## Discussion

Before editing an asset, use its [- canPerformEditOperation:](<../phasset/canperform(__).md>) method to see if the asset allows editing.

After you create a change request within a photo library change block, propose changes to the original asset’s properties by setting the corresponding properties of the change request. After Photos runs your change block, the asset’s properties reflect your changes. For details on change blocks, see [PHPhotoLibrary](../phphotolibrary.md).

To edit an asset’s image or video content, first begin a content editing session with the asset’s [- requestContentEditingInputWithOptions:completionHandler:](<../phasset/requestcontenteditinginput(with_completionhandler_).md>) method. You commit a content edit by setting the [contentEditingOutput](contenteditingoutput.md) property of a change request within a change block. For more information about asset content editing, see [PHAsset](../phasset.md).

## See Also

### Modifying Assets

- [creationDate](creationdate.md) — The date and time at which the asset claims to have been originally created.
- [location](location.md) — The location information saved with the asset.
- [favorite](isfavorite.md) — A Boolean value that indicates whether the asset is marked as one of the user’s favorites.
- [hidden](ishidden.md) — A Boolean value that indicates whether the asset is hidden in collections.
- [caption](caption.md) — An asset description to change to. Set to nil or an empty string to clear the caption. _(beta)_
- [- addKeyword:](<addkeyword(__).md>) — Add or remove a keyword associated with this asset Adding a keyword that is already associated (or removing a keyword that is not) will be silently ignored _(beta)_
- [- removeKeyword:](<removekeyword(__).md>) _(beta)_
- [rating](rating.md) _(beta)_
- [- setLivePhotoVideoPlaybackEnabled:](<setlivephotovideoplaybackenabled(__).md>) — Disable or enable the video part of a Live Photo so it just appears as a still image (disabled) or a Live Photo (enabled) _(beta)_
