---
title: DropOperation.Set
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dropoperation/set
source_url: 'https://developer.apple.com/documentation/swiftui/dropoperation/set'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropoperation/set.json'
content_hash: 'sha256:86e2e2c748a0bf38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DropOperation](../dropoperation.md)

# DropOperation.Set

<sub>Structure</sub>

A set of drop operations, corresponding to matching cases in `DropOperation`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct Set
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [Hashable](../../swift/hashable.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<set/init(rawvalue_).md>) — Creates a set of drop operations using the provided raw value.

### Type Properties

- [alias](set/alias.md)
- [cancel](set/cancel.md) — Cancel the operation.
- [copy](set/copy.md) — Copy the data to the modified view.
- [delete](set/delete.md) — Delete the data.
- [forbidden](set/forbidden.md) — The operation is forbidden.
- [move](set/move.md) — Move the data represented by the drag items instead of copying it.
