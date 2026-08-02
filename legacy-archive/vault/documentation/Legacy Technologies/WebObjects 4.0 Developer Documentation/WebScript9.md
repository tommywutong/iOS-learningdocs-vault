---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/WebScript9.html
archived_at: '2026-07-18T01:20:37.571281Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](The%20WebScript%20Language.md) [!Previous Section](WebScript8.md)

### Sending a Message to a Class

Usually, the object receiving a message is an _instance_ of a class. For example, in this statement the variable __aString__ is an instance of the class NSString:

```
[aString length];
```


You can also send messages to a class. You send a class a message when you want to create a new instance of that class. For example this statement tells the class NSString to invoke its __stringWithString:__ method, which returns an instance of NSString that contains the specified string:

```
aString = [NSString stringWithString:@"Fred"];
```


Note that a class is represented in a script by its corresponding class name-in this example, NSString.
In WebScript, the classes you use include both _class methods_ and _instance methods_. Most class methods create a new instance of that class, whereas instance methods provide behavior for instances of the class. In the following example, a class method, __stringWithFormat:__, is used to create an instance of a class, NSString. Instance methods are then used to operate on the instance __myString__:

```
// Use a class method to create an instance of NSString
NSString *myString = [NSString
    stringWithFormat:@"The next word is %@", word];

// Use instance methods to operate on the instance
myString
length = [myString length];
lcString = [myString lowercaseString];
```


In an Objective-C class definition, class methods are preceded by a plus sign (+), while instance methods are preceded by a minus sign (-). You cannot declare class methods in WebScript, but you can use the Objective-C class methods defined for any class.

[!Table of Contents](The%20WebScript%20Language.md) [!Next Section](WebScript10.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
