---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/FAQ3.html
archived_at: '2026-07-15T08:03:16.639971Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Answers%20to%20Common%20Design%20Questions.md) [!Previous Section](How%20Do%20I%20Generate%20Primary%20Keys.md)

# How Do I Use My Database Server's Integrity-Checking Features?

Most database systems offer features to help you maintain the integrity of your data. You can assign default values to columns, define rules that specify the format or allowable range of a column's values, and define constraints or triggers to enforce relational integrity rules. Enterprise Objects Framework has its own brand of solutions for the same issues. You have to decide whether to use the database system's solution, the Framework's solution, or a combination of the two. The decision involves answering the following questions:

- Can I avoid using the database's integrity-checking features?
- Is it possible that non-Enterprise Objects Framework tools and applications will access the database?
- Can I use the database system's feature without interfering with the way Enterprise Objects Framework works?
- How can I use both the database system's and Enterprise Objects Framework's solutions?

When you implement integrity checking in your Enterprise Objects Framework applications, you can reject erroneous data or illegal operations as soon as a user performs an invalid action. Enterprise Objects Framework relies on application-side integrity checking to provide feedback to users and to handle errors. Without it, it is much more difficult for you to develop the user interfaces for your Enterprise Objects Framework applications.
Because client-side business logic is required to create a highly interactive user interface and because duplication of business logic is inefficient and error-prone, you should try to avoid using database integrity-checking features. Sometimes, however, it's unavoidable. You usually use database integrity checking when users can access a database in many ways (using Enterprise Objects Framework applications, non-Enterprise Objects Framework applications, and interactive SQL sessions, for example). In this case, you may have to use the features of your database server to assure your data's integrity. As a result, you may choose to implement integrity checking in both your Enterprise Objects Framework applications and in the database.
The following sections discuss guidelines for using the
integrity-checking features of your database in concert with an Enterprise Objects Framework application.

## Defaults

Many databases allow you to specify a default value for a column. When a NULL value is inserted (or updated) in a column with a default, the database substitutes the default value for the NULL.
If you define defaults in your database, you should specify the defaults in your Enterprise Objects Framework application as well. Generally, you assign default values in your enterprise object's __awakeFromInsertion__ method (__awakeFromInsertionInEditingContext:__ in Objective-C). For example:
In Java:

```
public void awakeFromInsertion(EOEditingContext ec)
{
    super.awakeFromInsertion(ec);
    // Assign current date to memberSince
    if (memberSince == null)
        memberSince = new NSGregorianDate();
}
```


In Objective-C:

```objc
- (void)
    awakeFromInsertionInEditingContext:(EOEditingContext
*)ec
{
    [super awakeFromInsertionInEditingContext:ec];
    // Assign current date to memberSince
    if (!memberSince)
        memberSince = [[NSCalendarDate date] retain];
}
```


An alternative is to fetch newly inserted objects immediately after you save them to the database. If you don't assign the default values before you save an object and you don't refetch the object from the database after you save, the Framework's object snapshots will not be in sync with the contents of the database. As a result, the Framework may prevent subsequent updates to the object.

## Rules That Validate Values

Many databases allow you to define a rule (or constraint) for a column. A rule can verify that a value is in a proper format or is within an acceptable range. Whenever a value is inserted or updated, the database server verifies that the value conforms to the rule before it performs the operation.
You should implement data validation in your Enterprise Objects Framework application whether or not you use database rules. Depending on the nature of the validation, use a formatter or implement an appropriate __validate...__ method in your enterprise object class. For more information, see the chapter["Designing Enterprise Objects"](Designing%20Enterprise%20Objects.md#apple-ge2daobr).

## Constraints for Enforcing Relational Integrity Rules

Many databases provide mechanisms to enforce relational integrity rules. For example, you can define a constraint (or trigger) that prevents the deletion of a Department that still contains Employees. Enterprise Objects Framework also provides mechanisms for enforcing these types of rules. For example, you can specify delete rules for relationships in EOModeler.
If you use database triggers and constraints, you will have to duplicate the logic in your Enterprise Objects Framework application. In some cases, the duplication won't hurt anything, but in other cases you have to provide special handling to avoid run-time errors.
For example, suppose you have a constraint specifying that you can't delete a department if it still has employees. In addition, you specify the Deny delete rule on the Department entity's __employees__ relationship. When a user attempts to delete a department, Enterprise Objects Framework verifies that the corresponding Department object has no employees. If the department has one or more employees, the Framework doesn't allow the delete.
Further suppose that a user moves all the employees from one department to another, deletes the empty department, then saves all changes. Enterprise Objects Framework analyzes the object graph to determine what operations have taken place. It orders the operations by analyzing the relationships and identifying "master" and "detail" entities. In this example, the Department object, the master, would not be deleted until all the employees are updated to reflect their new department. In most cases, Enterprise Objects Framework just does the "right thing." However, if you discover a sequencing problem with your application, you can customize the order in which database operations are performed. For a complete description of the Framework's default ordering algorithm and how to programmatically reorder operations, see the section["How Do I Order Database Operations?"](How%20Do%20I%20Order%20Database%20Operations.md#apple-geydmoi).

[!Table of Contents](Answers%20to%20Common%20Design%20Questions.md) [!Next Section](How%20Do%20I%20Invoke%20a%20Stored%20Procedure.md)
