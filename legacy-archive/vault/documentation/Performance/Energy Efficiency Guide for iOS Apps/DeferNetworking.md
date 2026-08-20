---
title: Energy Efficiency Guide for iOS Apps
apple_id: TP40015243
resource_type: Guide
platform: watchOS|iOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/DeferNetworking.html
archived_at: '2026-07-18T01:47:30.930323Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for iOS Apps](index.md)



## Defer Networking

Apps that perform network operations should batch transactions and use appropriate APIs to minimize radio use, limit impact on the system, and increase energy efficiency. Apps should also let the system defer nonessential network activity for optimal times, such as when the device is plugged in or using Wi-Fi.

### Batch Transactions

Downloading content a bit at a time keeps the radios powered up almost continuously, wasting power. To the extent possible, your app should perform network operations together. For example:

- If your app streams video, download the entire file (or a large portion of the file) at once instead of requesting it in small pieces.
- If your app serves ads, download several at once and show them over a period of time, rather than downloading them as needed.
- If your app downloads email from a server, download multiple messages at once. Assume that the user will probably read most of them, rather than downloading each one individually as the user selects it.

### Delay Deferrable Network Operations

For upload and download activities over HTTP, the [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession) API provides the ability to create deferrable background sessions. A background session lets your app send URL requests to the system, which performs them at an optimal time and notifies your app when they are complete. There are several advantages to using this method for network activity:

- __Activity is performed out-of-process.__ Because the network operations are performed by the system, your app stays responsive, letting the user continue doing other work. Your app also doesn’t need to continue running for activity to complete.
- __Notifications keep your app informed.__ The system notifies your app when the activity is completed and if problems occur. Your app can even quit, relaunch, reconnect to a previous session, and resume receiving notifications. If your app isn’t running when the activities complete, or if authentication is required, the system can relaunch your app in the background.
- __Network activity is performed efficiently.__ It’s inefficient to perform network activity over a slow connection. Bandwidth monitoring lets the system defer the activity when throughput falls below a certain threshold.
- __Activity self-corrects.__ URL sessions can be automatically retried by the system when errors occur.

> [!NOTE]
> 

### Configure Background Session Options

Start by creating a background session configuration object. Give it a unique session identifier and flag it as a discretionary activity. Later, once the session is created, you can use the unique identifier to reconnect to the session even if your app is terminated and relaunched. See Listing 10-1.

__Listing 10-1__Configuring an NSURLSession background session

Objective-C

1. `// Set up a configuration with a background session ID`
2. `NSURLSessionConfiguration *configuration = [NSURLSessionConfiguration backgroundSessionConfigurationWithIdentifier:@"com.<YourApp>.<YourBackgroundSessionIdentifier>"];`
4. `// Set the configuration to discretionary`
5. `[configuration setDiscretionary: YES];`

Swift

1. `// Set up a configuration with a background session ID`
2. `let configuration = NSURLSessionConfiguration.backgroundSessionConfigurationWithIdentifier("com.<YourApp>.<YourBackgroundSessionIdentifier>")`
4. `// Set configuration to discretionary`
5. `configuration.discretionary = true`

> [!IMPORTANT]
> 

### Restrict the Background Session to only Wi-Fi

If desired, set the `allowsCellularAccess` property of the configuration object to perform the activity strictly when connected to Wi-Fi, as shown in Listing 10-2.

__Listing 10-2__Configuring a background NSURLSession session to run on Wi-Fi only

Objective-C

1. `// Set the configuration to run on Wi-Fi only`
2. `configuration.allowsCellularAccess = NO;`

Swift

1. `// Set the configuration to run on Wi-Fi only`
2. `configuration.allowsCellularAccess = false`

> [!IMPORTANT]
> 

### Adjust Scheduling Tolerance for the Background Session

By default, the system allows up to seven days for a background session to run. This means that the activity will occur at a power-optimal time _sometime_ within this timeframe. You can adjust the timeframe by changing the value (specified in seconds) of the `timeoutIntervalForResource` property of the configuration object. See Listing 10-3.

__Listing 10-3__Configuring a background NSURLSession session to run within a specified timeframe

Objective-C

1. `// Set the configuration to run sometime in the next 18 hours`
2. `[configuration setTimeoutIntervalForResource: 18 * 60 * 60];`

Swift

1. `// Set the configuration to run sometime in the next 18 hours`
2. `configuration.timeoutIntervalForResource(18 * 60 * 60)`

> [!IMPORTANT]
> 

### Create a Background Session Object

Once you set up a background session configuration object, create a new `NSURLSession` object for the configuration, as demonstrated in Listing 10-4.

__Listing 10-4__Creating an NSURLSession session using a configuration

Objective-C

1. `// Create the URL session`
2. `NSURLSession *backgroundSession = [NSURLSession sessionWithConfiguration:configuration delegate:self delegateQueue:nil];`

Swift

1. `// Create the URL session`
2. `let backgroundSession = NSURLSession(configuration: configuration, delegate: self, delegateQueue: nil)`

### Add a URL Request to the Background Session

Finally, create an instance of `NSURLRequest` and pass it to the background session, as shown in Listing 10-5.

__Listing 10-5__Creating a URL request and adding it to a background session

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
2. `let someURLToDownload = NSURL.URLWithString(<YourURLString>)`
4. `// Create a URL request`
5. `let downloadRequest = NSURLRequest.requestWithURL(someURLToDownload)`
7. `// Add request to background session`
8. `let downloadTask = backgroundSession.downloadTaskWithRequest(downloadRequest)`
10. `// Initiate activity`
11. `downloadTask.resume()`

> [!NOTE]
> 

### Get Notified About Background Session Activity

To receive callbacks when the background session receives a reply from the server, finishes downloading, or encounters an error, implement the appropriate delegate methods. Lists of available delegate methods are found in the following documents:

- _[NSURLSessionDataDelegate Protocol Reference](https://developer.apple.com/documentation/foundation/nsurlsessiondatadelegate)_
- _[NSURLSessionDelegate Protocol Reference](https://developer.apple.com/documentation/foundation/urlsessiondelegate)_
- _[NSURLSessionDownloadDelegate Protocol Reference](https://developer.apple.com/documentation/foundation/urlsessiondownloaddelegate)_
- _[NSURLSessionTaskDelegate Protocol Reference](https://developer.apple.com/documentation/foundation/nsurlsessiontaskdelegate)_

Listing 10-6 demonstrates how to respond to a callback once a URL download is complete.

__Listing 10-6__Example delegate method that is called once a URL finishes downloading

Objective-C

1. `- (void)URLSession:(NSURLSession *)session downloadTask:(NSURLSessionDownloadTask *)downloadTask didFinishDownloadingToURL:(NSURL *)location {`
2. `// Do any work following the completed download`
3. `};`

Swift

1. `func URLSession(session: NSURLSession, downloadTask downloadTask: NSURLSessionDownloadTask, didFinishDownloadingToURL location: NSURL) {`
2. `// Do any work following completed download`
3. `}`

[Minimize Networking](MinimizeNetworking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmjxfvjvomi)

[Voice Over IP (VoIP) Best Practices](OptimizeVoIP.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmzqfvjvomi)
