---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.32.html
archived_at: '2026-07-15T08:09:12.363885Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Implementing%20Custom%20Behavior%20for%20Your%20Classes.md) [!](Performing%20Validation.md) [!](Invoking%20Server%20Methods%20Remotely.md)

---

#  Providing Default Values for Newly Inserted Objects

When new objects are created in your application and inserted into the database, it's common to assign default values to some of their properties. For example, you might decide to assign newly created Studio objects a default budget (the budget is the amount a studio is allowed to spend on new movies).

To assign default values to newly created enterprise objects, use the method __awakeFromInsertion__

. This method is automatically invoked right after your enterprise object class creates a new object and inserts it into an EOEditingContext.

The following implementation of __awakeFromInsertion__ in the Studio class sets the default value of the __budget__ property to be one million dollars:

####  Studio.java (server and client)

public void awakeFromInsertion(EOEditingContext ec) {

   super.awakeFromInsertion(ec);

   if (budget() == null)

      setBudget(new BigDecimal("1000000"));
}

When a user clicks the Add Studio button in the StudioManager application, a new record is inserted, with "$1,000,000.00" already displayed as a value in the __budget__ column.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Implementing%20Custom%20Behavior%20for%20Your%20Classes.md) [!](Performing%20Validation.md) [!](Invoking%20Server%20Methods%20Remotely.md)
