---
title: Mocking Capabilities in the iOS Simulator
source: Saagar Jha
source_key: saagarjha
source_url: 'https://saagarjha.com/blog/2019/01/11/mocking-capabilities-in-the-ios-simulator/'
original_language: en
published: 2019-01-11
status: active
license: CC BY-SA 4.0 → 可再分发，但译文必须同样 BY-SA 并署名
archived_at: 2026-07-27
content_hash: 'sha256:03c0b924fcdc0a74'
translated: false
---

> 原文：[Mocking Capabilities in the iOS Simulator](https://saagarjha.com/blog/2019/01/11/mocking-capabilities-in-the-ios-simulator/)　·　Saagar Jha

# Mocking Capabilities in the iOS Simulator

Friday, January 11, 2019

The iOS Simulator, which ships as part of Xcode, gives developers a way to test their apps without needing to run them on a physical device. While the simulator’s fidelity in reproducing a real iOS device has slowly improved over the years, there are still a couple of differences in the two environments: although many of the system frameworks are quite similar across both, the iOS Simulator comes with a stripped-down set of applications; in addition, though features such as 3D Touch, location, and biometric authentication can be simulated, other sensors (including the camera, accelerometer, barometer, and magnetometer) are not emulated. Of course, the largest difference is that the iOS Simulator runs on a Mac, sharing the kernel with macOS but running in a separate Mach bootstrap context and its own set of processes (kicked off by launchd_sim). This makes the iOS Simulator _much_ easier to mess with: by relaxing protections in macOS–which, on production iOS hardware is designed to be impossible–we can make modifications that would usually require a jailbreak had they been performed on iOS.

In our case, we will be utilizing this flexibility, along with some quirks of the simulator, to grant the device it is emulating capabilities it does not have in real life. To be specific, we will be designing a “iPhone 9”: a device based on iPhone 8, but with Face ID capabilities. Outside of the simulator, this makes no sense due to iPhone lacking the requisite sensors, but since we are running on virtual hardware this is not an issue.

## Biometrics on iOS

While we don’t have time to go into the intricate details of how developers can implement Touch ID and Face ID in their apps, it’s still useful to go over some basics how the of the API works, since these will be relevant later. We can use this to create a small sample app to test whether our changes have any effect. At a high level, iOS apps interact with the system with the [LocalAuthentication](https://developer.apple.com/documentation/localauthentication) framework, and the majority of the functionality revolves around the [LAContext](https://developer.apple.com/documentation/localauthentication/lacontext) class. The first thing we should do is check whether we can use biometric authentication for this device:

```
var error: NSError?
let context = LAContext()
context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: &error)
print(error)
```

Excusing the unpleasant syntax (`LAContext.canEvaluatePolicy(_:error:)` takes an `NSErrorPointer` rather than throwing an error because it is annotated with `__attribute__((swift_error(none)))` for some reason), the code is relatively straightforward: the function returns a `Bool` indicating whether the device can successfully use biometric authentication, and if it cannot, `error` is populated. Error codes (defined in `LAError.Code`) of note are:

- `.biometryNotAvailable`: This device is missing the requisite hardware to perform biometric authentication.
- `.biometryNotEnrolled`: The device has not enrolled any fingerprints or faces. The iOS Simulator handles other errors, such as `.passcodeNotSet`, for us (since there isn’t a way to set a passcode!), but for this we need to enroll in the Hardware \> Touch ID (or Face ID, depending on your device).

After checking for the ability to evaluate the policy, we do the logical thing: evaluate it.

```
context.evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, localizedReason: "testing and stuff") { (success, error) in
	print(success, error)
}
```

Pretty simple. If you’re not getting a popup to authenticate, make sure you have a `NSFaceIDUsageDescription` key in your Info.plist (for Face ID, obviously) and a non-empty `localizedReason`: this is _not_ optional.

## The façade of LocalAuthentication

Given that the only API we have interacted with is from LocalAuthentication, it’s not unreasonable to conclude that this is where the checks for biometric hardware reside. However, quick look into the framework confirms that this is not the case: the majority of work is done in the coreauthd daemon (`/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`–inside the iOS root filesystem, of course), which advertises the Mach service `com.apple.CoreAuthentication.daemon` to which LocalAuthentication connects via XPC.

coreauthd itself is a rabbit hole of frameworks: the method of interest to us is `-[BiometryHelper deviceHasBiometryWithError:]` from DaemonUtils.framework (also inside the `Support` folder), which is loaded by MechanismBase.framework, which coreauthd links against. This method returns `YES` if it has a “device”, which it grabs by dynamically loading yet another framework, BiometricKit (in `/System/Library/PrivateFrameworks`) and calling `+[BKDeviceManager availableDevices:]` (using `NSClassFromString` (!)). A peek inside that method and we find a “touch-id” lookup that device creation is predicated on:

![Hopper disassembly of BiometricKit focused on +[BKDeviceManager availableDevices:]](https://saagarjha.com/blog/2019/01/11/mocking-capabilities-in-the-ios-simulator/HopperBiometricKit.png)

`MGGetBoolAnswer` is a function defined in MobileGestalt, and is used throughout iOS to look up hardware and software information to conditionally enable features–as we can see here, `MGGetBoolAnswer("touch-id")` returns `YES` if the current device has a Touch ID sensor. The other key, `"8olRm6C1xqr7AJGpLRnpSw"`, is a bit more mysterious, but it turns out to be the “obfuscated” MobileGestalt key for `"PearlIDCapability"`; a fact which we can quickly check by using [this handy list of deobfuscated keys](https://blog.timac.org/2018/1126-deobfuscated-libmobilegestalt-keys-ios-12/) (“pearl” referring the codename for Face ID, of course).

MobileGestalt is located at `/usr/lib/libMobileGestalt.dylib`. Since `MGGetBoolAnswer` seems to be able to let us know when we try to access an invalid key, it must have a list of keys inside of it; it’s easy to verify that the binary contains a list of “obfuscated” keys inside of it by running it through `strings`. Finding the key for `"touch-id"` (`"8Shl+AdVKo09f1Sldkb0kA"`) and walking through some cross-references and function calls leads us to this function:

![Hopper disassembly of a function inside of libMobileGestalt](https://saagarjha.com/blog/2019/01/11/mocking-capabilities-in-the-ios-simulator/HopperlibMobileGestalt.png)

It looks like MobileGestalt looks in its environment for `SIMULATOR_CAPABILITIES`, opens whatever it’s set to, and initializes capabilities from there. In hindsight, it seems pretty evident why this is included: the simulator must be able to simulate all possible capabilities, but it must also disable some of them when simulating certain devices. By setting `SIMULATOR_CAPABILITIES`, Xcode ensures that the correct device-specific capabilities are applied to the running device.

# Messing with the capabilities file

Now that we know where the simulator loads its configuration from, let’s see if we can modify it. First, we need to find the capabilities file, so let’s boot the iPhone 8 simulator and ask it where the file is:

```
$ xcrun simctl getenv booted SIMULATOR_CAPABILITIES
/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/Library/CoreSimulator/Profiles/DeviceTypes/iPhone 8.simdevicetype/Contents/Resources/capabilities.plist
```

Of course, it’s a standard property list, so we can should be able to check for the value of the “touch-id” key:

```
$ /usr/libexec/PlistBuddy -c "Print :capabilities:touch-id" "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/Library/CoreSimulator/Profiles/DeviceTypes/iPhone 8.simdevicetype/Contents/Resources/capabilities.plist"
true
```

Just like we expected. To test whether we can change these capabilities, let’s temporarily disable Touch ID. To avoid modifying the Xcode application bundle itself, let’s copy the capabilities file elsewhere and modify that:

```
$ cp "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/Library/CoreSimulator/Profiles/DeviceTypes/iPhone 8.simdevicetype/Contents/Resources/capabilities.plist" /tmp/capabilities.plist
$ /usr/libexec/PlistBuddy -c "Set :capabilities:touch-id false" /tmp/capabilities.plist
```

Now we need to tell the simulator to load our modified file. Unfortunately, `simctl` doesn’t have a “setenv” command; however, the help for `xcrun launch` has a particularly relevant tip:

```
$ xcrun simctl launch
Launch an application by identifier on a device.
Usage: simctl launch [-w | --wait-for-debugger] [--console|--console-pty] [--stdout=<path>] [--stderr=<path>] <device> <app identifier> [<argv 1> <argv 2> ... <argv n>]

	--console Block and print the application's stdout and stderr to the current terminal.
		Signals received by simctl are passed through to the application.
		(Cannot be combined with --stdout or --stderr)
	--console-pty Block and print the application's stdout and stderr to the current terminal via a PTY.
		Signals received by simctl are passed through to the application.
		(Cannot be combined with --stdout or --stderr)
	--stdout=<path> Redirect the application's standard output to a file.
	--stderr=<path> Redirect the application's standard error to a file.
		Note: Log output is often directed to stderr, not stdout.

If you want to set environment variables in the resulting environment, set them in the calling environment with a SIMCTL_CHILD_ prefix.
```

So, if we quit our simulator, set `SIMCTL_CHILD_SIMULATOR_CAPABILITIES` in our terminal, and relaunch the device from there using `simctl boot`, we should see our environment variable changed:

```
$ xcrun simctl shutdown "iPhone 8"
$ export SIMCTL_CHILD_SIMULATOR_CAPABILITIES=/tmp/capabilities.plist
$ xcrun simctl boot "iPhone 8"
$ xcrun simctl getenv booted SIMULATOR_CAPABILITIES
/tmp/capabilities.plist
```

Running the test code from before returns the `.biometryNotAvailable` error, as expected. Now, let’s go one step further, and set the value of the “pearl-id” key:

```
$ /usr/libexec/PlistBuddy -c "Add :capabilities:pearl-id bool true" /tmp/capabilities.plist
```

And the results:

![Face ID prompt on the iPhone 8 simulator](https://saagarjha.com/blog/2019/01/11/mocking-capabilities-in-the-ios-simulator/SimulatorFaceID.png)
