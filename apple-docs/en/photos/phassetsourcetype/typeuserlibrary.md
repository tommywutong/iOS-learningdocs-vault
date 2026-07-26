---
title: typeUserLibrary
framework: Photos
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetsourcetype/typeuserlibrary
source_url: 'https://developer.apple.com/documentation/photos/phassetsourcetype/typeuserlibrary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetsourcetype/typeuserlibrary.json'
content_hash: 'sha256:2129a5889ae6bb03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetSourceType](../phassetsourcetype.md)

# typeUserLibrary

<sub>Type Property</sub>

The asset is part of the user’s main Photos library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var typeUserLibrary: PHAssetSourceType { get }
```

## Discussion

The main library contains both assets that originate on the device (such as photos and videos captured with the Camera app or screenshots) and assets synchronized through iCloud Photo Library or My Photo Stream. These assets appear in Moments collections and can be edited or deleted.

## See Also

### Constants

- [PHAssetSourceTypeCloudShared](typecloudshared.md) — The asset originates from an iCloud Shared Album.
- [PHAssetSourceTypeiTunesSynced](typeitunessynced.md) — The asset originates from a Mac or PC and is present on the device through iTunes sync.
