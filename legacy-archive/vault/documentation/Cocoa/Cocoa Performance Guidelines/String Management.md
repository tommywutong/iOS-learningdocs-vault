---
title: Cocoa Performance Guidelines
apple_id: TP40001448
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2009-08-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaPerformance/Articles/StringDrawing.html
archived_at: '2026-07-15T07:13:19.253008Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Performance Guidelines](Introduction%20to%20Cocoa%20Performance%20Guidelines.md)


[Next](Notifications.md)[Previous](Improving%20NSBezierPath%20Rendering%20Times.md)

# String Management

Strings are used extensively throughout Cocoa, and it’s very likely your application uses many of them as well. If you run Instruments and notice that your application spends a fair amount of time manipulating or displaying strings, you might want to look at your usage of [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) methods. There might be better ways to do what you need to do.

NSString and its assorted subclasses provide tremendous flexibility in how you can manipulate text, but that flexibility comes at a performance cost. If your application manipulates strings frequently or in very intensive ways, you might want to carefully consider the NSString methods you use. You might also want to consider writing your own string utilities to optimize the manipulations you do.

If you want to iterate over the characters of a string, one of the things you should not do is use the `characterAtIndex:` method to retrieve each character separately. This method is not designed for repeated access. Instead, consider fetching the characters all at once using the `getCharacters:range:` method and iterating over the bytes directly.

If you want to search a string for specific characters or substrings, do not iterate through the characters one by one. Instead, use higher level methods such as `rangeOfString:`, `rangeOfCharacterFromSet:`, or `substringWithRange:`, which are optimized for searching the NSString characters. You might also consider using the methods of NSScanner to parse the string contents for substrings. NSScanner also lets you parse a string for numerical values and return those values as scalar types.

NSString provides convenience methods for rendering strings. Methods such as `drawAtPoint:withAttributes:` and `drawInRect:withAttributes:` let you draw the string content to a specific location in the current view. However, drawing strings in this manner can still incur a significant amount of overhead.

NSString uses the Cocoa text system for rendering string content. When you ask NSString to render itself for the first time, it must set up several text system objects and then lay out and draw the glyphs in the string. The Application Kit does try to cache the text system objects to avoid some of these costs in the future.

If you have used the Cocoa text system at all, you should understand the amount of work it takes to render text. Text rendering requires numerous calculations to make sure characters have the right font, spacing, position, and so on. Collecting these attributes and then locating the glyphs to be drawn can involve the creation of numerous objects. If you throw these objects away after each use, you incur a significant performance penalty each time you draw your code. Much of this penalty can be easily removed by caching the objects you create.

Many of the objects in the Cocoa text system can be set up once and retained for future use. Preserving these objects can significantly improve text rendering performance during subsequent drawing operations.

[Next](Notifications.md)[Previous](Improving%20NSBezierPath%20Rendering%20Times.md)

