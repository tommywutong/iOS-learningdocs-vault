---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies25.html
archived_at: '2026-07-18T01:22:24.997029Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Movies24.md)

# Adding the MovieDetails Page

The MovieDetails page shows you the detailed information about a movie you select in the Main page. For this to work, the Main page has to tell the MovieDetails page which movie the user selected. The MovieDetails page keeps track of the selected movie in its own instance variable. In this section, you'll:

- Create a new component whose interface you'll create yourself.
- Assign Main's selected movie to a variable in the MovieDetails page.
- Create a way to navigate from Main to MovieDetails and back.

In the sections following this one, you'll extend the MovieDetails page to display movie roles and the starring actors.

## Creating the MovieDetails Component

- In Project Builder, choose File ! New in Project.
- In the New File panel, click the Web Components suitcase.
- Type MovieDetails in the Name field.
- Click OK.
- In the wizard panel, choose None from the available assistance.
- Choose Java as the component language.
- Click Finish.
- Open the new component, __MovieDetails.wo__, in WebObjects Builder.

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Movies26.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
