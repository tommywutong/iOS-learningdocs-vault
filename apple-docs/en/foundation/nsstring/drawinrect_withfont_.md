---
title: 'drawInRect:withFont:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsstring/drawinrect:withfont:'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/drawinrect:withfont:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/drawinrect%3Awithfont%3A.json'
content_hash: 'sha256:c4fce63c95fbb591'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# drawInRect:withFont:

<sub>Instance Method</sub>

Draws the string in the current graphics context using the specified bounding rectangle and font.

> [!warning] Deprecated
> Use [- drawInRect:withAttributes:](<draw(in_withattributes_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (CGSize) drawInRect:(CGRect) rect withFont:(UIFont *) font;
```

## Parameters

- `rect` — The bounding rectangle (in the current graphics context) in which to draw the string.

- `font` — The font to use for rendering.

## Return Value

The size of the rendered string. The returned values may be rounded up to the nearest whole number.

## Discussion

This method draws as much of the string as possible using the given font and constraints. This method uses the [UILineBreakModeWordWrap](../../uikit/uilinebreakmode/uilinebreakmodewordwrap.md) line break mode and the [UITextAlignmentLeft](../../uikit/uitextalignment/uitextalignmentleft.md) alignment.

## See Also

### Deprecated

- [+ stringWithCString:](<string(withcstring_).md>) — Creates a new string using a given C-string. _(deprecated)_
- [+ stringWithCString:length:](<string(withcstring_length_).md>) — Returns a string containing the characters in a given C-string. _(deprecated)_
- [+ stringWithContentsOfFile:](<string(withcontentsoffile_).md>) — Returns a string created by reading data from the file named by a given path. _(deprecated)_
- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes the receiver, a newly allocated `NSString` object, by reading data from the file named by `path`. _(deprecated)_
- [+ stringWithContentsOfURL:](<string(withcontentsof_).md>) — Returns a string created by reading data from the file named by a given URL. _(deprecated)_
- [- writeToFile:atomically:](<write(tofile_atomically_).md>) — Writes the contents of the receiver to the file specified by a given path. _(deprecated)_
- [- writeToURL:atomically:](<write(to_atomically_).md>) — Writes the contents of the receiver to the location specified by a given URL. _(deprecated)_
- [- getCharacters:](<getcharacters(__).md>) — Copies all characters from the receiver into a given buffer. _(deprecated)_
- [- cString](<cstring().md>) — Returns a representation of the receiver as a C string in the default C-string encoding. _(deprecated)_
- [- lossyCString](<lossycstring().md>) — Returns a representation of the receiver as a C string in the default C-string encoding, possibly losing information in converting to that encoding. _(deprecated)_
- [- cStringLength](<cstringlength().md>) — Returns the length in char-sized units of the receiver’s C-string representation in the default C-string encoding. _(deprecated)_
- [- getCString:](<getcstring(__).md>) — Invokes [- getCString:maxLength:range:remainingRange:](<getcstring(__maxlength_range_remaining_).md>) with `NSMaximumStringLength` as the maximum length, the receiver’s entire extent as the range, and `NULL` for the remaining range. _(deprecated)_
- [- getCString:maxLength:](<getcstring(__maxlength_).md>) — Invokes [- getCString:maxLength:range:remainingRange:](<getcstring(__maxlength_range_remaining_).md>) with `maxLength` as the maximum length in char-sized units, the receiver’s entire extent as the range, and `NULL` for the remaining range. _(deprecated)_
- [- getCString:maxLength:range:remainingRange:](<getcstring(__maxlength_range_remaining_).md>) — Converts the receiver’s content to the default C-string encoding and stores them in a given buffer. _(deprecated)_
- [- stringByAddingPercentEscapesUsingEncoding:](<addingpercentescapes(using_).md>) — Returns a representation of the receiver using a given encoding to determine the percent escapes necessary to convert the receiver into a legal URL string. _(deprecated)_
