---
title: sender
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenuleaf/sender
source_url: 'https://developer.apple.com/documentation/uikit/uimenuleaf/sender'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenuleaf/sender.json'
content_hash: 'sha256:507f3dd1554e3304'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuLeaf](../uimenuleaf.md)

# sender

<sub>Instance Property</sub>

The object on behalf of which to perform the menu element’s primary action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var sender: Any? { get }
```

## Discussion

The system populates this property during the execution of the menu element’s action (its handler or selector).

## See Also

### Performing actions

- [- performWithSender:target:](<performwithsender(__target_).md>) — Performs the element’s primary action.
