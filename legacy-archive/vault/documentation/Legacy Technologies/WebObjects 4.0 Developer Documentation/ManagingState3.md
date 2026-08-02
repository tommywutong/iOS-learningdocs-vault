---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/ManagingState3.html
archived_at: '2026-07-18T01:20:14.855654Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Managing%20State.md) [!Previous Section](Objects%20and%20State.md)

## The Application Object and Application State

The application object is the logical place to store data that needs to be shared by all components in all sessions of an application. Application state is typically stored in the application object's instance variables.
For example, the following application object keeps information about the cars available and the possible prices:

```
// Java Application.java
public class Application extends WOApplication {
    public NSDictionary carData;
    public NSArray prices;
    public NSArray sortBys;

    public Application() {
        super();
        String filePath = resourceManager()
            .pathForResourceNamed("CarData.dict", null, null);
        if (null != filePath) {
            try {
                carData = new NSDictionary(new
                java.io.FilePath(filePath));
            }
            catch (Exception e) {
                //...
            }
        } else {
            // ...
        }
        int priceValues[] = { 8000, 10000, 12000, 14000, 16000, 18000,
            20000, 25000, 30000, 50000, 90000};
        NSMutableArray a = new NSMutableArray();
        for (int i=0; i<priceValues.length; i++) {
            Number num = new Integer(priceValues[i]);
            a.addObject(num);
        }
        prices = (NSArray) a;

        String sortByStrings[] = { "Price", "Type", "Model" };

        for (int i=0; i<sortByStrings.length; i++) {
            a.addObject(sortByStrings[i]);
        }
        sortBys = (NSArray) a;

}
// WebScript Application.wos
id carData;
id prices;
id sortBys;

- init {
    id filePath;

    [super init];
    filePath = [[self resourceManager]
pathForResourceNamed:@"CarData.dict" inFramework:nil
    languages:nil];
    if (filePath)
        carData =
            [NSDictionary dictionaryWithContentsOfFile:filePath];
    //...
    prices = @(8000, 10000, 12000, 14000, 16000, 18000, 20000, 25000,
30000, 50000, 90000);
    sortBys = @("Price", "Type", "Model");
    return self;
}
```


The WOComponent class defines a method __application__, which provides access to the component's application object. So any component can access application state this way:

```
//Java
public boolean isLuckyWinner() {
    Number sessionCount =
application().statisticsStore().objectForKey(
        "Total Sessions Created");
    if (sessionCount == 1000) {
        return true;
    return false;
}
// WebScript
- isLuckyWinner {
    id sessionCount = [[[self application] statisticsStore]
        objectForKey:@"Total Sessions Created"];
    if (sessionCount == 100])
        return YES;
    return NO;
}
```


WODirectActions can access application state using a similar method defined in WODirectAction. Sessions can use the WOApplication __application__ class or static method.
If you're implementing direct action request handling, the only type of state you store by default is application state. Session objects are not created unless specifically requested, and components and WODirectActions do not persist between cycles of the request-response loop.
Application state persists for as long as the application is running. If your site runs multiple instances of the same application, application state must be accessible to all instances. In this case, application state might be best stored in a file or database, where application instances could easily access it. This approach is also useful as a safeguard against losing application state (such as the number of visitors to the site) if an application instance crashes.

[!Table of Contents](Managing%20State.md) [!Next Section](ManagingState4.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
