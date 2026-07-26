---
title: UINavigationBarAppearance
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationbarappearance
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbarappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbarappearance.json'
content_hash: 'sha256:a1be27216cdc7ece'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UINavigationBarAppearance

<sub>Class</sub>

An object for customizing the appearance of a navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UINavigationBarAppearance
```

## Overview

After creating a [UINavigationBarAppearance](uinavigationbarappearance.md) object, use the methods and properties of this class to specify the appearance you want for items in the navigation bar. Use the inherited properties from [UIBarAppearance](uibarappearance.md) to configure the background and shadow attributes of the navigation bar itself.

## Relationships

- **Inherits From**: [UIBarAppearance](uibarappearance.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring the title

- [titleTextAttributes](uinavigationbarappearance/titletextattributes.md) — String attributes to apply to the text of a standard-size title.
- [largeTitleTextAttributes](uinavigationbarappearance/largetitletextattributes.md) — String attributes to apply to the text of a large-size title.
- [titlePositionAdjustment](uinavigationbarappearance/titlepositionadjustment.md) — The distance, in points, by which to offset the title horizontally and vertically.

### Configuring the subtitle

- [subtitleTextAttributes](uinavigationbarappearance/subtitletextattributes.md) — The default text attributes to apply to the subtitle rendered in the navigation bar.
- [largeSubtitleTextAttributes](uinavigationbarappearance/largesubtitletextattributes.md) — The default text attributes to apply to the subtitle when it’s rendered under the large title.

### Configuring bar button items

- [buttonAppearance](uinavigationbarappearance/buttonappearance.md) — The appearance attributes for plain bar button items in the navigation bar.

### Configuring the Back button

- [backButtonAppearance](uinavigationbarappearance/backbuttonappearance.md) — The appearance attributes for the back button.
- [backIndicatorImage](uinavigationbarappearance/backindicatorimage.md) — The image to display on the leading edge of the back button.
- [backIndicatorTransitionMaskImage](uinavigationbarappearance/backindicatortransitionmaskimage.md) — The image for masking content flowing under the back indicator image during push and pop transitions.
- [- setBackIndicatorImage:transitionMaskImage:](<uinavigationbarappearance/setbackindicatorimage(__transitionmaskimage_).md>) — Sets the back button indicator image and its transition mask.

### Configuring the Done button

- [doneButtonAppearance](uinavigationbarappearance/donebuttonappearance.md) — The appearance attributes for Done buttons. _(deprecated)_

### Instance Properties

- [prominentButtonAppearance](uinavigationbarappearance/prominentbuttonappearance.md) — The appearance attributes for Prominent buttons.
