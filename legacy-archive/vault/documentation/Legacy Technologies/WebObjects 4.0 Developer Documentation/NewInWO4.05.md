---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.05.html
archived_at: '2026-07-15T07:58:54.868727Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.04.md)

## Troubleshooting WebObjects 4.0 Request Handling

In previous WebObjects releases, the application, session, request component, and all of the dynamic elements in the request component got a chance to perform the __takeValuesFromRequest:inContext:__ and __invokeActionForRequest:inContext:__ methods during each cycle of the request-response loop. In WebObjects 4.0, there are some performance enhancements to this request-handling scheme:

- The take values phase is not always performed.

In release 4.0 if the request has no form values to use as input, the take values phase of the request-response loop (in which the application, the session, the request component, and the component's dynamic elements are sent takeValuesFromRequest:inContext:) is not performed.

If you have overridden takeValuesFromRequest:inContext: at the application, session, or component level and your method needs to be invoked even when there are no input values, you must either change your logic or disable 4.0 request handling at the application level. To disable 4.0 request handling, implement the following method in your application class:

```
//WARNING! Put this method in Application class, not component.
//Java implementation
public boolean requiresWOF35RequestHandling() {
    return true;
}
//WebScript implementation
- requiresWOF35RequestHandling {
    return YES;
}
```


It is the application object that makes the decision to perform the take values phase of the request-response loop; therefore, you must disable 4.0 request handling in the application class if you want to ensure that the take values phase always occurs.

- The take values phase does not iterate through WOBrowser and WOPopUpButton lists.

In previous releases, WebObjects would iterate through the __list__ attribute of the WOBrowser and WOPopUpButton looking for the item that the user selected. In release 4.0, this is no longer necessary because WebObjects can directly access the selected item without iterating. WebObjects is able to do this because the use of the __value__ attribute has changed so that by default it is set to the index of the item.

- Use of the __item__ attribute as the selection.
The __item__ attribute is intended to point to the current item, and it is updated upon each iteration through the list. Because WebObjects used to iterate through the list until it found a selection, the __item__ attribute ended up pointing to the selected item.
If you need to refer to the selected item, use the __selection__ attribute instead of __item__. Make sure __selection__ is bound to a variable in your component's code and then use that variable instead of the one bound to __item__.
- Use of the __value__ attribute.
The __value__ attribute was previously used as the string displayed in the browser or pop-up button. It also set the HTML value attribute for the __<OPTION>__ tag. In WebObjects 4.0, this attribute still sets the value in HTML, but it no longer specifies the display string. By default, it is set to an index value, which allows WebObjects to find the selection without iterating through the list.
If you have a binding for the __value__ attribute, change it to __displayString__, which is a new attribute that specifies the display string. Change this:
value = aCollege.name;
to this:
displayString = aCollege.name;
Use __value__ only if you really want to set the HTML value in the __<OPTION>__ tag.
- An __item__ attribute bound to a method.
If you bound the __item__ attribute to a method, your method used to be invoked several times during the take values phase, and now it is invoked only once (for the selected item). If your component depends upon the previous behavior, you either need to change your logic or use WOApplication's request-handling compatibility flag as described above.- The invoke action phase does not iterate through a WORepetition's list.

When a repetition's list is iterated upon, the __item__ and __index__ attribute values are updated at each iteration. In previous releases, list iteration occurred during the take values phase and during the invoke action phase of the request-response loop. In WebObjects 4.0, WORepetition list iteration occurs during take values only if the request has input values, and it doesn't occur during the invoke action phase. (WebObjects is able to forgo iterating during the invoke action phase because by default it sets the __identifier__ attribute to the item's element ID so that it is able to navigate directly to the list item that responds to the requested action. If you already declare a binding for the __identifier__ attribute, your binding is used instead of the element ID, and the invoke action phase does iterate through the list.)

If you've bound the __item__ or __index__ attribute to a method, your method used to be invoked several times during the take values phase, and then again several more times during the invoke action phase. In WebObjects 4.0, your method will only be invoked during the take values phase if there are input values in the request, and it won't be invoked during the invoke action phase (unless you specify a non-default binding for the __identifier__ attribute).

If your component depends upon the previous behavior, you either need to change your logic or use the component's request-handling compatibility flag. To set the component's request handling compatibility flag, implement this method in the component:

```
// Java implementation
public boolean requiresWOF35RequestHandling() {
    return true;
}
// WebScript implementation
- requiresWOF35RequestHandling {
    return YES;
}
```


When you implement this method at the component level, WebObjects uses the old behavior for invoke action on that component only. All other components use the new behavior for the invoke action phase.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.06.md)
