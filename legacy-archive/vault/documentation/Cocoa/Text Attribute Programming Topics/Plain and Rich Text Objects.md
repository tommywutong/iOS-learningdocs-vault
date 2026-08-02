---
title: Text Attribute Programming Topics
apple_id: 10000088i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2004-02-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextAttributes/PlainRichText.html
archived_at: '2026-07-15T07:20:07.373926Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Attribute Programming Topics](Introduction%20to%20Text%20Attributes.md)


[Next](RTF%20Files%20and%20Attributed%20Strings.md)[Previous](Changing%20an%20Attributed%20String.md)

# Plain and Rich Text Objects

Text objects such as NSText and NSTextView can contain either plain text or rich text. Plain text objects allow only one set of text attributes for all of their text; rich text objects allow multiple fonts, sizes, indents, and other attributes for different sets of characters and paragraphs. You can control whether a text object is plain or rich using the `setRichText:` method. Rich text objects are also capable of allowing the user to drag images and files into them. This behavior is controlled by the `setImportsGraphics:` method.

A rich NSText object can use RTF (Rich Text Format) as an interchange format. Not all RTF control words are supported, however. On input, an NSText object ignores any control word it doesn’t recognize; some of those it can read and interpret it doesn’t write out. Table 1 lists the RTF control words that any text object recognizes. Subclasses may recognize more.

__Table 1__  RTF control words recognized by all text objects

| Control word | Can be written out |
| `\ansi` | yes |
| `\b` | yes |
| `\cb` | yes |
| `\cf` | yes |
| `\colortbl` | yes |
| `\dnn` | yes |
| `\fin` | yes |
| `\fn` | yes |
| `\fonttbl` | yes |
| `\fsn` | yes |
| `\i` | yes |
| `\lin` | yes |
| `\margrn` | yes |
| `\paperwn` | yes |
| `\mac` | no |
| `\margln` | yes |
| `\par` | yes |
| `\pard` | no |
| `\pca` | no |
| `\qc` | yes |
| `\ql` | yes |
| `\qr` | yes |
| `\sn` | no |
| `\tab` | yes |
| `\upn` | yes |

[Next](RTF%20Files%20and%20Attributed%20Strings.md)[Previous](Changing%20an%20Attributed%20String.md)

