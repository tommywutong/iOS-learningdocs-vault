---
title: UIDocumentBrowserAction.Availability
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowseraction/availability-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowseraction/availability-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowseraction/availability-swift.struct.json'
content_hash: 'sha256:38d4ec37ea1ad276'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserAction](../uidocumentbrowseraction.md)

# UIDocumentBrowserAction.Availability

<sub>Structure</sub>

Values that determine where the action can appear in the document browser.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct Availability
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [UIDocumentBrowserActionAvailabilityMenu](availability-swift.struct/menu.md) — An action that appears in the Edit Menu when the user long presses a supported document.
- [UIDocumentBrowserActionAvailabilityNavigationBar](availability-swift.struct/navigationbar.md) — An action that appears in the navigation bar when the user puts the document browser in Select mode.

### Initializers

- [init(rawValue:)](<availability-swift.struct/init(rawvalue_).md>) — Returns a newly instantiated availability instance.

## See Also

### Accessing activity data

- [identifier](identifier.md) — The action’s unique identifier.
- [localizedTitle](localizedtitle.md) — The title that appears in the menu or navigation bar.
- [availability](availability-swift.property.md) — A value that defines where the action can appear (in the Edit Menu, the navigation bar, or both).
