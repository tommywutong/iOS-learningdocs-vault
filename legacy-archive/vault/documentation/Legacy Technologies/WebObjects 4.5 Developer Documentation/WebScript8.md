---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WebScript8.html
archived_at: '2026-07-15T08:06:37.202172Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](The%20WebScript%20Language.md) [!Previous Section](WebScript7.md)

### Accessor Methods

As stated previously, you can access any instance variable within any method declared in the same object. If you need to access a variable in a different object, you must send a message to that object.
_Accessor methods_ are methods that other objects can use to access an object's instance variables. When you declare an instance variable, WebScript automatically defines two accessor methods: one to retrieve the instance variable's value, and one to change the value.
For example, suppose an __Application.wos__ script declared this instance variable, which keeps track of the number of visitors:

```
id visitorNum;
```


When WebScript parses this file, it sees this declaration and implicitly defines two methods that work like this:

```
- visitorNum {
        return visitorNum;
}

- setVisitorNum:newValue {
        visitorNum = newValue;
}
```


(You don't see these methods in the script file.) The __Main.wos__ script can access the application's __visitorNum__ variable using these statements:

```
number = [[self application] visitorNum];
...
[[self application] setVisitorNum:number];
```


__Note:__  __self__ is a keyword that represents the current object. For more information, see ["Reserved Words"](WebScript13.md#apple-ha4tsna).

You can also access an instance variable declared in one component script from another component script. This is something you commonly do right before you navigate to a new page, for example:

```
id anotherPage = [[self application]
pageWithName:@"Hello"];
[anotherPage setNameString:newValue];
```


The current script uses the statement [anotherPage setNameString:newValue]; to set the value of __nameString__, which is declared in the page named Hello.

[!Table of Contents](The%20WebScript%20Language.md) [!Next Section](WebScript9.md)
