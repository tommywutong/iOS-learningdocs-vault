---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb27.html
archived_at: '2026-07-18T01:24:57.483266Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DirectToWeb26.md)

### Setting Up a Next-Page Callback

For query pages, you must create a component implementing the QueryPageInterface, and this component must create a callback object (an object that implements the NextPageCallback interface) that is pushed back into the page with the component is returned. When the submit button is clicked for the query (Query DB), the callback method is invoked.Here is an example of how to provide a callback:

```
public WOComponent d2wList() {
    QueryPageInterface qpi=D2W.factory().queryPageForEntityNamed("Movie",
session());
    qpi.setNextPageCallback(new NextPageCallback() {
        public WOComponent nextPage(WOComponent sender) {
            EODataSource=((QueryPageInterface)sender).queryDataSource();
            myDisplayGroup.setDataSource(dataSource);
            movieDisplayGroup.fetch();
            return MyComponent.this;
            }
        });
    return (WOComponent) qpi;
}
```

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Deploying%20a%20Direct%20To%20Web%20Application.md)
