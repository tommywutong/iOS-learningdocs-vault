---
title: nsSortDescriptors
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sectionedfetchrequest/configuration/nssortdescriptors
source_url: 'https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/configuration/nssortdescriptors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionedfetchrequest/configuration/nssortdescriptors.json'
content_hash: 'sha256:73dbf3d584ff4cc3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SectionedFetchRequest](../../sectionedfetchrequest.md) · [Configuration](../configuration.md)

# nsSortDescriptors

<sub>Instance Property</sub>

The request’s sort descriptors, accessed as reference types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nsSortDescriptors: [NSSortDescriptor]
```

## Discussion

Set this configuration value to cause a [SectionedFetchRequest](../../sectionedfetchrequest.md) to execute a fetch with a new collection of [NSSortDescriptor](../../../foundation/nssortdescriptor.md) instances. If you want to use [SortDescriptor](../../../foundation/sortdescriptor.md) instances, set [sortDescriptors](sortdescriptors.md) instead. Use care to coordinate section and sort updates, as described in [Configuration](../configuration.md).

Access this value for a given request by using the [nsSortDescriptors](../../sectionedfetchresults/nssortdescriptors.md) property on the associated [SectionedFetchResults](../../sectionedfetchresults.md) instance, either directly or with a [Binding](../../binding.md).

## See Also

### Setting sort descriptors

- [sortDescriptors](sortdescriptors.md) — The request’s sort descriptors, accessed as value types.
