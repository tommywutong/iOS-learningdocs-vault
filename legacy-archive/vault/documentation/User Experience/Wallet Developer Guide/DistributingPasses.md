---
title: Wallet Developer Guide
apple_id: TP40012195
resource_type: Guide
platform: watchOS|iOS
topic: User Experience
technology: PassKit
published: '2018-01-16'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/DistributingPasses.html
archived_at: '2026-07-18T02:12:14.316866Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Wallet Developer Guide](index.md)



## Distributing Passes

After you have created a signed, compressed pass bundle, getting it into Wallet is easy. Mail and Safari support passes in iOS 6 and later and in macOS v10.8.2 and later, so you can use them to distribute passes by email or from a website. In iOS, they add passes to the pass library directly. In macOS, they use iCloud to add passes to the user’s iOS devices.

> [!NOTE]
> 

The advantage of sending passes as an email attachment is simplicity. When users view the email, the pass appears and can be added to their pass library. During development, this is an easy way to get a pass onto your device. The disadvantage is that you can’t interact with the pass-installation process. For example, an email can’t present an alternative representation for older devices that don’t support passes.

Hosting passes on your web server gives you more control over the user experience, but it’s less simple. You can give your users a link to a landing page that lets them add the pass to their pass library. This page can also offer a representation of the pass in older formats, such as PDF. This landing page also gives you a place to ask the user to log in if needed.

> [!NOTE]
> 

Using your own app to install passes is appropriate when your app provides a richer experience by integrating with your systems and business. For information about how your app can interact with passes, see [Interacting with Passes in Your App](Apps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdcojvfvbuqnrnknltc).

Your website and email can use the Add to Wallet badge to give your users a visual queue to add the pass to Wallet. For more information, see the [Add to Apple Wallet Badge](https://developer.apple.com/wallet/) section of the Developer website. To create buttons for your app, use the [PKAddPassButton](https://developer.apple.com/documentation/passkit/pkaddpassbutton) class.

### Programmatically Adding Passes

Before attempting to add passes to Wallet, see whether the device supports adding passes. Call the [PKAddPassesViewController](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller) class’s [canAddPasses](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller/1619212-canaddpasses) method. If this method returns `YES``true`, add your passes.

To add a single pass, download the signed, encrypted package, and instantiate a [PKPass](https://developer.apple.com/documentation/passkit/pkpass) object using the downloaded data. Next, create a `PKAddPassesViewController` instance for the pass object. Present this view controller to the user.

This view controller shows the user your pass. The user can then approve or reject the pass.

> [!NOTE]
> 

Alternatively, you can bulk-add multiple passes, for example, when adding boarding passes for a multileg flight. Simply create an array of `PKPass` objects, and then present these passes to the user by calling the [PKPassLibrary](https://developer.apple.com/documentation/passkit/pkpasslibrary) class’s [addPasses:withCompletionHandler:](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617093-addpasses) method. This method presents a lightweight interface, letting the user review and approve all the passes in the array.

Due to the name change, apps running in iOS 9 and later should use buttons that refer to Wallet. Apps running in iOS 8 or earlier should use buttons that refer to Passbook. To create a Wallet-branded button, use the `PKAddPassButton` class. For Passbook branded buttons, use the resources described in [Passbook for Developers](https://developer.apple.com/passbook/) at the Developer website.

### Working with Web Views

If your pass is already available on the web, you may want to present that content directly in your app. There are several different ways to present web content from an iOS app. Some automatically handle pass files. Others require additional steps to download and process the pass.

Here are three recommended ways to present web content from an app:

- Open the web page in Safari, transferring control from your app to the Safari app.
- Present the content using an [SFSafariViewController](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller) view controller.
- Show the content in a [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview) instance.

Both the Safari app and the Safari view controller can import the pass files directly into the pass library.

If you want to load a file using a web view, you must detect the request, download the pass, and programmatically add the pass yourself.

For `WKWebView`, perform the following steps:

1. In your [WKNavigationDelegate](https://developer.apple.com/documentation/webkit/wknavigationdelegate) object’s [webView:decidePolicyForNavigationResponse:decisionHandler:](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455643-webview) method, check the response’s MIME type.
2. If the mime type is `application/vnd.apple.pkpass`, begin asynchronously downloading the pass from your server, and then call the delegate method’s decision handler. Pass [WKNavigationResponsePolicyCancel](https://developer.apple.com/documentation/webkit/wknavigationresponsepolicy/cancel) to keep the web view from loading the pass.
3. After the download completes, programatically add the pass using a [PKAddPassesViewController](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller) instance. For more information, see [Programmatically Adding Passes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdcojvfvbuqmjrfvjvomq).

[Pass Design and Creation](Creating.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdcojvfvbuqnbnknltc)

[Updating a Pass](Updating.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdcojvfvbuqnjnknltc)
