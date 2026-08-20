---
title: Pasteboard Programming Guide
apple_id: TP40008099
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2010-09-01'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PasteboardGuide106/Articles/pbCustom.html
archived_at: '2026-07-15T07:17:41.390313Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Pasteboard Programming Guide](Introduction.md)


[Next](Integrating%20with%20OS%20X%20v10.5%20and%20Earlier.md)[Previous](Reading%20from%20a%20Pasteboard.md)

# Custom Data

To be used with a pasteboard, an object must conform to the `NSPasteboardWriting` and/or `NSPasteboardReading` protocols. You can make your own custom objects conform to these protocols, or you can use instances of `NSPasteboardItem` to contain custom data.

Any object that you put on a pasteboard must conform to the `NSPasteboardWriting` [protocol](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45); to retrieve an instance of an object from the pasteboard, it must adopt the `NSPasteboardReading` protocol. Several of the common Foundation and Application Kit classes implement both of these protocols, including `NSString`, `NSImage`, `NSURL`, `NSColor`, `NSAttributedString`, and `NSPasteboardItem`.

If you want to be able to write your custom object to a pasteboard, or initialize an instance of your [custom class](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassDefinition.html#//apple_ref/doc/uid/TP40008195-CH6) from a pasteboard, your class must also adopt the corresponding protocol. In some situations, it may be appropriate to use `NSPasteboardItem`.

For the examples that follow, consider a simple model class that represents a bookmark as you might find in a web browser:

```objc
@interface Bookmark : NSObject <NSCoding, NSPasteboardWriting, NSPasteboardReading> {
}
@property (nonatomic, copy) NSString *title;
@property (nonatomic, copy) NSString *notes;
@property (nonatomic, retain) NSDate *date;
@property (nonatomic, retain) NSURL *url;
@property (nonatomic, retain) NSColor *color;
@end
```

Notice that the class adopts the `NSCoding` protocol so that it can be archived and unarchived.

To support writing to a pasteboard, your class must conform to the `NSPasteboardWriting` protocol. It has three methods—one of which is optional—as described below. The pasteboard sends these messages to your object when you add your object to the pasteboard, so that it can determine what types of data it will hold and to get the first data representation of your object. The last method may be invoked additional times if your object provides multiple representations.

__`- (NSArray *)writableTypesForPasteboard:(NSPasteboard *)pasteboard`__: This method returns an array of UTIs for the data types your object can write to the pasteboard.

The order in the array is the order in which the types should be added to the pasteboard—this is important as only the first type is written initially, the others are provided lazily (see [Promised Data](Pasteboard%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcmbrfvjvomjq)).

The method provides the pasteboard argument so that you can return different arrays for different pasteboards. You might, for example, put different data types on the dragging pasteboard than you do on the general pasteboard, or you might put on the same data types but in a different order. You might add to the dragging pasteboard a special representation that indicates the indexes of items being dragged so that they can be reordered.

__`- (NSPasteboardWritingOptions)writingOptionsForType:(NSString *)type pasteboard:(NSPasteboard *)pasteboard`__: This method is optional. It returns the options for writing data of a type to a pasteboard.

The only option currently supported is “promised”. You can use this if you want to customize the behavior—for example, to ensure that one particular type is only promised.

__`- (id)pasteboardPropertyListForType:(NSString *)type`__: This method returns the appropriate property list object representation of your object for the specified type.

In most cases, you just implement the two required methods—`writableTypesForPasteboard:` and `pasteboardPropertyListForType:`.

In the example of the Bookmark class, you could implement `writableTypesForPasteboard:` as follows:

```objc
- (NSArray *)writableTypesForPasteboard:(NSPasteboard *)pasteboard {
    static NSArray *writableTypes = nil;

    if (!writableTypes) {
        writableTypes = [[NSArray alloc] initWithObjects:BOOKMARK_UTI,
    (NSString *)kUTTypeURL, NSPasteboardTypeString, nil];
    }
    return writableTypes;
}
```

This implementation ignores the pasteboard type, however you might choose to return different types for say, a general and for a dragging pasteboard.

You could implement `pasteboardPropertyListForType:` as follows:

```objc
- (id)pasteboardPropertyListForType:(NSString *)type {

    if ([type isEqualToString:BOOKMARK_UTI]) {
        return [NSKeyedArchiver archivedDataWithRootObject:self];
    }

    if ([type isEqualToString:(NSString *)kUTTypeURL]) {
        return [url pasteboardPropertyListForType:(NSString *)kUTTypeURL];
    }

    if ([type isEqualToString:NSPasteboardTypeString]) {
        return [NSString stringWithFormat:@"<a href=\"%@\">%@</a>",
    [url absoluteString], title];
    }

    return nil;
}
```

In the example, the method returns either an `NSData` or an `NSString` object. The pasteboard accepts data values directly, and automatically converts the string to the appropriate data representation. If the method returned any other property list type, the pasteboard would automatically convert it to the appropriate data representation.

To support reading from a pasteboard, your class must conform to the `NSPasteboardReading` protocol. It has three methods, two of which are optional.

__`+ (NSArray *)readableTypesForPasteboard:(NSPasteboard *)pasteboard`__: This _class_ method returns an array of UTIs for the data types your object can read from the pasteboard.

The method provides the pasteboard argument so that you can return for different arrays for different pasteboards. As with reading, you might put different data types on the general pasteboard than you do on the dragging pasteboard, or you might put on the same data types but in a different order.

__`+ (NSPasteboardReadingOptions)readingOptionsForType:(NSString *)type pasteboard:(NSPasteboard *)pasteboard`__: This _class_ method is optional. It allows you to specify the options for reading from a pasteboard.

The options are expressed using a `NSPasteboardReadingOptions` bit field. You can specify that the corresponding data should be read as _one_ of:

- An `NSData` object (`NSPasteboardReadingAsData`)

  This simply returns the pasteboard data as-is.
- A string (`NSPasteboardReadingAsString`)

  The pasteboard data is returned as an instance of `NSString`.
- A property list (`NSPasteboardReadingAsPropertyList`)

  The data on the pasteboard is unserialized as a property list.
- An archive (`NSPasteboardReadingAsKeyedArchive`)

  The data on the pasteboard is treated as a keyed archive.

__`- (id)initWithPasteboardPropertyList:(id)propertyList ofType:(NSString *)type`__: This method is optional. You implement this method if it is possible to initialize an instance of your class using a property list.

__Important:__ This method is optional because: if your implementation of `readableTypesForPasteboard:` returns just a single type, and that type uses the `NSPasteboardReadingAsKeyedArchive` reading option, then `initWithCoder:` is called instead of this method.

The property list object is the `NSData` for that type on the pasteboard, but by specifying an `NSPasteboardReading` option for a type, the data can be automatically retrieved as a string or property list.

In the example of the Bookmark class, you could implement the protocol as follows

First, `readableTypesForPasteboard:` specifies that you can initialize a Bookmark using your own custom type and an URL:

```objc
+ (NSArray *)readableTypesForPasteboard:(NSPasteboard *)pasteboard {

    static NSArray *readableTypes = nil;
    if (!readableTypes) {
        readableTypes = [[NSArray alloc] initWithObjects:BOOKMARK_UTI, (NSString *)kUTTypeURL, nil];
    }
    return readableTypes;
}
```

Next, in this case provide an implementation of `readingOptionsForType:pasteboard:` to specify that if the type is your custom type you only want to treat the data as a keyed archive, and if the type is an URL type then support the same options as `NSURL`.

```objc
+ (NSPasteboardReadingOptions)readingOptionsForType:(NSString *)type pasteboard:(NSPasteboard *)pboard {
    if ([type isEqualToString:BOOKMARK_UTI]) {
        /*
         This means you don't need to implement code for this
         type from initWithPasteboardPropertyList:ofType:
        */
        return NSPasteboardReadingAsKeyedArchive;
    }
    else if ([type isEqualToString: (NSString *)kUTTypeURL]) {
        return [NSURL readingOptionsForType:type pasteboard:pboard];
    }
    return 0;
}
```

Finally, implement [initWithPasteboardPropertyList:ofType:](https://developer.apple.com/documentation/appkit/nspasteboardreading/1528252-initwithpasteboardpropertylist) as follows:

```objc
- (id)initWithPasteboardPropertyList:(id)propertyList ofType:(NSString *)type {

    if (self = [self init]) {
        if ([type isEqualToString:(NSString *)kUTTypeURL]) {
            [url release];
            url = [[NSURL alloc] initWithPasteboardPropertyList:propertyList ofType:type];
            [title release];
            title = [[url absoluteString] retain];
        } else {
            [self release];
            return nil;
        }
    }
    return self;
}
```

Notice two things:

1. The method calls the designated initializer, in this case `init`.
2. The method does not test for the custom Bookmark type. Recall that `readableTypesForPasteboard:` returned just a single type, and that `readingOptionsForType:pasteboard:` specified `NSPasteboardReadingAsKeyedArchive` as the sole reading option; thus for the custom Bookmark type `initWithCoder:` is called instead of `initWithPasteboardPropertyList:ofType:`.

Sometimes you want to write items to the pasteboard but you don’t have a convenient wrapper object, or you may want to provide data in a common format but only on demand. For example, you may want to be able to provide a string as an attributed string, a simple string, or as tabular text, where the tabular text is formatted differently from the simple string (so you can’t just write the attributed string directly to the pasteboard).

For these situations, you can use `NSPasteboardItem` objects. In general, `NSPasteboardItem` objects provide you with fine-grained control over what you might put on the pasteboard. They’re designed to be a temporary objects—they’re only associated with a single pasteboard, and only with one change count, so you shouldn’t maintain them after you’ve created them and put them on the pasteboard.

The following example illustrates how you might use an `NSPasteboardItem` object to create a pasteboard item with three representations—string, attributed string, and tabular text. The data for these representations is promised by a data provider—in this case, `self`. The data provider must conform to the [NSPasteboardItemDataProvider Protocol](https://developer.apple.com/documentation/appkit/nspasteboarditemdataprovider) protocol. In its implementation of [pasteboard:item:provideDataForType:](https://developer.apple.com/documentation/appkit/nspasteboarditemdataprovider/1508503-pasteboard), it generates and returns the data requested.

```
NSPasteboardItem *pasteboardItem = [[NSPasteboardItem alloc] init];
NSArray *types = [[NSArray alloc] initWithObjects:
    [NSPasteboardTypeRTF, NSPasteboardTypeString, NSPasteboardTypeTabularText, nil];
BOOL ok = [pasteboardItem setDataProvider:self forTypes:types];

if (ok) {
    NSPasteboard *pasteboard = [NSPasteboard generalPasteboard];
    [pasteboard clearContents];
    ok = [pasteboard writeObjects:[NSArray arrayWithObject:pasteboardItem]];
}
if (ok) {
    // Maintain the information required to provide the data if requested.
}
```


Suppose there are five items on the pasteboard, two contain TIFF data, two contain RTF data, one contains a private data type. Calling `readObjectsForClasses:options:` with just the `NSImage` class will return an array containing two image objects. Calling with just the `NSAttributedString` class will return an array containing two attributed strings. Calling with both classes (`NSImage` and `NSAttributedString`) will return two image objects and two attributed strings.

Notice that in the previous examples, the count of objects returned is less than the number of items on the pasteboard. Only objects of the requested classes are returned. If you add the `NSPasteboardItem` class to the array, then you will always get back an array that contains the same number of objects as there are items on the pasteboard. Since you provide the elements in the classes array in your preferred order, you should add the `NSPasteboardItem` class to the end of the array.

```
// NSPasteboard *pasteboard = <#Get a pasteboard#>; 
NSArray *classes = [[NSArray alloc] initWithObjects:
                    [NSImage class], [NSAttributedString class], [NSPasteboardItem class], nil];
NSDictionary *options = [NSDictionary dictionary];
NSArray *copiedItems = [pasteboard readObjectsForClasses:classes options:options];
if (copiedItems != nil) {
    // Do something with the contents.
```

In this case, the method will return an array with two images, two attributed strings, and one pasteboard item containing the private data type.

[Next](Integrating%20with%20OS%20X%20v10.5%20and%20Earlier.md)[Previous](Reading%20from%20a%20Pasteboard.md)

