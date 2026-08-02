---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/SessionObjAndState.html
archived_at: '2026-07-15T07:52:19.322137Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](AppObjAndState.md)

## The Session Object and Session State

A more interesting type of state that web applications can store is the state associated with a user's session. This state might include the selections a user makes from a catalog, the total cost of the selections so far, or the user's billing information.
You typically store session state as instance variables in your application's session object. It's also possible to store session state within a special dictionary provided by the session object, as we'll see shortly.
Session state is directly accessible to any component within the application (although those components can access only the state stored for their current session). The WOComponent class defines a __session__ method that provides this access. For example, the component can access a session's instance variable in this way:

```
    // WebScript
    elapsedTime = [[self session] timeSinceSessionBegan];
    //Java
    elapsedTime = this.session().timeSinceSessionBegan();
```


The application object can also access session state using the same method defined in WOApplication.
The WOSession class provides a dictionary where state can be stored by associating it with a key. WOSession's setObject:forKey: and objectForKey methods (in Java, __setObject__ and __objectForKey__) give access to this dictionary. For an example of when this session dictionary might be useful, consider a web site that collects users' preferences about movies. At this web site, users work their way through page after page of movie listings, selecting their favorite movie on each page. At the bottom of each page, a "Choices" component displays the favorites that have been picked so far in the user's session. The Choices component is a general-purpose reusable component that might be found in various applications.
The designer of the Choices component decided to store the sessionwide list in the session dictionary:

```
    [[self session] setObject:usersChoiceArray forKey:@"Choices"];
```


By storing the information in the session dictionary rather than in a discrete session instance variable, this component can be added to any application without requiring code changes such as adding variables to the session object.
This approach works well until you have multiple instances of a reusable component in the same page. For example, what if users were asked to pick their most _and least_ favorite movies from each list, with the results being displayed in two different Choices components in each page. In this case, each component would have to store its data under a separate key, such as "BestChoices" and "WorstChoices".
A more general solution to the problem of storing state when there are multiple instances of a reusable component is to store the state under unique keys in the session dictionary. One way to create such keys is to concatenate the component's name, context ID, and element IDs:

```
    //Java example
    String componentName;
    Context context;
    String contextID;
    String elementID;
    String uniqueKey;

    context = this.context();
    componentName = context.component().name();
    contextID = context.contextID();
    elementID = context.elementID();
    uniqueKey = componentName + "-" + contextID + "-" + elementID;
    this.session().setObject(someState, uniqueKey);
    // WebScript example
    id componentName;
    id context;
    id contextID;
    id elementID;
    id uniqueKey;

    context = [self context];
    componentName = [[context component] name];
    contextID = [context contextID];
    elementID = [context elementID];
    uniqueKey = [NSString stringWithFormat:@"%@-%@-%@", componentName,
    contextID, elementID];
    [[self session] setObject:someState forKey:uniqueKey];
```


Since, for a given context, each element in a page has its own element ID, combining the context and element IDs yields a unique key. The component name is added to the key for readability during debugging.
As described in the chapter ["WebObjects Viewed Through Its Classes"](../HowWOWorks/HowWOWorks.md), the URLs that make up the requests to a WebObjects application contain an identifier for a particular session within the application. Using this identifier, the application can restore the state corresponding to that session before the request is processed. If the request is that of a user contacting the application for the first time, a new session object is created for that user.

As you can imagine, storing data for each session has the potential of consuming excessive amounts of resources, so WebObjects lets you set a time-out for the session objects and lets you terminate them directly.
In summary, session state is accessible only to objects within the same session and persists only as long as the session object persists.

[!Table of Contents](StateTOC.md) [!Next Section](ComponentObjAndState.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
