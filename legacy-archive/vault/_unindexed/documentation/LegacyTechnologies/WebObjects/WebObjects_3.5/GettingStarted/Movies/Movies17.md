---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies17.html
archived_at: '2026-07-15T07:54:16.739411Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies16.md)

### Bindings in the Repetition Part

In the repetition part of the component where matching movies are listed, __movieDisplayGroup.displayedObjects__ is bound to a repetition. More specifically, __displayedObjects__ is bound to the repetition's __list__ attribute, providing a vector of movies for the repetition to iterate over.
The __movie__ variable is bound to the repetition's __item__ attribute to hold each movie in turn, and __movie.title__ is bound to the string element inside the repetition. These bindings produce a list of movie titles.!
The repetition's string element is enclosed in a hyperlink. By clicking a movie title, the user _selects_ the corresponding movie.

- Inspect the hyperlink.

Its __action__ attribute is bound to the action method __selectObject__.

!- Look in the __Main.java__ class to see how __selectObject__ is implemented.

The method (shown below) simply sets __movieDisplayGroup__'s selected object to the movie the user clicked.

```
public void selectObject() {
    movieDisplayGroup.selectObject(movie);
}
```

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies18.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
