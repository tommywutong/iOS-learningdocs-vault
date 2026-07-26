---
title: LabelStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/labelstyle
source_url: 'https://developer.apple.com/documentation/swiftui/labelstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/labelstyle.json'
content_hash: 'sha256:120dc8814039f185'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# LabelStyle

<sub>Protocol</sub>

A type that applies a custom appearance to all labels within a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol LabelStyle
```

## Overview

To configure the current label style for a view hierarchy, use the [labelStyle(_:)](<view/labelstyle(__).md>) modifier.

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

- **Conforming Types**: [DefaultLabelStyle](defaultlabelstyle.md), [IconOnlyLabelStyle](icononlylabelstyle.md), [TitleAndIconLabelStyle](titleandiconlabelstyle.md), [TitleOnlyLabelStyle](titleonlylabelstyle.md)

## Topics

### Getting built-in label styles

- [automatic](labelstyle/automatic.md) — A label style that resolves its appearance automatically based on the current context.
- [iconOnly](labelstyle/icononly.md) — A label style that only displays the icon of the label.
- [titleAndIcon](labelstyle/titleandicon.md) — A label style that shows both the title and icon of the label using a system-standard layout.
- [titleOnly](labelstyle/titleonly.md) — A label style that only displays the title of the label.

### Creating custom label styles

- [makeBody(configuration:)](<labelstyle/makebody(configuration_).md>) — Creates a view that represents the body of a label.
- [Configuration](labelstyle/configuration.md) — The properties of a label.
- [Body](labelstyle/body.md) — A view that represents the body of a label.

### Supporting types

- [DefaultLabelStyle](defaultlabelstyle.md) — The default label style in the current context.
- [IconOnlyLabelStyle](icononlylabelstyle.md) — A label style that only displays the icon of the label.
- [TitleAndIconLabelStyle](titleandiconlabelstyle.md) — A label style that shows both the title and icon of the label using a system-standard layout.
- [TitleOnlyLabelStyle](titleonlylabelstyle.md) — A label style that only displays the title of the label.

## See Also

### Styling views that display text

- [labelStyle(_:)](<view/labelstyle(__).md>) — Sets the style for labels within this view.
- [LabelStyleConfiguration](labelstyleconfiguration.md) — The properties of a label.
- [textFieldStyle(_:)](<view/textfieldstyle(__).md>) — Sets the style for text fields within this view.
- [TextFieldStyle](textfieldstyle.md) — A specification for the appearance and interaction of a text field.
- [textEditorStyle(_:)](<view/texteditorstyle(__).md>) — Sets the style for text editors within this view.
- [TextEditorStyle](texteditorstyle.md) — A specification for the appearance and interaction of a text editor.
- [TextEditorStyleConfiguration](texteditorstyleconfiguration.md) — The properties of a text editor.
