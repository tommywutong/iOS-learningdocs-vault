---
title: File System Overview
apple_id: 10000185i
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFileSystem/Articles/SortingRules.html
archived_at: '2026-07-15T08:15:35.427125Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Overview](Introduction%20to%20the%20File%20System%20Overview.md)


[Next](File%20System%20Guidelines.md)[Previous](Files%20and%20the%20Finder.md)

# Sorting Rules

Mac OS X provides many ways for users to sort and organize documents using the Finder, including by name, by size, by modification date, and so on. Mac OS X sorting is based on the Unicode Collation Algorithm (Technical Standard UTS #10) defined by the Unicode Consortium. This standard provides a complete and unambiguous sort ordering for all Unicode characters and is available on the Unicode Consortium website ([http://www.unicode.org](http://www.unicode.org/)).

The Finder in Mac OS X takes advantage of some sanctioned ways for altering the default sorting behavior defined by the Unicode standard. In particular, the Finder supports the following sorting rules:

- Punctuation and symbols are significant for sorting.
- Digit sub-strings are sorted by numeric value rather than as characters.
- Case is insignificant.

[Next](File%20System%20Guidelines.md)[Previous](Files%20and%20the%20Finder.md)

