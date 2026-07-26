---
title: CFTypeID
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cftypeid
source_url: 'https://developer.apple.com/documentation/corefoundation/cftypeid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftypeid.json'
content_hash: 'sha256:d69691ac8412f1b0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTypeID

<sub>Type Alias</sub>

A type for unique, constant integer values that identify particular Core Foundation opaque types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFTypeID = UInt
```

## Discussion

Defines a type identifier in Core Foundation. A type ID is an integer that identifies the opaque type to which a Core Foundation object “belongs.” You use type IDs in various contexts, such as when you are operating on heterogeneous collections. Core Foundation provides programmatic interfaces for obtaining and evaluating type IDs.

Because the value for a type ID can change from release to release, your code should not rely on stored or hard-coded type IDs nor should it hard-code any observed properties of a type ID (such as, for example, it being a small integer).

## See Also

### Data Types

- [CFHashCode](cfhashcode.md) — A type for hash codes returned by the `CFHash` function.
