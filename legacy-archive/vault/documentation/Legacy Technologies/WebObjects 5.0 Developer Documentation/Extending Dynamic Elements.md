---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.14.html
archived_at: '2026-07-15T08:14:48.876412Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.13.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.15.md)

#   Extending Dynamic Elements

##  Synopsis

Describes how to implement custom dynamic elements using components.

##  Discussion

Custom dynamic elements in WebObjects are built in one of two ways: based on a component or subclassed from WODynamicElement. A custom dynamic element based on a component consists of a HTML, a WOD and a WebScript file. The HTML file specifies how this dynamic element looks. The WOD file declares the WebObjects dynamic elements comprising the custom dynamic element. The WOS file implements the dynamic element. As an example, we will build a dynamic element MyText which is a HTML form text input with a description above it to act as a hint of what to enter.

####  MyText.HTML

```

<font size="2"><webobject name=AHint></webobject></font><br>
<webobject name=AText></webobject>
```

####  MyText.WOD_(Continued)_

```

AHint: WOString
{
    value = hintValue;
};
AText: WOText
{
    value = stringTextValue;
    rows = rowValue;
    cols = colValue;
    escapeHTML = escapeHTMLValue;
};
```

####  MyText.WOS

```

id hintValue, rowValue, colValue, stringTextValue, escapeHTMLValue;
```


We use the
MyText
dynamic element to input a headline. The following declarations are made in the WOD file.

####  WOD file

```

Headline: MyText

{

    stringTextValue = myDocument.headline;

    hintValue = "enter Headline here";

    rowValue = "2";

    colValue = "50";

    escapeHTMLValue = NO;

};
```


When the
Headline
element is displayed, "enter Headline here" appears on the top and the HTML form text field appears on the bottom.

Building a custom dynamic element by subclassing WODynamicElement is deprecated. In WebObjects 4, the performance and functionality of component-based dynamic elements eliminates the need to subclass WODynamicElement. The WebObjects Examples contain a framework called
ComponentElement.fproj
which contains component versions of every WebObjects dynamic element. This framework illustrates the power of component-based dynamic elements.

##  See Also

- 

  WOComponent class specification in the _WebObjects Framework Reference_
- 

  WOAssociation in the _WebObjects Framework Reference_
- 

  WODynamicElement in the _WebObjects Framework Reference_

##  Questions

- 

  How do I write a custom dynamic element?
- 

  How do I use a custom dynamic element?

##  Keywords

- 

  Dynamic
- 

  Element
- 

  Reusable
- 

  Component

##  Revision History

22 July, 1998. Winnie Pun. First Draft.
19 November, 1998. Clif Liu. Second Draft.

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.13.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.15.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
