---
title: UIBarButtonItemBadge
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitembadge
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitembadge'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitembadge.json'
content_hash: 'sha256:776518b3d76370d5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIBarButtonItemBadge

<sub>Class</sub>

A badge to be rendered on a bar button item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UIBarButtonItemBadge : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Instance Properties

- [backgroundColor](uibarbuttonitembadge/backgroundcolor.md) — The badge’s background color. A `nil` value will be treated as an indication to use the system default.
- [font](uibarbuttonitembadge/font.md) — The font to use for the badge. A `nil` value will be treated as an indication to use the system default.
- [foregroundColor](uibarbuttonitembadge/foregroundcolor.md) — The badge’s foreground color. A `nil` value will be treated as an indication to use the system default.
- [stringValue](uibarbuttonitembadge/stringvalue.md)

### Instance Methods

- [init](uibarbuttonitembadge/init.md)

### Type Methods

- [badgeWithCount:](uibarbuttonitembadge/badgewithcount_.md) — Creates a badge with the specified `count`.
- [badgeWithString:](uibarbuttonitembadge/badgewithstring_.md) — Creates a badge with the specified `string`.
- [indicatorBadge](uibarbuttonitembadge/indicatorbadge.md) — Creates a badge that’s empty, and just renders the badge background with no content.

## See Also

### Adding a badge

- [badge](uibarbuttonitem/badge-1zzen.md) — Sets a badge on the bar button item. Supported in navigation bars and toolbars.
