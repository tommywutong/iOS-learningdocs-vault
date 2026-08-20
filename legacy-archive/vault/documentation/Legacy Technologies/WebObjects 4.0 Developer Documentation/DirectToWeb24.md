---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb24.html
archived_at: '2026-07-18T01:24:57.230447Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](Using%20Direct%20to%20Web%20in%20Other%20WebObjects%20Applications.md)

### Direct to Web Component Reference

The current release defines five Direct to Web components in the __DirectToWeb__ framework.
D2WQuery
For information on the behavior and appearance of this component see ["Query Pages"](DirectToWeb7.md#apple-guytkni)__.

|  __Bindings__ |  Comments |
|  entityName |  The name of the entity for this query (NSString) |
|  displayKeys |  The properties of the entity to display for the query (NSArray or NSString) |
|  queryDataSource |  The data source for the query |
|  action |  The action method to invoke when Query DB is clicked. The __queryDataSource__ is pushed onto your page before this action is invoked. |

|  |
| --- |
|  |__

__Example__:

```
myQuery : D2WQuery {
    entityName = "Movie";
    displayKeys = "(title, roles)";
    queryDataSource = displayGroup.dataSource;
    action = displayGroup.fetch;
}

 D2WList
```


For information on the behavior and appearance of this component see ["List Pages and Select Components"](Using%20Direct%20to%20Web%20in%20Other%20WebObjects%20Applications.md#apple-gezdqmzt)__.

|  Bindings |  Comments |
|  entityName |  The name of the entity for this list (NSString) |
|  dataSource |  The data source for the list |
|  displayKeys |  The properties of the entity to display (NSArray or NSString) |

|  |
| --- |
|  |__

__Example__:

```
myList : D2WList {
    entityName = "Movie";
    dataSource = displayGroup.dataSource;
    displayKeys = "(title, roles)";
}

 D2WSelect
```


For information on the behavior and appearance of this component see ["List Pages and Select Components"](Using%20Direct%20to%20Web%20in%20Other%20WebObjects%20Applications.md#apple-gezdqmzt)__.

|  Bindings |  Comments |
|  entityName |  The name of the entity for this list (NSString) |
|  displayKeys |  The properties of the entity to display (NSArray or NSString) |
|  selectedObject |  Returns the object associated with the clicked Select button. |
|  dataSource |  The data source for the list |
|  action |  The action method to invoke when the Select button is clicked. The selectedObject is pushed onto your page before this method is invoked |

|  |
| --- |
|  |__

__Example__:

```
mySelect : D2WSelect {
    entityName = "Movie";
    selectedObject = displayGroup.selectedObject;
    dataSource = displayGroup.dataSource;
    action = selectAction;
}

 D2WInspect
```


For information on the behavior and appearance of this component see ["Inspect and Edit Pages"](DirectToWeb9.md#apple-guytmni)__.

|  Bindings |  Comments |
|  entityName |  The name of the entity for this record (NSString) |
|  object |  Returns the object associated with the clicked Inspect button. |
|  action |  The action method to invoke when the Return button is clicked |
|  displayKeys |  The properties of the entity to display (NSArray or NSString) |

|  |
| --- |
|  |__

__Example__:

```
myInspect : D2WInspect {
    entityName = "Movie";
    object = displayGroup.selectedObject;
    action = editAction;
}

 D2WEdit
```


For information on the behavior and appearance of this component see ["Inspect and Edit Pages"](DirectToWeb9.md#apple-guytmni)__.

|  Bindings |  Comments |
|  entityName |  The name of the entity for this record (NSString) |
|  object |  Returns the object associated with the clicked Edit button. |
|  action |  The action method to invoke when the Edit button is clicked |
|  displayKeys |  The properties of the entity to display (NSArray or NSString) |

|  |
| --- |
|  |__

__Example__:

```
myEdit : D2WEdit {
    entityName = "Movie";
    object = displayGroup.selectedObject;
    action = editAction;
}
```

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DirectToWeb25.md)
