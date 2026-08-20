---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.44.html
archived_at: '2026-07-15T08:09:16.869458Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Enterprise%20Objects%20Framework%20Concepts.md) [!](What%20is%20an%20Association.md) [!](Adding%20Behavior%20to%20Enterprise%20Objects.md)

---

#   When Do You Use a Custom Enterprise Object Class?

Enterprise Objects Framework provides a "default" enterprise object class, EOGenericRecord. An EOGenericRecord can take on values for any properties defined in your application's model, but it implements no custom behavior. EOGenericRecord objects can hold simple values as well as refer to other enterprise objects through relationships defined in the model.

The criterion for deciding whether to make your enterprise objects custom classes or to simply use the EOGenericRecord class is _behavior_
. One of the main reasons to use the Enterprise Objects Framework is to associate behavior with your persistent data. Behavior is implemented as methods that "do something" (as opposed to merely setting or returning the value for a property). Since the Framework itself handles most of the behavior related to persistent storage, you can focus on the behavior specific to your application.

Because the Studio and Talent classes need to have specialized behavior (for example, to perform validation when you attempt to save changes to the database), they need to be custom classes.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Enterprise%20Objects%20Framework%20Concepts.md) [!](What%20is%20an%20Association.md) [!](Adding%20Behavior%20to%20Enterprise%20Objects.md)
