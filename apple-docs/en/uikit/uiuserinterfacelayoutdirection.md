---
title: UIUserInterfaceLayoutDirection
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiuserinterfacelayoutdirection
source_url: 'https://developer.apple.com/documentation/uikit/uiuserinterfacelayoutdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiuserinterfacelayoutdirection.json'
content_hash: 'sha256:13f2839c085cf19a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIUserInterfaceLayoutDirection

<sub>Enumeration</sub>

Constants that specify the directional flow of the user interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIUserInterfaceLayoutDirection
```

## Overview

One of these constants is returned by the [userInterfaceLayoutDirection](uiapplication/userinterfacelayoutdirection.md) property. It indicates the directionality of the language in the user interface of the app.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIUserInterfaceLayoutDirectionLeftToRight](uiuserinterfacelayoutdirection/lefttoright.md) — The layout direction is left to right.
- [UIUserInterfaceLayoutDirectionRightToLeft](uiuserinterfacelayoutdirection/righttoleft.md) — The layout direction right to left.

### Initializers

- [init(rawValue:)](<uiuserinterfacelayoutdirection/init(rawvalue_).md>)

## See Also

### Accessing the layout direction

- [userInterfaceLayoutDirection](uiapplication/userinterfacelayoutdirection.md) — The layout direction of the user interface.
