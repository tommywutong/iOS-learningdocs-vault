---
title: Text Attribute Programming Topics
apple_id: 10000088i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2004-02-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextAttributes/RTFAndAttrStrings.html
archived_at: '2026-07-15T07:20:07.880517Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Attribute Programming Topics](Introduction%20to%20Text%20Attributes.md)


[Next](Document%20Revision%20History.md)[Previous](Plain%20and%20Rich%20Text%20Objects.md)

# RTF Files and Attributed Strings

Rich Text Format (RTF) is a text formatting language devised by Microsoft Corporation. You can represent character, paragraph, and document format attributes using plain text with interspersed RTF commands, groups, and escape sequences. RTF is widely used as a document interchange format to transfer documents with their formatting information across applications and computing platforms. Apple has extended RTF with custom commands, which are described in this chapter.

The Application Kit’s extensions for [NSAttributedString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/cl/NSAttributedString) add support for reading and writing a number of popular document formats, including RTF and RTFD, as described in Formatted Documents and Attributed Strings in _[Attributed String Programming Guide](../Attributed%20String%20Programming%20Guide/Introduction%20to%20Attributed%20String%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaztm2i)_. Although `NSAttributedString` has convenience methods for reading and writing RTF and RTFD data in particular, those methods have no advantage over the general-purpose methods, and they lack the useful `error:` parameter.

Apple has extended the RTF language to support text attributes and formatting constructs available in the Cocoa text system but not representable with standard RTF. The Apple extensions take the same form as standard RTF commands, groups, and escapes. RTF commands consist of a backslash followed by a string of alphabetic characters (case sensitive) followed by an optional integer parameter value which can be positive or negative. RTF groups begin with a left brace ({), followed by RTF sequences optionally including other groups, closed by a right brace (}). RTF escapes consist of a backslash followed by a special character, such as `\{`, which indicates a literal left brace instead of the beginning of a group.

RTF includes the concept of a _destination_, which is a group containing an RTF command and text possibly to be inserted at a different location in a document, such as a footnote. The escape sequence `\*` indicates that RTF readers that don’t understand the command that follows should ignore the contents of the destination.

Dimensions in RTF are expressed in _twips_—one twip is one twentieth of a point.

Table 1 lists Apple’s RTF extensions for character attributes.

__Table 1__  Character attribute RTF extensions

| RTF Sequence | Description | Parameter(s) |
| \CocoaLigature_N_ | Ligature control | Value of [NSLigatureAttributeName](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1524592-ligature).  0 = no ligatures, 1 = default ligatures, 2 = all ligatures. Default value 1. |
| \expansion_N_ | Expansion factor to be applied to glyphs | 2000 \* value of [NSExpansionAttributeName](https://developer.apple.com/documentation/appkit/nsexpansionattributename) (log of expansion factor).  Default value 0. |
| \obliqueness_N_ | Skew to be applied to glyphs | 2000 \* value of [NSObliquenessAttributeName](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1535353-obliqueness).  0 = no skew. Default value 0. |
| \fsmilli_N_ | A finer specification for font size | 1000 \* font size.  Written in addition to \fs when \fs is not an integral or half-point value; value is overridden by \fs, so this should be written immediately after \fs. Default driven by \fs. |
| \shadx_N_ \shady_N_ | Shadow offset, written in conjunction with \shad | X and Y offsets in twips (0 = no offset).  Defaults are \shadx3 and \shady-3. |
| \shadr_N_ | Shadow blur, written in conjunction with \shad | Blur radius in twips.  0 = no blur. Default value 0. |
| \strikec_N_ | Strikethrough color | Color number.  Default same as foreground text color. |
| \strikestyle_N_ | Strikethrough style, written where \strike, \striked, \strikew are not sufficient | Style and pattern mask, value of [NSObliquenessAttributeName](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1535353-obliqueness).  0 = none; 0x8000 = by word; styles: 1 = single, 2 = thick, 9 = double; patterns: 0x100 = dotted, 0x200 = dash, 0x300 = dash dot, 0x400 = dash dot dot. Default value 0. |
| \strokec_N_ | Stroke color | Color number.  Default same as foreground text color. |
| \strokewidth_N_ | Glyph stroke width, written in conjunction with \outl. | 20 \* stroke width as percentage of font point size.  0 = no stroke. Default value 0. Negative values indicate that glyphs are both stroked and filled; the stroke width is taken from the absolute value of the parameter. |
| \ulstyle_N_ | Underline style, written where the standard \ul commands are not sufficient | Style and pattern mask, value of [NSUnderlineStyleAttributeName](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1524865-underlinestyle).  0 = none; 0x8000 = by word; styles: 1 = single, 2 = thick, 9 = double; patterns: 0x100 = dotted, 0x200 = dash, 0x300 = dash dot, 0x400 = dash dot dot. Default value 0. |
| {{\NeXTGraphic _attachment_ \width_N_ \height_N_} _string_} | Name of attachment file in the same folder as the RTF file (typically packaged within an RTFD document) | The _attachment_ is the attachment file name, encoded in UTF-8 and properly RTF-escaped.  The width and height parameters optionally specify the attachment size in twips. The _string_ is always 0xAC. |
| {{}{\\*\glid_N_ _basestring_}_string_} | Glyph ID for explicitly specified glyphs. (The extra {} pair is necessary to work around an RTF reader bug in OS X version 10.2 and earlier.) | Glyph identifier (parameter to \glid). The _basestring_ is the string the glyph id is intended to override; this attribute is then applied to the specified _string_. Typically _string_ and _basestring_ are the same, although _string_ might contain multiple instances of _basestring_. |
| {{}{\\*\glid_N_ _basestring_\glcol_N_} _string_} | Glyph ID for explicitly specified glyphs | Character identifier (parameter to \glid) and character collection (parameter to \glcol).  Collection IDs: 0 = identity, 1 = Adobe-CNS1, 2 = Adobe-GB1, 3 = Adobe-Japan1, 4 = Adobe-Japan2, 5 = Adobe-Korea. |
| {{}{\\*\glid _basestring_\glnam _glyphname_}_string_} | Glyph ID for explicitly specified glyphs | The _glyphname_ is the glyph name in UTF-8 encoding. |
| \AppleTypeServicesU_N_ | Character shape control | Value of [NSCharacterShapeAttributeName](https://developer.apple.com/documentation/appkit/nscharactershapeattributename).  The value is interpreted as Apple Type Services kCharacterShapeType selector + 1. The value 0 disables this attribute. Default value 0. |

Table 2 lists Apple’s RTF extensions for paragraph attributes.

__Table 2__  Paragraph attribute RTF extensions

| RTF Sequence | Description | Parameter(s) |
| \pardeftab_N_ | Default tab interval for paragraph | Tab interval value in twips. 0 = no tabs other than those explicitly specified. Default value 0. |
| \qnatural | Natural text alignment for paragraph (based on script), written along with \ql | None |
| \slleading_N_ | Paragraph line spacing (NSParagraphStyle lineSpacing method) | Line spacing value in twips. Default value 0. |
| \slmaximum_N_ | Maximum line height (NSParagraphStyle maximumLineHeight method), written along with \sl and if needed \slmult | Maximum line height value in twips. Default value 0, implying no maximum. |
| \slminimum_N_ | Minimum line height (NSParagraphStyle minimumLineHeight method), written along with \sl and if needed \slmult | Minimum line height value in twips. Default value 0. |

Table 3 lists Apple’s RTF extensions for document attributes.

__Table 3__  Document attribute RTF extensions

| RTF Sequence | Description | Parameter(s) |
| \readonlydoc_N_ | Read-only document. This has nothing to do with the file system permissions or ownership of the file; it's just a hint that indicates that the document should be presented in a read-only fashion to the user, if the viewer or editor is capable. | 0 = Not read-only, 1 = read-only. Default value 0. |
| \cocoartf_N_ | Cocoa RTF-writer version number. This is a number used by Apple to indicate the version number of the RTF writer used to write this document. | Incrementing version number. 0 = Not Cocoa writer, 1 = NextStep, 40 = OpenStep, 100 = OS X v10.0, 102 = 10.2. (Other than incrementing the number for future versions, no assumptions should be made as to how the number will change in the future.) Default value 0, although some heuristics are used to recognize pre–OS X documents as such. |
| \viewh_N_ \vieww_N_ | Size of display area (not window or view size) to be used for displaying the document | Display area dimension in twips. Default value unspecified. |

[Next](Document%20Revision%20History.md)[Previous](Plain%20and%20Rich%20Text%20Objects.md)

