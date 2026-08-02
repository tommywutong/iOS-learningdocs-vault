---
title: App Sandbox Design Guide
apple_id: TP40011183
resource_type: Guide
platform: macOS
topic: Security
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AppSandboxQuickStart/AppSandboxQuickStart.html
archived_at: '2026-07-27T06:57:08.330780Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Sandbox Design Guide](About%20App%20Sandbox.md)


[Next](App%20Sandbox%20in%20Depth.md)[Previous](About%20App%20Sandbox.md)

# App Sandbox Quick Start

In this Quick Start you get a macOS app up and running in a sandbox. You verify that the app is indeed sandboxed and then learn how to troubleshoot and resolve a typical App Sandbox error. The apps you use are Xcode, Activity Monitor, Terminal, and Console.

## Create the Xcode Project

The app you create in this Quick Start uses a web view and consequently uses a network connection. Under App Sandbox, network connections don’t work unless you specifically allow them—making this a good example app for learning about sandboxing.

![bullet](attachments/Resources/1282/Images/task_2x.png)To create the Xcode project for this Quick Start

1. In Xcode, create a new Xcode project for a macOS Cocoa application.

   - Name the project AppSandboxQuickStart.
   - Set an organization name and identifier, if none is already set. The organization identifier, which becomes the first part of the bundle identifier, is typically constructed using the reverse-DNS format, as described in About Bundle IDs. So if your organization name is Acme, your organization identifier would be `com.Acme`, which results in a bundle identifier of `com.Acme.AppSandboxQuickStart`.
   - Ensure that the Use Storyboards checkbox is selected and that the other checkboxes are unselected.
2. In the project navigator, click the `Main.storyboard` file.

   The Interface Builder canvas appears.
3. In the object library (in the utilities area), locate the [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview) object.
4. Drag a WebKit view onto the view managed by the view controller in the View Controller Scene on the canvas.
5. (Optional) To improve the display of the web view in the running app, perform the following steps:

   - Drag the sizing controls on the web view so that it completely fills the view controller’s main view.
   - Add constraints to the web view to pin its top, bottom, left, and right edges to the main view.
6. Add the WebKit framework to the app.

   - Import the WebKit framework by adding the following statement above the interface block in the `ViewController.h` header file:

     ```
     @import WebKit;
     ```
   - Link the WebKit framework to the Quick Start project as a required framework.

   __Note:__ If you are compiling for OS X 10.7 and want to play HTML5 embedded videos in this application, you must also link to the AV Foundation framework. This is not required in macOS 10.8 and later.
7. Create and connect an outlet for the web view in the `ViewController` class.

   In the view controller’s interface (either in `ViewController.h` or in a category in `ViewController.m`), add this:

   ```objc
   @property (weak) IBOutlet WKWebView *webView;
   ```
8. Connect the web view to the app delegate outlet you just created.
9. Add the following to the `viewDidLoad` method of the view controller:

   ```
   [self.webView loadRequest:
       [NSURLRequest requestWithURL:
           [NSURL URLWithString: @"http://www.apple.com"]]];
   ```

   When the view loads, this method requests the specified URL from the computer’s network connection and then sends the result to the web view for display.

Now, build and run the app.

## Confirm That the App Is Sandboxed

The window opens, but no web content appears. This is because sandboxing is enabled for all new Cocoa apps by default, but you haven’t yet conferred permission to access a network connection.

Apart from blocked behavior, there are a few specific signs that a macOS app is sandboxed.

![bullet](attachments/Resources/1282/Images/task_2x.png)To confirm that the Quick Start app is successfully sandboxed

1. Select the project file in the Xcode project navigator, and then the target, and finally the Capabilities pane. You should see that the App Sandbox capability is On, but that no specific capabilities are selected. If you did want to disable sandboxing, you would do it by changing the switch to Off.
2. In Finder, look at the contents of the `~/Library/Containers/` folder.

   Because the Quick Start app is sandboxed, there's now a container folder named after your app. The name includes the company identifier for the project, so the complete folder name would be, for example, `com.Acme.AppSandboxQuickStart`.

   The system creates an app’s container folder, for a given user, the first time the user runs the app.

   __Note:__ In macOS 10.8 and later, Finder hides the `~/Library` folder by default. To see it, choose Go > Go To Folder… and enter `~/Library` in the dialog that appears.
3. In Activity Monitor, check that the system recognizes the app as sandboxed.

   - Launch Activity Monitor (available in `/Applications/Utilities`).
   - In Activity Monitor, choose View > Columns.

     Ensure that the Sandbox menu item is checked.
   - In the Sandbox column, confirm that the value for the Quick Start app is Yes.

     To make it easier to locate the app in Activity monitor, enter the name of the Quick Start app in the Filter field.
4. Check that the app binary is sandboxed. In a Terminal window, enter the following command:

   ```
   codesign -dvvv --entitlements :- <executable-path>
   ```

   where `<executable-path>` is the complete path for the app’s main executable binary inside the app bundle (for example, `AppSandboxQuickStart.app/Contents/MacOS/AppSandboxQuickStart`). The output generated by this command contains the property list of entitlements, which includes `com.apple.security.app-sandbox` set to `true` if the app is sandboxed.

__Important:__ The above steps are sufficient for the Quick Start app, but are not sufficient for apps that contain embedded helper apps, XPC services, or other tools. For more information, read [External Tools, XPC Services, and Privilege Separation](App%20Sandbox%20in%20Depth.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmznknlte).

![tip icon](attachments/Resources/1282/Images/tips_2x.png)

__Tip:__ If the app crashes when you attempt to run it, specifically by receiving an `EXC_BAD_INSTRUCTION` signal, the most likely reason is that you previously ran a sandboxed app with the same bundle identifier but a different code signature. This crashing upon launch is an App Sandbox security feature that prevents one app from masquerading as another and thereby gaining access to the other app’s container.

You learn how to design and build your apps, in light of this security feature, in [App Sandbox and Code Signing](App%20Sandbox%20in%20Depth.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmznknlts).

## Resolve an App Sandbox Violation

An App Sandbox violation occurs if your app tries to do something that App Sandbox doesn’t allow. For example, you have already seen in this Quick Start that the sandboxed app is unable to retrieve content from the web. Fine-grained restriction over access to system resources is the heart of how App Sandbox provides protection should an app become compromised by malicious code. Resolving such violations involves adding specific entitlements in Xcode corresponding to the capabilities your app needs.

![bullet](attachments/Resources/1282/Images/task_2x.png)To resolve the App Sandbox violation by adding the appropriate entitlement

1. Quit the Quick Start app.
2. In the Capabilities tab of the target editor, within the App Sandbox section, select the entitlement that corresponds to Outgoing Connections (Client). Doing so applies a `TRUE` value for the needed entitlement to the Xcode project by modifying the `.entitlements` property list file.

   __Note:__ Network entitlements are specified in terms of who establishes the connection, not the primary direction of data flow. In this example, you need the Outbound Connection capability because the app is initiating the connection. An app acting as a server would require the Inbound Connection entitlement.
3. Build and run the app.

   The intended webpage now displays in the app.

## Next Steps

This chapter has shown how to use entitlements to enable App Sandbox and request resource access for a simple example app, but this is only a start. For a real app, you additionally code sign your app with a distribution identity before you can distribute it. When you begin to access the file system, you work within your container directories. When files are brought into your sandbox by the user through natural interactions like drag and drop, you create security-scoped bookmarks to maintain persistent access to these files over time. As your app grows in complexity, you introduce privilege separation to implement even finer grained resource control. Together, these techniques offer a means to contain damage if the worst happens.

[Next](App%20Sandbox%20in%20Depth.md)[Previous](About%20App%20Sandbox.md)
