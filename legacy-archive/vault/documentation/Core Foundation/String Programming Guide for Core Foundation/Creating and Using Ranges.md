---
title: String Programming Guide for Core Foundation
apple_id: 10000131i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/Articles/UsingRanges.html
archived_at: '2026-07-15T07:22:57.901978Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [String Programming Guide for Core Foundation](Introduction%20to%20Strings%20Programming%20Guide%20for%20Core%20Foundation.md)


[Next](Character%20Sets.md)[Previous](Handling%20External%20Representations%20of%20Strings.md)

# Creating and Using Ranges

Many Core Foundation take ranges—a structure of type `CFRange`—as parameters. A range is a measure of a linear segment; it has a beginning location and a length. To create and initialize this structure you can use the convenience function `CFRangeMake`.

The following code fragment gets the number of subsequent elements in an array that match the first element:

```
CFRange aRange = CFRangeMake(1, CFArrayGetCount(array) - 1);
// Since start is 1, length of remainder of range is count-1
const void *aValue = CFArrayGetValueAtIndex(array, 0);
CFIndex numVals = CFArrayGetCountOfValue(array, aRange, aValue);
```

[Next](Character%20Sets.md)[Previous](Handling%20External%20Representations%20of%20Strings.md)

