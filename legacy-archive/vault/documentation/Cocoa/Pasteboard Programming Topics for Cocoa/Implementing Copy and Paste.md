---
title: Pasteboard Programming Topics for Cocoa
apple_id: 10000068i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2009-01-20'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CopyandPaste/Articles/pbImplementing.html
archived_at: '2026-07-15T07:13:54.450465Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Pasteboard Programming Topics for Cocoa](Introduction%20to%20Pasteboards%20Programming%20Topics.md)


[Next](Named%20Pasteboards.md)[Previous](Pasteboard%20Fundamentals.md)

# Implementing Copy and Paste

This article describes how you can implement copy and paste in your application.

To implement a copy operation you must first tell an `NSPasteboard` object what types of data you want to write, and then you typically write the data, once for each data type. To implement a paste operation, you typically first give the `NSPasteboard` object a list of data types your application can deal with (in your preferred order) and receive back from the pasteboard the identifier for the most preferred type that is actually available. You can then read the data for that type from the pasteboard.

Reading and writing most data types is straightforward, but fonts and RTFD data in particular have some peculiarities—see [Reading and Writing RTFD Data](Reading%20and%20Writing%20RTFD%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgqztelkcineuirkkjfaq) and [Reading and Writing Font Data](Reading%20and%20Writing%20Font%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denjwfvjvomi).

The first step in implementing a copy method is to decide what representations of your data you want to support. If your application has a custom data type that you want the user to be able to copy and paste within your application, then you need to write a representation of that data to the pasteboard. It may be, though, that you also want to allow the user to paste information from your application into other applications, in which case you need to write your data in a standard representation (such as a string) that other applications can deal with.

Consider an application that allows a user to track expenses. You may have a custom Expense class to represent expense items. In a copy operation, you need to write the currently selected Expense object to the pasteboard. If you want the user to be able to paste the information into another application, such as TextEdit or Mail, then you should also write a textual representation of the data to the pasteboard. If you want to support a custom data type, you must define a name for the type as it will appear on the pasteboard, for example:

```
NSString *ExpensePBoardType = @"ExpensePBoardType";
```

Typically this must be a global value, visible to any objects within your application that will copy this data type to or retrieve it from the pasteboard. Often you assign the variable in an implementation file and declare it as an external variable in a header file that you import from other implementation files:

```
extern NSString *ExpensePBoardType;
```

The first step in copying is to tell the pasteboard (for standard copy and paste operations, this is typically the general pasteboard) what representations you will write (using the method, [declareTypes:owner:](https://developer.apple.com/documentation/appkit/nspasteboard/1533561-declaretypes)):

```
NSPasteboard *pb = [NSPasteboard generalPasteboard];
NSArray *types = [NSArray arrayWithObjects:
    ExpensePBoardType, NSStringPboardType, NSRTFPboardType, nil];
[pb declareTypes:types owner:self];
```

The owner is typically `self`, and is used if you support lazy initialization (see [Lazy Writing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denjvfvjvomq)).

You then write the representations to the pasteboard, one at a time. Note that pasteboards support only a limited range of data types, so for custom representations you often need to transform the data into one of the types supported (for example, by archiving an object). In the following example, the Expense class implements custom methods `stringRepresentation` and `rtfRepresentation` to generate a string and RTF representation of the expense respectively.

```
// archive the given expense, and add it to the pasteboard as an Expense
[pb setData:[NSArchiver archivedDataWithRootObject:expense]
    forType:ExpensePBoardType];

// add the string representation
[pb setString:[expense stringRepresentation] forType:NSStringPboardType];

// add the RTF representation
NSAttributedString *rtfDescription = [expense rtfRepresentation];
NSData *rtfData = [rtfDescription
                    RTFFromRange:(NSMakeRange(0, [rtfDescription length]))
                    documentAttributes:nil];
[pb setData:rtfData forType:NSRTFPboardType];
```


To implement paste, you first need to determine what data representations are present on the pasteboard, and in particular find the best one available for the situation. You can do this in a single method call, [availableTypeFromArray:](https://developer.apple.com/documentation/appkit/nspasteboard/1526078-availabletypefromarray). You pass in an array of types you can support, ordered by preference, and get back the identifier for the best match (assuming there is one, otherwise `nil`). For example, if an Expense class provides a method to parse a string to extract attributes for a new Expense object, you might support both your custom type and the string type:

```
NSArray *pasteTypes = [NSArray arrayWithObjects:
    ExpensePBoardType, NSStringPboardType, nil];
NSString *bestType = [pb availableTypeFromArray:pasteTypes];
if (bestType != nil) {
    // pasteboard has data we can deal with
    // ...
```

Often, though, you support paste operations only for your custom types. In some cases, you might also factor out the code that determines whether the pasteboard contains a supported type:

```objc
- (BOOL)pasteboardHasExpense {
    // has the pasteboard got an expense?
    NSPasteboard *pb = [NSPasteboard generalPasteboard];
    NSArray *types = [NSArray arrayWithObject:ExpensePBoardType];
    NSString *bestType = [pb availableTypeFromArray:types];
    return (bestType != nil);
}
```

This is useful if you want to support user interface validation, so that for example the Paste menu item is enabled only if the pasteboard contains a data representation you support:

```objc
- (BOOL)validateUserInterfaceItem:(id <NSValidatedUserInterfaceItem>)item
{
    if ([item action] == @selector(paste:)) {
        return [self pasteboardHasExpense];
    }
    else {
        // ...
```

For more about menu validation, see [Enabling Menu Items](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MenuList/Articles/EnablingMenuItems.html#//apple_ref/doc/uid/20000261) and _[User Interface Validation](../User%20Interface%20Validation/Introduction%20to%20User%20Interface%20Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2da2i)_.

Assuming that the pasteboard does contain a representation that you support, then you retrieve the corresponding data with [dataForType:](https://developer.apple.com/documentation/appkit/nspasteboard/1531810-data).

```
NSData *data = [pb dataForType:ExpensePBoardType];
Expense *expense = [NSUnarchiver unarchiveObjectWithData:data];
```


A cut operation is simply a copy operation followed by a delete operation. In an Expenses application, the `cut:` method might be implemented as follows:

```objc
- (IBAction)cut:(id)sender
{
    [self copy: nil];
    [self deleteSelectedExpense: nil];
}
```


The ability to provide multiple representations of data to the pasteboard is a powerful feature but can result in your application incurring considerably more overhead than is necessary. Consider a bitmap-editing application where you want to support copying of images in a variety of different formats. If in your copy method you had to create each representation, this could require a lot of processing and significant memory overhead—after which the user might decide not to paste anyway. To avoid this situation, `NSPasteboard` supports the technique of lazy writing.

If you use lazy writing, you declare the types you can supply to a pasteboard but you do not set the corresponding data. If data is subsequently requested from a pasteboard in a format that is not present, the pasteboard owner is sent a `pasteboard:provideDataForType:` message asking it to supply the data in that format. The pasteboard owner must obviously keep the original data as long as necessary to fulfill any request. Following this pattern, the copy method in the Expenses application might simply contain:

```
NSPasteboard *pb = [NSPasteboard generalPasteboard];
NSArray *types = [NSArray arrayWithObjects:
    ExpensePBoardType, NSStringPboardType, NSRTFPboardType, nil];
[pb declareTypes:types owner:self];
// cache the item to be copied, in its current state
```

You then implement a `pasteboard:provideDataForType:` method. For the Expenses application, it might look similar to the following:

```objc
- (void)pasteboard:(NSPasteboard *)sender provideDataForType:(NSString *)type
{
    if ([type isEqualToString:ExpensePBoardType]) {
        [sender setData:[NSKeyedArchiver archivedDataWithRootObject:cachedExpense]
            forType:ExpensePBoardType];
    }
    else if ([type isEqualToString:NSStringPboardType]) {
        [sender setString:[cachedExpense stringRepresentation]
                forType:NSStringPboardType];
    }
    else if ([type isEqualToString:NSRTFPboardType]) {
        NSAttributedString *rtfDescription = [cachedExpense rtfRepresentation];
        NSData *rtfData = [rtfDescription
                    RTFFromRange:(NSMakeRange(0, [rtfDescription length]))
                    documentAttributes:nil];
        [sender setData:rtfData forType:NSRTFPboardType];
    }
}
```

The `pasteboard:provideDataForType:` messages may also be sent to the owner when the application is shut down through an application’s `terminate:` method (invoked in response to a Quit command). The user can therefore copy something, quit the application, and still paste the data that was copied.

To ensure you don’t keep the cached data longer than necessary, you also need to know when the user copies something else. If the user performs another copy, the pasteboard owner is sent a [pasteboardChangedOwner:](https://developer.apple.com/documentation/objectivec/nsobject/1532824-pasteboardchangedowner) message.

```objc
- (void)pasteboardChangedOwner:(NSPasteboard *)sender
{
    // remove cached expense
}
```

[Next](Named%20Pasteboards.md)[Previous](Pasteboard%20Fundamentals.md)

