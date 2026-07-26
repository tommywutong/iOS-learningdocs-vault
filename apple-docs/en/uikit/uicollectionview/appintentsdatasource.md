---
title: appIntentsDataSource
framework: AppIntents
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.4+, iPadOS 18.4+, tvOS 18.4+, visionOS 2.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/appintentsdatasource
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/appintentsdatasource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/appintentsdatasource.json'
content_hash: 'sha256:fc89f7e39525428f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# appIntentsDataSource

<sub>Instance Property</sub>

The object acting as the collection view’s data source for app entity identifiers that make a cell’s content avdiscoverable by Apple Intelligence and Siri.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency weak var appIntentsDataSource: (any UICollectionViewAppIntentsDataSource)? { get set }
```

## Discussion

For more information, refer to doc:providing-contextual-cues-to-Apple-Intelligence-and-Siri and [App Intents](../../appintents.md).
