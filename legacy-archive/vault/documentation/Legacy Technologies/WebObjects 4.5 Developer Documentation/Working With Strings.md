---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Foundation1.html
archived_at: '2026-07-15T08:05:33.466849Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](WebScript%20Programmer%27s%20Quick%20Reference%20to%20Foundation%20Classes.md) [!Previous Section](Foundation%20Objects.md)

# Working With Strings

NSString and NSMutableString objects represent static and dynamic character strings, respectively. They may be searched for substrings, compared with one another, combined into new strings, and so on.
The difference between NSStrings and NSMutableStrings is that you can't change an NSString's contents from its initial character string. While NSMutableString provides methods such as __appendString:__ and __setString:__ to add to or replace the string's contents, there are no such methods available for NSStrings. It's best to use NSStrings wherever possible. Only use an NSMutableString if you need to modify its contents after you create it.
You can create NSStrings with WebScript's "at sign" @ syntax for defining constant objects. For example, the following statement creates an NSString object:

```
id msg = @"This option is no longer available. Please
choose another.";
```


You can also create string objects with creation methods-methods whose names are preceded by a + and that return new objects. The strings created with the @ syntax are always NSStrings, so they can't be modified. If you use a creation method instead, you can choose to create either an NSString or a NSMutableString. The following code excerpt illustrates the creation of both NSString and NSMutableString objects:

```
// Create an immutable string
id message = [NSString stringWithString:@"Hi"];

// Create a mutable string
id message = [NSMutableString stringWithString:@"Hi"];
```


The methods provided by NSString and NSMutableString are described in more detail in the next section.

[!Table of Contents](WebScript%20Programmer%27s%20Quick%20Reference%20to%20Foundation%20Classes.md) [!Next Section](Commonly%20Used%20String%20Methods.md)
