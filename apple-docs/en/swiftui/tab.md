---
title: Tab
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tab
source_url: 'https://developer.apple.com/documentation/swiftui/tab'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tab.json'
content_hash: 'sha256:4f0c32d5a851112d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Tab

<sub>Structure</sub>

The content for a tab and the tab’s associated tab item in a tab view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Tab<Value, Content, Label>
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [TabContent](tabcontent.md)

## Topics

### Creating a tab

- [init(content:)](<tab/init(content_).md>) — Creates a new tab that you can use in a tab view, with an empty label.
- [init(value:content:)](<tab/init(value_content_).md>) — Creates a new tab that you can use in a tab view, with an empty label.
- [init(role:content:)](<tab/init(role_content_).md>) — Creates a new tab that you can use in a tab view, with an empty label.
- [init(value:role:content:)](<tab/init(value_role_content_).md>) — Creates a new tab with a label inferred from the role.

### Creating a tab with label

- [init(content:label:)](<tab/init(content_label_).md>) — Creates a new tab with a label that you can use in a tab view.
- [init(value:content:label:)](<tab/init(value_content_label_).md>) — Creates a new tab with a label that you can use in a tab view.
- [init(role:content:label:)](<tab/init(role_content_label_).md>) — Creates a new tab with a label that you can use in a tab view.
- [init(value:role:content:label:)](<tab/init(value_role_content_label_).md>) — Creates a new tab with a label that you can use in a tab view.

### Creating a tab with system symbol

- [init(_:systemImage:content:)](<tab/init(__systemimage_content_).md>) — Creates a new tab that you can use in a tab view using a system image for the tab item’s image, and a localized string key label.
- [init(_:systemImage:value:content:)](<tab/init(__systemimage_value_content_).md>) — Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value using a system image for the tab’s tab item image, with a localized string key label.
- [init(_:systemImage:role:content:)](<tab/init(__systemimage_role_content_).md>) — Creates a new tab that you can use in a tab view using a system image for the tab item’s image, and a localized string key label.
- [init(_:systemImage:value:role:content:)](<tab/init(__systemimage_value_role_content_).md>) — Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value using a system image for the tab’s tab item image, with a localized string key label.

### Creating a tab with image

- [init(_:image:content:)](<tab/init(__image_content_).md>) — Creates a new tab that you can use in a tab view, with a localized string key label.
- [init(_:image:value:content:)](<tab/init(__image_value_content_).md>) — Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value, with a localized string key label.
- [init(_:image:role:content:)](<tab/init(__image_role_content_).md>) — Creates a new tab that you can use in a tab view, with a localized string key label.
- [init(_:image:value:role:content:)](<tab/init(__image_value_role_content_).md>) — Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value, with a localized string key label.

### Supporting types

- [DefaultTabLabel](defaulttablabel.md) — The default label to use for a tab or tab section.

## See Also

### Presenting views in tabs

- [Enhancing your app’s content with tab navigation](enhancing-your-app-content-with-tab-navigation.md) — Keep your app content front and center while providing quick access to navigation using the tab bar.
- [TabView](tabview.md) — A view that switches between multiple child views using interactive user interface elements.
- [TabRole](tabrole.md) — A value that defines the purpose of the tab.
- [TabSection](tabsection.md) — A container that you can use to add hierarchy within a tab view.
- [tabViewStyle(_:)](<view/tabviewstyle(__).md>) — Sets the style for the tab view within the current environment.
