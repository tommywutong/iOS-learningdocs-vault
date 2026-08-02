---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/MachO.html
archived_at: '2026-07-18T02:53:52.463264Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# MachO Changes for Swift

### MachO

Added nlist.init(n_un: nlist.__Unnamed_union_n_un, n_type: UInt8, n_sect: UInt8, n_desc: Int16, n_value: UInt32)Added nlist.n_unAdded nlist_64.init(n_un: nlist_64.__Unnamed_union_n_un, n_type: UInt8, n_sect: UInt8, n_desc: UInt16, n_value: UInt64)Added nlist_64.n_unAdded ranlib.init(ran_un: ranlib.__Unnamed_union_ran_un, ran_off: UInt32)Added ranlib.ran_unModified nlist [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct nlist {     var n_type: UInt8     var n_sect: UInt8     var n_desc: Int16     var n_value: UInt32     init() } ``` |
| To | ``` struct nlist {     struct __Unnamed_union_n_un {         var n_strx: UInt32         init(n_strx n_strx: UInt32)         init()     }     var n_un: nlist.__Unnamed_union_n_un     var n_type: UInt8     var n_sect: UInt8     var n_desc: Int16     var n_value: UInt32     init()     init(n_un n_un: nlist.__Unnamed_union_n_un, n_type n_type: UInt8, n_sect n_sect: UInt8, n_desc n_desc: Int16, n_value n_value: UInt32) } ``` |

Modified nlist_64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct nlist_64 {     var n_type: UInt8     var n_sect: UInt8     var n_desc: UInt16     var n_value: UInt64     init() } ``` |
| To | ``` struct nlist_64 {     struct __Unnamed_union_n_un {         var n_strx: UInt32         init(n_strx n_strx: UInt32)         init()     }     var n_un: nlist_64.__Unnamed_union_n_un     var n_type: UInt8     var n_sect: UInt8     var n_desc: UInt16     var n_value: UInt64     init()     init(n_un n_un: nlist_64.__Unnamed_union_n_un, n_type n_type: UInt8, n_sect n_sect: UInt8, n_desc n_desc: UInt16, n_value n_value: UInt64) } ``` |

Modified ranlib [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ranlib {     var ran_off: UInt32     init() } ``` |
| To | ``` struct ranlib {     struct __Unnamed_union_ran_un {         var ran_strx: UInt32         init(ran_strx ran_strx: UInt32)         init()     }     var ran_un: ranlib.__Unnamed_union_ran_un     var ran_off: UInt32     init()     init(ran_un ran_un: ranlib.__Unnamed_union_ran_un, ran_off ran_off: UInt32) } ``` |

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
