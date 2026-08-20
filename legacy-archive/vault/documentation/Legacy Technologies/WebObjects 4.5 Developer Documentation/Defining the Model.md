---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/EOsI2.html
archived_at: '2026-07-15T08:03:06.870977Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Designing%20Enterprise%20Objects.md) [!Previous Section](Designing%20Your%20Schema.md)

# Defining the Model

The work of writing enterprise objects typically begins in EOModeler. You make the following decisions for your enterprise object in EOModeler:

- Should your enterprise object be an EOGenericRecord or a custom class?
- What database attributes do you want to include as properties in your class?
- What data types should the class properties be?
- What relationships does your enterprise object have with other objects?
- What referential integrity rules should you specify for the relationships in your enterprise object?
- Does your enterprise object class have inheritance relationships with other enterprise object classes?

These issues are discussed in the following sections.

## EOGenericRecord or Custom Class?

Enterprise Objects Framework provides a "default" enterprise object class, EOGenericRecord. An EOGenericRecord can take on values for any properties defined in your application's model (see the section ["Accessing an Enterprise Object's Data"](Implementing%20an%20Enterprise%20Object.md#apple-he2deni) for more discussion of this), but implements no custom behavior. EOGenericRecord objects can hold simple values as well as refer to other enterprise objects through relationships defined in the model.

The criterion for deciding whether to make your enterprise objects custom classes or to simply use the EOGenericRecord class is behavior. One of the main reasons to use the Enterprise Objects Framework is to associate behavior with your persistent data. Behavior is implemented as methods that "do something," as opposed to merely returning the value for a property. Since the Framework itself handles most of the behavior related to persistent storage, you can focus on the behavior specific to your application.
Because the Customer class in the Rentals database has specialized behavior-for example, it rents units-it needs to be a custom class.

## Which Attributes Should Be Class Properties?

By default, EOModeler marks all of the attributes read in from the database as class properties. When an attribute is marked as a class property, it means that the attribute will be included in your class definition when you generate source files for the class, and that it will be fetched and passed to your enterprise object when you create instances from the database.
The attributes you mark as class properties should only be ones whose values are meaningful in the object graph that's created when you fetch objects from the database. Attributes that are essentially database artifacts shouldn't be marked as class properties. For example:

- As a general rule, foreign and primary keys shouldn't be included in your enterprise object as class properties. The only exception to this rule is when the key has meaning to the user (such as a credit card number) and therefore must be displayed in the user interface.
- Relationships that are just used in EOModeler as a vehicle for flattening attributes from another entity shouldn't be included as class properties. For example, suppose an Employee class flattens address properties (__streetAddress__, __city__, and so on) from an Address entity and that Employee includes these flattened attributes as class properties. The relationship from Employee to Address doesn't need to be a class property if it's otherwise not needed. For more discussion of this topic see ["How Should Your Enterprise Object Manage Relationships with Other Objects?"](#apple-gm2dc).
- Relationships that represent an entity's relationship to an intermediate join table (also known as a _correlation_ table) shouldn't be included in your enterprise objects as class properties (unless they contain data that's meaningful in your application).

For example, in the Movie database, the Director table acts as an intermediate table between Movie and Talent and exists purely to define that relationship. It has no data besides its foreign keys. Because of this, you never need to fetch instances of Director into your application. However, it makes sense to specify a relationship between Movie and Director and between Director and Talent, and to flatten that second relationship to give Movie access to the Talent table. The flattened relationship, possibly named __directors__, can then be marked as a class property, because it contains objects that should be included in the object graph.

Although Director contains no data besides its foreign keys, some intermediate tables do. For example, the MovieRole table acts as an intermediate table between Movie and Talent, and it includes the attribute __roleName__. Because of this, it's likely that if your enterprise object had a relationship to MovieRole, you'd want to include that relationship as a class property to be able to access the value of __roleName__.

## What Data Types Should Your Properties Be?

When you create a new model, Enterprise Objects Framework maps external database data types to the following standard value classes:

|  __Java__ |  Objective-C |
|  String |  NSString |
|  BigDecimal (java.math) |  NSDecimalNumber |
|  Number |  NSNumber |
|  NSGregorianDate |  NSCalendarDate |
|  NSData |  NSData |

```
```


Additionally, you can map external data types to custom value classes defined by your application. When you're working with custom data, you'll typically want to convert binary data into a meaningful form. However, since you define its form, you have to convert it yourself. The Framework allows you to define a custom class whose instances are initialized with binary or string data; this prevents your accessor methods from having to explicitly convert the data, and allows other objects to access your enterprise object's property in its intended form rather than as an NSData object. For more discussion of this subject, see the chapter ["Advanced Enterprise Object Modeling"](Advanced%20Enterprise%20Object%20Modeling.md#apple-ge2danbw).

### Working with Numeric Values

There are basically two different choices for representing numeric values in your model:

- Numbers that correspond to money values should be represented in your model as BigDecimals (or NSDecimalNumbers in Objective-C). This is because in the Enterprise Objects Framework, numeric database values are stored in one of two types of objects: Number and its subclasses or BigDecimal (NSNumber or NSDecimalNumber in Objective-C). When you use Number, values are limited to double precision, and operations are inexact. Using BigDecimal provides high precision and smooth conversions between strings, BigDecimals, and money.
- Numbers that represent integer or floating point values in your database should be declared as Number objects (NSNumbers in Objective-C) in your model. You then use the Attribute Inspector to specify the scalar type to which the Number will be coerced. For example, if you're working with scientific data, you should represent it as a Number that will be coerced to a __double__.

### Conversion of Numeric Values

When the Framework passes a Number value (NSNumber in Objective-C) to your object, the value can be converted to the corresponding scalar (numeric) type if your accessor method or instance variable requires it (for more information, see["Accessing an Enterprise Object's Data"](Implementing%20an%20Enterprise%20Object.md#apple-he2deni)). For example, suppose your enterprise object defines these accessor methods:

public void __setAge__(int _age_)
public int __age__

For the __setAge__ method, the Number value for the "age" key is converted to an __int__ and passed as _age_. Similarly, the return value of the __age__ method is converted to an Number.

## How Should Your Enterprise Object Manage Relationships with Other Objects?

In EOModeler you can specify relationships between entities. For example, in the Rentals database in the on-line examples, the Member entity can have several relationships to other entities, including:

- To-one relationship to Customer
- To-one relationship to CreditCard
- To-many relationship to Guest
- To-many relationship to Rental
- To-many relationship to Fee

You can use relationships to access data in the destination entity from the source entity.
When you include relationships as class properties, to-one relationships are represented as references in the object graph and to-many relationships are represented as NSArrays. You can see this more clearly if you look at the way Customer's to-one relationship to CreditCard and to-many relationship to Rental are represented as instance variables in the Customer class:

```
// Reference to a CreditCard object in the object graph
protected CreditCard creditCard;

// Array of Rental objects
protected NSMutableArray rentals;
```


For the most part, you access the data in other objects by using relationship properties to traverse the in-memory object graph in your running application. For example, the following statement uses Customer's __creditCard__ relationship to access the __authorizationDate__ property in the CreditCard object:

```
date = customer.creditCard().authorizationDate();
```


Likewise, the following statement uses the Customer's __rentals__ relationship to return an NSArray containing a customer's Rental objects:

```
rentalArray = customer.rentals();
```


### Referential Integrity

When your enterprise object has relationships with other objects, you can use EOModeler to define rules to govern those relationships. Each of the rules possible are described briefly in the following sections. For more information on how to set these options, see the book _Enterprise Objects Framework Tools and Techniques_.
Optionality
Optionality refers to whether a relationship is optional or mandatory. For example, you can require all departments to have a location (mandatory), but not require that every employee have a manager (optional).
Delete Rules
This refers to the rules that should be applied to an entity that's involved in a relationship when the source object is deleted. For example, you might have a department with multiple employees. When a user tries to delete the department, you can:

- Delete the department and remove any back reference the employee has to the department (nullify).
- Delete the department and all of the employees it contains (cascade).
- Refuse the deletion if the department contains employees (deny).
- Delete the department but _do not_ remove any back reference the employee has to the department. _Use this option with caution as dangling references may result._

Owns Destination

You can set a source object as owning its destination objects. When a source object owns its destination objects and you remove a destination object from the source object's relationship array, you're also deleting it from the database (alternatively, you can transfer it to a new owner). This is because ownership implies that the owned object can't exist without an owner-for example, line items can't exist outside of a purchase order. By contrast, you might have a department object that doesn't own its employee objects. If you remove an employee from a department's employees array, the employee continues to exist in the database, but its department variable is set to __null__ (or __nil__ in Objective-C). If you really intend to delete the employee from the database, you'd have to do it explicitly.
Propagates Primary Key
You can also specify in EOModeler that the primary key of the source entity should be propagated to newly inserted objects in the destination of the relationship. This is used for a to-one owning relationship, where the owned object has the same primary key as the source. For example, in the Movies database the TalentPhoto entity has the same primary key as the entity that owns it, Talent. In this scenario, if you create a new Talent object and the Talent doesn't already have a TalentPhoto, the Framework automatically creates a TalentPhoto object for you.

### Mapping an Entity Across Multiple Tables

In certain special cases you may decide to use EOModeler to "flatten" attributes from one entity into another. In general you should only flatten attributes across one-to-one relationships (like Employee to Address) where the destination entity is never fetched directly. Otherwise, you run the risk that the values of flattened attributes can get out of sync with the most current view of data in your application.
Some examples of good uses of flattened attributes are as follows:

- Combining multiple tables to form a logical unit.

For example, you might have employee data that's spread across multiple tables such as Address, Benefits, and so on. If you have no need to access these tables individually (that is, if you'd never create an Address object since the address data is always subsumed in Employee), then it makes sense to flatten attributes from those entities into Employee.

- Implementing vertical inheritance mapping.

For example, the Member class in the RentalsInheritance model has two flattened attributes: __firstName__ and __lastName__. It flattens these attributes from the Customer entity. Customer is a parent entity of Member and Guest that provides attributes common to both. Because Customer is an abstract entity and is therefore never instantiated in the object graph, the only way to access Customer's data is to flatten the appropriate attributes into its sub-entities. The relationship between Member, Guest, and Customer is an example of vertical inheritance mapping-for more discussion of this topic, see the chapter ["Advanced Enterprise Object Modeling"](Advanced%20Enterprise%20Object%20Modeling.md#apple-ge2danbw).

- If your application (or the property in question) is read-only.

When you use flattened attributes, you don't need to include the relationship as a class property-there's no need to since the data it would be used to access is already included in the source entity.
For more discussion of this topic, see the book _Enterprise Objects Framework Tools and Techniques_.

## What about Inheritance?

You can use the Advanced Entity Inspector in EOModeler to specify an entity's parent entity. For example, the Customer entity is a parent to both Member and Guest in the RentalsInheritance model. For more discussion of the different approaches you can use for inheritance, see the chapter["Advanced Enterprise Object Modeling"](Advanced%20Enterprise%20Object%20Modeling.md#apple-ge2danbw).

[!Table of Contents](Designing%20Enterprise%20Objects.md) [!Next Section](Implementing%20an%20Enterprise%20Object.md)
