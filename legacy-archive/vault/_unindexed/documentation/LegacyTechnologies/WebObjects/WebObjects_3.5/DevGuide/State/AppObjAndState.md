---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/AppObjAndState.html
archived_at: '2026-07-15T07:52:09.337136Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](ObjectsAndState.md)

## The Application Object and Application State

The application object is the logical place to store data that needs to be shared by all components in all sessions of an application. Application state is typically stored in the application object's instance variables. For example, the application object in the DodgeLite example application (in <DocRoot>__/WebObjects/Examples__ where <DocRoot> is your web server's document root), keeps information about the cars available and the possible prices:

```
    // Java DodgeLite Application.java
    public class Application extends WebApplication {
        public ImmutableHashtable dodgeData;
        public ImmutableVector prices;
        public ImmutableVector sortBys;

        public Application() {
            super();
            String filePath = resourceManager()
                .pathForResourceNamedInFramework("DodgeData.dict", null);
            if (null != filePath) {
                try {
                    dodgeData = new ImmutableHashtable(new
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
            MutableVector a = new MutableVector();
            for (int i=0; i<priceValues.length; i++) {
                Number num = new Integer(priceValues[i]);
                a.addElement(num);
            }
            prices = (ImmutableVector) a;

            String sortByStrings[] = { "Price", "Type", "Model" };

            for (int i=0; i<sortByStrings.length; i++) {
                a.addElement(sortByStrings[i]);
            }
            sortBys = (ImmutableVector) a;

    }

    // WebScript DodgeLite Application.wos
    id dodgeData;
    id prices;
    id sortBys;

    - init {
        id filePath;

        [super init];
        filePath = [[self resourceManager]
    pathForResourceNamed:@"DodgeData.dict" inFramework:nil];
        if (filePath)
            dodgeData = [NSDictionary dictionaryWithContentsOfFile:filePath];
        //...
        prices = @(8000, 10000, 12000, 14000, 16000, 18000, 20000, 25000, 30000, 50000, 90000);
        sortBys = @("Price", "Type", "Model");
        return self;
    }
```


The WOComponent class defines a method __application__, which provides access to the component's application object. So any component can access application state this way:

```
    //Java
    public boolean isLuckyWinner() {
        Number sessionCount = application().statisticsStore().get(
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


Sessions can access application state using the same method defined in WOSession.
Application state persists for as long as the application is running. If your site runs multiple instances of the same application, application state must be accessible to all instances. In this case, application state might be best stored in a file or database, where application instances could easily access it. This approach is also useful as a safeguard against losing application state (such as the number of visitors to the site) if an application instance crashes.

[!Table of Contents](StateTOC.md) [!Next Section](SessionObjAndState.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
