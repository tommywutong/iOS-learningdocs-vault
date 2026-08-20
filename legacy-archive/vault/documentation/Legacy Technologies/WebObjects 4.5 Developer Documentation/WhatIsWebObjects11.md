---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WhatIsWebObjects11.html
archived_at: '2026-07-15T08:06:40.225603Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Previous Section](WhatIsWebObjects10.md)

### Template

You use a _template_ to specify how the page you're creating should look. This file typically contains static HTML elements (such as <H1> or <P>) along with some _dynamic elements_. Dynamic elements are the basic building blocks of a WebObjects application. They link an application's behavior with the HTML page shown in the web browser, and their contents are defined at run-time. Some of the more commonly-used dynamic elements are listed in the following table:

|  Element Name |  Description |
|  WOActionURL |  Enables the creation of URLs to invoke methods or specify pages to return. |
|  WOApplet |  Generates HTML to specify a Java applet. |
|  WOBody |  Specifies the background image to display for the HTML page. |
|  WOBrowser |  A selection list that displays multiple items at a time. |
|  WOCheckBox |  A check-box user interface control. |
|  WOConditional |  Controls whether a portion of the HTML page will be generated. |
|  WOForm |  A container element that generates a fill-in form. |
|  WOHyperlink |  Generates a hypertext link. |
|  WOImage |  Displays an image. |
|  WOImageButton |  A graphical submit button. |
|  WOJavaScript |  Lets you embed a script written in JavaScript in a dynamically-generated page. |
|  WORadioButton |  Represents an on-off switch. |
|  WORepetition |  A container element that repeats its contents (that is, everything between the <WEBOBJECT...> and </WEBOBJECT...> tags in the template file) a given number of times. |
|  WOResetButton |  A reset button. |
|  WOString |  A dynamically generated string. |
|  WOSubmitButton |  A submit button. |
|  WOText |  A multi-line field for text input and display. |
|  WOTextField |  A text input field. |

```
```


For a complete list of dynamic elements, along with their parameters, see the _Dynamic Elements Reference_.
An HTML template can also contain a reference to another component (called a _reusable component_ or _subcomponent_) that represents a portion of an HTML page. This reference behaves just like a reference to a dynamic element.

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Next Section](WhatIsWebObjects12.md)
