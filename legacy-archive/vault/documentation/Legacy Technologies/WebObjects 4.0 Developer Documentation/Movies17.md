---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies17.html
archived_at: '2026-07-18T01:22:05.380255Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Movies16.md)

### Bindings in the Repetition Part

In the repetition part of the component where matching movies are listed, __movieDisplayGroup.displayedObjects__ is bound to a repetition. More specifically, __displayedObjects__ is bound to the repetition's __list__ attribute, providing an array of movies for the repetition to iterate over.
The __movie__ variable is bound to the repetition's __item__ attribute to hold each movie in turn, and __movie.title__ is bound to the string element inside the repetition. These bindings produce a list of movie titles.

!

The repetition's string element is enclosed in a hyperlink. By clicking a movie title, the user _selects_ the corresponding movie.

- Inspect the hyperlink.

Its __action__ attribute is bound to the action method __selectObject__.

!

- Look in the __Main.java__ class to see how the __selectObject__ method is implemented.

The method (shown below) simply sets __movieDisplayGroup__'s selected object to the movie the user clicked.

```
public void selectObject() {
    movieDisplayGroup.selectObject(movie);
}
```

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Movies18.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
