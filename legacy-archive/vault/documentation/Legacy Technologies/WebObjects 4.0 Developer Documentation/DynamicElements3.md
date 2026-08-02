---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/DynamicElements3.html
archived_at: '2026-07-18T01:20:09.775865Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Dynamic%20Elements.md) [!Previous Section](DynamicElements2.md)

## Binding Values to Dynamic Elements

In the previous example, all of the dynamic elements are bound to variables and methods from the component that contains them (the Main component). It's common to bind to variables and methods declared directly in the current component; however, you can bind to any value that the component can access.
This means, for instance, that you can bind to variables from the application or session object because the WOComponent class declares two instance variables, __application__ and __session__, which point to the current application and the current session. For example, you might define a component that displays relevant information about the application, including the date and time the application was started. It makes sense for the application object to store this date and time. Your component's __.wod__ file would access it through this declaration:

```
UP_SINCE:WOString {value = application.upSince.description};
```


To retrieve a value from this binding, WebObjects uses _key-value coding_, a standard interface for accessing an object's properties either through methods designed for that purpose or directly through its instance variables. With key-value coding, WebObjects sends the same message (__takeValue:forKey:__, or __takeValueForKey__ in Java) to any object it is trying to access. Key-value coding first attempts to access properties through accessor methods based on the key's name.
For example, to resolve the binding for the WOString element in the above component using key-value coding, WebObjects performs the following steps:

- It resolves the value for the __application__ key by looking for a method named __application__ in the component object.

In this case, WOComponent defines the __application__ method, which returns the WOApplication object.

- It resolves the value for the __upSince__ key by looking for a method named __upSince__ in the application object.

If the method is not found, it looks for an __upSince__ instance variable. In this case, the __upSince__ instance variable is defined in the application's code file.

- It resolves the value for the __description__ key by looking for a method named __description__ in the __upSince__ object.

Because __upSince__ is a date object, it defines a __description__ method, which prints the object's value as a string.

__Note:__ The Java equivalent of the __description__ method is __toString__, but you must use the WebScript name for methods and literals in the __.wod__ file even though the application is written in Java.

Here are the general rules for binding dynamic element attributes:

- You must bind to a variable or method accessible by the current component. (You can also bind to constant values.)
- If you bind to a method, the method must take no arguments. (If you need to bind to a method that takes arguments, you can wrap it inside of a method that doesn't take arguments.)
- You can bind to any key for objects that define keys.

For example, dictionary objects store key-value pairs. Suppose you declare a __person__ dictionary that has the keys __name__, __address__, and __phone__. These keys aren't really instance variables in the dictionary, but because WebObjects accesses values using
key-value coding, the following binding works:

```
myString : WOString { value = person.name };
```


Enterprise objects also define keys, so the same binding would work if __person__ was an enterprise object.

__Note:__  Be aware that __value = person.count__ will not work, as __count__ is assumed to be a dictionary key.

- You must use the Objective-C names for methods and literals.

Even if your entire application is written in Java, you must use the Objective-C names for methods and for literals. For example, you must use __YES__ instead of __true__, __NO__ instead of __false__, and __description__ instead of __toString__.

[!Table of Contents](Dynamic%20Elements.md) [!Next Section](DynamicElements4.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
