---
title: localizedStringResource
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/localizedstringresource/localizedstringresource
source_url: 'https://developer.apple.com/documentation/foundation/localizedstringresource/localizedstringresource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/localizedstringresource/localizedstringresource.json'
content_hash: 'sha256:190dd07d69ba7372'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [LocalizedStringResource](../localizedstringresource.md)

# localizedStringResource

<sub>Instance Property</sub>

A resource that helps provide a description of the instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var localizedStringResource: LocalizedStringResource { get }
```

## Discussion

This property implements the [CustomLocalizedStringResourceConvertible](../customlocalizedstringresourceconvertible.md) protocol, which allows conforming types to provide a [LocalizedStringResource](../localizedstringresource.md) that describes the instance.
