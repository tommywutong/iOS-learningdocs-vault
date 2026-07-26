---
title: 'setFunctions(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlvisiblefunctiontable/setfunctions(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlvisiblefunctiontable/setfunctions(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvisiblefunctiontable/setfunctions%28_%3Arange%3A%29.json'
content_hash: 'sha256:61fe9d99715afe4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVisibleFunctionTable](../mtlvisiblefunctiontable.md)

# setFunctions(_:range:)

<sub>Instance Method</sub>

Sets a range of table entries to point to an array of callable functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setFunctions(_ functions: [(any MTLFunctionHandle)?], range: Range<Int>)
```

## Parameters

- `functions` — An array of function handles for the functions to be called.

- `range` — A range of indices to change in the table.

## See Also

### Setting a table entry

- [- setFunction:atIndex:](<setfunction(__index_).md>) — Sets a table entry to point to a callable function.
