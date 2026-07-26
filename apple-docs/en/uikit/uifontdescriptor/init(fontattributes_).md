---
title: 'init(fontAttributes:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifontdescriptor/init(fontattributes:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/init(fontattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/init%28fontattributes%3A%29.json'
content_hash: 'sha256:e6873663b5a3fbf5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontDescriptor](../uifontdescriptor.md)

# init(fontAttributes:)

<sub>Initializer</sub>

Creates a font descriptor with the specified attributes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(fontAttributes attributes: [UIFontDescriptor.AttributeName : Any] = [:])
```

## Parameters

- `attributes` — The attributes for the new font descriptor. If `nil`, the font descriptor’s attribute dictionary will be empty.

## Return Value

The new font descriptor.

## See Also

### Initializing a font descriptor

- [- init](<init().md>) — Creates a font descriptor.
- [- initWithCoder:](<init(coder_).md>) — Creates a font descriptor from data in an unarchiver.
