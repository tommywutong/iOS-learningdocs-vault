---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/Debugging/JavaPitfalls.html
archived_at: '2026-07-15T07:51:20.056955Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DebuggingTOC.md) [!Previous Section](Pitfalls.md)

## Java Programming Pitfalls

When debugging Java code, watch out for the following tricky spots:

- You can't define multiple constructors or overloaded methods for the classes WebApplication, WebSession, Component, or any other class that originates as an Objective-C class. For example, the following code causes your application to crash:

```
    public class MyComponent extends Component {
        public void myMethod() { .... }

        //WRONG! Overloaded method causes runtime error.
        public void myMethod(int anInt) { ... }
    }
```

- The __pageWithName__ method creates the page by looking up and instantiating the component class that has the same name as the argument you provide to __pageWithName__. For this reason, your subclass of Component shouldn't be given a package name. For example, if you create a component named __MyPage.wo__ and place its Java file in the package __myClasses.web__, __pageWithName__ won't find the __MyPage.class__ file.
- Java is a more strictly typed language than is Objective-C or WebScript. If you're more familiar with Objective-C, you'll find that you need to cast the return types frequently. For example, suppose you define a method named __verify__ in the file __Session.java__ and you want to invoke that method from a component's Java file. To do so, you must cast the return type of the component's __session__ method as in the following:

```
    // From a component's Java file.
    ((Session)session()).verify();
```


By definition, __session__ returns a WebSession object. Because WebSession does not define a method named __verify__, your code won't compile unless you cast the return value of __session__ to your WebSession subclass.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
