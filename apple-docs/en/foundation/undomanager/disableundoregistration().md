---
title: disableUndoRegistration()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/disableundoregistration()
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/disableundoregistration()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/disableundoregistration%28%29.json'
content_hash: 'sha256:f1e14a159d83c6be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# disableUndoRegistration()

<sub>Instance Method</sub>

Disables the recording of undo operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func disableUndoRegistration()
```

## Discussion

This method disables undos recorded by [- registerUndoWithTarget:selector:object:](<registerundo(withtarget_selector_object_).md>) or invocation-based undo.

This method can be invoked multiple times by multiple clients. The [- enableUndoRegistration](<enableundoregistration().md>) method must be invoked an equal number of times to re-enable undo registration.

## See Also

### Enabling and disabling undo

- [- enableUndoRegistration](<enableundoregistration().md>) — Enables the recording of undo operations.
- [undoRegistrationEnabled](isundoregistrationenabled.md) — A Boolean value that indicates whether the recording of undo operations is enabled.
