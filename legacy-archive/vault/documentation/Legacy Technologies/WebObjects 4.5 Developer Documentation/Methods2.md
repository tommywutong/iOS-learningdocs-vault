---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Methods2.html
archived_at: '2026-07-15T08:05:55.176893Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Common%20Methods.md) [!Previous Section](Action%20Methods.md)

## Component Actions

In component actions, the component currently being displayed defines the action method to be performed. For example, the first page of a WebObjects application is the Main component, so Main defines the first action method to be performed.
To associate the component's action method to a user action, you map it to a dynamic element that has an attribute named __action__ (such as a WOSubmitButton, WOActiveImage, or WOHyperlink). When the user performs the associated action, your method is invoked. For example, in the HelloWorld example application, the submit button is mapped to a method named __sayHello__ in the Main component. When a user types in a name and clicks the button on the main page, it initiates the application's request-response loop, and __sayHello__ is invoked.
Action methods take no arguments and return a page (component) that will be packaged with an HTTP response. For example, the __sayHello__ method creates a new page named Hello and sends that page the name the user has typed into the text field.

```
//WebScript HelloWorld Main.wos
- sayHello
{
        id nextPage;
        nextPage = [self pageWithName:@"Hello"];
        [nextPage setVisitorName:visitorName];
        return nextPage;
}
```


If you're programming in Java, the __sayHello__ method looks like this:

```
//Java HelloWorld Main.java
public WOComponent sayHello() {
        Hello nextPage = this.pageWithName("Hello");
        nextPage.setVisitorName(visitorName);
        return nextPage;
}
```


In this example, the component Main is used to generate the page that handles the user request, and the component Hello generates the page that represents the response. Main is the _request component_ or the _request page_, and Hello is the _response component_ or the _response page_.
It's common for action methods to determine the response page based on user input. For example, the following action method returns an error page if the user has entered an invalid part number (stored in the variable __partnumber__); otherwise, it returns an inventory summary:

```
// WebScript example
- showPart {
        id errorPage;
        id inventoryPage;

        if ([self isValidPartNumber:partnumber]) {
            errorPage = [self pageWithName:@"Error"];
            [errorPage setErrorMessage:@"Invalid part number %@.",
                partnumber];
            return errorPage;
        }
        inventoryPage = [self pageWithName:@"Inventory"];
        [inventoryPage setPartNumber:partnumber];
        return inventoryPage;
}
// Java example
public WOComponent showPart() {
        Error errorPage;
        Inventory inventoryPage;

        if (isValidPartNumber(partNumber)) {
            errorPage = (Error)this.pageWithName("Error");
            errorPage.setErrorMessage("Invalid part number " +
                partnumber);
            return errorPage;
        }
        inventoryPage = (Inventory)this.pageWithName("Inventory");
        inventoryPage.setPartNumber(partnumber);
        return inventoryPage;
}
```


Component action methods don't have to return a new page. They can instead direct the application to use the request page as the response page by returning __nil__ (__null__ in Java). For example, the following action method records the name of the last visitor, clears the text field, and redraws the Main component, which contains it:

```
// WebScript Main.wos
- recordMe
{
        if ([aName length]) {
            [[self application] setLastVisitor:aName];
            [self setAName:@""]; // clear the text field
        }
}
// Java Main.java
public WOComponent recordMe
{
        if (aName.length != 0) {
            ((Application)application()).setLastVisitor(aName);
            aName = ""; // clear the text field
        }
        return null;
}
```


__Note:__  Always return __nil__ (__null__) in an action method instead of returning __self__ (__this__). Returning __nil__ uses the request component as the response component. Returning __self__ uses the _current_ component as the response component. At first glance, these two return values seem to do the same thing. However, if the action method is in a component that's nested inside of the request component, a return value of __self__ will make the application try to use the nested component, which represents only a portion of the page, as the response component. This, most likely, is not what you want. Therefore, it is safer to always return __nil__.

[!Table of Contents](Common%20Methods.md) [!Next Section](Methods3.md)
