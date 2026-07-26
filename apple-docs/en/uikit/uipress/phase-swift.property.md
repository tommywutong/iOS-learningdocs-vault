---
title: phase
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipress/phase-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uipress/phase-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipress/phase-swift.property.json'
content_hash: 'sha256:421081d8eddcaf6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPress](../uipress.md)

# phase

<sub>Instance Property</sub>

The current press phase of the object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var phase: UIPress.Phase { get }
```

## Discussion

For a list of all possible press phases, see the [Phase](phase-swift.enum.md) enumeration.

## See Also

### Getting press attributes

- [key](key.md) — The key pressed or released on a physical keyboard.
- [type](type.md) — The type of the specified press.
- [timestamp](timestamp.md) — The time when the press occurred or when it was last mutated.
