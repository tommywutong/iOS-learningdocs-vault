---
title: 'sortedArray(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/sortedarray(using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/sortedarray(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/sortedarray%28using%3A%29.json'
content_hash: 'sha256:651bb510e10168f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# sortedArray(using:)

<sub>Instance Method</sub>

Returns an array of the set’s content sorted as specified by a given array of sort descriptors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sortedArray(using sortDescriptors: [NSSortDescriptor]) -> [Any]
```

## Parameters

- `sortDescriptors` — An array of [NSSortDescriptor](../nssortdescriptor.md) objects.

## Return Value

An NSArray containing the set’s content sorted as specified by `sortDescriptors`.

## Discussion

The first descriptor specifies the primary key path to be used in sorting the set’s contents. Any subsequent descriptors are used to further refine sorting of objects with duplicate values. See [NSSortDescriptor](../nssortdescriptor.md) for additional information.
