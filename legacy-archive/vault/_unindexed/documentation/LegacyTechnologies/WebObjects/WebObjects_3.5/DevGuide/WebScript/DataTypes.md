---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/WebScript/DataTypes.html
archived_at: '2026-07-15T07:52:30.176182Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.md) [!Previous Section](CreatingObjects.md)

## Data Types

Several of the examples in this chapter show how you can specify a data type when you define a method or variable. For example:

```objc
    NSString *myString = @"This is my string.";

    - (NSString *)appendString:(NSString *)aString {
        NSString *returnString = [NSString
            stringWithFormat:@"%@ %@", myString, aString];
        return returnString;
    }
```


Explicitly specifying a class in a variable or method declaration is called _static typing_.
Because variables and return values are always objects, the only supported data types are classes. You can specify any class that your application recognizes when you statically type a variable or a method. For example, each component in your application is a class, so you can do this:

```
    CarPage *carPage = [[self application] pageWithName:"CarPage"];
```


Also, the default application executable used to run your application contains the definitions of classes from the Foundation, WebObjects, and Enterprise Objects frameworks, so these declarations are valid:

```
    NSString *myString; //Foundation classes
WOContext *theContext; //WebObjects classes
EOEditingContext *editingContext; //Enterprise Objects classes
```


Plus, if you're writing a component that uses database access, your application has an EOModel file that translates tables in your database into objects. You can specify any entity named in that model file as a class. For example:

```
    Movies *moviesEntity; //entities from your eomodel
```


Static typing is supported so that WebObjects Builder can correctly parse your script file and help you decide which variables you can correctly bind to certain dynamic elements. (For more information on this, see the online book _WebObjects Tools and Techniques_.) As far as WebScript is concerned, all variables are of type __id__.
__Note:__  WebObjects performs absolutely no type checking. The following is valid WebScript:

```
    NSNumber *aNumber = @"Wait! I'm a string, not a number!";
    NSString *aString = 1 + 2;
```

[!Table of Contents](WebScript.md) [!Next Section](StatementsOperators.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
