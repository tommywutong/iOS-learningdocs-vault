---
title: enableUndoRegistration()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/enableundoregistration()
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/enableundoregistration()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/enableundoregistration%28%29.json'
content_hash: 'sha256:02291b446ece3e34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# enableUndoRegistration()

<sub>Instance Method</sub>

Enables the recording of undo operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enableUndoRegistration()
```

## Discussion

Because undo registration is enabled by default, it is often used to balance a prior [- disableUndoRegistration](<disableundoregistration().md>) message. Undo registration isn’t actually re-enabled until an enable message balances the last disable message in effect. Raises an `NSInternalInconsistencyException` if invoked while no [- disableUndoRegistration](<disableundoregistration().md>) message is in effect.

## See Also

### Enabling and disabling undo

- [- disableUndoRegistration](<disableundoregistration().md>) — Disables the recording of undo operations.
- [undoRegistrationEnabled](isundoregistrationenabled.md) — A Boolean value that indicates whether the recording of undo operations is enabled.
