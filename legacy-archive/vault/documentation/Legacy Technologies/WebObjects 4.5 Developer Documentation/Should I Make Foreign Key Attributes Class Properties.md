---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/FAQ7.html
archived_at: '2026-07-15T08:03:18.592457Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Answers%20to%20Common%20Design%20Questions.md) [!Previous Section](How%20Are%20Enterprise%20Objects%20Cleaned%20Up.md)

# Should I Make Foreign Key Attributes Class Properties?

You should _not_ make foreign key attributes class properties. If you need to access a foreign key value (because you want to display it in the user interface, for example), you should access it through the corresponding destination object.
Class properties that are foreign keys can become out of sync with their corresponding destination objects. For example, assume that an Employee class defines a relationship, __department__, to its department and has a class property, __departmentID__, for the corresponding foreign key. Assigning an employee to a new department doesn't update the __departmentID__ property in the employee object until the enterprise object is saved to the database. Thus, __departmentID__ contains the primary key value for the old department while the __department__ relationship points to the new department.
Instead of making the foreign key a class property of an enterprise object, you should implement a method that gets the value from the destination object. For example:
In Java:

```
public Object departmentID() {
    NSDictionary primaryKey =
        EOUtilities.primaryKeyForObject(
            department.editingContext(),
            department);
    return primaryKey.objectForKey("departmentID");
}
```


In Objective-C:

```objc
- (id)departmentID
{
    NSDictionary *primaryKey = [[department editingContext]
        primaryKeyForObject:department];
    return [primaryKey objectForKey:@"departmentID"];
}
```


In the Java implementation, the EOUtilities static method __primaryKeyForObject__ returns the primary key dictionary for the __department__ object. In Objective-C, the method is __primaryKeyForObject:__, which is added to the EOEditingContext description through the EOUtilities category in EOAccess.

[!Table of Contents](Answers%20to%20Common%20Design%20Questions.md) [!Next Section](How%20Do%20I%20Share%20Models%20Across%20Applications.md)
