---
title: Pasteboard Programming Topics for Cocoa
apple_id: 10000068i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2009-01-20'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CopyandPaste/Articles/pbFontData.html
archived_at: '2026-07-15T07:13:53.439250Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Pasteboard Programming Topics for Cocoa](Introduction%20to%20Pasteboards%20Programming%20Topics.md)


[Next](Reading%20and%20Writing%20RTFD%20Data.md)[Previous](Data%20Types.md)

# Reading and Writing Font Data

Font information is stored on the font pasteboard as an attribute of RTF data from an attributed string. To copy and paste a font, therefore, you need to respectively create an attributed string with the appropriate attribute and unpack the information from an attributed string.

You copy a font using the pasteboard named `NSFontPboard`. You must first get the pasteboard, then declare the appropriate type—`NSFontPboardType`. To create the data to place on the pasteboard, you create an instance of `NSAttributedString`; the string itself is arbitrary, but you must specify an attribute dictionary that contains the key `NSFontAttributeName` and the corresponding value the font that you want to write to the pasteboard. You then create from the string an `NSData` object to represent the RTF data and set that as the data on the pasteboard for the `NSFontPboardType`.

The following code example illustrates how to write font information to the font pasteboard. The example uses a statically-defined font; in your code you typically find the font of the currently-selected text item and use that.

```
NSPasteboard *pb = [NSPasteboard pasteboardWithName:NSFontPboard];
[pb declareTypes:[NSArray arrayWithObject:NSFontPboardType] owner:self];

NSFont *font = [NSFont fontWithName:@"Helvetica" size:12.0];
NSDictionary *attributes = [NSDictionary dictionaryWithObject:font forKey:NSFontAttributeName];

NSAttributedString *aString = [[NSAttributedString alloc] initWithString:@"a" attributes:attributes];
NSRange aRange = NSMakeRange(0, 1);

NSData *aStringData = [aString RTFFromRange:aRange documentAttributes:nil];
[aString release];

[pb setData:aStringData forType:NSFontPboardType];
```


You read a font using the pasteboard named `NSFontPboard`. You must first get the pasteboard, then ask the pasteboard for the appropriate type—`NSFontPboardType`. The font data is in the form of RTF data created from an attributed string. You therefore create an instance of `NSAttributedString` from this data, then get the font attribute from the attributed string.

The following code example illustrates how to read font information from the font pasteboard.

```
NSPasteboard *pb = [NSPasteboard pasteboardWithName:NSFontPboard];
NSString *bestType = [pb availableTypeFromArray:
                             [NSArray arrayWithObject:NSFontPboardType]];
NSFont *font;

if (bestType != nil) {

    NSData *data = [pb dataForType:NSFontPboardType];
    NSAttributedString *aString =
            [[NSAttributedString alloc] initWithRTF:data documentAttributes:NULL];

    if (aString != nil) {
        font = [aString attribute:NSFontAttributeName atIndex:0 effectiveRange:NULL];
        NSLog(@"font: %@", [font description]);
    }
    else {
        NSLog(@"couldn't get attributed string");
    }
    [aString release];
}
else {
    NSLog(@"couldn't get NSFontPboardType");
}
```

[Next](Reading%20and%20Writing%20RTFD%20Data.md)[Previous](Data%20Types.md)

