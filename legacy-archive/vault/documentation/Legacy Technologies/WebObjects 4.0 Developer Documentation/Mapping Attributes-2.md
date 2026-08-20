---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/More/MappingAttributes.html
archived_at: '2026-07-18T01:28:23.328640Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](Creating%20Attributes-2.md)
[!](SQL%20Statement%20Formats-2.md)

---

# Mapping Attributes

---

## Mapping from Database to Objects

Every EOAttribute has an external type, which is the type used by the database to store its associated data, and an Objective-C class used as the type for that data in the client application. The type used by the database is accessed with the [`setExternalType:`](../EOAttribute.md#apple-heyta) and [`externalType`](../EOAttribute.md#apple-hazdq) methods. The class type used by the application is accessed with the [`valueClassName`](../EOAttribute.md#apple-he4ta) method. You can map database types to a set of standard value classes, which includes:

- NSString
- NSNumber
- NSDecimalNumber
- NSData
- NSDate

Database-specific adaptors automatically handle value conversions for these classes. You can also create your own custom value class, so long as you define a format that it uses to interpret data. Your value class must also implement the EOCustomClassArchiving protocol to work as a customvalue; see that protocol specification for more information. For more information on using EOAttribute methods to work with custom data types, see the next section, "[Working with Custom Data Types](#apple-gm2tomy)."

The handling of dates assumes by default that both the database server and the client application are running in the same, local, time zone. You can alter the server time zone with the [`setServerTimeZone:`](../EOAttribute.md#apple-he2dk) method. If you alter the server time zone, the adaptor automatically converts dates as they pass into and out of the server.

---

## Working with Custom Data Types

When you create a new model, EOModeler maps each attribute in your model to one of the primitive data types the adaptor knows how to manipulate: NSString, NSNumber, NSDecimalNumber, NSData, and NSDate. For example, suppose you have a `photo` attribute that's stored in the database as a LONG RAW. When you create a new model, this attribute is mapped to NSData. However, NSData is just an object wrapper for binary data-for instance, it doesn't have any methods for operating on images, which would limit what you'd be able to do with the image in your application. This is a case in which you'd probably choose to use a custom data type, such as NSImage.

For a custom data type to be usable in Enterprise Objects Framework, it must supply methods for importing and exporting itself as one of the primitive types so that it can be read from and written to the database. Specifically, to use a custom data type you need to do the following:

- Set the attribute's value class using the method [`setValueClassName:`](../EOAttribute.md#apple-gqzdaoa).
- Set the factory method that will be used to create instances of your class from raw data using the method [`setValueFactoryMethodName:`](../EOAttribute.md#apple-he2tq).
- Set the type of the argument that should be passed to the factory method using the method [`setFactoryMethodArgumentType:`](../EOAttribute.md#apple-heyti).
- Set the conversion method that is used to convert your data back into one of the primitive data types the adaptor can work with using the method [`setAdaptorValueConversionMethodName:`](../EOAttribute.md#apple-ha4tc); this enables the data to be stored in the database.

If an EOAttribute represents a binary column in the database, the factory method argument type can be either [EOFactoryMethodArgumentIsNSData](EOAttribute-2.md#apple-hazte) or EOFactoryMethodArgumentIsBytes, indicating that the method takes an NSData object or raw bytes as an argument. If the EOAttribute represents a string or character column, the factory method argument type can be either EOFactoryMethodArgumentIsNSString or EOFactoryMethodArgumentIsBytes, indicating that the method takes an NSString object or raw bytes as an argument. These types apply when fetching custom values, as described below.

The following code excerpt demonstrates how these methods work together. The example shows two custom data types: an image that's initialized with an NSData, and a custom zip code that's initialized with a string.

> ```
>     [imageAttribute setValueClassName:@"NSImage"];
> ```

> ```
>     [imageAttribute setFactoryMethodArgumentType:EOFactoryMethodArgumentIsNSData];
> ```

> ```
>     [imageAttribute setValueFactoryMethodName:@"imageWithData:"];
> ```

> ```
>     [imageAttribute setAdaptorValueConversionMethodName:@"TIFFRepresentation"];
> ```

> ```
>     [zipCodeAttribute setValueClassName:@"MyZipCodeClass"];
> ```

> ```
>     [zipCodeAttribute setFactoryMethodArgumentType:EOFactoryMethodArgumentIsBytes];
> ```

> ```
>     [zipCodeAttribute setValueFactoryMethodName:@"zipCodeWithBytes:length:"];
> ```

> ```
>     [zipCodeAttribute setAdaptorValueConversionMethodName:@"zipCodeString"];
> ```

Instead of setting the class information programmatically, you can use the Attributes Inspector in EOModeler, which is more common. For more information, see the chapter "Advanced Modeling Techniques" in the _Enterprise Objects Framework Developer's Guide_.

---

### Fetching Custom Values

Custom values are created during fetching in EOAdaptorChannel's [`fetchRowWithZone:`](../EOAdaptorChannel.md#apple-gyztsni) method. This method fetches data in the external (server) type and converts it to a value object. For scalar database types such as numbers and dates, the EOAdaptorChannel converts the value itself. For binary and string database types, it calls upon the EOAttribute being fetched to perform the conversion, into either a standard or custom value class. EOAttribute's methods for performing this conversion are [`newValueForBytes:length:`](../EOAttribute.md#apple-ge3tcnzx) for binary data and [`newValueForBytes:length:encoding:`](../EOAttribute.md#apple-ge3tcobt) for strings. These methods either convert the raw data directly into an NSData or NSString, or apply the custom value factory method to convert it into the custom class. Once the value is converted, the EOAdaptorChannel puts it into the dictionary for the row being fetched.

`newValueForBytes:length:` can handle NSData and raw bytes (`void *`). It converts the raw bytes into an NSData if the custom value argument type is [EOFactoryMethodArgumentIsNSData](EOAttribute-2.md#apple-hazte), then invokes the custom value factory method with the NSData or bytes. If the EOAttribute has no custom value factory method, this method simply returns an NSData object containing the bytes.

`newValueForBytes:length:encoding:` can handle NSString and raw bytes. It converts the raw bytes into an NSString if the custom value argument type is EOFactoryMethodArgumentIsNSString, then it invokes the custom value factory method with the string or bytes. If the EOAttribute has no custom value factory method, this method simply returns an NSString object created from the bytes.

---

### Converting Custom Values

Custom values are converted back to binary or character data in EOAdaptorChannel's [`evaluateExpression:`](../EOAdaptorChannel.md#apple-geydaoi) method. For each value in the EOSQLExpression to be evaluated, the EOAdaptorChannel sends the appropriate EOAttribute an [`adaptorValueByConvertingAttributeValue:`](../EOAttribute.md#apple-guydkny) message to convert it. If the value is any of the standard value classes, it's returned unchanged. If the value is of a custom class, though, it's converted by applying the conversion method ([`adaptorValueConversionMethod`](../EOAttribute.md#apple-guydama)) specified in the EOAttribute.

****

---

[!](Creating%20Attributes-2.md)
[!](SQL%20Statement%20Formats-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
