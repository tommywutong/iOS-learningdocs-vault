---
title: sectionIdentifier
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sectionedfetchrequest/configuration/sectionidentifier
source_url: 'https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/configuration/sectionidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionedfetchrequest/configuration/sectionidentifier.json'
content_hash: 'sha256:e76691ea4d285a5c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SectionedFetchRequest](../../sectionedfetchrequest.md) · [Configuration](../configuration.md)

# sectionIdentifier

<sub>Instance Property</sub>

The request’s section identifier key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sectionIdentifier: KeyPath<Result, SectionIdentifier>
```

## Discussion

Set this configuration value to cause a [SectionedFetchRequest](../../sectionedfetchrequest.md) to execute a fetch with a new section identifier. You can’t change the section identifier type without creating a new fetch request. Use care to coordinate section and sort updates, as described in [Configuration](../configuration.md).

Access this value for a given request by using the [sectionIdentifier](../../sectionedfetchresults/sectionidentifier.md) property on the associated [SectionedFetchResults](../../sectionedfetchresults.md) instance, either directly or with a [Binding](../../binding.md).
