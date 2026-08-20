---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/RunLoop/invokeActionForRequest.html
archived_at: '2026-07-15T07:47:32.362376Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](RunLoop.book.md)
[!Previous Section](takeValuesFromRequest.md)

# invokeActionForRequest:inContext:

The second phase of the request-response loop involves __invokeActionForRequest:inContext:__. This method is invoked, in turn, in the application object, the session object, the request page, and in every dynamic element on that page. Normally, the message is forward from object to object until it is handled by the dynamic element associated with the user action (typically a WOSubmitButton, a WOHyperLink, an WOActiveImage, or WOForm).

A common use of this "hook" in __Appliation.wos__, __Session.wos__, or a component script to return a page other than the one requested. A scenario where this might occur is when the user requests a page which has a dependency on another page that the user must fill out first. The user might finish ordering items from a catalog application and want to go to a fulfillment page; but first he or she must supply credit card information.

The following __invokeActionForRequest:inContext:__ method, implemented in __Session.wos__, returns a "CreditCard" page if the user hasn't supplied this information yet:

```
- invokeActionForRequest:request inContext:context {
    id creditPage;
    id responsePage = [super invokeActionForRequest:request inContext:context];
    id nameOfNextPage = [responsePage name];
    if ([self verified]==NO &&
        [nameOfNextPage isEqual:@"Fulfillment"]) {
        creditPage = [[self application] pageWithName:@"CreditCard"];
        [creditPage setNameOfNextPage:nameOfNextPage];
        return creditPage;
    }
    return responsePage;
}
```

When the application receives a request for a new page (say, a fulfillment page), the session determines whether or not the user has supplied valid credit-card data by checking the value of its __verified__ variable. If the value of __verified__ is NO, the session returns the "CreditCard" component. As shown in the following action method, the "CreditCard" component sets the __verified__ session variable to YES when the user has supplied valid credit information and returns the user to the original request page to try again.

```
- verifyUser {
    if ([self isValidCredit]) {
        [[self session] setVerified:YES];
        return [[self application] pageWithName:nameOfNextPage];
    }
    return nil;
}
```

## Limitations on Direct Requests

By specifying a page in a URL, a user can attempt to access any page in an application without invoking an action. For example, you can access the second page of HelloWorld without invoking the __sayHello__ action by opening the URL:

```
http://serverhost/cgi-bin/WebObjects/Examples/HelloWorld.woa/Hello.wo/
```

When a WebObjects application receives such a request, it bypasses the user-input (__takeValuesFromRequest:inContext:__) and action-invocation (__invokeActionForRequest:inContext:__) phases because there is no user input to store and no action to invoke. As a result, the object representing the requested page---Hello in this case---generates the response.

By implementing security mechanisms in __invokeActionForRequest:inContext:__, you can prevent users from accessing pages without authorization, but only if those pages are not directly requested in URLs.

[!Table of Contents](RunLoop.book.md)
[!Next Section](appendToResponse.md)
