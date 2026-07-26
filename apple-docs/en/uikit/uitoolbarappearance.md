---
title: UIToolbarAppearance
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitoolbarappearance
source_url: 'https://developer.apple.com/documentation/uikit/uitoolbarappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitoolbarappearance.json'
content_hash: 'sha256:da51f28f1b2a94ff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIToolbarAppearance

<sub>Class</sub>

An object for customizing the appearance of a toolbar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIToolbarAppearance
```

## Overview

After creating a [UIToolbarAppearance](uitoolbarappearance.md) object, use the methods and properties of this class to specify the appearance of items in the toolbar. Use the inherited properties from [UIBarAppearance](uibarappearance.md) to configure the background and shadow attributes of the toolbar itself.

## Relationships

- **Inherits From**: [UIBarAppearance](uibarappearance.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring bar button items

- [buttonAppearance](uitoolbarappearance/buttonappearance.md) — The appearance attributes for plain bar button items in the toolbar.
- [prominentButtonAppearance](uitoolbarappearance/prominentbuttonappearance.md) — The appearance attributes for Prominent buttons.

### Configuring the Done button

- [doneButtonAppearance](uitoolbarappearance/donebuttonappearance.md) — The appearance attributes for Done buttons. _(deprecated)_
