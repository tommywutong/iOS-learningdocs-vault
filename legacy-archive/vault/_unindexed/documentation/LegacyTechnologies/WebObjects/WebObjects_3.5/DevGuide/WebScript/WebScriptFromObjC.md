---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/WebScript/WebScriptFromObjC.html
archived_at: '2026-07-15T07:52:35.226990Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.md) [!Previous Section](NoteToObjCDev.md)

## Accessing WebScript Methods From Objective-C Code

As stated previously, you can mix WebScript and Objective-C code. Often, programmers use WebScript for component logic, and then supply the bulk of the application (the "business logic") in compiled code.
To access Objective-C code from a WebScript file, you simply use the Objective-C class like any other class:

```
    id myObject = [[MyCustomObjCClass alloc] init];
```


To access a WebScript object from Objective-C code, you simply get the object that implements the method and send it a message. If you're accessing a method in the application or session script, you can use WOApplication methods to access the object:

```
    [[WOApplication application] applicationScriptMethod];
    [[[WOApplication application] session] sessionScriptMethod];
```


To access a component's methods, you must store the component in the session and then access it through the session. For example, suppose you wanted to rewrite the SelectedCars component of the DodgeDemo so that its database fetch code was in a compiled object and that object directly set the value of the __message__ variable in the SelectedCars component. You'd add the following statement to the __init__ method __SelectedCars.wos__:

```
    /* Store the component in the session. */
    [self.session setObject:self forKey:@"SelectedCars"];
```


and then you can access it in you custom object's __fetchSelectedCars__ method this way:

```
    /* Get the component from the session. */
    WOComponent *selectedCarsPage = [[[WOApplication application]
        session] objectForKey:@"SelectedCars"];

    /* Send it a message. */
    [selectedCarsPage setMessage:@"You must supply a name and address"];
```


To avoid compiler warnings, you should declare the scripted method you want to invoke in your code. This is because scripted objects don't declare methods-their methods are parsed from the script at runtime. If you don't declare their methods in your code, the compiler issues a warning that the methods aren't part of the receiver's interface.
__Note:__  This step isn't strictly required-your code will still build, you'll just get warnings.
For the example above, you'd add the following declaration to your object's implementation (__.m__) file:

```objc
    @interface WOComponent (SelectedCarsComponent)
    - (void)setMessage:(NSString *)aMessage;
    @end
```


While it's certainly straightforward to access a scripted object's methods from Objective-C code, you may not want to have that degree of interdependence between your scripts and your compiled code. You may want to minimize the interdependence to facilitate reusability.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
