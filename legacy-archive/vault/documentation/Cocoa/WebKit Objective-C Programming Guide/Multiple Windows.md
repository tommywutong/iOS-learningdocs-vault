---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Tasks/MultipleWindows.html
archived_at: '2026-07-15T07:14:52.745310Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Objective-C Programming Guide](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)


[Next](Loading%20Pages.md)[Previous](Simple%20Browsing.md)

# Multiple Windows

If you are building a simple browser application, you’ll want to allow the user to open multiple windows and type in URLs. You also need to make some policy decisions about how to handle new window requests.

You can implement multiple windows in a WebKit application easily by beginning with a Cocoa document-based architecture as follows:

1. Using Xcode, create a document-based Cocoa application. Your new project file will already contain the needed classes and interface files to support multiple windows (namely `MyDocument.h`, `MyDocument.m`, and `MyDocument.nib`).
2. Add the WebKit frameworks to your project.
3. Open `MyDocument.nib` using Interface Builder and drag a WebView from the Cocoa—GraphicsViews palette to your document window.
4. Create a `webView` outlet in `MyDocument.h` and read the file into Interface Builder. Connect the `webView` outlet of the File’s Owner to the WebView object you created in the previous step.
5. Add code to `MyDocument.m` to load a default page. You can add this code fragment to the [windowControllerDidLoadNib:](https://developer.apple.com/documentation/appkit/nsdocument/1515221-windowcontrollerdidloadnib) method:

```
NSString *urlText = [NSString stringWithString:@"http://www.apple.com"];
[[webView mainFrame] loadRequest:[NSURLRequest requestWithURL:[NSURL URLWithString:urlText]]];
```
6. Build and run your application.

When you run your application you should see a window open displaying web content. You can also open multiple windows by selecting New from the File menu. This example demonstrates multiple WebView objects independently displaying web content.

If you want a user to type in her own URL, add a text field to the window and make a new load request every time the user enters a new URL. Here are the steps you follow:

1. Add a text field to the window in `MyDocument.nib`.
2. Add a `textField` outlet and a `connectURL:` action to `MyDocument.h`. Read in the changes to `MyDocument.h` from Interface Builder.
3. In Interface Builder, make a connection from the text field you created to the `textField` outlet of the File’s Owner and set the action to `connectURL:`. This method is invoked when the user enters in a new URL.
4. Implement the `connectURL:` method to load the URL typed in by the user:

```objc
- (IBAction)connectURL:(id)sender{
    [[webView mainFrame] loadRequest:[NSURLRequest requestWithURL:[NSURL URLWithString:[sender stringValue]]]];
}
```
5. Build and run your application.

Now when you enter a new URL in the text field, a new page is loaded.

By default, if you click a link that requests a new window be opened to display the content of that link, nothing happens. If you want to change this behavior, your application needs to make a policy decision about new window requests. You need to implement a `WebUIDelegate` object to handle this case. Again, implement the delegate methods you want. Here are the steps to follow:

1. Set the delegate after `MyDocument.nib` is loaded. If you have a Cocoa document-based application, then you can add this code to MyDocument’s [windowControllerDidLoadNib:](https://developer.apple.com/documentation/appkit/nsdocument/1515221-windowcontrollerdidloadnib) method:

```
[webView setUIDelegate:self];
```
2. It is good practice for browser-like applications to set the group name of WebView objects after they are loaded from a nib file. Otherwise, clicking on some links may result in multiple new window requests because the HTML code for a link might not use the same frame name. The group name is an arbitrary identifier used to group related frames. For example, you can set the group name as follows:

```
[webView setGroupName:@"MyDocument"];
```
3. Implement the `webView:createWebViewWithRequest:` delegate method to create a window containing a web view, and load the request:

```objc
- (WebView *)webView:(WebView *)sender createWebViewWithRequest:(NSURLRequest *)request
{
    id myDocument = [[NSDocumentController sharedDocumentController] openUntitledDocumentAndDisplay:YES error:nil];
    [[[myDocument webView] mainFrame] loadRequest:request];
    return [myDocument webView];
}
```
4. Build and run your application.

Now, when you click a link that requests a new window, a new window is created to display the content of that link. This is just one example of many decisions your application can make about policies and the behavior of the user interface. You use the other WebUIDelegate methods and other WebView delegates to modify the behavior.

[Next](Loading%20Pages.md)[Previous](Simple%20Browsing.md)

