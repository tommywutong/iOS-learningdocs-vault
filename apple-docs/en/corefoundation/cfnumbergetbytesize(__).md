---
title: 'CFNumberGetByteSize(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnumbergetbytesize(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumbergetbytesize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumbergetbytesize%28_%3A%29.json'
content_hash: 'sha256:3e10d4ebf7639d20'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberGetByteSize(_:)

<sub>Function</sub>

Returns the number of bytes used by a CFNumber object to store its value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNumberGetByteSize(_ number: CFNumber!) -> CFIndex
```

## Parameters

- `number` — The CFNumber object to examine.

## Return Value

The size in bytes of the value contained in `number`.

## Discussion

Because a CFNumber object might store a value using a type different from that of the original value with which it was created, this function may return a size different from the size of the original value’s type.

## See Also

### Getting Information About Numbers

- [CFNumberGetType](<cfnumbergettype(__).md>) — Returns the type used by a CFNumber object to store its value.
- [CFNumberGetValue](<cfnumbergetvalue(______).md>) — Obtains the value of a CFNumber object cast to a specified type.
- [CFNumberIsFloatType](<cfnumberisfloattype(__).md>) — Determines whether a CFNumber object contains a value stored as one of the defined floating point types.
