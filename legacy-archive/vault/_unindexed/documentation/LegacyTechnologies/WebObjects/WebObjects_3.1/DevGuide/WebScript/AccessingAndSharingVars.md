---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/WebScript/AccessingAndSharingVars.html
archived_at: '2026-07-15T07:47:57.400942Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.mif.book.md)
[!Previous Section](VarScopeSummary.md)

# Accessing and Sharing Variables

WebScript automates the process of accessing non-local variables, whether they're declared in an application script, a session script, or in a component script. For a non-local variable __myVar__, for example, you can set and return its value from the script that declares it, as follows:

```
[self myVar];
[self setMyVar:newValue];
```

You don't have to implement these methods to invoke them---WebScript does this work behind the scenes. For example, you may notice that the Visitors __Application.wos__ script doesn't implement __visitorNum__, __setVisitorNum:__, or __setLastVisitor:__ methods, yet the __Main.wos__ script invokes them.

In these statements:

```
[self myVar];
[self setMyVar:newValue];
```

the __myVar__ and __setMyVar:__ messages are sent to __self__, which indicates that the variable __myVar__ is declared in the script that's accessing it. Sometimes a component script has to access application or session variables declared elsewhere. When you work with application and session variables, remember that they're owned by the application and session objects, respectively. To set or return their values, you send a message to the appropriate object, which, from a component script, you can always get by sending __application__ or __session__ to __self__. For example, the __Main.wos__ script in the Visitors example includes these statements:

```
number = [[self application] visitorNum];
[[self application] setVisitorNum:number];
[[self application] setLastVisitor:[[self application] aName]];
```

__Note:__  The application object is also represented by the global variable WOApp. However, use of WOApp is discouraged because global variables are not permitted in some of the languages supported by WebObjects.

You can also access a non-local variable declared in one component script from another component script. This is something you commonly do right before you navigate to a new page, for example:

```
id anotherPage = [[self application] pageWithName:@"Hello"];
[anotherPage setNameString:newValue];
```

The current script uses the statement `[anotherPage setNameString:newValue];` to set the value of __nameString__, which is declared in the page entitled "Hello".

This example uses the __pageWithName:__ method, which takes the name of a page as an argument and returns that page. You most commonly use __pageWithName:__ inside a method that returns a new page for display in the browser. Such a method could be associated with a hyperlink or a submit button. For example:

```
- contactPsychicNetwork
{
    id nextPage;
    nextPage = [[self application] pageWithName:@"Predictions"];
    return nextPage;
}
```

[!Table of Contents](WebScript.mif.book.md)
[!Next Section](LanguageSummary.md)
