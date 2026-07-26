---
title: 'compileAndReturnError(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsapplescript/compileandreturnerror(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsapplescript/compileandreturnerror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsapplescript/compileandreturnerror%28_%3A%29.json'
content_hash: 'sha256:fa4c65988b07b6d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleScript](../nsapplescript.md)

# compileAndReturnError(_:)

<sub>Instance Method</sub>

Compiles the receiver, if it is not already compiled.

<sub>Mac Catalyst, macOS</sub>

```swift
func compileAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool
```

## Parameters

- `errorInfo` — On return, if an error occurs, a pointer to an error information dictionary.

## Return Value

[true](../../swift/true.md) for success or if the script was already compiled, [false](../../swift/false.md) otherwise.

## See Also

### Compiling and Executing a Script

- [- executeAndReturnError:](<executeandreturnerror(__).md>) — Executes the receiver, compiling it first if it is not already compiled.
- [- executeAppleEvent:error:](<executeappleevent(__error_).md>) — Executes an Apple event in the context of the receiver, as a means of allowing the application to invoke a handler in the script.
