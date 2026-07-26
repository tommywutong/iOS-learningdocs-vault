---
title: UINavigationItem.ItemStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/itemstyle
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/itemstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/itemstyle.json'
content_hash: 'sha256:e7814f2a7d6364b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# UINavigationItem.ItemStyle

<sub>Enumeration</sub>

Constants that determine how the content of the navigation item lays out in the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum ItemStyle
```

## Overview

Navigation styles allow you to customize the behavior and content density of your navigation bar according to your app type.

- Navigator apps like Settings support a traditional navigation model for hierarchical data.
- Browser apps like Safari or Files support browsing through and navigating back and forth between multiple documents or folder structures.
- Editor apps support focused viewing or editing of individual documents.

> [!note] Related Sessions from WWDC22
> Session 10069: [Meet desktop-class iPad](https://developer.apple.com/wwdc22/10069)
>
> Session 10070: [Build a desktop-class iPad app](https://developer.apple.com/wwdc22/10070)

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UINavigationItemStyleNavigator](itemstyle/navigator.md) — A style for a traditional navigation-based interface.
- [UINavigationItemStyleBrowser](itemstyle/browser.md) — A style for a browser app interface.
- [UINavigationItemStyleEditor](itemstyle/editor.md) — A style for an editor app interface.

### Initializers

- [init(rawValue:)](<itemstyle/init(rawvalue_).md>)

## See Also

### Specifying the navigation style

- [style](style.md) — A style that determines how the content of the navigation item lays out in the navigation bar.
