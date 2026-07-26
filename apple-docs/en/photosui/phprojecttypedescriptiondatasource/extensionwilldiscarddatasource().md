---
title: extensionWillDiscardDataSource()
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.14+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phprojecttypedescriptiondatasource/extensionwilldiscarddatasource()
source_url: 'https://developer.apple.com/documentation/photosui/phprojecttypedescriptiondatasource/extensionwilldiscarddatasource()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phprojecttypedescriptiondatasource/extensionwilldiscarddatasource%28%29.json'
content_hash: 'sha256:5e22107b503083f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHProjectTypeDescriptionDataSource](../phprojecttypedescriptiondatasource.md)

# extensionWillDiscardDataSource()

<sub>Instance Method</sub>

Provides an opportunity to use the data source before it’s released.

<sub>macOS</sub>

```swift
optional func extensionWillDiscardDataSource()
```

## Discussion

After this call, the extension context no longer strongly references the data source. Fetch any last data you need here before the data source goes out of scope.
