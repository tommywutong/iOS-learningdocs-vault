---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/ReusableComponents1.html
archived_at: '2026-07-18T01:20:18.416735Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Creating%20Reusable%20Components.md) [!Previous Section](Creating%20Reusable%20Components.md)

## Centralizing Application Resources

One of the challenges of maintaining a web-based application is the sheer number of pages that must be created and maintained. Even a modest application can contain scores of HTML pages. Although some pages must be crafted individually for each application, many (for example, a page that gathers customer information) could be identical across applications. Even pages that aren't identical across applications can share at least some portions (header, footer, navigation bars, and so on) with pages in other applications. With reusable components, you can factor out a portion of a page (or a complete page) that's used throughout one or more applications, define it once, and then use it wherever you want, simply by referring to it by name. This is a simple but powerful concept, as the following example illustrates.
Suppose you want to display a navigational control like the one shown in [Figure 31](#apple-giyti) at the bottom of each page of your application.

!

Figure 31. A Navigational Control

The HTML code for this control is:

```
<HTML>
<HEAD>
    <TITLE>World Wide Web Wisdom, Inc.</TITLE>
</HEAD>

<BODY>
Please come visit us again!

<!-- start of navigation control -->
<CENTER>
<TABLE BORDER = 7 CELLPADDING = 0 CELLSPACING = 5>
    <TR ALIGN = center>
        <TH COLSPAN = 4> World Wide Web Wisdom, Inc.</TH>
    </TR>
    <TR ALIGN = center>
        <TD><A HREF = "http://www.wwww.com/home.html"> Home
<a></TD>
        <TD><A HREF = "http://www.wwww.com/sales.html"> Sales
<a></TD>
        <TD><A HREF = "http://www.wwww.com/service.html"> Service
<a></TD>
        <TD><A HREF = "http://www.wwww.com/search.html"> Search
<a></TD>
    </TR>
</TABLE>
</CENTER>
<!-- end of navigation control -->

</BODY>
</HTML>
```


Thirteen lines of HTML code define the HTML table that constitutes the navigational control. You could copy these lines into each of the application's pages or use a graphical HTML editor to assemble the table wherever you need one. But as application size increases, these approaches becomes less practical. And obviously, when a decision is made to replace the navigational table with an active image, you must update this code in each page. Duplicating HTML code across pages is a recipe for irritation and long hours of tedium.
With a reusable component, you could define the same page like this:

```
<HTML>
<HEAD>
    <TITLE>World Wide Web Wisdom, Inc.</TITLE>
</HEAD>

<BODY>
Please come visit us again!

<!-- start of navigation control -->
<WEBOBJECT NAME="NAVCONTROL"></WEBOBJECT>
<!-- end of navigation control -->

</BODY>
</HTML>
```


The thirteen lines are reduced to one, which positions the WebObject named NAVCONTROL. The declarations file for this page binds the WebObject named NAVCONTROL to the component named NavigationControl:

```
NAVCONTROL: NavigationControl {};
```


All of the application's pages would have entries identical to these in their template and declarations files.
NavigationControl is a component that's defined once, for the use of all of the application's pages. Its definition is found in the directory __NavigationControl.wo__ in the file __NavigationControl.html__ and contains the HTML for the table:

```
<CENTER>
<TABLE BORDER = 7 CELLPADDING = 0 CELLSPACING = 5>
<TR ALIGN = center>
    <TH COLSPAN = 4> World Wide Web Wisdom, Inc.</TH>
</TR>
<TR ALIGN = center>
    <TD><A HREF = "http://www.wwww.com/home.html"> Home <a></TD>
    <TD><A HREF = "http://www.wwww.com/sales.html"> Sales <a></TD>
    <TD><A HREF = "http://www.wwww.com/service.html"> Service
<a></TD>
    <TD><A HREF = "http://www.wwww.com/search.html"> Search
<a></TD>
</TR>
</TABLE>
</CENTER>
```


Since NavigationControl defines a group of static elements, no declaration or code file is needed. However, a reusable component could just as well be associated with complex, dynamically determined behavior, as defined in an associated code file.
Now, to change the navigational control on all of the pages in this application, you simply change the NavigationControl component. What's more, since reusable components can be shared by multiple applications, the World Wide Web Wisdom company could change the look of the navigational controls in all of its applications by changing this one component.
If your application's pages are highly structured, reusable components could be the prevailing feature of each page:

```
<HTML>
<HEAD>
    <TITLE>World Wide Web Wisdom, Inc.</TITLE>
</HEAD>

<BODY>

<WEBOBJECT NAME="HEADER"></WEBOBJECT>
<WEBOBJECT NAME="PRODUCTDESCRIPTION"></WEBOBJECT>
<WEBOBJECT NAME="NAVCONTROL"></WEBOBJECT>
<WEBOBJECT NAME="FOOTER"></WEBOBJECT>

</BODY>
</HTML>
```


The corresponding declarations file might look like this:

```
HEADER: CorporateHeader {};
PRODUCTDESCRIPTION: ProductTable {productCode = "WWWW0314"};
NAVCONTROL: NavigationControl {};
FOOTER: Footer {type = "catalogFooter"};
```


Notice that some of these components above take arguments-that is, they are parameterized. For example, the ProductTable component's __productCode__ attribute is set to a particular product identifier, presumably to display a description of that particular product. The combination of reusability and customizability is particularly powerful, as you'll see in the next section.

[!Table of Contents](Creating%20Reusable%20Components.md) [!Next Section](ReusableComponents2.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
