---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Foundation/StringIntro.html
archived_at: '2026-07-15T07:46:47.697163Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Foundation.book.md) [!Previous Section](FoundationIntro.md)

# Working with Strings

NSString and NSMutableString objects represent static and dynamic character strings, respectively. They may be searched for substrings, compared against one another, combined into new strings, and so on.
The difference between NSStrings and NSMutableStrings is that you can't change an NSString's contents from its initial character string. While NSMutableStrings provide methods such as __appendString:__ and __setString:__ to add to or replace the string's contents, there are no such methods available for NSStrings. For clarity, it's best to use NSStrings wherever possible. Only use an NSMutableString if you need to modify its contents after you create it.
You can create NSStrings with WebScript's "at sign" @ syntax for defining constant objects. For example, the following statement creates an NSString:

```
id msg = @"The option you chose is no longer available. Please choose
another.";
```


You can also create string objects with creation methods-methods whose names are preceded by a + and that return new objects. The strings created with the @ syntax are always NSStrings, so they can't be modified. If you use a creation method instead, you can choose to create either an NSString or a NSMutableString. The following code excerpt illustrates the creation of both NSString and NSMutableString objects:

```
// Create an immutable NSString
id message = [NSString stringWithString:@"Hi"];

// Create a mutable NSMutableString
id message = [NSMutableString stringWithString:@"Hi"];
```


The methods provided by NSString and NSMutableString are described in more detail in the next section, "[Commonly Used String Methods](StringMethods.md#apple-hezds)."

[!Table of Contents](Foundation.book.md) [!Next Section](StringMethods.md)
