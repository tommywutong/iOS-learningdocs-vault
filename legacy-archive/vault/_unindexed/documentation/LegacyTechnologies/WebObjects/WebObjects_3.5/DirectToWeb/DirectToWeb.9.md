---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DirectToWeb/DirectToWeb.9.html
archived_at: '2026-07-15T07:53:04.948384Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.8.md)[Previous
Section](DirectToWeb.8.md) 

##   The Direct to Web Components

The Direct to Web Framework consists of a number of components that are used to generate the pages you see in your application. Each property in a query, list, edit, or inspect page is shown in a default way.

For example, the figure below shows a list page for the Movie entity. It illustrates some of the components that can be used to display properties.

##### 

!

The Studio, Directors, and Roles properties are relationships:

- 

  Roles is a to-many relationship that is displayed using the DisplayToManyFault component. "Fault" indicates that the records in the relationship aren't displayed until they are asked for; that is, until the user clicks Inspect. When you click Inspect, a list page appears, showing all the records in the relationship (that is, all roles in the movie).

By default, all to-many relationships are displayed using DisplayToManyFault, and to-one relationships use DisplayToOneFault.

- 

  The Directors relationship is also a to-many relationship (because a movie can possibly have more than one director). To display it as shown in the figure, you would select Directors in the WebAssistant and click Pick to display a list of components to use.

_Note:_
If Pick is disabled, there is no choice of components for the selected property.

##### 

!

In this example, the DisplayToMany component is used to display the directors. This component shows all the records in the relationship, identified by a target key, which you also select from a list. The target keys for Directors are __firstName__
and __lastName__
. In addition, Direct to Web provides a default key called __userPresentableDescription__
, which is usually a combination of the relationship's keys. The example shown in the list page above uses this key to show both the last and first names of the directors.

__Note:__
In the example shown, there happens to be only one director per movie.

- 

  The Studio relationship is a to-one relationship. Therefore, there is only one target record in the relationship. As shown in the figure below, it uses the DisplayToOne component with the __name__
  target key. Therefore, in the list page, the studio's name appears in the Studio column, as a hyperlink that you can click to bring up an inspect page for the studio.

##### 

!

[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.a.md)[Next
Section](DirectToWeb.a.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
