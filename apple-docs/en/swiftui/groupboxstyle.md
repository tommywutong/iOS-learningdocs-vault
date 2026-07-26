---
title: GroupBoxStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/groupboxstyle
source_url: 'https://developer.apple.com/documentation/swiftui/groupboxstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/groupboxstyle.json'
content_hash: 'sha256:847f4daa9c1c4165'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# GroupBoxStyle

<sub>Protocol</sub>

A type that specifies the appearance and interaction of all group boxes within a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency protocol GroupBoxStyle
```

## Overview

To configure the current `GroupBoxStyle` for a view hierarchy, use the [groupBoxStyle(_:)](<view/groupboxstyle(__).md>) modifier.

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

- **Conforming Types**: [DefaultGroupBoxStyle](defaultgroupboxstyle.md)

## Topics

### Getting built-in group box styles

- [automatic](groupboxstyle/automatic.md) — The default style for group box views.

### Creating custom group box styles

- [makeBody(configuration:)](<groupboxstyle/makebody(configuration_).md>) — Creates a view representing the body of a group box.
- [Configuration](groupboxstyle/configuration.md) — The properties of a group box instance.
- [Body](groupboxstyle/body.md) — A view that represents the body of a group box.

### Supporting types

- [DefaultGroupBoxStyle](defaultgroupboxstyle.md) — The default style for group box views.

## See Also

### Styling groups

- [controlGroupStyle(_:)](<view/controlgroupstyle(__).md>) — Sets the style for control groups within this view.
- [ControlGroupStyle](controlgroupstyle.md) — Defines the implementation of all control groups within a view hierarchy.
- [ControlGroupStyleConfiguration](controlgroupstyleconfiguration.md) — The properties of a control group.
- [formStyle(_:)](<view/formstyle(__).md>) — Sets the style for forms in a view hierarchy.
- [FormStyle](formstyle.md) — The appearance and behavior of a form.
- [FormStyleConfiguration](formstyleconfiguration.md) — The properties of a form instance.
- [groupBoxStyle(_:)](<view/groupboxstyle(__).md>) — Sets the style for group boxes within this view.
- [GroupBoxStyleConfiguration](groupboxstyleconfiguration.md) — The properties of a group box instance.
- [indexViewStyle(_:)](<view/indexviewstyle(__).md>) — Sets the style for the index view within the current environment.
- [IndexViewStyle](indexviewstyle.md) — Defines the implementation of all `IndexView` instances within a view hierarchy.
- [labeledContentStyle(_:)](<view/labeledcontentstyle(__).md>) — Sets a style for labeled content.
- [LabeledContentStyle](labeledcontentstyle.md) — The appearance and behavior of a labeled content instance..
- [LabeledContentStyleConfiguration](labeledcontentstyleconfiguration.md) — The properties of a labeled content instance.
