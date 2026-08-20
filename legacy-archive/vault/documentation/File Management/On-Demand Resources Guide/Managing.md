---
title: On-Demand Resources Guide
apple_id: TP40015083
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: Foundation
published: '2017-01-12'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/On_Demand_Resources_Guide/Managing.html
archived_at: '2026-07-15T07:32:09.332629Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [On-Demand Resources Guide](index.md)



## Accessing and Downloading On-Demand Resources

An app uses [NSBundleResourceRequest](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest) to:

- Request access to on-demand resources
- Inform the operating system when access is no longer needed
- Update the priority of a download
- Track the progress of a download
- Check for a notification of low disk space

You use other methods in [NSBundle](https://developer.apple.com/documentation/foundation/nsbundle) to set the preservation priority in local storage of the downloaded resources.

### Requesting Access

The app must request access to a tag before using any of the tag’s associated resources by initializing an `NSBundleResourceRequest` instance. The first step is to create an `NSBundleResourceRequest` object for the tags. A tag can be managed by multiple `NSBundleResourceRequest` objects.

### Initializing an NSBundleResourceRequest Instance

Each instance of `NSBundleResourceRequest` manages a set of tags that are in the same resource bundle. For more information on bundles, see _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_. You set the managed tags and their bundle when the instance is initialized using one of two methods:

- Use [initWithTags:](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614837-initwithtags) if all of the resources associated with the tags are in the main bundle.
- Use [initWithTags:bundle:](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614842-initwithtags) if all of the resources associated with the tags are in the same custom bundle.

  > [!NOTE]
  > 

> [!IMPORTANT]
> 

Listing 4-1 shows an example of initializing a resource manager for managing access to the on-demand resources that are tagged with `birds`, `bridge`, or `city`. The tags and their associated resources are configured in Xcode as described in [Creating and Assigning Tags](Tagging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2taobtfvbuqmznknltc). All of the resources are part of the main bundle.

__Listing 4-1__ Initializing an `NSBundleResourceRequest` instance

1. `// Create an NSSet object with the desired tags`
2. `NSSet *tags = [NSSet setWithObjects: @"birds", @"bridge", @"city"];`
4. `// Use the shorter initialization method as all resources are in the main bundle`
5. `resourceRequest = [[NSBundleResourceRequest alloc] initWithTags:tags];`

> [!IMPORTANT]
> 

### Requesting Access to the Tags

After initializing the instance, the next step is to request access to the on-demand resources that are associated with the tags. When all the resources for the requested tags are in local storage, the operating system retains them and uses a callback to inform the app that they are available. For more information, see stage 6 of the [On-Demand Resource Life Cycle](index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2taobtfvbuqmrnknlte).

You can use one of two methods to request access to resources. The main difference between the methods is how they respond if the resources are not on the device:

- [beginAccessingResourcesWithCompletionHandler:](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614840-beginaccessingresources) downloads the resources from the App Store.
- [conditionallyBeginAccessingResourcesWithCompletionHandler:](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614834-conditionallybeginaccessingresou) does not download the resources.

Each method takes a callback block that is called with the result of the access request. All of the associated resources will be on the device when the callback is invoked with a successful result.

Listing 4-2 shows [beginAccessingResourcesWithCompletionHandler:](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614840-beginaccessingresources). The callback block sets a flag that indicates whether the resources were downloaded. Your code should handle any errors including presenting feedback to the user. If there is no error, the app can start accessing the on-demand resources.

__Listing 4-2__ Using `beginAccessingResourcesWithCompletionHandler:`

1. `// Request access to the tags for this resource request`
2. `[resourceRequest beginAccessingResourcesWithCompletionHandler:`
3. `^(NSError * __nullable error)`
4. `{`
5. `// Check if there is an error`
6. `if (error) {`
7. `// There is a problem so update the app state`
8. `self.resourcesLoaded = NO;`
10. `// Should also inform the user of the error`
12. `return;`
13. `}`
15. `// The associated resources are loaded`
16. `self.resourcesAvailable = YES;`
17. `}`
18. `];`

The callback block is not called on the main thread. Any actions that access the user interface, such as presenting an error, must be dispatched to the main thread for execution. For information on how to dispatch calls to the main thread, see _[Concurrency Programming Guide](../../General/Concurrency%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojr)_.

> [!IMPORTANT]
> 

### Checking Whether Tags Are Already on the Device

[conditionallyBeginAccessingResourcesWithCompletionHandler:](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614834-conditionallybeginaccessingresou) grants access if the tags are already on the device. If the tags are not on the device, the app needs to call [beginAccessingResourcesWithCompletionHandler:](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614840-beginaccessingresources) to download them. Listing 4-3 shows an example of checking whether resources are already on the device. The callback checks whether the textures and graphics for an area of a world are loaded. If so it continues. Otherwise it calls another routine to load the resources.

> [!IMPORTANT]
> 

__Listing 4-3__ Using `conditionallyBeginAccessingResourcesWithCompletionHandler:`

1. `// Request access to tags that may already be on the device`
2. `[resourceRequest conditionallyBeginAccessingResourcesWithCompletionHandler:`
3. `^(BOOL resourcesAvailable)`
4. `{`
5. `// Check whether the resources are available`
6. `if (resourcesAvailable) {`
7. `// the associated resources are loaded, start using them`
8. `self.loadNewWorldArea = YES;`
9. `} else {`
10. `// The resources are not on the device and need to be loaded`
11. `// Queue up a call to a custom method for loading the tags using`
12. `// beginAccessingResourcesWithCompletionHandler:`
13. `NSOperationQueue.mainQueue().addOperationWithBlock(^{`
14. `[self loadTags:resourceRequest.tags forWorldArea:worldArea];`
15. `});`
16. `}`
17. `}`
18. `];`

### When to Request Tags

Request tags before you need them because it takes time to download the associated resources from the App Store. For example, if the user is playing level 1, start downloading level 2 so that it is loaded by the time the user has finished level 1.

The amount of time depends on several factors including the size of the associated resources and the speed of the connection between the device and the App Store.

In an ideal case with no restrictions on bandwidth or processing power, a tag with a size of 64 MB would take at least 1.7 seconds to download over a 300 Mbps 802.11n Wi-Fi or LTE cellular phone connection (peak LTE is 299.6 Mbps). However, in the real world, the amount of data that can flow over a connection to the Internet is far slower than 300 Mbps. In addition, the operating system usually uses a small amount of system resources for the download, resulting in longer transfer times.

You should test downloading speeds under various network conditions on the kinds of devices you expect your customers to use. Use the download speeds from the testing to estimate download times.

For more information, see [Designing for On-Demand Resources](AboutDesigningODR.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2taobtfvbuqmjvfvjvomi).

### Downloading and Downloading Priority

The [loadingPriority](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614841-loadingpriority) property of a resource request is used by the operating system as a hint for prioritizing the order of your download requests. Requests with a higher value for [loadingPriority](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614841-loadingpriority) are loaded before ones with a lower value.

Resource requests have a default priority that can be changed at any time, including during the download. Listing 4-4 shows an example of the code for changing the priority of a request.

__Listing 4-4__ Changing the priority of a download

1. `// The priority is a number between 0.0 and 1.0`
2. `self.resourceRequest.loadingPriority = 0.1;`

If the download is urgent, the app can use `NSBundleResourceRequestLoadingPriorityUrgent` for the loading priority. This tells the operating system to download the content as quickly as possible. One use for the constant is when the user must wait for the download before doing anything else. Listing 4-5 shows an example of setting the priority as urgent if the user is waiting.

__Listing 4-5__ Raising the priority of a request

1. `// Raise the priority based on the urgency`
2. `if (self.userWaiting) {`
3. `// The user is waiting, request the fastest download time`
4. `self.resourceRequest.loadingPriority = NSBundleResourceRequestLoadingPriorityUrgent;`
5. `} else {`
6. `// Set a higher priority`
7. `self.resourceRequest.loadingPriority = 0.8;`
8. `}`

### Tracking Download Progress

Soon after a download begins, the resource request starts updating [progress](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614838-progress), a property of type [NSProgress](https://developer.apple.com/documentation/foundation/nsprogress). The app tracks download progress using key-value observing (KVO) on the [fractionCompleted](https://developer.apple.com/documentation/foundation/nsprogress/1408579-fractioncompleted) property of [progress](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614838-progress). This requires that you start and stop observation and add code that executes when the value changes. Listing 4-6 shows how to start and stop observing the progress of the download. Listing 4-7 shows executing code when the value changes.

__Listing 4-6__ Start and stop tracking download progress

1. `// Start observing fractionCompleted to track the progress`
2. `[self.resourceRequest.progress addObserver:self`
3. `forKeyPath:@"fractionCompleted"`
4. `options:NSKeyValueObservingOptionNew`
5. `context:@"observeForrestLoad"`
6. `];`
8. `// Stop observing fractionCompleted to stop tracking the progress`
9. `[self.resourceRequest.progress removeObserver:self`
10. `forKeyPath:@"fractionCompleted"`
11. `context:@"observeForrestLoad"`
12. `];`

__Listing 4-7__ Executing code when [fractionCompleted](https://developer.apple.com/documentation/foundation/nsprogress/1408579-fractioncompleted) changes value

1. `-(void)observeValueForKeyPath:(NSString *)keyPath`
2. `ofObject:(id)object`
3. `change:(NSDictionary *)change`
4. `context:(void *)context`
5. `{`
6. `// Check for the progress object and key`
7. `if ((object == self.resourceRequest.progress) &&`
8. `([keyPath isEqualToString:@"fractionCompleted"])) {`
9. `// Get the current progress as a value between 0 and 1`
10. `double progressSoFar = self.resourceRequest.progress.fractionCompleted;`
12. `// Do something with the value`
13. `}`
14. `}`

Two important uses for tracking the download are:

- __Adjusting the download priority.__ The download priority can be raised if the download is taking too long, and lowered if there is lots of time.
- __Providing feedback on progress to the user.__ Feedback uses the value of [fractionCompleted](https://developer.apple.com/documentation/foundation/nsprogress/1408579-fractioncompleted).

### Pausing and Canceling the Download

You pause, resume, or cancel the active download for the resource request by using the [progress](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614838-progress) property and the methods provided by [NSProgress](https://developer.apple.com/documentation/foundation/nsprogress) (see Listing 4-8). For more information on the methods, see _[NSProgress Class Reference](https://developer.apple.com/documentation/foundation/progress)_.

__Listing 4-8__ Pausing, resuming, and canceling the current download

1. `// Pause the current download`
2. `[self.resourceRequest.progress pause];`
4. `// Resume the current download`
5. `[self.resourceRequest.progress resume];`
7. `// Cancel the current download`
8. `[self.resourceRequest.progress cancel];`

### Ending Access

Ending access when the app has finished using a resource request allows the operating system to release the storage on the device. If there are no other resource requests using the same storage, the operating system can reclaim the storage if needed. For more information see stages 8 and 9 of [On-Demand Resource Life Cycle](index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2taobtfvbuqmrnknlte).

There are two ways to end access:

- Send [endAccessingResources](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614843-endaccessingresources) to the resource request, as shown in Listing 4-9.
- Deallocate the resource request.

> [!IMPORTANT]
> 

__Listing 4-9__ Ending access to requested tags

1. `// End access to the managed resources by calling this method`
2. `[self.resourceRequest endAccessingResources];`

After `endAccessingResources` is called, the resource request cannot be used again to request access. If the app needs to access the same tags, it must allocate another instance of [NSBundleResourceRequest](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest).

### Setting Preservation Priority

The preservation priority of a tag provides a hint to the operating system about the relative importance of keeping the associated resources in local storage. When the operating system needs to purge tags, it starts with the lowest preservation priority. You can set a high-preservation priority for tags that contain resources that are more important than others such as an in-app purchase, or resources for functionality that is used more frequently.

Preservation priority is set and checked using methods added to [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) as show in Listing 4-10.

__Listing 4-10__ Checking and setting preservation priority for a tag

1. `// Check the preservation priority for the an in-app purchase module`
2. `double currentPriority = [[NSBundle mainBundle] preservationPriorityForTag:@"iap-llamas"];`
4. `// Set the priority to the maximum of 1.0 (the default is 0.0)`
6. `// Create a set of tags used in the call to set priority`
7. `NSSet *tags = [NSSet setWithArray: @[@"iap-llamas"]];`
8. `[[NSBundle mainBundle] setPreservationPriority:1.0 forTags:tags];`

> [!NOTE]
> 

### Low-Space Warning

The operating system sends out the [NSBundleResourceRequestLowDiskSpaceNotification](https://developer.apple.com/documentation/foundation/nsbundleresourcerequestlowdiskspacenotification) notification if it is unable to free up enough storage space for the current resource request. Your app should stop accessing any tags that are not required, as described in [Ending Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2taobtfvbuqnbnknlti) above. The app can be terminated if the operating system is unable to free enough space.

In the simple example of a game with multiple levels, the user is in level 4, and the app requests tags for levels 3, 5, and 6. When a low-space warning occurs, the app can release the tags for levels 3 and 6. Listing 4-11 shows code to register for the low-space notification. Listing 4-12 shows a routine that releases tags that are not required.

__Listing 4-11__ Registering for the `NSBundleResourceRequestLowDiskSpaceNotification` notification

1. `// Register to call self.lowDiskSpace when the notification occurs`
2. `[[NSNotificationCenter defaultCenter]`
3. `addObserver:self`
4. `selector:@selector(lowDiskSpace:)`
5. `name:NSBundleResourceRequestLowDiskSpaceNotification`
6. `object:nil`
7. `];`

Registration for the notification is usually done by the app delegate or master view.

__Listing 4-12__ Notification handler for low disk space notification

1. `// Notification handler for low disk space warning`
2. `-(void)lowDiskSpace:(NSNotification*)theNotification`
3. `{`
4. `// Free the lower priority resource requests`
5. `for (NSBundleResourceRequest *atRequest in self.lowPriorityRequests) {`
6. `// End accessing the resources`
7. `[atRequest endAccessingResources];`
8. `}`
10. `// clear lowPriorityRequests preventing multiple calls to endAccesingResource`
11. `[self.lowPriorityRequests removeAllObjects];`
12. `}`

`lowPriorityRequests` is not part of any class provided by the operating system. It is a mutable set that that the app needs to create and maintain.

[Platform Sizes for On-Demand Resources](PlatformSizesforOn-DemandResources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2taobtfvbuqmrtfvjvomi)

[Debugging On-Demand Resources](DebugTips.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2taobtfvbuqnrnknlte)
