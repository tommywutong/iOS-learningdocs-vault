---
title: sortDescriptors
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/fetchrequest/configuration/sortdescriptors
source_url: 'https://developer.apple.com/documentation/swiftui/fetchrequest/configuration/sortdescriptors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fetchrequest/configuration/sortdescriptors.json'
content_hash: 'sha256:ea95a038ddebc139'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [FetchRequest](../../fetchrequest.md) · [Configuration](../configuration.md)

# sortDescriptors

<sub>Instance Property</sub>

The request’s sort descriptors, accessed as value types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var sortDescriptors: [SortDescriptor<Result>] { get set }
```

## Discussion

Set this configuration value to cause a [FetchRequest](../../fetchrequest.md) to execute a fetch with a new collection of [SortDescriptor](../../../foundation/sortdescriptor.md) instances. If you want to use [NSSortDescriptor](../../../foundation/nssortdescriptor.md) instances, set [nsSortDescriptors](nssortdescriptors.md) instead.

Access this value of a [Configuration](../configuration.md) structure for a given request by using the [sortDescriptors](../../fetchedresults/sortdescriptors.md) property on the associated [FetchedResults](../../fetchedresults.md) instance, either directly or through a [Binding](../../binding.md).

## See Also

### Setting sort descriptors

- [nsSortDescriptors](nssortdescriptors.md) — The request’s sort descriptors, accessed as reference types.
