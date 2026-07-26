---
title: 'CFNumberGetType(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnumbergettype(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumbergettype(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumbergettype%28_%3A%29.json'
content_hash: 'sha256:d735bc606d8a4202'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberGetType(_:)

<sub>Function</sub>

Returns the type used by a CFNumber object to store its value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNumberGetType(_ number: CFNumber!) -> CFNumberType
```

## Parameters

- `number` — The CFNumber object to examine.

## Return Value

A constant that indicates the data type of the value contained in `number`. See [CFNumberType](cfnumbertype.md) for a list of possible values.

## Discussion

The type specified in the call to [CFNumberCreate](<cfnumbercreate(______).md>) is not necessarily preserved when a new CFNumber object is created—it uses whatever internal storage type the creation function deems appropriate.

## See Also

### Getting Information About Numbers

- [CFNumberGetByteSize](<cfnumbergetbytesize(__).md>) — Returns the number of bytes used by a CFNumber object to store its value.
- [CFNumberGetValue](<cfnumbergetvalue(______).md>) — Obtains the value of a CFNumber object cast to a specified type.
- [CFNumberIsFloatType](<cfnumberisfloattype(__).md>) — Determines whether a CFNumber object contains a value stored as one of the defined floating point types.
