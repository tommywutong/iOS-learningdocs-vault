---
title: key
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipress/key
source_url: 'https://developer.apple.com/documentation/uikit/uipress/key'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipress/key.json'
content_hash: 'sha256:3ea77eeb36f192bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPress](../uipress.md)

# key

<sub>Instance Property</sub>

The key pressed or released on a physical keyboard.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var key: UIKey? { get }
```

## Discussion

This property is `nil` when the press event isn’t from a keyboard; for example, a button press on an Apple TV remote.

## See Also

### Getting press attributes

- [type](type.md) — The type of the specified press.
- [phase](phase-swift.property.md) — The current press phase of the object.
- [timestamp](timestamp.md) — The time when the press occurred or when it was last mutated.
