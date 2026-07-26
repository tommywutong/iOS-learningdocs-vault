---
title: DefaultFocusEvaluationPriority
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/defaultfocusevaluationpriority
source_url: 'https://developer.apple.com/documentation/swiftui/defaultfocusevaluationpriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/defaultfocusevaluationpriority.json'
content_hash: 'sha256:ad35f8e54ed0a3a8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DefaultFocusEvaluationPriority

<sub>Structure</sub>

Prioritizations for default focus preferences when evaluating where to move focus in different circumstances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DefaultFocusEvaluationPriority
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the priorities

- [automatic](defaultfocusevaluationpriority/automatic.md) — Use the default focus preference when focus moves into the affected branch automatically, but ignore it when the movement is driven by a user-initiated navigation command.
- [userInitiated](defaultfocusevaluationpriority/userinitiated.md) — Always use the default focus preference when focus moves into the affected branch.

## See Also

### Controlling default focus

- [prefersDefaultFocus(_:in:)](<view/prefersdefaultfocus(__in_).md>) — Indicates that the view should receive focus by default for a given namespace.
- [defaultFocus(_:_:priority:)](<view/defaultfocus(____priority_).md>) — Defines a region of the window in which default focus is evaluated by assigning a value to a given focus state binding.
