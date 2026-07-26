---
title: 'presentedItemDidChangeUbiquityAttributes(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilepresenter/presenteditemdidchangeubiquityattributes(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/presenteditemdidchangeubiquityattributes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/presenteditemdidchangeubiquityattributes%28_%3A%29.json'
content_hash: 'sha256:86a0ea05729631f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# presentedItemDidChangeUbiquityAttributes(_:)

<sub>Instance Method</sub>

Tells your object that the file or file package’s ubiquity attributes have changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
optional func presentedItemDidChangeUbiquityAttributes(_ attributes: Set<URLResourceKey>)
```

## Parameters

- `attributes` — The set of ubiquity attributes that have changed. For information about valid ubiquity attributes, see the [observedPresentedItemUbiquityAttributes](observedpresenteditemubiquityattributes.md) property.

## Discussion

To specify the ubiquity attributes that trigger notifications, implement your file provider’s [observedPresentedItemUbiquityAttributes](observedpresenteditemubiquityattributes.md) property. If you do not implement this property, the system sends notifications when any ubiquity attribute changes.

> [!note] Note
> Changes to the ubiquity attributes don’t typically align with [- presentedItemDidChange](<presenteditemdidchange().md>) notifications.

## See Also

### Related Documentation

- [- itemAtURL:didChangeUbiquityAttributes:](<../nsfilecoordinator/item(at_didchangeubiquityattributes_).md>) — Tells observing file providers that the item’s ubiquity attributes have changed.

### Ubiquity Change Notifications

- [observedPresentedItemUbiquityAttributes](observedpresenteditemubiquityattributes.md) — A list of ubiquity attributes used to generate and send notifications whenever an attribute in the list changes.
