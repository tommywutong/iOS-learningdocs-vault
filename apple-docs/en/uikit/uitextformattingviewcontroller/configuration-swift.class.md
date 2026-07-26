---
title: UITextFormattingViewController.Configuration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextformattingviewcontroller/configuration-swift.class
source_url: 'https://developer.apple.com/documentation/uikit/uitextformattingviewcontroller/configuration-swift.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextformattingviewcontroller/configuration-swift.class.json'
content_hash: 'sha256:5cad2f364dd95311'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFormattingViewController](../uitextformattingviewcontroller.md)

# UITextFormattingViewController.Configuration

<sub>Class</sub>

Text formatting view controller configuration object.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class Configuration
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSCoding](../../foundation/nscoding.md), [NSCopying](../../foundation/nscopying.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [NSSecureCoding](../../foundation/nssecurecoding.md)

## Topics

### Initializers

- [- init](<configuration-swift.class/init().md>) — Creates a default configuration with most common text formatting options.
- [init(coder:)](<configuration-swift.class/init(coder_).md>)
- [- initWithGroups:](<configuration-swift.class/init(groups_).md>) — Creates a configuration object with provided component groups.

### Instance Properties

- [fontPickerConfiguration](configuration-swift.class/fontpickerconfiguration.md) — Configuration object that will be used to customize `UIFontPickerViewController` if presented by `UITextFormattingViewController`.
- [formattingStyles](configuration-swift.class/formattingstyles.md)
- [groups](configuration-swift.class/groups.md) — Component groups displayed by text formatting view.

## See Also

### Classes

- [Component](component.md) — Defines text formatting view component.
- [ComponentGroup](componentgroup.md) — Defines grouping of text formatting components in view.
