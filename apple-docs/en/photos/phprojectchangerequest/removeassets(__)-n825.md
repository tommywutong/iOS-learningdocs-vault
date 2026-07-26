---
title: 'removeAssets(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.14+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phprojectchangerequest/removeassets(_:)-n825'
source_url: 'https://developer.apple.com/documentation/photos/phprojectchangerequest/removeassets(_:)-n825'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phprojectchangerequest/removeassets%28_%3A%29-n825.json'
content_hash: 'sha256:7c86eb8d8ff75e0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHProjectChangeRequest](../phprojectchangerequest.md)

# removeAssets(_:)

<sub>Instance Method</sub>

Removes assets of a certain type from the collection.

<sub>macOS</sub>

```swift
func removeAssets<T>(_ assets: T) where T : Collection, T.Element == PHAsset
```

## Parameters

- `assets` — The type of assets to remove from the collection.

## See Also

### Removing Assets

- [removeAssets(_:)](<removeassets(__)-3ytt3.md>) — Removes assets based on a fetch result.
