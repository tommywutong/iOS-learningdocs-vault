---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies11.html
archived_at: '2026-07-15T07:54:10.696297Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies10.md)

## Choosing Attributes to Display

The next step is to choose which of the Movie entity's attributes to display in the editing part at the bottom of the page.

- Move attributes from the Don't Include list to the Include list.
!

The order in which you add the attributes determines the order in which they appear on the page, so add them in the following order: __title__, __category__, __rating__, __dateReleased__, and __revenue__.

Don't add any of the remaining attributes (__language__, __movieId__, and __studioId__). They don't have meaning to users, and should not be displayed in the page.

- Click Next.

## Choosing an Attribute to Display as a Hyperlink

You now need to specify the attribute used in the repetition part of the page to identify each record. This attribute will be displayed as a hyperlink. Clicking the hyperlink displays the corresponding record in the detail part of the page.

- Add the __title__ attribute to the Include browser.
- Click Next.

## Choosing Attributes to Query On

Specify the attributes to display in the query part of the page. The wizard creates search criteria fields for each of the attributes you choose.

- Add the __title__, __category__, and __rating__ attributes to the Include browser.
- Click Finish.

When the wizard finishes, your new project is displayed in Project Builder. The wizard has produced all the files and resources for a fully functional, one-page application. All you need to do before running your Movies application is build it.

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies12.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
