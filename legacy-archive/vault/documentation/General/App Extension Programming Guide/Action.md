---
title: App Extension Programming Guide
apple_id: TP40014214
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: null
published: '2017-10-19'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Action.html
archived_at: '2026-07-15T07:33:46.337054Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Extension Programming Guide](index.md)



## Action

An Action extension helps users view or transform content originating in a host app. For example, an Action extension might help users edit an image in a document that they’re viewing in a text editor. Another type of Action extension might let users view a selected item in a different way, such as viewing an image in a different format or reading text in a different language.

The system offers an Action extension to users only when the extension declares it can work with the type of content a user is currently using. For example, if an Action extension declares it works only with text, it isn’t made available when a user is viewing images.

To learn how to declare the types of content an Action extension can work with, read [Declaring Supported Data Types for a Share or Action Extension](ExtensionScenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqmrrfvjvooa)).

> [!NOTE]
> 

### Understand Action Extensions

Action extensions behave differently depending on the platform. In OS X, an Action extension:

- Can be an editor, in which users can make changes to selected content, or a viewer, in which users can view selected content in a new way
- Can transmit to the host app the content changes that users make within the app extension
- Can appear in a modal view that emerges from the host app’s window or in a custom view that surrounds the user’s selected items
- Automatically receives the user’s selected content as part of the extension context

In iOS, an Action extension:

- Helps users view the current document in a different way
- Always appears in an action sheet or full-screen modal view
- Receives selected content only if explicitly provided by the host app

On both platforms, users get access to Action extensions in the system-provided UI. In iOS, an Action extension is listed in the action area of the activity view controller that appears when users tap the Share button. In OS X, there are a few ways in which users can reveal a list of Action extensions. For example, users can:

- Move the pointer over some selected content and click the button that appears
- Click the Share toolbar button
- Click the Action extension’s custom toolbar button

> [!NOTE]
> 

### Use the Xcode Action Extension Template

The Xcode Action extension template provides default source files for the principal view controller class (called `ActionViewController`), an `Info.plist` file, and an interface file (that is, a storyboard or xib file).

By default, the Action template supplies the following `Info.plist` keys and values, shown here for an OS X target:

1. `<key>NSExtension</key>`
2. `<dict>`
3. `<key>NSExtensionAttributes</key>`
4. `<dict>`
5. `<key>NSExtensionServiceRoleType</key>`
6. `<string>NSExtensionServiceRoleTypeEditor</string>`
7. `</dict>`
8. `<key>NSExtensionPointIdentifier</key>`
9. `<string>com.apple.ui-services</string>`
10. `<key>NSExtensionPrincipalClass</key>`
11. `<string>ActionViewController</string>`
12. `</dict>`

To specify the task your OS X Action extension enables, use one of the following values for the required `NSExtensionServiceRoleType` key:

- `NSExtensionServiceRoleTypeEditor`—The extension enables editing or other content transformation and returns the user’s edits to the host app
- `NSExtensionServiceRoleTypeViewer`—The extension lets users view the selected content in a different way, such as in a different format

An Action extension uses the view controller’s [extensionContext](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621411-extensioncontext) property to get an [NSExtensionContext](https://developer.apple.com/documentation/foundation/nsextensioncontext) object. In OS X, the extension context contains the user’s selected content as well as the size and position of that content.

In iOS, an extension context has content specified explicitly by the host app; this can, at the discretion of the host, include user selected content.

To learn more about the extension context, see [Respond to the Host App’s Request](ExtensionCreation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqnjnknltg).

### Design the UI

> [!IMPORTANT]
> 

__iOS.__ If you want to present your iOS Action extension full screen, add the following key-value pair to the extension’s `NSExtension` dictionary:

1. `<key>NSExtensionActionWantsFullScreenPresentation</key>`
2. `<true/>`

__OS X.__ Consider the size and position of the selected content in the host app when specifying the size and position of the Action extension’s view.

Use the [preferredContentSize](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434409-preferredcontentsize) property of the [NSViewController](https://developer.apple.com/documentation/appkit/nsviewcontroller) class to specify the extension view’s preferred size, based on the size of the selected content. (You can also specify minimum and maximum sizes for the extension’s view, to ensure that a host app doesn’t make unreasonable adjustments to your view.) To specify a preferred position for the extension view, set the [preferredScreenOrigin](https://developer.apple.com/documentation/appkit/nsviewcontroller/1434468-preferredscreenorigin) property to the lower-left corner of the extension’s view.

### Returning Edited Content to the Host

On both platforms, an Action extension uses an [NSExtensionContext](https://developer.apple.com/documentation/foundation/nsextensioncontext) method to send the user’s edits to the host app. [Listing 5-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqmjtfvjvonq) shows code that returns edited text to the host app when the user chooses a Done button.

__Listing 5-1__Sending edited items to the host app

1. `- (IBAction)done:(id)sender {`
2. `NSExtensionItem *outputItem = [[NSExtensionItem alloc] init];`
3. `outputItem.attributedContentText = self.myTextView.attributedString;`
5. `NSArray *outputItems = @[outputItem];`
6. `[self.extensionContext completeRequestReturningItems:outputItems];`
7. `}`

[Handling Common Scenarios](ExtensionScenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqmrrfvjvomi)

[Audio Unit](AudioUnit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqmrsfvjvomi)
