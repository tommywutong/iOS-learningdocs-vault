---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WebScript7.html
archived_at: '2026-07-15T08:06:36.688674Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](The%20WebScript%20Language.md) [!Previous Section](WebScript6.md)

### Invoking Methods

When you want an object to perform one of its methods, you send the object a _message_. In WebScript, message expressions are enclosed in square brackets:

```
[receiver message]
```


The _receiver_ is an object, and the _message_ tells it what to do. For example, the following statement tells the object __aString__ to perform its __length__ method, which returns the string's length:

```
[aString length];
```


When the method requires arguments, you pass values by placing them to the right of the colon. For example, to invoke the method __addFirstValue:toSecondValue:__ shown previously, you would do this:

```
three = [aComponent addFirstValue:2 toSecondValue:1];
```


One message can also be nested inside another. Here the __description__ method returns the string representation of an NSCalendarDate object __myDate__, which is then appended to __aString__. The resulting string is assigned to __newString__:

```
newString = [aString stringByAppendingString:[myDate
description]];
```


As another example, here the array __anArray__ returns an object at a specified index. That object is then sent the __description__ message, which tells the object to return a string representation of itself, which is assigned to __desc__:

```
id desc = [[anArray objectAtIndex:anIndex] description];
```

[!Table of Contents](The%20WebScript%20Language.md) [!Next Section](WebScript8.md)
