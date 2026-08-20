---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/CommonMethods/StructureOfInitAwake.html
archived_at: '2026-07-15T07:51:16.994232Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](CommonMethods.md) [!Previous Section](InitializationMethods.md)

## The Structures of init and awake

The __init__ method must begin with an invocation of super's __init__ method and must end by returning __self__.

```
    - init {
        [super init];
        /* initializations go here */
        return self;
    }
```


Likewise, in Java, the constructor must begin with an invocation of the superclass's constructor (as with all Java classes):

```
    public Application() {
        super();
        /* initializations go here */
    }
```


The __awake__ method has no such structure. In it, you don't need to send a message to __super__ or return anything.

```
    - awake {
        /* initializations go here */
    }
    public void awake () {
        /* initializations go here. */
    }
```

[!Table of Contents](CommonMethods.md) [!Next Section](ApplicationInit.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
