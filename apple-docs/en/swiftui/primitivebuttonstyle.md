---
title: PrimitiveButtonStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/primitivebuttonstyle
source_url: 'https://developer.apple.com/documentation/swiftui/primitivebuttonstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/primitivebuttonstyle.json'
content_hash: 'sha256:da464e942797d8c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PrimitiveButtonStyle

<sub>Protocol</sub>

A type that applies custom interaction behavior and a custom appearance to all buttons within a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol PrimitiveButtonStyle
```

## Overview

To configure the current button style for a view hierarchy, use the [buttonStyle(_:)](<view/buttonstyle(__).md>) modifier. Specify a style that conforms to `PrimitiveButtonStyle` to create a button with custom interaction behavior. To create a button with the standard button interaction behavior defined for each platform, use [ButtonStyle](buttonstyle.md) instead.

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

- **Conforming Types**: [AccessoryBarActionButtonStyle](accessorybaractionbuttonstyle.md), [AccessoryBarButtonStyle](accessorybarbuttonstyle.md), [BorderedButtonStyle](borderedbuttonstyle.md), [BorderedProminentButtonStyle](borderedprominentbuttonstyle.md), [BorderlessButtonStyle](borderlessbuttonstyle.md), [CardButtonStyle](cardbuttonstyle.md), [DefaultButtonStyle](defaultbuttonstyle.md), [GlassButtonStyle](glassbuttonstyle.md), [GlassProminentButtonStyle](glassprominentbuttonstyle.md), [LinkButtonStyle](linkbuttonstyle.md), [PlainButtonStyle](plainbuttonstyle.md)

## Topics

### Getting built-in button styles

- [automatic](primitivebuttonstyle/automatic.md) — The default button style, based on the button’s context.
- [accessoryBar](primitivebuttonstyle/accessorybar.md) — A button style that is typically used in the context of an accessory toolbar (sometimes refererred to as a “scope bar”), for buttons that narrow the focus of a search or other operation.
- [accessoryBarAction](primitivebuttonstyle/accessorybaraction.md) — A button style that you use for extra actions in an accessory toolbar.
- [bordered](primitivebuttonstyle/bordered.md) — A button style that applies the standard border style based on the button’s context.
- [borderedProminent](primitivebuttonstyle/borderedprominent.md) — A button style that applies the standard bordered prominent style based on the button’s context.
- [borderless](primitivebuttonstyle/borderless.md) — A button style that doesn’t apply a border.
- [card](primitivebuttonstyle/card.md) — A button style that doesn’t pad the content, and applies a Liquid Glass effect when the button has focus.
- [glass](primitivebuttonstyle/glass.md) — A button style that applies a Liquid Glass effect based on the button’s context.
- [glassProminent](primitivebuttonstyle/glassprominent.md) — A button style that applies a prominent Liquid Glass effect based on the button’s context.
- [glass(_:)](<primitivebuttonstyle/glass(__).md>) — A button style that applies a configurable Liquid Glass effect based on the button’s context.
- [link](primitivebuttonstyle/link.md) — A button style for buttons that emulate links.
- [plain](primitivebuttonstyle/plain.md) — A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.

### Creating custom button styles

- [makeBody(configuration:)](<primitivebuttonstyle/makebody(configuration_).md>) — Creates a view that represents the body of a button.
- [Configuration](primitivebuttonstyle/configuration.md) — The properties of a button.
- [Body](primitivebuttonstyle/body.md) — A view that represents the body of a button.

### Supporting types

- [DefaultButtonStyle](defaultbuttonstyle.md) — The default button style, based on the button’s context.
- [AccessoryBarButtonStyle](accessorybarbuttonstyle.md) — A button style that you use for actions in an accessory toolbar that narrow the focus of a search or other operation.
- [AccessoryBarActionButtonStyle](accessorybaractionbuttonstyle.md) — A button style that you use for extra actions in an accessory toolbar.
- [BorderedButtonStyle](borderedbuttonstyle.md) — A button style that applies standard border artwork based on the button’s context.
- [BorderedProminentButtonStyle](borderedprominentbuttonstyle.md) — A button style that applies standard border prominent artwork based on the button’s context.
- [BorderlessButtonStyle](borderlessbuttonstyle.md) — A button style that doesn’t apply a border.
- [CardButtonStyle](cardbuttonstyle.md) — A button style that doesn’t pad the content, and applies a motion effect when a button has focus.
- [LinkButtonStyle](linkbuttonstyle.md) — A button style for buttons that emulate links.
- [PlainButtonStyle](plainbuttonstyle.md) — A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.

## See Also

### Styling buttons

- [buttonStyle(_:)](<view/buttonstyle(__).md>) — Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [ButtonStyle](buttonstyle.md) — A type that applies standard interaction behavior and a custom appearance to all buttons within a view hierarchy.
- [ButtonStyleConfiguration](buttonstyleconfiguration.md) — The properties of a button.
- [PrimitiveButtonStyleConfiguration](primitivebuttonstyleconfiguration.md) — The properties of a button.
- [signInWithAppleButtonStyle(_:)](<view/signinwithapplebuttonstyle(__).md>) — Sets the style used for displaying the control (see `SignInWithAppleButton.Style`).
- [buttonSizing(_:)](<view/buttonsizing(__).md>) — The preferred sizing behavior of buttons in the view hierarchy.
- [ButtonSizing](buttonsizing.md) — The sizing behavior of `Button`s and other button-like controls.
