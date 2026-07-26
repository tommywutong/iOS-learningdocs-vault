---
title: 'components(separatedBy:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/components(separatedby:)-238fy'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/components(separatedby:)-238fy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/components%28separatedby%3A%29-238fy.json'
content_hash: 'sha256:0cd9811dd874ed60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# components(separatedBy:)

<sub>Instance Method</sub>

Returns an array containing substrings from the receiver that have been divided by a given separator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func components(separatedBy separator: String) -> [String]
```

## Parameters

- `separator` — The separator string.

## Return Value

An `NSArray` object containing substrings from the receiver that have been divided by `separator`.

## Discussion

The substrings in the array appear in the order they did in the receiver. Adjacent occurrences of the separator string produce empty strings in the result. Similarly, if the string begins or ends with the separator, the first or last substring, respectively, is empty. For example, this code fragment:

```objc
NSString *list = @"Karin, Carrie, David";
NSArray *listItems = [list componentsSeparatedByString:@", "];
```

produces the array `@[@"Karin", @"Carrie", @"David"]`.

If `list` begins with a comma and space—for example, `@", Norman, Stanley, Fletcher"`—the array has these contents: `@[@"", @"Norman", @"Stanley", @"Fletcher"]`.

If `list` has no separators—for example, `@"Karin"`—the array contains the string itself, in this case `@[@"Karin"]`.

## See Also

### Related Documentation

- [pathComponents](pathcomponents.md) — The file-system path components of the receiver.
- [- componentsJoinedByString:](<../nsarray/componentsjoined(by_).md>) — Constructs and returns an `NSString` object that is the result of interposing a given separator between the elements of the array.

### Dividing Strings

- [- componentsSeparatedByCharactersInSet:](<components(separatedby_)-27x9g.md>) — Returns an array containing substrings from the receiver that have been divided by characters in a given set.
- [- stringByTrimmingCharactersInSet:](<trimmingcharacters(in_).md>) — Returns a new string made by removing from both ends of the receiver characters contained in a given character set.
- [- substringFromIndex:](<substring(from_).md>) — Returns a new string containing the characters of the receiver from the one at a given index to the end.
- [- substringWithRange:](<substring(with_).md>) — Returns a string object containing the characters of the receiver that lie within a given range.
- [- substringToIndex:](<substring(to_).md>) — Returns a new string containing the characters of the receiver up to, but not including, the one at a given index.
