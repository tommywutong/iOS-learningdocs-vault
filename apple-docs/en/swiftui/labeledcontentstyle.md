---
title: LabeledContentStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/labeledcontentstyle
source_url: 'https://developer.apple.com/documentation/swiftui/labeledcontentstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/labeledcontentstyle.json'
content_hash: 'sha256:30a5ea28b1dc3d10'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# LabeledContentStyle

<sub>Protocol</sub>

The appearance and behavior of a labeled content instance..

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol LabeledContentStyle
```

## Overview

Use [labeledContentStyle(_:)](<view/labeledcontentstyle(__).md>) to set a style on a view.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Relationships

- **Conforming Types**: [AutomaticLabeledContentStyle](automaticlabeledcontentstyle.md)

## Topics

### Getting built-in labeled content styles

- [automatic](labeledcontentstyle/automatic.md) — A labeled content style that resolves its appearance automatically based on the current context.

### Creating custom labeled content styles

- [makeBody(configuration:)](<labeledcontentstyle/makebody(configuration_).md>) — Creates a view that represents the body of labeled content.
- [Configuration](labeledcontentstyle/configuration.md) — The properties of a labeled content instance.
- [Body](labeledcontentstyle/body.md) — A view that represents the appearance and behavior of labeled content.

### Supporting types

- [AutomaticLabeledContentStyle](automaticlabeledcontentstyle.md) — The default labeled content style.

## See Also

### Styling groups

- [controlGroupStyle(_:)](<view/controlgroupstyle(__).md>) — Sets the style for control groups within this view.
- [ControlGroupStyle](controlgroupstyle.md) — Defines the implementation of all control groups within a view hierarchy.
- [ControlGroupStyleConfiguration](controlgroupstyleconfiguration.md) — The properties of a control group.
- [formStyle(_:)](<view/formstyle(__).md>) — Sets the style for forms in a view hierarchy.
- [FormStyle](formstyle.md) — The appearance and behavior of a form.
- [FormStyleConfiguration](formstyleconfiguration.md) — The properties of a form instance.
- [groupBoxStyle(_:)](<view/groupboxstyle(__).md>) — Sets the style for group boxes within this view.
- [GroupBoxStyle](groupboxstyle.md) — A type that specifies the appearance and interaction of all group boxes within a view hierarchy.
- [GroupBoxStyleConfiguration](groupboxstyleconfiguration.md) — The properties of a group box instance.
- [indexViewStyle(_:)](<view/indexviewstyle(__).md>) — Sets the style for the index view within the current environment.
- [IndexViewStyle](indexviewstyle.md) — Defines the implementation of all `IndexView` instances within a view hierarchy.
- [labeledContentStyle(_:)](<view/labeledcontentstyle(__).md>) — Sets a style for labeled content.
- [LabeledContentStyleConfiguration](labeledcontentstyleconfiguration.md) — The properties of a labeled content instance.
