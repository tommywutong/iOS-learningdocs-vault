---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/EOsII1.html
archived_at: '2026-07-18T01:19:40.311616Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](Advanced%20Enterprise%20Object%20Modeling.md) [!Previous Section](Advanced%20Enterprise%20Object%20Modeling.md)

# Modeling Complex Attributes

When you create a new model, EOModeler provides a default mapping from external database data types to one of the primitive value classes:

|  Java |  Objective-C |
|  String |  NSString |
|  BigDecimal (java.math) |  NSDecimalNumber |
|  Number |  NSNumber |
|  NSGregorianDate |  NSCalendarDate |
|  NSData |  NSData |

```
```


For example, in Oracle, VARCHAR columns are mapped to Strings, DATE columns are mapped to NSGregorianDates, and so on. The default mapping is appropriate for most data types, but you have to customize the mapping for attributes with special requirements.
For example, suppose you have a __photo__ attribute that's stored in the database as a LONG RAW (an Oracle data type). When you create a new model, this attribute is mapped to an NSData. However, NSData is just an object-oriented wrapper for binary data-it doesn't have any methods for operating on images, which limits what you'd be able to do with the image in your application. So, for example, in an Application Kit application, you could customize the default behavior and map __photo__ to an NSImage instead.
This section describes how to work with complex attributes such as RTF text, images, and custom data types. Of these attributes, RTF text is the easiest to handle. You don't have to change the default mapping at all, but you have to use special interface objects to display the RTF text.
For images and custom data types, you must customize the default mapping to map to a "non-primitive" class. To map to an existing class (such as NSImage for image attributes), you simply specify additional mapping information in EOModeler. You do the same work in EOModeler to use a custom class. However, you must also provide methods for translating instances of your class to instances of the primitive value classes.

## RTF Text

RTF text is one type of data that is commonly stored in NSDatas. In the database, store RTF data in a binary data type such as Oracle's LONG RAW; and in your enterprise object, store it in an NSData instance variable. EOModeler automatically maps binary data types to NSData, so the default mapping is correct for RTF attributes.

!

Figure 21. Model Settings for an RTF Text Attribute

For Application Kit applications, Enterprise Objects Framework provides the EOTextAssociation class that extracts RTF text from an NSData object and displays it in an NSTextView object. To display an RTF text attribute in an Application Kit user interface, use Interface Builder to make a connection from a text object to your EODisplayGroup.
__Note:__  Click in the text area to select the NSTextView before you control-drag to form the association. Unless the cursor is in the text area, control-dragging from the text area forms a connection from the text's super view, an NSScrollView. To be sure that the NSTextView is selected, open the inspector and check that it's displaying the NSTextView Inspector.
You probably wouldn't use RTF-formatted text in a WebObjects of Java client application. If you have RTF-formatted text that you want to use in a web application, the best approach is probably to filter the text to another format (such as plain text or HTML) before displaying it in a web page.

## Images

You can store image data in a binary data type (for example, LONG RAW in Oracle or image in Sybase) in the database. Alternatively, you can store the path name to an image file in the file system. This second approach is often times more practical for web applications.
When you store image data in the database itself, Enterprise Objects Framework initially maps it to an NSData object. Depending on the type of application you're writing-WebObjects or Application Kit -you can leave the image as an NSData, or you can further map the NSData to an NSImage object.
Image data formats (EPS, BMP, and GIF, for example) are usually different for WebObjects and Application Kit applications. In a WebObjects application, you generally work with GIF and JPEG images; whereas Application Kit applications typically use EPS, TIFF, and BMP images.
There are numerous techniques for displaying images in a WebObjects application, so how you display them is up to you. (For more information, see the "_Dynamic Elements Reference_" in the WebObjects documentation set.) However, most of the approaches use binary image data, so it's customary to model image attributes as NSDatas when you're designing an enterprise object for use in a web application. If you store images in a binary column in the database, you can then simply use EOModeler's default mapping.
In an Application Kit application, model an enterprise object's image as an NSImage. In the EOModeler's Attribute Inspector:

- Set the Internal Data Type pop-up list to Custom.
- In the Class field, specify NSImage as the custom class.
- In the Factory Method field, specify __imageWithData:__ as the method to use to create NSImage instances.
- In the Conversion Method field, specify __TIFFRepresentation__ as the method to use to convert NSImages into a form that can be stored in the database.
- Set the Init Argument pop-up list to NSData, indicating that the argument to the factory method (__imageWithData:__) is an NSData object.

!

Figure 22. Model Settings for an Image Attribute in an Application Kit Application

To display an image attribute in an Application Kit user interface, make an EOControlAssociation from an NSImageView object to your EODisplayGroup.

## Custom Data Types

In addition to supporting RTF text and image data, Enterprise Objects Framework also provides support for mapping attributes to custom objects. In other words, you can map an attribute to an Objective-C class that you have written-PhoneNumber, for example.
Enterprise Objects Framework maps attributes to a custom object using the same mechanism that it uses to map attributes to NSImages. In EOModeler's Attribute Inspector:

- Set the Internal Data Type pop-up list to Custom.
- If relevant, specify an external width in the External Width field.

Binary data types such as Oracle's LONG RAW don't usually have width constraints. However, string columns such as VARCHARs often do have widths that you should enter.

- In the Class field, specify the name of your custom class.
- In the Factory Method field, specify the method to use to create instances of your class.

This method should have one argument whose type matches the type specified in the Init Argument pop-up list.

- In the Conversion Method field, specify the method to use to convert instances of your class into a form that can be stored in the database.

This method should return an NSData object if the Init Argument type is NSData or Bytes, otherwise it should return an NSString.

- Set the Init Argument pop-up list to indicate the data type (NSData, NSString, or Bytes) for the factory method's argument.

As an example, you might use the settings shown in [Figure 23](#apple-he2te) for a PhoneNumber class.

!

Figure 23. Attribute Settings For a Custom Data Type

Using the mapping information in [Figure 23](#apple-he2te), Enterprise Objects Framework fetches the __phoneNumber__ attribute from the database, maps it to an NSString object, creates a PhoneNumber object using the PhoneNumber class method __phoneNumberWithString:__, and assigns the PhoneNumber object to its enterprise object. Similarly, Enterprise Objects Framework converts the PhoneNumber object to an NSString using the __phoneNumberAsString__ method before saving it to the database.

__Note:__  You can also use a Java custom value class. If you do, set the Factory Method to a static method in your custom class that creates instances. Also, the Init Argument must be set to either NSData or NSString (which is mapped to java.lang.String); it can't be set to bytes.
For more information on using custom data types, see the EOAttribute class specification in the _Enterprise Objects Framework Reference_.

[!Table of Contents](Advanced%20Enterprise%20Object%20Modeling.md) [!Next Section](Modeling%20Relationships.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
