---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.31.html
archived_at: '2026-07-15T08:09:12.339810Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Implementing%20Custom%20Behavior%20for%20Your%20Classes.md) [!](Writing%20Derived%20Methods.md) [!](Providing%20Default%20Values%20for%20Newly%20Inserted%20Objects.md)

---

#  Performing  Validation

Another element you'll likely want to add to your enterprise object classes is validation. For example, suppose that when a studio buys a new movie, you want to check to make sure that acquiring the movie won't cause the studio to exceed its budget. You could implement a method in the Studio class like the following:

####  Studio.java (server and client)

public void validateBudget(Number budget) throws
   EOValidation.Exception {
   if (budget.intValue() < 100) {
      throw new EOValidation.Exception
         ("A budget cannot be less than $100");
   }
}

Now when a studio buys more movies than it can afford, a panel displaying the message "A budget cannot be less than $100" appears when the user attempts to save the changes to the database.

Validation methods must be of the form __validate___Attribute_. The __validateBudget__ method is invoked by the __validateValueForKey__ method, which is part of the EOValidation interface that uses the EOClassDescription class to provide default implementations of validation methods. These methods are invoked automatically by framework components such as EODisplayGroup and EOEditingContext. They are:

- 

  validateValueForKey
- 

  validateForSave
- 

  validateForDelete
- 

  validateForInsert
- 

  validateForUpdate

For more discussion of this topic, see the chapter "Designing Enterprise Objects" in the Enterprise Objects Framework Developer's Guide and the NSObject Additions class specification in the Enterprise Objects Framework Reference.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Implementing%20Custom%20Behavior%20for%20Your%20Classes.md) [!](Writing%20Derived%20Methods.md) [!](Providing%20Default%20Values%20for%20Newly%20Inserted%20Objects.md)
