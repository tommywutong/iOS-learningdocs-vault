---
title: 'CFHash(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfhash(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfhash(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfhash%28_%3A%29.json'
content_hash: 'sha256:bce91ef951c75ed4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFHash(_:)

<sub>Function</sub>

Returns a code that can be used to identify an object in a hashing structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFHash(_ cf: CFTypeRef!) -> CFHashCode
```

## Parameters

- `cf` — A CFType object to examine.

## Return Value

An integer of type [CFHashCode](cfhashcode.md) that represents a hashing value for `cf`.

## Discussion

Two objects that are equal (as determined by the [CFEqual](<cfequal(____).md>) function) have the same hashing value. However, the converse is not true: two objects with the same hashing value might not be equal. That is, hashing values are not necessarily unique.

The hashing value for an object might change from release to release or from platform to platform.
