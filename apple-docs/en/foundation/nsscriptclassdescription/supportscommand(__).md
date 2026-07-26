---
title: 'supportsCommand(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptclassdescription/supportscommand(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptclassdescription/supportscommand(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptclassdescription/supportscommand%28_%3A%29.json'
content_hash: 'sha256:77ec04c01eea06a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptClassDescription](../nsscriptclassdescription.md)

# supportsCommand(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the receiver or any superclass supports the specified command.

<sub>Mac Catalyst, macOS</sub>

```swift
func supportsCommand(_ commandDescription: NSScriptCommandDescription) -> Bool
```

## Parameters

- `commandDescription` — A description for a script command, such as `duplicate`, `make`, or `move`. Encapsulates the scriptability information for that command, such as its Objective-C selector, its argument names and types, and its return type (if any).

## Return Value

[true](../../swift/true.md) if an the receiver or the instance of `NSScriptClassDescription` of any superclass of the receiver’s class lists the command described by `commandDesc` among its supported commands; otherwise, [false](../../swift/false.md).

## See Also

### Getting command information

- [- selectorForCommand:](<selector(forcommand_).md>) — Returns the selector associated with the receiver for the specified command description.
