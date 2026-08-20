---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies27.html
archived_at: '2026-07-15T07:54:31.479417Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies26.md)

## Navigating from Main to MovieDetails

To get to the MovieDetails page from the Main page, users use a hyperlink. Clicking the hyperlink should set MovieDetail's __selectedMovie__ variable and then open the MovieDetails page.

- Add a hyperlink at the bottom of the Main component.
- Replace the text "Hyperlink" with "Movie Details."
!- Choose Add Action from the pull-down menu.
- In the Add Action panel, type showDetails in the Name field.
- Type MovieDetails in the "Page returned" field.
- Click Add.
- Bind the __showDetails__ action to the hyperlink's __action__ attribute.
- In Project Builder, modify the __showDetails__ action to look like the following:

```
public Component showDetails()
{
    MovieDetails nextPage =
        (MovieDetails)application().pageWithName("MovieDetails");
    EnterpriseObject selection =
        (EnterpriseObject)movieDisplayGroup.selectedObject();

    nextPage.setSelectedMovie(selection);
    return nextPage;
}
```


This method creates the MovieDetails page and then invokes its __setSelectedMovie__ method with the movie that's selected in the Main page. The display group method __selectedObject__ returns its selected object, which, in the Main component, is set when a user clicks a movie title hyperlink.

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies28.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
