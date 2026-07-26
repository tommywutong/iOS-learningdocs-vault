---
title: KeyPress.Phases
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/keypress/phases
source_url: 'https://developer.apple.com/documentation/swiftui/keypress/phases'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keypress/phases.json'
content_hash: 'sha256:bfaaf0e26812de32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [KeyPress](../keypress.md)

# KeyPress.Phases

<sub>Structure</sub>

Options for matching different phases of a key-press event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct Phases
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Getting the phases

- [down](phases/down.md) — The user pressed down on a key.
- [up](phases/up.md) — The user released a key.
- [repeat](phases/repeat.md) — The user held a key down to issue a sequence of repeating events.
- [all](phases/all.md) — A value that matches all key press phases.

## See Also

### Getting the phase of the keypress

- [phase](phase.md) — The phase of the key-press event (`.down`, `.repeat`, or `.up`).
