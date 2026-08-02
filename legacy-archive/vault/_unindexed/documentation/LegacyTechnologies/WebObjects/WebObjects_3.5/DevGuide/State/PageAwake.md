---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/PageAwake.html
archived_at: '2026-07-15T07:52:16.794256Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](PageCacheSize.md)

### Using awake and sleep

Another way to control the amount of component state that's maintained between cycles is to make use of WOComponent's awake and sleep methods. Unlike WOComponent's init method that's invoked just once in the life of the component, a component's awake and sleep methods are invoked at the beginning and end of any request-response loop that involves the component.
By moving a component's variable initialization routines from its init method to its awake method and implementing a sleep method to release those variables, you can reduce the space requirements for storing a component. For example, the code for DodgeLite's Main component could be changed to:

```
    // rewritten DodgeLite Main.wos
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


Note that in WebScript you set a variable to nil to mark it for release. In Objective-C you send the object a release message:

```
    - sleep {
        [models release];
        [types release];
        [prices release];
    }
```


Of course, what you save in storage by moving variable initialization to the awake method is lost in performance, since these variables will be reinitialized on each cycle of the request-response loop.

[!Table of Contents](StateTOC.md) [!Next Section](PageWithName.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
