---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/Introduction/Dynamic_HTML_Publishing.html
archived_at: '2026-07-15T08:15:07.715706Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](What_Is_WebObjects.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Web_Enabled_pplications.md)

## Dynamic HTML Publishing

Much of the content on the Web is textual or graphical material
that doesn't change much over time. However, there is increasing
demand for sites that publish ever-changing data: breaking news
stories, up-to-the-minute stock quotes, or the current weather are
good examples.

A typical website is organized like [Figure 2-1](#apple-ijauer2cjfcui). A user's Web browser
requests pages using URLs (Uniform Resource Locators). These requests
are sent over the network to the Web server, which analyzes each
request and selects the appropriate Web page to return to the user's
browser. This Web page is simply a text file that contains HTML.
Using the HTML tags embedded within the file received from the Web
server, the browser renders the page.

__Figure
2-1 A static publishing site__

![[image: ../Art/StaticPublishing.gif]](../Art/StaticPublishing.gif)

Static publishing sites are easy to maintain. There are a
number of tools on the market that allow you to create HTML pages
with a relatively small amount of effort, and as long as the page
content doesn't change too often, it isn't that difficult to
keep them up-to-date. Dynamic publishing sites, however, are a different
story. Without WebObjects it could take a small army to keep a breaking
news site up to date.

WebObjects was designed from the beginning to allow you to
quickly and easily publish dynamic data over the Web. You create
HTML templates that indicate where on the Web page the dynamic data
is to be placed, and a WebObjects application fills in the content when
your application is accessed. The process is much like a mail merge.
The information your Web pages publish can reside in a database,
it can reside in some other permanent data storage (files, perhaps),
or it can even be calculated or generated at the time a page is accessed.
The pages are also highly interactive-you can fully specify the
way the user navigates through them.

[Figure 2-2](#apple-ijaueq2bivceg) shows a WebObjects-based dynamic publishing site.
Again, the request (in the form of a URL) originates with a client
browser. If the Web server detects that the request is to be handled
by WebObjects, it passes the request to a WebObjects adaptor. The
adaptor packages the incoming request in a form the WebObjects application
can understand and forwards it to the application. Based upon templates
you've defined and the relevant data from the data store, the
application generates an HTML page that it passes back through the
adaptor to the Web server. The Web server sends the page to the
client browser, which renders it.

__Figure
2-2 A dynamic publishing site__

![[image: ../Art/DynamicPublishing.gif]](../Art/DynamicPublishing.gif)

This type of WebObjects application is referred to as "HTML-based,"
since the result is a series of dynamically generated HTML pages.

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](What_Is_WebObjects.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Web_Enabled_pplications.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
