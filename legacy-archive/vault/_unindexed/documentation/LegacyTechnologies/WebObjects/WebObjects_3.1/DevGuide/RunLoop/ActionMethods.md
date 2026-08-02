---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/RunLoop/ActionMethods.html
archived_at: '2026-07-15T07:47:25.404097Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](RunLoop.book.md)
[!Previous Section](ComponentInit.md)

# Action Methods

An action method is a method that's associated with a user action. You associate methods with a user action using a dynamic element. For example, WOSubmitButton has an attribute named __action__ to which you can assign a method. When the submit button in the corresponding HTML page is clicked, the action method is invoked in the subsequent cycle of the request-response loop. This declaration in the HelloWorld application associates the action method __sayHello__ with a submit button:

```
SUBMIT_BUTTON: WOSubmitButton {action = sayHello};
```

Clicking the submit button sends a request to the HelloWorld application, initiating a cycle of the request-response loop in which __sayHello__ is invoked.

__Note:__  The WOActiveImage, WOHyperlink, and WOForm dynamic elements can also be used to associate action methods to a user action.

Action methods take no arguments and return a page that will be packaged with an HTTP response. For example, the __sayHello__ action method of the HelloWorld example is defined as follows:

```
- sayHello
{
    id nextPage = [WOApp pageWithName:@"Hello"];
    [nextPage setNameString:nameString];
    return nextPage;
}
```

As in __sayHello__, most action methods perform page navigation. It is common for action methods to determine the response page based on user input. For example, the following action method returns an error page if the user has entered an invalid part number (stored in the component variable __partnumber__) or an inventory summary otherwise:

```
- showPart {
    id errorPage;
    id inventoryPage;

    if ([self isValidPartNumber:partnumber]) {
        errorPage = [[self application] pageWithName:@"Error"];
        [errorPage setErrorMessage:@"Invalid part number %@.", partnumber];
        return errorPage;
    }
    inventoryPage = [[self application] pageWithName:@"Inventory"];
    [inventoryPage setPartNumber:partnumber];

    return inventoryPage;
}
```

Action methods don't have to return a new page. They can instead direct the application to regenerate the request page. When an action method returns __nil__, the application uses the request component as the response component.

__Note:__  Returning __self__ in an action method generally has the same effect as returning __nil__. However, there's a difference when the action method is implemented in a nested component. When a nested component---a component representing only a portion of the request page---returns __self__ in an action, the application attempts to use the nested component to generate the response page. Since the component only represents a portion of a page, returning __self__ is probably an error. Returning __nil__ always has the effect of using the request page---the component representing the whole request page---as the response page. As a result, returning __nil__ is considered to be a better practice than returning __self__.

In the Visitors example, the request page is also used as the response page. The WebScript __recordMe__ action method records the name of the last visitor and clears the text field:

```
- recordMe
{
   if ([aName length]) {
       [[self application] setLastVisitor:aName];
       [self setAName:@""]; // clear the text field
   }
   return nil;
}
```

[!Table of Contents](RunLoop.book.md)
[!Next Section](RequestHandlingMethods.md)
