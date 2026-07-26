---
title: 'titleTextAttributes(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibaritem/titletextattributes(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibaritem/titletextattributes(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibaritem/titletextattributes%28for%3A%29.json'
content_hash: 'sha256:42772b9e408c7e0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarItem](../uibaritem.md)

# titleTextAttributes(for:)

<sub>Instance Method</sub>

Returns the title’s text attributes for a given control state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func titleTextAttributes(for state: UIControl.State) -> [NSAttributedString.Key : Any]?
```

## Parameters

- `state` — The control state for which you want to know the text attributes for the title.

## Return Value

The title’s text attributes for `state`.

## Discussion

The dictionary may contain key-value pairs for text attributes for the font, text color, text shadow color, and text shadow offset using the keys listed in NSString UIKit Additions Reference.

## See Also

### Customizing appearance

- [- setTitleTextAttributes:forState:](<settitletextattributes(__for_).md>) — Sets the title’s text attributes for a given control state.
