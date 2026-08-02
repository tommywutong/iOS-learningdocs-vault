---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/DynamicElement.html
archived_at: '2026-07-15T08:01:08.106584Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Extending Dynamic Elements

##  Synopsis

Describes how to implement custom dynamic elements using components.

##  Discussion

Custom dynamic elements in WebObjects are built in one of two ways: based on a component or subclassed from WODynamicElement. A custom dynamic element based on a component consists of a HTML, a WOD and a WebScript file. The HTML file specifies how this dynamic element looks. The WOD file declares the WebObjects dynamic elements comprising the custom dynamic element. The WOS file implements the dynamic element. As an example, we will build a dynamic element MyText which is a HTML form text input with a description above it to act as a hint of what to enter.

#####  Figure 1. MyText.HTML

```
<font size="2"><webobject name=AHint></webobject></font>
```



```
<webobject name=AText></webobject>
```


#####  Figure 2. MyText.WOD

```
AHint: WOString
```



```
{
```



```
    value = hintValue;
```



```
};
```



```
AText: WOText
```



```
{
```



```
    value = stringTextValue;
```



```
    rows = rowValue;
```



```
    cols = colValue;
```



```
    escapeHTML = escapeHTMLValue;
```



```
};
```


#####  Figure 3. MyText.WOS

```
id hintValue, rowValue, colValue, stringTextValue, escapeHTMLValue;
```


We will use the _MyText_
dynamic element to input a headline. The following declarations are made in the WOD file.

#####  Figure 4. WOD file

```
Headline: MyText
```



```
{
```



```
    stringTextValue = myDocument.headline;
```



```
    hintValue = "enter Headline here";
```



```
    rowValue = "2";
```



```
    colValue = "50";
```



```
escapeHTMLValue = NO;
```



```
};
```


When the _Headline_
element is displayed, "enter Headline here" appears on the top and the HTML form text field appears on the bottom.

To build a custom dynamic element subclassed from WODynamicElement, you must declare the variable bindings for your custom dynamic element as WOAssociation. For example,

#####  Figure 5. Objective-C Code

```objc
@interface WOSubscribePanel : WODynamicElement
```



```
{
```



```
    WOAssociation * emailAddress;
```



```
    WOAssociation * subscribeAction;
```



```
}
```


You must also implement the following three methods:

#####  Figure 6. Objective-C Code

```objc
- (id)initWithName:(NSString *) aName associations:(NSDictionary *)
```



```
   someAssociations template: (WOElement *) aTemplate;
```



```objc
- (void)takeValuesFromRequest:(WORequest *) aRequest inContext:
```



```
   (WOContext *) aContext;
```



```objc
- (WOElement *)invokeActionForRequest:(WORequest *) aRequest inContext:
```



```
   (WOContext *) aContext;
```



```objc
- (void)appendToResponse:(WOResponse *) aResponse inContext:
```



```
   (WOContext *) aContext;
```


Details of these three methods can be found in the documentation of WODynamicElement.

##  See Also

· Reusable Components

· WOComponent

· WOAssociation

· WODynamicElement

##  Questions

· How do I write a custom dynamic element?

· How do I use a custom dynamic element?

##  Keywords

· Dynamic Element

· Reusable Component

##  Revision History

22 July, 1998. Winnie Pun. First Draft.
19 November, 1998. Clif Liu. Second Draft.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
