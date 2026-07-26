---
title: UILetterformAwareSizingRule
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiletterformawaresizingrule
source_url: 'https://developer.apple.com/documentation/uikit/uiletterformawaresizingrule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiletterformawaresizingrule.json'
content_hash: 'sha256:56bef1e5e6f2f923'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UILetterformAwareSizingRule

<sub>Enumeration</sub>

Constants that specify typographic bounds-sizing behavior to handle text in fonts with oversize characters.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UILetterformAwareSizingRule
```

## Overview

For more information on typographic bounds sizing behavior, see [UILetterformAwareAdjusting](uiletterformawareadjusting.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Setting bounds-sizing behavior

- [UILetterformAwareSizingRuleOversize](uiletterformawaresizingrule/oversize.md) — Bounds-sizing behavior that displays oversize characters fully but may negatively impact typographic alignment.
- [UILetterformAwareSizingRuleTypographic](uiletterformawaresizingrule/typographic.md) — Standard typographic bounds-sizing behavior, which may clip oversize characters.

### Initializers

- [init(rawValue:)](<uiletterformawaresizingrule/init(rawvalue_).md>)

## See Also

### Specifying text-sizing behavior

- [sizingRule](uiletterformawareadjusting/sizingrule.md) — The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.
