---
title: 'CFNumberIsFloatType(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnumberisfloattype(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumberisfloattype(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumberisfloattype%28_%3A%29.json'
content_hash: 'sha256:ba067d1e32b4d715'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberIsFloatType(_:)

<sub>Function</sub>

Determines whether a CFNumber object contains a value stored as one of the defined floating point types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNumberIsFloatType(_ number: CFNumber!) -> Bool
```

## Parameters

- `number` — The CFNumber object to examine.

## Return Value

`true` if `number`’s value is one of the defined floating point types, otherwise `false`. The valid floating point types are listed in [CFNumberType](cfnumbertype.md).

## See Also

### Getting Information About Numbers

- [CFNumberGetByteSize](<cfnumbergetbytesize(__).md>) — Returns the number of bytes used by a CFNumber object to store its value.
- [CFNumberGetType](<cfnumbergettype(__).md>) — Returns the type used by a CFNumber object to store its value.
- [CFNumberGetValue](<cfnumbergetvalue(______).md>) — Obtains the value of a CFNumber object cast to a specified type.
