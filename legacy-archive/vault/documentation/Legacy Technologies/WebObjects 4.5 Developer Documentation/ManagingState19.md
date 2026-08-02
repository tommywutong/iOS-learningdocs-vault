---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/ManagingState19.html
archived_at: '2026-07-15T08:05:43.584922Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Managing%20State.md) [!Previous Section](ManagingState18.md)

### Using awake and sleep

Another way to control the amount of component state that's maintained between cycles is to make use of WOComponent's __awake__ and __sleep__ methods. Unlike WOComponent's __init__ method that's invoked just once in the life of the component, a component's __awake__ and __sleep__ methods are invoked at the beginning and end of any request-response loop that involves the component.
By moving a component's variable initialization routines from its __init__ method to its __awake__ method and implementing a __sleep__ method to release those variables, you can reduce the space requirements for storing a component. For example, the code shown in the section ["Component Objects and Component State"](ManagingState5.md#apple-gu3tqma) could be changed to:

```
// rewritten Main.wos
id models, model, selectedModels;
id prices, price, selectedPrices;
id types, type, selectedTypes;

- awake {
    anApplication = [WOApplication application];
    models = [[anApplication modelsDict] allValues];
    types = [[anApplication typesDict] allValues];
    prices = [anApplication prices];
}

- sleep {
    models = nil;
    types = nil;
    prices = nil;
}
```


Note that in WebScript you set a variable to __nil__ to mark it for release. In Objective-C you send the object a __release__ message:

```
- sleep {
    [models release];
    models = nil;
    [types release];
    types = nil;
    [prices release];
    prices = nil;
}
```


Of course, what you save in storage by moving variable initialization to the __awake__ method is lost in performance, since these variables will be reinitialized on each cycle of the request-response loop.

[!Table of Contents](Managing%20State.md) [!Next Section](ManagingState20.md)
