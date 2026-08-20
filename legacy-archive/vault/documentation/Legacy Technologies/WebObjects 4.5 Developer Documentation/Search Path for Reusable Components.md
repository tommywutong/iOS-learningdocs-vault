---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/ReusableComponents8.html
archived_at: '2026-07-15T08:06:06.625711Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Creating%20Reusable%20Components.md) [!Previous Section](Sharing%20Reusable%20Components%20Across%20Applications.md)

# Search Path for Reusable Components

When WebObjects encounters the name of a reusable component at runtime:

```
NAVCONTROL: NavigationControl {};
```


it must find a WOComponent object to represent the component and then find the component's resources (the HTML template file, image files, and so on).
To find an object to represent the component, WebObjects looks in the run-time system for a subclass of WOComponent with the same name as the component ("NavigationControl" in the example above). For compiled reusable components this search should succeed, but for scripted ones it should fail.
Next, WebObjects looks within the application directory for the reusable component's resources. For example, if you manually start an application that resides in __<DocRoot>/WebObjects/MyWOApps/Fortune.woa__, the __Fortune.woa__ directory will be searched.
If WebObjects doesn't find the component there, it assumes that the reusable component is included in a framework. It searches all frameworks that were linked in to the application executable for a component with that name. For example, applications written entirely in WebScript use the default application executable, __WODefaultApp__. This executable is linked to the frameworks __WebObjects.framework__ and __WOExtensions.framework__; any components defined in WOExtensions can be used in a scripted application.

[!Table of Contents](Creating%20Reusable%20Components.md) [!Next Section](Designing%20for%20Reusability.md)
