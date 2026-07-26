---
title: directParameter
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommand/directparameter
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommand/directparameter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommand/directparameter.json'
content_hash: 'sha256:d8dc8d38bbd4e01a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommand](../nsscriptcommand.md)

# directParameter

<sub>Instance Property</sub>

Sets the object that corresponds to the direct parameter of the Apple event from which the receiver derives.

<sub>Mac Catalyst, macOS</sub>

```swift
var directParameter: Any? { get set }
```

## Parameters

- `directParameter` — An object to be set as the direct parameter.

## Discussion

You don’t normally override this method.
