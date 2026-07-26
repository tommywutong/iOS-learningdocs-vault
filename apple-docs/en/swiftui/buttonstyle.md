---
title: ButtonStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/buttonstyle
source_url: 'https://developer.apple.com/documentation/swiftui/buttonstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/buttonstyle.json'
content_hash: 'sha256:f2a0634e88aaf86d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ButtonStyle

<sub>Protocol</sub>

A type that applies standard interaction behavior and a custom appearance to all buttons within a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol ButtonStyle
```

## Overview

To configure the current button style for a view hierarchy, use the [buttonStyle(_:)](<view/buttonstyle(__).md>) modifier. Specify a style that conforms to `ButtonStyle` when creating a button that uses the standard button interaction behavior defined for each platform. To create a button with custom interaction behavior, use [PrimitiveButtonStyle](primitivebuttonstyle.md) instead.

## Topics

### Custom button styles

- [makeBody(configuration:)](<buttonstyle/makebody(configuration_).md>) — Creates a view that represents the body of a button.
- [Configuration](buttonstyle/configuration.md) — The properties of a button.
- [Body](buttonstyle/body.md) — A view that represents the body of a button.

## See Also

### Styling buttons

- [buttonStyle(_:)](<view/buttonstyle(__).md>) — Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [ButtonStyleConfiguration](buttonstyleconfiguration.md) — The properties of a button.
- [PrimitiveButtonStyle](primitivebuttonstyle.md) — A type that applies custom interaction behavior and a custom appearance to all buttons within a view hierarchy.
- [PrimitiveButtonStyleConfiguration](primitivebuttonstyleconfiguration.md) — The properties of a button.
- [signInWithAppleButtonStyle(_:)](<view/signinwithapplebuttonstyle(__).md>) — Sets the style used for displaying the control (see `SignInWithAppleButton.Style`).
- [buttonSizing(_:)](<view/buttonsizing(__).md>) — The preferred sizing behavior of buttons in the view hierarchy.
- [ButtonSizing](buttonsizing.md) — The sizing behavior of `Button`s and other button-like controls.
