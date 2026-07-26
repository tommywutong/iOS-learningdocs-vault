---
title: 'init(forName:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/valuetransformer/init(forname:)'
source_url: 'https://developer.apple.com/documentation/foundation/valuetransformer/init(forname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/valuetransformer/init%28forname%3A%29.json'
content_hash: 'sha256:11cfd8e46fda8619'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ValueTransformer](../valuetransformer.md)

# init(forName:)

<sub>Initializer</sub>

Returns the value transformer identified by a given identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(forName name: NSValueTransformerName)
```

## Parameters

- `name` — The transformer identifier.

## Return Value

The value transformer identified by `name` in the shared registry, or `nil` if not found.

## Discussion

If `valueTransformerForName:` does not find a registered transformer instance for `name`, it will attempt to find a class with the specified name. If a corresponding class is found an instance will be created and initialized using its `init:` method and then automatically registered with `name`.

## See Also

### Using the Name-Based Registry

- [+ setValueTransformer:forName:](<setvaluetransformer(__forname_).md>) — Registers the provided value transformer with a given identifier.
- [+ valueTransformerNames](<valuetransformernames().md>) — Returns an array of all the registered value transformers.
- [NSValueTransformerName](../nsvaluetransformername.md) — Named value transformers defined by `NSValueTransformer`.
