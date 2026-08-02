---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.37.html
archived_at: '2026-07-18T01:29:46.077392Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Examining%20the%20Bindings.md) [!](Bindings%20in%20the%20Query%20Part.md) [!](Bindings%20in%20the%20Editing%20Part.md)

---

#  Bindings in the Repetition Part

In the repetition part of the component where matching movies are listed, __movieDisplayGroup.displayedObjects__ is bound to a repetition. More specifically, __displayedObjects__ is bound to the repetition's __list__ attribute, providing an array of movies for the repetition to iterate over.

The __movie__ variable is bound to the repetition's __item__ attribute to hold each movie in turn, and __movie.title__ is bound to the string element inside the repetition. These bindings produce a list of movie titles.!

The repetition's string element is enclosed in a hyperlink. By clicking a movie title, the user _selects_ the corresponding movie.

1. 

   Inspect the hyperlink.`

   Its __action__ attribute is bound to the action method __selectObject__.

   !
2. 

   Look in the __Main.java__ class to see how the __selectObject__ method is implemented.`

   The method (shown below) simply sets the selected object of __movieDisplayGroup__ to the movie the user clicked.

   public void selectObject() {
   movieDisplayGroup.selectObject(movie);
   }

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Examining%20the%20Bindings.md) [!](Bindings%20in%20the%20Query%20Part.md) [!](Bindings%20in%20the%20Editing%20Part.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
