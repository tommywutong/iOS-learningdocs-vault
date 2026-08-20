---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WORedirect.html
archived_at: '2026-07-15T07:55:31.778445Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WOExtensionsTOC.md) [!Previous Section](WORadioButtonList.md)

## WORedirect

### Synopsis

**__WORedirect__ __{__ __url =__ _aURL___; };__**

### Description

WORedirect is a component that may be returned to force the user's browser to redirect to another URL. You should only return this component as a response to an action method and never use it in an declarations file directly. This component can be useful, for example, if you have an image map with both static and dynamic actions.

### Examples

```objc
- (WOComponent *)someAction
{
    WOComponent *aRedirect = [[self application] pageWithName:@"WORedirect"];
    [aRedirect setURL:@"http://enterprise.apple.com"];
    return aRedirect;
}
```

[!Table of Contents](WOExtensionsTOC.md) [!Next Section](WOSimpleArrayDisplay.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
