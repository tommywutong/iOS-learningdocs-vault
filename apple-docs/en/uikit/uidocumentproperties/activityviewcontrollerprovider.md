---
title: activityViewControllerProvider
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentproperties/activityviewcontrollerprovider
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentproperties/activityviewcontrollerprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentproperties/activityviewcontrollerprovider.json'
content_hash: 'sha256:b6e8cf35498f89a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentProperties](../uidocumentproperties.md)

# activityViewControllerProvider

<sub>Instance Property</sub>

A closure that provides an activity view controller for sharing the document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var activityViewControllerProvider: (() -> UIActivityViewController)? { get set }
```

## Discussion

To support sharing, assign a closure that returns a [UIActivityViewController](../uiactivityviewcontroller.md) that you configure to share the document. When you set this property, a person can share the document by tapping the share button in the navigation item’s title menu.
