---
title: UIMenuElement.ImageVisibility
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uimenuelement/imagevisibility
source_url: 'https://developer.apple.com/documentation/uikit/uimenuelement/imagevisibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenuelement/imagevisibility.json'
content_hash: 'sha256:593e2436e7651b51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuElement](../uimenuelement.md)

# UIMenuElement.ImageVisibility

<sub>Enumeration</sub>

Visibility options for a menu element’s image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum ImageVisibility
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [UIMenuElementImageVisibilityAutomatic](imagevisibility/automatic.md) — The element’s image visibility is determined by the platform and context. _(beta)_
- [UIMenuElementImageVisibilityHidden](imagevisibility/hidden.md) — The element prefers its image to be hidden, even in contexts where images are shown by default. _(beta)_
- [UIMenuElementImageVisibilityVisible](imagevisibility/visible.md) — The element prefers its image to be visible, even in contexts where images are not shown by default. _(beta)_

### Initializers

- [init(rawValue:)](<imagevisibility/init(rawvalue_).md>) _(beta)_
