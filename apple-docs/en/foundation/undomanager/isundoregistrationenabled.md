---
title: isUndoRegistrationEnabled
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/undomanager/isundoregistrationenabled
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/isundoregistrationenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/isundoregistrationenabled.json'
content_hash: 'sha256:6996b233726060e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UndoManager](../undomanager.md)

# isUndoRegistrationEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the recording of undo operations is enabled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isUndoRegistrationEnabled: Bool { get }
```

## Discussion

[true](../../swift/true.md) if registration is enabled; otherwise, [false](../../swift/false.md).

The default is [true](../../swift/true.md).

## See Also

### Enabling and disabling undo

- [- disableUndoRegistration](<disableundoregistration().md>) — Disables the recording of undo operations.
- [- enableUndoRegistration](<enableundoregistration().md>) — Enables the recording of undo operations.
