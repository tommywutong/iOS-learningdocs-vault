---
title: AutomaticProductPlaceholderIcon
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/automaticproductplaceholdericon
source_url: 'https://developer.apple.com/documentation/storekit/automaticproductplaceholdericon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/automaticproductplaceholdericon.json'
content_hash: 'sha256:b73ffed5524b1ddb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# AutomaticProductPlaceholderIcon

<sub>Structure</sub>

A view that represents the default placeholder icon for an in-app store product.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct AutomaticProductPlaceholderIcon
```

## Overview

You don’t use this type directly. Instead, create a [ProductView](productview.md) or [StoreView](storeview.md) and provide product identifiers without a custom placeholder icon.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)
