---
title: 'executeAndReturnError(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsapplescript/executeandreturnerror(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsapplescript/executeandreturnerror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsapplescript/executeandreturnerror%28_%3A%29.json'
content_hash: 'sha256:7134c1764483109e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleScript](../nsapplescript.md)

# executeAndReturnError(_:)

<sub>Instance Method</sub>

Executes the receiver, compiling it first if it is not already compiled.

<sub>Mac Catalyst, macOS</sub>

```swift
func executeAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor
```

## Parameters

- `errorInfo` — On return, if an error occurs, a pointer to an error information dictionary.

## Return Value

The result of executing the event, or `nil` if an error occurs.

## Discussion

Any changes to property values caused by executing the script do not persist.

## See Also

### Compiling and Executing a Script

- [- compileAndReturnError:](<compileandreturnerror(__).md>) — Compiles the receiver, if it is not already compiled.
- [- executeAppleEvent:error:](<executeappleevent(__error_).md>) — Executes an Apple event in the context of the receiver, as a means of allowing the application to invoke a handler in the script.
