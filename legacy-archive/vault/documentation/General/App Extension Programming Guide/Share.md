---
title: App Extension Programming Guide
apple_id: TP40014214
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: null
published: '2017-10-19'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Share.html
archived_at: '2026-07-15T07:34:02.672880Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Extension Programming Guide](index.md)



## Share

Share extensions give users a convenient way to share content with other entities, such as social sharing websites or upload services. For example, in an app that includes a Share button, users can choose a Share extension that represents a social sharing website and then use it to post a comment or other content.

> [!NOTE]
> 

### Understand Share Extensions

On both platforms, a Share extension should:

- Make it easy for users to post content
- Let users preview, edit, annotate, and configure content, if appropriate
- Validate the user’s content before sending it

> [!NOTE]
> 

Users get access to Share extensions in the system-provided UI. In iOS, users tap the Share button and choose a Share extension from the sharing area of the activity view controller that appears. In OS X, users can reveal the list of sharing services in a few different ways. For example:

- Click the Share button in an app.
- View the Social area in Notification Center.
- Select some content, Control-click to reveal a contextual menu, and choose Share.

When users choose your Share extension, you display a view in which they compose their content and post it. You can base your view on the system-provided compose view controller, or you can create a completely custom compose view. The system-provided compose view controller builds in some support for common tasks, such as previewing and validating standard items, synchronizing content and view animation, and configuring a post.

### Use the Xcode Share Template

The Xcode Share template provides default header and implementation files for the principal view controller class (called `SharingViewController`), an `Info.plist` file, and an interface file (that is, a storyboard or xib file).

> [!NOTE]
> 

When you create a target that uses the standard compose view UI, the principal view controller class inherits from [SLComposeServiceViewController](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller) and the default files include stubs for methods such as [didSelectPost](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1488578-didselectpost) and [isContentValid](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1488591-iscontentvalid).

By default, the Share template supplies the following `Info.plist` keys and values (shown here for an iOS target):

1. `<key>NSExtension</key>`
2. `<dict>`
3. `<key>NSExtensionMainStoryboard</key>`
4. `<string>MainInterface</string>`
5. `<key>NSExtensionPointIdentifier</key>`
6. `<string>com.apple.share-services</string>`
7. `</dict>`

Depending on the functionality of your Share extension, you might need to add keys and values to the default property list. For example, to provide a JavaScript file that accesses a webpage, add the `NSExtensionAttributes` key and a dictionary that specifies the file. (To learn more about how to use JavaScript to access a webpage, see [Accessing a Webpage](ExtensionScenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqmrrfvjvomjs).) You also add keys and values if you want to specify the data types your extension works with (to learn more, see [Declaring Supported Data Types for a Share or Action Extension](ExtensionScenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqmrrfvjvooa)).

A Share extension uses its principal view controller’s [extensionContext](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621411-extensioncontext) property to get the [NSExtensionContext](https://developer.apple.com/documentation/foundation/nsextensioncontext) object that contains the user’s initial text and any attachments for a post, such as links, images, or videos. The extension context object also contains information about the status of the posting operation. (To learn more about how an extension can interact with its context, see [Respond to the Host App’s Request](ExtensionCreation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqnjnknltg).)

The default [SLComposeServiceViewController](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller) object includes a text view that displays the user’s editable text content. When a user chooses Post, a Share extension validates the text view’s content (in addition to attachments, if any) and calls the `completeRequestReturningItems:expirationHandler:completion:` method of `NSExtensionContext`, using code like the following:

1. `NSExtensionItem *outputItem = [[NSExtensionItem alloc] init];`
2. `// Set the appropriate value in outputItem`
3. `NSArray *outputItems = @[outputItem];`
4. `[self.extensionContext completeRequestReturningItems:outputItems expirationHandler:nil completion:nil];`

### Design the UI

> [!IMPORTANT]
> 

The sharing UI on both platforms is constrained in size. In particular, your Share extension can’t increase in width, and although it may increase in height, you don’t want to force users to scroll too much.

If the system-supplied compose view meets your needs, you don’t need to supply any custom UI.

In general, you don’t want to overcomplicate a simple task, but you also want to give users the options they expect. For example, you want users to be able to post a simple remark with very little effort, but you may also want to help users preview an attachment, tag a post, or specify details, such as a privacy setting or an album to use.

When you have additional content to display, you can rely on Auto Layout constraints to adjust the view’s height as appropriate. If you don’t use Auto Layout, you can use the `UIViewController` property [preferredContentSize](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621476-preferredcontentsize) to specify the view’s new height.

__iOS.__ If you want to animate the display of your content to coincide with the resize animation, implement `viewWillTransitionToSize:withTransitionCoordinator:`, using [animateAlongsideTransition:completion:](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/1619300-animatealongsidetransition) to add your animations to the `coordinator` parameter.

### Posting Content

The primary purpose of a Share extension is to help users post content. When a user chooses the Post or Send button in your Share extension, a system-provided animation provides feedback that the action is being processed. The system then calls the [didSelectPost](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1488578-didselectpost) method of the `SLComposeServiceViewController` class. Implement this method to:

- Set up a background-mode URL session (using the [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession) class) that includes the content to post
- Initiate the upload
- Call the [completeRequestReturningItems:completionHandler:](https://developer.apple.com/documentation/foundation/nsextensioncontext/1411301-completerequest) method, which signals the host app that its original request is complete
- Prepare to be terminated by the system

[Listing 12-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqmjsfvjvomjv) shows one way to implement the `didSelectPost` method.

__Listing 12-1__An example implementation of `didSelectPost`

1. `- (void)didSelectPost {`
2. `// Perform the post operation.`
3. `// When the operation is complete (probably asynchronously), the Share extension should notify the success or failure, as well as the items that were actually shared.`
5. `NSExtensionItem *inputItem = self.extensionContext.inputItems.firstObject;`
7. `NSExtensionItem *outputItem = [inputItem copy];`
8. `outputItem.attributedContentText = [[NSAttributedString alloc] initWithString:self.contentText attributes:nil];`
9. `// Complete this implementation by setting the appropriate value on the output item.`
11. `NSArray *outputItems = @[outputItem];`
13. `[self.extensionContext completeRequestReturningItems:outputItems expirationHandler:nil completion:nil];`
14. `// Or call [super didSelectPost] to use the superclass's default completion behavior.`
15. `}`

> [!NOTE]
> 

If a user cancels a post, or if a post is canceled for some other reason, the system calls the Share extension’s [didSelectCancel](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1488556-didselectcancel) method when the feedback animation completes. Implement this method if it makes sense to customize the extension context’s completion operation.

### Validating Input

Share extensions should validate the user’s content before posting it. It’s best when the compose view gives users feedback about their content by enabling or disabling the Post button and, optionally, by displaying the current character count.

If you’re using the standard compose view controller (an instance of the [SLComposeServiceViewController](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller) class), check the validity of the user’s current content by implementing the [isContentValid](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1488591-iscontentvalid) method. The system calls `isContentValid` when the user changes the text in the standard compose view, so you can display the current character count and enable the Post button when appropriate. [Listing 12-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqmjsfvjvomjq) shows an example implementation of the `isContentValid` method for a sharing service that requires posts to contain fewer than 100 characters.

__Listing 12-2__An example implementation of `isContentValid`

1. `- (BOOL)isContentValid {`
2. `NSInteger messageLength = [[self.contentText stringByTrimmingCharactersInSet:[NSCharacterSet whitespaceCharacterSet]] length];`
3. `NSInteger charactersRemaining = 100 - messageLength;`
4. `self.charactersRemaining = @(charactersRemaining);`
6. `if (charactersRemaining >= 0) {`
7. `return YES;`
8. `}`
10. `return NO;`
11. `}`

If your Share extension needs to validate content in custom ways, do the validation in an implementation of the [validateContent](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1488550-validatecontent) method. Depending on the result, you can return the correct value in your [isContentValid](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1488591-iscontentvalid) method.

For example, if you need to shrink an asset before letting users upload it, you don’t want to enable the Post button until the shrinking is complete. To find out if the shrinking is done, call `validateContent` within your `isContentValid` method and return the appropriate result.

### Previewing Content (iOS Only)

To help users preview their selected content, the system-provided compose view controller ([SLComposeServiceViewController](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller)) provides a default view that can automatically display previews of standard data types, such as photos, videos, and webpages. If your iOS Share extension can handle nonstandard data types, you can implement the [loadPreviewView](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1623321-loadpreviewview) method to display them. Typically, an iOS Share extension checks the content in the [attachments](https://developer.apple.com/documentation/foundation/nsextensionitem/1416690-attachments) property of an extension item and provides a custom preview view, if appropriate.

iOS displays preview views next to the text-editing area in the sharing UI. As much as possible, you should create small preview views to avoid making the text area uncomfortably small. And although the sharing UI can expand in height, greater height can cause your content to display behind the keyboard, forcing users to scroll.

### Configuring a Post (iOS Only)

The [SLComposeSheetConfigurationItem](https://developer.apple.com/documentation/social/slcomposesheetconfigurationitem) class makes it easy for iOS Share extensions to provide a list of items that help users configure a post. For example, you might let users choose an account to post from, specify privacy settings, or autocomplete a custom text entry, such as a Twitter mention. By default, the standard compose view controller (`SLComposeServiceViewController`) displays your configuration items in a table view at the bottom of the sharing UI.

A Share extension uses the [configurationItems](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1623325-configurationitems) property of the `SLComposeServiceViewController` class to return an array of `SLComposeSheetConfigurationItem` instances, each of which identifies a type of configuration the user can make. When a user taps a configuration item, the item can display a custom view controller that lets the user perform the configuration.

To display a custom configuration view controller, you typically define a block of type [SLComposeSheetConfigurationItemTapHandler](https://developer.apple.com/documentation/social/slcomposesheetconfigurationitemtaphandler) (in which you create the view controller) and then call [pushConfigurationViewController:](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1623322-pushconfigurationviewcontroller) to display it. The standard compose view controller uses a [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) instance to display your configuration view controller, so users can tap the Back button to return to the sharing UI. You can also call [popConfigurationViewController](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1623323-popconfigurationviewcontroller) to return to the sharing UI in response to some other user action.

If appropriate, you can replace the list of configuration items with a custom view controller that displays custom autocompletion suggestions while a user is entering text. You might want to do this if your sharing service defines certain textual items that users are likely to enter.

[Photo Editing](Photos.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqmjxfvjvomi)

[Today](Today.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqmjrfvjvomi)
