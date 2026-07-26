---
title: nsPredicate
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/fetchrequest/configuration/nspredicate
source_url: 'https://developer.apple.com/documentation/swiftui/fetchrequest/configuration/nspredicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fetchrequest/configuration/nspredicate.json'
content_hash: 'sha256:8df94c6a7244e493'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [FetchRequest](../../fetchrequest.md) · [Configuration](../configuration.md)

# nsPredicate

<sub>Instance Property</sub>

The request’s predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var nsPredicate: NSPredicate?
```

## Discussion

Set this configuration value to cause a [FetchRequest](../../fetchrequest.md) to execute a fetch with a new predicate.

Access this value of a [Configuration](../configuration.md) structure for a given request by using the [nsPredicate](../../fetchedresults/nspredicate.md) property on the associated [FetchedResults](../../fetchedresults.md) instance, either directly or through a [Binding](../../binding.md).
