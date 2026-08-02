---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/CommonMethods/ComponentInit.html
archived_at: '2026-07-15T07:51:15.040326Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](CommonMethods.md) [!Previous Section](SessionInit.md)

## Component Initialization

A component object's __init__ method is invoked when the component object is created. Just how often a particular component object is created depends on whether the application object is caching pages. For more information, see ["WebObjects Viewed Through Its Classes"](../HowWOWorks/HowWOWorks.md). If page caching is turned on (as it is by default), the application object generally creates the component object once and then restores that object from the cache every time it is involved in a user request. If page caching is turned off, the component object is freed at the end of the request-response loop.

__Note:__  The __pageWithName:__ method shown in the section ["Action Methods"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/CommonMethods/ActionsMethods.html#6452) always creates a new component object, even if page caching is turned on.

A component object's __init__ method usually initializes component variables. For example, in the EmployeeBook example, the __Department.wos__ script uses __init__ to initialize the __departments__ component variable:

```
    // WebScript EmployeeBook Department.wos
    id departments;
    - init {
        id departmentsPath;

        [super init];
        departmentsPath = [[self application]
            pathForResourceNamed:@"Departments" ofType:@"array"];
        departments = [NSArray arrayWithContentsOfFile:departmentsPath];
        return self;
    }
```


The component __awake__ method is invoked immediately after the __init__ method and each time the component object is restored from the page cache. Just as in __init__, you can implement an __awake__ method that initializes component variables. For example, in the DodgeDemo application, the __Car.wos__ script uses __awake__ to initialize the __shoppingCart__ component variable:

```
    // WebScript DodgeDemo Car.wos
    - awake {
        shoppingCart = [[self session] shoppingCart];
    }
```


In general, you use __init__ to initialize component instance variables instead of __awake__. The reason is that __init__ is invoked only at component initialization time, whereas __awake__ is potentially invoked much more than that. If, however, you want to minimize the amount of state stored between cycles of the request-response loop, you might choose to initialize component instance variables in __awake__ and then deallocate them in __sleep__ (by setting them to __nil__ in WebScript or __null__ in Java). For more information, see the chapter ["Managing State"](../State/StateTOC.md).

[!Table of Contents](CommonMethods.md) [!Next Section](RequestHandlingMethods.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
