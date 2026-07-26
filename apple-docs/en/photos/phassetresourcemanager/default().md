---
title: default()
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourcemanager/default()
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcemanager/default()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcemanager/default%28%29.json'
content_hash: 'sha256:82ab79e698bfc447'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceManager](../phassetresourcemanager.md)

# default()

<sub>Type Method</sub>

Returns the shared asset resource manager object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func `default`() -> PHAssetResourceManager
```

## Return Value

The asset resource manager.

## Discussion

This method always returns the same asset resource manager object, which is shared for all uses in your app.
