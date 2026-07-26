---
title: 'init(contentsOf:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifiltergenerator/init(contentsof:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltergenerator/init(contentsof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltergenerator/init%28contentsof%3A%29.json'
content_hash: 'sha256:9c574adabd971154'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilterGenerator](../cifiltergenerator.md)

# init(contentsOf:)

<sub>Initializer</sub>

Initializes a filter generator object with the contents of a filter generator file.

<sub>macOS</sub>

```swift
init?(contentsOf aURL: URL)
```

## Parameters

- `aURL` — The location of a filter generator file.

## Return Value

The initialized [CIFilterGenerator](../cifiltergenerator.md) object. Returns `nil` if the file can’t be read.
