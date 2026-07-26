---
title: default()
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagemanager/default()
source_url: 'https://developer.apple.com/documentation/photos/phimagemanager/default()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagemanager/default%28%29.json'
content_hash: 'sha256:315d1279b6c1751f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageManager](../phimagemanager.md)

# default()

<sub>Type Method</sub>

Returns the shared image manager object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func `default`() -> PHImageManager
```

## Return Value

The image manager.

## Discussion

This method always returns the same image manager object, which is shared for all uses in your app.
