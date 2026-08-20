---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/WebScript/Categories.html
archived_at: '2026-07-15T07:52:29.137148Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.md) [!Previous Section](ScriptedClasses.md)

## Categories

A category is a set of methods you add to an existing class. You can add a category to any custom or WebObjects-provided Objective-C class. Because the methods added by the category become part of the class type, you can invoke them on any object of that type within an application. That is, you don't have to instantiate a special subclass.
To create a category, you must implement it within an __@implementation__ block, which is terminated by the __@end__ directive. Place the category name in parentheses after the class name.
The following example is a simple category of WORequest that gets the sender's Internet e-mail address from the request headers ("From" key) and returns it (or "None").

```objc
    @implementation WORequest(RequestUtilities)
    - emailAddressOfSender {
        NSString *address = [self headerForKey:@"From"];
        if (!address) address = @"None";
        return address;
    }
    @end
```


Elsewhere in your WebScript code, you invoke this method on WORequest objects just as you do with any other method of that class. Here's an example:

```
    - takeValuesFromRequest:request inContext:context {
        [super takeValuesFromRequest:request inContext:context];
        [self logWithFormat:@"Email address of sender: %@",
            [request emailAddressOfSender]];
    }
```


The category must be included either at the end of a component's script file (that is, a script file within a __.wo__) or it must be included in a scripted class's stand-alone script file. Do not place categories in the application or session script.

[!Table of Contents](WebScript.md) [!Next Section](NoteToObjCDev.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
