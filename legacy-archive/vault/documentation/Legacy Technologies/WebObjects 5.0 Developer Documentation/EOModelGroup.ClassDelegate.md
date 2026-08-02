---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Protocols/EOModelGroupClassDelegate.html
archived_at: '2026-07-15T08:13:42.030551Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EOModelGroup.ClassDelegate

> __(informal interface)__

> **__Package:__**
> : com.webobjects.eoaccess

---

## Interface Description

---

An EOModelGroup object should have a delegate which can influence how it finds and loads models. In addition to the delegates you assign to EOModelGroup instances, the EOModelGroup class itself can have a delegate. The class delegate implements a single method- [defaultModelGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjvxwizlmi5zg65lqfzbwyyltoncgk3dfm5qxizjpmrswmylvnr2e233emvweo4tpovya).

For more information on EOModelGroup instance delegate methods, see the EOModelGroup. Delegate interface specification.

## Instance Methods

---

### defaultModelGroup

`public abstract EOModelGroup defaultModelGroup()`

If implemented by the EOModelGroup class delegate, this method should return the EOModelGroup to be returned in response to the message __defaultModelGroup__. If this delegate method returns `null`, EOModelGroup uses the default behavior of the __defaultModelGroup__ class method. Note that this method is implemented by the delegate assigned to the EOModelGroup class object.

__See Also:__ classDelegate (EOModelGroup class), setClassDelegate (EOModelGroup class)

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
