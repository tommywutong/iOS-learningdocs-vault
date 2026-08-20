---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/ClientSide/Integrating3.html
archived_at: '2026-07-15T07:46:37.668824Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ClientSideComponents.mif.md)
[!Previous Section](Integrating2.md)

## __3. Declare and initialize variables for bound keys__

In the implementation file or ".wos" script of the server-side component, declare transaction variables for each of the key bindings made in the ".wod" file. Then you can initialize these variables in the __init__ or __awake__ methods. These initialized values are downloaded to the applets when the page is composed.

```
    id inputString;
    id outputString;
    id functionItemList;
    id functionSelectedItem;

    - init {
        self = [super init];

        // Set up parameter values
        inputString = @"Scrumptious";
        outputString = @"";
        functionItemList = [NSArray arrayWithObjects:@"Uppercase",
            @"Lowercase", @"Capitalize", @"Flandersize", nil];
        functionSelectedItem = @"0";

        return self;
    }
```

In this example, the initial values of both TextFieldApplets are set as well the items of the ListApplet. Setting the __functionSelectedItem__ to zero causes the first item in the __functionItemList__ array ("Uppercase") to be preselected.

[!Table of Contents](ClientSideComponents.mif.md)
[!Next Section](Integrating4.md)
