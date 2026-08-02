---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/WebScript/CreatingObjects.html
archived_at: '2026-07-15T07:52:29.673980Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.md) [!Previous Section](MessageToClass.md)

### Creating Instances of Classes

The section ["Variables"](DeclaringVariables.md#apple-gu4tqny) told you how to declare variables, which represent objects. Before you use a variable, you must first create the object, or _instantiate_ the class that defines the object. In WebScript, there are two different ways to create objects. The first approach, which applies only to the most commonly used classes, is to initialize with constant objects as described in the section ["Assigning Values to Variables"](DeclaringVariables.md#apple-gq2tmmi). The second approach, which applies to all classes, is to use creation methods.

All classes provide creation methods that you can use to create an instance of that class. Depending on the class and the particular creation method, the instances of the class you create are either _mutable_ (modifiable) or _immutable_ (constant). Usually, the instances of a class are always mutable or always immutable. (You must read the specifications in the _Foundation Framework Reference_ to find out if a particular class is immutable or mutable.) However, some classes, including NSString, NSArray, and NSDictionary provide both mutable and immutable forms, and you can choose which one to create. It's best to create immutable objects wherever possible. Use a mutable object only if you need to change its value after you initialize it.
Here are some examples of using creation methods to create mutable and immutable NSString, NSArray, and NSDictionary objects:

```
    // Create a mutable string
    string = [NSMutableString stringWithFormat:@"The string is %@", aString];

    // Create an immutable string
    string = [NSString stringWithFormat:@"The string is %@", aString];

    // Create a mutable array
    array = [NSMutableArray array];
    anotherArray = [NSMutableArray arrayWithObjects:@"Marsha", @"Greg",
        @"Cindy", nil];

    // Create an immutable array
    array = [NSArray arrayWithObjects:@"Bobby", @"Jan", @"Peter", nil];

    // Create a mutable dictionary
    dictionary = [NSMutableDictionary dictionary];
    // Create an immutable dictionary
    id stooges = [NSDictionary
            dictionaryWithObjects:@("Mo", "Larry", "Curley")
            forKeys:@("Stooge1", "Stooge2", "Stooge3")];
```


The following examples show how you can create and work with NSCalendarDates, which are always immutable:

```
    // Using the creation method date, create an NSCalendarDate instance
    // 'now' that contains the current date and time
    now = [NSCalendarDate date];

    // Return a string representation of 'now' using a format string
    dateString = [now descriptionWithCalendarFormat:@"%B %d, %Y"];

    // Using the creation method dateWithString:, create an NSCalendarDate
    // instance 'newDate' from 'dateString'
    newDate = [NSCalendarDate dateWithString:dateString
        calendarFormat:@"%B %d, %Y"];

    // Return a new date in which newDate's day field is decremented
    date = [newDate addYear:0 month:0 day:-1 hour:0 minute:0 second:0];
```


For a detailed discussion of these classes and a more complete listing of methods, see the chapter ["WebScript Programmer's Quick Reference to Foundation Classes"](../Foundation/FoundationTOC.md#apple-gq4to).

[!Table of Contents](WebScript.md) [!Next Section](DataTypes.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
