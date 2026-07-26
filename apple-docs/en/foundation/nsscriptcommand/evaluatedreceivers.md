---
title: evaluatedReceivers
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommand/evaluatedreceivers
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommand/evaluatedreceivers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommand/evaluatedreceivers.json'
content_hash: 'sha256:100ea9aa3ca57e18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommand](../nsscriptcommand.md)

# evaluatedReceivers

<sub>Instance Property</sub>

Returns the object or objects to which the command is to be sent (called both the “receivers” or “targets” of script commands).

<sub>Mac Catalyst, macOS</sub>

```swift
var evaluatedReceivers: Any? { get }
```

## Discussion

It evaluates receivers, which are always object specifiers, to a proper object. If the command does not specify a receiver, or if the receiver doesn’t accept the command, it returns `nil`.

## See Also

### Accessing receivers

- [receiversSpecifier](receiversspecifier.md) — Sets the object specifier to `receiversSpec` that, when evaluated, indicates the receiver or receivers of the command.
