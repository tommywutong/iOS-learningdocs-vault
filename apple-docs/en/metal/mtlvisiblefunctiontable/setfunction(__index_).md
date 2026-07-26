---
title: 'setFunction(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlvisiblefunctiontable/setfunction(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlvisiblefunctiontable/setfunction(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvisiblefunctiontable/setfunction%28_%3Aindex%3A%29.json'
content_hash: 'sha256:2be930b3dc94d152'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVisibleFunctionTable](../mtlvisiblefunctiontable.md)

# setFunction(_:index:)

<sub>Instance Method</sub>

Sets a table entry to point to a callable function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setFunction(_ function: (any MTLFunctionHandle)?, index: Int)
```

## Parameters

- `function` — A function handle for the function to be called.

- `index` — The index of the table entry to change.

## See Also

### Setting a table entry

- [setFunctions(_:range:)](<setfunctions(__range_).md>) — Sets a range of table entries to point to an array of callable functions.
