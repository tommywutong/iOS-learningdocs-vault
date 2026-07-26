---
title: 'init(_:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/template/init(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/template/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/template/init%28_%3A%29.json'
content_hash: 'sha256:789150c32cddb710'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URL](../../url.md) · [Template](../template.md)

# init(_:)

<sub>Initializer</sub>

Creates a new template from its text form.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ template: String)
```

## Discussion

The template string needs to be a valid RFC 6570 template.

This will parse the template and return `nil` if the template is invalid.
