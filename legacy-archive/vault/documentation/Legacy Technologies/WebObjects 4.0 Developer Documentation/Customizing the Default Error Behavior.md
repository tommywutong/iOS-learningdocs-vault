---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/CustomizingDefaultErr.html
archived_at: '2026-07-15T08:01:00.794591Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Customizing the Default Error Behavior

##  Synopsis

Describes how to replace the default WebObjects error page with more user-friendly pages.

##  Description

By default, WebObjects displays a standard error page in the browser when an application error occurs. This page provides useful debugging information, but generally shouldn't be seen by end-users of the application. Most deployed sites use one or more custom error pages.

Custom error pages can be provided in your application in two ways. The first way is to replace the default WOExceptionPage component. While this method requires no coding, it causes all WebObjects applications to display your custom page when an error occurs. Another way to provide custom error behavior is to override the exception handlers in the WOApplication class. Although this method requires some coding, it can display different error pages for different types of exceptions and it does not affect the behavior of other WebObjects applications.

####  Replacing the WOExceptionPage Component

The default WebObjects error page is defined in $NEXT_ROOT\Library\Frameworks\WOExtensions.framework\Resources\WOExceptionPage.wo. This component may be edited using WebObjects Builder. It is highly recommended that you make a backup copy before you modify the default WebObjects error page.

####  Overriding the WOApplication Exception Handlers

The WOApplication class provides the following methods that you can override to show your own error page. These methods return a WOResponse object which your code needs to provide. The example code shows how to override these exception handling methods and redirect WebObjects to different pages depending on the type of exceptions that occur.

######  TABLE 1. WOApplication Class Methods

|   Method Invoked |   When |
|   handleSessionCreationError |   The application needs to create a new session but cannot. |
|   handleSessionRestorationError |   The application receives a request from a session that has timed out. |
|   handlePageRestorationError |   The application tries to access an existing page but cannot. Usually, this occurs when the user has backtracked beyond the limit set by setPageCacheSize() and setPageRefreshOnBacktrackEnabled() is set to NO. |
|   handleException |   The application receives any exception. |

#####  Figure 1. Java Code

```
public WOResponse handleException (java.lang.Throwable anException,
```



```
    WOContext aContext) {
```



```

```



```
    WOComponent errorPage;
```



```
    String exceptionDescription = anException.toString();
```



```

```



```
    if (exceptionDescription.indexOf("EOValidationException") > -1) {
```



```
        System.err.println ("validation error");
```



```
        errorPage = pageWithName("ValErrorPage",aContext);
```



```
    } else {
```



```
      System.err.println ("error" + exceptionDescription);
```



```
      errorPage = pageWithName("ErrorPage",aContext);
```



```
    }
```



```
    WOResponse response = errorPage.generateResponse();
```



```
    return response;
```



```
}
```



```

```


##  See Also

· Understanding the Default WebObjects Error Page

· WOApplication

· WOResponse

##  Questions

· How do I change the default WebObjects error page?

· How can I trap exceptions in a WebObjects application?

##  Keywords

· Error Page

· Error Handling

· Exception Handling

##  Revision History

22 July, 1998. John Malach. First Draft.

15 July, 1998. Carmine Marino. Exception Handling Code.

27 October, 1998. Clif Liu. Second Draft.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
