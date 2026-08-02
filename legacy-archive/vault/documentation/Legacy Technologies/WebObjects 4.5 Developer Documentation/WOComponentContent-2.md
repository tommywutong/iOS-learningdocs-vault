---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOComponentContent.html
archived_at: '2026-07-15T08:09:52.179652Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Dynamic Elements

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)

---

# WOComponentContent

## Element Description

WOComponentContent allows you to write nested components as
HTML container elements: elements that can include text and other
elements between their opening and closing tags. Using WOComponentContent
you can, for example, write a component that defines the header
and footer for all of your application's pages.

The WOComponentContent dynamic element doesn't have any
attributes. It's simply a marker that specifies where the contents
wrapped by the component's `<WEBOBJECT>` tag
should go.

|  |
| --- |
| You can only have one WOComponentContent element in a given component. |

## Synopsis

WOComponentContent { };

## Example

To write a component that defines the header and footer for
some or all of your application's pages, first define a component
with HTML similar to the following:

> ```
> <HTML>
>     <HEAD>
>         <TITLE>Cool WebObjects App</TITLE>
>     </HEAD>
>     <BODY>
>     <!-- A banner common to all pages here -->
>     <!-- Start of content defined by the parent element -->
>     <WEBOBJECT name=ParentContent></WEBOBJECT>
>     <!-- End of content defined by the parent element -->
>     <!-- Put a footer common to all pages here. -->
>     </BODY>
> </HTML>
> ```

The <WEBOBJECT> element above is a WOComponentContent
element declared like this:

> ```
> ParentContent : WOComponentContent {};
> ```

To use this component, wrap the contents of all of your other
components with a `<WEBOBJECT>` tag
that specifies the component defined above. For example, suppose
you named the above component `HeaderFooterPage.wo`.
You could use it in another component like this:

> ```
> <!-- HTML for a simple component wrapped with HeaderFooterPage -->
> <WEBOBJECT name = templateWrapperElement>
>     <P>Hello, world!</P>
> </WEBOBJECT>
> ```

Where `templateWrapperElement` is
declared in the `.wod` file
like this:

> ```
> templateWrapperElement : HeaderFooterPage {};
> ```

At runtime, the contents wrapped by `templateWrapperElement` are
substituted for the WOComponentContent definition. As a result,
the HTML generated for this component would be:

> ```
> <HTML>
>     <HEAD>
>         <TITLE>Cool WebObjects App</TITLE>
>     </HEAD>
>     <BODY>
>     <!-- A banner common to all pages here -->
>     <!-- Start of content defined by the parent element -->
>     <P>Hello, world!</P>
>     <!-- End of content defined by the parent element -->
>     <!-- Put a footer common to all pages here. -->
>     </BODY>
> </HTML>
> ```

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)
