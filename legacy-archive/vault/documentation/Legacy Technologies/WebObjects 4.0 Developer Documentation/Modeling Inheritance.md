---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/EOsII3.html
archived_at: '2026-07-18T01:19:44.319371Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](Advanced%20Enterprise%20Object%20Modeling.md) [!Previous Section](Modeling%20Relationships.md)

# Modeling Inheritance

One of the issues that may arise in designing your enterprise objects-whether you're creating your schema from scratch or working with an existing database-is the modeling of inheritance relationships.
In object-oriented programming, when a subclass inherits from a superclass, the instantiation of the subclass implies that all the superclass' data is available for use by the subclass. When you instantiate objects of a subclass from database data, all database tables that contain the data held in each class (whether subclass or superclass) must be accessed so that the data can be retrieved and put in the appropriate enterprise objects.
Even in the simplest scenario in which there is a one-to-one mapping between a single database table and an enterprise object, the database and the enterprise objects instantiated from its data have no knowledge of each other. Their mapping is determined by an EOModel. Likewise, inheritance relationships between enterprise objects and the mapping of those relationships onto a database are also managed by an EOModel.
__Note:__  Enterprise Objects Framework doesn't support mapping inheritance hierarchies across tables in separate databases. Instead, you can set up groups of objects connected by cross-database relationships, where related objects forward messages to each other.

## Types of Inheritance

Suppose you're designing an application that includes Employee and Customer objects. Employees and customers share certain characteristics, such as a name and address, but they also have specialized characteristics. For example, an employee has a salary and a department, and a customer has account information.
Based on these data requirements, you might design a class hierarchy that has a Person class, and Employee and Customer subclasses. As subclasses of Person, Employee and Customer inherit Person's attributes (name and address), but they also implement attributes and behaviors that are specific to their classes.

!

Figure 27. Class Hierarchy

In addition to designing your class hierarchy, you need to decide how to structure your database so that when objects of the classes are instantiated, the appropriate data is retrieved. Some of the issues you need to weigh in deciding on an approach are:

- Are fetches usually directed at the leaves or the root of the class hierarchy?

When a class hierarchy is mapped onto a relational database, data is accessed in two different ways: By fetching just the leaves (for example, just Employee or Customer), and by fetching at the root (Person) to get instances of all levels of the class hierarchy (Employees and Customers).

- How deep is the class hierarchy?

While deep class hierarchies can be a useful technique in object-oriented programming, you should try to avoid them for enterprise objects. When you attempt to map a deep class hierarchy onto a relational database, the result is likely to be poor performance and a database that's difficult to maintain.

- What is the database storage cost for NULL attributes?
- Will I need to modify my schema on an ongoing basis?
- Will other tools be accessing the database?
- Do I need to use inheritance at all?

The primary consideration in deciding whether to use inheritance is if you'll ever need to perform a deep fetch. In an inheritance hierarchy, fetching just objects of a particular class is a shallow fetch, while fetching all instances of a class and its subclasses is a deep fetch. For example, even if the Objective-C classes for Customer and Employee inherit from Person, if your application never performs a fetch for "all people including Customers and Employees," then there is no need to tell Enterprise Objects Framework about your class hierarchy.
Enterprise Objects Framework supports the three primary approaches for mapping inheritance hierarchies to database tables:

- Vertical mapping
- Horizontal mapping
- One table mapping

These approaches, along with the advantages and disadvantages of each, are discussed in the following sections. None of them represents a perfect solution-which one is appropriate depends on the needs of your application.

## Vertical Mapping

In this approach, each class has a separate table associated with it. There is a Person table, an Employee table, and a Customer table; each table contains only the attributes defined by that class.

!

Figure 28. Vertical Inheritance Mapping

This method of storage directly reflects the class hierarchy. If an object of the Employee class is retrieved, data for the Employee's Person attributes must be fetched along with Employee data. The relationship between Employee and Person is resolved through a join to give Employee access to its Person data. This is also true for Customer.

### Creating an EOModel for Vertical Mapping

Assuming that the entities for each of the participating tables already exist, you do the following to implement vertical mapping in your EOModel:

- Create a to-one relationship from each of the child entities (Employee and Customer) to the parent entity (Person) joining on the primary keys, and set it so it isn't a class property.
- Flatten the Person parent attributes into each child entity (Employee and Customer) setting them as class properties if they are class properties in Person.
- Flatten the Person parent entity's relationships into each child entity (Employee and Customer), setting them as class properties if they are class properties in Person.
- Set the parent entity for each child entity (Employee and Customer) to Person.
- In the Advanced Entity Inspector, set the Person parent entity to be abstract if you won't ever instantiate instances of Person.

### Advantages

With vertical mapping, a subclass can be added at any time without modifying the Person table. Existing subclasses can also be modified without affecting the other classes in the class hierarchy. The primary virtue of this approach is its clean, "normalized" design.

### Disadvantages

Vertical mapping is the least efficient of all of the approaches. Every layer of the class hierarchy requires a join to resolve the relationships. For example, if you want to do a deep fetch from Person, three fetches are performed: a fetch from Employee (with a join to Person), a fetch from Customer (with a join to Person), and a fetch from Person to retrieve all the Person attributes. (If Person is an abstract superclass for which no objects are ever instantiated, the last fetch is not performed.)

## Horizontal Mapping

In this approach, you have separate tables for Employee and Customer that each contain columns for Person. The Employee and Customer tables contain not only their own attributes, but all of the Person attributes as well. If instances of Person exist that are not classified as Employees or Customers, a third table would be required (where Person is _not_ an abstract class). In other words, with horizontal mapping every concrete class has a self-contained database table that contains all of the attributes necessary to instantiate objects of the class.

!

Figure 29. Horizontal Inheritance Mapping

This technique entails the same fetching pattern as vertical mapping, except that no joins are performed.

### Creating an EOModel for Horizontal Mapping

To implement horizontal mapping, you do the following in your EOModel:

- If a Person entity doesn't already exist, create one. (If there isn't a database table exclusively for Persons who aren't Employees or Customers, EOModeler doesn't automatically create an entity for Person.)
- Set Person as the parent entity of Employee and Customer.
- In the Advanced Entity Inspector, set the parent entity to be abstract if you never fetch Person objects that aren't Employees or Customers (you never instantiate instances of Person). Under horizontal mapping, if Person doesn't have its own table, then it's an abstract entity.

Unlike vertical mapping, you don't need to flatten any of Person's attributes into Employee and Customer since they already include all of its attributes.

### Advantages

Similar to vertical mapping, a subclass can be added at any time without modifying other tables. Existing subclasses can also be modified without affecting the other classes in the class hierarchy.
This approach works well for deep class hierarchies, as long as the fetch occurs against the leaves of the class hierarchy (Employee and Customer) rather than against the root (Person). In the case of a deep fetch, it's more efficient than vertical mapping (since no joins are performed). It's the most efficient approach, if you only fetch instances of one leaf subclass at a time.

### Disadvantages

Problems may occur when attributes need to be added to the Person superclass. The number of tables that need to be altered is equal to the number of subclasses-the more subclasses you have, the more effort is required to maintain the superclass. However, if table maintenance happens far less often than fetches, this might be a viable approach for your application.

## Single Table Mapping

In this approach, you put all of the data in one table that contains all superclass and subclass attributes. Each row contains all of the columns for the superclass as well as for all of the subclasses. The attributes that don't apply for each object have NULL values. You fetch an Employee or Customer by using a query that just returns objects of the specified type (the table would probably include a type column to distinguish records of one type from the other).

!

Figure 30. Single Table Mapping

### Creating an EOModel for Single Table Mapping

To implement a single table mapping, you do the following in your EOModel:

- Add Employee and Customer entities to your model. (You can use EOModeler's Create Subclass command for this purpose.)
- Set Person as the parent entity of Employee and Customer.
- In the Advanced Entity Inspector, assign a restricting qualifier to the Employee entity that distinguishes its rows from the rows of other entities. Similarly, assign a restricting qualifier to the Customer entity.
- In the Advanced Entity Inspector, set the Person entity to be abstract if you won't ever instantiate Person instances.

Unlike vertical mapping, you don't need to flatten any of Person's attributes into Employee and Customer since these entities already have all of Person's attributes.
Each sub-entity maps to the same table and contains attributes only for the properties that are relevant for that class.

### Advantages

This approach is faster than the other two methods for deep fetches. Unlike vertical or horizontal mapping, you can retrieve superclass objects with a single fetch, without performing joins. Adding a subclass or modifying the superclass requires changes to just one table.

### Disadvantages

Single table mapping can consume an inordinate amount of space since every row includes columns for every one of the other entities' attributes. This may depend on how your database stores NULLs. Some databases condense NULL values, thereby reducing the storage space needed, but some databases maintain the length of the actual data type of the column regardless of the value stored. Most databases also have limitations on how many columns a table can have (typically this is around 250 columns), which can make it impossible to use single table mapping for a deep class hierarchy that has lots of instance variables.
Also, if you have a lot of data, this approach can actually be less efficient than horizontal mapping since with single table mapping you have to search the entire table to find the rows needed to instantiate objects of a particular type. (Horizontal mapping is only more efficient if your application just fetches one type of leaf object at a time (instances of a particular subclass).

## Data Access Patterns for Inheritance

The following table summarizes how data is fetched in each of the approaches.

|  |  Fetches from Leaves |  Fetches from Root |
|  Vertical Mapping |  1 fetch using join |  n fetches using join |
|  Horizontal Mapping |  1 fetch |  n fetches |
|  Single Table Mapping |  1 fetch |  1 fetch |

```
```


In the table, "n" represents the number of entities involved in a deep fetch. For example, when you perform a deep fetch against Person in the Person, Customer, Employee class hierarchy, n equals 3.

## Fetching and Inheritance

Once you've designed your class hierarchy and set up your EOModel to support that class hierarchy, you can use this information to fetch objects of the desired type. For example, you might want to just fetch Person objects, not Customer or Employee objects-or you might want to fetch all Person objects, including Customers and Employees.
You can control deep versus shallow fetches by using EOFetchSpecification's __setIsDeep__ method (__setIsDeep:__ in Objective-C). This method specifies whether a fetch should include sub-entities of the fetch specification's entity. If this method is set to __true__ (YES in Objective-C), sub-entities are also fetched; if it's set to __false__ (NO), they aren't. EOFetchSpecifications are deep by default.
When multiple entities are mapped to a single database table, you must set a qualifier on each entity to distinguish its rows from the rows of other entities. You can either do this programmatically by using EOEntity method __setRestrictingQualifier__ (__setRestrictingQualifier:__ in Objective-C), or you can directly specify the qualifier in the EOModeler Advanced Entity Inspector. A restricting qualifier maps an entity to a subset of rows in a table. If you're using single table inheritance mapping, you must use a restricting qualifier that identifies objects of the desired type.

## Delegation Hooks for Optimizing Inheritance

EOModelGroup includes delegate methods that you can use to exercise more fine-grained control over inheritance. These include:
relationshipForRow
This method (__entity:relationshipForRow:relationship:__ in Objective-C) is invoked when relationships are instantiated for a newly fetched object. The delegate can use the information in the row to determine which entity the target enterprise object should be associated with, and replace the relationship appropriately.
subEntityForEntity
This method (__subEntityForEntity:primaryKey:isFinal:__ in Objective-C) allows the delegate to fine-tune inheritance by indicating from which sub-entity an object should be fetched based on its primary key. The entity returned must be a sub-entity of the specified entity.
In Objective-C, if the delegate knows that the object should be fetched from the returned entity and not one of its sub-entities, it should set the __isFinal__ argument (a pointer to a BOOL) to YES. (In Java, the object must be fetched from the returned entity; it must be final.)
classForObjectWithGlobalID
This method (__entity:classForObjectWithGlobalID:__ in Objective-C) is also used to fine-tune inheritance. The delegate can use the specified globalID to determine a subclass to be used in place of the one specified in the entity argument.

## Java Limitation With Ambiguous To-One Relationships

In both Java and Objective-C you can have to-many relationships to instances of both leaf and non-leaf subclasses in your class hierarchy. For example, the SoftballTeam entity can have a to-many relationship to Person or just the Employee entity (as in a company only team).
Similarly, you can have to-one relationships to instances of leaf subclasses. For example, the PurchaseOrder entity can have a to-one relationship to the Customer entity.
However, in Java you can _not_ have a to-one relationship to a non-leaf entity, an _ambiguous to-one relationship_, unless you implement a workaround. Ambiguous to-one relationships are not possible in Java because of strong typing in the language. In Objective-C, the class of an instance can be changed after it is instantiated (i.e., from the parent class to the leaf class).
There are two workarounds for Java programmers. You can encode class information in your primary and foreign keys, and implement EOModelGroup's delegate methods as described in ["Delegation Hooks for Optimizing Inheritance"](#apple-gq2dona). If you choose this option, then consider using single table mapping since the table would already contain class information.

The second workaround is to implement the ambiguous to-one relationship as a to-many, similar to dealing with an optional to-one relationship above. ["Use a To-Many Relationship"](Modeling%20Relationships.md#apple-he2tg)

[!Table of Contents](Advanced%20Enterprise%20Object%20Modeling.md) [!Next Section](Designing%20Database-Savvy%20Enterprise%20Objects.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
