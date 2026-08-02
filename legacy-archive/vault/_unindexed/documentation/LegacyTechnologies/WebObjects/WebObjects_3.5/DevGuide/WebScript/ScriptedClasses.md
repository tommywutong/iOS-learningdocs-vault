---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/WebScript/ScriptedClasses.html
archived_at: '2026-07-15T07:52:34.287339Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.md) [!Previous Section](Advanced.md)

## Scripted Classes

The syntax for creating a scripted class is very similar to the syntax for creating a class in Objective-C. The instances of a class created in such a manner behave like any other Objective-C object.
To create a scripted class, you specify the class interface in an __@interface...@end__ block and the class implementation in an __@implementation...@end__ block. To ensure the class is loaded properly, the scripted class code should be in its own __.wos__ file. The following example is in a file named __Surfshop.wos__:

```objc
    @interface Surfshop:NSObject {
        id name;
        NSArray *employees;
    }
    @end

    @implementation Surfshop
    - (Surfshop *)initWithName:aName employees:theEmployees {
        name = [aName copy];
        employees = [theEmployees retain];
        return self;
    }
    @end
```


Do not use separate files for the __@interface__ and __@implementation__ blocks. They must both be in the same file.
To use the class, you locate it in the application, load it, and then allocate and initialize instances using the class object. Here's an example:

```
    NSMutableArray *allSurfshops;
    - init {
        id scriptPath;
        id surfshopClass;

        [super init];
        scriptPath = [[[self application] resourceManager]
            pathForResourceNamed:@"Surfshop.wos" inFramework:nil];
        surfshopClass = [[self application]
            scriptedClassWithPath:scriptPath];
        allSurfshops = [NSMutableArray array];
        [allSurfshops addObject:[[[surfshopClass alloc] initWithName:
            "Banana Surfshop" employees:@("John Popp", "Jenna de Rosnay")]
            autorelease]];
        [allSurfshops addObject:[[[surfshopClass alloc] initWithName:
            "Rad Swell" employees:@("Robby Naish", "Nathalie Simon")]
            autorelease]];

        return self;
    }
```

[!Table of Contents](WebScript.md) [!Next Section](Categories.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
