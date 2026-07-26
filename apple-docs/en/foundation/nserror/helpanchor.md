---
title: helpAnchor
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nserror/helpanchor
source_url: 'https://developer.apple.com/documentation/foundation/nserror/helpanchor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nserror/helpanchor.json'
content_hash: 'sha256:6a0a75e331c037fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSError](../nserror.md)

# helpAnchor

<sub>Instance Property</sub>

A string to display in response to an alert panel help anchor button being pressed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var helpAnchor: String? { get }
```

## Discussion

The object in the user info dictionary for the key [NSHelpAnchorErrorKey](../nshelpanchorerrorkey.md). If the user info dictionary doesn’t contain a value for [NSHelpAnchorErrorKey](../nshelpanchorerrorkey.md), this property is `nil`.

If this property is non-`nil` for an error being presented by [init(error:)](<../../appkit/nsalert/init(error_).md>), the alert panel will include a help anchor button that can display this string.
