---
title: App Extension Programming Guide
apple_id: TP40014214
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: null
published: '2017-10-19'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Today.html
archived_at: '2026-07-15T07:34:03.163159Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Extension Programming Guide](index.md)



## Today

App extensions in the Today view are called _widgets_. Widgets give users quick access to information that’s important right now. For example, users open the Today view to check current stock prices or weather conditions, see today’s schedule, or perform a quick task such as marking an item as done. Users tend to open the Today view frequently, and they expect the information they’re interested in to be instantly available.

A Today widget can appear on the lock screen of an iOS device if the user has enabled this. They do so in the “Allow Access When Locked” area by going to Settings > Touch ID & Passcode > Notifications View.

> [!NOTE]
> 

### Understand Today Widgets

On both platforms, a Today widget should:

- Ensure that content always looks up to date
- Respond appropriately to user interactions
- Perform well (in particular, iOS widgets must use memory wisely or the system may terminate them)

Because user interaction with Today widgets is quick and limited, you should design a simple, streamlined UI that highlights the information users are interested in. In general, it’s a good idea to limit the number of interactive items in a widget. In particular, note that iOS widgets don’t support keyboard entry.

> [!NOTE]
> 

Users configure Today widgets differently depending on the platform they’re using.

__iOS.__ Because Today widgets don’t allow keyboard entry, users need to be able to use the containing app to configure a widget’s content and behavior. In the Stocks widget, for example, users can switch between different representations of a symbol’s value, but they must open the Stocks app to manage the list of symbols.

__OS X.__ The containing app might not perform any functions, so the Today widget may need to give users ways to configure it while it’s running. For example, the Stocks widget in OS X lets users find and add market symbols they want to track. The Notification Center API in OS X includes methods you can use to let users configure widgets.

After users install an app that contains a Today widget, they can add the widget to the Today view. When users choose Edit in the Today view, Notification Center reveals a view that lets users add, reorder, and remove widgets.

### Use the Xcode Today Template

The Xcode Today template provides default header and implementation files for the principal class (named `TodayViewController`), an `Info.plist` file, and an interface file (that is, a storyboard or xib file).

By default, the Today template supplies the following `Info.plist` keys and values (shown here for an OS X target):

1. `<key>NSExtension</key>`
2. `<dict>`
3. `<key>NSExtensionPointIdentifier</key>`
4. `<string>com.apple.widget-extension</string>`
5. `<key>NSExtensionPrincipalClass</key>`
6. `<string>TodayViewController</string>`
7. `</dict>`

If you use a custom view controller subclass, use the custom class name to replace the `TodayViewController` value for the `NSExtensionPrincipalClass` key.

__iOS.__ If you don’t want to use the storyboard file provided by the template, remove the `NSExtensionMainStoryboard` key and add the `NSExtensionPrincipalClass` key, using the name of your view controller for the value.

Most of the work you do to create a Today widget involves designing the UI and implementing a view controller subclass that performs your custom functionality.

### Design the UI

> [!IMPORTANT]
> 

Because space in the Today view is limited and the expected user experience is quick and focused, you shouldn’t create a widget that's too big by default. On both platforms, a Today widget must fit within the width of the Today view, but it can increase in height to display more content.

A Today widget created using the Xcode Today template includes Auto Layout constraints for standard margin insets. To get the inset values for your calculations, implement the [widgetMarginInsetsForProposedMarginInsets:](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/1490248-widgetmargininsets) method. (The template’s principal view controller conforms to the [NCWidgetProviding](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding) protocol, which provides this method.) Be sure to draw all your widget content within these standard margin insets. To learn more about designing the appearance of your widget, see Today Widgets in _iOS Human Interface Guidelines_.

If a widget has additional content to display, you can rely on Auto Layout constraints to adjust the widget’s height as appropriate. If you don’t use Auto Layout, you can use the `UIViewController` property [preferredContentSize](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621476-preferredcontentsize) to request a height for the widget. For example:

1. `- (void)receivedAdditionalContent {`
2. `self.preferredContentSize = [self sizeNeededToShowAdditionalContent];`
3. `}`

> [!NOTE]
> 

__iOS.__ If you want to animate the display of your content to coincide with the resize animation, implement `viewWillTransitionToSize:withTransitionCoordinator:`, using [animateAlongsideTransition:completion:](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/1619300-animatealongsidetransition) to add your animations to the `coordinator` parameter.

To ensure that your widget gets the vibrancy effect that’s appropriate for displaying items in the Today view, use `notificationCenterVibrancyEffect`.

__OS X.__ Widgets inherit `NSAppearanceNameVibrantDark` from the view their view controller is placed in. When you use standard controls, you automatically get the right appearance. If you use custom colors, be sure to choose colors that look good in a vibrant dark view.

### Updating Content

The Today extension point provides API for managing a widget’s state and handling updates to its content (you can read about this API in the _[Notification Center Framework Reference](https://developer.apple.com/documentation/notificationcenter)_). Although there are a few platform-specific differences in the Today API, the functionality supported on both platforms is mostly the same.

To help your widget look up to date, the system occasionally captures snapshots of your widget’s view. When the widget becomes visible again, the most recent snapshot is displayed until the system replaces it with a live version of the view.

To update a widget’s state before a snapshot is taken, be sure to conform to the [NCWidgetProviding](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding) protocol. When your widget receives the [widgetPerformUpdateWithCompletionHandler:](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/1490262-widgetperformupdatewithcompletio) call, update your widget’s view with the most recent content and call the completion handler, using one of the following constants to describe the result of the update:

- `NCUpdateResultNewData`—The new content required you to redraw the view
- `NCUpdateResultNoData`—The widget doesn’t require updating
- `NCUpdateResultFailed`—An error occurred during the update process

### Specifying When a Widget Should Appear

If your widget should be visible in the Today view only in certain circumstances—such as when it has new or noteworthy content—use the [setHasContent:forWidgetWithBundleIdentifier:](https://developer.apple.com/documentation/notificationcenter/ncwidgetcontroller/1456693-sethascontent) method from [NCWidgetController](https://developer.apple.com/documentation/notificationcenter/ncwidgetcontroller) class. This method lets you declare the state of a widget’s content, which in turn prompts the system to show or hide the widget.

You can call the `setHasContent:forWidgetWithBundleIdentifier:` method from your widget or from its containing app. Indeed, the containing app can call this method even while the widget isn’t running. For example, you can employ a push notification to the containing app to trigger a call to this method. The next time a user opens the Today view, your widget is visible.

To declare that your widget has no content and can therefore be hidden, call the `setHasContent:forWidgetWithBundleIdentifier:` method with a `flag` parameter value of `NO``false`. Notification Center won’t launch your widget again until the containing app calls this method passing `YES``true` in the `flag` parameter, to specify that the widget has content to display.

### Opening the Containing App

In some cases, it can make sense for a Today widget to request its containing app to open. For example, the Calendar widget in OS X opens Calendar when users click an event. (Note that in iOS, a user may have to unlock the device before the containing app can open.) To ensure that your containing app opens in a way that makes sense in the context of the user’s current task, you need to define a custom URL scheme that both the app and its widgets can use.

A widget doesn’t directly tell its containing app to open; instead, it uses the [openURL:completionHandler:](https://developer.apple.com/documentation/foundation/nsextensioncontext/1416791-open) method of [NSExtensionContext](https://developer.apple.com/documentation/foundation/nsextensioncontext) to tell the system to open its containing app. When a widget uses this method to open a URL, the system validates the request before fulfilling it.

### Supporting Edits (OS X Only)

To support an editing mode within your OS X widget, conform to the [NCWidgetProviding](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding) protocol. When you set the [widgetAllowsEditing](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/1490251-widgetallowsediting) property to `YES``true`, the Info button is automatically displayed in your widget’s header area. (When users click the Info button, it automatically switches to a Done button.) When you use the [NCWidgetProviding](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding) protocol to support editing, the Edit, Done, and Cancel buttons are automatically provided when the view goes into editing mode.

To observe changes between editing and nonediting modes in a widget, use the [widgetDidBeginEditing](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/1490249-widgetdidbeginediting) and [widgetDidEndEditing](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/1490258-widgetdidendediting) methods of the `NCWidgetProviding` protocol.

If you also want to present a modal search UI while users are editing your widget, use the `NCWidgetProvidingPresentationStyles` category on [NSViewController](https://developer.apple.com/documentation/appkit/nsviewcontroller) to present your search view controller. When users indicate that they’re done searching, use the [dismissViewControllerAnimated:completion:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621505-dismissviewcontrolleranimated) method to dismiss the search view controller. (Note that you can also use the `presentViewControllerInWidget:` method to present a nonsearch modal view that needs a Cancel button in the header area.)

### Testing a Today Widget

__iOS.__ You can test an iOS widget in iOS Simulator or on a device.

__OS X.__ To test a widget in OS X, it’s easiest to use the Xcode Widget Simulator, because Notification Center dismisses as soon as you switch to another app, or click outside its bounds. You can specify the Widget Simulator in a scheme for the widget target.

To learn about debugging app extensions in general, see [Debug, Profile, and Test Your App Extension](ExtensionCreation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqnjnknltq).

[Share](Share.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqmjsfvjvomi)
