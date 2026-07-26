---
title: containerValues
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sectionconfiguration/containervalues
source_url: 'https://developer.apple.com/documentation/swiftui/sectionconfiguration/containervalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionconfiguration/containervalues.json'
content_hash: 'sha256:b8c1962bae82d8a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SectionConfiguration](../sectionconfiguration.md)

# containerValues

<sub>Instance Property</sub>

The container values associated with the given section.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var containerValues: ContainerValues { get }
```

## Discussion

Only explicitly created sections are able to have container values, meaning this container values will be empty if the section is implicit.
