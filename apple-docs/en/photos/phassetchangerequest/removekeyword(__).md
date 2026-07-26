---
title: 'removeKeyword(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/photos/phassetchangerequest/removekeyword(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetchangerequest/removekeyword(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetchangerequest/removekeyword%28_%3A%29.json'
content_hash: 'sha256:d79ba0fa284e0243'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetChangeRequest](../phassetchangerequest.md)

# removeKeyword(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeKeyword(_ keyword: String)
```

## See Also

### Modifying Assets

- [+ changeRequestForAsset:](<init(for_).md>) — Creates a request for modifying the specified asset.
- [creationDate](creationdate.md) — The date and time at which the asset claims to have been originally created.
- [location](location.md) — The location information saved with the asset.
- [favorite](isfavorite.md) — A Boolean value that indicates whether the asset is marked as one of the user’s favorites.
- [hidden](ishidden.md) — A Boolean value that indicates whether the asset is hidden in collections.
- [caption](caption.md) — An asset description to change to. Set to nil or an empty string to clear the caption. _(beta)_
- [- addKeyword:](<addkeyword(__).md>) — Add or remove a keyword associated with this asset Adding a keyword that is already associated (or removing a keyword that is not) will be silently ignored _(beta)_
- [rating](rating.md) _(beta)_
- [- setLivePhotoVideoPlaybackEnabled:](<setlivephotovideoplaybackenabled(__).md>) — Disable or enable the video part of a Live Photo so it just appears as a still image (disabled) or a Live Photo (enabled) _(beta)_
