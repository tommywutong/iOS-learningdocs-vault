---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies28.html
archived_at: '2026-07-18T01:22:26.138000Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Movies27.md)

## Designing MovieDetails' User Interface

Now lay out the user interface for MovieDetails. When you're done, your component should look like the following:

!

- Create a top-level heading with the text Movie Details.

Recall that to create a top-level heading, you type the text of the heading, select the text, click the ! button to add a heading element around the text, and then use the Inspector to set the heading's level, as you did in [Using the Inspector](UsingInspector.md#apple-guzdgnq).

- Below the heading, add a string element.
- With the string element selected, add a heading.

This adds a new level 3 heading element around the string. The MovieDetails page will show the title of the selected movie in this heading.

- Add labels and string elements to display the selected movie's category, date released, and revenue.
- Bold the labels.
- Bind __selectedMovie__.__title__ to the __value__ attribute of the first string element (the one in the heading).
- Similarly, create bindings for the Category, Date Released, and Revenue strings.
- At the bottom of the page, add a horizontal rule.

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Movies29.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
