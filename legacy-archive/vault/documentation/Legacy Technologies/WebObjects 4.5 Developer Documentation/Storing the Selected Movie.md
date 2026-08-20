---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.40.html
archived_at: '2026-07-15T08:07:58.490834Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Adding%20the%20MovieDetails%20Page.md) [!](Creating%20the%20MovieDetails%20Component.md) [!](Navigating%20from%20Main%20to%20MovieDetails.md)

---

#  Storing the Selected Movie

Now, in the MovieDetails component, create a variable that holds the application's selected movie. Later on, you'll add code to the __Main.java__ class that assigns Main's selected movie to this variable.

1. 

   Choose Add Key from the pull-down list.!
2. 

   Name the variable selectedMovie.
3. 

   Set the variable's type to Movie.

   Movie isn't actually a class; it's an entity. It's listed in the combo box as a type along with entries for all the entities in your model. When you choose an entity as the type for your variable, WebObjects Builder recognizes that the variable is an enterprise object. Using information in the model, WebObjects Builder can determine the entity's corresponding enterprise object class and the properties of that class.
4. 

   Check the "An instance variable" box.
5. 

   Check the "A method returning the value" box.
6. 

   Check the "A method setting the value" box.
7. 

   Click Add.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Adding%20the%20MovieDetails%20Page.md) [!](Creating%20the%20MovieDetails%20Component.md) [!](Navigating%20from%20Main%20to%20MovieDetails.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
