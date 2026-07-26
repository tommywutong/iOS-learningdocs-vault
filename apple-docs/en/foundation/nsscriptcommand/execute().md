---
title: execute()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommand/execute()
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommand/execute()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommand/execute%28%29.json'
content_hash: 'sha256:b062db3319c83ef9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommand](../nsscriptcommand.md)

# execute()

<sub>Instance Method</sub>

Executes the command if it is valid and returns the result, if any.

<sub>Mac Catalyst, macOS</sub>

```swift
func execute() -> Any?
```

## Discussion

Before this method executes the command (through `NSInvocation` mechanisms), it evaluates all object specifiers involved in the command, validates that the receivers can actually handle the command, and verifies that the types of any arguments that were initially object specifiers are valid.

You shouldn’t have to override this method. If the command’s receivers want to handle the command themselves, this method invokes their defined handler. Otherwise, it invokes [- performDefaultImplementation](<performdefaultimplementation().md>).

## See Also

### Related Documentation

- [evaluatedReceivers](evaluatedreceivers.md) — Returns the object or objects to which the command is to be sent (called both the “receivers” or “targets” of script commands).
- [evaluatedArguments](evaluatedarguments.md) — Returns a dictionary containing the arguments of the command, evaluated from object specifiers to objects if necessary. The keys in the dictionary are the argument names.

### Executing the command

- [- performDefaultImplementation](<performdefaultimplementation().md>) — Overridden by subclasses to provide a default implementation for the command represented by the receiver.
