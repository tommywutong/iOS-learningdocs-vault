---
title: 'init(_:comparing:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/sortdescriptor/init(_:comparing:)'
source_url: 'https://developer.apple.com/documentation/foundation/sortdescriptor/init(_:comparing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/sortdescriptor/init%28_%3Acomparing%3A%29.json'
content_hash: 'sha256:11304785adcc2a4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [SortDescriptor](../sortdescriptor.md)

# init(_:comparing:)

<sub>Initializer</sub>

Creates a sort descriptor using a sort descriptor and a type that you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ descriptor: NSSortDescriptor, comparing comparedType: Compared.Type) where Compared : NSObject
```

## Parameters

- `descriptor` — A sort descriptor.

- `comparedType` — The type that the sort descriptor compares.

## Discussion

Returns `nil` if there isn’t a [SortDescriptor](../sortdescriptor.md) equivalent to the [NSSortDescriptor](../nssortdescriptor.md) you specify, or if the selector to [NSSortDescriptor](../nssortdescriptor.md) isn’t one of the standard string comparison algorithms or `compare(_:)`.

The comparison for the created [SortDescriptor](../sortdescriptor.md) uses the selector to the associated [NSSortDescriptor](../nssortdescriptor.md) directly, so in cases where the comparison of [NSSortDescriptor](../nssortdescriptor.md) might crash, the [SortDescriptor](../sortdescriptor.md) comparison crashes as well.
