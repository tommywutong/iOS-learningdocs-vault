---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/ReusableComponents6.html
archived_at: '2026-07-18T01:20:21.862168Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Creating%20Reusable%20Components.md) [!Previous Section](ReusableComponents5.md)

# Creating a "Container" Reusable Component

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

[!Table of Contents](Creating%20Reusable%20Components.md) [!Next Section](Sharing%20Reusable%20Components%20Across%20Applications.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
