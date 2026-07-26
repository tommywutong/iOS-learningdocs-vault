---
title: UIBarAppearance
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarappearance
source_url: 'https://developer.apple.com/documentation/uikit/uibarappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarappearance.json'
content_hash: 'sha256:ec6194a2124a95a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIBarAppearance

<sub>Class</sub>

An object for customizing the basic appearance of system bars.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIBarAppearance
```

## Overview

A [UIBarAppearance](uibarappearance.md) object contains the common traits shared by navigation bars, tab bars, and toolbars. When configuring a specific type of bar, you usually instantiate the appropriate bar appearance subclass. However, you may also create a [UIBarAppearance](uibarappearance.md) object, configure its properties, and use it to create new bar appearance objects in your app.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UINavigationBarAppearance](uinavigationbarappearance.md), [UITabBarAppearance](uitabbarappearance.md), [UIToolbarAppearance](uitoolbarappearance.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a custom bar appearance object

- [- initWithIdiom:](<uibarappearance/init(idiom_).md>) — Creates a new bar appearance object that targets the specified idiom.
- [- initWithBarAppearance:](<uibarappearance/init(barappearance_).md>) — Creates a new bar appearance object by copying relevant data from the specified appearance object.
- [- init](<uibarappearance/init().md>) — Creates a new bar appearance object containing default values.
- [- initWithCoder:](<uibarappearance/init(coder_).md>) — Creates an appearance object from data in an unarchiver.

### Copying a custom bar appearance object

- [- copy](<uibarappearance/copy().md>) — Creates a copy of the appearance object.

### Resetting the appearance properties

- [- configureWithDefaultBackground](<uibarappearance/configurewithdefaultbackground().md>) — Configures the bar appearance object with default background and shadow values.
- [- configureWithOpaqueBackground](<uibarappearance/configurewithopaquebackground().md>) — Configures the bar appearance object with a set of opaque colors that are appropriate for the current theme.
- [- configureWithTransparentBackground](<uibarappearance/configurewithtransparentbackground().md>) — Configures the bar appearance object with a transparent background and no shadow.

### Configuring the background appearance

- [backgroundEffect](uibarappearance/backgroundeffect.md) — The blur effect to apply to the bar’s background.
- [backgroundColor](uibarappearance/backgroundcolor.md) — The background color of the bar.
- [backgroundImage](uibarappearance/backgroundimage.md) — The image to display on top of the bar’s background color.
- [backgroundImageContentMode](uibarappearance/backgroundimagecontentmode.md) — The content mode to use when displaying the bar’s background image.

### Configuring the shadow appearance

- [shadowColor](uibarappearance/shadowcolor.md) — The color to apply to the bar’s custom or default shadow.
- [shadowImage](uibarappearance/shadowimage.md) — The image to use for the bar’s shadow.

### Getting the supported idiom

- [idiom](uibarappearance/idiom.md) — The idiom targeted by this bar appearance object.

### Instance Properties

- [overrideUserInterfaceStyle](uibarappearance/overrideuserinterfacestyle.md) — Overrides the userInterfaceStyle of the bar. _(beta)_

## See Also

### Shared appearance

- [UIBarButtonItemAppearance](uibarbuttonitemappearance.md) — An object for customizing the appearance of bar button items.
- [UIBarButtonItemStateAppearance](uibarbuttonitemstateappearance.md) — A data object containing the specific customizations for a bar button item in a particular state.
