---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.018.html
archived_at: '2026-07-15T07:58:30.258258Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](Direct%20Actions.md)

## How Direct Action Requests Are Sent

Dynamic elements that have an __action__ attribute are bound to component actions. Dynamic elements that have a __directActionName__ attribute are bound to direct actions. The list of dynamic elements bound to direct actions includes WOActiveImage, WOForm, WOFrame, WOHyperlink, WOImageButton, and WOSubmitButton.
When you create a WebObjectsApplication project in release 4.0, a subclass of WODirectAction (a new class in WebObjects 4.0 that is a container for action methods) named "DirectAction" is created for you (along with the WOApplication subclass named "Application" and the WOSession subclass named "Session"). "DirectAction" is the default name for a WODirectAction subclass, and can be renamed if you prefer. You can create several WODirectAction subclasses each performing a single action or a set of actions, or you can have a single WODirectAction subclass perform all of the actions.
For example, the declaration for a WOHyperlink that triggers a direct action might look like this:

```
myLink: WOHyperlink {
    actionClass = "MyActions";
    directActionName = "logout";
}
```


The __actionClass__ parameter specifies a subclass of WODirectAction (it defaults to "DirectAction" if omitted). The __directActionName__ should refer to an action name; if omitted, WebObjects invokes the method __defaultAction__ within the specified class. Method names are derived from action names by appending "Action" to the action name; thus, a __directActionName__ of "logout" corresponds to the __logoutAction__ method.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.019.md)
