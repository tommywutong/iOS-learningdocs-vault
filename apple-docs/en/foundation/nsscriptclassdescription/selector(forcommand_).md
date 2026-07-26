---
title: 'selector(forCommand:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptclassdescription/selector(forcommand:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptclassdescription/selector(forcommand:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptclassdescription/selector%28forcommand%3A%29.json'
content_hash: 'sha256:29c05fc05c9e0015'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptClassDescription](../nsscriptclassdescription.md)

# selector(forCommand:)

<sub>Instance Method</sub>

Returns the selector associated with the receiver for the specified command description.

<sub>Mac Catalyst, macOS</sub>

```swift
func selector(forCommand commandDescription: NSScriptCommandDescription) -> Selector?
```

## Parameters

- `commandDescription` — A description for a script command, such as `duplicate`, `make`, or `move`. Encapsulates the scriptability information for that command, such as its Objective-C selector, its argument names and types, and its return type (if any).

## Return Value

The selector from the receiver for the command specified by `commandDescription`. Searches in the receiver first, then in any superclass. Returns `NULL` if no matching selector is found.

## See Also

### Getting command information

- [- supportsCommand:](<supportscommand(__).md>) — Returns a Boolean value indicating whether the receiver or any superclass supports the specified command.
