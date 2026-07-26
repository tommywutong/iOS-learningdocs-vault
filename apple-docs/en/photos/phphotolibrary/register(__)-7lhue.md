---
title: 'register(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/photos/phphotolibrary/register(_:)-7lhue'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/register(_:)-7lhue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/register%28_%3A%29-7lhue.json'
content_hash: 'sha256:ae8b5dd2364b8a6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# register(_:)

<sub>Instance Method</sub>

Registers an observer to be notified when persistent changes occur in the photo library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func register(_ observer: any PHPhotoLibraryPersistentChangesObserver)
```

## Discussion

The observer is held weakly by the photo library. The observer’s [- photoLibraryPersistentChangesDidUpdate:](<../phphotolibrarypersistentchangesobserver/photolibrarypersistentchangesdidupdate(__).md>) method is called on an arbitrary serial queue when changes are committed to the photo library. Use [- fetchPersistentChangesSinceToken:error:](<fetchpersistentchanges(since_).md>) to retrieve the specific changes.

Requires read-write photo library authorization ([PHAccessLevelReadWrite](../phaccesslevel/readwrite.md)).
