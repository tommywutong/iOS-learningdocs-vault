---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/RunLoop/ApplicationInit.html
archived_at: '2026-07-15T07:47:27.351131Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](RunLoop.book.md)
[!Previous Section](initOrAwake.md)

# Application Initialization

The application __init__ method is invoked when the application is launched---either from the command line or by autostarting---and never again. It's common to initialize application variables in an application __init__ method. For example, the follow excerpt from the __Application.wos__ script in the DodgeDemo example initializes the __models__, __categories__, and __priceRange__ application variables.

```
id models, categories, priceRange;
- init {
     id modelSource, categorySource;
    [super init];
    [self logWithFormat:@"Welcome to DodgeDemo!!!"];

    // code not shown...

    // Create Model data source and fetch the models
    modelSource = [[[EODatabaseDataSource alloc] initWithEditingContext:
    editingContext entityName:@"Model"] autorelease];
    if (!modelSource) {
        [self logWithFormat:@"Cannot create model data source"];
        [self terminate];
    }
    models = [modelSource fetchObjects];
    // Create Category data source and fetch the categories
    categorySource = [[[EODatabaseDataSource alloc] initWithEditingContext:
    editingContext entityName:@"Type"] autorelease];
    if (!categorySource) {
        [self logWithFormat:@"Cannot create category data source"];
        [self terminate];
    }
    categories = [categorySource fetchObjects];
     // Price range for price browsers
    priceRange = @(8000, 10000, 12000, 14000, 16000, 18000, 20000, 25000,
    30000, 50000, 90000);
  return self;
}
```

When scripted applications are run, WebObjects automatically creates an instance of a special subclass of WOApplication and adds to it the code from the application script. When you send __init__ to __super__ in an application script, you invoke the __init__ method of the superclass of the instance: WOApplication. You can also create your own subclass of WOApplication and override __init__ to perform any necessary initialization. It is more common, however, to implement the __init__ method in an application script.

Because all applications are not reparsed after the first time, changing a scripted application __init__ method has no effect on a running WebObjects application . To have changes to a scripted application's __init__ method take effect, you must restart the application.

In addition to using the application __init__ method to initialize application variables, you can also use it to configure the application's behavior. For example, you can set the application time-out period and specify the page-cache size:

```
// Set the number of transactions pages are persistent
[self setPageCacheSize:10];
// Set application timeout
[self setTimeOut:43200];
```

[!Table of Contents](RunLoop.book.md)
[!Next Section](SessionInit.md)
