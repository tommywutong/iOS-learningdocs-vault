---
title: How do I work-around an issue where some lines in my Core Text output have
  extra line spacing?
apple_id: DTS40010203
resource_type: QA
platform: iOS
topic: Data Management
technology: null
published: '2010-07-26'
source_url: https://developer.apple.com/library/archive/qa/qa1698/_index.html
archived_at: '2026-07-18T02:34:12.213675Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1698

# How do I work-around an issue where some lines in my Core Text output have extra line spacing?

## Q:  How do I work-around an issue where some lines in my Core Text output on iPhone OS devices have extra line spacing?

A: You may be encountering situations where text that you have rendered using Core Text on iPhone OS devices running iPhone OS 3.2 result in some lines in a given paragraph drawn with a small amount of extra space between lines. This is most often visible on the last line of a multi-line paragraph.

This is caused by a known problem where fractional line height information is getting accumulated over multiple lines, which eventually results in slightly larger line heights. The work-around is to specify that Core Text not use fractional heights for lines.

You can specify this by using the `kCTParagraphStyleSpecifierMinimumLineHeight` and `kCTParagraphStyleSpecifierMaximumLineHeight` paragraph styles with a non-fractional line height, and setting these attributes on your text's attributed string. An example of this is given in Listing 1.

__Listing 1__  Forcing use of non-fractional heights for lines.

```
 CGFloat lineHeight = 15;

    CTParagraphStyleSetting settings[] = {
        { kCTParagraphStyleSpecifierMinimumLineHeight, sizeof(lineHeight), &lineHeight },
        { kCTParagraphStyleSpecifierMaximumLineHeight, sizeof(lineHeight), &lineHeight },
    };

    CTParagraphStyleRef paragraphStyle = CTParagraphStyleCreate(settings, sizeof(settings) / sizeof(settings[0]));

    NSDictionary * attrs = [[NSDictionary alloc] initWithObjectsAndKeys:
                            (id)font,
                            kCTFontAttributeName,
                            paragraphStyle,
                            kCTParagraphStyleAttributeName,
                            nil];

    // Add attribute dictionary for paragraph text range onto your NSMutableAttributedString
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-07-26 | New document that describes how to work-around an issue with Core Text output where some lines in a paragraph have a small amount of extra space between lines. |

