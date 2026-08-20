---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/WebScript/WritingOwnMethods.html
archived_at: '2026-07-15T07:52:36.216284Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.md) [!Previous Section](DeclaringVariables.md)

## Methods

To define a new method, simply put its implementation in the script file. You don't need to declare it ahead of time. For example, this is the definition of a method from the Main component in the Visitors example:

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


In these examples, note the following:

- Type information is optional. When there is no type, __id__ is assumed.

- Explicitly specifying the __id__ type is not allowed:

```objc
    // NO!! This won't work.
    - (id)aMethod:(id)anArg { ... }
```

- A return type of __void__ is not allowed:

```objc
    // This won't work either.
    - (void) aMethod:(NSString *)anArg { ... }
```


Both example methods return a value, stored in __result__. If a method doesn't return a meaningful value, you don't have to include a return statement (and, as stated above, even if a method returns no value you shouldn't declare it as returning __void__).

[!Table of Contents](WebScript.md) [!Next Section](Messaging.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
