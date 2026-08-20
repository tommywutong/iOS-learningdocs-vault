---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.033.html
archived_at: '2026-07-15T07:58:41.592396Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](Improved%20Nested%20Component%20Support.md)

## "Container" Components (WOComponentContent)

WOComponentContent is a dynamic element that allows you to write nested components as HTML container elements. A container element is an element that can include text and other elements between its opening and closing tags. For example, the HTML FORM element is a container element. As well, WORepetition is a container element.
Using WOComponentContent you can, for example, write a component that defines the header and footer for all of your application's pages. To do so, you'd define a component with HTML similar to the following:

```
<HTML>
    <HEAD>
        <TITLE>Cool WebObjects App</TITLE>
    </HEAD>
    <BODY>
        <!-- A banner common to all pages here -->
        <!-- Start of content defined by the parent element -->
        <WEBOBJECT name=ParentContent></WEBOBJECT>
        <!-- End of content defined by the parent element -->
        <!-- Put a footer common to all pages here. -->
    </BODY>
</HTML>
```


The __<WEBOBJECT>__ element on this page is a WOComponentContent element declared like this:

```
ParentContent : WOComponentContent {};
```


WOComponentContent is simply a marker that specifies where the contents wrapped by this component's __WEBOBJECT__ tag should go. You can have only one WOComponentContent element in a given component.
To use the component shown above, you'd wrap the contents of all of the other components in the application with a __<WEBOBJECT>__ tag that specifies the component defined above. For example, suppose you named the above component __HeaderFooterPage.wo__. You could use it in another component like this:

```
<!-- HTML for a simple component wrapped with HeaderFooterPage -->
<WEBOBJECT name = templateWrapperElement>
    <P>Hello, world!</P>
</WEBOBJECT>
```


Where __templateWrapperElement__ is declared in the __.wod__ file like this:

```
templateWrapperElement : HeaderFooterPage {};
```


At run-time, the contents wrapped by __templateWrapperElement__ are substituted for the WOComponentContent definition. As a result, the HTML generated for this component would be:

```
<!-- HTML for a simple component wrapped with HeaderFooterPage -->
<HTML>
    <HEAD>
        <TITLE>Cool WebObjects App</TITLE>
    </HEAD>
    <BODY>
        <!-- A banner common to all pages here -->
        <!-- Start of content defined by the parent element -->
        <P>Hello, world!</P>
        <!-- End of content defined by the parent element -->
        <!-- Put a footer common to all pages here. -->
    </BODY>
</HTML>
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.034.md)
