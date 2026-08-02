---
title: Energy Efficiency Guide for iOS Apps
apple_id: TP40015243
resource_type: Guide
platform: watchOS|iOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/MotionBestPractices.html
archived_at: '2026-07-18T01:48:24.701732Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for iOS Apps](index.md)



## Reduce the Frequency of Motion Updates

Users generate motion events whenever they move, shake, or tilt an iOS device. These motion events are detected by device hardware, such as the accelerometer, gyroscope, and magnetometer. An app can use this information to provide an immersive user experience. For example, a game may allow the user to move a character around the screen by tilting the device.

> [!NOTE]
> 

### Stop Orientation Change Notifications When No Longer Needed

Your app can register to receive notifications when the orientation of the device changes, providing an opportunity to readjust the layout or perform other reactive actions. Make sure you disable these notifications if they become unnecessary—for example, if the user has navigated to a different view that is only available in portrait orientation. Doing so lets the system power down the accelerometer hardware if it’s not being used elsewhere.

Before registering for orientation change notifications, activate the accelerometer by calling the [beginGeneratingDeviceOrientationNotifications](https://developer.apple.com/documentation/uikit/uidevice/1620041-begingeneratingdeviceorientation) method for the current device object. To start notifications, send the message [addObserver:selector:name:object:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/instm/NSNotificationCenter/addObserver:selector:name:object:) to the default notification center of your app (an instance of [NSNotificationCenter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/cl/NSNotificationCenter)). Pass it `UIDeviceOrientationDidChangeNotification` and a selector to call when the device orientation changes. Then, when you no longer need to know about orientation changes, call the default notification center’s [removeObserver:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/instm/NSNotificationCenter/removeObserver:) method to stop the notifications. Finally, call the [endGeneratingDeviceOrientationNotifications](https://developer.apple.com/documentation/uikit/uidevice/1620033-endgeneratingdeviceorientationno) method for the current device object to let the system know you don’t need the accelerometer anymore. See Listing 15-1.

__Listing 15-1__Starting and stopping orientation change notifications when a view appears and dismisses

Objective-C

1. `-(void) viewDidLoad {`
2. `// Turn on the accelerometer`
3. `[[UIDevice currentDevice] beginGeneratingDeviceOrientationNotifications];`
5. `//Register for orientation change notifications`
6. `[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(orientationChanged:) name:UIDeviceOrientationDidChangeNotification object:nil];`
7. `}`
9. `- (void)orientationChanged:(NSNotification *)notification {`
10. `// Respond to changes in orientation here`
11. `}`
13. `-(void) viewDidDisappear: (BOOL) animated {`
14. `// Stop receiving orientation change notifications`
15. `[[NSNotificationCenter defaultCenter] removeObserver:self];`
17. `// Turn off the accelerometer`
18. `[[UIDevice currentDevice] endGeneratingDeviceOrientationNotifications];`
19. `}`

Swift

1. `override func viewDidLoad() {`
2. `// Turn on the accelerometer`
3. `UIDevice.currentDevice.beginGeneratingDeviceOrientationNotifications()`
5. `//Register for orientation change notifications`
6. `NSNotificationCenter.defaultCenter().addObserver(self, selector: "orientationChanged:", name: UIDeviceOrientationDidChangeNotification, object: nil)`
7. `}`
9. `func orientationChanged(notification: NSNotification!) {`
10. `// Respond to changes in orientation here`
11. `}`
13. `override func viewDidDisappear(animated: Bool) {`
14. `// Stop receiving orientation change notifications`
15. `NSNotificationCenter.defaultCenter().removeObserver(self)`
17. `// Turn off the accelerometer`
18. `UIDevice.currentDevice().endGeneratingDeviceOrientationNotifications()`
19. `}`

> [!NOTE]
> 

### Request Fewer Continuous Motion Updates

The Core Motion framework provides APIs that let an app receive continuous motion updates in the form of accelerometer, gyroscope, and device motion (rotation, acceleration, and more) events. Once any of these APIs is initiated, the app can request motion updates at any time. It can also register to receive recurring updates.

Before registering for recurring updates, specify an interval that meets your app’s needs. The larger the interval, the fewer events are delivered to your app, improving battery life. Call any of the methods in Table 15-1 on the Core Motion Manager class ([CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)), and pass an interval of type [NSTimeInterval](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSTimeInterval).

__Table 15-1__Core Location Manager methods for specifying a recurring motion update interval

| Method | Description |
| --- | --- |
| [accelerometerUpdateInterval](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616135-accelerometerupdateinterval) | Call this method to set the interval for recurring accelerometer updates. |
| [gyroUpdateInterval](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616160-gyroupdateinterval) | Call this method to set the interval for recurring gyroscope updates. |
| [deviceMotionUpdateInterval](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616065-devicemotionupdateinterval) | Call this method to set the interval for recurring device motion updates. |

To enable continuous motion tracking, call any of the methods in Table 15-2 on the `CMMotionManager` class, depending on the requirements of your app.

__Table 15-2__Core Location Manager methods for enabling continuous motion tracking

| Method | Description |
| --- | --- |
| [startAccelerometerUpdates](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616171-startaccelerometerupdates) | Call this method to start recording accelerometer events. To request event details at any time, query the [accelerometerData](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1615992-accelerometerdata) property of the `CMMotionManager` class. |
| [startAccelerometerUpdatesToQueue:withHandler:](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616148-startaccelerometerupdatestoqueue) | Call this method to start recording accelerometer events and receiving updates. Pass it a processing handler to call at a recurring interval, and an operation queue on which to run the handler. |
| [startGyroUpdates](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616156-startgyroupdates) | Call this method to start recording gyroscope events. To request event details at any time, check the [gyroData](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616154-gyrodata) property of the `CMMotionManager` class. |
| [startGyroUpdatesToQueue:withHandler:](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616104-startgyroupdatestoqueue) | Call this method to start recording gyroscope events and receiving updates. Pass it a handler to call at a recurring interval, and an operation queue on which to run the handler. |
| [startDeviceMotionUpdates](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616110-startdevicemotionupdates) | Call this method to start recording device motion events. To request event details at any time, check the [deviceMotion](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616040-devicemotion) property of the `CMMotionManager` class. |
| [startDeviceMotionUpdatesToQueue:withHandler:](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616048-startdevicemotionupdatestoqueue) | Call this method to start recording device motion events and receiving updates. Pass it a handler to call at a recurring interval, and an operation queue on which to run the handler. |

When motion updates are no longer needed, make sure you explicitly stop the updates so the corresponding hardware can be powered down. Call any of the methods in Table 15-3 on the `CMMotionManager` class, as appropriate.

__Table 15-3__Core Location Manager methods for stopping continuous motion tracking

| Method | Description |
| --- | --- |
| [stopAccelerometerUpdates](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616138-stopaccelerometerupdates) | Call this method to stop receiving accelerometer updates. |
| [stopGyroUpdates](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616059-stopgyroupdates) | Call this method to stop receiving gyroscope updates. |
| [stopDeviceMotionUpdates](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616115-stopdevicemotionupdates) | Call this method to stop receiving device motion updates. |

Listing 15-2 demonstrates the techniques above by registering for and stopping recurring accelerometer updates.

__Listing 15-2__Registering for and stopping recurring accelerometer motion updates

Objective-C

1. `-(void) viewDidLoad {`
2. `[super viewDidLoad];`
4. `// Create a Core Motion Manager object`
5. `self.motionManager = [[CMMotionManager alloc] init];`
6. `}`
8. `- (void)startAccelerometerUpdates {`
9. `// Check whether the accelerometer is available`
10. `if ([self.motionManager isAccelerometerAvailable] == YES) {`
12. `// Update the recurring update interval`
13. `[self.motionManager setAccelerometerUpdateInterval:updateInterval];`
15. `// Start accelerometer updates`
16. `[self.motionManager startAccelerometerUpdatesToQueue:[NSOperationQueue mainQueue] withHandler:^(CMAccelerometerData *accelerometerData, NSError *error) {`
18. `// Handler to process accelerometer data`
20. `}];`
21. `}`
23. `}`
25. `- (void)stopUpdates {`
26. `// Check whether the accelerometer is available`
27. `if ([self.motionManager isAccelerometerActive] == YES) {`
29. `// Start accelerometer updates`
30. `[self.motionManager stopAccelerometerUpdates];`
32. `}`
33. `}`

Swift

1. `override func viewDidLoad() {`
2. `// Create a location manager object`
3. `self.motionManager = CMMotionManager()`
4. `}`
6. `func startAccelerometerUpdates() {`
7. `// Check whether the accelerometer is available`
8. `if self.motionManager.accelerometerAvailable {`
10. `// Update the recurring update interval`
11. `self.motionManager.accelerometerUpdateInterval = updateInterval`
13. `// Start accelerometer updates`
14. `self.motionManager.startAccelerometerUpdatesToQueue(NSOperationQueue.mainQueue()) { (accelerometerData: CMAccelerometerData!, error: NSError!) in`
16. `// Handler to process accelerometer data`
18. `}`
19. `}`
21. `}`
23. `func stopUpdates() {`
24. `// Check whether the accelerometer is available`
25. `if self.motionManager.accelerometerActive {`
27. `// Start accelerometer updates`
28. `self.motionManager.stopAccelerometerUpdates()`
30. `}`
31. `}`

> [!NOTE]
> 

[Reduce Location Accuracy and Duration](LocationBestPractices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmrufvjvomi)

[Notification Best Practices](NotificationBestPractices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmrwfvjvomi)
