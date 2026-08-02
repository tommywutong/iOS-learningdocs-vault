---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/EOsII4.html
archived_at: '2026-07-15T08:03:14.984713Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Advanced%20Enterprise%20Object%20Modeling.md) [!Previous Section](Modeling%20Inheritance.md)

# Designing Database-Savvy Enterprise Objects

The main function of a class object is to act as a factory for its instances, so a class method is a natural place to implement custom instantiation. When instances are initialized with data fetched from a database, why not implement common database queries in the class object as creation methods? For example, a video rental store application based on the sample Rentals database might have a requirement to fetch all overdue rentals. To fulfill this requirement, you could write a Rental class method such as the following that fetches all its overdue instances:
In Java:

```
public static NSArray overdueRentalsWithEditingContext(
    EOEditingContext ec)
{
    NSGregorianDate today = new NSGregorianDate();
    EOQualifier qualifer = new EOKeyValueQualifier(
        "dueDate",
        EOQualifier.QualifierOperatorLessThan,
        today);
    EOFetchSpecification fetchSpec = new
EOFetchSpecification(
        @"Rental",
        qualifer,
        null);

    return ec.objectsWithFetchSpecification(fetchSpec);
}
```


In Objective-C:

```objc
+ (NSArray *)
    overdueRentalsWithEditingContext:(EOEditingContext
*)ec
{
    NSCalendarDate *today = [NSCalendarDate calendarDate];
    EOQualifier *qualifer =
        [EOQualifier qualifierWithQualifierFormat:
            @"dueDate < %@",
            today];
    EOFetchSpecification *fetchSpec =
        [EOFetchSpecification
            fetchSpecificationWithEntityName:@"Rental"
            qualifier:qualifer sortOrderings:nil];

    return [ec objectsWithFetchSpecification:fetchSpec];
}
```


You would then invoke the method as follows:
In Java:

```
rentalArray =
Rental.overdueRentalsWithEditingContext(ec);
```


In Objective-C:

```
rentalArray = [Rental
overdueRentalsWithEditingContext:ec];
```


Note that __overdueRentalsWithEditingContext__ takes an EOEditingContext as an argument. This is because enterprise objects are fetched into a particular EOEditingContext. An EOEditingContext establishes a single, internally consistent "object view" of the database, and an enterprise object in one editing context shouldn't have references to enterprise objects in another one. Consequently, methods that fetch enterprise objects must fetch them using the correct EOEditingContext.
Because a class object is global, its static methods (class methods in Objective-C) can be invoked from anywhere in an application. Thus, a class method that returns enterprise objects fetched from the database needs to receive the correct EOEditingContext as an argument.
__Note:__  While the Rental class in this example closely resembles the Rental class for the sample Rentals database, __dueDate__ has been added here to simplify the qualifier for fetching overdue rentals. The Rental class for the sample Rentals database doesn't have a __dueDate__ attribute.
[!Table of Contents](Advanced%20Enterprise%20Object%20Modeling.md) [!Next Section](Application%20Configurations.md)
