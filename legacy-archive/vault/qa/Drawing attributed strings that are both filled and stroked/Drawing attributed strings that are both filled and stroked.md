---
title: Drawing attributed strings that are both filled and stroked
apple_id: DTS40007490
resource_type: QA
platform: macOS
topic: Data Management
technology: AppKit
published: '2013-04-29'
source_url: https://developer.apple.com/library/archive/qa/qa1531/_index.html
archived_at: '2026-07-18T02:32:12.116345Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1531

# Drawing attributed strings that are both filled and stroked

## Q:  How can I draw a string that specifies both a fill color and a stroke width?

A: Supply a negative value for `NSStrokeWidthAttributeName` when you wish to draw a string that is both filled and stroked.

This is because the sign of the value for `NSStrokeWidthAttributeName` is interpreted as a mode; it indicates whether the attributed string is to be filled, stroked, or both. Specifically, a zero value displays a fill only, while a positive value displays a stroke only. A negative value allows displaying both a fill and stroke.

__Figure 1__  A zero value for stroke width indicates fill with no stroke.

!

__Figure 2__  A positive value makes a stroke with no fill.

!

The code in Listing 1 demonstrates a custom view rendering an attributed string that's both filled and stroked. The results are in Figure 3.

__Listing 1__  Render a filled and stroked attributed string.

```objc
- (void)drawRect:(NSRect)rect {
    NSString    *string = @"Got Fill?";
    NSMutableDictionary *stringAttributes = [NSMutableDictionary dictionary];

    // Define the font and fill color
    [stringAttributes setObject: [NSFont fontWithName:@"Arial-Black" size:64] forKey: NSFontAttributeName];
    [stringAttributes setObject: [NSColor whiteColor] forKey: NSForegroundColorAttributeName];

    // Supply a negative value for stroke width that is 2% of the font point size in thickness
    [stringAttributes setObject: [NSNumber numberWithFloat: -2.0] forKey: NSStrokeWidthAttributeName];
    [stringAttributes setObject: [NSColor blackColor] forKey: NSStrokeColorAttributeName];

    // Paint the background
    [[NSColor grayColor] set];
    [NSBezierPath fillRect: [self bounds]];

    // Draw the string
    [string drawAtPoint: NSMakePoint(100, 100) withAttributes: stringAttributes];
}
```


__Figure 3__  Supplying a negative value for stroke width creates both a fill and stroke.

!

__See Also__

For more information on drawing strings, see the [String Programming Guide for Cocoa](../../documentation/Cocoa/String%20Programming%20Guide/Introduction%20to%20String%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaztklktk4yq), the [Attributed Strings Programming Guide](../../documentation/Cocoa/Attributed%20String%20Programming%20Guide/Introduction%20to%20Attributed%20String%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaztmlkcijbugr2eijdq) and [Cocoa Drawing Guide: Text](../../documentation/Cocoa/Cocoa%20Drawing%20Guide/Text.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqhewueq2jivcusr2d).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-04-29 | Editorial correction. |
| 2008-03-25 | New document that describes how the value of NSStrokeWidthAttributeName indicates fill, stroke, or both, in attributed strings. |

