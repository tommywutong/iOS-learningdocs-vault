---
title: localizedTitle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimutableapplicationshortcutitem/localizedtitle
source_url: 'https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem/localizedtitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimutableapplicationshortcutitem/localizedtitle.json'
content_hash: 'sha256:79c2c7b1c4a89b68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMutableApplicationShortcutItem](../uimutableapplicationshortcutitem.md)

# localizedTitle

<sub>Instance Property</sub>

The required, user-visible title for the Home Screen dynamic mutable quick action.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var localizedTitle: String { get set }
```

## Discussion

Every Home Screen mutable quick action must have a user-visible title.

If the title fits on one line, the system displays it as a single line quick action. If the title is too long for one line and you have not specified a [localizedSubtitle](localizedsubtitle.md) string, the system displays the title on two lines.

To internationalize the title for a Home Screen dynamic quick action, employ the [NSLocalizedString](../../foundation/nslocalizedstring.md) Foundation function, described in [Foundation Functions](../../foundation/foundation-functions.md), along with a `Localizable.strings` file in your Xcode project.

## See Also

### Inspecting a Home Screen dynamic mutable quick action

- [localizedSubtitle](localizedsubtitle.md) — The optional, user-visible subtitle for the Home Screen dynamic mutable quick action.
- [type](type.md) — A required, app-specific string that you can employ to identify the type of quick action to perform.
- [icon](icon.md) — The optional icon for the Home Screen dynamic mutable quick action.
- [userInfo](userinfo.md) — Optional, app-specific information that you can provide for use when your app performs the Home Screen dynamic mutable quick action.
