---
title: Energy Efficiency Guide for iOS Apps
apple_id: TP40015243
resource_type: Guide
platform: watchOS|iOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/MinimizeNetworking.html
archived_at: '2026-07-18T01:47:57.807648Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for iOS Apps](index.md)



## Minimize Networking

Network operations may be unavoidable and essential to your app. In many cases, however, networking can be minimized by adhering to some general guidelines.

### Reduce Data Sizes

Network transactions should be as small as possible to reduce overhead.

> [!TIP]
> 

### Reduce Media Quality and Size

If your app uploads, downloads, or streams media content, lower quality and smaller sizes reduce the amount of data being sent and received. Some apps let the user specify the quality and size. For example, when emailing a photo, Mail lets the user send a scaled version of the image at small, medium, or large size. The smallest size is the most energy efficient.

### Compress Data

Use compression algorithms to compact data as much as possible before sending or receiving it.

### Avoid Redundant Transfers

Your app shouldn’t repeatedly download the same data.

### Cache Data

Use caching to store infrequently updated data locally. Redownload the data only when it has changed or the user requests it. The [NSURLCache](https://developer.apple.com/documentation/foundation/nsurlcache) and [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession) APIs can be used to implement in-memory and on-disk caches for URL request data.

### Use Pausable and Resumable Transactions

Network conditions fluctuate, and signal loss can be a regular occurrence. Be prepared to resume interrupted transactions so the same content isn’t downloaded multiple times. In some cases, it makes sense to let users pause downloads and resume them later. For example, iOS lets users pause app downloads by tapping on a partially downloaded app icon.

The [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession) API lets you implement pause and resume functionality, without implementing caching.

### Handle Errors

Don’t attempt to perform network operations when the network is unavailable.

### Check Signal Conditions

If network operations fail, use the `SCNetworkReachability` API to to see whether the host is available. If there are signal problems, alert the user or defer work until the host is available again.

To determine whether a host is reachable, check for the absence of the `kSCNetworkReachabilityFlagsReachable` reachability flag, as demonstrated in Listing 9-1.

__Listing 9-1__Checking the availability of a host

Objective-C

1. `#import "SystemConfiguration/SCNetworkReachability.h"`
2. `...`
3. `// Create a reachability object for the desired host`
4. `NSString *hostName = @"someHostName";`
5. `SCNetworkReachabilityRef reachability = SCNetworkReachabilityCreateWithName(NULL, [hostName UTF8String]);`
7. `// Create a place in memory for reachability flags`
8. `SCNetworkReachabilityFlags flags;`
10. `// Check the reachability of the host`
11. `SCNetworkReachabilityGetFlags(reachability, &flags);`
13. `// Release the reachability object`
14. `CFRelease(reachability);`
16. `// Check to see if the reachable flag is set`
17. `if ((flags & kSCNetworkReachabilityFlagsReachable) == 0) {`
18. `// The target host is not reachable`
19. `// Alert the user or defer the activity`
20. `}`

Swift

1. `import SystemConfiguration`
2. `...`
3. `// Create a reachability object for the desired host`
4. `let hostName = "someHostName"`
5. `let reachability = SCNetworkReachabilityCreateWithName(nil, (hostName as NSString).UTF8String).takeRetainedValue()`
7. `// Create a place in memory for reachability flags`
8. `var flags: SCNetworkReachabilityFlags = 0`
10. `// Check the reachability of the host`
11. `SCNetworkReachabilityGetFlags(reachability, &flags)`
13. `// Check to see if the reachable flag is set`
14. `if ((flags & kSCNetworkReachabilityFlagsReachable) == 0) {`
15. `// The target host is not reachable`
16. `// Alert the user or defer the activity`
17. `}`

> [!NOTE]
> 

### Provide an Escape Route

Don’t wait forever for a response from the server that never comes. Let the user cancel long-running or stalled network operations, and set appropriate timeouts so your app doesn’t keep connections open needlessly.

### Use Retry Policies

If a transaction fails, try again when the network becomes available. Use the `SCNetworkReachability` API to determine or be notified when the network is available again.

[Energy and Networking](EnergyandNetworking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmjwfvjvomi)

[Defer Networking](DeferNetworking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmjyfvjvomi)
