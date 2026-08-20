---
title: How do I get the hexadecimal value of an NSColor object?
apple_id: DTS10004571
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2007-12-19'
source_url: https://developer.apple.com/library/archive/qa/qa1576/_index.html
archived_at: '2026-07-18T02:32:19.734535Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1576

# How do I get the hexadecimal value of an NSColor object?

## Q:  How do I get the hexadecimal value of an NSColor object?

A: How do I get the hexadecimal value of an NSColor object?

Below are the steps required to get the hexadecimal value of an NSColor object.

1. Convert the color object to the RGB color space.

   This step is important for it is illegal to access the components of an NSColor that are not defined for its color space. Use the `colorUsingColorSpaceName` method to convert a color to the RGB color space.
2. Get the red, green, and blue components of the color.

   These components are floating point values on the domain [0, 1] with the minimum intensity being 0 and the maximum intensity being 1. Use the `getRed:(CGFloat *)red green:(CGFloat *)green blue:(CGFloat *)blue alpha:(CGFloat *)alpha` method to obtain a color's red, green, and blue components.
3. Convert the components to the web color space, which consists of numbers (unsigned decimal integer) between 0 and 255.

   The goal here is to produce three two-digit hexadecimal color components with values that range from 0x00 ( 0 decimal, minimum intensity) through 0xFF ( 255 decimal, maximum intensity).
4. Convert each number to a two-digit hex string.
5. Concatenate the red, green, and blue components' hex strings together with a "#".

Listing 1 shows how to programmatically implement these steps; it builds an Objective-C `category` that adds the `hexadecimalValueOfAnNSColor` method to the NSColor class.

__Listing 1__  Adding a category to NSColor.

```objc
#import <Cocoa/Cocoa.h> @interface NSColor(NSColorHexadecimalValue)  -(NSString *)hexadecimalValueOfAnNSColor; @end  @implementation NSColor(NSColorHexadecimalValue)  -(NSString *)hexadecimalValueOfAnNSColor {     float redFloatValue, greenFloatValue, blueFloatValue;     int redIntValue, greenIntValue, blueIntValue;     NSString *redHexValue, *greenHexValue, *blueHexValue;    //Convert the NSColor to the RGB color space before we can access its components     NSColor *convertedColor=[self colorUsingColorSpaceName:NSCalibratedRGBColorSpace];      if(convertedColor)     {         // Get the red, green, and blue components of the color         [convertedColor getRed:&redFloatValue green:&greenFloatValue blue:&blueFloatValue alpha:NULL];          // Convert the components to numbers (unsigned decimal integer) between 0 and 255         redIntValue=redFloatValue*255.99999f;         greenIntValue=greenFloatValue*255.99999f;         blueIntValue=blueFloatValue*255.99999f;          // Convert the numbers to hex strings         redHexValue=[NSString stringWithFormat:@"%02x", redIntValue];          greenHexValue=[NSString stringWithFormat:@"%02x", greenIntValue];         blueHexValue=[NSString stringWithFormat:@"%02x", blueIntValue];          // Concatenate the red, green, and blue components' hex strings together with a "#"         return [NSString stringWithFormat:@"#%@%@%@", redHexValue, greenHexValue, blueHexValue];     }     return nil; } @end
```


__Listing 2__  Getting the hexadecimal value of an NSColor object.

```
//aColor is an NSColor object  NSString *hexValue=[aColor hexadecimalValueOfAnNSColor];
```


- [Color Programming Topics for Cocoa: Working With Color Spaces](https://developer.apple.com/documentation/Cocoa/Conceptual/DrawColor/Tasks/UsingColorSpaces.html#//apple_ref/doc/uid/TP40001807-96846)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-12-19 | New document that describes how to convert an NSColor object to its Hexadecimal value. |

