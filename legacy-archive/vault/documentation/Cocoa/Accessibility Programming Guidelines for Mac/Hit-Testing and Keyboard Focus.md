---
title: Accessibility Programming Guidelines for Mac
apple_id: 10000118i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Accessibility/cocoaAXUItesting/cocoaAXUItesting.html
archived_at: '2026-07-15T05:25:26.380768Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Accessibility Programming Guidelines for Mac](Introduction%20to%20Accessibility%20Programming%20Guidelines%20for%20Cocoa.md)


[Next](Accessibility%20Notifications.md)[Previous](Accessibility%20Objects%20and%20the%20Accessibility%20Hierarchy.md)

# Hit-Testing and Keyboard Focus

Assistive applications frequently need to be able to access the user interface object that is at a specific screen location or that currently has keyboard focus. The NSAccessibility protocol defines methods an assistive application uses to get this information from your application.

Hit-testing identifies the deepest member of the accessibility hierarchy that is located at a particular point on the screen. For example, an assistive application may want to identify the user-accessible object that lies beneath the current cursor position.

The NSAccessibility protocol defines the `accessibilityHitTest:` method which, similarly to the standard `hitTest:` view method, returns the farthest descendent of the accessibility hierarchy that contains the specified point (in bottom-left relative screen coordinates). Unlike the standard `hitTest:` view method, however, the `accessibilityHitTest:` method is never called unless the Cocoa accessibility implementation has already determined that the point lies within the receiver. This means that a class needs to override this method only when it contains child accessibility objects; childless accessibility objects never have to override this method.

When an accessibility object receives the `accessibilityHitTest:` method, therefore, it knows that the specified point lies somewhere within it. The accessibility object then has the opportunity to perform deeper hit-testing by identifying which child accessibility object, if any, contains the point. NSMatrix, for example, identifies which of its cells contains the point and propagates the `accessibilityHitTest:` message to it. Eventually, a childless accessibility object acknowledges that it is the object at the specified point and returns `self` from the method. An ignored accessibility object without any children does not return `self`; instead, it returns its first unignored ancestor.

Focus-testing identifies the deepest member of the accessibility hierarchy that has the keyboard focus. The NSAccessibility protocol defines the `accessibilityFocusedUIElement` method an assistive application can send to determine which object has keyboard focus.

As with the `accessibilityHitTest:` method, the `accessibilityFocusedUIElement` method is never called unless the Cocoa accessibility implementation has already determined that the receiver has keyboard focus somewhere within it. This means that a class needs to override this method only when it contains child accessibility objects; childless accessibility objects never have to override this method.

When an accessibility object receives the `accessibilityFocusedUIElement` message, therefore, it knows that it (or one of its children) has keyboard focus. The accessibility object then has the opportunity to perform deeper focus-testing by determining which of its children has keyboard focus and sending to it the `accessibilityFocusedUIElement` message. NSMatrix, for example, identifies which of its cells has the focus and propagates the `accessibilityFocusedUIElement` message to it. Eventually, a childless accessibility object acknowledges that it has keyboard focus and returns `self` from the method. An ignored object without any children returns its first unignored ancestor instead of `self`.

[Next](Accessibility%20Notifications.md)[Previous](Accessibility%20Objects%20and%20the%20Accessibility%20Hierarchy.md)

