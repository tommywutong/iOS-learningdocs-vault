---
title: performDefaultImplementation()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommand/performdefaultimplementation()
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommand/performdefaultimplementation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommand/performdefaultimplementation%28%29.json'
content_hash: 'sha256:7568a747bd0fe05b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommand](../nsscriptcommand.md)

# performDefaultImplementation()

<sub>Instance Method</sub>

Overridden by subclasses to provide a default implementation for the command represented by the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
func performDefaultImplementation() -> Any?
```

## Discussion

Do not invoke this method directly. [- executeCommand](<execute().md>) invokes this method when the command being executed is not supported by the class of the objects receiving the command. The default implementation returns `nil`.

You need to create a subclass of `NSScriptCommand` only if you need to provide a default implementation of a command.

## See Also

### Executing the command

- [- executeCommand](<execute().md>) — Executes the command if it is valid and returns the result, if any.
