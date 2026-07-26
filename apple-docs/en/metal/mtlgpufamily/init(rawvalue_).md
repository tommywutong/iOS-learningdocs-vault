---
title: 'init(rawValue:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlgpufamily/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlgpufamily/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlgpufamily/init%28rawvalue%3A%29.json'
content_hash: 'sha256:ad33059f1e86f7b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLGPUFamily](../mtlgpufamily.md)

# init(rawValue:)

<sub>Initializer</sub>

Creates a GPU family instance from a raw value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(rawValue: Int)
```

## Parameters

- `rawValue` — An integer value that represents a GPU family.

## Discussion

You don’t need to call this initializer because it’s part of how Swift represents an enumeration from an Objective-C framework.

> [!tip] Tip
> Use one of the [MTLGPUFamily](../mtlgpufamily.md) cases, such as [MTLGPUFamilyMetal3](metal3.md), instead of this initializer.
