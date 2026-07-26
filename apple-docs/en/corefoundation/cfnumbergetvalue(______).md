---
title: 'CFNumberGetValue(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnumbergetvalue(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumbergetvalue(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumbergetvalue%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:b43d3c771ca16824'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberGetValue(_:_:_:)

<sub>Function</sub>

Obtains the value of a CFNumber object cast to a specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNumberGetValue(_ number: CFNumber!, _ theType: CFNumberType, _ valuePtr: UnsafeMutableRawPointer!) -> Bool
```

## Parameters

- `number` — The CFNumber object to examine.

- `theType` — A constant that specifies the data type to return. See [CFNumberType](cfnumbertype.md) for a list of possible values.

- `valuePtr` — On return, contains the value of `number`.

## Return Value

`true` if the operation was successful, otherwise `false`.

## Discussion

If the argument type differs from the return type, and the conversion is lossy or the return value is out of range, then this function passes back an approximate value in `valuePtr` and returns `false`.

## See Also

### Getting Information About Numbers

- [CFNumberGetByteSize](<cfnumbergetbytesize(__).md>) — Returns the number of bytes used by a CFNumber object to store its value.
- [CFNumberGetType](<cfnumbergettype(__).md>) — Returns the type used by a CFNumber object to store its value.
- [CFNumberIsFloatType](<cfnumberisfloattype(__).md>) — Determines whether a CFNumber object contains a value stored as one of the defined floating point types.
