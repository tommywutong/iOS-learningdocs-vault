---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/PageAwake.html
archived_at: '2026-07-15T07:47:47.956021Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](PageCacheSize.md)

# Using awake and sleep

Another way to control the amount of component state that's maintained between transactions is to make use of WOComponent's __awake__ and __sleep__ methods. Unlike the component's __init__ method that's invoked just once in the life of the component, a component's __awake__ and __sleep__ methods are invoked at the beginning and end of any request-response loop that involves the component.

By moving a component's variable initialization routines from its __init__ method to its __awake__ method and implementing a __sleep__ method to release those variables, you can reduce the space requirements for storing a component. For example, the code for DodgeLite's Main component that we looked at earlier could be changed to:

```
id models, model, selectedModels;
id prices, price, selectedPrices;
id types, type, selectedTypes;

- awake {
    models = [[WOApp modelsDict] allValues];
    types = [[WOApp typesDict] allValues];
    prices = [WOApp prices];
}

- sleep {
    models = nil;
    types = nil;
    prices = nil;
}
```

Note that in WebScript you set a variable to __nil__ to mark it for release; whereas, in Objective-C you send the object a __release__ message:

```
- sleep {
    [models release];
    [types release];
    [prices release];
}
```

Of course, what you save in storage by moving variable initialization to the __awake__ method is lost in performance since these variables will be reinitialized on each cycle of the request-response loop.

[!Table of Contents](ManagingState.book.md)
[!Next Section](PageWithName.md)
