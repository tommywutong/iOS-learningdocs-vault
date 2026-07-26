---
title: beginEditing()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutableattributedstring/beginediting()
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/beginediting()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/beginediting%28%29.json'
content_hash: 'sha256:aaadce84456f2954'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# beginEditing()

<sub>Instance Method</sub>

Begins the buffering of changes to the string’s characters and attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func beginEditing()
```

## Discussion

Override this method in a subclass to buffer or optimize a series of changes to the string’s characters or attributes. The string continues to buffer text until you call [- endEditing](<endediting().md>), at which time it consolidates the changes and notifies observers.

You can nest pairs of [- beginEditing](<beginediting().md>) and [- endEditing](<endediting().md>) messages.

## See Also

### Grouping Changes

- [- endEditing](<endediting().md>) — Ends the buffering of changes to the string’s characters and attributes.
