---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.42.html
archived_at: '2026-07-15T08:08:00.447936Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Adding%20the%20MovieDetails%20Page.md) [!](Navigating%20from%20Main%20to%20MovieDetails.md) [!](Adding%20Date%20and%20Number%20Formats.md)

---

#  Designing MovieDetails' User Interface

Now lay out the user interface for MovieDetails. When you're done, your component should look like the following:!

1. 

   Create a top-level heading with the text Movie Details.

   Recall that to create a top-level heading, you type the text of the heading, select the text, click the ! button to add a heading element around the text, and then use the Inspector to set the heading's level, as you did in [Using the Inspector](Using%20the%20Inspector.md#apple-gi4dcobt)
   .
2. 

   Below the heading, add a string element.
3. 

   With the string element selected, add a heading.

   This adds a new level-1 heading element around the string. The MovieDetails page will show the title of the selected movie in this heading.
4. 

   Click <H1> in the path view. The Inspector now displays the Heading Level.
5. 

   Click 3 in the Heading Inspector.
6. 

   Add labels and string elements to display the selected movie's category, date released, and revenue.
7. 

   Bold the labels.
8. 

   Bind __selectedMovie__.__title__ to the __value__ attribute of the first string element (the one in the heading).
9. 

   Similarly, create bindings for the Category, Date Released, and Revenue strings.
10. 

    At the bottom of the page, add a horizontal rule.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Adding%20the%20MovieDetails%20Page.md) [!](Navigating%20from%20Main%20to%20MovieDetails.md) [!](Adding%20Date%20and%20Number%20Formats.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
