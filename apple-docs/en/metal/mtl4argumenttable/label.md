---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4argumenttable/label
source_url: 'https://developer.apple.com/documentation/metal/mtl4argumenttable/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4argumenttable/label.json'
content_hash: 'sha256:5687bbfb64327308'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ArgumentTable](../mtl4argumenttable.md)

# label

<sub>Instance Property</sub>

Assigns an optional label with this argument table for debugging purposes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get }
```

## Discussion

You set this label by setting property [label](../mtl4argumenttabledescriptor/label.md) on the descriptor object, prior to creating this table instance.
