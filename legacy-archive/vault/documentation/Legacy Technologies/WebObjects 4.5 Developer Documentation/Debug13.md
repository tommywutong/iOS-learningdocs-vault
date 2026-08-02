---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Debug13.html
archived_at: '2026-07-15T08:05:12.315327Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Debugging%20a%20WebObjects%20Application.md) [!Previous Section](Programming%20Pitfalls%20to%20Avoid.md)

## Java Programming Pitfalls

When debugging Java code, watch out for the following tricky spots:

- You can't define multiple constructors or overloaded methods for the classes WOApplication, WOSession, WOComponent, or any other class that originates as an Objective-C class. For example, the following code causes your application to crash:

```
public class MyComponent extends WOComponent {
    public void myMethod() { .... }

    //WRONG! Overloaded method causes runtime error.
    public void myMethod(int anInt) { ... }
}
```

- The __pageWithName__ method creates the page by looking up and instantiating the component class that has the same name as the argument you provide to __pageWithName__. For this reason, your subclass of WOComponent shouldn't be given a package name. For example, if you create a component named __MyPage.wo__ and place its Java file in the package __myClasses.web__, __pageWithName__ won't find the __MyPage.class__ file.
- Java is a more strictly typed language than is Objective-C or WebScript. If you're more familiar with Objective-C, you'll find that you need to cast the return types frequently. For example, suppose you define a method named __verify__ in the file __Session.java__ and you want to invoke that method from a component's Java file. To do so, you must cast the return type of the component's __session__ method as in the following:

```
// From a component's Java file.
((Session)session()).verify();
```


By definition, __session__ returns a WOSession object. Because WOSession does not define a method named __verify__, your code won't compile unless you cast the return value of __session__ to your WOSession subclass.

[!Table of Contents](Debugging%20a%20WebObjects%20Application.md) [!Next Section](WebObjects%20Viewed%20Through%20Its%20Classes.md)
