---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/WhatIsWOApp/Components.html
archived_at: '2026-07-15T07:52:41.848570Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WhatIsWOApp.md) [!Previous Section](Ingredients.md)

## Components

To write a WebObjects application, you create components and then connect them. A _component_ is a web page, or a portion of one, that has both content and behavior. Usually a component represents an entire page, so the word "page" is used interchangeably with the word "component." However, remember, that not all components represent an entire page. For example, a component might represent only a header or footer of a page, and you can nest that component inside of a component that does represent the entire page.
Each component is located in its own directory, named _Component___.wo__, and generally contains these parts:

- A template that specifies how the component looks
- Code that specifies how the component acts
- Bindings that associate the component's template with its code

[Figure 1](#apple-g43de) shows the contents of the __Main.wo__ component from the HelloWorld example. (__Main.wo__ is almost always the name of the first page of a WebObjects application.) In this example, the __Main.wo__ component contains three files: a template in the form of an HTML file (__Main.html__), the code file (__Main.wos__), and the declarations file (__Main.wod__), which contains the bindings between the template and the code.

!Figure 1. The Contents of a WebScript Component Directory
Typically, components contain some form of the three files shown in [Figure 1](#apple-g43de); however, any given component might contain more or fewer files. For example, components whose code is written in a compiled language do not contain code files. A component may not need a code file at all; it may need only a template file and a declarations file. Another component might have a code file but no template file or declarations file. Plus, if you create a component using Project Builder or WebObjects Builder, you'll get a fourth file, _Component___.api__, which contains API that should be made public to other components.

The next three sections describe more completely these template, code, and declarations files.

### Template

You use a _template_ (__Main.html__) to specify how the page you're creating should look. This file typically contains static HTML elements (such as <H1> or <P>) along with some dynamic elements. _Dynamic elements_ are the basic building blocks of a WebObjects application. They link an application's behavior with the HTML page shown in the web browser, and their contents are defined at runtime.
An HTML template can also contain a reference to another component (called a _reusable component_ or _subcomponent_) that represents a portion of an HTML page. This reference behaves just like a reference to a dynamic element.

### Code or Script File

You use the _code file_ (__Main.wos__) to define your component's attributes and actions. The attributes are called _variables_ or _instance variables_, and the actions are called _methods_.
With WebObjects, you can write your code file in one of three programming languages: Java, Objective-C, or WebScript. Java is the language of choice for many people; others prefer Objective-C. Because both of these languages require compiling, they aren't as well suited to rapid prototyping as a scripting language is. For this reason WebObjects provides a scripting language named WebScript, described in the chapter ["The WebScript Language"](../WebScript/WebScript.md). You may have noticed that the examples directory mentioned previously offers examples in all three languages.

__Note:__  Java support is not available on the Mach or HP-UX platform.
The __Main.wo__ component shown in [Figure 1](#apple-g43de) uses a WebScript file to define its behavior. (The __.wos__ extension signifies WebScript.) If you want to use Java or Objective-C, the code file resides at the same level as the __Main.wo__ directory as shown in [Figure 2](#apple-guztgmy). (In Project Builder, Java and Objective-C code files are shown under Classes instead of with the component under Web Components.)

!Figure 2. Location of Code File for Java Component
You can mix languages. It's common to use WebScript to write your interface logic (that is, the files described in this chapter) and use Java or Objective-C to write your business logic. Many simple applications are written entirely in WebScript. Some programmers prototype using WebScript and then create a compiled version of the same application to improve performance.

### Bindings

You use a _declarations file_ (__Main.wod__) to define the bindings, or mapping, between the methods and variables you defined in your code and the dynamic elements in your template. For example in the HelloWorld application, the HTML template for the Main component contains two dynamic elements. The declarations file specifies that the first dynamic element represents a text field whose value maps to the __visitorName__ variable in the component's script. When the user types a name in the text field, WebObjects assigns it to the __visitorName__ variable. The declarations file also specifies that the second dynamic element is a submit button and that when the user clicks the button, WebObjects invokes the __sayHello__ method.

[!Table of Contents](WhatIsWOApp.md) [!Next Section](AppCode.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
