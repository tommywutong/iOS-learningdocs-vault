---
title: 'collectionView(_:sceneActivationConfigurationForItemAt:point:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:sceneactivationconfigurationforitemat:point:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:sceneactivationconfigurationforitemat:point:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Asceneactivationconfigurationforitemat%3Apoint%3A%29.json'
content_hash: 'sha256:aa5ebe7b0f7d84c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:sceneActivationConfigurationForItemAt:point:)

<sub>Instance Method</sub>

Returns a scene activation configuration that allows the cell to expand into a new scene.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, sceneActivationConfigurationForItemAt indexPath: IndexPath, point: CGPoint) -> UIWindowScene.ActivationConfiguration?
```

## Parameters

- `collectionView` — The collection view.

- `indexPath` — The index path of the cell with which the user is interacting.

- `point` — The location of the interaction in the collection view’s coordinate space.

## Return Value

A [ActivationConfiguration](../uiwindowscene/activationconfiguration.md) object that facilitates expanding the cell into a new scene. Return `nil` to prevent the interaction from starting.
