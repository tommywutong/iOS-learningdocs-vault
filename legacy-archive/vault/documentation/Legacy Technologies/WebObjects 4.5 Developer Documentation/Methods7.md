---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Methods7.html
archived_at: '2026-07-15T08:05:58.118790Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Common%20Methods.md) [!Previous Section](Initialization%20and%20Deallocation%20Methods.md)

## The Structure of init

The __init__ method must begin with an invocation of super's __init__ method and must end by returning __self__.

```
- init {
        self = [super init];
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

[!Table of Contents](Common%20Methods.md) [!Next Section](Methods8.md)
