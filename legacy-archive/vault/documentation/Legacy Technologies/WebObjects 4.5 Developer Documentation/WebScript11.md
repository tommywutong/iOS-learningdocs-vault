---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WebScript11.html
archived_at: '2026-07-15T08:06:27.155678Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](The%20WebScript%20Language.md) [!Previous Section](WebScript10.md)

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
CarPage *carPage = [[self application]
pageWithName:"CarPage"];
```


Also, the default application executable used to run your application contains the definitions of classes from the Foundation, WebObjects, and Enterprise Objects frameworks, so these declarations are valid:

```
NSString *myString; //Foundation classes
WOContext *theContext; //WebObjects classes
EOEditingContext *editingContext; //Enterprise Objects
classes
```


Plus, if you're writing a component that uses database access, your application has an EOModel file that translates tables in your database into objects. You can specify any entity named in that model file as a class. For example:

```
Movies *moviesEntity; //Entities from your eomodel.
```


Static typing is supported so that WebObjects Builder can correctly parse your script file and help you decide which variables you can correctly bind to certain dynamic elements. (For more information on this, see the online book [_WebObjects Tools and Techniques_](WebObjects%20Tools%20and%20Techniques.md).) As far as WebScript is concerned, all variables are of type __id__.

__Note:__  WebObjects performs absolutely no type checking. The following is valid WebScript:

```
NSNumber *aNumber = @"Wait! I'm a string, not a number!";
NSString *aString = 1 + 2;
```

[!Table of Contents](The%20WebScript%20Language.md) [!Next Section](WebScript12.md)
