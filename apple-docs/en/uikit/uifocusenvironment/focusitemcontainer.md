---
title: focusItemContainer
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusenvironment/focusitemcontainer
source_url: 'https://developer.apple.com/documentation/uikit/uifocusenvironment/focusitemcontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusenvironment/focusitemcontainer.json'
content_hash: 'sha256:a2fcf178e704fce4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusEnvironment](../uifocusenvironment.md)

# focusItemContainer

<sub>Instance Property</sub>

The container for the child focus items in this focus environment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var focusItemContainer: (any UIFocusItemContainer)? { get }
```

## Discussion

The value of this property is `nil` when no container exists.

## See Also

### Checking the ancestry of the environment

- [parentFocusEnvironment](parentfocusenvironment.md) — The parent focus environment for this environment.
