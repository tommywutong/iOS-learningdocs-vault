---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/Reuse/SearchPath.html
archived_at: '2026-07-15T07:52:06.283982Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ReuseTOC.md) [!Previous Section](Sharing.md)

# Search Path for Reusable Components

When WebObjects encounters the name of a reusable component at runtime:

```
    NAVCONTROL: NavigationControl {};
```


it must find a WOComponent object to represent the component and then find the component's resources (the HTML template file, image files, and so on).
To find an object to represent the component, WebObjects looks in the runtime system for a subclass of WOComponent (in Java, Component) with the same name as the component ("NavigationControl" in the example above). For compiled reusable components this search should succeed, but for scripted ones it should fail.
Next, WebObjects looks within the application directory for the reusable component's resources. For example, if you manually start an application that resides in <DocRoot>__/WebObjects/MyWOApps/Fortune.woa__, the __Fortune.woa__ directory will be searched.
If WebObjects doesn't find the component there, it assumes that the reusable component is included in a framework. It searches all frameworks that were linked in to the application executable for a component with that name. For example, applications written entirely in WebScript use the default application executable, __WODefaultApp__. This executable is linked to the frameworks __WebObjects.framework__ and __WOExtensions.framework__, so any components defined in either of these two frameworks can be used in a scripted application.

[!Table of Contents](ReuseTOC.md) [!Next Section](Designing.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
