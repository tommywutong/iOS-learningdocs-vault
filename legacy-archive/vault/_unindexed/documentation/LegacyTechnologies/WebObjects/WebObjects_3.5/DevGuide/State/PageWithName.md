---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/PageWithName.html
archived_at: '2026-07-15T07:52:18.296126Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](PageAwake.md)

### pageWithName: and Page Caching

When the application object receives a pageWithName: message, it creates a new component. For example, in the HelloWorld example a user enters a name in the first page (the Main component), clicks Submit, and is presented with a personal greeting on the second page (the Hello component). Clicking the Submit button in the first page invokes the sayHello method in the Main component. As part of its implementation sayHello sends a pageWithName: message to the application object:

```
    // Java HelloWorld
    String visitorName;

    public Component sayHello() {
        //Create the next page
        Hello nextPage = (Hello)application().pageWithName("Hello");

        // Set state in the Hello page
        nextPage.setVisitorName(visitorName);

        // Return the Hello page
        return nextPage;
    }
```


Each time the sayHello method is invoked, a new Hello component is created. For example, if the user backtracks to the main page and clicks the Submit button again, another Hello page is created. It's unlikely this duplication of components will be a problem for the HelloWorld application, since users quickly tire of its charms. But, depending on design, some applications may benefit by modifying the operation of pageWithName: so that an existing component can be reused.
If you want to extend WebObjects' page caching mechanism to include pages returned by pageWithName:, you must implement your own solution. Fortunately, it's easy. One approach is to have the session maintain a dictionary that maps page names to page objects. Here's the code you would add to the session object:

```
    // example Session.java
    MutableHashtable pageDictionary;

    public Session() {
        super();
        pageDictionary = new MutableHashtable();
    }

    public Component pageWithName(String aName) {
        return (Component)pageDictionary.get(aName);
    }

    public void storePage(String aName, Component aPage) {
        pageDictionary.put(aName, aPage)
    }

    // example Application.java
    public Component pageWithName(String aName) {
        Component aPage;

        if (aName == null)
            aName = "Main";
        aPage = ((Session)session()).pageWithName(aName);
        if (aPage == null) {
            aPage = super.pageWithName(aName);
            ((Session)session().storePage(aName, aPage);
        }
        return aPage;
    }
```


Note that we store pages in the session object because we want to cache these pages on a per-session basis. (Implementing the dictionary in the application object would cache pages on a per-application basis.) Our override of WOApplication's __pageWithName:__ first attempts to retrieve the page from the current session's dictionary before creating a new copy of the page.

[!Table of Contents](StateTOC.md) [!Next Section](ClientCaching.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
