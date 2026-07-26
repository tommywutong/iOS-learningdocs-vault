---
title: 'attributedString(for:withDefaultAttributes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatter/attributedstring(for:withdefaultattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/formatter/attributedstring(for:withdefaultattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatter/attributedstring%28for%3Awithdefaultattributes%3A%29.json'
content_hash: 'sha256:cc7cb455e556e7c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Formatter](../formatter.md)

# attributedString(for:withDefaultAttributes:)

<sub>Instance Method</sub>

The default implementation returns `nil` to indicate that the formatter object does not provide an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func attributedString(for obj: Any, withDefaultAttributes attrs: [NSAttributedString.Key : Any]? = nil) -> NSAttributedString?
```

## Parameters

- `obj` — The object for which a textual representation is returned.

- `attrs` — The default attributes to use for the returned attributed string.

## Return Value

An attributed string that represents `anObject`.

## Discussion

When implementing a subclass, return an `NSAttributedString` object if the string for display should have some attributes. For instance, you might want negative values in a financial application to appear in red text. Invoke your implementation of [- stringForObjectValue:](<string(for_).md>) to get the non-attributed string, then create an `NSAttributedString` object with it (see [- initWithString:](<../nsattributedstring/init(string_).md>)). Use the `attributes` default dictionary to reset the attributes of the string when a change in value warrants it (for example, a negative value becomes positive) For information on creating attributed strings, see [Attributed String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AttributedStrings/AttributedStrings.html#//apple_ref/doc/uid/10000036i).

## See Also

### Getting Textual Representations of Object Values

- [- stringForObjectValue:](<string(for_).md>) — The default implementation of this method raises an exception.
- [- editingStringForObjectValue:](<editingstring(for_).md>) — The default implementation of this method invokes [- stringForObjectValue:](<string(for_).md>).
