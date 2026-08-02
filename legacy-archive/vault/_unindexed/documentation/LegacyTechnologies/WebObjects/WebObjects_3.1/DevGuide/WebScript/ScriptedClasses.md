---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/WebScript/ScriptedClasses.html
archived_at: '2026-07-15T07:48:05.913110Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.mif.book.md)
[!Previous Section](Categories.md)

# Scripted Classes

You can create an Objective-C class in a script file, then load that class into your application at run time and generate instances from it. The instances will behave as any other Objective-C object.

As with categories, no typing is permitted. You must specify the class interface in an __@interface...@end__ block and the class implementation in an __@implementation...@end__ block. For the sake of loading, the scripted class code should be in its own ".wos" file. The following example is in a file named __Surfshop.wos__:

```objc
@interface Surfshop:NSObject {
id name;
id employees;
}
@end
@implementation Surfshop
- initWithName:aName employees:theEmployees {
    name = [aName copy];
    employees = [theEmployees retain];
    return self;
}
@end
```

To use the class, you locate it in the application, load it, and then allocate and initialize instances using the class object. For example:

```
id allSurfshops;
- init
{
    id scriptPath;
    id surfshopClass;
    [super init];
    scriptPath = [WOApp pathForResourceNamed:@"Surfshop" ofType:@"wos"];
    surfshopClass = [WOApp scriptedClassWithPath:scriptPath];
    allSurfshops = [NSMutableArray array];
    [allSurfshops addObject:[[[surfshopClass alloc] initWithName:
        "Banana Surfshop" employees:@("John Popp", "Jenna de Rosnay")] autorelease]];
    [allSurfshops addObject:[[[surfshopClass alloc] initWithName:
        "Rad Swell" employees:@("Robby Naish", "Nathalie Simon")] autorelease]];
    return self;
}
```

[!Table of Contents](WebScript.mif.book.md)
[!Next Section](ModernSyntax.md)
