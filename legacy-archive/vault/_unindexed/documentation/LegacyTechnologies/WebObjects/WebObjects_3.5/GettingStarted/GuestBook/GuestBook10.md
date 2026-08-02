---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/GuestBook/GuestBook10.html
archived_at: '2026-07-15T07:53:17.495145Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBookTOC.md) [!Previous Section](GuestBook9.md)

# Binding Elements

When a user enters information in GuestBook's form elements, your application needs a way of accessing that information. This is done by _binding_ the form elements to variables in your application. When the user submits the form, WebObjects puts the data into the variables you've specified.
Then, your application typically processes the data and returns a new page (or the same page) displaying information that makes sense based on the user's input. The information displayed is usually represented by other dynamic elements that are bound to variables and methods in your code.
This process of receiving a request (triggered by actions such as submitting a form or clicking a hyperlink) and responding by returning a page is known as the _request-response loop__._ This loop is at the heart of WebObjects programming.
In this tutorial, you'll have WebObjects return the same page, with the information you received from the user displayed, in a slightly different format, at the bottom. In the second chapter, you'll add an additional page to your application.

[!Table of Contents](GuestBookTOC.md) [!Next Section](GuestBook11.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
