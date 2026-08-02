---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/WebScript/Categories.html
archived_at: '2026-07-15T07:47:59.465106Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.mif.book.md)
[!Previous Section](WhatIsSelf.md)

# Categories

Categories are a feature of WebScript borrowed from Objective-C. They allow you to add methods to an existing class without having to create a subclass of that class. The existing class can be a WebObjects public class or any custom or NeXT-provided Objective-C class. The methods added by the category become part of the class type. You can invoke them on any object of that type within an application.

To create a category you must implement it within an __@implementation__ block, which is terminated by the __@end__ directive. The category name appears in parentheses after the class name. Unlike Objective-C categories, no typing of method arguments or return values is allowed. The category can be in any script file of the application.

The following example is a simple category of WORequest that gets the sender's Internet e-mail address from the request headers ("From" key) and returns it (or "None").

```objc
@implementation WORequest(RequestUtilities)
- emailAddressOfSender {
    id address = [self headerForKey:@"From"];
    if (!address) address = @"None";
    return address;
}
@end
```

Elsewhere in your WebScript code, you invoke this method on WORequest objects just as you do with any other method of that class:

```
- takeValuesFromRequest:request inContext:context {
    [super takeValuesFromRequest:request inContext:context];
    [self logWithFormat:@"Email address of sender: %@",
        [request emailAddressOfSender]];
}
```

[!Table of Contents](WebScript.mif.book.md)
[!Next Section](ScriptedClasses.md)
