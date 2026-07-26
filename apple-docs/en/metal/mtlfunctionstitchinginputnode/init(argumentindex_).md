---
title: 'init(argumentIndex:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlfunctionstitchinginputnode/init(argumentindex:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionstitchinginputnode/init(argumentindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionstitchinginputnode/init%28argumentindex%3A%29.json'
content_hash: 'sha256:3b30cdaffdaeb0cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionStitchingInputNode](../mtlfunctionstitchinginputnode.md)

# init(argumentIndex:)

<sub>Initializer</sub>

Creates a new input node.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(argumentIndex argument: Int)
```

## Parameters

- `argument` — The index of the parameter in the  stitched function’s parameter list. The first parameter is `0`, the second is `1`, and so on.
