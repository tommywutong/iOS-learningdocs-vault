---
title: LibraryItem
framework: DeveloperToolsSupport
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/developertoolssupport/libraryitem
source_url: 'https://developer.apple.com/documentation/developertoolssupport/libraryitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/developertoolssupport/libraryitem.json'
content_hash: 'sha256:7ecf6e29ea3de1fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [DeveloperToolsSupport](../developertoolssupport.md)

# LibraryItem

<sub>Structure</sub>

A single item to add to the Xcode library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct LibraryItem
```

## Overview

Declare a library item to describe an entry in the Xcode library. Xcode discovers and validates library items that you place in the context of a [LibraryContentProvider](librarycontentprovider.md) instance.

At a minimum, you provide an expression that Xcode uses when the user chooses the library item. You can provide any expression that compiles in the context of the library item instantiation. However, Xcode only honors items that adhere to certain restrictions, as described in [views](librarycontentprovider/views.md) and [modifiers(base:)](<librarycontentprovider/modifiers(base_).md>).

You can also provide additional characteristics, like a title and a category, to help you find the item when searching the library.

## Topics

### Creating a Library Item

- [init(_:visible:title:category:matchingSignature:)](<libraryitem/init(__visible_title_category_matchingsignature_).md>) — Creates a new library item.
- [Category](libraryitem/category.md) — The kinds of library items that you can create.

## See Also

### Library customization

- [LibraryContentProvider](librarycontentprovider.md) — A source of Xcode library and code completion content.
