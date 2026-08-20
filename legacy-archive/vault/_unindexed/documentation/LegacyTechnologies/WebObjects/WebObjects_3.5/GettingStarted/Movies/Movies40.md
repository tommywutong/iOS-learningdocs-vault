---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies40.html
archived_at: '2026-07-15T07:54:53.859103Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies39.md)

## Managing a DisplayGroup's Selection

Remember how clicking a movie title in the Main page selects the corresponding Movie object in __movieDisplayGroup__. MovieDetails has a similar behavior for selecting a MovieRole object in __movieRoleDisplayGroup__.
First you need to add a hyperlink element around the repetition's role name string so that users can select a particular MovieRole. When a user clicks one of the movie role hyperlinks, the application should select the corresponding MovieRole object in the __movieRoleDisplayGroup__.

- Select the repetition's role name string element.
- Click the Add WOHyperlink button in the Other WebObjects toolbar to add a hyperlink element around the string.

Now you need to create an action method to invoke when the hyperlink is clicked.

- Use the Add Action command in the pull-down menu to add an action named __selectObject__, returning __null__.

Before you write the body of the __selectObject__ method, bind it to the hyperlink while you're still in WebObjects Builder.

- Bind the __selectObject__ method to the hyperlink's __action__ attribute.

Now write the code for __selectObject__ in __MovieDetail.java__.

- Modify the __selectObject__ action to look like the following:

```
    public Component selectObject()
    {
        movieRoleDisplayGroup.selectObject(movieRole);
        return null;
    }
```

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies41.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
