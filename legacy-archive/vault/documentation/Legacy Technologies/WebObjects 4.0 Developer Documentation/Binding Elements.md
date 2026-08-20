---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/GuestBook/BindingElements.html
archived_at: '2026-07-18T01:20:43.852763Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20Simple%20WebObjects%20Application.md) [!Previous Section](ResizingFormElements.md)

# Binding Elements

When a user enters information in GuestBook's form elements, your application needs a way of accessing that information. This is done by _binding_ the form elements to variables in your application. When the user submits the form, WebObjects puts the data into the variables you've specified.
Your application typically processes the data and returns a new page (or the same page) displaying information that makes sense based on the user's input. The information displayed is usually represented by other dynamic elements that are bound to variables and methods in your code.
This process of receiving a request (triggered by actions such as submitting a form or clicking a hyperlink) and responding by returning a page is known as the _request-response loop__._ This loop is at the heart of WebObjects programming.
In this tutorial, you'll have WebObjects return the same page, with the information you received from the user displayed in a slightly different format at the bottom.

[!Table of Contents](Creating%20a%20Simple%20WebObjects%20Application.md) [!Next Section](CreatingVariables.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
