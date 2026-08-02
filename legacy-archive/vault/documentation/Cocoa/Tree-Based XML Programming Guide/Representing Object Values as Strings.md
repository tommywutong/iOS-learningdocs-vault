---
title: Tree-Based XML Programming Guide
apple_id: TP40001269
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/Articles/TransformObjectValues.html
archived_at: '2026-07-15T07:17:04.398325Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Tree-Based XML Programming Guide](Introduction%20to%20Tree-Based%20XML%20Programming%20Guide%20for%20Cocoa.md)


[Next](Handling%20Attributes%20and%20Namespaces.md)[Previous](Modifying%20an%20XML%20Document.md)

# Representing Object Values as Strings

[Changing the Values of Nodes](Modifying%20an%20XML%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenjzfu4tomzwgm) discusses how, through the `setObjectValue:` method of NSXMLNode, you can set the value of an NSXML node to be an Objective-C object other than an NSString. For example, you can set the value of a “date” node to be an NSCalendarDate object derived from a string value such as `“10/31/04”`. With the value as an object, you can easily perform computations, comparisons, and other operations that the object’s class makes possible.

When you request a node to emit its value by sending it a `stringValue` or an `XMLString` message, it must, of course, represent that value as a string. The following sections describe the string representations provided for standard atomic data types and explain how to obtain string representations for custom objects.

The NSXML classes provide canonical string representations for a standard set of atomic data types, each of which is represented by a Foundation object as an object value. For example, if you store an NSCalendarDate as a node’s object value and then send `stringValue` to that node, you get back something like this:

```
2004-06-23T14:31:04
```

The canonical string representations for simple and derived types are defined in the W3C XML Schema Data Types specification ([http://www.w3.org/TR/xmlschema-2/](http://www.w3.org/TR/xmlschema-2/)). Table 1 lists the more important types, along with their associated Foundation class and canonical string representation.

__Table 1__  Canonical string representations of W3C types

| Class | W3C type | Canonical string representation |
| NSNumber | boolean |  |
| NSNumber | decimal | Example: `0.3` Not allowed: other leading or trailing zeroes, “+” sign |
| NSNumber | integer | Examples: `-1`, `0`, `1267896` |
| NSNumber | float | Examples: `-1E4`, `1267.43233E12`, `12`, `INF`, `NaN` |
| NSNumber | double | Examples: `-1E4`, `1267.43233E12`, `12`, `INF`, `NaN` |
| NSCalendarDate | dateTime | Format: _CCYY_`-`_MM_`-`_DD_`T`_hh_`:`_mm_`:`_ss_[`Z`] Example: `2004-10-31T20:15:34` Notes: “T” is date-time separator; optional “Z” indicates Coordinated Universal Time. |
| NSData | base64Binary | Encoded using Base64 Content Transfer Encoding (RFC 2045) |
| NSURL | URI (URL) | A URI as defined by RFC 2396 and amended by RFC 2732 |

These string representations follow the XML Schema canonical form as a result of a design choice, not because the NSXML classes look at the `xsi:`_type_ attribute or pick an output format based on an element’s associated type in the validating schema.

The NSXML classes implement their string representations for the standard W3C types through value transformers—that is, instances of custom subclasses of NSValueTransformer. You can easily create and register value transformers for your own custom objects. You can even override the implementations of the standard value transformers implemented by the NSXML classes.

When requested to render an object value as a string, the NSXML classes scan the global registry of value transformers looking for transformer names in the following format:

- `NSXML` + _Class Name_ + `TransformerName`

For example, if your class was named “MyCustomClass”, the proper transformer name would be “NSXMLMyCustomClassTransformerName”. The NSXML classes extract the class name from the transformer name and use it to identify the object value to transform.

For complete details on creating a custom value transformer, see _[Value Transformer Programming Guide](../Value%20Transformer%20Programming%20Guide/Introduction%20to%20Value%20Transformers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tk2i)_. In summary, you must override the NSValueTransformer class methods `transformedValueClass` and `allowsReverseTransformation` and the instance method `transformedValue`. Listing 1 shows an example of such a transformation for a custom object with a name and a date instance variable.

__Listing 1__  Implementing a value transformer for an object value

```objc
@implementation NSXMLNameDateTransformer

+ (Class)transformedValueClass {
    return [NameDate class];
}

// transformation is oneway
+ (BOOL)allowsReverseTransformation {
    return NO;
}

- (id)transformedValue:(id)value {
    if ( [value isKindOfClass:[NameDate class]] ) {
        NSString *dateStr = [[value date]
            descriptionWithCalendarFormat:@"%Y-%m-%dT%H:%M:%S"];
        NSString *retVal = [NSString stringWithFormat:@"Name: %@ - Date: %@",
            [value name], dateStr];
        return retVal;
    }
    return @"";
}
@end
```

Your application should register the custom value transformer with the NSValueTransformer class as soon as possible. A good place for registration is in an override of the `initialize` class method. To register the value transformer, send a `setValueTransformer:forName:` message to the NSValueTransformer class. Make sure that the transformer name conforms to the requirement for NSXML value transformers. See Listing 2 for an example.

__Listing 2__  Registering the value transformer

```objc
#import “NSXMLNameDateTransformer.h”
+ (void)initialize {
    NSValueTransformer *myTransformer = [[[NSXMLNameDateTransformer alloc]
        init] autorelease];
    [NSValueTransformer setValueTransformer:myTransformer
        forName:@"NSXMLNameDateTransformerName"];
}
```


[Next](Handling%20Attributes%20and%20Namespaces.md)[Previous](Modifying%20an%20XML%20Document.md)

