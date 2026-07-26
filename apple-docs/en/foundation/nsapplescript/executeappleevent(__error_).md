---
title: 'executeAppleEvent(_:error:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsapplescript/executeappleevent(_:error:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsapplescript/executeappleevent(_:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsapplescript/executeappleevent%28_%3Aerror%3A%29.json'
content_hash: 'sha256:9ed4f5e0fe98bdc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleScript](../nsapplescript.md)

# executeAppleEvent(_:error:)

<sub>Instance Method</sub>

Executes an Apple event in the context of the receiver, as a means of allowing the application to invoke a handler in the script.

<sub>Mac Catalyst, macOS</sub>

```swift
func executeAppleEvent(_ event: NSAppleEventDescriptor, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor
```

## Parameters

- `event` — The Apple event to execute.

- `errorInfo` — On return, if an error occurs, a pointer to an error information dictionary.

## Return Value

The result of executing the event, or `nil` if an error occurs.

## Discussion

Compiles the receiver before executing it if it is not already compiled.

> [!important] Important
> You cannot use this method to send Apple events to other applications.

## See Also

### Compiling and Executing a Script

- [- compileAndReturnError:](<compileandreturnerror(__).md>) — Compiles the receiver, if it is not already compiled.
- [- executeAndReturnError:](<executeandreturnerror(__).md>) — Executes the receiver, compiling it first if it is not already compiled.
