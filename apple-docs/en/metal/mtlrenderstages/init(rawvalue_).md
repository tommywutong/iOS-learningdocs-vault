---
title: 'init(rawValue:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrenderstages/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderstages/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderstages/init%28rawvalue%3A%29.json'
content_hash: 'sha256:cc99cd01a798b00a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderStages](../mtlrenderstages.md)

# init(rawValue:)

<sub>Initializer</sub>

Creates a render stage from a raw value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(rawValue: UInt)
```

## Parameters

- `rawValue` — A bit field value of a render stage as an integer.

## Discussion

Use of the [MTLRenderStages](../mtlrenderstages.md) type’s static properties, such as [MTLRenderStageMesh](mesh.md), [MTLRenderStageVertex](vertex.md), or [MTLRenderStageFragment](fragment.md) instead of creating a render stage instance yourself with this initializer.
