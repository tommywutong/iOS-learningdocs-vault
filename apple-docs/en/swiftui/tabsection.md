---
title: TabSection
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabsection
source_url: 'https://developer.apple.com/documentation/swiftui/tabsection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabsection.json'
content_hash: 'sha256:180088f5c949990e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TabSection

<sub>Structure</sub>

A container that you can use to add hierarchy within a tab view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TabSection<Header, Content, Footer, SelectionValue>
```

## Overview

Use [TabSection](tabsection.md) to organize tab content into separate sections. Each section has custom tab content that you provide on a per-instance basis. You can also provide a header for each section.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [TabContent](tabcontent.md)

## Topics

### Creating a tab section

- [init(content:)](<tabsection/init(content_).md>) — Creates a section with the provided section content.
- [init(_:content:)](<tabsection/init(__content_).md>) — Creates a section with the provided content.
- [init(content:header:)](<tabsection/init(content_header_).md>) — Creates a section with a header and the provided section content.

### Supporting types

- [DefaultTabLabel](defaulttablabel.md) — The default label to use for a tab or tab section.

## See Also

### Presenting views in tabs

- [Enhancing your app’s content with tab navigation](enhancing-your-app-content-with-tab-navigation.md) — Keep your app content front and center while providing quick access to navigation using the tab bar.
- [TabView](tabview.md) — A view that switches between multiple child views using interactive user interface elements.
- [Tab](tab.md) — The content for a tab and the tab’s associated tab item in a tab view.
- [TabRole](tabrole.md) — A value that defines the purpose of the tab.
- [tabViewStyle(_:)](<view/tabviewstyle(__).md>) — Sets the style for the tab view within the current environment.
