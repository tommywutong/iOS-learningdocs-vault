---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies29.html
archived_at: '2026-07-15T07:54:34.298890Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies28.md)

## Adding Date and Number Formats

String elements have __dateformat__ and __numberformat__ attributes just like text field elements. Create bindings for the Date Released and Revenue strings so that __dateReleased__ and __revenue__ values are displayed the way they are in the Main page.

- Add the date format "%d %b %Y" to the Date Released string.
- Add the number format "$ #,##0.00" to the Revenue string.

## Navigating from MovieDetails to Main

Now add a hyperlink to the MovieDetails page so users can navigate back to the Main page from MovieDetails.

- Add a hyperlink to the bottom of the page.
- Label it MovieSearch.
!- Bind the hyperlink's __pageName__ attribute to the text (including the quotes) "Main".

Recall that the __pageName__ attribute is a mechanism for navigating to another page without writing code. By setting the attribute to "Main", you're telling the application to open the MovieSearch page when the hyperlink is clicked.

## Running Movies

Be sure that all your project's files are saved (including the components in WebObjects Builder), and build and run your application. In the Main page, select a movie and click the Movie Details link. The MovieDetails page should display all the movie's information.

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies30.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
