---
title: UITabSidebarItem
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabsidebaritem
source_url: 'https://developer.apple.com/documentation/uikit/uitabsidebaritem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabsidebaritem.json'
content_hash: 'sha256:c75ce9975e33eebe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITabSidebarItem

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UITabSidebarItem
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Classes

- [Request](uitabsidebaritem/request.md)

### Initializers

- [+ itemFromRequest:](<uitabsidebaritem/init(request_).md>) — Creates a sidebar item from the specified request. The sidebar item will be preconfigured with the appropriate defaults for its content.

### Instance Properties

- [accessories](uitabsidebaritem/accessories-2peu2.md)
- [backgroundConfiguration](uitabsidebaritem/backgroundconfiguration-10tw8.md)
- [configurationState](uitabsidebaritem/configurationstate-1knk1.md)
- [content](uitabsidebaritem/content-swift.property.md)
- [contentConfiguration](uitabsidebaritem/contentconfiguration-254nx.md)

### Instance Methods

- [defaultBackgroundConfiguration()](<uitabsidebaritem/defaultbackgroundconfiguration().md>)
- [defaultContentConfiguration()](<uitabsidebaritem/defaultcontentconfiguration().md>)

### Enumerations

- [Content](uitabsidebaritem/content-swift.enum.md)

## See Also

### Supporting the sidebar

- [mode](uitabbarcontroller/mode-swift.property.md) — The display mode for a tab bar.
- [Mode](uitabbarcontroller/mode-swift.enum.md) — A tab bar’s display mode.
- [sidebar](uitabbarcontroller/sidebar-swift.property.md) — A tab bar’s corresponding sidebar.
- [Sidebar](uitabbarcontroller/sidebar-swift.class.md) — An object for managing and configuring the sidebar.
- [Request](uitabsidebaritem/request.md)
- [Animating](uitabbarcontroller/sidebar-swift.class/animating.md)
