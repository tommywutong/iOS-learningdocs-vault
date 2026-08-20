---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/CommonMethods/invokeActionForRequest.html
archived_at: '2026-07-15T07:51:17.999862Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](CommonMethods.md) [!Previous Section](takeValuesFromRequest.md)

## Invoking an Action

The second phase of the request-response loop involves __invokeActionForRequest:inContext:__. WebObjects forwards this method from object to object until it is handled by the dynamic element associated with the user action (typically, a submit button, a hyperlink, and active image, or a form).
Use __invokeActionForRequest:inContext:__ if you want to return a page other than the one requested. This scenario might occur if the user requests a page that has a dependency on another page that the user must fill out first. The user might, for example, finish ordering items from a catalog application and want to go to a fulfillment page but first have to supply credit card information.
The following example, implemented in __Session.wos__, returns a "CreditCard" page if the user hasn't supplied this information yet:

```
    // WebScript example
    - invokeActionForRequest:request inContext:context {
        id creditPage;
        id responsePage = [super invokeActionForRequest:request
            inContext:context];
        id nameOfNextPage = [responsePage name];

        if ([self verified]==NO &&
            [nameOfNextPage isEqual:@"Fulfillment"]) {
            creditPage = [[self application]
                pageWithName:@"CreditCard"];
            [creditPage setNameOfNextPage:nameOfNextPage];
            return creditPage;
        }
        return responsePage;
    }

    //Java example
    public Element invokeActionForRequest(Request request, Context context) {
        Component creditPage;
        Component responsePage = super.invokeActionForRequest(request,
            context);
        String nameOfNextPage = responsePage.name();

        if (verified()==false &&
            (nameOfNextPage.compareTo("Fulfillment") == 0) {
            creditPage = application().pageWithName("CreditCard");
            creditPage.setNameOfNextPage(nameOfNextPage);
            return creditPage;
        }
        return responsePage;
    }
```


When the application receives a request for a new page (say, a fulfillment page), the session object determines whether or not the user has supplied valid credit-card data by checking the value of its __verified__ variable. If the value of __verified__ is NO, the session object returns the "CreditCard" component. As shown in the following action method, the "CreditCard" component sets the __verified__ session variable to YES when the user has supplied valid credit information and returns the user to the original request page to try again.

```
    - verifyUser {
        if ([self isValidCredit]) {
            [[self session] setVerified:YES];
            return [[self application] pageWithName:nameOfNextPage];
        }
        return nil;
    }
```


### Limitations on Direct Requests

Users can access any page in an application without invoking an action. All they need to do is type in the appropriate URL. For example, you can access the second page of HelloWorld without invoking the __sayHello__ action by opening this URL:

```
    http://serverhost/cgi-bin/WebObjects/Examples/HelloWorld.woa/-/Hello.wo/
```


When a WebObjects application receives such a request, it bypasses the user-input (__takeValuesFromRequest:inContext:__) and action-invocation (__invokeActionForRequest:inContext:__) phases because there is no user input to store and no action to invoke. As a result, the object representing the requested page-Hello in this case-generates the response.
By implementing security mechanisms in __invokeActionForRequest:inContext:__, you can prevent users from accessing pages without authorization, but only if those pages are not directly requested in URLs. To prevent users from directly accessing pages in URLs, you must implement another strategy.

[!Table of Contents](CommonMethods.md) [!Next Section](appenToResponse.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
