---
title: observedPresentedItemUbiquityAttributes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilepresenter/observedpresenteditemubiquityattributes
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/observedpresenteditemubiquityattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/observedpresenteditemubiquityattributes.json'
content_hash: 'sha256:7c022efc160691f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# observedPresentedItemUbiquityAttributes

<sub>Instance Property</sub>

A list of ubiquity attributes used to generate and send notifications whenever an attribute in the list changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
optional var observedPresentedItemUbiquityAttributes: Set<URLResourceKey> { get }
```

## Discussion

Valid attributes include the [NSURLIsUbiquitousItemKey](../urlresourcekey/isubiquitousitemkey.md) attribute and any attribute whose name starts with `ubiquitousItem` or `ubiquitousSharedItem` (or `NSURLUbiquitousItem` or `NSURLUbiquitousSharedItem` in Objective-C).

If the property is not implemented, the system generates notifications for all the ubiquity attributes.

The system checks this property only when the file coordinator’s [+ addFilePresenter:](<../nsfilecoordinator/addfilepresenter(__).md>) method is called. Make all changes to this property before calling [+ addFilePresenter:](<../nsfilecoordinator/addfilepresenter(__).md>).

## See Also

### Ubiquity Change Notifications

- [- presentedItemDidChangeUbiquityAttributes:](<presenteditemdidchangeubiquityattributes(__).md>) — Tells your object that the file or file package’s ubiquity attributes have changed.
