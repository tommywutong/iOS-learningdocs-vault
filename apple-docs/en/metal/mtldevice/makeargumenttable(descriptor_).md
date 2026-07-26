---
title: 'makeArgumentTable(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makeargumenttable(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makeargumenttable(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makeargumenttable%28descriptor%3A%29.json'
content_hash: 'sha256:b6c54bbdfac909d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeArgumentTable(descriptor:)

<sub>Instance Method</sub>

Creates a new argument table from an argument table descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeArgumentTable(descriptor: MTL4ArgumentTableDescriptor) throws -> any MTL4ArgumentTable
```

## Parameters

- `descriptor` — A [MTL4ArgumentTableDescriptor](../mtl4argumenttabledescriptor.md) instance that configures the [MTL4ArgumentTable](../mtl4argumenttable.md) instance.

## Return Value

A [MTL4ArgumentTable](../mtl4argumenttable.md) instance, or `nil` if the function failed.
