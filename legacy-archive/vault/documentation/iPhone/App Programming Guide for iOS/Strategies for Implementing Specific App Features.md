---
title: App Programming Guide for iOS
apple_id: TP40007072
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/StrategiesforImplementingYourApp/StrategiesforImplementingYourApp.html
archived_at: '2026-07-27T06:57:07.055813Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Programming Guide for iOS](About%20iOS%20App%20Architecture.md)


[Next](Inter-App%20Communication.md)[Previous](Strategies%20for%20Handling%20App%20State%20Transitions.md)

# Strategies for Implementing Specific App Features

Different apps have different needs but some behaviors are common to many types of app. The following sections provide guidance about how to implement specific types of features in your app.

## Privacy Strategies

Protecting a user’s privacy is an important consideration in the design of an app. Privacy protection includes protecting the user’s data, including the user’s identity and personal information. The system frameworks already provide privacy controls for managing data such as contacts but your app should take steps to protect the data that you use locally.

### Protecting Data Using On-Disk Encryption

Data protection uses built-in hardware to store files in an encrypted format on disk and to decrypt them on demand. While the user’s device is locked, protected files are inaccessible, even to the app that created them. The user must unlock the device (by entering the appropriate passcode) before an app can access one of its protected files.

Data protection is available on most iOS devices and is subject to the following requirements:

- The file system on the user’s device must support data protection. Most devices support this behavior.
- The user must have an active passcode lock set for the device.

To protect a file, you add an attribute to the file indicating the desired level of protection. Add this attribute using either the `NSData` class or the `NSFileManager` class. When writing new files, you can use the [writeToFile:options:error:](https://developer.apple.com/documentation/foundation/nsdata/1414800-writetofile) method of `NSData` with the appropriate protection value as one of the write options. For existing files, you can use the [setAttributes:ofItemAtPath:error:](https://developer.apple.com/documentation/foundation/nsfilemanager/1413667-setattributes) method of `NSFileManager` to set or change the value of the [NSFileProtectionKey](https://developer.apple.com/documentation/foundation/fileattributekey/1616632-protectionkey). When using these methods, specify one of the following protection levels for the file:

- No protection—The file is encrypted but is not protected by the passcode and is available when the device is locked. Specify the [NSDataWritingFileProtectionNone](https://developer.apple.com/documentation/foundation/nsdata/writingoptions/1616757-nofileprotection) option (`NSData`) or the [NSFileProtectionNone](https://developer.apple.com/documentation/foundation/nsfileprotectionnone) attribute (`NSFileManager`).
- Complete—The file is encrypted and inaccessible while the device is locked. Specify the [NSDataWritingFileProtectionComplete](https://developer.apple.com/documentation/foundation/nsdatawritingoptions/nsdatawritingfileprotectioncomplete) option (`NSData`) or the [NSFileProtectionComplete](https://developer.apple.com/documentation/foundation/nsfileprotectioncomplete) attribute (`NSFileManager`).
- Complete unless already open—The file is encrypted. A closed file is inaccessible while the device is locked. After the user unlocks the device, your app can open the file and use it. If the user locks the device while the file is open, though, your app can continue to access it. Specify the [NSDataWritingFileProtectionCompleteUnlessOpen](https://developer.apple.com/documentation/foundation/nsdatawritingoptions/nsdatawritingfileprotectioncompleteunlessopen) option (`NSData`) or the [NSFileProtectionCompleteUnlessOpen](https://developer.apple.com/documentation/foundation/nsfileprotectioncompleteunlessopen) attribute (`NSFileManager`).
- Complete until first login—The file is encrypted and inaccessible until after the device has booted and the user has unlocked it once. Specify the [NSDataWritingFileProtectionCompleteUntilFirstUserAuthentication](https://developer.apple.com/documentation/foundation/nsdata/writingoptions/1617028-completefileprotectionuntilfirst) option (`NSData`) or the [NSFileProtectionCompleteUntilFirstUserAuthentication](https://developer.apple.com/documentation/foundation/fileprotectiontype/1616633-completeuntilfirstuserauthentica) attribute (`NSFileManager`).

If you protect a file, your app must be prepared to lose access to that file. When complete file protection is enabled, your app loses the ability to read and write the file’s contents when the user locks the device. You can track changes to the state of protected files using one of the following techniques:

- The app delegate can implement the [applicationProtectedDataWillBecomeUnavailable:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623019-applicationprotecteddatawillbeco) and [applicationProtectedDataDidBecomeAvailable:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623044-applicationprotecteddatadidbecom) methods.
- Any object can register for the [UIApplicationProtectedDataWillBecomeUnavailable](https://developer.apple.com/documentation/uikit/uiapplicationprotecteddatawillbecomeunavailable) and [UIApplicationProtectedDataDidBecomeAvailable](https://developer.apple.com/documentation/uikit/uiapplication/1623039-protecteddatadidbecomeavailablen) notifications.
- Any object can check the value of the [protectedDataAvailable](https://developer.apple.com/documentation/uikit/uiapplication/1622925-protecteddataavailable) property of the shared `UIApplication` object to determine whether files are currently accessible.

For new files, it is recommended that you enable data protection before writing any data to them. If you are using the `writeToFile:options:error:` method to write the contents of an [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) object to disk, this happens automatically. For existing files, adding data protection replaces an unprotected file with a new protected version.

### Identifying Unique Users of Your App

You should identify a user of your app only when doing so offers a clear benefit to that user. In cases where you only need to differentiate one user of your app from another, iOS provides identifiers that can help you do that. However, if you need a higher level of security, you might need to do more work on your own. For example, an app that provides financial services would likely want to prompt the user for login credentials to ensure that the user is authorized to access a specific account.

__Important:__ When identifying a user, always be transparent about what you intend to do with any information you obtain. It is not acceptable to identify a user so that you can track them surreptitiously.

Here are some common scenarios that might require you to identify a user, along with solutions for how to implement them.

- __You want to link a user to a specific account on your server.__ Include a login screen that requires the user to enter their account information securely. Always protect the account information you gather from the user by storing it in an encrypted form.
- __You want to differentiate instances of your app running on different devices.__ Use the [identifierForVendor](https://developer.apple.com/documentation/uikit/uidevice/1620059-identifierforvendor) property of the `UIDevice` class to obtain an ID that differentiates a user on one device from users on other devices. This technique does now allow you to identify specific users. A single user can have multiple devices, each with a different ID value.
- __You want to identify a user for the purposes of advertising.__ Use the [advertisingIdentifier](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614151-advertisingidentifier) property of the `ASIdentifierManager` class to obtain an ID for the user.

Because users are allowed to run apps on all of their iOS devices, Apple does not provide a way to identify the same user on multiple devices. If you need to identify a specific user, you must provide your own solution using universally unique IDs (UUIDs), a login account, or some other type of identification system.

## Respecting Restrictions

Users can set restrictions that specify the ratings of media they want to consume in apps. If your app plays media or modifies its behavior based on restrictions, you need to determine the current settings and respond when the settings change.

To get the current settings, get the shared [standardUserDefaults](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/clm/NSUserDefaults/standardUserDefaults) object and use the [objectForKey:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/objectForKey:) method to view the values for the following keys:

Media rating keyValue

com.apple.content-rating.ExplicitBooksAllowed

`Boolean`. If the value of this key is `NO`, explicit books are not allowed

com.apple.content-rating.ExplicitMusicPodcastsAllowed

`Boolean`. If the value of this key is `NO`, explicit music, movies, and podcasts are not allowed.

com.apple.content-rating.AppRating

`NSNumber`. The value of this key ranges from 0 to 1000. An app whose rating is higher than the current key value is not allowed.

com.apple.content-rating.MovieRating

`NSNumber`. The value of this key ranges from 0 to 1000. A movie whose rating is higher than the current key value is not allowed.

com.apple.content-rating.TVShowRating

`NSNumber`. The value of this key ranges from 0 to 1000. A TV show whose rating is higher than the current key value is not allowed.

__Note:__ If `objectForKey:` returns `nil` for a specific key, it means that information about this particular restriction is not available. In this case, your app can use its own policies to determine appropriate ratings.

To detect when the user makes a change to a restriction, register for the notification [NSUserDefaultsDidChangeNotification](https://developer.apple.com/documentation/foundation/userdefaults/1408206-didchangenotification). The shared `standardUserDefaults` object sends this notification to your app when it detects a change to a preference located in one of the persistent domains.

App ratings are defined for the `us` country code and are universally applied. Table 5-1 shows the value associated with each US app rating.

__Table 5-1__  App ratings

| Rating name | Numerical value |
| 4+ | 100 |
| 9+ | 200 |
| 12+ | 300 |
| 17+ | 600 |

Movie and TV ratings vary by country. If a country or region doesn’t specify a rating system for movies or TV shows, your app should use its own policies to determine appropriate ratings. Although most regions define movie ratings, only a few define TV show ratings.

A region can define several rating levels, each of which is associated with a name that describes the rating and a number in the range of 0 to 1000. For example, the US uses the string “G” and the number 100 to specify the lowest movie rating level.

Even if your app doesn’t play media, you might want to map your own rating system to a movie or TV show rating system. For example, a game might enable certain features only when the US movie rating “R” is allowed. To view the current list of ratings, download this document’s companion file (the link is near the top of the page).

## Supporting Multiple Versions of iOS

An app that supports the latest version of iOS plus one or more earlier versions must use runtime checks to prevent the use of newer APIs on older versions of iOS. Runtime checks prevent your app from crashing when it tries to use a feature that is not available on the current operating system.

There are several types of checks that you can make:

- To determine whether a class exists, see if its `Class` object is `nil`. The linker returns `nil` for any unknown class objects, making it possible to use a conditional check similar to the following:

  ```
  if ([UIPrintInteractionController class]) {
     // Create an instance of the class and use it.
  }
  else {
     // The print interaction controller is not available so use an alternative technique.
  }
  ```
- To determine whether a method is available on an existing class, use the [instancesRespondToSelector:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/instancesRespondToSelector:) class method or the [respondsToSelector:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/respondsToSelector:) instance method.
- To determine whether a C-based function is available, perform a Boolean comparison of the function name to `NULL`. If the symbol is not `NULL`, you can call the function. For example:

  ```
  if (UIGraphicsBeginPDFPage != NULL) {
      UIGraphicsBeginPDFPage();
  }
  ```

For more information and examples of how to write code that supports multiple deployment targets, see _[SDK Compatibility Guide](../../Developer%20Tools/SDK%20Compatibility%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dg2i)_.

## Preserving Your App’s Visual Appearance Across Launches

Even if your app supports background execution, it cannot run forever. At some point, the system might need to terminate your app to free up memory for the current foreground app. However, the user should never have to care if an app is already running or was terminated. From the user’s perspective, quitting an app should just seem like a temporary interruption. When the user returns to an app, that app should always return the user to the last point of use, so that the user can continue with whatever task was in progress. This behavior provides a better experience for the user and with the state restoration support built in to UIKit is relatively easy to achieve.

The state preservation system in UIKit provides a simple but flexible infrastructure for preserving and restoring the state of your app’s view controllers and views. The job of the infrastructure is to drive the preservation and restoration processes at the appropriate times. To do that, UIKit needs help from your app. Only you understand the content of your app, and so only you can write the code needed to save and restore that content. And when you update your app’s UI, only you know how to map older preserved content to the newer objects in your interface.

There are three places where you have to think about state preservation in your app:

- Your app delegate object, which manages the app’s top-level state
- Your app’s view controller objects, which manage the overall state for your app’s user interface
- Your app’s custom views, which might have some custom data that needs to be preserved

UIKit allows you to choose which parts of your user interface you want to preserve. And if you already have custom code for handling state preservation, you can continue to use that code and migrate portions to the UIKit state preservation system as needed.

### Enabling State Preservation and Restoration in Your App

State preservation and restoration is not an automatic feature and apps must opt-in to use it. Apps indicate their support for the feature by implementing the following methods in their app delegate:

- [application:shouldSaveApplicationState:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623089-application)
- [application:shouldRestoreApplicationState:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622987-application)

Normally, your implementations of these methods just return `YES` to indicate that state preservation and restoration can occur. However, apps that want to preserve and restore their state conditionally can return `NO` in situations where the operations should not occur. For example, after releasing an update to your app, you might want to return `NO` from your [application:shouldRestoreApplicationState:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622987-application) method if your app is unable to usefully restore the state from a previous version.

### The Preservation and Restoration Process

State preservation and restoration is an opt-in feature and works with the help of your app. Your app identifies objects that should be preserved and UIKit does the work of preserving and restoring those objects at appropriate times. Because UIKit handles so much of the process, it helps to understand what it does behind the scenes so that you know how your custom code fits into the overall scheme.

When thinking about state preservation and restoration, it helps to separate the two processes first. UIKit preserves your app’s state at appropriate times, such as when your app moves from the foreground to the background. When UIKit determines new state information is needed, it looks at your app’s views and view controllers to see which ones should be preserved. For each of those objects, UIKit writes preservation-related data to an encrypted on-disk file. The next time your app launches from scratch, UIKit looks for that file and, if it is present, uses it to try and restore your app’s state. Because the file is encrypted, state preservation and restoration only happens when the device is unlocked.

During the restoration process, UIKit uses the preserved data to reconstitute your interface but the creation of actual objects is handled by your code. Because your app might load objects from a storyboard file automatically, only your code knows which objects need to be created and which might already exist and can simply be returned. After creating each object, UIKit initializes them with the preserved state information.

During the preservation and restoration process, your app has a handful of responsibilities.

- During preservation, your app is responsible for:

  - Telling UIKit that it supports state preservation.
  - Telling UIKit which view controllers and views should be preserved.
  - Encoding relevant data for any preserved objects.
- During restoration, your app is responsible for:

  - Telling UIKit that it supports state restoration.
  - Providing (or creating) the objects that are requested by UIKit.
  - Decoding the state of your preserved objects and using it to return the object to its previous state.

Of your app’s responsibilities, the most significant are telling UIKit which objects to preserve and providing those objects during subsequent launches. Those two behaviors are where you should spend most of your time when designing your app’s preservation and restoration code. They are also where you have the most control over the actual process. To understand why that is the case, it helps to look at an example.

Figure 5-1 shows the view controller hierarchy of a tab bar interface after the user has interacted with several of the tabs. As you can see, some of the view controllers are loaded automatically as part of the app’s main storyboard file but some of the view controllers were presented or pushed onto the view controllers in different tabs. Without state restoration, only the view controllers from the main storyboard file would be restored during subsequent launches. By adding support for state restoration to your app, you can preserve all of the view controllers.

__Figure 5-1__  A sample view controller hierarchy

（原归档配图获取待重试：`state_vc_hierarchy_initial_2x.png`）

UIKit preserves only those objects that have an assigned restoration identifier. A _restoration identifier_ is a string that identifies the view or view controller to UIKit and your app. The value of this string is significant only to your code but the presence of this string tells UIKit that it needs to preserve the tagged object. During the preservation process, UIKit walks your app’s view controller hierarchy and preserves all objects that have a restoration identifier. If a view controller does not have a restoration identifier, that view controller and all of its views and child view controllers are not preserved. Figure 5-2 shows an updated version of the previous view hierarchy, now with restoration identifies applied to most (but not all) of the view controllers.

__Figure 5-2__  Adding restoration identifies to view controllers

（原归档配图未能恢复：`state_vc_hierarchy_preserve_2x.png`）

Depending on your app, it might or might not make sense to preserve every view controller. If a view controller presents transitory information, you might not want to return to that same point on restore, opting instead to return the user to a more stable point in your interface.

For each view controller you choose to preserve, you also need to decide how you want to restore it later. UIKit offers two ways to recreate objects. You can let your app delegate recreate it or you can assign a restoration class to the view controller and let that class recreate it. A _restoration class_ implements the [UIViewControllerRestoration](https://developer.apple.com/documentation/uikit/uiviewcontrollerrestoration) protocol and is responsible for finding or creating a designated object at restore time. Here are some tips for when to use each one:

- __If the view controller is always loaded from your app’s main storyboard file at launch time, do not assign a restoration class.__ Instead, let your app delegate find the object or take advantage of UIKit’s support for implicitly finding restored objects.
- __For view controllers that are not loaded from your main storyboard file at launch time, assign a restoration class.__ The simplest option is to make each view controller its own restoration class.

During the preservation process, UIKit identifies the objects to save and writes each affected object’s state to disk. Each view controller object is given a chance to write out any data it wants to save. For example, a tab view controller saves the identity of the selected tab. UIKit also saves information such as the view controller’s restoration class to disk. And if any of the view controller’s views has a restoration identifier, UIKit asks them to save their state information too.

The next time the app is launched, UIKit loads the app’s main storyboard or nib file as usual, calls the app delegate’s [application:willFinishLaunchingWithOptions:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623032-application) method, and then tries to restore the app’s previous state. The first thing it does is ask your app to provide the set of view controller objects that match the ones that were preserved. If a given view controller had an assigned restoration class, that class is asked to provide the object; otherwise, the app delegate is asked to provide it.

#### Flow of the Preservation Process

Figure 5-3 shows the high-level events that happen during state preservation and shows how the objects of your app are affected. Before preservation even occurs, UIKit asks your app delegate if it _should_ occur by calling the [application:shouldSaveApplicationState:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623089-application) method. If that method returns `YES`, UIKit begins gathering and encoding your app’s views and view controllers. When it is finished, it writes the encoded data to disk.

__Figure 5-3__  High-level flow interface preservation

（原归档配图未能恢复：`save_process_simple_2x.png`）

The next time your app launches, the system automatically looks for a preserved state file, and if present, uses it to restore your interface. Because this state information is only relevant between the previous and current launch cycles of your app, the file is typically discarded after your app finishes launching. The file is also discarded any time there is an error restoring your app. For example, if your app crashes during the restoration process, the system automatically throws away the state information during the next launch cycle to avoid another crash.

#### Flow of the Restoration Process

Figure 5-4 shows the high-level events that happen during state restoration and shows how the objects of your app are affected. After the standard initialization and UI loading is complete, UIKit asks your app delegate if state restoration should occur at all by calling the [application:shouldRestoreApplicationState:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622987-application) method. This is your app delegate’s opportunity to examine the preserved data and determine if state restoration is possible. If it is, UIKit uses the app delegate and restoration classes to obtain references to your app’s view controllers. Each object is then provided with the data it needs to restore itself to its previous state.

__Figure 5-4__  High-level flow for restoring your user interface

（原归档配图未能恢复：`restoration_process_simple_2x.png`）

Although UIKit helps restore the individual view controllers, it does not automatically restore the relationships between those view controllers. Instead, each view controller is responsible for encoding enough state information to return itself to its previous state. For example, a navigation controller encodes information about the order of the view controllers on its navigation stack. It then uses this information later to return those view controllers to their previous positions on the stack. Other view controllers that have embedded child view controllers are similarly responsible for encoding any information they need to restore their children later.

__Note:__ Not all view controllers need to encode their child view controllers. For example, tab bar controllers do not encode information about their child view controllers. Instead, it is assumed that your app follows the usual pattern of creating the appropriate child view controllers prior to creating the tab bar controller itself.

Because you are responsible for recreating your app’s view controllers, you have some flexibility to change your interface during the restoration process. For example, you could reorder the tabs in a tab bar controller and still use the preserved data to return each tab to its previous state. Of course, if you make dramatic changes to your view controller hierarchy, such as during an app update, you might not be able to use the preserved data.

### What Happens When You Exclude Groups of View Controllers?

When the restoration identifier of a view controller is `nil`, that view controller and any child view controllers it manages are not preserved automatically. For example, in Figure 5-5, because a navigation controller did not have a restoration identifier, it and all of its child view controllers and views are omitted from the preserved data.

__Figure 5-5__  Excluding view controllers from the automatic preservation process

（原归档配图未能恢复：`state_vc_caveats_2x.png`）

Even if you decide not to preserve view controllers, that does not mean all of those view controllers disappear from the view hierarchy altogether. At launch time, your app might still create the view controllers as part of its default setup. For example, if any view controllers are loaded automatically from your app’s storyboard file, they would still appear, albeit in their default configuration, as shown in Figure 5-6.

__Figure 5-6__  Loading the default set of view controllers

（原归档配图未能恢复：`state_vc_caveats_2_2x.png`）

Something else to realize is that even if a view controller is not preserved automatically, you can still encode a reference to that view controller and preserve it manually. In [Figure 5-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanzsfvbuqnjnknltgna), the three child view controllers of the first navigation controller have restoration identifiers, even though there parent navigation controller does not. If your app delegate (or any preserved object) encodes a reference to those view controllers, their state is preserved. Even though their order in the navigation controller is not saved, you could still use those references to recreate the view controllers and install them in the navigation controller during subsequent launch cycles.

### Checklist for Implementing State Preservation and Restoration

Supporting state preservation and restoration requires modifying your app delegate and view controller objects to encode and decode the state information. If your app has any custom views that also have preservable state information, you need to modify those objects too.

When adding state preservation and restoration to your code, use the following list to remind you of the code you need to write.

- (Required) Implement the [application:shouldSaveApplicationState:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623089-application) and [application:shouldRestoreApplicationState:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622987-application) methods in your app delegate; see [Enabling State Preservation and Restoration in Your App](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanzsfvbuqnjnknltgmy).
- (Required) Assign restoration identifiers to each view controller you want to preserve by assigning a non empty string to their [restorationIdentifier](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621499-restorationidentifier) property; see [Marking Your View Controllers for Preservation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanzsfvbuqnjnknlteoi).

  If you want to save the state of specific views too, assign non empty strings to their [restorationIdentifier](https://developer.apple.com/documentation/uikit/uiview/1622494-restorationidentifier) properties; see [Preserving the State of Your Views](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanzsfvbuqnjnknltgmq).
- (Required) Show your app’s window from the [application:willFinishLaunchingWithOptions:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623032-application) method of your app delegate. The state restoration machinery needs the window so that it can restore scroll positions and other relevant bits of your app’s interface.
- Assign restoration classes to the appropriate view controllers. (If you do not do this, your app delegate is asked to provide the corresponding view controller at restore time.) See [Restoring Your View Controllers at Launch Time](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanzsfvbuqnjnknltenq).
- (Recommended) Encode and decode the state of your views and view controllers using the [encodeRestorableStateWithCoder:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621461-encoderestorablestatewithcoder) and [decodeRestorableStateWithCoder:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621429-decoderestorablestatewithcoder) methods of those objects; see [Encoding and Decoding Your View Controller’s State](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanzsfvbuqnjnknlteny).
- Encode and decode any version information or additional state information for your app using the [application:willEncodeRestorableStateWithCoder:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623099-application) and [application:didDecodeRestorableStateWithCoder:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623006-application) methods of your app delegate; see [Preserving Your App’s High-Level State](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanzsfvbuqnjnknltgmi).
- Objects that act as data sources for table views and collection views should implement the [UIDataSourceModelAssociation](https://developer.apple.com/documentation/uikit/uidatasourcemodelassociation) protocol. Although not required, this protocol helps preserve the selected and visible items in those types of views. See [Implementing Preservation-Friendly Data Sources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanzsfvbuqnjnknltgma).

### Enabling State Preservation and Restoration in Your App

State preservation and restoration is not an automatic feature and apps must opt-in to use it. Apps indicate their support for the feature by implementing the following methods in their app delegate:

- [application:shouldSaveApplicationState:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623089-application)
- [application:shouldRestoreApplicationState:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622987-application)

Normally, your implementations of these methods just return `YES` to indicate that state preservation and restoration can occur. However, apps that want to preserve and restore their state conditionally can return `NO` in situations where the operations should not occur. For example, after releasing an update to your app, you might want to return `NO` from your [application:shouldRestoreApplicationState:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622987-application) method if your app is unable to usefully restore the state from a previous version.

### Preserving the State of Your View Controllers

Preserving the state of your app’s view controllers should be your main goal. View controllers define the structure of your user interface. They manage the views needed to present that interface and they coordinate the getting and setting of the data that backs those views. To preserve the state of a single view controller, you must do the following:

- (Required) Assign a restoration identifier to the view controller; see [Marking Your View Controllers for Preservation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanzsfvbuqnjnknlteoi).
- (Required) Provide code to create or locate new view controller objects at launch time; see [Restoring Your View Controllers at Launch Time](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanzsfvbuqnjnknltenq).
- (Optional) Implement the [encodeRestorableStateWithCoder:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621461-encoderestorablestatewithcoder) and [decodeRestorableStateWithCoder:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621429-decoderestorablestatewithcoder) methods to encode and restore any state information that cannot be recreated during a subsequent launch; see [Encoding and Decoding Your View Controller’s State](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanzsfvbuqnjnknlteny).

#### Marking Your View Controllers for Preservation

UIKit preserves only those view controllers whose [restorationIdentifier](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621499-restorationidentifier) property contains a valid string object. For view controllers that you know you want to preserve, set the value of this property when you initialize the view controller object. If you load the view controller from a storyboard or nib file, you can set the restoration identifier there.

Choosing an appropriate value for restoration identifiers is important. During the restoration process, your code uses the restoration identifier to determine which view controller to retrieve or create. If every view controller object is based on a different class, you can use the class name for the restoration identifier. However, if your view controller hierarchy contains multiple instances of the same class, you might need to choose different names based on each view usage.

When it asks you to provide a view controller, UIKit provides you with the restoration path of the view controller object. A _restoration path_ is the sequence of restoration identifiers starting at the root view controller and walking down the view controller hierarchy to the current object. For example, imagine you have a tab bar controller whose restoration identifier is `TabBarControllerID`, and the first tab contains a navigation controller whose identifier is `NavControllerID` and whose root view controller’s identifier is `MyViewController`. The full restoration path for the root view controller would be `TabBarControllerID/NavControllerID/MyViewController`.

The restoration path for every object must be unique. If a view controller has two child view controllers, each child must have a different restoration identifier. However, two view controllers with different parent objects may use the same restoration identifier because the rest of the restoration path provides the needed uniqueness. Some UIKit view controllers, such as navigation controllers, automatically disambiguate their child view controllers, allowing you to use the same restoration identifiers for each child. For more information about the behavior of a given view controller, see the corresponding class reference.

At restore time, you use the provided restoration path to determine which view controller to return to UIKit. For more information on how you use restoration identifiers and restoration paths to restore view controllers, see [Restoring Your View Controllers at Launch Time](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanzsfvbuqnjnknltenq).

#### Restoring Your View Controllers at Launch Time

During the restoration process, UIKit asks your app to create (or locate) the view controller objects that comprise your preserved user interface. UIKit adheres to the following process when trying to locate view controllers:

1. __If the view controller had a restoration class, UIKit asks that class to provide the view controller.__ UIKit calls the [viewControllerWithRestorationIdentifierPath:coder:](https://developer.apple.com/documentation/uikit/uiviewcontrollerrestoration/1616859-viewcontroller) method of the associated restoration class to retrieve the view controller. If that method returns `nil`, it is assumed that the app does not want to recreate the view controller and UIKit stops looking for it.
2. __If the view controller did not have a restoration class, UIKit asks the app delegate to provide the view controller.__ UIKit calls the [application:viewControllerWithRestorationIdentifierPath:coder:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623062-application) method of your app delegate to look for view controllers without a restoration class. If that method returns `nil`, UIKit tries to find the view controller implicitly.
3. __If a view controller with the correct restoration path already exists, UIKit uses that object.__ If your app creates view controllers at launch time (either programmatically or by loading them from a resource file) and assigns restoration identifiers to them, UIKit finds them implicitly through their restoration paths.
4. __If the view controller was originally loaded from a storyboard file, UIKit uses the saved storyboard information to locate and create it.__ UIKit saves information about a view controller’s storyboard inside the restoration archive. At restore time, it uses that information to locate the same storyboard file and instantiate the corresponding view controller if the view controller was not found by any other means.

It is worth noting that if you specify a restoration class for a view controller, UIKit does not try to find your view controller implicitly. If the `viewControllerWithRestorationIdentifierPath:coder:` method of your restoration class returns `nil`, UIKit stops trying to locate your view controller. This gives you control over whether you really want to create the view controller. If you do not specify a restoration class, UIKit does everything it can to find the view controller for you, creating it as necessary from your app’s storyboard files.

If you choose to use a restoration class, the implementation of your `viewControllerWithRestorationIdentifierPath:coder:` method should create a new instance of the class, perform some minimal initialization, and return the resulting object. Listing 5-1 shows an example of how you might use this method to load a view controller from a storyboard. Because the view controller was originally loaded from a storyboard, this method uses the [UIStateRestorationViewControllerStoryboardKey](https://developer.apple.com/documentation/uikit/uiapplication/1616861-staterestorationviewcontrollerst) key to get the storyboard from the archive. Note that this method does not try to configure the view controller’s data fields. That step occurs later when the view controller’s state is decoded.

__Listing 5-1__  Creating a new view controller during restoration

```objc
+ (UIViewController*) viewControllerWithRestorationIdentifierPath:(NSArray *)identifierComponents
                      coder:(NSCoder *)coder {
   MyViewController* vc;
   UIStoryboard* sb = [coder decodeObjectForKey:UIStateRestorationViewControllerStoryboardKey];
   if (sb) {
      vc = (PushViewController*)[sb instantiateViewControllerWithIdentifier:@"MyViewController"];
      vc.restorationIdentifier = [identifierComponents lastObject];
      vc.restorationClass = [MyViewController class];
   }
    return vc;
}
```

Reassigning the restoration identifier and restoration class, as in the preceding example, is a good habit to adopt when creating new view controllers. The simplest way to restore the restoration identifier is to grab the last item in the `identifierComponents` array and assign it to your view controller.

For objects that were already loaded from your app’s main storyboard file at launch time, do not create a new instance of each object. Instead, implement the `application:viewControllerWithRestorationIdentifierPath:coder:` method of your app delegate and use it to return the appropriate objects or let UIKit find those objects implicitly.

#### Encoding and Decoding Your View Controller’s State

For each object slated for preservation, UIKit calls the object’s [encodeRestorableStateWithCoder:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621461-encoderestorablestatewithcoder) method to give it a chance to save its state. During the decode process, a matching call to the [decodeRestorableStateWithCoder:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621429-decoderestorablestatewithcoder) method is made to decode that state and apply it to the object. The implementation of these methods is optional, but recommended, for your view controllers. You can use them to save and restore the following types of information:

- References to any data being displayed (not the data itself)
- For a container view controller, references to its child view controllers
- Information about the current selection
- For view controllers with a user-configurable view, information about the current configuration of that view.

In your encode and decode methods, you can encode any values supported by the coder, including other objects. For all objects except views and view controllers, the object must adopt the [NSCoding](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSCoding/Description.html#//apple_ref/occ/intf/NSCoding) protocol and use the methods of that protocol to write its state. For views and view controllers, the coder does not use the methods of the `NSCoding` protocol to save the object’s state. Instead, the coder saves the restoration identifier of the object and adds it to the list of preservable objects, which results in that object’s `encodeRestorableStateWithCoder:` method being called.

The `encodeRestorableStateWithCoder:` and `decodeRestorableStateWithCoder:` methods of your view controllers should always call `super` at some point in their implementation. Calling `super` gives the parent class a chance to save and restore any additional information. Listing 5-2 shows a sample implementation of these methods that save a numerical value used to identify the specified view controller.

__Listing 5-2__  Encoding and decoding a view controller’s state.

```objc
- (void)encodeRestorableStateWithCoder:(NSCoder *)coder {
   [super encodeRestorableStateWithCoder:coder];

   [coder encodeInt:self.number forKey:MyViewControllerNumber];
}

- (void)decodeRestorableStateWithCoder:(NSCoder *)coder {
   [super decodeRestorableStateWithCoder:coder];

   self.number = [coder decodeIntForKey:MyViewControllerNumber];
}
```

Coder objects are not shared during the encode and decode process. Each object with preservable state receives its own coder that it can use to read or write data. The use of unique coders means that you do not have to worry about key namespace collisions among your own objects. However, you must still avoid using some special key names that UIKit provides. Specifically, each coder contains the [UIApplicationStateRestorationBundleVersionKey](https://developer.apple.com/documentation/uikit/uiapplication/1616852-staterestorationbundleversionkey) and [UIApplicationStateRestorationUserInterfaceIdiomKey](https://developer.apple.com/documentation/uikit/uiapplication/1616853-staterestorationuserinterfaceidi) keys, which provide information about the bundle version and current user interface idiom. Coders associated with view controllers may also contain the [UIStateRestorationViewControllerStoryboardKey](https://developer.apple.com/documentation/uikit/uiapplication/1616861-staterestorationviewcontrollerst) key, which identifies the storyboard from which that view controller originated.

For more information about implementing your encode and decode methods for your view controllers, see _[UIViewController Class Reference](https://developer.apple.com/documentation/uikit/uiviewcontroller)_.

### Preserving the State of Your Views

If a view has state information worth preserving, you can save that state with the rest of your app’s view controllers. Because they are usually configured by their owning view controller, most views do not need to save state information. The only time you need to save a view’s state is when the view itself can be altered by the user in a way that is independent of its data or the owning view controller. For example, scroll views save the current scroll position, which is information that is not interesting to the view controller but which does affect how the view presents itself.

To designate that a view’s state should be saved, you do the following:

- Assign a valid string to the view’s [restorationIdentifier](https://developer.apple.com/documentation/uikit/uiview/1622494-restorationidentifier) property.
- Use the view from a view controller that also has a valid restoration identifier.
- For table views and collection views, assign a data source that adopts the [UIDataSourceModelAssociation](https://developer.apple.com/documentation/uikit/uidatasourcemodelassociation) protocol.

As with view controllers, assigning a restoration identifier to a view tells the system that the view object has state that your app wants to save. The restoration identifier can also be used to locate the view later.

Like view controllers, views define methods for encoding and decoding their custom state. If you create a view with state worth saving, you can use these methods to read and write any relevant data.

#### UIKit Views with Preservable State

In order to save the state of any view, including both custom and standard system views, you must assign a restoration identifier to the view. Views without a restoration identifier are not added to the list of preservable objects by UIKit.

The following UIKit views have state information that can be preserved:

- [UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview)
- [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview)
- [UIScrollView](https://developer.apple.com/documentation/uikit/uiscrollview)
- [UITableView](https://developer.apple.com/documentation/uikit/uitableview)
- [UITextField](https://developer.apple.com/documentation/uikit/uitextfield)
- [UITextView](https://developer.apple.com/documentation/uikit/uitextview)
- [UIWebView](https://developer.apple.com/documentation/uikit/uiwebview)

Other frameworks may also have views with preservable state. For information about whether a view saves state information and what state it saves, see the reference for the corresponding class.

#### Preserving the State of a Custom View

If you are implementing a custom view that has restorable state, implement the [encodeRestorableStateWithCoder:](https://developer.apple.com/documentation/uikit/uiview/1622516-encoderestorablestate) and [decodeRestorableStateWithCoder:](https://developer.apple.com/documentation/uikit/uiview/1622638-decoderestorablestate) methods and use them to encode and decode that state. Use those methods to save only the data that cannot be easily reconfigured by other means. For example, use these methods to save data that is modified by user interactions with the view. Do not use these methods to save the data being presented by the view or any data that the owning view controller can configure easily.

Listing 5-3 shows an example of how to preserve and restore the selection for a custom view that contains editable text. In the example, the range is accessible using the `selectionRange` and `setSelectionRange:` methods, which are custom methods the view uses to manage the selection. Encoding the data only requires writing it to the provided coder object. Restoring the data requires reading it and applying it to the view.

__Listing 5-3__  Preserving the selection of a custom text view

```objc
// Preserve the text selection
- (void) encodeRestorableStateWithCoder:(NSCoder *)coder {
    [super encodeRestorableStateWithCoder:coder];

    NSRange range = [self selectionRange];
    [coder encodeInt:range.length forKey:kMyTextViewSelectionRangeLength];
    [coder encodeInt:range.location forKey:kMyTextViewSelectionRangeLocation];
}

// Restore the text selection.
- (void) decodeRestorableStateWithCoder:(NSCoder *)coder {
   [super decodeRestorableStateWithCoder:coder];
   if ([coder containsValueForKey:kMyTextViewSelectionRangeLength] &&
           [coder containsValueForKey:kMyTextViewSelectionRangeLocation]) {
      NSRange range;
      range.length = [coder decodeIntForKey:kMyTextViewSelectionRangeLength];
      range.location = [coder decodeIntForKey:kMyTextViewSelectionRangeLocation];
      if (range.length > 0)
         [self setSelectionRange:range];
   }
}
```

#### Implementing Preservation-Friendly Data Sources

Because the data displayed by a table or collection view can change, both classes save information about the current selection and visible cells only if their data source implements the [UIDataSourceModelAssociation](https://developer.apple.com/documentation/uikit/uidatasourcemodelassociation) protocol. This protocol provides a way for a table or collection view to identify the content it contains without relying on the index path of that content. Thus, regardless of where the data source places an item during the next launch cycle, the view still has all the information it needs to locate that item.

In order to implement the `UIDataSourceModelAssociation` protocol successfully, your data source object must be able to identify items between subsequent launches of the app. This means that any identification scheme you devise must be invariant for a given piece of data. This is essential because the data source must be able to retrieve the same piece of data for the same identifier each time it is requested. Implementing the protocol itself is a matter of mapping from a data item to its unique ID and back again.

Apps that use Core Data can implement the protocol by taking advantage of object identifiers. Each object in a Core Data store has a unique object identifier that can be converted into a URI and used to locate the object later. If your app does not use Core Data, you need to devise your own form of unique identifiers if you want to support state preservation for your views.

__Note:__ Remember that implementing the `UIDataSourceModelAssociation` protocol is only necessary to preserve attributes such as the current selection in a table or collection view. This protocol is not used to preserve the actual data managed by your data source. It is your app’s responsibility to ensure that its data is saved at appropriate times.

### Preserving Your App’s High-Level State

In addition to the data preserved by your app’s view controllers and views, UIKit provides hooks for you to save any miscellaneous data needed by your app. Specifically, the `UIApplicationDelegate` protocol includes the following methods for you to override:

- [application:willEncodeRestorableStateWithCoder:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623099-application)
- [application:didDecodeRestorableStateWithCoder:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623006-application)

If your app contains state that does not live in a view controller, but that needs to be preserved, you can use the preceding methods to save and restore it. The `application:willEncodeRestorableStateWithCoder:` method is called at the very beginning of the preservation process so that you can write out any high-level app state, such as the current version of your user interface. The `application:didDecodeRestorableStateWithCoder:` method is called at the end of the restoration state so that you can decode any data and perform any final cleanup that your app requires.

### Tips for Saving and Restoring State Information

As you add support for state preservation and restoration to your app, consider the following guidelines:

- __Encode version information along with the rest of your app’s state.__ During the preservation process, it is recommended that you encode a version string or number that identifies the current revision of your app’s user interface. You can encode this state in the [application:willEncodeRestorableStateWithCoder:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623099-application) method of your app delegate. When your app delegate’s [application:shouldRestoreApplicationState:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622987-application) method is called, you can retrieve this information from the provided coder and use it to determine if state preservation is possible.
- __Do not include objects from your data model in your app’s state.__ Apps should continue to save their data separately in iCloud or to local files on disk. Never use the state restoration mechanism to save that data. Preserved interface data may be deleted if problems occur during a restore operation. Therefore, any preservation-related data you write to disk should be considered purgeable.
- __The state preservation system expects you to use view controllers in the ways they were designed to be used.__ The view controller hierarchy is created through a combination of view controller containment and by presenting one view controller from another. If your app displays the view of a view controller by another means—for example, by adding it to another view without creating a containment relationship between the corresponding view controllers—the preservation system will not be able to find your view controller to preserve it.
- __Remember that you might not want to preserve all view controllers.__ In some cases, it might not make sense to preserve a view controller. For example, if the user left your app while it was displaying a view controller to change the user’s password, you might want to cancel the operation and restore the app to the previous screen. In such a case, you would not preserve the view controller that asks for the new password information.
- __Avoid swapping view controller classes during the restoration process.__ The state preservation system encodes the class of the view controllers it preserves. During restoration, if your app returns an object whose class does not match (or is not a subclass of) the original object, the system does not ask the view controller to decode any state information. Thus, swapping out the old view controller for a completely different one does not restore the full state of the object.
- __The system automatically deletes an app’s preserved state when the user force quits the app.__ Deleting the preserved state information when the app is killed is a safety precaution. (As a safety precaution, the system also deletes preserved state if the app crashes twice during launch.) If you want to test your app’s ability to restore its state, you should not use the multitasking bar to kill the app during debugging. Instead, use Xcode to kill the app or kill the app programmatically by installing a temporary command or gesture to call `exit` on demand.

## Tips for Developing a VoIP App

A _Voice over Internet Protocol (VoIP)_ app allows the user to make phone calls using an Internet connection instead of the device’s cellular service. In iOS 8 and later, you can use the Apple Push Notification service (APNs) and the APIs of the PushKit framework to create a VoIP app. Relying on push notifications to enable VoIP functionality means that your app doesn’t have to maintain a persistent network connection to the associated service or configure a socket for VoIP usage. When a VoIP push notification arrives, your app is given time to handle the notification, even if the app is currently terminated.

__Note:__ VoIP push notifications are sent only to devices running iOS 8 or later. If you need to support devices that run earlier versions of iOS, you’re responsible for maintaining a compatible implementation.

As with any background audio app, the audio session for a VoIP app must be configured properly to ensure the app works smoothly with other audio-based apps. Because audio playback and recording for a VoIP app are not used all the time, it is especially important that you create and configure your app’s audio session object only when it’s needed. For example, you would create the audio session to notify the user of an incoming call or while the user was actually on a call. As soon as the call ends, you would then remove strong references to the audio session and give other audio apps the opportunity to play their audio.

For information about how to configure and manage an audio session for a VoIP app, see _[Audio Session Programming Guide](../../Audio/Audio%20Session%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzv)_. To learn more about using VoIP push notifications and the PushKit APIs to create a VoIP app, see _[Energy Efficiency Guide for iOS Apps](../../Performance/Energy%20Efficiency%20Guide%20for%20iOS%20Apps/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbt)_.

There are several requirements for implementing a VoIP app:

1. Enable the Voice over IP background mode for your app. (Because VoIP apps involve audio content, it is recommended that you also enable the Audio and AirPlay background mode.) You enable background modes in the Capabilities tab of your Xcode project.
2. Use PushKit APIs to register to receive VoIP push notifications and handle incoming notifications.
3. Configure your audio session to handle transitions to and from active use.
4. To ensure a better user experience on iPhone, use the Core Telephony framework to adjust your behavior in relation to cell-based phone calls; see _[Core Telephony Framework Reference](https://developer.apple.com/documentation/coretelephony)_.
5. To ensure good performance for your VoIP app, use the System Configuration framework to detect network changes and allow your app to sleep as much as possible.
6. Request a VoIP Services certificate to allow your notification server to connect to the VoIP service.

Enabling the VoIP background mode lets the system know that it should allow the app to run in the background as needed to manage its network sockets. This key also permits your app to play background audio (although enabling the Audio and AirPlay mode is still encouraged). An app that supports this mode is also relaunched in the background immediately after system boot to ensure that the VoIP services are always available.

### Using the Reachability Interfaces to Improve the User Experience

Because VoIP apps rely heavily on the network, they should use the reachability interfaces of the System Configuration framework to track network availability and adjust their behavior accordingly. The reachability interfaces allow an app to be notified whenever network conditions change. For example, a VoIP app could close its network connections when the network becomes unavailable and recreate them when it becomes available again. The app could also use those kinds of changes to keep the user apprised about the state of the VoIP connection.

To use the reachability interfaces, you must register a callback function with the framework and use it to track changes. To register a callback function:

1. Create a [SCNetworkReachabilityRef](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachability) structure for your target remote host.
2. Assign a callback function to your structure (using the [SCNetworkReachabilitySetCallback](https://developer.apple.com/documentation/systemconfiguration/1514903-scnetworkreachabilitysetcallback) function) that processes changes in your target’s reachability status.
3. Add that target to an active run loop of your app (such as the main run loop) using the [SCNetworkReachabilityScheduleWithRunLoop](https://developer.apple.com/documentation/systemconfiguration/1514894-scnetworkreachabilityschedulewit) function.

Adjusting your app’s behavior based on the availability of the network can also help improve the battery life of the underlying device. Letting the system track the network changes means that your app can let itself go to sleep more often.

For more information about the reachability interfaces, see _[System Configuration Framework Reference](https://developer.apple.com/documentation/systemconfiguration)_.

[Next](Inter-App%20Communication.md)[Previous](Strategies%20for%20Handling%20App%20State%20Transitions.md)
