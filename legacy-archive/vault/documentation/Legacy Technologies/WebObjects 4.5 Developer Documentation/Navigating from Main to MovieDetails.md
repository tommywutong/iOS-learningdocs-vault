---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.41.html
archived_at: '2026-07-15T08:07:59.545772Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Adding%20the%20MovieDetails%20Page.md) [!](Storing%20the%20Selected%20Movie.md) [!](Designing%20MovieDetails%27%20User%20Interface.md)

---

#  Navigating from Main to MovieDetails

To get to the MovieDetails page from the Main page, users use a hyperlink. Clicking the hyperlink should set MovieDetail's __selectedMovie__ variable and then open the MovieDetails page.

1. 

   Add a hyperlink at the bottom of the Main component.
2. 

   Replace the text "Hyperlink" with "Movie Details."!
3. 

   Choose Add Action from the pull-down list.
4. 

   In the Add Action panel, type showDetails in the Name field.
5. 

   Select MovieDetails from the "Page returned" combo box.
6. 

   Click Add.
7. 

   Bind the __showDetails__ action to the hyperlink's __action__ attribute.
8. 

   In Project Builder, modify the __showDetails__ action in __Main.java__ to look like the following:

   public MovieDetails showDetails() {

      MovieDetails nextPage =

   (MovieDetails)pageWithName("MovieDetails");

      // Initialize your component here

      EOEnterpriseObject selection =

        (EOEnterpriseObject)movieDisplayGroup.selectedObject();

      nextPage.setSelectedMovie(selection);

      return nextPage;

   }

   This method creates the MovieDetails page and then invokes its __setSelectedMovie__ method with the movie that's selected in the Main page. The display group method __selectedObject__ returns its selected object, which, in the Main component, is set when a user clicks a movie title hyperlink.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Adding%20the%20MovieDetails%20Page.md) [!](Storing%20the%20Selected%20Movie.md) [!](Designing%20MovieDetails%27%20User%20Interface.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
