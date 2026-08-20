---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WebScript16.html
archived_at: '2026-07-15T08:06:29.696955Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](The%20WebScript%20Language.md) [!Previous Section](Advanced%20WebScript.md)

## Scripted Classes

The syntax for creating a scripted class is very similar to the syntax for creating a class in Objective-C. The instances of a class created in such a manner behave like any other Objective-C object.
To create a scripted class, you specify the class interface in an __@interface...@end__ block and the class implementation in an __@implementation...@end__ block. To ensure the class is loaded properly, the scripted class code should be in its own __.wos__ file, with the class name matching the filename. The following example is in a file named __Surfshop.wos__:

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
        pathForResourceNamed:@"Surfshop.wos"
inFramework:nil
        languages:nil];
    surfshopClass = [[self application]
        scriptedClassWithPath:scriptPath];
    allSurfshops = [NSMutableArray array];
    [allSurfshops addObject:[[[surfshopClass alloc]
initWithName:
        "Banana Surfshop" employees:@("John Popp", "Jenna de
Rosnay")]
        autorelease]];
    [allSurfshops addObject:[[[surfshopClass alloc]
initWithName:
        "Rad Swell" employees:@("Robby Naish", "Nathalie
Simon")]
        autorelease]];

    return self;
}
```

[!Table of Contents](The%20WebScript%20Language.md) [!Next Section](WebScript17.md)
