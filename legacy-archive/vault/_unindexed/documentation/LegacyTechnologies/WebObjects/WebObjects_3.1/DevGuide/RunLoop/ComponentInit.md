---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/RunLoop/ComponentInit.html
archived_at: '2026-07-15T07:47:27.861207Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](RunLoop.book.md)
[!Previous Section](SessionInit.md)

# Component Initialization

It's common in a component's __init__ method to initialize component variables. For example, the __Department.wos__ script in the EmployeeBook example application uses __init__ to initialize the __departments__ component variable:

```
id departments;
- init {
    id departmentsPath;
    [super init];
    departmentsPath = [WOApp pathForResourceNamed:@"Departments" ofType:@"array"];
    departments = [NSArray arrayWithContentsOfFile:departmentsPath];
    return self;
}
```

The WOComponent class---an abstract class that implements basic component behavior---defines the __init__ method for components and implements it to initialize some basic attributes. When a component object must be generated in a scripted application, WebObjects automatically creates an instance of a special subclass of WOComponent and adds to it the code from the component script. When you send __init__ to __super__ in an component script, you are invoking the __init__ method of the superclass of the instance: WOComponent. You can also subclass WOComponent and override __init__ to perform any necessary initialization. It is more common, however, to implement the __init__ method in a component script.

A component's __init__ method is invoked only when the component must be created. This happens at the start of a transaction _except_ when the component is restored from the page cache as a result of the user backtracking or a request component returning itself as the response page. Even then, __init__ is invoked only in cycles in which the component is participating. Generally, a component participates in a cycle of the request-response loop if:

- It represents the request page---the page associated with the request.
- It represents the response page---the page returned to the server.
- It's nested in either the request or response page.
- It's messaged in any other way during the current cycle.

The __awake__ method is immediately invoked in a component after __init__ and after each time the component is restored from the page cache. Just as in __init__, you can implement a component __awake__ method that initializes component variables. For example, the __Main.wos__ script in the CyberWind application uses __awake__ to initialize the __options__ component variable:

```
- awake {
  options = @("See surfshop information", "Buy a new sailboard");
}
```

You can subclass WOComponent and override __awake__ to perform any necessary initialization, but it is more common to implement the __awake__ method in a component script.

[!Table of Contents](RunLoop.book.md)
[!Next Section](ActionMethods.md)
