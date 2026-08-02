---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/WebScript/VariablesAndScope.html
archived_at: '2026-07-15T07:48:06.926607Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.mif.book.md)
[!Previous Section](DurationOfComponent.md)

# Variables and Scope

In WebScript, the scope of variables depends on where and how you declare them. The notion of scope in WebScript really encompasses two different ideas: a variable's visibility and its lifetime.

The simplest kind of variable in WebScript is a local variable, which is declared inside a method as follows:

```
- aMethod {

    id localVar;
    /*...*/
}
```

Local variables have no visibility outside the method in which they're declared, and no lifetime beyond the method's execution. For this reason, they're the only type of variable that can't be referenced in a declarations file.

All other variables have some degree of persistence within your application. To understand the role of these variables, it's useful to think about the flow of activity in a WebObjects application. The life of a WebObjects application is marked by the continual recurrence of _requests_ (such as a user clicking a control to initiate an action), and the subsequent _responses_ (such as the server returning a dynamically generated HTML page in response to a request). A request-response cycle is called a _transaction_. Processing and variable scoping in a WebObjects application is organized around transactions.

Non-local variables behave differently depending on whether they're declared in an application script (where they're called application variables), in a session script (where they're called session variables), or in a component script (where they're called component variables).

## Application variables

Application variables can be accessed from all pages of an application, and they last for the duration of an application. An application variable is available across all sessions, and there is one copy of the variable per application. Application variables are declared in the application script outside a method as follows:

```
id applicationVar;
```

## Session Variables

Whereas all users of an application see an application variable with the same value, each session has its own unique set of session variables. A variable with session scope lasts for the duration of a session. A session represents a browser (user) accessing a WebObjects application, which could be serving multiple users. A session is initiated when a browser (single user) connects to a WebObjects application, at which time the session is assigned a unique identifier. This session ID is embedded in the URLs of the pages associated with the application. The session ID lasts as long as the session is valid. A session is terminated either when the user quits out of his or her browser, or when the application explicitly times the session out.

A session variable is accessible from every component script and from the application script. Its value is stored and restored at the beginning and the end of each request-response cycle. There is one copy of the variable per user session. Session variables are declared in the session script (__Session.wos__) outside a method. You can access those variables by sending a message to the current WOSession object, obtainable through a message to __self__:

```
id value = [[self session] mySessionVariable];
[[self session] setMyApplicationVariable:newValue];
```

## Component Variables

A component variable is declared in a component script outside a method, as follows:

```
id myVar;
```

This kind of variable lasts the lifetime of a component. The WOApplication object usually stores each component through multiple transactions, the number of which is determined by the application's page-cache size. (See "[The Duration of a Component](DurationOfComponent.md#apple-kjcummzzgy3ds)" for more information.) Component variables are visible to all of the methods within the script in which they're declared.

[!Table of Contents](WebScript.mif.book.md)
[!Next Section](VarScopeSummary.md)
