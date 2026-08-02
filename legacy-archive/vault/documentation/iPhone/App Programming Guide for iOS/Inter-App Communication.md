---
title: App Programming Guide for iOS
apple_id: TP40007072
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Inter-AppCommunication/Inter-AppCommunication.html
archived_at: '2026-07-27T06:57:07.074154Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Programming Guide for iOS](About%20iOS%20App%20Architecture.md)


[Next](Performance%20Tips.md)[Previous](Strategies%20for%20Implementing%20Specific%20App%20Features.md)

# Inter-App Communication

Apps communicate only indirectly with other apps on a device. You can use AirDrop to share files and data with other apps. You can also define a custom URL scheme so that apps can send information to your app using URLs.

__Note:__ You can also send files between apps using a [UIDocumentInteractionController](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller) object or a document picker. For information about adding support for a document interaction controller, see _[Document Interaction Programming Topics for iOS](../../File%20Management/Document%20Interaction%20Programming%20Topics%20for%20iOS/About%20Document%20Interaction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydimbt)_. For information about using a document picker to open files, see _[Document Picker Programming Guide](../../File%20Management/Document%20Picker%20Programming%20Guide/About%20the%20Document%20Picker.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dinjr)_.

## Supporting AirDrop

AirDrop lets you share photos, documents, URLs, and other types of data with nearby devices. AirDrop takes advantage of peer-to-peer networking to find nearby devices and connect to them.

### Sending Files and Data to Another App

To send files and data using AirDrop, use a [UIActivityViewController](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller) object to display an activity sheet from your user interface using. When creating this view controller, you specify the data objects that you want to share. The view controller displays only those activities that support the specified data. For AirDrop, you can specify images, strings, URLs, and several other types of data. You can also pass custom objects that adopt the [UIActivityItemSource](https://developer.apple.com/documentation/uikit/uiactivityitemsource) protocol.

To display an activity view controller, you can use code similar to that shown in Listing 6-1. The activity view controller automatically uses the type of the specified object to determine what activities to display in the activity sheet. You do not have to specify the AirDrop activity explicitly. However, you can prevent the sheet from displaying specific types using the view controller’s [excludedActivityTypes](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/1622009-excludedactivitytypes) property. When displaying an activity view controller on iPad, you must use a popover.

__Listing 6-1__  Displaying an activity sheet on iPhone

```objc
- (void)displayActivityControllerWithDataObject:(id)obj {
   UIActivityViewController* vc = [[UIActivityViewController alloc]
                                initWithActivityItems:@[obj] applicationActivities:nil];
    [self presentViewController:vc animated:YES completion:nil];
}
```

For more information about using the activity view controller, see _[UIActivityViewController Class Reference](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller)_. For a complete list of activities and the data types they support, see _[UIActivity Class Reference](https://developer.apple.com/documentation/uikit/uiactivity)_.

### Receiving Files and Data Sent to Your App

To receive files sent to your app using AirDrop, do the following:

- In Xcode, declare support for the document types your app is capable of opening.
- In your app delegate, implement the [application:openURL:sourceApplication:annotation:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623073-application) method. Use that method to receive the data that was sent by the other app.

The Info tab of your Xcode project contains a Document Types section for specifying the document types your app supports. At a minimum, you must specify a name for your document type and one or more UTIs that represent the data type. For example, to declare support for PNG files, you would include `public.png` as the UTI string. iOS uses the specified UTIs to determine if your app is eligible to open a given document.

After transferring an eligible document to your app’s container, iOS launches your app (if needed) and calls the `application:openURL:sourceApplication:annotation:` method of its app delegate. If your app is in the foreground, you should use this method to open the file and display it to the user. If your app is in the background, you might decide only to note that the file is there so that you can open it later. Because files transferred via AirDrop are encrypted using data protection, you cannot open files unless the device is currently unlocked.

Your app has permission to read and delete a file that it receives but it does not have permission to write to that file. If you plan to modify the file, you must move it out of its current location before doing so. It is recommended that you delete the original version of the file afterward.

For more information about supporting document types in your app, see _[Document-Based App Programming Guide for iOS](../../Data%20Management/Document-Based%20App%20Programming%20Guide%20for%20iOS/About%20Document-Based%20Applications%20in%20iOS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbz)_.

## Using URL Schemes to Communicate with Apps

A URL scheme lets you communicate with other apps through a protocol that you define. To communicate with an app that implements such a scheme, you must create an appropriately formatted URL and ask the system to open it. To implement support for a custom scheme, you must declare support for the scheme and handle incoming URLs that use the scheme.

__Note:__ Apple provides built-in support for the `http`, `mailto`, `tel`, and `sms` URL schemes among others. It also supports `http`–based URLs targeted at the Maps, YouTube, and iPod apps. The handlers for these schemes are fixed and cannot be changed. If your URL type includes a scheme that is identical to one defined by Apple, the Apple-provided app is launched instead of your app. For information about the schemes supported by apple, see _[Apple URL Scheme Reference](../../../featuredarticles/Apple%20URL%20Scheme%20Reference/About%20Apple%20URL%20Schemes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqojz)_.

### Sending a URL to Another App

When you want to send data to an app that implements a custom URL scheme, create an appropriately formatted URL and call the [openURL:](https://developer.apple.com/documentation/uikit/uiapplication/1622961-openurl) method of the app object. The `openURL:` method launches the app with the registered scheme and passes your URL to it. At that point, control passes to the new app.

The following code fragment illustrates how one app can request the services of another app (“todolist” in this example is a hypothetical custom scheme registered by an app):

```
NSURL *myURL = [NSURL URLWithString:@"todolist://www.acme.com?Quarterly%20Report#200806231300"];
[[UIApplication sharedApplication] openURL:myURL];
```

If your app defines a custom URL scheme, it should implement a handler for that scheme as described in [Implementing Custom URL Schemes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanzsfvbuqnrnknltcma). For more information about the system-supported URL schemes, including information about how to format the URLs, see _[Apple URL Scheme Reference](../../../featuredarticles/Apple%20URL%20Scheme%20Reference/About%20Apple%20URL%20Schemes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqojz)_.

### Implementing Custom URL Schemes

If your app can receive specially formatted URLs, you should register the corresponding URL schemes with the system. Apps often use custom URL schemes to vend services to other apps. For example, the Maps app supports URLs for displaying specific map locations.

#### Registering Custom URL Schemes

To register a URL type for your app, include the `CFBundleURLTypes` key in your app’s `Info.plist` file. The `CFBundleURLTypes` key contains an array of dictionaries, each of which defines a URL scheme the app supports. Table 6-1 describes the keys and values to include in each dictionary.

__Table 6-1__  Keys and values of the `CFBundleURLTypes` property

| Key | Value |
| `CFBundleURLName` | A string containing the abstract name of the URL scheme. To ensure uniqueness, it is recommended that you specify a reverse-DNS style of identifier, for example, `com.acme.myscheme`.  The string you specify is also used as a key in your app’s `InfoPlist.strings` file. The value of the key is the human-readable scheme name. |
| `CFBundleURLSchemes` | An array of strings containing the URL scheme names—for example, `http`, `mailto`, `tel`, and `sms`. |

__Note:__ If more than one third-party app registers to handle the same URL scheme, there is currently no process for determining which app will be given that scheme.

#### Handling URL Requests

An app that has its own custom URL scheme must be able to handle URLs passed to it. All URLs are passed to your [app delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14), either at launch time or while your app is running or in the background. To handle incoming URLs, your delegate should implement the following methods:

- Use the [application:willFinishLaunchingWithOptions:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623032-application) and [application:didFinishLaunchingWithOptions:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) methods to retrieve information about the URL and decide whether you want to open it. If either method returns `NO`, your app’s URL handling code is not called.
- Use the [application:openURL:sourceApplication:annotation:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623073-application) method to open the file.

If your app is not running when a URL request arrives, it is launched and moved to the foreground so that it can open the URL. The implementation of your `application:willFinishLaunchingWithOptions:` or `application:didFinishLaunchingWithOptions:` method should retrieve the URL from its options dictionary and determine whether the app can open it. If it can, return `YES` and let your `application:openURL:sourceApplication:annotation:` (or `application:handleOpenURL:`) method handle the actual opening of the URL. (If you implement both methods, both must return `YES` before the URL can be opened.) Figure 6-1 shows the modified launch sequence for an app that is asked to open a URL.

__Figure 6-1__  Launching an app to open a URL

（原归档配图获取待重试：`app_open_url_2x.png`）

If your app is running but is in the background or suspended when a URL request arrives, it is moved to the foreground to open the URL. Shortly thereafter, the system calls the delegate’s `application:openURL:sourceApplication:annotation:` to check the URL and open it. Figure 6-2 shows the modified process for moving an app to the foreground to open a URL.

__Figure 6-2__  Waking a background app to open a URL

（原归档配图获取待重试：`app_bg_open_url_2x.png`）

__Note:__ Apps that support custom URL schemes can specify different launch images to be displayed when launching the app to handle a URL. For more information about how to specify these launch images, see [Displaying a Custom Launch Image When a URL is Opened](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanzsfvbuqnrnknltcoa).

All URLs are passed to your app in an [NSURL](https://developer.apple.com/documentation/foundation/nsurl) object. It is up to you to define the format of the URL, but the `NSURL` class conforms to the RFC 1808 specification and therefore supports most URL formatting conventions. Specifically, the class includes methods that return the various parts of a URL as defined by RFC 1808, including the user, password, query, fragment, and parameter strings. The “protocol” for your custom scheme can use these URL parts for conveying various kinds of information.

In the implementation of [application:openURL:sourceApplication:annotation:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623073-application) shown in Listing 6-2, the passed-in URL object conveys app-specific information in its query and fragment parts. The delegate extracts this information—in this case, the name of a to-do task and the date the task is due—and with it creates a model object of the app. This example assumes that the user is using a Gregorian calendar. If your app supports non-Gregorian calendars, you need to design your URL scheme accordingly and be prepared to handle those other calendar types in your code.

__Listing 6-2__  Handling a URL request based on a custom scheme

```objc
- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url
        sourceApplication:(NSString *)sourceApplication annotation:(id)annotation {
    if ([[url scheme] isEqualToString:@"todolist"]) {
        ToDoItem *item = [[ToDoItem alloc] init];
        NSString *taskName = [url query];
        if (!taskName || ![self isValidTaskString:taskName]) { // must have a task name
            return NO;
        }
        taskName = [taskName stringByReplacingPercentEscapesUsingEncoding:NSUTF8StringEncoding];

        item.toDoTask = taskName;
        NSString *dateString = [url fragment];
        if (!dateString || [dateString isEqualToString:@"today"]) {
            item.dateDue = [NSDate date];
        } else {
            if (![self isValidDateString:dateString]) {
                return NO;
            }
            // format: yyyymmddhhmm (24-hour clock)
            NSString *curStr = [dateString substringWithRange:NSMakeRange(0, 4)];
            NSInteger yeardigit = [curStr integerValue];
            curStr = [dateString substringWithRange:NSMakeRange(4, 2)];
            NSInteger monthdigit = [curStr integerValue];
            curStr = [dateString substringWithRange:NSMakeRange(6, 2)];
            NSInteger daydigit = [curStr integerValue];
            curStr = [dateString substringWithRange:NSMakeRange(8, 2)];
            NSInteger hourdigit = [curStr integerValue];
            curStr = [dateString substringWithRange:NSMakeRange(10, 2)];
            NSInteger minutedigit = [curStr integerValue];

            NSDateComponents *dateComps = [[NSDateComponents alloc] init];
            [dateComps setYear:yeardigit];
            [dateComps setMonth:monthdigit];
            [dateComps setDay:daydigit];
            [dateComps setHour:hourdigit];
            [dateComps setMinute:minutedigit];
            NSCalendar *calendar = [s[NSCalendar alloc] initWithCalendarIdentifier:NSGregorianCalendar];
            NSDate *itemDate = [calendar dateFromComponents:dateComps];
            if (!itemDate) {
                return NO;
            }
            item.dateDue = itemDate;
        }

        [(NSMutableArray *)self.list addObject:item];
        return YES;
    }
    return NO;
}
```

Be sure to validate the input you get from URLs passed to your app; see [Validating Input and Interprocess Communication](../../Security/Secure%20Coding%20Guide/Validating%20Input%20and%20Interprocess%20Communication.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenbw) in _[Secure Coding Guide](../../Security/Secure%20Coding%20Guide/Introduction%20to%20Secure%20Coding%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjv)_ to find out how to avoid problems related to URL handling. To learn about URL schemes defined by Apple, see _[Apple URL Scheme Reference](../../../featuredarticles/Apple%20URL%20Scheme%20Reference/About%20Apple%20URL%20Schemes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqojz)_.

### Displaying a Custom Launch Image When a URL is Opened

Apps that support custom URL schemes can provide a custom launch image for each scheme. When the system launches your app to handle a URL and no relevant snapshot is available, it displays the launch image you specify. To specify a launch image, provide a PNG image whose name uses the following naming conventions:

_<basename>_`-`_<url_scheme>__<other_modifiers>_`.png`

In this naming convention, basename represents the base image name specified by the `UILaunchImageFile` key in your app’s `Info.plist` file. If you do not specify a custom base name, use the string `Default`. The _<url_scheme>_ portion of the name is your URL scheme name. To specify a generic launch image for the `myapp` URL scheme, you would include an image file with the name `Default-myapp@2x.png` in the app’s bundle. (The @2x modifier signifies that the image is intended for Retina displays. If your app also supports standard resolution displays, you would also provide a `Default-myapp.png` image.)

For information about the other modifiers you can include in launch image names, see the description of the `UILaunchImageFile` name key in _[Information Property List Key Reference](../../General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_.

[Next](Performance%20Tips.md)[Previous](Strategies%20for%20Implementing%20Specific%20App%20Features.md)
