---
title: 'boundingRect(with:options:context:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/boundingrect(with:options:context:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/boundingrect(with:options:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/boundingrect%28with%3Aoptions%3Acontext%3A%29.json'
content_hash: 'sha256:4d3919c80250d9f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# boundingRect(with:options:context:)

<sub>Instance Method</sub>

Returns the bounding rectangle necessary to draw the string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func boundingRect(with size: CGSize, options: NSStringDrawingOptions = [], context: NSStringDrawingContext?) -> CGRect
```

<sub>macOS</sub>

```swift
func boundingRect(with size: CGSize, options: NSString.DrawingOptions = [], context: NSStringDrawingContext?) -> CGRect
```

## Parameters

- `size` — The width and height constraints to apply when computing the string’s bounding rectangle.

- `options` — Additional drawing options to apply to the string during rendering. For a list of possible values, see [NSStringDrawingOptions](../../uikit/nsstringdrawingoptions.md).

- `context` — A context object with information about how to adjust the font tracking and scaling information. On return, the specified object contains information about the actual values used to render the string. This parameter may be `nil`.

## Return Value

A rectangle whose size component indicates the width and height required to draw the entire contents of the string.

## Discussion

You can use this method to compute the space required to draw the string. The constraints you specify in the size parameter are a guide for the renderer for how to size the string. However, the actual bounding rectangle returned by this method can be larger than the constraints if additional space is needed to render the entire string. Typically, the renderer preserves the width constraint and adjusts the height constraint as needed.

In iOS 7 and later, this method returns fractional sizes (in the `size` component of the returned rectangle); to use a returned size to size views, you must use raise its value to the nearest higher integer using the [ceil](../../kernel/1557272-ceil.md) function.

### Special Considerations

To calculate the bounding rectangle, this method uses the baseline origin by default, so it behaves as a single line. To render the string in multiple lines, specify [usesLineFragmentOrigin](../../uikit/nsstringdrawingoptions/useslinefragmentorigin.md) in `options`.

## See Also

### Getting metrics for the string

- [- size](<size().md>) — Returns the size necessary to draw the string.
- [- containsAttachmentsInRange:](<containsattachments(in_).md>) — Returns a Boolean value that indicates if the attributed string contains an attachment in the specified range.
