---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/Debug8.html
archived_at: '2026-07-18T01:20:03.461861Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Debugging%20a%20WebObjects%20Application.md) [!Previous Section](Debug7.md)

## Writing Debug Messages

The method __debugWithFormat:__ (in Java, __debugString__) writes a formatted string to standard error (__stderr__).
In WebScript and Objective-C, __debugWithFormat:__ works like the __printf()__ function in C. This method takes a format string and a variable number of additional arguments. For example, the following code excerpt prints the string "The value of myString is Elvis":

```
myString = @"Elvis";
[self debugWithFormat:@"The value of myString is %@", myString];
```


When this code is parsed, the value of __myString__ is substituted for the conversion specification __%@__. The conversion character @ indicates that the data type of the variable being substituted is an object (that is, of the __id__ data type).
Because in WebScript all variables are objects, the conversion specification you use must always be __%@__. Unlike __printf()__, you can't supply conversion specifications for primitive C data types such as __%d__, __%s__, __%f__, and so on. (If you do, you might see the address of the variable rather than its value.)
In Java, the equivalent of __debugWithFormat:__ is __debugString__. You can send it to WOApplication, WODirectAction, and WOComponent objects. Instead of using __printf__-style specifications, __debugWithFormat:__ uses concatenation to construct the string. For example, here's how you'd write the same lines of code in Java:

```
myString = "Elvis";
application().debugString("The value of myString is " + myString);
```


Perhaps the most effective debugging technique is to use __debugWithFormat:__ to print the contents of __self__. This prints the values of all of your component variables. For example, this statement at the end of the __sayHello__ method in HelloWorld's __Main.wos__:

```
[self debugWithFormat:@"The contents of self in sayHello are %@",
self];
```


produces output that resembles the following:

```
The contents of self in sayHello are <<Main: 0x8cb08 name=Main
subcomponents=0x0> visitorName=frank>
```


Here's how you'd write the same line of code in Java:

```
application().debugString("The contents of this in sayHello are "
    + this.toString());
```


All objects that respond to the __debugWithFormat:__ message also respond to the __logWithFormat:__ (or __logString__) message. It's recommended to use __debugWithFormat:__ for debugging messages because you can turn off the output of these messages with the WODebuggingEnabled user default. By default, WODebuggingEnabled is set to YES so all __debugWithFormat:__ messages print to __stderr__ while you are in development mode. When you are ready to deploy the application, you can disable the debugging messages with this command:

```
% defaults write MyApplication WODebuggingEnabled NO
```


When WODebuggingEnabled is NO, debugging statements are not printed. Thus, you should use __logWithFormat:__ messages for information that you want to print to __stderr__ whether or not you are in development mode.
__Note:__  Although setting WODebuggingEnabled to NO prevents debugging statements from being printed, __debugWithFormat:__ imposes a small performance penalty each time it is encountered. Once a component has stabilized, you'll want to strip out debugging statements.

[!Table of Contents](Debugging%20a%20WebObjects%20Application.md) [!Next Section](Debug9.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
