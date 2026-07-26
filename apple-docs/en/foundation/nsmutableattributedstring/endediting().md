---
title: endEditing()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutableattributedstring/endediting()
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/endediting()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/endediting%28%29.json'
content_hash: 'sha256:e63b29ad56bfe08a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# endEditing()

<sub>Instance Method</sub>

Ends the buffering of changes to the string’s characters and attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func endEditing()
```

## Discussion

Override this method in a subclass to consolidate changes made since a previous call to [- beginEditing](<beginediting().md>). When you call this method, the string notifies observers of the changes.

The default implementation of this method does nothing. Subclasses such as [NSTextStorage](../../appkit/nstextstorage.md) override this method and use it to tell the layout manager to update the text layout.

## See Also

### Related Documentation

- [processEditing()](<../../appkit/nstextstorage/processediting().md>) — Cleans up changes to the text storage object and notifies its delegate and layout managers of changes.

### Grouping Changes

- [- beginEditing](<beginediting().md>) — Begins the buffering of changes to the string’s characters and attributes.
