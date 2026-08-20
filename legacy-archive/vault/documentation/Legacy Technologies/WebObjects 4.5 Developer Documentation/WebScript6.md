---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WebScript6.html
archived_at: '2026-07-15T08:06:36.284274Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](The%20WebScript%20Language.md) [!Previous Section](WebScript5.md)

## Methods

To define a new method, simply put its implementation in the script file. You don't need to declare it ahead of time. For example:

```
- recordMe {
    if ([aName length]) {
        [[self application] setLastVisitor:aName];
        [self setAName:@""]; // clear the text field
    }
}
```


Methods can take arguments. To define a method that takes arguments, you place the argument name after a colon (:). For example, the following method takes two arguments. It adds the two arguments together and returns the result:

```
- addFirstValue:firstValue toSecondValue:secondValue {
    id result;
    result = firstValue + secondValue;
    return result;
}
```


The strings that appear to the left of the colons are part of the method name. The method above is named __addFirstValue:toSecondValue:__. It takes two arguments, which it calls __firstValue__ and __secondValue__.
If you want, you can add type information for the return values and parameter values. For example, the following method, __subtractFirstValue:fromSecondValue:__, subtracts one number from another and returns the result:

```objc
- (NSNumber *)subtractFirstValue:(NSNumber *)firstValue
fromSecondValue:(NSNumber *)secondValue {
    NSNumber *result;
    result = secondValue - firstValue;
    return result;
}
```


In these examples, note that type information is optional. When there is no type, __id__ is assumed. Also note that both example methods return a value, stored in __result__. If a method doesn't return a meaningful value, you don't have to include a return statement (a return value of __nil__ is returned for methods without an explicit return statement).

[!Table of Contents](The%20WebScript%20Language.md) [!Next Section](WebScript7.md)
