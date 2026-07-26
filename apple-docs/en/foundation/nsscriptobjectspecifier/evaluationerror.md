---
title: evaluationError
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptobjectspecifier/evaluationerror
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/evaluationerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptobjectspecifier/evaluationerror.json'
content_hash: 'sha256:c56e371c4152d4d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptObjectSpecifier](../nsscriptobjectspecifier.md)

# evaluationError

<sub>Instance Property</sub>

Returns the object specifier in which an evaluation error occurred.

<sub>Mac Catalyst, macOS</sub>

```swift
var evaluationError: NSScriptObjectSpecifier? { get }
```

## Return Value

The object specifier in which an evaluation error occurred.

## Discussion

The object specifier failing to evaluate could be the receiver or any container specifier “above” the receiver.

## See Also

### Getting evaluation errors

- [evaluationErrorNumber](evaluationerrornumber.md) — Sets the value of the evaluation error.
