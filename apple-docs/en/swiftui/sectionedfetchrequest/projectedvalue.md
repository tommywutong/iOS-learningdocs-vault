---
title: projectedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sectionedfetchrequest/projectedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/projectedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionedfetchrequest/projectedvalue.json'
content_hash: 'sha256:7a0d2da2fd822c77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SectionedFetchRequest](../sectionedfetchrequest.md)

# projectedValue

<sub>Instance Property</sub>

A binding to the request’s mutable configuration properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var projectedValue: Binding<SectionedFetchRequest<SectionIdentifier, Result>.Configuration> { get }
```

## Discussion

This property behaves like the [projectedValue](../fetchrequest/projectedvalue.md) of a [FetchRequest](../fetchrequest.md). In particular, SwiftUI returns the value associated with this property when you use [SectionedFetchRequest](../sectionedfetchrequest.md) as a property wrapper on a [SectionedFetchResults](../sectionedfetchresults.md) instance and then access the results with a dollar sign (`$`) prefix. The value that SwiftUI returns is a [Binding](../binding.md) to the request’s [Configuration](configuration.md) structure, which dynamically configures the request.

## See Also

### Configuring a request dynamically

- [Configuration](configuration.md) — The request’s configurable properties.
