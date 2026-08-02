---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.43a.html
archived_at: '2026-07-15T08:08:02.490414Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Adding%20the%20MovieDetails%20Page.md) [!](Adding%20Date%20and%20Number%20Formats.md) [!](Running%20Movies-2.md)

---

#  Navigating from MovieDetails to Main

###  Navigating from MovieDetails to Main

Now add a hyperlink to the MovieDetails page so users can navigate back to the Main page from MovieDetails.

1. 

   Add a hyperlink to the bottom of the page.
2. 

   Label it Movie Search.!
3. 

   Bind the hyperlink's __pageName__ attribute to the text (including the quotes) "Main". You can select "Main" from the combo box in the inspector's binding column.

   Recall that the __pageName__ attribute is a mechanism for navigating to another page without writing code. By setting the attribute to "Main", you're telling the application to open the MovieSearch page when the hyperlink is clicked.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Adding%20the%20MovieDetails%20Page.md) [!](Adding%20Date%20and%20Number%20Formats.md) [!](Running%20Movies-2.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
