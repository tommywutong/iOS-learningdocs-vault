---
title: tokenBackgroundColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchtextfield/tokenbackgroundcolor
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtextfield/tokenbackgroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtextfield/tokenbackgroundcolor.json'
content_hash: 'sha256:0a0e2f6e24110917'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchTextField](../uisearchtextfield.md)

# tokenBackgroundColor

<sub>Instance Property</sub>

The background color for all tokens in the search text field.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var tokenBackgroundColor: UIColor! { get set }
```

## Discussion

If you set this property to `nil`, the search field reverts to the default token background color.

## See Also

### Customizing token behavior

- [- tokensInRange:](<tokens(in_).md>) — Returns the search field’s tokens that are within a given range.
- [- positionOfTokenAtIndex:](<positionoftoken(at_).md>) — Converts a token index into a text position.
