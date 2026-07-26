---
title: 'rangeOfComposedCharacterSequence(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/rangeofcomposedcharactersequence(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/rangeofcomposedcharactersequence(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/rangeofcomposedcharactersequence%28at%3A%29.json'
content_hash: 'sha256:038552243a4e52de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# rangeOfComposedCharacterSequence(at:)

<sub>Instance Method</sub>

Returns the range in the receiver of the composed character sequence located at a given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func rangeOfComposedCharacterSequence(at index: Int) -> NSRange
```

## Parameters

- `index` — The index of a character in the receiver. The value must not exceed the bounds of the receiver.

## Return Value

The range in the receiver of the composed character sequence located at `anIndex`.

## Discussion

The composed character sequence includes the first decomposed base letter found at or before `anIndex`, and its length includes the decomposed base letter and all combining characters that follow.

## See Also

### Determining Composed Character Sequences

- [- rangeOfComposedCharacterSequencesForRange:](<rangeofcomposedcharactersequences(for_).md>) — Returns the range in the string of the composed character sequences for a given range.
