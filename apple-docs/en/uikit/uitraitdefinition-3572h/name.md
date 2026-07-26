---
title: name
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitdefinition-3572h/name
source_url: 'https://developer.apple.com/documentation/uikit/uitraitdefinition-3572h/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitdefinition-3572h/name.json'
content_hash: 'sha256:52e7c68228a9d42f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitDefinition](../uitraitdefinition-3572h.md)

# name

<sub>Type Property</sub>

A short human-readable name for the trait, e.g. for printing and debugging output. By default, the trait’s class name is used when not implemented.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (class, nonatomic, readonly) NSString * name;
```

## See Also

### Type Properties

- [affectsColorAppearance](affectscolorappearance.md) — Whether the trait is used to resolve dynamic colors (or images), and changes to the trait should automatically trigger views using dynamic colors/images to update their appearance. Default is NO.
- [identifier](identifier.md) — A unique identifier string for the trait (reverse-DNS format recommended). Allows the trait to be encoded/decoded, and to map both a Swift and Objective-C trait to the same data.
