---
title: NSMutableParagraphStyle
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsmutableparagraphstyle
source_url: 'https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsmutableparagraphstyle.json'
content_hash: 'sha256:1369611341205d73'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSMutableParagraphStyle

<sub>Class</sub>

An object for changing the values of the subattributes in a paragraph style attribute.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class NSMutableParagraphStyle
```

## Overview

The [NSMutableParagraphStyle](nsmutableparagraphstyle.md) class adds methods to its superclass, [NSParagraphStyle](nsparagraphstyle.md), for changing the values of the subattributes in a paragraph style attribute. For more information, see [NSParagraphStyle](nsparagraphstyle.md) and [NSAttributedString](../foundation/nsattributedstring.md).

> [!important] Important
> Don’t mutate a paragraph style object after adding it to an attributed string. Doing so can cause your app to crash.

## Relationships

- **Inherits From**: [NSParagraphStyle](nsparagraphstyle.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Setting style information

- [- setParagraphStyle:](<nsmutableparagraphstyle/setparagraphstyle(__).md>) — Replaces the subattributes of the paragraph with those in the specified paragraph style object.
- [alignment](nsmutableparagraphstyle/alignment.md) — The text alignment of the paragraph.
- [firstLineHeadIndent](nsmutableparagraphstyle/firstlineheadindent.md) — The indentation of the first line of the paragraph.
- [headIndent](nsmutableparagraphstyle/headindent.md) — The indentation of the paragraph’s lines other than the first.
- [tailIndent](nsmutableparagraphstyle/tailindent.md) — The trailing indentation of the paragraph.
- [lineHeightMultiple](nsmutableparagraphstyle/lineheightmultiple.md) — The line height multiple.
- [maximumLineHeight](nsmutableparagraphstyle/maximumlineheight.md) — The paragraph’s maximum line height.
- [minimumLineHeight](nsmutableparagraphstyle/minimumlineheight.md) — The paragraph’s minimum line height.
- [lineSpacing](nsmutableparagraphstyle/linespacing.md) — The distance in points between the bottom of one line fragment and the top of the next.
- [paragraphSpacing](nsmutableparagraphstyle/paragraphspacing.md) — The space after the end of the paragraph.
- [paragraphSpacingBefore](nsmutableparagraphstyle/paragraphspacingbefore.md) — The distance between the paragraph’s top and the beginning of its text content.
- [baseWritingDirection](nsmutableparagraphstyle/basewritingdirection.md) — The base writing direction for the paragraph.

### Specifying tab information

- [- addTabStop:](<nsmutableparagraphstyle/addtabstop(__).md>) — Adds the specified tab stop to the paragraph.
- [- removeTabStop:](<nsmutableparagraphstyle/removetabstop(__).md>) — Removes the first text tab with a location and type equal to the specified tab stop.
- [tabStops](nsmutableparagraphstyle/tabstops.md) — The text tab objects that represent the paragraph’s tab stops.
- [defaultTabInterval](nsmutableparagraphstyle/defaulttabinterval.md) — A number used as the document’s default tab spacing.

### Setting text blocks and lists

- [textBlocks](nsmutableparagraphstyle/textblocks.md) — The text blocks that contain the paragraph.
- [textLists](nsmutableparagraphstyle/textlists.md) — The text lists that contain the paragraph.

### Setting line-break information

- [lineBreakMode](nsmutableparagraphstyle/linebreakmode.md) — The mode for breaking lines in the paragraph.
- [lineBreakStrategy](nsmutableparagraphstyle/linebreakstrategy.md) — The strategies that the text system may use to break lines while laying out the paragraph.
- [hyphenationFactor](nsmutableparagraphstyle/hyphenationfactor.md) — The paragraph’s threshold for hyphenation.
- [usesDefaultHyphenation](nsmutableparagraphstyle/usesdefaulthyphenation.md) — A Boolean value that indicates whether the paragraph style uses the system hyphenation settings.
- [tighteningFactorForTruncation](../appkit/nsmutableparagraphstyle/tighteningfactorfortruncation.md) — The threshold for using tightening as an alternative to truncation.
- [allowsDefaultTighteningForTruncation](nsmutableparagraphstyle/allowsdefaulttighteningfortruncation.md) — A Boolean value that indicates whether the system tightens intercharacter spacing before truncating text.

### Setting HTML header level

- [headerLevel](../appkit/nsmutableparagraphstyle/headerlevel.md) — The paragraph’s header level for HTML generation.

## See Also

### Formatting and attributes

- [NSParagraphStyle](nsparagraphstyle.md) — The paragraph or ruler attributes for an attributed string.
- [NSTextTab](nstexttab.md) — A tab in a paragraph.
- [NSTextList](nstextlist.md) — A section of text that forms a single list.
- [Adding tables to attributed strings in UIKit](adding-tables-to-attributed-strings.md) — Create and configure tables in attributed strings and display them in a text view.
