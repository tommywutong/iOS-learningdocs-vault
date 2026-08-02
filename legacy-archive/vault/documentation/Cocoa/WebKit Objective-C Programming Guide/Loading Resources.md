---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Tasks/ResourceLoading.html
archived_at: '2026-07-15T07:14:53.764346Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Objective-C Programming Guide](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)


[Next](Paging%20Back%20and%20Forward.md)[Previous](Loading%20Pages.md)

# Loading Resources

Your application can also monitor the progress of loading content—that is, the progress of loading individual resources on a page. A resource is any data on a page that is loaded separately, such as images, scripts, style sheets and webpages contained in frames. A webpage can include multiple resources, each having their own request and response messages. Once a page is requested, each resource for that page can arrive independently and in any order. Some may load successfully, and others may not. If you want to be notified of the progress, success or failure of loading resources, you need to implement a resource load delegate for your WebView object.

As a resource goes through the process of loading, WebKit sends a series of messages to the resource load delegate. The exact sequence depends on the resource and if an error occurred during the load. Since _[WebResourceLoadDelegate Protocol Reference](https://developer.apple.com/documentation/webkit/webresourceloaddelegate)_ is an informal protocol a message is not sent to the delegate unless it responds to it. For example, the sequence of messages for a resource that loads successfully might be:

1. `webView:identifierForInitialRequest:fromDataSource:` —invoked before other delegate methods to return the application-defined resource identifier.
2. `webView:resource:willSendRequest:redirectResponse:fromDataSource:` —invoked one or more times before a request to load a resource is sent.
3. `webView:resource:didReceiveResponse:fromDataSource:`—invoked once when the first byte of data arrives.
4. `webView:resource:didReceiveContentLength:fromDataSource:`—invoked zero or multiple times per resource until all the data for that resource is loaded.
5. `webView:resource:didFinishLoadingFromDataSource:` —invoked when all the data for the resource has arrived.

If the resource load failed, then `webView:resource:didFailLoadingWithError:fromDataSource:` is invoked instead of `webView:resource:didFinishLoadingFromDataSource:`. Other messages per redirects can arrive, too. See _[WebResourceLoadDelegate Protocol Reference](https://developer.apple.com/documentation/webkit/webresourceloaddelegate)_ for a complete list of delegate methods.

Because resource load delegates might need to distinguish between the different resources on a page, a resource identifier is passed as one of the arguments of the messages to delegates. The identifier remains the same for each load even if the request changes. For example, a request may change if headers are added, the URL is canonicalized, or the URL is redirected.

Your application can provide this identifier by implementing the `webView:identifierForInitialRequest:fromDataSource:` method to create and return a resource identifier. Otherwise, the resource identifier passed to subsequent delegate messages will not be unique. For example, this method can return a sequential number:

```objc
- (id)webView:(WebView *)sender
identifierForInitialRequest:(NSURLRequest *)request fromDataSource:(WebDataSource *)dataSource
{
    // Return some object that can be used to identify this resource
    return [NSNumber numberWithInt:resourceCount++];
}
```


One reason for implementing a resource load delegate is to track the progress of individual resource loads. For example, you can keep track of the number of resources successfully and unsuccessfully loaded per page by implementing the following delegate methods. In this example, the resource status is displayed as “Loaded X of Y resources, Z resource errors.” Each delegate method below increments these X, Y and Z values. Follow these steps to display the resource load status messages:

1. Add these instance variables to your delegate class:

```
 int resourceCount;
 int resourceFailedCount;
 int resourceCompletedCount;
```
2. Implement the `webView:resource:willSendRequest:redirectResponse:fromDataSource:` method to update the display when WebKit begins to load a resource. Note that this method also allows you to return a modified request. Normally you don’t need to modify it.

```objc
-(NSURLRequest *)webView:(WebView *)sender
resource:(id)identifier
willSendRequest:(NSURLRequest *)request
redirectResponse:(NSURLResponse *)redirectResponse
fromDataSource:(WebDataSource *)dataSource
{
    // Update the status message
    [self updateResourceStatus];
    return request;
}
```
3. Implement the `updateResourceStatus` method, invoked in the sample code above, to use the `resourceCount` instance variable to update the display. You increment the `resourceCount` instance variable in the `webView:identifierForInitialRequest:fromDataSource:` method as shown in Identifying Resources.
4. Implement the `webView:resource:didFailLoadingWithError:fromDataSource:` method to increment the number of failed resource loads and update the display as in:

```objc
-(void)webView:(WebView *)sender resource:(id)identifier
didFailLoadingWithError:(NSError *)error
fromDataSource:(WebDataSource *)dataSource
{
    resourceFailedCount++;
    // Update the status message
    [self updateResourceStatus];
}
```
5. Implement the `webView:resource:didFinishLoadingFromDataSource:` method to increment the number of successful resource loads, and update the display as in:

```objc
-(void)webView:(WebView *)sender
resource:(id)identifier
didFinishLoadingFromDataSource:(WebDataSource *)dataSource
{
    resourceCompletedCount++;
    // Update the status message
    [self updateResourceStatus];
}
```
6. Implement the `updateResourceStatus` method to update your display.
7. Also, implement the frame load `webView:didStartProvisionalLoadForFrame:` delegate method to reset these variables to `0` when a new page load starts.
8. Build and run your application.

When you run your application you should see a progress message showing the total number of resources per page, and progressively how many resources are loaded successfully and unsuccessfully.

[Next](Paging%20Back%20and%20Forward.md)[Previous](Loading%20Pages.md)

