---
title: Section
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/section
source_url: 'https://developer.apple.com/documentation/swiftui/section'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/section.json'
content_hash: 'sha256:9dcccd354d53b889'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Section

<sub>Structure</sub>

A container view that you can use to add hierarchy within certain views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Section<Parent, Content, Footer>
```

## Overview

Use `Section` instances in views like [List](list.md), [Picker](picker.md), and [Form](form.md) to organize content into separate sections. Each section has custom content that you provide on a per-instance basis. You can also provide headers and footers for each section.

### Collapsible sections

Create sections that expand and collapse by using an initializer that accepts an `isExpanded` binding. A collapsible section in a [List](list.md) that uses the [sidebar](liststyle/sidebar.md) style shows a disclosure indicator next to the section’s header. Tapping on the disclosure indicator toggles the appearance of the section’s content.

> [!note] Note
> Not all contexts provide a default control to trigger collapse or expansion.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [TableRowContent](tablerowcontent.md), [View](view.md)

## Topics

### Creating a section

- [init(content:)](<section/init(content_).md>) — Creates a section with the provided section content.
- [init(_:content:)](<section/init(__content_).md>) — Creates a section with the provided section content.

### Adding headers and footers

- [init(content:header:)](<section/init(content_header_).md>) — Creates a section with a header and the provided section content.
- [init(content:footer:)](<section/init(content_footer_).md>) — Creates a section with a footer and the provided section content.
- [init(content:header:footer:)](<section/init(content_header_footer_).md>) — Creates a section with a header, footer, and the provided section content.

### Controlling collapsibility

- [init(_:isExpanded:content:)](<section/init(__isexpanded_content_).md>) — Creates a section with the provided section content.
- [init(isExpanded:content:header:)](<section/init(isexpanded_content_header_).md>) — Creates a section with the provided section content.

### Deprecated symbols

- [init(header:content:)](<section/init(header_content_).md>) — Creates a section with a header and the provided section content. _(deprecated)_
- [init(footer:content:)](<section/init(footer_content_).md>) — Creates a section with a footer and the provided section content. _(deprecated)_
- [init(header:footer:content:)](<section/init(header_footer_content_).md>) — Creates a section with a header, footer, and the provided section content. _(deprecated)_
- [collapsible(_:)](<section/collapsible(__).md>) — Sets whether a section can be collapsed by the user. _(deprecated)_

## See Also

### Organizing views into sections

- [SectionCollection](sectioncollection.md) — An opaque collection representing the sections of view.
- [SectionConfiguration](sectionconfiguration.md) — Specifies the contents of a section.
