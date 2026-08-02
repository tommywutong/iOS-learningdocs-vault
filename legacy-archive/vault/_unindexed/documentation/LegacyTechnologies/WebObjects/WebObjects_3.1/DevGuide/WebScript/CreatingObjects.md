---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/WebScript/CreatingObjects.html
archived_at: '2026-07-15T07:47:59.988570Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.mif.book.md)
[!Previous Section](Messaging.md)

# Creating Objects

There are two different ways to create objects in WebScript. The first approach, which applies to all classes, is to use class creation methods. The second approach applies to just NSStrings, NSArrays, and NSDictionaries. For these classes WebScript provides a convenient syntax for initializing constant objects.

## Using Creation Methods

All classes provide creation methods that you can use to create an instance of that class. Depending on the class and the particular creation method, the instances of the class you create might be either mutable (modifiable) or immutable (constant). When you use creation methods to create NSStrings, NSArrays, and NSDictionaries, you can choose to create either an immutable or a mutable object. For clarity, it's best to use immutable objects wherever possible. Only use a mutable object if you need to change its value after you initialize it.

Here are some examples of using creation methods to create mutable and immutable NSString, NSArray, and NSDictionary objects:

```
// Create a mutable string
string = [NSMutableString stringWithFormat:@"The string is %@", aString];
// Create an immutable string
string = [NSString stringWithFormat:@"The string is %@", aString];
// Create a mutable array
array = [NSMutableArray array];
anotherArray = [NSMutableArray arrayWithObjects:@"Marsha", @"Greg", @"Cindy", nil];
// Create an immutable array
array = [NSArray arrayWithObjects:@"Bobby", @"Jan", @"Peter", nil];
// Create a mutable dictionary
dictionary = [NSMutableDictionary dictionary];
// Create an immutable dictionary
id stooges = [NSDictionary
    dictionaryWithObjects:@("Mo", "Larry", "Curley")
    forKeys:@("Stooge1", "Stooge2", "Stooge3")];
```

The instances of some classes are always mutable or always immutable. The following examples show how you can create and work with NSCalendarDates, which are always immutable:

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

For a detailed discussion of these classes and a more complete listing of methods, see the chapter "A Foundation for WebScript Programmers: Quick Guide to Useful Classes."

## Creating Constant NSStrings, NSArrays, and NSDictionaries

NSStrings, NSArrays, and NSDictionaries are the classes you use most often in WebScript. WebScript provides a convenient syntax for initializing constant objects of these types. In such an assignment statement, the value you're assigning to the constant object is preceded by an at sign (@). You use parentheses to enclose the elements of an NSArray, and curly braces to enclose the key-value pairs of an NSDictionary. The following are examples of how you use this syntax to assign values to constant NSStrings, NSArrays, and NSDictionaries in WebScript:

```
myString = @"hello world";
myArray = @("hello", "goodbye");
myDictionary = @{"key" = 16};
anotherArray = @(1, 2, 3, "hello");
aDict = @{ "a" = 1; "b" = "hello world"; "c" = (1,2,3);
"d" = { "x" = 1; "r" = 2 }};
```

The following rules apply when you use this syntax to create constant objects:

- The value you assign must be a constant (that is, it can't include variables). For example, the following is not allowed:

```
    // This is not allowed!!
    myArray = @("hello", aVariable);
```

- You shouldn't use @ to identify NSStrings, NSArrays, or NSDictionaries inside the value being assigned. For example:

```
    // This is not allowed!!
    myDictionary = @(@"value" = 3);
    // Do this instead
    myDictionary = @("value" = 3);
```

For more information on NSStrings, NSDictionaries, and NSArrays, see the _Foundation Framework Reference_.

[!Table of Contents](WebScript.mif.book.md)
[!Next Section](WritingOwnMethods.md)
