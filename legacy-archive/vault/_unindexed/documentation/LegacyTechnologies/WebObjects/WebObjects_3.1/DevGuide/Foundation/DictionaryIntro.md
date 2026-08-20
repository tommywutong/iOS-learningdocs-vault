---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Foundation/DictionaryIntro.html
archived_at: '2026-07-15T07:46:46.204475Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Foundation.book.md) [!Previous Section](ArrayMethods.md)

# Working with Dictionaries

NSDictionary and NSMutableDictionary objects store collections of key-value pairs. The key-value pairs within a dictionary are called _entries_. Each entry consists of an object that represents the key and a second object that represents the key's value. Within a dictionary, the keys are unique. That is, no two keys in a single dictionary are equivalent.
The difference between NSDictionary and NSMutableDictionary is that you can't add, modify, or remove entries from an NSDictionary's initial collection of entries. Insertion and deletion methods provided for NSMutableDictionaries are not available for NSDictionaries. Although their use is limited to managing static collections of objects, it's best to use NSDictionaries wherever possible.
You can create NSDictionaries with WebScript's @ syntax for defining constant objects. For example, the following statements create NSDictionaries:

```
id sizes = @{"S" = "Small"; "M" = "Medium"; "L" = "Large"; "X" = "Extra
Large"};
id defaultPreferences = @{
    "seatAssignment" = "Window";
    "smoking" = "Non-smoking";
    "aircraft" = "747"};
```


You can also create dictionaries with creation methods. For example, if you want to create an NSDictionary that contains variables, you have to use a creation method. You can't use variables with WebScript's @ syntax. The following statement creates an NSDictionary that contains variables:

```
id customerPreferences = [NSDictionary dictionaryWithObjectsAndKeys:
    seatingPreference, @"seatAssignment",
    smokingPreference, @"smoking",
    aircraftPreference, @"aircraft", nil];
```


The variable __customerPreferences__ is an NSDictionary, so its initial collection of entries can't be modified. To create a dictionary that can be modified, use a creation method to create an NSMutableDictionary. For example, the following statement creates an empty NSMutableDictionary:

```
id dictionary = [NSMutableDictionary dictionary];
```


The methods provided by NSDictionary and NSMutableDictionary are described in more detail in the next section, "[Commonly Used Dictionary Methods](DictionaryMethods.md#apple-geytimq)."

[!Table of Contents](Foundation.book.md) [!Next Section](DictionaryMethods.md)
