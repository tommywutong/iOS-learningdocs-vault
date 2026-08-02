---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOCustomObjects/Using_Custom_Logic.html
archived_at: '2026-07-15T08:13:00.796173Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

## Using Custom Logic

In this section you'll modify `Main.wo` to
use the `fullName` property
of Author to display an author's full name.

1. Open the `Main.wo` component
   in WebObjects Builder.

   [Figure 11-1](#apple-ijauuqskjfeec) shows that WebObjects
   Builder recognizes the type of `authorItem` as Author.
   Also, a browser for the Author class appears next to the browser
   for the Main class. Notice that the new method, `fullName`,
   is represented as a property of the `authorItem` variable.

   __Figure
   11-1 Main.wo after adding the fullName
   derived property to Author.java__

   ![[image: ../Art/authorsmainwo2.gif]](../Art/authorsmainwo2.gif)
2. Remove the comma and the WOString that displays `authorItem.firstName`.
3. Bind the remaining WOString's `value` attribute
   to `authorItem.fullName`.
   You can now use the drag method to perform the binding because WebObjects
   Builder has more information about `authorItem` than
   when it was an EOGenericRecord. Your component should look like [Figure 11-2](#apple-ijbusscjijdeg).

   __Figure
   11-2 Main.wo using the fullName derived
   property__

   ![[image: ../Art/authorsmainwo3.gif]](../Art/authorsmainwo3.gif)
4. Save `Main.wo`, and
   build and run the application.

   [Figure 11-3](#apple-ijauurckjjcek) shows that when an author's
   first name is missing, the comma is not displayed, as it was before.

__Figure
11-3 The Authors application using the
fullName method to display author information__

![[image: ../Art/authorsie2.gif]](../Art/authorsie2.gif)

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Adding_Custom_Logic.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Setting_Default_Values.md)

---

© 2001 Apple Computer, Inc.

Shop the [Apple Online Store](http://www.apple.com/store/) (1-800-MY-APPLE), visit an [Apple Retail Store](http://www.apple.com/retail/), or find a [reseller](http://www.apple.com/buy/locator/).

- [Mailing Lists](http://lists.apple.com/)
- [RSS Feeds](https://developer.apple.com/rss/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
