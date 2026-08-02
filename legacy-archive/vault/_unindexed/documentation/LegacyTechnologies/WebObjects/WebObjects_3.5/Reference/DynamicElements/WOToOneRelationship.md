---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOToOneRelationship.html
archived_at: '2026-07-15T07:55:38.431335Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WOExtensionsTOC.md) [!Previous Section](WOToManyRelationship.md)

## WOToOneRelationship

### Synopsis

**__WOToOneRelationship__ __{ sourceEntityName =__ _anEntity___; relationshipKey =__ _aKey___;__ __sourceObject =__ _anObject___;__ [__dataSource =__ _aDataSource___;__][__destinationDisplayKey =__ _aKey___;__][__isMandatory =__ YES|NO__;__] [__uiStyle = "radio"__|__"popup"__|__"browser";__] __};__**

### Description

The WOToOneRelationship component displays items from a to-one relationship in a pop-up list, a radio button list, or a browser. Users can select an item from this list to learn more about that item.
For example, suppose you have a database of Movies where each movie is a table (or entity). Each movie has only one studio, which means that the Movies table would have a to-one relationship with the Studios table. You could use this component on a page that displays information about a movie, using this component to display the studio associated with the movie.
This component is used only in applications that access a database using the Enterprise Objects Framework. In particular, it is used if you use Direct to Web to create your application. Because WOToOneRelationship returns a form element, it must be used within an HTML form.

**__sourceEntityName__**
: The name of the entity that contains the relationship. In the Movies example, this would be "Movies."

**__relationshipKey__**
: The key for the relationship that you want to display. In the Movies example, you'd want to display the __studios__ key.

**__sourceObject__**
: An object that contains the actual relationship value. This object can be an enterprise object, a mutable dictionary, or anything else that can contain the relationship. Upon return, this object contains the user's selection.

**__dataSource__**
: EODatabaseDataSource containing the items in the to-one relationship.

**__destinationDisplayKey__**
: Property to display in the list. For example, with the Studio entity, you would want to display the __name__ property.

**__isMandatory__**
: If YES, the relationship must exist. If NO, the relationship is optional.

**__uiStyle__**
: Specifies how to display the list: as a browser, a radio button list, or a pop-up list. The default depends on the number of items in the list. If there are less than 5 items, the default is a radio button list. If between 5 and 20 items, the default is a pop-up list. If there are more than 20 items, a browser is used.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
