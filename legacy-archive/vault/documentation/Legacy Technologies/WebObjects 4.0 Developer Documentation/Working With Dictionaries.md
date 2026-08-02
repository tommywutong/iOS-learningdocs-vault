---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/Foundation5.html
archived_at: '2026-07-18T01:20:12.832614Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](WebScript%20Programmer%27s%20Quick%20Reference%20to%20Foundation%20Classes.md) [!Previous Section](Commonly%20Used%20Array%20Methods.md)

# Working With Dictionaries

NSDictionary and NSMutableDictionary objects store collections of key-value pairs. The key-value pairs within a dictionary are called _entries_. Each entry consists of an object that represents the key, and a second object that represents the key's value. Within a dictionary, the keys are unique. That is, no two keys in a single dictionary are equivalent.
The difference between NSDictionary and NSMutableDictionary is that you can't add, modify, or remove entries from an NSDictionary's initial collection of entries. Insertion and deletion methods provided for NSMutableDictionaries are not available for NSDictionaries. Although their use is limited to managing static collections of objects, it's best to use NSDictionaries wherever possible.
You can create NSDictionaries using WebScript's @ syntax for defining constant objects. For example, the following statements create NSDictionaries:

```
id sizes = @{"S" = "Small"; "M" = "Medium"; "L" = "Large";
"X" = "Extra Large"};
id defaultPreferences = @{
    "seatAssignment" = "Window";
    "smoking" = "Non-smoking";
    "aircraft" = "747"};
```


You can also create dictionaries using creation methods. For example, if you want to create an NSDictionary that contains variables, you have to use a creation method. You can't use variables with WebScript's @ syntax. The following statement creates an NSDictionary that contains variables:

```
id customerPreferences = [NSDictionary
dictionaryWithObjectsAndKeys:
    seatingPreference, @"seatAssignment",
    smokingPreference, @"smoking",
    aircraftPreference, @"aircraft", nil];
```


The variable __customerPreferences__ is an NSDictionary, so its initial collection of entries can't be modified. To create a dictionary that can be modified, use a creation method to create an NSMutableDictionary. For example, the following statement creates an empty NSMutableDictionary:

```
id dictionary = [NSMutableDictionary dictionary];
```


The methods provided by NSDictionary and NSMutableDictionary are described in more detail next.

[!Table of Contents](WebScript%20Programmer%27s%20Quick%20Reference%20to%20Foundation%20Classes.md) [!Next Section](Commonly%20Used%20Dictionary%20Methods.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
