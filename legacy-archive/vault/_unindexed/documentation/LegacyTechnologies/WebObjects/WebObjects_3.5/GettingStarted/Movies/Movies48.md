---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies48.html
archived_at: '2026-07-15T07:55:00.848773Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies47.md)

## Adding Custom Behavior to Talent

Now add the __fullName__ method to Talent and bind it to the browser.

- Open __Talent.java__ in Project Builder.

The class file declares instance variables for all of Talent's class properties (__firstName__ and __lastName__) and implements set and get methods for those instance variables.

- Add the method, __fullName__, as follows.

```
public String fullName() { return firstName() + " " + lastName(); }
```


After you save, __fullName__ appears in the object browser of WebObjects Builder as a property of Talent.

- Bind __talent.fullName__ to the browser's __value__ attribute.

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies49.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
