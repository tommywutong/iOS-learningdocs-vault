---
title: 'setFunction(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlintersectionfunctiontable/setfunction(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setfunction(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlintersectionfunctiontable/setfunction%28_%3Aindex%3A%29.json'
content_hash: 'sha256:6ad6bd6fed24a30d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md)

# setFunction(_:index:)

<sub>Instance Method</sub>

Sets an entry in the table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setFunction(_ function: (any MTLFunctionHandle)?, index: Int)
```

## Parameters

- `function` — A function handle for the intersection function.

- `index` — The index of the table entry to change.

## See Also

### Setting a table entry

- [setFunctions(_:range:)](<setfunctions(__range_).md>) — Sets a range of entries in the table.
