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
doc_path: /documentation/swiftui/fetchrequest/configuration/nssortdescriptors
source_url: 'https://developer.apple.com/documentation/swiftui/fetchrequest/configuration/nssortdescriptors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fetchrequest/configuration/nssortdescriptors.json'
content_hash: 'sha256:cd7a222995ada53c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [FetchRequest](../../fetchrequest.md) · [Configuration](../configuration.md)

# nsSortDescriptors

<sub>Instance Property</sub>

The request’s sort descriptors, accessed as reference types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var nsSortDescriptors: [NSSortDescriptor]
```

## Discussion

Set this configuration value to cause a [FetchRequest](../../fetchrequest.md) to execute a fetch with a new collection of [NSSortDescriptor](../../../foundation/nssortdescriptor.md) instances. If you want to use [SortDescriptor](../../../foundation/sortdescriptor.md) instances, set [sortDescriptors](sortdescriptors.md) instead.

Access this value of a [Configuration](../configuration.md) structure for a given request by using the [nsSortDescriptors](../../fetchedresults/nssortdescriptors.md) property on the associated [FetchedResults](../../fetchedresults.md) instance, either directly or through a [Binding](../../binding.md).

## See Also

### Setting sort descriptors

- [sortDescriptors](sortdescriptors.md) — The request’s sort descriptors, accessed as value types.
