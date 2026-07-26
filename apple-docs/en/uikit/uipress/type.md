---
title: type
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipress/type
source_url: 'https://developer.apple.com/documentation/uikit/uipress/type'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipress/type.json'
content_hash: 'sha256:5b7ac030a14185f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPress](../uipress.md)

# type

<sub>Instance Property</sub>

The type of the specified press.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var type: UIPress.PressType { get }
```

## Discussion

For a list of all possible types, see the [PressType](presstype.md) enumeration.

## See Also

### Getting press attributes

- [key](key.md) — The key pressed or released on a physical keyboard.
- [phase](phase-swift.property.md) — The current press phase of the object.
- [timestamp](timestamp.md) — The time when the press occurred or when it was last mutated.
