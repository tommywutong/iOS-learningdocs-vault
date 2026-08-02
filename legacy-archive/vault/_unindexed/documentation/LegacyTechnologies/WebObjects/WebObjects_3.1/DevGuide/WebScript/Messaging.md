---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/WebScript/Messaging.html
archived_at: '2026-07-15T07:48:02.422107Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.mif.book.md)
[!Previous Section](MakingAssignments.md)

## Messaging in WebScript

To get an object to do something in WebScript, you send it a message telling it to perform a method. In WebScript, message expressions are enclosed in square brackets:

[_receiver message_]

The receiver is an object, and the message tells it what to do. For example, the statement:

```
[aString length];
```

tells the object __aString__ to perform its __length__ method, which returns the string's length. Methods can also take arguments. For example, this statement:

```
[aString isEqual:anotherString];
```

tells the object __aString__ to perform its __isEqual:__ method, which takes another object as an argument and tests it against __aString__ for equality. A method can take multiple arguments. For example the statement:

```
[aString insertString:anotherString atIndex:3];
```

inserts the characters of __anotherString__ into __aString__ at the specified index. Note that the method name __insertString:atIndex:__ has two colons, one for each of its arguments. The colons are preceded by keywords that describe their arguments (for example, __atIndex:__ takes as its argument an integer representing an index).

One message can also be nested inside another. Here the __description__ method returns the string representation of an NSCalendarDate object __myDate__, which is then appended to __aString__.The resulting string is assigned to __newString__:

```
newString = [aString stringByAppendingString:[myDate description]];
```

To give another example, here the array __anArray__ returns an object at a specified index. That object is then sent the __description__ message, which tells the object to return a string representation of itself, which is assigned to __desc__:

```
id desc = [[anArray objectAtIndex:anIndex] description];
```

### Sending a Message to a Class

Most commonly, the object receiving a message is an _instance_ of a class. For example, in the statement:

```
[aString length];
```

the variable __aString__ is an instance of the class NSString.

However, sometimes you send messages to a class. You send a class a message when you want to create a new instance of that class. For example the statement:

```
aString = [NSString stringWithString:@"Fred"];
```

tells the class NSString to invoke its __stringWithString:__ method, which returns an instance of NSString that contains the specified string. Note that a class is represented in a script by its corresponding class name---in this example, NSString.

The classes you use in WebScript include both class and instance methods. Most class methods create a new instance of that class, while instance methods provide behavior for instances of the class. The following example shows how you use an NSString class method to create an instance of NSString, and then use instance methods to operate on the instance __myString__:

```
// Use a class method to create an instance of NSString
id myString = [NSString stringWithFormat:@"The next word is %@", word];
// Use instance methods to operate on the instance myString
length = [myString length];
lcString = [myString lowercaseString];
```

In a class definition, class methods are preceded by a plus sign (+), while instance methods are preceded by a minus sign (-). You can define new classes in WebScript: see "[Scripted Classes](ScriptedClasses.md#apple-kjcumojvg43do)" for details. Or you can take advantage of existing classes. For more information, see the _Foundation Framework Reference_.

[!Table of Contents](WebScript.mif.book.md)
[!Next Section](CreatingObjects.md)
