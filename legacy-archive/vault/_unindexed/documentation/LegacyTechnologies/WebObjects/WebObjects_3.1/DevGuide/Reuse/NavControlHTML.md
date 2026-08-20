---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Reuse/NavControlHTML.html
archived_at: '2026-07-15T07:47:20.333565Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Reuse.book.md)
[!Previous Section](CentralResources.md)

# Navigation Control in HTML

Suppose you want to display a navigational control at the bottom of each page of your application, something like this

!
 ____Figure 1.__  Navigational Control__

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
    <TD><A HREF = "http://www.wwww.com/home.html"> Home <a></TD>
    <TD><A HREF = "http://www.wwww.com/sales.html"> Sales <a></TD>
    <TD><A HREF = "http://www.wwww.com/service.html"> Service <a></TD>
    <TD><A HREF = "http://www.wwww.com/search.html"> Search <a></TD>
    </TR>
</TABLE>
</CENTER>
<!-- end of navigation control -->
</BODY>
</HTML>
```

Thirteen lines of HTML code define the HTML table that constitutes the navigational control. You could copy these lines into each of the application's pages or use a graphical HTML editor to assemble the table wherever you need one. But as application size increases, these approaches becomes less practical. And obviously, when a decision is made to replace the navigational table with an active image, you must update this code in each page. Duplicating HTML code across pages is a recipe for irritation and long hours of tedium.

[!Table of Contents](Reuse.book.md)
[!Next Section](NavControlWO.md)
