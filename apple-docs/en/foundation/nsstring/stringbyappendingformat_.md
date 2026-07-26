---
title: 'stringByAppendingFormat:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/stringbyappendingformat:'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/stringbyappendingformat:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/stringbyappendingformat%3A.json'
content_hash: 'sha256:606f5bbe2deed41b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# stringByAppendingFormat:

<sub>Instance Method</sub>

Returns a string made by appending to the receiver a string constructed from a given format string and the following arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSString *) stringByAppendingFormat:(NSString *) format;
```

## Parameters

- `format` — A format string. See [Formatting String Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943) for more information. This value must not be `nil`. > [!important] Important > Raises an `NSInvalidArgumentException` if `format` is `nil`.

## Return Value

A string made by appending to the receiver a string constructed from `format` and the following arguments, in the manner of [stringWithFormat:](stringwithformat_.md).

## Discussion

Pass a comma-separated list of variadic arguments to substitute into `format`.

## See Also

### Combining Strings

- [- stringByAppendingString:](<appending(__).md>) — Returns a new string made by appending a given string to the receiver.
- [- stringByPaddingToLength:withString:startingAtIndex:](<padding(tolength_withpad_startingat_).md>) — Returns a new string formed from the receiver by either removing characters from the end, or by appending as many occurrences as necessary of a given pad string.
