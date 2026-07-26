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
doc_path: /documentation/swiftui/sectionedfetchrequest/configuration/nspredicate
source_url: 'https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/configuration/nspredicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionedfetchrequest/configuration/nspredicate.json'
content_hash: 'sha256:d9e1054a2eb21e41'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SectionedFetchRequest](../../sectionedfetchrequest.md) · [Configuration](../configuration.md)

# nsPredicate

<sub>Instance Property</sub>

The request’s predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nsPredicate: NSPredicate?
```

## Discussion

Set this configuration value to cause a [SectionedFetchRequest](../../sectionedfetchrequest.md) to execute a fetch with a new predicate.

Access this value for a given request by using the [nsPredicate](../../sectionedfetchresults/nspredicate.md) property on the associated [SectionedFetchResults](../../sectionedfetchresults.md) instance, either directly or with a [Binding](../../binding.md).
