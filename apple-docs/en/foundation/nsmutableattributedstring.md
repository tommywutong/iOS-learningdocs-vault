---
title: NSMutableAttributedString
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutableattributedstring
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring.json'
content_hash: 'sha256:82ecd5124813fa72'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMutableAttributedString

<sub>Class</sub>

A mutable string with associated attributes (such as visual style, hyperlinks, or accessibility data) for portions of its text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMutableAttributedString
```

## Overview

The `NSMutableAttributedString` class declares additional methods for mutating the content of an attributed string. You can add and remove characters (raw strings) and attributes separately or together as attributed strings. See the class description for [NSAttributedString](nsattributedstring.md) for more information about attributed strings.

`NSMutableAttributedString` adds two primitive methods to those of `NSAttributedString`. These primitive methods provide the basis for all the other methods in its class. The primitive [- replaceCharactersInRange:withString:](<nsmutableattributedstring/replacecharacters(in_with_)-6oq9r.md>) method replaces a range of characters with those from a string, leaving all attribute information outside that range intact. The primitive [- setAttributes:range:](<nsmutableattributedstring/setattributes(__range_).md>) method sets attributes and values for a given range of characters, replacing any previous attributes and values for that range.

In macOS, AppKit also uses [NSParagraphStyle](../appkit/nsparagraphstyle.md) and its subclass [NSMutableParagraphStyle](../appkit/nsmutableparagraphstyle.md) to encapsulate the paragraph or ruler attributes used by the `NSAttributedString` classes.

Note that the default font for `NSAttributedString` objects is Helvetica 12-point, which may differ from the macOS system font, so you may wish to create the string with non-default attributes suitable for your application using, for example, [- initWithString:attributes:](<nsattributedstring/init(string_attributes_).md>).

> [!note] iOS Note
> In iOS, this class is used primarily in conjunction with the Core Text framework.

`NSMutableAttributedString` is “toll-free bridged” with its Core Foundation counterpart, [CFMutableAttributedString](../corefoundation/cfmutableattributedstring.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

## Relationships

- **Inherits From**: [NSAttributedString](nsattributedstring.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Retrieving Character Information

- [mutableString](nsmutableattributedstring/mutablestring.md) — The character contents of the receiver as a mutable string object.

### Changing Characters

- [- replaceCharactersInRange:withString:](<nsmutableattributedstring/replacecharacters(in_with_)-6oq9r.md>) — Replaces the characters in the given range with the characters of the given string.
- [- deleteCharactersInRange:](<nsmutableattributedstring/deletecharacters(in_).md>) — Deletes the characters in the given range along with their associated attributes.

### Changing Attributes

- [- setAttributes:range:](<nsmutableattributedstring/setattributes(__range_).md>) — Sets the attributes for the characters in the specified range to the specified attributes.
- [- addAttribute:value:range:](<nsmutableattributedstring/addattribute(__value_range_).md>) — Adds an attribute with the given name and value to the characters in the specified range.
- [- addAttributes:range:](<nsmutableattributedstring/addattributes(__range_).md>) — Adds the given collection of attributes to the characters in the specified range.
- [- removeAttribute:range:](<nsmutableattributedstring/removeattribute(__range_).md>) — Removes the named attribute from the characters in the specified range.
- [- applyFontTraits:range:](<nsmutableattributedstring/applyfonttraits(__range_).md>) — Applies the specified font-related attributes to characters in the string.
- [- setAlignment:range:](<nsmutableattributedstring/setalignment(__range_).md>) — Sets the alignment characteristic of the paragraph style attribute for the specified range of text.
- [- setBaseWritingDirection:range:](<nsmutableattributedstring/setbasewritingdirection(__range_).md>) — Sets the base writing direction for the characters to the specified direction.
- [- subscriptRange:](<nsmutableattributedstring/subscriptrange(__).md>) — Decrements the value of the superscript attribute for characters in the specified range by one.
- [- superscriptRange:](<nsmutableattributedstring/superscriptrange(__).md>) — Increments the value of the superscript attribute for characters in the specified range by one.
- [- unscriptRange:](<nsmutableattributedstring/unscriptrange(__).md>) — Removes the superscript attribute from the characters in the specified range.

### Changing Characters and Attributes

- [- appendAttributedString:](<nsmutableattributedstring/append(__).md>) — Adds the characters and attributes of a given attributed string to the end of the receiver.
- [- insertAttributedString:atIndex:](<nsmutableattributedstring/insert(__at_).md>) — Inserts the characters and attributes of the given attributed string into the receiver at the given index.
- [- replaceCharactersInRange:withAttributedString:](<nsmutableattributedstring/replacecharacters(in_with_)-1uaw7.md>) — Replaces the characters and attributes in a given range with the characters and attributes of the given attributed string.
- [- setAttributedString:](<nsmutableattributedstring/setattributedstring(__).md>) — Replaces the receiver’s entire contents with the characters and attributes of the given attributed string.

### Grouping Changes

- [- beginEditing](<nsmutableattributedstring/beginediting().md>) — Begins the buffering of changes to the string’s characters and attributes.
- [- endEditing](<nsmutableattributedstring/endediting().md>) — Ends the buffering of changes to the string’s characters and attributes.

### Updating Attachment Contents

- [- updateAttachmentsFromPath:](<nsmutableattributedstring/updateattachments(frompath_).md>) — Updates all attachments based on files contained in the RTFD file package at the specified file path.

### Fixing Attributes After Changes

- [- fixAttributesInRange:](<nsmutableattributedstring/fixattributes(in_).md>) — Cleans up font, paragraph style, and attachment attributes within the given range.
- [- fixAttachmentAttributeInRange:](<nsmutableattributedstring/fixattachmentattribute(in_).md>) — Cleans up attachment attributes in the specified range and removes all attachment attributes assigned to characters except the designated attachment character.
- [- fixFontAttributeInRange:](<nsmutableattributedstring/fixfontattribute(in_).md>) — Fixes the font attribute in the specified range and assigns default fonts where appropriate.
- [- fixParagraphStyleAttributeInRange:](<nsmutableattributedstring/fixparagraphstyleattribute(in_).md>) — Fixes the paragraph style attributes in the specified range and assigns a paragraph style to all characters in the paragraph.

### Reading Content

- [- readFromData:options:documentAttributes:error:](<nsmutableattributedstring/read(from_options_documentattributes_)-5mbcx.md>) — Sets the contents of the attributed string using the specified data object`.`
- [- readFromURL:options:documentAttributes:error:](<nsmutableattributedstring/read(from_options_documentattributes_)-54wth.md>) — Sets the contents of attributed string using the contents of the specified file.

### Deprecated

- [- readFromData:options:documentAttributes:](<nsmutableattributedstring/read(from_options_documentattributes_)-967j7.md>) — Sets the contents of the receiver from the specified data object`.` _(deprecated)_
- [- readFromURL:options:documentAttributes:](<nsmutableattributedstring/read(from_options_documentattributes_)-85y1d.md>) — Sets the contents of receiver from the file at the specified URL. _(deprecated)_
- [- readFromFileURL:options:documentAttributes:error:](<nsmutableattributedstring/read(fromfileurl_options_documentattributes_).md>) — Sets the contents of the receiver from the file at the given URL. _(deprecated)_

## See Also

### Strings with Metadata

- [AttributedString](attributedstring.md) — A value type for a string with associated attributes for portions of its text.
- [AttributedSubstring](attributedsubstring.md) — A portion of an attributed string.
- [Attributed String Supporting Types](attributed-string-supporting-types.md) — Types that the attributed string, attributed substring, and helper types extend or conform to, for sharing common functionality.
- [NSAttributedString](nsattributedstring.md) — A string of text that manages data, layout, and stylistic information for ranges of characters to support rendering.
