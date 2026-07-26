---
title: SidebarRowSize
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sidebarrowsize
source_url: 'https://developer.apple.com/documentation/swiftui/sidebarrowsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sidebarrowsize.json'
content_hash: 'sha256:86333531eadcd5f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SidebarRowSize

<sub>Enumeration</sub>

The standard sizes of sidebar rows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum SidebarRowSize
```

## Overview

On macOS, sidebar rows have three different sizes: small, medium, and large. The size is primarily controlled by the current users’ “Sidebar Icon Size” in Appearance settings, and applies to all applications.

On all other platforms, the only supported sidebar size is `.medium`.

This size can be read or written in the environment using `EnvironmentValues.sidebarRowSize`.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting row sizes

- [SidebarRowSize.small](sidebarrowsize/small.md) — The standard “small” row size
- [SidebarRowSize.medium](sidebarrowsize/medium.md) — The standard “medium” row size
- [SidebarRowSize.large](sidebarrowsize/large.md) — The standard “large” row size

## See Also

### Configuring the sidebar

- [sidebarRowSize](environmentvalues/sidebarrowsize.md) — The current size of sidebar rows.
