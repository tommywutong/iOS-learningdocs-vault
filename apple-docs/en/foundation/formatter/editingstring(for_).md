---
title: 'editingString(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatter/editingstring(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/formatter/editingstring(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatter/editingstring%28for%3A%29.json'
content_hash: 'sha256:a03acac5911783f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Formatter](../formatter.md)

# editingString(for:)

<sub>Instance Method</sub>

The default implementation of this method invokes [- stringForObjectValue:](<string(for_).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func editingString(for obj: Any) -> String?
```

## Parameters

- `obj` — The object for which to return an editing string.

## Return Value

An `NSString` object that is used for editing the textual representation of `anObject`.

## Discussion

When implementing a subclass, override this method only when the string that users see and the string that they edit are different. In your implementation, return an `NSString` object that is used for editing, following the logic recommended for implementing [- stringForObjectValue:](<string(for_).md>). As an example, you would implement this method if you want the dollar signs in displayed strings removed for editing.

## See Also

### Getting Textual Representations of Object Values

- [- stringForObjectValue:](<string(for_).md>) — The default implementation of this method raises an exception.
- [- attributedStringForObjectValue:withDefaultAttributes:](<attributedstring(for_withdefaultattributes_).md>) — The default implementation returns `nil` to indicate that the formatter object does not provide an attributed string.
