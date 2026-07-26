---
title: UIBarButtonItemAppearance
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitemappearance
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitemappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitemappearance.json'
content_hash: 'sha256:37663f9925b0f958'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIBarButtonItemAppearance

<sub>Class</sub>

An object for customizing the appearance of bar button items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIBarButtonItemAppearance
```

## Overview

Use a [UIBarButtonItemAppearance](uibarbuttonitemappearance.md) object to customize the appearance of a bar button item in each of its possible states. You can customize the appearance differently for different states. For example, you might apply different colors to the button’s title in the [normal](uibarbuttonitemappearance/normal.md) and [highlighted](uibarbuttonitemappearance/highlighted.md) states.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a bar button item appearance object

- [- initWithStyle:](<uibarbuttonitemappearance/init(style_).md>) — Creates an appearance with default values that are appropriate for the specified button style.
- [- init](<uibarbuttonitemappearance/init().md>) — Creates an appearance object with default values that are appropriate for a plain button.
- [- initWithCoder:](<uibarbuttonitemappearance/init(coder_).md>) — Creates an appearance object from data in an unarchiver.

### Copying a bar button item bar appearance object

- [- copy](<uibarbuttonitemappearance/copy().md>) — Creates a copy of the appearance object.

### Resetting the appearance properties

- [- configureWithDefaultForStyle:](<uibarbuttonitemappearance/configurewithdefault(for_).md>) — Configures the bar button item appearance object with appropriate values for the specified button style.

### Configuring attributes for different button states

- [normal](uibarbuttonitemappearance/normal.md) — The appearance data to apply to the button when it’s in the normal state.
- [disabled](uibarbuttonitemappearance/disabled.md) — The appearance data to apply to the button when it’s in the disabled state.
- [highlighted](uibarbuttonitemappearance/highlighted.md) — The appearance data to apply to the button when it’s in the highlighted state.
- [focused](uibarbuttonitemappearance/focused.md) — The appearance data to apply to the button when it’s focused.

## See Also

### Shared appearance

- [UIBarAppearance](uibarappearance.md) — An object for customizing the basic appearance of system bars.
- [UIBarButtonItemStateAppearance](uibarbuttonitemstateappearance.md) — A data object containing the specific customizations for a bar button item in a particular state.
