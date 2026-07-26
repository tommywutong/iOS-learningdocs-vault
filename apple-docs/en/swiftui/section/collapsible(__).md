---
title: 'collapsible(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/section/collapsible(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/section/collapsible(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/section/collapsible%28_%3A%29.json'
content_hash: 'sha256:4f401193f82e0b11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Section](../section.md)

# collapsible(_:)

<sub>Instance Method</sub>

Sets whether a section can be collapsed by the user.

> [!warning] Deprecated
> To disable collapsibility in macOS 14 and later, use one of the [Section](../section.md) initializers that lacks collapsibility.

<sub>macOS</sub>

```swift
func collapsible(_ collapsible: Bool) -> some View

```

## Discussion

This modifier only applies to sections in [List](../list.md) views that have the [sidebar](../liststyle/sidebar.md) style.

## See Also

### Deprecated symbols

- [init(header:content:)](<init(header_content_).md>) — Creates a section with a header and the provided section content. _(deprecated)_
- [init(footer:content:)](<init(footer_content_).md>) — Creates a section with a footer and the provided section content. _(deprecated)_
- [init(header:footer:content:)](<init(header_footer_content_).md>) — Creates a section with a header, footer, and the provided section content. _(deprecated)_
