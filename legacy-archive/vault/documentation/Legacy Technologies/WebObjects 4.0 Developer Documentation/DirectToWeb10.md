---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb10.html
archived_at: '2026-07-18T01:24:15.982760Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DirectToWeb9.md)

### Edit-Relationship Pages

An edit-relationship page allows users to add records to a relationship and remove records from the relationship. Users typically come to these pages when they click an Edit button next to a relationship in an edit page. Edit-relationship pages consist of three separate components, of which two are shown at any one time. The first component is a browser that lists the to-many relationships of a particular property and contains several controls. In addition to the browser, a query component initially appears for locating another object to link to for that property.

!

This user interface facilitates the following tasks:

- To remove a record from the property, select the key identifying the record in the browser and click Remove.
- To add a new record to the property, click New Record. An edit component appears underneath the list of relationships; fill out the fields of the edit component and click Save to add the new record to the database _and_ the new relationship to the property above.
- To locate an existing record to add to the relationship, enter the properties to search on in the query component and click Query DB.

When a query is executed (assuming matching records are found) a select component replaces the query component.

!

To add a listed record to the to-many relationship, click the Select button. To construct a new query, click the Build Query button.
When you have finished editing a to-many relationship, click the Return button under the browser to return to the original edit page. You must click the Save button in this page to store the changed relationship in the database.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DirectToWeb11.md)
