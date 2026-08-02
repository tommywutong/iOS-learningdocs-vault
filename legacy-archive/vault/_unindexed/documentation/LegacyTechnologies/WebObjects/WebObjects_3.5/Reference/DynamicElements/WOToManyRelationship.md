---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOToManyRelationship.html
archived_at: '2026-07-15T07:55:38.004148Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WOExtensionsTOC.md) [!Previous Section](WOStats.md)

## WOToManyRelationship

### Synopsis

**__WOToManyRelationship__ __{__ __sourceEntityName =__ _anEntity___; relationshipKey =__ _aKey___;__ __sourceObject =__ _anObject___;__ [__isMandatory =__ YES|NO__;__] [__destinationDisplayKey__ __=__ _aKey___;__] [__dataSource__ __=__ _aDataSource___;__] [__uiStyle = "browser"__ | __"checkbox"__ __;__] __};__**

### Description

The WOToManyRelationship component displays items from a to-many relationship in either a browser or a check-box list. Users can select one or more items from this list to learn more about those items.
For example, suppose you have a database of Movies where each movie is a table (or entity). Each movie has one or more roles, which means that the Movies table would have a to-many relationship with the MovieRoles table. You could use this component on a page that displays information about a movie, using this component to display the roles associated with this movie.
This component is used only in applications that access a database using the Enterprise Objects Framework. In particular, it is used if you use Direct to Web to create your application. Because WOToManyRelationship returns a form element, it must be used within an HTML form.

**__sourceEntityName__**
: The name of the entity that contains the relationship. In the Movies example, this would be "Movies."

**__relationshipKey__**
: The key for the relationship that you want to display. In the Movies example, you'd want to display the __roles__ key.

**__sourceObject__**
: An object that contains the actual relationship value. This object can be an enterprise object, a mutable dictionary, or anything else that can contain the relationship. Upon return, this object contains the user's selection.

**__isMandatory__**
: If YES, the relationship must exist. If the relationship must exist, the element must have at least one item selected when the form is submitted, so the WOToManyRelationship selects the first item if the list if the user has not selected any. If NO, the relationship is optional.

**__destinationDisplayKey__**
: Property to display in the list. For example, with the MovieRoles entity, you would want to display the __roleName__ property.

**__dataSource__**
: EODatabaseDatasource containing the items in the to-many relationship.

**__uiStyle__**
: If __"browser"__, displays as a browser. If __"checkbox"__, displays as a list of check boxes. The default depends on the number of items in the list. If there are less than 5 items, the default is a check-box list. If there are 5 items or more, the default is a browser.

[!Table of Contents](WOExtensionsTOC.md) [!Next Section](WOToOneRelationship.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
