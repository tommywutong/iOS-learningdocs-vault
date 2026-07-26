---
title: FormStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/formstyle
source_url: 'https://developer.apple.com/documentation/swiftui/formstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/formstyle.json'
content_hash: 'sha256:c245d80755808f64'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FormStyle

<sub>Protocol</sub>

The appearance and behavior of a form.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol FormStyle
```

## Overview

To configure the style for a single [Form](form.md) or for all form instances in a view hierarchy, use the [formStyle(_:)](<view/formstyle(__).md>) modifier.

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

- **Conforming Types**: [AutomaticFormStyle](automaticformstyle.md), [ColumnsFormStyle](columnsformstyle.md), [GroupedFormStyle](groupedformstyle.md)

## Topics

### Getting built-in form styles

- [automatic](formstyle/automatic.md) — The default form style.
- [columns](formstyle/columns.md) — A non-scrolling form style with a trailing aligned column of labels next to a leading aligned column of values.
- [grouped](formstyle/grouped.md) — A form style with grouped rows.

### Creating custom form styles

- [makeBody(configuration:)](<formstyle/makebody(configuration_).md>) — Creates a view that represents the body of a form.
- [Configuration](formstyle/configuration.md) — The properties of a form instance.
- [Body](formstyle/body.md) — A view that represents the appearance and interaction of a form.

### Supporting types

- [AutomaticFormStyle](automaticformstyle.md) — The default form style.
- [ColumnsFormStyle](columnsformstyle.md) — A non-scrolling form style with a trailing aligned column of labels next to a leading aligned column of values.
- [GroupedFormStyle](groupedformstyle.md) — A form style with grouped rows.

## See Also

### Styling groups

- [controlGroupStyle(_:)](<view/controlgroupstyle(__).md>) — Sets the style for control groups within this view.
- [ControlGroupStyle](controlgroupstyle.md) — Defines the implementation of all control groups within a view hierarchy.
- [ControlGroupStyleConfiguration](controlgroupstyleconfiguration.md) — The properties of a control group.
- [formStyle(_:)](<view/formstyle(__).md>) — Sets the style for forms in a view hierarchy.
- [FormStyleConfiguration](formstyleconfiguration.md) — The properties of a form instance.
- [groupBoxStyle(_:)](<view/groupboxstyle(__).md>) — Sets the style for group boxes within this view.
- [GroupBoxStyle](groupboxstyle.md) — A type that specifies the appearance and interaction of all group boxes within a view hierarchy.
- [GroupBoxStyleConfiguration](groupboxstyleconfiguration.md) — The properties of a group box instance.
- [indexViewStyle(_:)](<view/indexviewstyle(__).md>) — Sets the style for the index view within the current environment.
- [IndexViewStyle](indexviewstyle.md) — Defines the implementation of all `IndexView` instances within a view hierarchy.
- [labeledContentStyle(_:)](<view/labeledcontentstyle(__).md>) — Sets a style for labeled content.
- [LabeledContentStyle](labeledcontentstyle.md) — The appearance and behavior of a labeled content instance..
- [LabeledContentStyleConfiguration](labeledcontentstyleconfiguration.md) — The properties of a labeled content instance.
