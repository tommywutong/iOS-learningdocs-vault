---
title: 'sizeWithFont:constrainedToSize:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsstring/sizewithfont:constrainedtosize:'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/sizewithfont:constrainedtosize:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/sizewithfont%3Aconstrainedtosize%3A.json'
content_hash: 'sha256:8f50ebde72b98be6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# sizeWithFont:constrainedToSize:

<sub>Instance Method</sub>

Returns the size of the string if it were rendered and constrained to the specified size.

> [!warning] Deprecated
> Use [- boundingRectWithSize:options:attributes:context:](<boundingrect(with_options_attributes_context_).md>) instead. See also [UILabel](../../uikit/uilabel.md) as a possible alternative for some use cases.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (CGSize) sizeWithFont:(UIFont *) font constrainedToSize:(CGSize) size;
```

## Parameters

- `font` — The font to use for computing the string size.

- `size` — The maximum acceptable size for the string. This value is used to calculate where line breaks and wrapping would occur.

## Return Value

The width and height of the resulting string’s bounding box. These values may be rounded up to the nearest whole number.

## Discussion

You can use this method to obtain the layout metrics you need to draw a string in your user interface. This method does not actually draw the string or alter the receiver’s text in any way.

This method computes the metrics needed to draw the specified string. This method lays out the receiver’s text and attempts to make it fit the specified size using the specified font and the [NSLineBreakMode.byWordWrapping](../../appkit/nslinebreakmode/bywordwrapping.md) line break option. During layout, the method may break the text onto multiple lines to make it fit better. If the receiver’s text does not completely fit in the specified size, it lays out as much of the text as possible and truncates it (for layout purposes only) according to the specified line break mode. It then returns the size of the resulting truncated string. If the height specified in the `size` parameter is less than a single line of text, this method may return a height value that is bigger than the one specified.

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
