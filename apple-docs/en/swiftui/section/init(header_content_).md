---
title: 'init(header:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/section/init(header:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/section/init(header:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/section/init%28header%3Acontent%3A%29.json'
content_hash: 'sha256:e543cc68a7e2a66a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Section](../section.md)

# init(header:content:)

<sub>Initializer</sub>

Creates a section with a header and the provided section content.

> [!warning] Deprecated
> Use `init(content:header:)-29e2l` instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(header: Parent, @ContentBuilder content: () -> Content)
```

## Parameters

- `header` — A view to use as the section’s header.

- `content` — The section’s content.

## See Also

### Deprecated symbols

- [init(footer:content:)](<init(footer_content_).md>) — Creates a section with a footer and the provided section content. _(deprecated)_
- [init(header:footer:content:)](<init(header_footer_content_).md>) — Creates a section with a header, footer, and the provided section content. _(deprecated)_
- [collapsible(_:)](<collapsible(__).md>) — Sets whether a section can be collapsed by the user. _(deprecated)_
