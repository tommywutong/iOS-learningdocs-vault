---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb26.html
archived_at: '2026-07-18T01:24:57.408801Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DirectToWeb25.md)

### Implementing the Action Method

To implement the action methods needed for linking to Direct to Web pages you must use methods of the D2W class and the page-specific Direct to Web interfaces. You also need to specify a hyperlink, active image, or similar HTML control with which to invoke the action method. Take the following example of a hyperlink; first, the HTML WebObjects tag:

```
<webObject name=D2WListPage>D2W list page</webObject>
```


Then, in the __.wod__ file, bind the hyperlink to the action:

```
D2WListPage: WOHyperlink {
    action = d2wList;
}
```


The method for linking to a Direct to Web page must return a component (that is, a WOComponent object) that implements the interface appropriate to the required type of page. For example, if you want to link to a dynamically generated list page, the component returned must implement the ListPageInterface interface. Fortunately, the D2W class provides methods that create such components:

```
public WOComponent d2wList() {
        ListPageInterface
lpi=D2W.factory().listPageForEntityNamed("Movie",session());
        lpi.setDataSource(movieDisplayGroup.dataSource());
        lpi.setNextPage(this);
        return (WOComponent)lpi;
    }
```


Notice that before you return the component, you must set things such as the data source for the component and the page to go to when users click the Return button (__setNextPage__).

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DirectToWeb27.md)
