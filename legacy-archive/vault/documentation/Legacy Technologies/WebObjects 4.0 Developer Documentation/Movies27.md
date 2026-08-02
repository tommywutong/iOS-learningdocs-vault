---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies27.html
archived_at: '2026-07-18T01:22:25.669322Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Movies26.md)

## Navigating from Main to MovieDetails

To get to the MovieDetails page from the Main page, users use a hyperlink. Clicking the hyperlink should set MovieDetail's __selectedMovie__ variable and then open the MovieDetails page.

- Add a hyperlink at the bottom of the Main component.
- Replace the text "Hyperlink" with "Movie Details."

!

- Choose Add Action from the pull-down menu.
- In the Add Action panel, type showDetails in the Name field.
- Select MovieDetails from the "Page returned" pull-down menu.
- Click Add.
- Bind the __showDetails__ action to the hyperlink's __action__ attribute.
- In Project Builder, modify the __showDetails__ action in __Main.java__ to look like the following:

```
public MovieDetails showDetails() {
    MovieDetails nextPage =
        (MovieDetails)pageWithName("MovieDetails");

    // Initialize your component here
    EOEnterpriseObject selection =
        (EOEnterpriseObject)movieDisplayGroup.selectedObject();
    nextPage.setSelectedMovie(selection);

    return nextPage;
}
```


This method creates the MovieDetails page and then invokes its __setSelectedMovie__ method with the movie that's selected in the Main page. The display group method __selectedObject__ returns its selected object, which, in the Main component, is set when a user clicks a movie title hyperlink.

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Movies28.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
