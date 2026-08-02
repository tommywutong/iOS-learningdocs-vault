---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Intro/RoleOfExecutable.html
archived_at: '2026-07-15T07:47:11.414365Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Start.book.md) [!Previous Section](Adaptors.md)

## The WebObjects Application Executable

When a WebObjects application receives a request from a WebObjects adaptor, it processes the request in three phases. As shown in [Figure 6](#apple-g44tk), the application uses the page-to-script mappings defined in the declarations files to:

- Extract the values from the request and map them to the script.
- Invoke an action.
- Generate a response page.
!Figure 6. Request-Response Loop

The following sections describes what happens during each phase.

### Take Values From Request

The application prepares for the request by updating variables in the request page-the page from which the request was made. That is, if a user has provided any input that maps to a component variable, the application assigns the new value to the variable. For example, when a user clicks Submit in the first page of the HelloWorld example application (in __NextDeveloper/Examples/WebObjects/HelloWorld.woa__), the application gets the value from the text field and assigns it to the __visitorName__ variable defined in the Main component.

### Invoke Action

After preparing for the request, the application determines whether or not the user has triggered an action. If an action has been triggered-for example, if the user clicked a button or a hyperlink-the application invokes the action method that corresponds to what the user did. For example, clicking Submit in HelloWorld has the effect of invoking the __sayHello__ action method. An action method returns a component that represents the _response page_-the page that is sent back to the web server. __sayHello__ returns a component that represents the Hello page. If the user does not trigger an action, the components for the request page also represents the response page.

### Generate Response

The response page component generates the HTML for the response. Using the HTML template and declarations file, the component generates the HTML that is eventually displayed in the user's web browser. For example, after Submit is clicked in HelloWorld and __sayHello__ returns the component for the Hello page, the Hello page component generates the resulting personalized greeting.

[!Table of Contents](Start.book.md) [!Next Section](WhereThingsGo.md)
