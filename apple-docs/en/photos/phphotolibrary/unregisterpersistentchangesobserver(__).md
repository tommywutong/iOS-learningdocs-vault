---
title: 'unregisterPersistentChangesObserver(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/photos/phphotolibrary/unregisterpersistentchangesobserver(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/unregisterpersistentchangesobserver(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/unregisterpersistentchangesobserver%28_%3A%29.json'
content_hash: 'sha256:b7966f01fc796c8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# unregisterPersistentChangesObserver(_:)

<sub>Instance Method</sub>

Unregisters a previously registered persistent changes observer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func unregisterPersistentChangesObserver(_ observer: any PHPhotoLibraryPersistentChangesObserver)
```

## Discussion

After calling this method, the observer will no longer receive persistent changes callbacks.
