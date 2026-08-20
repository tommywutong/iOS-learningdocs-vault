---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Methods3.html
archived_at: '2026-07-15T08:05:56.178318Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Common%20Methods.md) [!Previous Section](Methods2.md)

## Direct Actions

If you want your application to perform direct action request handling instead of component action request handling (as described in ["The Request-Response Loop"](WhatIsWebObjects6.md#apple-he2deni)), you place your action methods in a different class and you write them slightly differently.

With direct actions, there is no concept of a request page that can perform the requested action. (Recall from the previous section that the Main component is the request page for the __sayHello__ action, meaning that Main implements the __sayHello__ method.) Instead, the direct action method is defined in a subclass of WODirectAction.
To associate a direct action method to a user action, bind the dynamic element's __directActionName__ attribute to the action method's name (enclosing the __directActionName__ attribute value in double-quotes), and optionally bind the element's __actionClass__ attribute to the name of the WODirectAction subclass that implements the action method. If you don't specify the element's __actionClass__, a default class name of "DirectAction" is assumed. As well, if you've specified an __actionClass__ or WODirectActionRequestHandler is the default request handler, you can omit the __directActionName__ and WebObjects will invoke the "defaultAction" method within the specified (or default) __actionClass__. For an example of how to make WODirectActionRequestHandler the default request handler, see ["Setting the Default Request Handler"](Methods5.md#apple-ha3tanq).

When working with elements inside a WOForm, note that the WOForm's request handler determines how the form's elements are processed. If the WOForm uses component action request handling, setting the __actionClass__ or __directActionName__ attributes on action elements inside the form-such as the WOSubmitButton-will have no effect. Instead, you must either assign the __actionClass__ and __directActionName__ attributes to the WOForm element itself, or you must set the WOForm's __actionClass__ as follows, which then causes the WOForm's direct action element attributes to be used:

```
myForm : WOForm {
    actionClass = "";
}
button : WOSubmitButton {
    directActionName = "sayHello";
    actionClass = "MyAction";
}
```


Direct action method names are derived from action names by appending "Action" to the action name. Thus, setting your element's __directActionName__ attribute to "sayHello" as in the above code causes MyAction's __sayHelloAction__ method to be invoked when the WOSubmitButton is clicked.
The WODirectAction class is simply a container for action methods. When you create a WebObjects application project in Project Builder, you automatically get a subclass of WODirectAction named DirectAction (DirectAction is the default name for the WODirectAction subclass; you can rename it, if you prefer). Each action method in your WODirectAction class must end with the string "Action" and should return either a WOComponent or a WOResponse object. For example:

```objc
- (WOComponent *)sayHelloAction
```


or:

```
public WOComponent sayHelloAction()
```


Note that your application can use as many WODirectAction subclasses as necessary.
Your direct action method should return an object that conforms to the WOActionResults protocol (Java interface); typically, your method will return a WOComponent or a WOResponse (both implement the methods in WOActionResults). Unlike component actions, direct actions may not return __nil__ or __null__.
To use a more complete illustration, in an implementation of the HelloWorld application using direct actions the Main component's declarations file might look like this:

```
myForm : WOForm {
    directActionName = "";
}

textField : WOTextField {
    value = visitorNameIVar;
    name = "visitorName";
}

button : WOSubmitButton {
    directActionName = "sayHello";
    actionClass = "MyAction";
}
```


The __actionClass__ and __directActionName__ attributes specify that clicking this hyperlink should trigger the MyAction object's __sayHelloAction__ method. Note that WOForms cannot have submit buttons to both component and direct actions. Because of this, when using a submit button bound to a direct action the WOForm must be triggered to cooperate. You do this by having an empty binding for direct action, as shown in the previous code excerpt, or by just putting the action directly on the WOForm.
The implementation of __sayHelloAction__ is similar to the implementation of __sayHello__ shown in the previous section. It creates a new page named Hello and sends that page the name the user has typed into the text field.

```objc
//WebScript DirectAction.wos
- (WOComponent *)sayHelloAction
{
        id nextPage;
        id aName = [[self request] formValueForKey:@"visitorName"];

        nextPage = [self pageWithName:@"Hello"];
        [nextPage setVisitorName:aName];
        return nextPage;
}
//Java DirectAction.java
public WOComponent sayHelloAction() {
        Hello nextPage;
        String aName =
(String)request().formValueForKey("visitorName");
        nextPage = (Hello)this.pageWithName("Hello");
        nextPage.setVisitorName(aName);
        return (WOComponent)nextPage;
}
```


Where __sayHelloAction__ differs from __sayHello__ is that it must perform an additional step: it must extract the form values out of the request itself. The visitor's name is recorded in an instance variable in the Main component (__visitorNameIVar__ in the example above). With component actions, any action that is performed by a dynamic element in Main is implemented in Main's code. Because the action is implemented in Main, you can reference the instance variable directly. Direct actions are performed in a separate class and do not have access to Main's instance variables. Instead, direct action methods must extract the information they need from the HTTP request. In this example, the visitor's name is recorded in a text field named "visitorName." Thus, __sayHelloAction__ asks for the value for "visitorName" from the request and passes that value to the Hello component.

[!Table of Contents](Common%20Methods.md) [!Next Section](Methods4.md)
