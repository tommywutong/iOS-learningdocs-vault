---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies36.html
archived_at: '2026-07-18T01:22:41.648954Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Setting%20Up%20a%20Master-Detail%20Configuration.md)

## Creating a Detail Display Group

You can create a detail display group several different ways. You can write a declaration for it in Project Builder, or you can use WebObjects Builder's Add Variable/Method command. But the easiest way to create a detail display group is by dragging a relationship from EOModeler into your component, as described below.

- In EOModeler's tree view, expand the Movie entity.

!

- Drag the Movie's __toMovieRole__ relationship from the tree view into the MovieDetails component's object browser.

!

An Add Display Group panel opens.

!

- In the Add Display Group panel, change the name to movieRoleDisplayGroup.
- Click Add and Configure.

The Display Group Options panel opens so you can immediately configure the newly created display group.

!

Ensure that the "Has detail data source" box is checked. This means that __movieRoleDisplayGroup__ gets its objects from a EODetailDataSource object.

All display groups use some kind of _data source_ to fetch their objects. A data source is an object that exists primarily as a simple means for a WODisplayGroup to access a store of objects. It's through a data source that a display group fetches, inserts, updates, and deletes database records.

A EODetailDataSource is a subclass of DataSource that's intended for use in master-detail configurations. A detail data source keeps track of a _master object_ and a _detail key_. The master object is typically the selected object in a master display group, but a master display group isn't strictly required. The detail key is the name of the relationship on which the master-detail configuration is based.

When a detail display group asks its data source to fetch, the EODetailDataSource simply gets the destination objects from the master object as follows:

```
detailObjects = masterObject.valueForKey(detailKey);
```


In your master-detail configuration, the master object is the selected Movie, and the detail key is __toMovieRole__. When __movieRoleDisplayGroup__ asks its data source for its MovieRole objects, the detail WODisplayGroup returns the objects in the selected Movie's __toMovieRole__ array of MovieRoles. Similarly, when MovieRole objects are inserted or deleted in __movieRoleDisplayGroup__, they are added and removed from the master object's __toMovieRole__ array.

- Set the display group to sort alphabetically by __roleName__.
- Check the "Fetches on load" box.

When "Fetches on load" is selected, the display group fetches its objects as soon as the component is loaded into the application. You want this feature in the MovieDetails page so that users are immediately presented with the selected movie's roles. In contrast, the Main page does not fetch on load; it shouldn't present a list of movies until the user has entered search criteria and clicked Match.

- Click OK.
- In Project Builder, modify MovieDetail's __setSelectedMovie__ method to look like the following:

```
public void setSelectedMovie(EOEnterpriseObject
newSelectedMovie) {
    selectedMovie = newSelectedMovie;
    movieRoleDisplayGroup.setMasterObject(newSelectedMovie);
}
```


With this addition, whenever a user navigates to the MovieDetails page, __setSelectedMovie__ updates the __movieRoleDisplayGroup__'s master object so it displays the corresponding MovieRole objects.

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Movies37.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
