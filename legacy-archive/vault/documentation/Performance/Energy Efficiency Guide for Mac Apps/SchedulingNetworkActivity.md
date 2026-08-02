---
title: Energy Efficiency Guide for Mac Apps
apple_id: TP40013929
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/SchedulingNetworkActivity.html
archived_at: '2026-07-18T01:50:25.301933Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for Mac Apps](index.md)



## Schedule Background Networking

Apps that perform background networking should use appropriate APIs to limit impact on the system and increase energy efficiency. Nonessential network activity should allow the system to schedule the network activity for optimal times, such as when the Mac is plugged-in or on Wi-Fi.

### Schedule Deferrable Network Operations

For background upload and download activities over HTTP, `NSURLSession` provides the ability to create background sessions. A background session allows your app to issue URL requests to be performed. These requests are then sent to a system daemon, which performs them out-of-process and notifies your app when they are complete. There are numerous advantages to using this method for background network activity:

- Activity is performed out-of-process. Because the network activity is performed by the system, your app doesn’t need to be running anymore for activity to complete.
- Notifications keep your app informed. The system notifies your delegate when the activity is completed. Your app can even quit, relaunch, reconnect to a previous session, and resume receiving callbacks. If your app isn’t running when the activities complete, or if authentication is required, the system can even launch your app in the background.
- Network activity is performed efficiently. It’s inefficient to perform network activity over a slow connection. Bandwidth monitoring allows activity to be automatically deferred when throughput falls below a certain threshold. A background session can also defer activity when system thermals rise.
- Activity self-corrects. URL sessions can be automatically retried when errors occur.

### Configure a Background Session

To create a background session, create a new `NSURLSession`, give it a unique session identifier, and denote it as discretionary activity, as shown in Listing 13-1. Once the session has been created, you can use the unique identifier to reconnect to the session if your app quits and relaunches.

__Listing 13-1__Configuring and creating an NSURLSession background session

Objective-C

1. `// Set up a configuration with a background session ID`
2. `NSURLSessionConfiguration *configuration = [NSURLSessionConfiguration`
3. `backgroundSessionConfigurationWithIdentifier:@"com.<YourApp>.<YourBackgroundSessionIdentifier>"];`
5. `// Set configuration to discretionary`
6. `configuration.discretionary = YES;`
8. `// Create URL session`
9. `NSURLSession *backgroundSession = [NSURLSession sessionWithConfiguration:configuration delegate:self delegateQueue:nil];`

Swift

1. `// Set up a configuration with a background session ID`
2. `var configuration = NSURLSessionConfiguration.backgroundSessionConfigurationWithIdentifier("com.<YourApp>.<YourBackgroundSessionIdentifier>")`
4. `// Set configuration to discretionary`
5. `configuration.discretionary = true`
7. `// Create URL session`
8. `var backgroundSession = NSURLSession(configuration: configuration, delegate: self, delegateQueue: nil)`

Next, create an instance of `NSURLRequest`, and pass it to the background session, as shown in Listing 13-2.

__Listing 13-2__Creating a URL request and adding it to a background session

Objective-C

1. `// Set up a URL`
2. `NSURL *someURLToDownload = [NSURL URLWithString:<YourURLString>];`
4. `// Create a URL request`
5. `NSURLRequest *downloadRequest = [NSURLRequest requestWithURL:someURLToDownload];`
7. `// Add the request to the background session`
8. `NSURLSessionDownloadTask *downloadTask = [backgroundSession downloadTaskWithRequest:downloadRequest];`
10. `// Initiate the activity`
11. `[downloadTask resume];`

Swift

1. `// Set up a URL`
2. `var someURLToDownload = NSURL.URLWithString(<YourURLString>)`
4. `// Create a URL request`
5. `var downloadRequest = NSURLRequest.requestWithURL(someURLToDownload)`
7. `// Add request to background session`
8. `var downloadTask = backgroundSession.downloadTaskWithRequest(downloadRequest)`
10. `// Initiate activity`
11. `downloadTask.resume()`

To receive callbacks when the activity completes, implement the desired delegate methods, as demonstrated in Listing 13-3.

__Listing 13-3__Example delegate method to be called once a URL has been downloaded

Objective-C

1. `- (void)URLSession:(NSURLSession *)session downloadTask:(NSURLSessionDownloadTask *)downloadTask didFinishDownloadingToURL:(NSURL *)location {`
2. `// Do any work following the completed download`
3. `};`

Swift

1. `func URLSession(session: NSURLSession, downloadTask downloadTask: NSURLSessionDownloadTask, didFinishDownloadingToURL location: NSURL) {`
2. `// Do any work following completed download`
3. `}`

For additional information on the available delegate methods, refer to the relevant documentation:

- _[NSURLSessionDataDelegate Protocol Reference](https://developer.apple.com/documentation/foundation/nsurlsessiondatadelegate)_
- _[NSURLSessionDelegate Protocol Reference](https://developer.apple.com/documentation/foundation/urlsessiondelegate)_
- _[NSURLSessionDownloadDelegate Protocol Reference](https://developer.apple.com/documentation/foundation/urlsessiondownloaddelegate)_
- _[NSURLSessionTaskDelegate Protocol Reference](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate)_

For detailed information about creating URL sessions and requests, see _[NSURL Class Reference](https://developer.apple.com/documentation/foundation/nsurl)_, _[NSURLRequest Class Reference](https://developer.apple.com/documentation/foundation/nsurlrequest)_, and _[NSURLSession Class Reference](https://developer.apple.com/documentation/foundation/nsurlsession)_.

[Schedule Background Activity](SchedulingBackgroundActivity.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmzsfvjvomi)

[Defer Tasks with XPC Activity](CentralizedTaskScheduling.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmznknltc)
