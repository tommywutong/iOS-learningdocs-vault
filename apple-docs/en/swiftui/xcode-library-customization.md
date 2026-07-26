---
title: Xcode library customization
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/xcode-library-customization
source_url: 'https://developer.apple.com/documentation/swiftui/xcode-library-customization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/xcode-library-customization.json'
content_hash: 'sha256:74ec64f3faf2e6ff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Xcode library customization

Expose custom views and modifiers in the Xcode library.

## Overview

You can add your custom SwiftUI views and view modifiers to Xcode’s library. This allows anyone developing your app or adopting your framework to access them by clicking the Library button (+) in Xcode’s toolbar. You can select and drag the custom library items into code, just like you would for system-provided items.

![](../../../attachments/75621f8df7fbcc9a90dc8e0bf967ef78/xcode-library-customization-hero@2x.png)

To add items to the library, create a structure that conforms to the [LibraryContentProvider](../developertoolssupport/librarycontentprovider.md) protocol and encapsulate any items you want to add as [LibraryItem](../developertoolssupport/libraryitem.md) instances. Implement the [views](../developertoolssupport/librarycontentprovider/views.md) computed property to add library items containing views. Implement the [modifiers(base:)](<../developertoolssupport/librarycontentprovider/modifiers(base_).md>) method to add items containing view modifiers. Xcode harvests items from all of the library content providers in your project as you work, and makes them available to you in its library.

## Topics

### Creating library items

- [LibraryContentProvider](../developertoolssupport/librarycontentprovider.md) — A source of Xcode library and code completion content.
- [LibraryItem](../developertoolssupport/libraryitem.md) — A single item to add to the Xcode library.

## See Also

### Tool support

- [Previews in Xcode](previews-in-xcode.md) — Generate dynamic, interactive previews of your custom views.
- [Performance analysis](performance-analysis.md) — Measure and improve your app’s responsiveness.
