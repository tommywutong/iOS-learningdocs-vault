---
title: 'rangeOfComposedCharacterSequences(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/rangeofcomposedcharactersequences(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/rangeofcomposedcharactersequences(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/rangeofcomposedcharactersequences%28for%3A%29.json'
content_hash: 'sha256:d9de1b27bcc486e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# rangeOfComposedCharacterSequences(for:)

<sub>Instance Method</sub>

Returns the range in the string of the composed character sequences for a given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func rangeOfComposedCharacterSequences(for range: NSRange) -> NSRange
```

## Parameters

- `range` — A range in the receiver. The range must not exceed the bounds of the receiver.

## Return Value

The range in the receiver that includes the composed character sequences in `range`.

## Discussion

This method provides a convenient way to grow a range to include all composed character sequences it overlaps.

## See Also

### Determining Composed Character Sequences

- [- rangeOfComposedCharacterSequenceAtIndex:](<rangeofcomposedcharactersequence(at_).md>) — Returns the range in the receiver of the composed character sequence located at a given index.
