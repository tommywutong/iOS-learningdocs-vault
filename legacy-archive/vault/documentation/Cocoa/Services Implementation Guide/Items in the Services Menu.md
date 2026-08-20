---
title: Services Implementation Guide
apple_id: 10000101i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SysServices/Articles/menu.html
archived_at: '2026-07-15T07:19:49.730380Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Services Implementation Guide](Introduction.md)


[Next](Services%20Properties.md)[Previous](Services%20Overview.md)

# Items in the Services Menu

Applications that provide services may be installed anywhere on the system. The applications’ information property lists declare the services the applications provide (see [Services Properties](Services%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha2telkdjbceurcgjfbq)). OS X collects the property list information and uses it to populate the items in the Services menu based on the particular data types supported by each application.

The Services menu is included in the default nib file created by Xcode and Interface Builder for Cocoa applications. If the application’s menu is instead created programmatically, you need to designate a Services menu using the `NSApplication` method `setServicesMenu:`. If an application registers for services (see [Using Services](Using%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha2tilkdivduircijjfa)), the appropriate items are automatically available in the Services menu.

The items in the Services menu are commands categorized by what type of data they operate on. The application icon of the application providing a service appears to the left of the service’s name in the menu. If two or more applications provide a service with an identical name, the name of the application providing each one is appended in parentheses after the name of the service in the menu.

The Services menu is populated when the menu is opened. Choosing the Services menu causes the current responder chain to be searched for objects that can provide or receive data of the types used by each service listed in the Services menu. If an object is found that can use a given service, the service’s menu item is shown in the menu. Menu items for which no suitable object is found are not shown in the menu.

[Next](Services%20Properties.md)[Previous](Services%20Overview.md)

