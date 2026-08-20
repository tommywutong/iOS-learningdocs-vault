---
title: Searching Directories with PBCatSearch
apple_id: DTS10001191
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-11-01'
source_url: https://developer.apple.com/library/archive/qa/fl/fl05.html
archived_at: '2026-07-18T02:29:28.722251Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > File Management](https://developer.apple.com/referencelibrary/Carbon/idxFileManagement-date.html)

|  |
| --- |
| Technical Q&A FL05Searching Directories with PBCatSearch |

|  |
| --- |
| ---   Q: I need to get a list of files in a particular directory. Should I use PBCatSearch, or should I use indexed `PBGetCatInfo` or `PBGetFInfo` requests?  A: The "Cat" in `PBCatSearch` stands for "Catalog" and that is what `PBCatSearch` searches: the whole volume catalog. You can specify that matches found by `PBCatSearch` be limited to a specific directory by setting the `fsSBFlParID` bit in the `ioSearchBits` field of the parameter block, and then specify the directory to match on by setting `ioFlParID` in `ioSearchInfo1` and `ioSearchInfo2` to the directory ID you're interested in. However, using `PBCatSearch` may not be what you want to use for a couple of reasons:   - The matches `PBCatSearch` finds by matching on `ioFlParID` are only in that one directory -- not from any of that directory's subdirectories. - Because the whole catalog file is searched, this is usually not the fastest way to look through a specific directory's contents.   If you need matches in both the directory \*and\* its subdirectories and you don't want to search the whole volume, there's a routine in the DTS sample code MoreFiles named `IndexedSearch` that is compatible with `PBCatSearch`'s parameter blocks, except that `IndexedSearch` lets you specify what directory you want to search. `IndexedSearch` uses indexed `PBGetCatInfo` calls to search a directory and its subdirectories.  If you only need matches from a single directory (and not from that directory's subdirectories), there's another `MoreFiles` routine named `GetDirItems`. `GetDirItems` uses `PBGetCatInfo` to index through a directory's entries and returns `FSSpecs` to the entries found. In this case, indexed `PBGetCatInfo` calls are much faster than searching the whole catalog with `PBCatSearch`. |

#### [May 01 1995]

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
