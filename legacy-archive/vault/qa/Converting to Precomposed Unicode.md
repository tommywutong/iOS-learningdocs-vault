---
title: Converting to Precomposed Unicode
apple_id: DTS10001757
resource_type: QA
platform: iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-09-14'
source_url: https://developer.apple.com/library/archive/qa/qa1235/_index.html
archived_at: '2026-07-18T02:30:12.750702Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1235

# Converting to Precomposed Unicode

## Q:  How do I convert a Unicode string to its precomposed form?

A: Mac OS X and iOS provide a variety of APIs for converting to the various Unicode normal forms. The easiest to use are the NSString methods shown in Table 1.

__Table 1__  NSString normal form methods

| Method | Normal Form Name | Common Name |
| -decomposedStringWithCanonicalMapping | D | decomposed |
| -precomposedStringWithCanonicalMapping | C | precomposed |
| -decomposedStringWithCompatibilityMapping | KD |  |
| -precomposedStringWithCompatibilityMapping | KC |  |

Certain Unicode characters can be encoded in more than one way. For example, an Á (A acute) can be encoded either precomposed, as U+00C1 (LATIN CAPITAL LETTER A WITH ACUTE), or decomposed, as U+0041 U+0301 (LATIN CAPITAL LETTER A followed by a COMBINING ACUTE ACCENT). Precomposed characters are more common in the Windows world, whereas decomposed characters are more common on Apple platforms.

You can find a lot more information about Unicode on the [Unicode consortium web site](http://unicode.org/). Specifically of interest is the Unicode Standard Annex #15 [Unicode Normalization Forms](http://www.unicode.org/reports/tr15/).

When working in our platforms you will find yourself using a mixture of precomposed and decomposed Unicode. For example, HFS Plus converts all file names to decomposed Unicode, while Macintosh keyboards generally produce precomposed Unicode. This isn't a problem as long as you use system-provided APIs to process text. Apple's APIs correctly handle both precomposed and decomposed Unicode.

However, you may need to convert to precomposed Unicode when you interact with other platforms. For example, the following are all valid reasons why you might want to convert to precomposed Unicode:

- If you implement a network protocol which is defined to use precomposed Unicode.
- When creating a cross-platform file (or volume) whose specification dictates precomposed Unicode.
- If you incorporate a large body of cross-platform code into your application, where that code is expecting precomposed Unicode.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-09-14 | Rewritten to focus on modern techniques. |
| 2003-02-07 | New document that describes how to convert a string to precomposed Unicode. |

