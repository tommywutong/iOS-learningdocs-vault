---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Customizing/Adding_a_Lo_o_Web_Pages.html
archived_at: '2026-07-15T08:12:23.564461Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Customizing_Application.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Using_Direc_pplications.md)

## Adding a Logo to Your Direct to Web Pages

The Neutral look is well-suited for adding a logo because
it doesn't already display the Apple or WebObjects logos, unlike
the Basic and WebObjects looks. To add a company logo to your Direct
to Web pages, you need to add the HTML code that displays the logo to
two components: `Main.wo`,
which implements the login page, and `PageWrapper.wo`,
which provides the backdrop for all of the pages Direct to Web generates.
In this example, the Apple logo is added to `PageWrapper.wo`.

1. Edit `PageWrapper.html`.
   Line 3 reads:

   ```
   <TABLE BORDER=0 CELLPADDING=4 CELLSPACING=0 WIDTH=100%>
   ```

   After
   this line add

   ```
   <TR>
       <TD><WEBOBJECT NAME=Image1></WEBOBJECT></TD>
       <TD COLSPAN=3></TD>
   </TR>
   ```
2. Edit `PageWrapper.wod` to
   specify the bindings for the WOImage. Add the following lines:

   ```
   Image1: WOImage {
       filename = "Apple-bw.gif";
       framework = "JavaDirectToWeb";
   }
   ```

Now all of the pages Direct to Web generates appear with the
Apple logo.

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Customizing_Application.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Using_Direc_pplications.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
