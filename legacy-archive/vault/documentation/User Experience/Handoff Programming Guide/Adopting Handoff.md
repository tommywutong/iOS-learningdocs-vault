---
title: Handoff Programming Guide
apple_id: TP40014338
resource_type: Guide
platform: watchOS|iOS|macOS
topic: User Experience
technology: null
published: '2016-04-01'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Handoff/AdoptingHandoff/AdoptingHandoff.html
archived_at: '2026-07-18T02:11:28.715012Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Handoff Programming Guide](About%20Handoff.md)


[Next](Document%20Revision%20History.md)[Previous](About%20Handoff.md)

# Adopting Handoff

User activities can be shared among apps that are signed with the same developer team identifier and supporting a given activity type. If an app is document-based, it can opt to support Handoff automatically. Otherwise, apps must adopt a small API in Foundation, as described in this chapter.

The first step in implementing Handoff is to identify the types of user activities that your app supports. For example, an email app could support composing and reading messages as two separate user activities. A list-handling app could support creating (and editing) list items as one user activity type, and it could support browsing lists and items as another. Your app can support as many activity types as you wish, whatever users do in your app. For each activity type, your app needs to identify when an activity of that type begins and ends, and it needs to maintain up-to-date state data sufficient to enable the activity to continue on another device.

User activities can be shared among any apps signed with the same team identifier, and you don’t need a one-to-one mapping between originating and resuming apps. For example, one app creates three different types of activities, and those activities are resumed by three different apps on the second device. This asymmetry can be a common scenario, given the preference for iOS apps to be smaller and more focused on a dedicated purpose than more comprehensive Mac apps.

Document-based apps on iOS and OS X automatically support Handoff by automatically creating [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) objects for iCloud-based documents if the app’s `Info.plist` property list file includes a `CFBundleDocumentTypes` key of `NSUbiquitousDocumentUserActivityType`, as shown in Listing 2-1. The value of `NSUbiquitousDocumentUserActivityType` is a string used for the [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) object’s activity type. The activity type correlates with the app’s role for the given document type, such as editor or viewer, and an activity type can apply to multiple document types. In Listing 2-1 the string is a reverse-DNS app designator with the name of the activity, `editing`, appended. If they are represented in this way, the activity type entries do not need to be repeated in the `NSUserActivityTypes` array of the app’s `Info.plist`.

__Listing 2-1__  Info.plist entry for Handoff in document-based apps

```
<key>CFBundleDocumentTypes</key>
<array>
    <dict>
        <key>CFBundleTypeName</key>
        <string>NSRTFDPboardType</string>
        . . .
        <key>LSItemContentTypes</key>
        <array>
            <string>com.myCompany.rtfd</string>
        </array>
        . . .
        <key>NSUbiquitousDocumentUserActivityType</key>
        <string>com.myCompany.myEditor.editing</string>
    </dict>
</array>
```

The document's URL is put into the [userInfo](https://developer.apple.com/documentation/foundation/nsuseractivity/1411706-userinfo) dictionary with the `NSUserActivityDocumentURLKey`.

The automatically created user activity object is available through the document’s [userActivity](https://developer.apple.com/documentation/appkit/nsdocument/1526106-useractivity) property and can be referenced by other objects in the app, such as a view controller in iOS or window controller in OS X. This referencing enables apps to track position in a document, for example, or to track the selection of particular elements. The app sets the activity object’s [needsSave](https://developer.apple.com/documentation/foundation/nsuseractivity/1408791-needssave) property to `YES` whenever that state changes and saves the state in its [updateUserActivityState:](https://developer.apple.com/documentation/appkit/nsdocument/1529014-updateuseractivitystate) callback.

The [userActivity](https://developer.apple.com/documentation/appkit/nsdocument/1526106-useractivity) property can be used from any thread. It conforms to the key-value observing (KVO) protocol so that a [userActivity](https://developer.apple.com/documentation/appkit/nsdocument/1526106-useractivity) object can be shared with other objects that need to be kept in sync as the document moves into and out of iCloud. A document’s user activity objects are invalidated when the document is closed.

Adopting Handoff in your app requires you to write code that uses APIs in UIKit and AppKit provided for creating a user activity object, updating the state of the object to track the activity, and continuing the activity on another device.

Every user activity that can potentially be handed off to a continuing device or designated as searchable is represented by a user activity object instantiated from the [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) class. An originating app creates a user activity object for each user activity it supports. The nature of those user activities depends on the app. For example, a web browser might designate the user browsing a web page as one activity. The app creates an [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) instance, as shown in Listing 2-2, whenever the user opens a new window or tab displaying content from a URL, placing the URL in the activity object’s [userInfo](https://developer.apple.com/documentation/foundation/nsuseractivity/1411706-userinfo) dictionary, along with the scroll position of the page. Place this code in a controller object such as a window or view controller that has knowledge of the current state of the activity and that can update the state data in the activity object as necessary.

__Listing 2-2__  Creating the user activity object

```
NSUserActivity *myActivity = [[NSUserActivity alloc]
                      initWithActivityType: @"com.myCompany.myBrowser.browsing"];
myActivity.userInfo = @{ ... };
myActivity.title = @"Browsing";
```

To designate an activity as searchable, you can amend the code in Listing 2-2 to include code that provides more information about the activity and sets its eligibility, as shown in Listing 2-3.

__Listing 2-3__  Designating an activity as searchable

```
myActivity.keywords = [NSSet setWithArray:@[...]];

// Enable the activity to participate in search results.
myActivity.eligibleForSearch = YES;
```

After setting up an activity, set its state to current, as shown here:

```
[myActivity becomeCurrent];
```

When your app is finished with an [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) object, it should call [invalidate](https://developer.apple.com/documentation/foundation/nsuseractivity/1416401-invalidate) before deallocating the object. This makes the object disappear from all devices (if it was present) and frees up any system resources devoted to that user activity object.

The activity type identifier is a short string appearing in your app's `Info.plist` property list file in its `NSUserActivityTypes` array, which lists all the activity types your app supports. The same string is passed when you create the activity, as shown in [Listing 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dgmzyfvbuqmrnknltc) where the activity object is created with the activity type of `com.myCompany.myBrowser.browsing`, a reverse-DNS-style notation meant to avoid collisions. When the user chooses to continue the activity, the activity type (along with the app’s Team ID) determines which app to launch on the receiving device to continue the activity.

For example, a Reminders-style app serializes the reminder list the user is looking at. When the user clicks on a new reminder list, the app tracks that activity in the [NSUserActivityDelegate](https://developer.apple.com/documentation/foundation/nsuseractivitydelegate). Listing 2-4 shows a possible implementation of a method that gets called whenever the user switches to a different reminder list. This app appends an activity name to the app’s bundle identifier to create the activity type to use when it creates its [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) object.

__Listing 2-4__  Tracking a user activity

```
    // UIResponder and NSResponder have a userActivity property
    NSUserActivity *currentActivity = [self userActivity];

   // Build an activity type using the app's bundle identifier
    NSString *bundleName = [[NSBundle mainBundle] bundleIdentifier];
    NSString *myActivityType =
                    [bundleName stringByAppendingString:@".selected-list"];

    if(![[currentActivity activityType] isEqualToString:myActivityType]) {
        [currentActivity invalidate];

        currentActivity = [[NSUserActivity alloc]
                                      initWithActivityType:myActivityType];
        [currentActivity setDelegate:self];
        [currentActivity setNeedsSave:YES];

        [self setUserActivity:currentActivity];

    } else {

        // Already tracking user activity of this type
        [currentActivity setNeedsSave:YES];

    }
```

The code in Listing 2-4 uses the `setNeedsSave:` accessor method to mark the user activity object as needing to to be updated. This enables the system to coalesce updates and perform them lazily.

The activity object has a user info dictionary that contains whatever data is needed to hand off the activity to the continuing app. The user info dictionary can contain [NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray), [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData), [NSDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/cl/NSDate), [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary), [NSNull](https://developer.apple.com/documentation/foundation/nsnull), [NSNumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/cl/NSNumber), [NSSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSSet), [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString), and [NSURL](https://developer.apple.com/documentation/foundation/nsurl) objects. The system modifies [NSURL](https://developer.apple.com/documentation/foundation/nsurl) objects that use the `file:` scheme and point at iCloud documents to point to those same items in the corresponding container on the receiving device.

Listing 2-5 shows an example that creates a user activity object for an app that reads documents on a website. The activity type, set when the object is created, is shown in reverse-DNS-style notation that specifies the company, app, and finally the particular activity. The [webpageURL](https://developer.apple.com/documentation/foundation/nsuseractivity/1418086-webpageurl) property represents the URL where the document being read is located, and the user info dictionary is populated with keys and values representing the document’s name and the current page number and scroll position. As the reader progresses through a document, your app needs to keep that information current.

__Listing 2-5__  Initializing a user info dictionary

```
NSUserActivity* myActivity = [[NSUserActivity alloc]
                      initWithActivityType: @"com.myCompany.myReader.reading"];

// Initialize userInfo
NSURL* webpageURL = [NSURL URLWithString:@"http://www.myCompany.com"];
myActivity.userInfo = @{
             @"docName" : currentDoc,
             @"pageNumber" : self.pageNumber,
             @"scrollPosition" : self.scrollPosition
};
```


You can associate responder objects (inheriting from [NSResponder](https://developer.apple.com/documentation/appkit/nsresponder) on OS X or [UIResponder](https://developer.apple.com/documentation/uikit/uiresponder) on iOS) with a given user activity if you set the activity as the responder’s [userActivity](https://developer.apple.com/documentation/uikit/uiresponder/1621089-useractivity) property. The system automatically saves the [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) object at appropriate times, calling the responder’s [updateUserActivityState:](https://developer.apple.com/documentation/uikit/uiresponder/1621095-updateuseractivitystate) override to add current data to the user activity object using the activity object’s [addUserInfoEntriesFromDictionary:](https://developer.apple.com/documentation/foundation/nsuseractivity/1410066-adduserinfoentriesfromdictionary) method.

__Listing 2-6__  Responder override for updating an activity's state

```objc
- (void)updateUserActivityState:(NSUserActivity *)userActivity {
    . . .
    [userActivity setTitle: self.activityTitle];
    [userActivity addUserInfoEntriesFromDictionary: self.activityUserInfo];
}
```


Handoff automatically advertises user activities that are available to be continued on iOS and OS X devices that are in physical proximity to the originating device and signed into the same iCloud account as the originating device. When the user chooses to continue a given activity, Handoff launches the appropriate app and sends the app delegate messages that determine how the activity is resumed, as described in [Continuing an Activity Using the App Delegate](About%20Handoff.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dgmzyfvbuqmznknltm).

Implement the [application:willContinueUserActivityWithType:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622919-application) method to let the user know the activity will continue shortly. Use the the [application:continueUserActivity:restorationHandler:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623072-application) method to configure the app to continue the activity. The system calls this method when the activity object, including activity state data in its [userInfo](https://developer.apple.com/documentation/foundation/nsuseractivity/1411706-userinfo) dictionary, is available to the continuing app.

Additional configuration of your app for continuing the activity can optionally be performed by objects you give to the restoration handler block that is passed in with the [application:continueUserActivity:restorationHandler:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623072-application) message. Listing 2-7 shows a simple implementation of this method.

__Listing 2-7__  Continuing a user activity

```objc
- (BOOL)application:(NSApplication *)application
             continueUserActivity: (NSUserActivity *)userActivity
             restorationHandler: (void (^)(NSArray *))restorationHandler {

    BOOL handled = NO;

    // Extract the payload
    NSString *type = [userActivity activityType];
    NSString *title = [userActivity title];
    NSDictionary *userInfo = [userActivity userInfo];

    // Assume the app delegate has a text field to display the activity information
    [appDelegateTextField setStringValue: [NSString stringWithFormat:
        @"User activity is of type %@, has title %@, and user info %@",
        type, title, userInfo]];

    restorationHandler(self.windowControllers);
    handled = YES;

    return handled;
}
```

In this case, the app delegate has an array of [NSWindowController](https://developer.apple.com/documentation/appkit/nswindowcontroller) objects, `windowControllers`. These window controllers know how to configure all of the app’s windows to resume the activity. After you pass that array to the `restorationHandler` block, Handoff sends each of those objects a [restoreUserActivityState:](https://developer.apple.com/documentation/appkit/nsresponder/1526024-restoreuseractivitystate) message, passing in the resuming activity’s [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) object. The window controllers inherit the [restoreUserActivityState:](https://developer.apple.com/documentation/appkit/nsresponder/1526024-restoreuseractivitystate) method from [NSResponder](https://developer.apple.com/documentation/appkit/nsresponder), and each controller object overrides that method to configure its window, using the information in the activity object’s [userInfo](https://developer.apple.com/documentation/foundation/nsuseractivity/1411706-userinfo) dictionary.

To support graceful failure, the app delegate should implement the [application:didFailToContinueUserActivityWithType:error:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428613-application) method. If you don’t implement that method, the app framework nonetheless displays diagnostic information contained in the passed-in [NSError](https://developer.apple.com/documentation/foundation/nserror) object.

When using a native app on the originating device, the user may want to continue the activity on another device that does not have a corresponding native app. If there is a web page that corresponds to the activity, it can still be handed off. For example, video library apps enable users to browse movies available for viewing, and mail apps enable users to read and compose email, and in many cases users can do the same activity though a web-page interface. In this case, the native app knows the URL for the web interface, possibly including syntax designating a particular video being browsed or message being read. So, when the native app creates the [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) object, it sets the [webpageURL](https://developer.apple.com/documentation/foundation/nsuseractivity/1418086-webpageurl) property, and if the receiving device doesn't have an app that supports the user activity’s [activityType](https://developer.apple.com/documentation/foundation/nsuseractivity/1409611-activitytype), it can resume the activity in the default web-browser of the continuing platform.

A web browser on OS X that wants to continue an activity in this way should claim the `NSUserActivityTypeBrowsingWeb` activity type (by entering that string in its `NSUserActivityTypes` array in the app's `Info.plist` property list file). This ensures that if the user selects that browser as their default browser, it receives the activity object instead of Safari.

In the opposite case, if the user is using a web browser on the originating device, and the receiving device is an iOS device with a native app that claims the domain portion of the [webpageURL](https://developer.apple.com/documentation/foundation/nsuseractivity/1418086-webpageurl) property, then iOS launches the native app and sends it an [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) object with an [activityType](https://developer.apple.com/documentation/foundation/nsuseractivity/1409611-activitytype) value of `NSUserActivityTypeBrowsingWeb`. The [webpageURL](https://developer.apple.com/documentation/foundation/nsuseractivity/1418086-webpageurl) property contains the URL the user was visiting, while the [userInfo](https://developer.apple.com/documentation/foundation/nsuseractivity/1411706-userinfo) dictionary is empty.

The native app on the receiving device must opt into this behavior by claiming a domain in the `com.apple.developer.associated-domains` entitlement. The value of that entitlement has the format `<service>:<fully qualified domain name>`, for example, `activitycontinuation:example.com`. In this case the service must be `activitycontinuation`. To match all subdomains of an associated domain, you can specify a wildcard by prefixing `*.` before the beginning of a specific domain (the period is required). Add the value for the `com.apple.developer.associated-domains` entitlement in Xcode in the Associated Domains section under the Capabilities tab of the target settings. You specify should specify no more than about 20 to 30 domains.

If that domain matches the [webpageURL](https://developer.apple.com/documentation/foundation/nsuseractivity/1418086-webpageurl) property, Handoff downloads a list of approved app IDs from the domain. Domain-approved apps are authorized to continue the activity. On your website, you list the approved apps in a JSON file named `apple-app-site-association`, for example, `https://example.com/apple-app-site-association`. (You must use an actual device, rather than the simulator, to test downloading the JSON file.) Handoff first searches for the file in the `.well-known` subdirectory (for example, `https://example.com/.well-known/apple-app-site-association`), falling back to the top-level domain if you don’t use the `.well-known` subdirectory.

The JSON file contains a dictionary that specifies a list of app identifiers in the format `<team identifier>.<bundle identifier>` in the General tab of the target settings, for example, `YWBN8XTPBJ.com.example.myApp`. Listing 2-8 shows an example of such a JSON file formatted for reading.

__Listing 2-8__  Server-side web credentials

```json
{
    "activitycontinuation": {
    "apps": [    "YWBN8XTPBJ.com.example.myApp",
                 "YWBN8XTPBJ.com.example.myOtherApp" ]
    }
}
```

If your app runs in iOS 9 or later, the `apple-app-site-association` file may be a JSON file with a MIME type of `application/json`, and you don't need to sign it. If your app runs in iOS 8, the file must be CMS signed by a valid TLS certificate and have a MIME type of `application/pkcs7-mime`. To sign the JSON file, put the content into a text file and sign it. You can perform this task with Terminal commands such as those shown in Listing 2-9, removing the white space from the text for ease of manipulation, and using the `openssl` command with the certificate and key for an identity issued by a certificate authority trusted by iOS (that is, listed at [http://support.apple.com/kb/ht5012](http://support.apple.com/kb/ht5012)). It need not be the same identity hosting the web credentials ([https://example.com](https://example.com/) in the example listing), but it must be a valid TLS certificate for the domain name in question.

__Listing 2-9__  Signing the credentials file

```
echo '{"activitycontinuation":{"apps":["YWBN8XTPBJ.com.example.myApp",
"YWBN8XTPBJ.com.example.myOtherApp"]}}' > json.txt

cat json.txt | openssl smime -sign -inkey example.com.key
                             -signer example.com.pem
                             -certfile intermediate.pem
                             -noattr -nodetach
                             -outform DER > apple-app-site-association
```

The output of the `openssl` command is the JSON file that you put on your website at the `apple-app-site-association` URL, in this example, `https://example.com/apple-app-site-association`.

An app can set the [webpageURL](https://developer.apple.com/documentation/foundation/nsuseractivity/1418086-webpageurl) property to any web URL, but it only receives activity objects whose [webpageURL](https://developer.apple.com/documentation/foundation/nsuseractivity/1418086-webpageurl) domain is in its `com.apple.developer.associated-domains` entitlement. Also, the scheme of the [webpageURL](https://developer.apple.com/documentation/foundation/nsuseractivity/1418086-webpageurl) must be `http` or `https`. Any other scheme throws an exception.

If resuming an activity requires more data than can be efficiently transferred by the initial Handoff payload, a continuing app can call back to the originating app’s activity object to open streams between the apps and transfer more data. In this case, the originating app sets its [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) object’s Boolean property [supportsContinuationStreams](https://developer.apple.com/documentation/foundation/nsuseractivity/1409195-supportscontinuationstreams) to `YES`, sets the user activity delegate, then calls [becomeCurrent](https://developer.apple.com/documentation/foundation/nsuseractivity/1413665-becomecurrent), as shown in Listing 2-10.

__Listing 2-10__  Setting up streams

```
NSUserActivity* activity = [[NSUserActivity alloc] init];
activity.title = @"Editing Mail";
activity.supportsContinuationStreams = YES;
activity.delegate = self;
[activity becomeCurrent];
```

On the continuing device, after users indicate they want to resume the activity, the system launches the appropriate app and begins sending messages to the app delegate. The app delegate can then request streams back to the originating app by sending its user activity object the [getContinuationStreamsWithCompletionHandler:](https://developer.apple.com/documentation/foundation/nsuseractivity/1409931-getcontinuationstreams) message, as shown in the override implementation in Listing 2-11.

__Listing 2-11__  Requesting streams

```objc
- (BOOL)application:(UIApplication *)application
        continueUserActivity: (NSUserActivity *)userActivity
        restorationHandler: (void(^)(NSArray *restorableObjects))restorationHandler
{
    [userActivity getContinuationStreamsWithCompletionHandler:^(
                        NSInputStream *inputStream,
                        NSOutputStream *outputStream, NSError *error) {

        // Do something with the streams

        }];

    return YES;
}
```

On the originating device, the user activity delegate receives the streams in a callback to its [userActivity:didReceiveInputStream:outputStream:](https://developer.apple.com/documentation/foundation/nsuseractivitydelegate/1407386-useractivity) method, which it implements to provide the data needed to continue the user activity on the resuming device using the streams.

[NSInputStream](https://developer.apple.com/documentation/foundation/inputstream) provides read-only access to stream data, and [NSOutputStream](https://developer.apple.com/documentation/foundation/nsoutputstream) provides write-only access. Therefore, data written to the output stream on the originating side is read from the input stream on the continuing side, and vice versa. Streams are meant to be used in a request-and-response fashion; that is, the continuing side uses the streams to request more continuation data from the originating side which then uses the streams to provide the requested data.

Continuation streams are an optional feature of Handoff, and most user activities do not need them for successful continuation. Even when streams are needed, in most cases there should be minimal back and forth between the apps. A simple request from the continuing app accompanied by a response from the originating app should be enough for most continuation events.

Implementing successful continuation of activities requires careful design because numerous and various components, apps, software objects, and platforms can be involved.

- Transfer as small a payload as possible in the [userInfo](https://developer.apple.com/documentation/foundation/nsuseractivity/1411706-userinfo) dictionary—3KB or less. The more payload data you deliver, the longer it takes the activity to resume.
- When a large amount of data transfer is unavoidable, use streams, but recognize that they have a cost in terms of network setup and overhead.
- Plan for different versions of apps on different platforms to work well with each other or fail gracefully. Remember that the complementary app design can be asymmetrical—for example, a monolithic Mac app can route each of its activity types to smaller, special-purpose apps on iOS.
- Use reverse-DNS notation for your activity types to avoid collisions. If the activity pertains only to a single app, you can use the app identifier with an extra field appended to describe the activity type. For example, use a format such as `com.<company>.<app>.<activity type>`, as in `com.myCompany.myEditor.editing`. If you have a user activity that works across more than one app, you can drop the app field, as in `com.myCompany.editing`.
- To update the activity object’s [userInfo](https://developer.apple.com/documentation/foundation/nsuseractivity/1411706-userinfo) dictionary efficiently, configure its delegate and set its [needsSave](https://developer.apple.com/documentation/foundation/nsuseractivity/1408791-needssave) property to `YES` whenever the [userInfo](https://developer.apple.com/documentation/foundation/nsuseractivity/1411706-userinfo) needs updating. At appropriate times, Handoff invokes the delegate’s [userActivityWillSave:](https://developer.apple.com/documentation/foundation/nsuseractivitydelegate/1414848-useractivitywillsave) callback, and the delegate can update the activity state.
- Be sure the delegate of the continuing app implements its [application:willContinueUserActivityWithType:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622919-application) to let the user know the activity will be continued. The user activity object may not be available instantly.

In addition to these best practices, there are a few things you should do to ensure that users have a great search experience.

- When users tap a result, take them directly to the appropriate area in your app. As much as possible, avoid presenting intervening screens or experiences that delay users from reaching the content they’re interested in.
- Avoid over-indexing your app content or adding unrelated keywords and attributes in an attempt to improve the ranking of your results. Items that users don’t find useful are quickly identified and can eventually stop showing up in results.
- In general, provide a thumbnail image and a succinct title for each activity to enrich the search results.

If you also use Core Spotlight APIs to index user content in your app, use a unique ID to relate a user activity and an item. (To learn more about Core Spotlight APIs, see _[Core Spotlight Framework Reference](https://developer.apple.com/documentation/corespotlight)_.) For example:

```
// Create an attribute set that specifies a related unique ID for a Core Spotlight item.
CSSearchableItemAttributeSet *attributes = [[CSSearchableItemAttributeSet alloc] initWithItemContentType:@"public.image"];
attributes.relatedUniqueIdentifier = coreSpotlightUniqueIdentifier;

// Use the attribute set to create an NSUserActivity that's related to a Core Spotlight item.
NSUserActivity *myActivity = [[NSUserActivity alloc]
  initWithActivityType:@“com.mycompany.viewing-message”];
myActivity.contentAttributeSet = attributes;
```

[Next](Document%20Revision%20History.md)[Previous](About%20Handoff.md)

