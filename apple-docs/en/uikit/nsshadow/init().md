---
title: init()
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsshadow/init()
source_url: 'https://developer.apple.com/documentation/uikit/nsshadow/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsshadow/init%28%29.json'
content_hash: 'sha256:c565b0ea3cf6afd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSShadow](../nsshadow.md)

# init()

<sub>Initializer</sub>

Creates a shadow object with default values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Return Value

An `NSShadow` object initialized with `0` as its offset, `0` as its blur radius, and the default color as its color. The returned object may be different from the original receiver.

## See Also

### Creating a shadow

- [- initWithCoder:](<init(coder_).md>) — Creates a shadow object from data in an unarchiver.
