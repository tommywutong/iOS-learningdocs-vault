---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/WebScript13.html
archived_at: '2026-07-18T01:20:35.582220Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](The%20WebScript%20Language.md) [!Previous Section](WebScript12.md)

## Reserved Words

WebScript includes the following reserved words:

```
if
else
for
while
id
break
continue
self
super
nil
YES
NO
```


Three reserved words are special kinds of references to objects: __self__, __super__, and __nil__. You can use these reserved words in any method.
__self__ refers to the object (the WOApplication object, the WOSession object, the WOComponent object, or the WODirectAction object) associated with a script. When you send a message to __self__, you're telling the object associated with the script to perform a method that's implemented in the script. For example, suppose you have a script that implements the method __giveMeARaise__. From another method in the same script, you could invoke __giveMeARaise__ as follows:

```
[self giveMeARaise];
```


This tells the WOApplication, WOSession, WOComponent, or WODirectAction object associated with the script to perform its __giveMeARaise__ method.
When you send a message to __self__, the method doesn't have to be physically located in the script file. Remember that part of the advantage of object-oriented programming is that a subclass automatically implements all of its superclass's methods. For example, WOComponent defines a method named __application__, which retrieves the WOApplication associated with this component. Thus, you can send this message in any of your components to retrieve the application object:

```
[self application]
```


WOComponent also defines a session method, so you can do this to retrieve the current session:

```
[self session]
```


Sometimes, you actually do want to invoke the superclass's method rather than the current object's method. For example, when you initialize an object, you should always give the superclass a chance to perform its initialization method before the current subclass. To do this, you send the __init__ message to __super__, which represents the superclass of the current object.

```
- init {
        [super init];
        // my initialization.
        return self;
}
```


The __nil__ keyword represents an empty object. Any object before it is initialized has the value __nil__. __nil__ is similar to a null pointer in C. For example, to test whether an object has been allocated and initialized, you do this:

```
if (myArray == nil) //myArray hasn't been initialized.
```


This next statement also tests to see if __myArray__ is equal to __nil__:

```
if (!myArray) //myArray hasn't been initialized.
```

[!Table of Contents](The%20WebScript%20Language.md) [!Next Section](WebScript14.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
