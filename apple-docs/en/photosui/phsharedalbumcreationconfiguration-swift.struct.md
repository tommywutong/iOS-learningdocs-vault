---
title: PHSharedAlbumCreationConfiguration
framework: PhotosUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/photosui/phsharedalbumcreationconfiguration-swift.struct
source_url: 'https://developer.apple.com/documentation/photosui/phsharedalbumcreationconfiguration-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phsharedalbumcreationconfiguration-swift.struct.json'
content_hash: 'sha256:fdeb24bdb9388646'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHSharedAlbumCreationConfiguration

<sub>Structure</sub>

An object used to configure a `PHSharedAlbumCreationViewController`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct PHSharedAlbumCreationConfiguration
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Initializers

- [init(photoLibrary:)](<phsharedalbumcreationconfiguration-swift.struct/init(photolibrary_).md>)

### Instance Properties

- [defaultPolicy](phsharedalbumcreationconfiguration-swift.struct/defaultpolicy.md) — The default sharing policy of the shared album. If not specified, this defaults to `PHSharedAlbumCreationSharingPolicyPrivate`.
- [defaultTitle](phsharedalbumcreationconfiguration-swift.struct/defaulttitle.md) — The default title for the shared album. Useful for suggesting a relevant title to the user. Defaults to `nil`.
- [photoLibrary](phsharedalbumcreationconfiguration-swift.struct/photolibrary.md) — The photo library in which the shared album will be created.
