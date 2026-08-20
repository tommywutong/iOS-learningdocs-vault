---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/Deployment/ErrorHandling.html
archived_at: '2026-07-15T07:51:23.587026Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Deployment.md) [!Previous Section](Stats.md)

# Error Handling

When an error occurs, WebObjects by default returns a page containing debugging information and displays that page in the web browser. This information is useful when you're in the debugging phase, but when you're ready to deploy, you probably want to make sure that your users don't see such information.
The WOApplication class (WebApplication in Java) provides the following methods that you can override to show your own error page.

|  __Method__ |  Invoked When |
|  handleSessionCreationError |  The application needs to create a new session but can't. |
|  handleSessionRestorationError |  The application receives a request from a session that has timed out. |
|  handlePageRestorationError |  The application tries to access an existing page but cannot. Usually, this occurs when the user has backtracked beyond the limit set by __setPageCacheSize:__ and __setPageRefreshOnBacktrackEnabled:__ is NO. |
|  handleException: |  The application receives an exception; that is, any general type of error has occurred. |

```
```


For example, the following implementation of __handleException:__ returns a component named ErrorPage whenever an error occurs in the application.

```
    public Response handleException(java.lang.Throwable anException) {
        Response response = new Response();
        Request request = context().request();
        String newURL = "http://" + request.applicationHost() +
            request.adaptorPrefix() + "/" + request.applicationName() +
            ".woa/-/ErrorPage.wo";

        response.setHeader(newURL, "location");
        response.setHeader("text/html", "content-type");
        response.setHeader("0", "content-length");
        response.setStatus(302);

        return response;
    }
```


Notice that this method, and all of the error-handling methods, return a WOResponse object instead of a WOComponent object. It creates the response by directly setting the URL in the HTTP header to point to the component that it wants to return (in this case, the component is named ErrorPage). Notice how you can retrieve much of the information about the application URL through the current request object, which you can access from the current context object.

[!Table of Contents](Deployment.md) [!Next Section](TerminateApp.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
