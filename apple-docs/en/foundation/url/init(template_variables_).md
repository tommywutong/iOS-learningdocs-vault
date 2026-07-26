---
title: 'init(template:variables:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/init(template:variables:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/init(template:variables:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/init%28template%3Avariables%3A%29.json'
content_hash: 'sha256:903868f7c1f6ad3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# init(template:variables:)

<sub>Initializer</sub>

Creates a new `URL` by expanding the RFC 6570 template and variables.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(template: URL.Template, variables: [URL.Template.VariableName : URL.Template.Value])
```

## Parameters

- `template` — The RFC 6570 template to be expanded.

- `variables` — Variables to expand in the template.

## Discussion

This will fail if variable expansion does not produce a valid, well-formed URL.

All text will be converted to NFC (Unicode Normalization Form C) and UTF-8 before being percent-encoded if needed.
