---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Concepts/When_Do_You_ject_Class_.html
archived_at: '2026-07-15T08:13:58.364040Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/JavaClient/Images/previous.gif)](What_Is_an_Association_.md)[![Next](attachments/JavaClient/Images/next.gif)](Adding_Beha_ise_Objects.md)

## When Do You Use a Custom Enterprise Object Class?

Enterprise Objects Framework provides a "default" enterprise
object class, EOGenericRecord. An EOGenericRecord can take on values
for any properties defined in your application's model, but it
implements no custom behavior. EOGenericRecord objects can hold
simple values as well as refer to other enterprise objects through relationships
defined in the model.

The criterion for deciding whether to make your enterprise
objects custom classes or to simply use the EOGenericRecord class
is behavior. One of the main reasons to use the Enterprise Objects
Framework is to associate behavior with your persistent data. Behavior is
implemented as methods that "do something" (as opposed to merely
setting or returning the value for a property). Since the Framework
itself handles most of the behavior related to persistent storage,
you can focus on the behavior specific to your application.

Because the Studio and Talent classes need to have specialized
behavior (for example, to perform validation when you attempt to
save changes to the database), they need to be custom classes.

[![Previous](attachments/JavaClient/Images/previous.gif)](What_Is_an_Association_.md)[![Next](attachments/JavaClient/Images/next.gif)](Adding_Beha_ise_Objects.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
