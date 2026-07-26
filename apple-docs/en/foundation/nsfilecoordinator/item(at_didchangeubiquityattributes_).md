---
title: 'item(at:didChangeUbiquityAttributes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilecoordinator/item(at:didchangeubiquityattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/item(at:didchangeubiquityattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/item%28at%3Adidchangeubiquityattributes%3A%29.json'
content_hash: 'sha256:fb9001f161166798'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileCoordinator](../nsfilecoordinator.md)

# item(at:didChangeUbiquityAttributes:)

<sub>Instance Method</sub>

Tells observing file providers that the item’s ubiquity attributes have changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func item(at url: URL, didChangeUbiquityAttributes attributes: Set<URLResourceKey>)
```

## Discussion

This method triggers the [NSFilePresenter](https://developer.apple.com/library/archive/releasenotes/Foundation/RN-FoundationOlderNotes/index.html#//apple_ref/doc/uid/TP40008080-TRANSLATED_CHAPTER_965-TRANSLATED_DEST_6) protocol’s [- presentedItemDidChangeUbiquityAttributes:](<../nsfilepresenter/presenteditemdidchangeubiquityattributes(__).md>) method on any file presenters that are observing the item, even if they are running in different processes.

For information about the types of attributes that can trigger notifications, see the [NSFilePresenter](../nsfilepresenter.md) protocol’s [observedPresentedItemUbiquityAttributes](../nsfilepresenter/observedpresenteditemubiquityattributes.md) property.
