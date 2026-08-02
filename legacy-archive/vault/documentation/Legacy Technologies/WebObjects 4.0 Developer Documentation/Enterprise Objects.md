---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/WhatsEOF7.html
archived_at: '2026-07-18T01:19:55.695792Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](What%20Is%20Enterprise%20Objects%20Framework.md) [!Previous Section](Enterprise%20Objects%20Framework%20Layers.md)

# Enterprise Objects

So far, you've seen the components of an application that Enterprise Objects Framework provides. The component of an application that the Framework doesn't provide-the part that you write-is your application's business logic. Typically you code the bulk of this business logic in enterprise object classes.
An enterprise object is like any other object in that it couples data with the methods for operating on that data. However, an enterprise object class has certain characteristics that distinguish it from other classes:

- It has properties that map to _stored_ or persistent data; an enterprise object instance typically corresponds to a single row or record in a database.
- It knows how to interact with other parts of the Framework to give and receive values for its properties.

Although you write the business logic, the Framework specifies how it gets invoked. In addition to providing classes that manage a graph of enterprise objects in memory, the control layer defines an API to which enterprise objects must conform. So you can concentrate on the parts of your enterprise object classes that are specific to your application, it also provides default implementations of most of this API.
To find out more about writing enterprise object classes, see the chapter ["Designing Enterprise Objects"](Designing%20Enterprise%20Objects.md#apple-ge2daobr).

[!Table of Contents](What%20Is%20Enterprise%20Objects%20Framework.md) [!Next Section](Enterprise%20Objects%20Framework%20Viewed%20Through%20Its%20Classes.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
