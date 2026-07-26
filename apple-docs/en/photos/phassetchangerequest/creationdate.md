---
title: creationDate
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetchangerequest/creationdate
source_url: 'https://developer.apple.com/documentation/photos/phassetchangerequest/creationdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetchangerequest/creationdate.json'
content_hash: 'sha256:ba409009db825d3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetChangeRequest](../phassetchangerequest.md)

# creationDate

<sub>Instance Property</sub>

The date and time at which the asset claims to have been originally created.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var creationDate: Date? { get set }
```

## Discussion

Set this property to change the creation date of an asset.

## See Also

### Modifying Assets

- [+ changeRequestForAsset:](<init(for_).md>) — Creates a request for modifying the specified asset.
- [location](location.md) — The location information saved with the asset.
- [favorite](isfavorite.md) — A Boolean value that indicates whether the asset is marked as one of the user’s favorites.
- [hidden](ishidden.md) — A Boolean value that indicates whether the asset is hidden in collections.
- [caption](caption.md) — An asset description to change to. Set to nil or an empty string to clear the caption. _(beta)_
- [- addKeyword:](<addkeyword(__).md>) — Add or remove a keyword associated with this asset Adding a keyword that is already associated (or removing a keyword that is not) will be silently ignored _(beta)_
- [- removeKeyword:](<removekeyword(__).md>) _(beta)_
- [rating](rating.md) _(beta)_
- [- setLivePhotoVideoPlaybackEnabled:](<setlivephotovideoplaybackenabled(__).md>) — Disable or enable the video part of a Live Photo so it just appears as a still image (disabled) or a Live Photo (enabled) _(beta)_
