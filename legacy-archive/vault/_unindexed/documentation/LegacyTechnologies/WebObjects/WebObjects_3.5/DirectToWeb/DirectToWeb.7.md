---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DirectToWeb/DirectToWeb.7.html
archived_at: '2026-07-15T07:53:00.485104Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.6.md)[Previous
Section](DirectToWeb.6.md) 

##   Inspect and Edit Pages

Inspect pages and edit pages display the data for a single record of an entity. An edit page allows you to make changes to the record and save the changes, while an inspect page is read-only.

An inspect page looks like this:

##### 

!

Note the buttons at the bottom of the page:

- 

  Delete allows you to delete the record from the database.
- 

  Cancel takes you back to the page from which you accessed this inspect page.
- 

  Edit brings up the equivalent edit page for this record, so that you can make changes.

_Note:_
If your model specifies a particular entity as read-only, you won't be able to edit it in a Direct to Web application.

An edit page looks like this:

##### 

!

It is similar to the inspect page, except that it has a Save button (for saving changes to the database) instead of an Edit button.

For best results when navigating through a Direct to Web application, don't use your web browser's backtrack buttons. Instead:

- 

  To return to the previous page from an edit or inspect page, click Cancel.
- 

  To return to a query page from a list page, select the entity in the Entities pop-up list and click Build Query.

[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.8.md)[Next
Section](DirectToWeb.8.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
