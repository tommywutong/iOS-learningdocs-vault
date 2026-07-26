---
title: 'init(content:footer:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/section/init(content:footer:)'
source_url: 'https://developer.apple.com/documentation/swiftui/section/init(content:footer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/section/init%28content%3Afooter%3A%29.json'
content_hash: 'sha256:c692c93a03c3845a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Section](../section.md)

# init(content:footer:)

<sub>Initializer</sub>

Creates a section with a footer and the provided section content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) init(@ContentBuilder content: () -> Content, @ContentBuilder footer: () -> Footer)
```

## Parameters

- `content` — The section’s content.

- `footer` — A view to use as the section’s footer.

## See Also

### Adding headers and footers

- [init(content:header:)](<init(content_header_).md>) — Creates a section with a header and the provided section content.
- [init(content:header:footer:)](<init(content_header_footer_).md>) — Creates a section with a header, footer, and the provided section content.
