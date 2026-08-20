---
title: Core Bluetooth Programming Guide
apple_id: TP40013257
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: CoreBluetooth
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/CoreBluetoothBackgroundProcessingForIOSApps/PerformingTasksWhileYourAppIsInTheBackground.html
archived_at: '2026-07-18T01:33:42.447714Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Bluetooth Programming Guide](About%20Core%20Bluetooth.md)


[Next](Best%20Practices%20for%20Interacting%20with%20a%20Remote%20Peripheral%20Device.md)[Previous](Performing%20Common%20Peripheral%20Role%20Tasks.md)

# Core Bluetooth Background Processing for iOS Apps

For iOS apps, it is crucial to know whether your app is running in the foreground or the background. An app must behave differently in the background than in the foreground, because system resources are more limited on iOS devices. For an overall discussion of background operation on iOS, see [Background Execution](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html#//apple_ref/doc/uid/TP40007072-CH4) in _[App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072)_.

By default, many of the common Core Bluetooth tasks—on both the central and peripheral side—are disabled while your app is in the background or in a suspended state. That said, you can declare your app to support the Core Bluetooth background execution modes to allow your app to be woken up from a suspended state to process certain Bluetooth-related events. Even if your app doesn’t need the full range of background processing support, it can still ask to be alerted by the system when important events occur.

Even if your app supports one or both of the Core Bluetooth background execution modes, it can’t run forever. At some point, the system may need to terminate your app to free up memory for the current foreground app—causing any active or pending connections to be lost, for instance. As of iOS 7, Core Bluetooth supports saving state information for central and peripheral manager objects and restoring that state at app launch time. You can use this feature to support long-term actions involving Bluetooth devices.

As with most iOS apps, unless you request permission to perform specific background tasks, your app transitions to the suspended state shortly after entering the background state. While in the suspended state, your app is unable to perform Bluetooth-related tasks, nor is it aware of any Bluetooth-related events until it resumes to the foreground.

On the central side, foreground-only apps—apps that have not declared to support either of the Core Bluetooth background execution modes—cannot scan for and discover advertising peripherals while in the background or while suspended. On the peripheral side, advertising is disabled, and any central trying to access a dynamic characteristic value of one of the app’s published services receives an error.

Depending on the use case, this default behavior can affect your app in several ways. As an example, imagine that you are interacting with the data on a peripheral that you’re currently connected to. Now imagine that your app moves to the suspended state (because, for example, the user switches to another app). If the connection to the peripheral is lost while your app is suspended, you won’t be aware that any disconnection occurred until your app resumes to the foreground.

All Bluetooth-related events that occur while a foreground-only app is in the suspended state are queued by the system and delivered to the app only when it resumes to the foreground. That said, Core Bluetooth provides a way to alert the user when certain central role events occur. The user can then use these alerts to decide whether a particular event warrants bringing the app back to the foreground.

You can take advantage of these alerts by including one of the following peripheral connection options when calling the [connectPeripheral:options:](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518766-connect) method of the [CBCentralManager](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager) class to connect to a remote peripheral:

- [CBConnectPeripheralOptionNotifyOnConnectionKey](https://developer.apple.com/documentation/corebluetooth/cbconnectperipheraloptionnotifyonconnectionkey)—Include this key if you want the system to display an alert for a given peripheral if the app is suspended when a successful connection is made.
- [CBConnectPeripheralOptionNotifyOnDisconnectionKey](https://developer.apple.com/documentation/corebluetooth/cbconnectperipheraloptionnotifyondisconnectionkey)—Include this key if you want the system to display a disconnection alert for a given peripheral if the app is suspended at the time of the disconnection.
- [CBConnectPeripheralOptionNotifyOnNotificationKey](https://developer.apple.com/documentation/corebluetooth/cbconnectperipheraloptionnotifyonnotificationkey)—Include this key if you want the system to display an alert for all notifications received from a given peripheral if the app is suspended at the time.

For more information about the peripheral connection options, see the `Peripheral Connection Options` constants, detailed in _[CBCentralManager Class Reference](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager)_.

If your app needs to run in background to perform certain Bluetooth-related tasks, it must declare that it supports a Core Bluetooth background execution mode in its [Information property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/InfoPlist.html#//apple_ref/doc/uid/TP40008195-CH61) (`Info.plist`) file. When your app declares this, the system wakes it up from a suspended state to allow it to handle Bluetooth-related events. This support is important for apps that interact with Bluetooth low energy devices that deliver data at regular intervals, such as a heart rate monitor.

There are two Core Bluetooth background execution modes that an app may declare—one for apps implementing the central role, and another for apps implementing the peripheral role. If your app implements both roles, it may declare that it supports both background execution modes. The Core Bluetooth background execution modes are declared by adding the `[UIBackgroundModes](../../../../General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.md#apple-f4xwc4dqnrsv64tfmyxwi33df5ygy2ltoqxws3tgn4xvkskcmfrwwz3sn52w4zcnn5sgk4y)` key to your `Info.plist` file and setting the key’s value to an array containing one of the following strings:

- `bluetooth-central`—The app communicates with Bluetooth low energy peripherals using the Core Bluetooth framework.
- `bluetooth-peripheral`—The app shares data using the Core Bluetooth framework.

For information about how to configure the contents of your `Info.plist` file, see [Xcode Help](https://help.apple.com/xcode).

When an app that implements the central role includes the `[UIBackgroundModes](../../../../General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.md#apple-f4xwc4dqnrsv64tfmyxwi33df5ygy2ltoqxws3tgn4xvkskcmfrwwz3sn52w4zcnn5sgk4y)` key with the `bluetooth-central` value in its `Info.plist` file, the Core Bluetooth framework allows your app to run in the background to perform certain Bluetooth-related tasks. While your app is in the background you can still discover and connect to peripherals, and explore and interact with peripheral data. In addition, the system wakes up your app when any of the [CBCentralManagerDelegate](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate) or [CBPeripheralDelegate](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate) delegate methods are invoked, allowing your app to handle important central role events, such as when a connection is established or torn down, when a peripheral sends updated characteristic values, and when a central manager’s state changes.

Although you can perform many Bluetooth-related tasks while your app is in the background, keep in mind that scanning for peripherals while your app is in the background operates differently than when your app is in the foreground. In particular, when your app is scanning for device while in the background:

- The [CBCentralManagerScanOptionAllowDuplicatesKey](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerscanoptionallowduplicateskey) scan option key is ignored, and multiple discoveries of an advertising peripheral are coalesced into a single discovery event.
- If all apps that are scanning for peripherals are in the background, the interval at which your central device scans for advertising packets increases. As a result, it may take longer to discover an advertising peripheral.

These changes help minimize radio usage and improve the battery life on your iOS device.

To perform certain peripheral role tasks while in the background, you must include the `[UIBackgroundModes](../../../../General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.md#apple-f4xwc4dqnrsv64tfmyxwi33df5ygy2ltoqxws3tgn4xvkskcmfrwwz3sn52w4zcnn5sgk4y)` key with the `bluetooth-peripheral` value in your app’s `Info.plist` file. When this key-value pair is included in the app’s `Info.plist` file, the system wakes up your app to process read, write, and subscription events.

In addition to allowing your app to be woken up to handle read, write, and subscription requests from connected centrals, the Core Bluetooth framework allows your app to advertise while in the background state. That said, you should be aware that advertising while your app is in the background operates differently than when your app is in the foreground. In particular, when your app is advertising while in the background:

- The [CBAdvertisementDataLocalNameKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdatalocalnamekey) advertisement key is ignored, and the local name of peripheral is not advertised.
- All service UUIDs contained in the value of the [CBAdvertisementDataServiceUUIDsKey](https://developer.apple.com/documentation/corebluetooth/cbadvertisementdataserviceuuidskey) advertisement key are placed in a special “overflow” area; they can be discovered only by an iOS device that is explicitly scanning for them.
- If all apps that are advertising are in the background, the frequency at which your peripheral device sends advertising packets may decrease.

Although declaring your app to support one or both of the Core Bluetooth background execution modes may be necessary to fulfill a particular use case, you should always perform background processing responsibly. Because performing many Bluetooth-related tasks require the active use of an iOS device’s onboard radio—and, in turn, radio usage has an adverse effect on an iOS device’s battery life—try to minimize the amount of work you do in the background. Apps woken up for any Bluetooth-related events should process them and return as quickly as possible so that the app can be suspended again.

Any app that declares support for either of the Core Bluetooth background executions modes must follow a few basic guidelines:

- Apps should be session based and provide an interface that allows the user to decide when to start and stop the delivery of Bluetooth-related events.
- Upon being woken up, an app has around 10 seconds to complete a task. Ideally, it should complete the task as fast as possible and allow itself to be suspended again. Apps that spend too much time executing in the background can be throttled back by the system or killed.
- Apps should not use being woken up as an opportunity to perform extraneous tasks that are unrelated to why the app was woken up by the system.

For more-general information about how your app should be behave in the background state, see [Being a Responsible Background App](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html#//apple_ref/doc/uid/TP40007072-CH4-SW8) in _[App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072)_.

Some apps may need to use the Core Bluetooth framework to perform long-term actions in the background. As an example, imagine you are developing a home security app for an iOS device that communicates with a door lock (equipped with Bluetooth low energy technology). The app and the lock interact to automatically lock the door when the user leaves home and unlock the door when the user returns—all while the app is in the background. When the user leaves home, the iOS device may eventually become out of range of the lock, causing the connection to the lock to be lost. At this point, the app can simply call the [connectPeripheral:options:](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518766-connect) method of the [CBCentralManager](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager) class, and because connection requests do not time out, the iOS device will reconnect when the user returns home.

Now imagine that the user is away from home for a few days. If the app is terminated by the system while the user is away, the app will not be able to reconnect to the lock when the user returns home, and the user may not be able to unlock the door. For apps like these, it is critical to be able to continue using Core Bluetooth to perform long-term actions, such as monitoring active and pending connections.

Because state preservation and restoration is built in to Core Bluetooth, your app can opt in to this feature to ask the system to preserve the state of your app’s central and peripheral managers and to continue performing certain Bluetooth-related tasks on their behalf, even when your app is no longer running. When one of these tasks completes, the system relaunches your app into the background and gives your app the opportunity to restore its state and to handle the event appropriately. In the case of the home security app described above, the system would monitor the connection request, and re-relaunch the app to handle the [centralManager:didConnectPeripheral:](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518969-centralmanager) delegate callback when the user returned home and the connection request completed.

Core Bluetooth supports state preservation and restoration for apps that implement the central role, peripheral role, or both. When your app implements the central role and adds support for state preservation and restoration, the system saves the state of your central manager object when the system is about to terminate your app to free up memory (if your app has multiple central managers, you can choose which ones you want the system to keep track of). In particular, for a given [CBCentralManager](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager) object, the system keeps track of:

- The services the central manager was scanning for (and any scan options specified when the scan started)
- The peripherals the central manager was trying to connect to or had already connected to
- The characteristics the central manager was subscribed to

Apps that implement the peripheral role can likewise take advantage of state preservation and restoration. For [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager) objects, the system keeps track of:

- The data the peripheral manager was advertising
- The services and characteristics the peripheral manager published to the device’s database
- The centrals that were subscribed to your characteristics’ values

When your app is relaunched into the background by the system (because a peripheral your app was scanning for is discovered, for instance), you can reinstantiate your app’s central and peripheral managers and restore their state. The following section describes in detail how to take advantage of state preservation and restoration in your app.

State preservation and restoration in Core Bluetooth is an opt-in feature and requires help from your app to work. You can add support for this feature in your app by following this process:

1. (Required) Opt in to state preservation and restoration when you allocate and initialize a central or peripheral manager object. This step is described in Opt In to State Preservation and Restoration.
2. (Required) Reinstantiate any central or peripheral manager objects after your app is relaunched by the system. This step is described in [Reinstantiate Your Central and Peripheral Managers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjxfvbuqnznknltcmy).
3. (Required) Implement the appropriate restoration delegate method. This step is described in [Implement the Appropriate Restoration Delegate Method](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjxfvbuqnznknltcna).
4. (Optional) Update your central and peripheral managers’ initialization process. This step is described in [Update Your Initialization Process](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjxfvbuqnznknltcni).

To opt in to the state preservation and restoration feature, simply provide a unique restoration identifier when you allocate and initialize a central or peripheral manager. A _restoration identifier_ is a string that identifies the central or peripheral manager to Core Bluetooth and to your app. The value of the string is significant only to your code, but the presence of this string tells Core Bluetooth that it needs to preserve the state of the tagged object. Core Bluetooth preserves the state of only those objects that have a restoration identifier.

For example, to opt in to state preservation and restoration in an app that uses only one instance of a [CBCentralManager](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager) object to implement the central role, specify the [CBCentralManagerOptionRestoreIdentifierKey](https://developer.apple.com/documentation/corebluetooth/cbcentralmanageroptionrestoreidentifierkey) initialization option and provide a restoration identifier for the central manager when you allocate and initialize it.

```
    myCentralManager =
        [[CBCentralManager alloc] initWithDelegate:self queue:nil
         options:@{ CBCentralManagerOptionRestoreIdentifierKey:
         @"myCentralManagerIdentifier" }];
```

Although the above example does not demonstrate this, you opt in to state preservation and restoration in an app that uses peripheral manager objects in an analogous way: Specify the [CBPeripheralManagerOptionRestoreIdentifierKey](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanageroptionrestoreidentifierkey) initialization option, and provide a restoration identifier when you allocate and initialize each peripheral manager object.

When your app is relaunched into the background by the system, the first thing you need to do is reinstantiate the appropriate central and peripheral managers with the same restoration identifiers as they had when they were first created. If your app uses only one central or peripheral manager, and that manager exists for the lifetime of your app, there is nothing more you need to do for this step.

If your app uses more than one central or peripheral manager or if it uses a manager that isn’t around for the lifetime of your app, your app needs to know which managers to reinstantiate when it is relaunched by the system. You can access a list of all the restoration identifiers for the manager objects the system was preserving for your app when it was terminated, by using the appropriate launch option keys ([UIApplicationLaunchOptionsBluetoothCentralsKey](https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/1622965-bluetoothcentrals) or [UIApplicationLaunchOptionsBluetoothPeripheralsKey](https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/1623116-bluetoothperipherals)) when implementing your app delegate’s [application:didFinishLaunchingWithOptions:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) method.

For example, when your app is relaunched by system, you can retrieve all the restoration identifiers for the central manager objects the system was preserving for your app, like this:

```objc
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

    NSArray *centralManagerIdentifiers =
        launchOptions[UIApplicationLaunchOptionsBluetoothCentralsKey];
    ...
```

After you have the list of restoration identifiers, simply loop through it and reinstantiate the appropriate central manager objects.

After you have reinstantiated the appropriate central and peripheral managers in your app, restore them by synchronizing their state with the state of the Bluetooth system. To bring your app up to speed with what the system has been doing on its behalf (while it was not running), you must implement the appropriate restoration delegate method. For central managers, implement the [centralManager:willRestoreState:](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518819-centralmanager) delegate method; for peripheral managers, implement the [peripheralManager:willRestoreState:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393317-peripheralmanager) delegate method.

In both of the above delegate methods, the last parameter is a dictionary that contains information about the managers that were preserved at the time the app was terminated. For a list of the available dictionary keys, see the `Central Manager State Restoration Options` constants in _[CBCentralManagerDelegate Protocol Reference](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate)_ and the `Peripheral_Manager_State_Restoration_Options` constants in _[CBPeripheralManagerDelegate Protocol Reference](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate)_.

To restore the state of a [CBCentralManager](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager) object, use the keys to the dictionary that is provided in the [centralManager:willRestoreState:](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518819-centralmanager) delegate method. As an example, if your central manager object had any active or pending connections at the time your app was terminated, the system continued to monitor them on your app’s behalf. As the following shows, you can use the [CBCentralManagerRestoredStatePeripheralsKey](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerrestoredstateperipheralskey) dictionary key to get of a list of all the peripherals (represented by [CBPeripheral](https://developer.apple.com/documentation/corebluetooth/cbperipheral) objects) the central manager was connected to or was trying to connect to:

```objc
- (void)centralManager:(CBCentralManager *)central
      willRestoreState:(NSDictionary *)state {

    NSArray *peripherals =
        state[CBCentralManagerRestoredStatePeripheralsKey];
    ...
```

What you do with the list of restored peripherals in the above example depends on the use case. For instance, if your app keeps a list of the peripherals the central manager discovers, you may want to add the restored peripherals to that list to keep references to them. As described in [Connecting to a Peripheral Device After You’ve Discovered It](Performing%20Common%20Central%20Role%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenjxfvbuqmznknlti), be sure to set a peripheral’s delegate to ensure that it receives the appropriate callbacks.

You can restore the state of a [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager) object in a similar way by using the keys to the dictionary that is provided in the [peripheralManager:willRestoreState:](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393317-peripheralmanager) delegate method.

After you have implemented the previous three required steps, you may want to take a look at updating your central and peripheral managers’ initialization process. Although this is an optional step, it can be important in ensuring that things run smoothly in your app. As an example, your app may have been terminated while it was in the middle of exploring the data of a connected peripheral. When your app is restored with this peripheral, it won’t know how far it made it the discovery process at the time it was terminated. You’ll want to make sure you’re starting from where you left off in the discovery process.

For example, when initializing your app in the [centralManagerDidUpdateState:](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518888-centralmanagerdidupdatestate) delegate method, you can find out if you successfully discovered a particular service of a restored peripheral (before your app was terminated), like this:

```
    NSUInteger serviceUUIDIndex =
        [peripheral.services indexOfObjectPassingTest:^BOOL(CBService *obj,
        NSUInteger index, BOOL *stop) {
            return [obj.UUID isEqual:myServiceUUIDString];
        }];

    if (serviceUUIDIndex == NSNotFound) {
        [peripheral discoverServices:@[myServiceUUIDString]];
        ...
```

As the above example shows, if the system terminated your app before it finished discovering the service, begin the exploring the restored peripheral’s data at that point by calling the [discoverServices:](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518706-discoverservices). If your app discovered the service successfully, you can then check to see whether the appropriate characteristics were discovered (and whether you already subscribed to them). By updating your initialization process in this manner, you’ll ensure that you’re calling the right methods at the right time.

[Next](Best%20Practices%20for%20Interacting%20with%20a%20Remote%20Peripheral%20Device.md)[Previous](Performing%20Common%20Peripheral%20Role%20Tasks.md)

