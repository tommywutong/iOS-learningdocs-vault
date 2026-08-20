---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Reuse/SearchPath.html
archived_at: '2026-07-15T07:47:22.344236Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Reuse.book.md)
[!Previous Section](Synchronize.md)

# Search Path for Reusable Components

When WebObjects encounters the name of a reusable component at run time:

```
NAVCONTROL: NavigationControl {};
```

it must find a WOComponent object to represent the component and then find the component's resources (HTML template file, image files, etc.).

To find an object to represent the component, WebObjects looks in the Objective-C run time for a subclass of WOComponent with the same name as the component ("NavigationControl" in the example above). For compiled reusable components this search should succeed, but for scripted ones it should fail. For scripted components, WebObjects provides its own private subclass of WOComponent.

Next, WebObjects looks withinthe application directory for the reusable component's resources. For example, if you manually start an application that resides in ___Doc_Root_/WebObjects/MyWOApps/Fortune.woa__, the __Fortune.woa__ directory will be searched.

WebObjects pages and reusable components can be located in subdirectories within the application directory. For example, assuming you use different navigation controls for different parts of your application, you might specify the navigation control for your application's catalog pages as:

```
NAVCONTROL: CatalogPages/ReusableComponents/NavigationControl {};
```

This causes WebObjects to search the application directory's __CatalogPages/ReusableComponents__ subdirectory for the NavigationControl's resources. You'll find that grouping reusable components within subdirectories like this helps keep your application directories organized.

[!Table of Contents](Reuse.book.md)
[!Next Section](Designing.md)
