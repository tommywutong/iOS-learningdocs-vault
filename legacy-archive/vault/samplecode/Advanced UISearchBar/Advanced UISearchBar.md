---
title: Advanced UISearchBar
apple_id: DTS40013493
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2013-07-24'
source_url: https://developer.apple.com/library/archive/samplecode/AdvancedTableSearch/Introduction/Intro.html
archived_at: '2026-07-18T03:00:48.720247Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Advanced UISearchBar

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2013-07-24 "AdvancedTableSearch" demonstrates how to search contents of a table view using UISearchDisplayController. |
| __Build Requirements:__ | iOS 6.0 SDK or later |
| __Runtime Requirements:__ | iOS 6.0 or later, Automatic Reference Counting (ARC) |

"AdvancedTableSearch" demonstrates how to use the UISearchDisplayController object in conjunction with a UISearchBar, effectively filtering in and out the contents of that table. If an iOS application has large amounts of table data, this sample shows how to filter it down to a manageable amount so that users to scroll through less content in a table.
This sample is continuation of the "TableSearch" sample, yet provides a more advanced search algorithm on a more complex data source. Instead of simple string comparisons to filter out search results, this advanced version uses "filteredArrayUsingPredicate" on the NSArray of objects. To perform a search across multiple fields of an NSObject subclass, this sample makes use of compound predicates (NSCompoundPredicate) and NSExpressions to create a more advanced search algorithm.

[Next](ReadMe.txt.md)

