---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Reuse/NavControlWO.html
archived_at: '2026-07-15T07:47:21.336003Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Reuse.book.md)
[!Previous Section](NavControlHTML.md)

# Navigation Control with WebObjects

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

WebObjects Builder makes reusable components even more attractive by providing a graphical way to create and maintain them. With the builder, you can assemble these components graphically and then put them on a palette for later use. Adding a custom reusable component to you application becomes a simple matter of dragging it from Builder's palette into your application and binding its attributes to variables or methods just as you would a dynamic element you drag from Builder's palettes. See "Advanced WebObjects Builder Tasks" in the _WebObjects Builder Guide_ for more information.

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
    <TD><A HREF = "http://www.wwww.com/service.html"> Service <a></TD>
    <TD><A HREF = "http://www.wwww.com/search.html"> Search <a></TD>
    </TR>
</TABLE>
</CENTER>
```

Since NavigationControl defines a group of static elements, no declaration or script file is needed. However, a reusable component could just as well be associated with complex, dynamically determined behavior, as defined in an associated script file.

[!Table of Contents](Reuse.book.md)
[!Next Section](RevisedNavControl.md)
