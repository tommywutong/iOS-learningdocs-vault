---
title: Pasteboard Programming Guide
apple_id: TP40008099
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2010-09-01'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PasteboardGuide106/Articles/pbReading.html
archived_at: '2026-07-15T07:17:41.484627Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Pasteboard Programming Guide](Introduction.md)


[Next](Custom%20Data.md)[Previous](Copying%20to%20a%20Pasteboard.md)

# Reading from a Pasteboard

This article describes how to read data from a pasteboard.

You read data from the pasteboard using the method, [readObjectsForClasses:options:](https://developer.apple.com/documentation/appkit/nspasteboard/1524454-readobjectsforclasses).

The method takes two arguments:

1. An array of the classes, instances of which you’re interested in reading from the pasteboard.

   It’s important that you order this array such that your preferred class is at the beginning of the array, with any remaining classes ordered in decreasing preference. (This will be explained in more detail in a moment.)
2. A dictionary containing options associated with the request.

   Using the options dictionary, you can place additional constraints on the such as restricting the search to file URLs with particular content types. If you don’t want to add further constraints, provide an empty dictionary.

The method returns an array of items that meet the criteria specified by the arguments. (If there is an error in retrieving the requested items from the pasteboard or if no objects of the specified classes can be created, the method returns `nil`.) For every _item_ on the pasteboard:

1. Each class in the classes array is queried for the types it can read (using `readableTypesForPasteboard:`).
2. An instance is created of the _first_ class found in the classes array whose readable types match a conforming type contained in the pasteboard item

   This is why it’s important to order the classes in the classes array according to your preference. (If no class is found, then no instance is created.)

Any instances that could be created from pasteboard item data are returned in the array. The returned array therefore contains at most the same number of elements as there are items on the pasteboard.

The following example shows how you can read strings from the pasteboard.

```
NSPasteboard *pasteboard = <#Get a pasteboard#>; 
NSArray *classes = [[NSArray alloc] initWithObjects:[NSString class], nil];
NSDictionary *options = [NSDictionary dictionary];
NSArray *copiedItems = [pasteboard readObjectsForClasses:classes options:options];
if (copiedItems != nil) {
    // Do something with the contents...
```


Sometimes you may be willing to handle multiple representations. There are at least two strategies for retrieving items from the pasteboard.

1. Make a single invocation of `readObjectsForClasses:options:` passing an array containing the classes you wish to handle.
2. Make multiple invocations of `readObjectsForClasses:options:`, each time passing a different array of classes.

The following examples illustrate the two approaches.

In this example, for any item that can provide both a rich text and a string representation, the rich text is preferred:

```
NSPasteboard *pasteboard = <#Get a pasteboard#>; 
NSArray *classes = [[NSArray alloc] initWithObjects:[NSAttributedString class], [NSString class], nil];
NSDictionary *options = [NSDictionary dictionary];
NSArray *copiedItems = [pasteboard readObjectsForClasses:classes options:options];
if (copiedItems != nil) {
    // Do something with the contents...
}
```

In this example, the pasteboard is searched first for string objects, and then for attributed strings. This sequence may result in pasteboard items being “used” twice if they can provide both string and attributed string representations.

```
NSPasteboard *pasteboard = <#Get a pasteboard#>;
NSDictionary *options = [NSDictionary dictionary];
NSArray *classes;

classes = [[NSArray alloc] initWithObjects:[NSString class], nil];
NSArray *strings = [pasteboard readObjectsForClasses:classes options:options];
if (strings != nil) {
    // Do something with the strings...
}

classes = [[NSArray alloc] initWithObjects:[NSAttributedString class], nil];
NSArray *attributedStrings = [pasteboard readObjectsForClasses:classes options:options];
if (copiedItems != nil) {
    // Do something with the attributed strings...
}
```


Sometimes you want to know whether a pasteboard contains data that you can use, but without actually retrieving the data. For example, you might want to know whether a Paste menu item should be enabled, or whether a drop operation (in a drag and drop sequence) is valid.

To determine whether a pasteboard contains data that can create instances of classes you’re interested in, you can send the pasteboard a [canReadObjectForClasses:options:](https://developer.apple.com/documentation/appkit/nspasteboard/1533360-canreadobject) message.

```
NSPasteboard *pasteboard = <#Get a pasteboard#>;
NSArray *classes = [[NSArray alloc] initWithObjects:[NSAttributedString class], [NSString class], nil];
NSDictionary *options = [NSDictionary dictionary];
BOOL ok = [pasteboard canReadObjectForClasses:classes options:options];
if (ok) {
    // ...
}
```


Sometimes you may want to retrieve URLs from a pasteboard, but only if they meet certain constraints—for example, you may only be interested in file URLs, or URLs that point to data of a particular type. You can impose such constraints using the options argument when you validate the contents of a pasteboard using [canReadObjectForClasses:options:](https://developer.apple.com/documentation/appkit/nspasteboard/1533360-canreadobject), or read from a pasteboard using [readObjectsForClasses:options:](https://developer.apple.com/documentation/appkit/nspasteboard/1524454-readobjectsforclasses).

You use the [NSPasteboardURLReadingFileURLsOnlyKey](https://developer.apple.com/documentation/appkit/nspasteboard/readingoptionkey/1526217-urlreadingfileurlsonly) option to constrain results to file URLs, as shown in this example.

```
NSPasteboard *pasteboard = <#Get a pasteboard#>;
NSArray *classes = [NSArray arrayWithObject:[NSURL class]];

NSDictionary *options = [NSDictionary dictionaryWithObject:
    [NSNumber numberWithBool:YES] forKey:NSPasteboardURLReadingFileURLsOnlyKey];

NSArray *fileURLs =
    [pasteboard readObjectsForClasses:classes options:options];
```

You use the [NSPasteboardURLReadingContentsConformToTypesKey](https://developer.apple.com/documentation/appkit/nspasteboardurlreadingcontentsconformtotypeskey) option to constrain results to URLs that point to particular types of data. The following example illustrates how you can retrieve only URLs that point to image data.

```
NSPasteboard *pasteboard = <#Get a pasteboard#>;
NSArray *classes = [NSArray arrayWithObject:[NSURL class]];

NSDictionary *options = [NSDictionary dictionaryWithObject:
    [NSImage imageTypes], forKey:NSPasteboardURLReadingContentsConformToTypesKey];

NSArray *imageURLs =
    [pasteboard readObjectsForClasses:classes options:options];
```

You can combine the two options; to retrieve only file URLs that point to image data, you would create the options dictionary as follows:

```
NSDictionary *options = [NSDictionary dictionaryWithObjectsAndKeys:
    [NSNumber numberWithBool:YES], NSPasteboardURLReadingFileURLsOnlyKey,
    [NSImage imageTypes], NSPasteboardURLReadingContentsConformToTypesKey, nil];
```

[Next](Custom%20Data.md)[Previous](Copying%20to%20a%20Pasteboard.md)

