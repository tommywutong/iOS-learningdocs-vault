---
title: UIFontPickerViewController.Configuration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontpickerviewcontroller/configuration-swift.class
source_url: 'https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontpickerviewcontroller/configuration-swift.class.json'
content_hash: 'sha256:8f3f2b7c235c9dec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontPickerViewController](../uifontpickerviewcontroller.md)

# UIFontPickerViewController.Configuration

<sub>Class</sub>

The filters and display settings a font picker view controller uses to set up a font picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class Configuration
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSCopying](../../foundation/nscopying.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md)

## Topics

### Customizing the font picker’s appearance

- [displayUsingSystemFont](configuration-swift.class/displayusingsystemfont.md) — A Boolean value that determines whether to use the system font for all font names in the font picker.

### Filtering available fonts

- [includeFaces](configuration-swift.class/includefaces.md) — A Boolean value that determines whether the font picker should allow the user to select from font faces, or just font families.
- [filteredTraits](configuration-swift.class/filteredtraits.md) — A predicate to filter fonts based on their traits, like bold, italic, or monospace.
- [filteredLanguagesPredicate](configuration-swift.class/filteredlanguagespredicate.md) — A predicate to filter fonts based on the languages they support. _(deprecated)_
- [+ filterPredicateForFilteredLanguages:](<configuration-swift.class/filterpredicate(forfilteredlanguages_).md>) — Creates a font picker filter based on language support. _(deprecated)_

### Instance Properties

- [languageFilter](configuration-swift.class/languagefilter.md)

## See Also

### Font picker

- [UIFontPickerViewController](../uifontpickerviewcontroller.md) — A view controller that manages the interface for selecting a font that the system provides or the user installs.
- [UIFontPickerViewControllerDelegate](../uifontpickerviewcontrollerdelegate.md) — A set of optional methods for receiving messages about the user’s interaction with the font picker.
