---
title: shared()
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phphotolibrary/shared()
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/shared()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/shared%28%29.json'
content_hash: 'sha256:66b9fcd66510295d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# shared()

<sub>Type Method</sub>

Retrieves the shared photo library object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func shared() -> PHPhotoLibrary
```

## Return Value

The singleton photo library object.

## Discussion

You may use the shared photo library object from any thread.
