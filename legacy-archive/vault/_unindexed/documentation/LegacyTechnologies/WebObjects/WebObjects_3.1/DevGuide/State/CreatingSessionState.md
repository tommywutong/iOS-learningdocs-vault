---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/CreatingSessionState.html
archived_at: '2026-07-15T07:47:43.380136Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](ControllingSessionState.md)

# Creating and Accessing Session State

You typically store session state as instance variables in your application's session object. Using WebScript, you add these variables to a session script file named __Session.wos__, which is located in the application directory (for example, __MyApp.woa/Session.wos__). A less common but equally effective alternative is to add these instance variables to a compiled session object. It's also possible to store session state within a special dictionary provided by the session object, as we'll see shortly.

Session state is directly accessible to any component within the application. One way to access a session variable is to bind it to an attribute of a dynamic element. For instance, if you open the Visitors example application in WebObjects Builder, you'll see that the value of a WOString dynamic element is bound to the session variable that stores the elapsed time since the session began:

!

__Figure 1.__  Binding a WOString to a Session Variable

Another way to access session variables is from a component's scripted or compiled code:

```
elapsedTime = [[self session] timeSinceSessionBegan];
```

(A component inherits from the WOComponent class, which defines convenience methods such as __session__ and __application__, making it easy for a component to access these other objects simply by sending a message to __self__.)

The WOSession class also provides a dictionary where state can be stored by associating it with a key. WOSession's __setObject:forKey:__ and __objectForKey__ methods give access to this dictionary. For an example of when this session dictionary might be useful, consider a web site that collects users' preferences about movies. At this web site, users work their way through page after page of movie listings, selecting their favorite movie on each page. A "Choices" component at the bottom of each page displays the favorites that have been picked so far in the user's session. The Choices component is a general purpose reusable component that might be found in various applications.

The designer of the Choices component decided to store the session-wide list in the session dictionary:

```
[[self session] setObject:usersChoiceArray forKey:@"Choices"];
```

By storing the information in the session dictionary rather than in a discrete session instance variable, this component can be added to any application without requiring code changes such as adding variables to the session object.

This approach works well until you have multiple instances of a reusable component in the same page. For example, what if users were asked to pick their most _and least_ favorite movies from each list, with the results being displayed in two different Choices components in each page. In this case, each component would have to store its data under a separate key, such as "BestChoices" and "WorstChoices".

A more general solution to the problem of storing state when there are multiple instances of a reusable component is to store the state under unique keys in the session dictionary. One way to create such keys is to concatenate the component's name, context ID, and element IDs:

```
id componentName;
id context;
id contextID;
id elementID;
id uniqueKey;

context = [self context];
componentName = [[context component] name];
contextID = [context contextID];
elementID = [context elementID];
uniqueKey = [NSString stringWithFormat:@"%@-%@-%@", componentName, contextID,
  elementID];
[[self session] setObject:someState forKey:uniqueKey];
```

Since, for a given context, each element in a page has its own element ID, combining the context and element IDs yields a unique key. We added the component name to the key for readability during debugging.

[!Table of Contents](ManagingState.book.md)
[!Next Section](ManagingSessionResources.md)
