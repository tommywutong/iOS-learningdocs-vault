---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/WebScript17.html
archived_at: '2026-07-18T01:20:35.919488Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](The%20WebScript%20Language.md) [!Previous Section](WebScript16.md)

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
    [super takeValuesFromRequest:request
inContext:context];
    [self logWithFormat:@"Email address of sender: %@",
        [request emailAddressOfSender]];
}
```


__Note:__  If your category is at the end of a scripted component, you must restart your app each time you change that file.

[!Table of Contents](The%20WebScript%20Language.md) [!Next Section](WebScript18.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
