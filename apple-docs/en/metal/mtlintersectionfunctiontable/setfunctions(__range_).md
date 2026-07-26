---
title: 'setFunctions(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlintersectionfunctiontable/setfunctions(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setfunctions(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlintersectionfunctiontable/setfunctions%28_%3Arange%3A%29.json'
content_hash: 'sha256:d1b05d28161cb987'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md)

# setFunctions(_:range:)

<sub>Instance Method</sub>

Sets a range of entries in the table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setFunctions(_ functions: [(any MTLFunctionHandle)?], range: Range<Int>)
```

## Parameters

- `functions` — The new entries for the table.

- `range` — A range of indices to change in the table.

## See Also

### Setting a table entry

- [- setFunction:atIndex:](<setfunction(__index_).md>) — Sets an entry in the table.
