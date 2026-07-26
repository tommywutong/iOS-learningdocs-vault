---
title: UINib
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uinib
source_url: 'https://developer.apple.com/documentation/uikit/uinib'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinib.json'
content_hash: 'sha256:10b876ecea70fe70'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UINib

<sub>Class</sub>

An object that contains Interface Builder nib files.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UINib
```

## Overview

A [UINib](uinib.md) object caches the contents of a nib file in memory, ready for unarchiving and instantiation. When your app needs to instantiate the contents of the nib file, it can do so without having to load the data from the nib file first, which improves performance. The [UINib](uinib.md) object can automatically release this cached nib data to free up memory for your app under low-memory conditions, reloading that data the next time your app instantiates the nib.

Your app should use [UINib](uinib.md) objects whenever it needs to repeatedly instantiate the same nib data. For example, if your table view uses a nib file to instantiate table view cells, caching the nib in a [UINib](uinib.md) object can improve performance.

When you create a [UINib](uinib.md) object using the contents of a nib file, the object loads the object graph in the referenced nib file, but it doesn’t unarchive it yet. To unarchive all of the nib data and instantiate the nib, your app calls the [- instantiateWithOwner:options:](<uinib/instantiate(withowner_options_).md>) method. For more information about the steps that the [UINib](uinib.md) object follows to instantiate the nib’s object graph, see [Resource Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Introduction/Introduction.html#//apple_ref/doc/uid/10000051i).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a nib object

- [+ nibWithNibName:bundle:](<uinib/init(nibname_bundle_).md>) — Returns a nib object from the nib file in the specified bundle.
- [+ nibWithData:bundle:](<uinib/init(data_bundle_).md>) — Creates a nib object from nib data stored in memory.

### Retrieving objects from the nib file

- [- instantiateWithOwner:options:](<uinib/instantiate(withowner_options_).md>) — Unarchives and instantiates the in-memory contents of the nib object’s nib file, creating a distinct object tree and set of top-level objects.
- [OptionsKey](uinib/optionskey.md) — Options that specify how to unarchive and instantiate the nib.
