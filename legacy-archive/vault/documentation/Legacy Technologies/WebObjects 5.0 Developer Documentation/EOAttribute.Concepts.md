---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/Concepts/EOAttribute.html
archived_at: '2026-07-15T08:13:38.604681Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Classes/Art/up.gif)](../../EOAccessTOC.md)

# EOAttribute.Concepts

## Creating Attributes

An attribute may be simple, derived, or flattened. A simple attribute typically corresponds to a single column in the database, and may be read or updated directly from or to the database. A simple EOAttribute may also be set as read-only with its setReadOnly method. Read-only attributes of enterprise objects are never updated.

A derived attribute doesn't necessarily correspond to a single database column in its entity's database table, and is usually based on some other attribute, which is modified in some way. For example, if an Employee entity has a simple monthly salary attribute, you can define a derived __annualSalary__ attribute as "salary \* 12". Derived attributes, since they don't correspond to actual values in the database, are read-only; it makes no sense to write a derived value.

A flattened attribute of an entity is actually an attribute of some other entity that's fetched through a relationship with a database join. A flattened attribute's external definition is a data path ending in an attribute name. For example, if the Employee entity has the relationship __toAddress__ and the Address entity has the attribute __street__, you can define __streetName__ as an attribute of your Employee EOEntity by creating an EOAttribute for it with a definition of "toAddress.street".

### Creating a Simple Attribute

A simple attribute needs at least the following characteristics:

- A name unique within its EOEntity
- The name of a column in the database table for its entity (the EOAttribute's external name)
- A declaration of the type of that column as defined by the database and adaptor (the EOAttribute's external type)
- A declaration of the Java class used to represent values outside the context of an enterprise object
- For Java value classes that require it, a subtype for such distinctions as between numeric types

You also have to set whether the attribute is part of its entity's primary key, is a class property, or is used for locking. See the EOEntity class description for more information.

### Creating a Derived Attribute

A derived attribute depends on another attribute, so you base it on a definition including that attribute's name rather than on an external name. Because a derived attribute isn't mapped directly to anything in the database, you shouldn't include it in the entity's set of primary key attributes or attributes used for locking.

### Creating a Flattened Attribute

A flattened attribute depends on a relationship, so you base it on a definition including that relationship's name rather than on an external name. Because a flattened attribute doesn't correspond directly to anything in its entity's table, you don't have to specify an external name, and shouldn't include it in the entity's set of primary key attributes or attributes used for locking.

Instead of flattening attributes in your model, a better approach is often to directly traverse the object graph through relationships.

: 

## Mapping from Database to Objects

Every EOAttribute has an external type, which is the type used by the database to store its associated data, and a Java class used as the type for that data in the client application. The type used by the database is accessed with the setExternalType and externalType methods. The class type used by the application is accessed with the valueClassName method. You can map database types to a set of standard value classes, which includes:

- String
- Number
- java.math.BigDecimal
- NSData
- NSDate

Database-specific adaptors automatically handle value conversions for these classes. You can also create your own custom value class, so long as you define a format that it uses to interpret data. For more information on using EOAttribute methods to work with custom data types, see the next section, ["Working with Custom Data Types"](#apple-ineegq2fijbuk).

The handling of dates assumes by default that both the database server and the client application are running in the same, local, time zone. You can alter the server time zone with the setServerTimeZone method. If you alter the server time zone, the adaptor automatically converts dates as they pass into and out of the server.

## Working with Custom Data Types

When you create a new model, EOModeler maps each attribute in your model to one of the primitive data types the adaptor knows how to manipulate: String, Number, java.math.BigDecimal, NSData, and NSDate. For example, suppose you have a __photo__ attribute that's stored in the database as a LONG RAW. When you create a new model, this attribute is mapped to NSData. However, NSData is just an object wrapper for binary data-for instance, it doesn't have any methods for operating on images, which would limit what you'd be able to do with the image in your application. This is a case in which you'd probably choose to use a custom data type, such as com.apple.cocoa.NSImage.

For a custom data type to be usable in Enterprise Objects Framework, it must supply methods for importing and exporting itself as one of the primitive types so that it can be read from and written to the database. Specifically, to use a custom data type you need to do the following:

- Set the attribute's value class using the method setValueClassName.
- Set the factory method that will be used to create instances of your class from raw data using the method setValueFactoryMethodName.
- Set the type of the argument that should be passed to the factory method using the method setFactoryMethodArgumentType.
- Set the conversion method that is used to convert your data back into one of the primitive data types the adaptor can work with using the method setAdaptorValueConversionMethodName; this enables the data to be stored in the database.

If an EOAttribute represents a binary column in the database, the factory method argument type can be either FactoryMethodArgumentIsData or FactoryMethodArgumentIsBytes, indicating that the method takes an NSData object or raw bytes as an argument. If the EOAttribute represents a string or character column, the factory method argument type can be either FactoryMethodArgumentIsString or `FactoryMethodArgumentIsBytes`, indicating that the method takes a String object or raw bytes as an argument. These types apply when fetching custom values.

Instead of setting the class information programmatically, you can use the Attributes Inspector in EOModeler, which is more common. For more information, see the chapter "Advanced Enterprise Objects Modeling" in the _Enterprise Objects Framework Developer's Guide_.

### Fetching Custom Values

Custom values are created during fetching in EOAdaptorChannel's fetchRow method. This method fetches data in the external (server) type and converts it to a value object, applying the custom value factory method (valueFactoryMethod) to convert a value into the custom class if necessary. Once the value is converted, the EOAdaptorChannel puts it into the dictionary for the row being fetched.

### Converting Custom Values

Custom values are converted back to binary or character data in EOAdaptorChannel's evaluateExpression method. For each value in the EOSQLExpression to be evaluated, the EOAdaptorChannel sends the appropriate EOAttribute an adaptorValueByConvertingAttributeValue message to convert it. If the value is any of the standard value classes, it's returned unchanged. If the value is of a custom class, though, it's converted by applying the conversion method (adaptorValueConversionMethod) specified in the EOAttribute.

## SQL Statement Formats

In addition to mapping database values to object values, an EOAttribute can alter the way values are selected, inserted, and updated in the database by defining special format strings. These format strings allow a client application to extend its reach right down to the server for certain operations. For example, you might want to view an employee's salary on a yearly basis, without defining a derived attribute as in a previous example. In this case, you could set the salary attribute's SELECT statement format to "salary \* 12" (with setReadFormat) and the INSERT and UPDATE statement formats to "salary / 12" (setWriteFormat). Thus, whenever your application retrieves values for the salary attribute they're multiplied by 12, and when it writes values back to the database they're divided by 12.

Your application can use any legal SQL value expression in a format string, and can even access server-specific features such as functions and stored procedures (see EOEntity's setStoredProcedure method description for more information). Accessing server-specific features can offer your application great flexibility in dealing with its server, but does limit its portability. You're responsible for ensuring that your SQL is well-formed and will be understood by the database server.

Format strings for the setReadFormat and setWriteFormat methods should use "%P" as the substitution character for the value that is being formatted. "%@" will not work. For example:

> ```
> myAttribute.setReadFormat("TO_UPPER(%P)");
> myAttribute.setWriteFormat("TO_LOWER(%P)");
> ```

Instead of setting the read and write formats programmatically, you can set them in EOModeler, which is more common. For more information, see _Enterprise Objects Framework Tools and Techniques_.

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Classes/Art/up.gif)](../../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
