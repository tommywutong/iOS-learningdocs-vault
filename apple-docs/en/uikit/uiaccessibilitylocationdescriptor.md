---
title: UIAccessibilityLocationDescriptor
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitylocationdescriptor
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitylocationdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitylocationdescriptor.json'
content_hash: 'sha256:29b3760d2516ff8a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilityLocationDescriptor

<sub>Class</sub>

An accessibility descriptor for a specific geometric point of interest within a view, for use by assistive apps.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIAccessibilityLocationDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Initializing the descriptor

- [- initWithAttributedName:point:inView:](<uiaccessibilitylocationdescriptor/init(attributedname_point_in_).md>) — Initializes a new accessibility location descriptor using an attributed string and a specified point in a view.
- [- initWithName:point:inView:](<uiaccessibilitylocationdescriptor/init(name_point_in_).md>) — Initializes a new accessibility location descriptor with a specified point in a view.
- [- initWithName:view:](<uiaccessibilitylocationdescriptor/init(name_view_).md>) — Initializes a new accessibility location descriptor with a specified view’s activation point.

### Getting the descriptor information

- [name](uiaccessibilitylocationdescriptor/name.md) — Returns the plaintext string representation of the name for the accessibility location descriptor.
- [attributedName](uiaccessibilitylocationdescriptor/attributedname.md) — Returns the attributed string representation of the name for the accessibility location descriptor.
- [point](uiaccessibilitylocationdescriptor/point.md) — Returns the geometric point of interest for the accessibility location descriptor within its associated view and in the coordinate space of the view.
- [view](uiaccessibilitylocationdescriptor/view.md) — Returns the view associated with the accessibility location descriptor.

### Initializers

- [init(attributedName:point:inView:)](<uiaccessibilitylocationdescriptor/init(attributedname_point_inview_).md>)
- [init(name:point:inView:)](<uiaccessibilitylocationdescriptor/init(name_point_inview_).md>)
