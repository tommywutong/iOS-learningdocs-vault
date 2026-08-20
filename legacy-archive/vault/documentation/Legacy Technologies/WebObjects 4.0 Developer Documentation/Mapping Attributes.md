---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/More/MappingAttributes.html
archived_at: '2026-07-18T01:28:13.882469Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](Creating%20Attributes.md)
[!](SQL%20Statement%20Formats.md)

---

# Mapping Attributes

---

## Mapping from Database to Objects

Every EOAttribute has an external type, which is the type used by the database to store its associated data, and a Java class used as the type for that data in the client application. The type used by the database is accessed with the [`setExternalType`](../EOAttribute.md#apple-heyta) and [`externalType`](../EOAttribute.md#apple-hazdq) methods. The class type used by the application is accessed with the [`valueClassName`](../EOAttribute.md#apple-he4ta) method. You can map database types to a set of standard value classes, which includes:

- java.lang.String
- java.lang.Number
- java.math.BigDecimal
- NSData
- NSDate

Database-specific adaptors automatically handle value conversions for these classes. You can also create your own custom value class, so long as you define a format that it uses to interpret data. For more information on using EOAttribute methods to work with custom data types, see the next section, "[Working with Custom Data Types](#apple-gm2tomy)."

The handling of dates assumes by default that both the database server and the client application are running in the same, local, time zone. You can alter the server time zone with the [`setServerTimeZone`](../EOAttribute.md#apple-he2dk) method. If you alter the server time zone, the adaptor automatically converts dates as they pass into and out of the server.

---

## Working with Custom Data Types

When you create a new model, EOModeler maps each attribute in your model to one of the primitive data types the adaptor knows how to manipulate: String, Number, java.math.BigDecimal, NSData, and NSDate. For example, suppose you have a `photo` attribute that's stored in the database as a LONG RAW. When you create a new model, this attribute is mapped to NSData. However, NSData is just an object wrapper for binary data-for instance, it doesn't have any methods for operating on images, which would limit what you'd be able to do with the image in your application. This is a case in which you'd probably choose to use a custom data type, such as com.apple.yellow.application.NSImage.

For a custom data type to be usable in Enterprise Objects Framework, it must supply methods for importing and exporting itself as one of the primitive types so that it can be read from and written to the database. Specifically, to use a custom data type you need to do the following:

- Set the attribute's value class using the method [`setValueClassName`](../EOAttribute.md#apple-gqzdaoa).
- Set the factory method that will be used to create instances of your class from raw data using the method [`setValueFactoryMethodName`](../EOAttribute.md#apple-he2tq).
- Set the type of the argument that should be passed to the factory method using the method [`setFactoryMethodArgumentType`](../EOAttribute.md#apple-heyti).
- Set the conversion method that is used to convert your data back into one of the primitive data types the adaptor can work with using the method [`setAdaptorValueConversionMethodName`](../EOAttribute.md#apple-ha4tc); this enables the data to be stored in the database.

If an EOAttribute represents a binary column in the database, the factory method argument type can be either EOFactoryMethodArgumentIsNSData or EOFactoryMethodArgumentIsBytes, indicating that the method takes an NSData object or raw bytes as an argument. If the EOAttribute represents a string or character column, the factory method argument type can be either EOFactoryMethodArgumentIsNSString or EOFactoryMethodArgumentIsBytes, indicating that the method takes a String object or raw bytes as an argument. These types apply when fetching custom values.

Instead of setting the class information programmatically, you can use the Attributes Inspector in EOModeler, which is more common. For more information, see the chapter "Advanced Modeling Techniques" in the _Enterprise Objects Framework Developer's Guide_.

---

### Fetching Custom Values

Custom values are created during fetching in EOAdaptorChannel's [`fetchRow`](../EOAdaptorChannel.md#apple-gyztsni) method. This method fetchesdata in the external (server) type and converts it to a value object, applying the custom value factory method ([`valueFactoryMethod`](../EOAttribute.md#apple-he4tk)) to convert a value into the custom class if necessary. Once the value is converted, the EOAdaptorChannel puts it into the dictionary for the row being fetched.

---

### Converting Custom Values

Custom values are converted back to binary or character data in EOAdaptorChannel's [`evaluateExpression`](../EOAdaptorChannel.md#apple-geydaoi) method. For each value in the EOSQLExpression to be evaluated, the EOAdaptorChannel sends the appropriate EOAttribute an [`adaptorValueByConvertingAttributeValue`](../EOAttribute.md#apple-guydkny) message to convert it. If the value is any of the standard value classes, it's returned unchanged. If the value is of a custom class, though, it's converted by applying the conversion method ([`adaptorValueConversionMethod`](../EOAttribute.md#apple-guydama)) specified in the EOAttribute.

****

---

[!](Creating%20Attributes.md)
[!](SQL%20Statement%20Formats.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
