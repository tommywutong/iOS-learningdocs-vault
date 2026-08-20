---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/Foundation/ArrayIntro.html
archived_at: '2026-07-15T07:51:35.259981Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](FoundationTOC.md) [!Previous Section](StringMethods.md)

# Working With Arrays

NSArray and NSMutableArray objects manage immutable and mutable collections of objects, respectively. Each has the following attributes:

- A count of the number of objects in the array
- The objects contained in the array

The difference between NSArray and NSMutableArray is that you can't add to or remove from an NSArray's initial collection of objects. That is, insertion and deletion methods provided for NSMutableArrays are not available for NSArrays. Although their use is limited to managing static collections of objects, it is best to use NSArrays wherever possible.
You can create NSArrays with WebScript's @ syntax for defining constant objects. For example, the following statements create NSArrays:

```
    id availableQuantities = @(1, 6, 12, 48);
    id shortWeekDays = @("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat");
```


You can also create NSArrays with creation methods. If you want to create a static array that contains variables, you have to use a creation method because you can't use variables in WebScript's @ syntax. The following statement creates an NSArray that contains variables:

```
    id dinnerPreferences = [NSArray arrayWithObjects:firstChoice,
        secondChoice, nil];
```


The variable __dinnerPreferences__ is an NSArray, so its initial collection of objects can't be added to or subtracted from. When you need to create an array that can be modified, use a creation method to create an NSMutableArray. For example, the following statement creates an empty NSMutableArray to which you can add objects:

```
    id mutableArray = [NSMutableArray array];
```


The methods provided by NSArray and NSMutableArray are described in more detail in the next section.

[!Table of Contents](FoundationTOC.md) [!Next Section](ArrayMethods.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
