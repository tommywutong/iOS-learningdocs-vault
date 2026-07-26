---
title: 'CFXMLCreateStringByEscapingEntities(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfxmlcreatestringbyescapingentities(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlcreatestringbyescapingentities(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlcreatestringbyescapingentities%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:467a51e7176bbc22'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLCreateStringByEscapingEntities(_:_:_:)

<sub>Function</sub>

Given a CFString object containing XML source with unescaped entities, returns a string with specified XML entities escaped.

<sub>macOS</sub>

```swift
func CFXMLCreateStringByEscapingEntities(_ allocator: CFAllocator!, _ string: CFString!, _ entitiesDictionary: CFDictionary!) -> CFString!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `string` — Any CFString object that may contain XML source. This function translates any substring that is mapped to an entity in `entitiesDictionary` to the specified entity.

- `entitiesDictionary` — Specifies the entities to be replaced. Dictionary keys should be the entity names (for example, “para” for ¶), and the values should be CFString objects containing the expansion. Pass `NULL` to indicate no entities other than the standard five.

## Return Value

A CFString object derived from `string` with substrings identified in `entitiesDictionary` escaped to their corresponding entities. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The standard five predefined entities are automatically supported.

As an example of using this function, say you apply this function to string “Refer to ¶ 5 of the contract” with a key of “para” mapped to “¶” in `entitiesDictionary`. The resulting string is “Refer to ¶ 5 of the contract”.

> [!note] Note
> Currently, only the standard predefined entities are supported; passing `NULL` for `entitiesDictionary` is sufficient.

## See Also

### CFXMLTree Miscellaneous Functions

- [CFXMLCreateStringByUnescapingEntities](<cfxmlcreatestringbyunescapingentities(______).md>) — Given a CFString object containing XML source with escaped entities, returns a string with specified XML entities unescaped.
