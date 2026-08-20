---
title: Magic Mouse Developer Release Notes
apple_id: TP40009300
resource_type: Release Note
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: null
published: '2009-10-20'
source_url: https://developer.apple.com/library/archive/releasenotes/DriversKernelHardware/RN-MagicMouse/index.html
archived_at: '2026-07-18T02:50:30.952666Z'
---
> 导航：[总目录](../README.md) · [releasenotes](../_indexes/releasenotes.md)



# Magic Mouse Developer Release Notes

### Opting Out of Momentum Scroll Events

After the user physically stops scrolling a view, the device can synthesize and generate momentum scroll events to simulate the scrolling motion slowly coming to a stop. These events are dispatched via the usual delivery mechanism to the view that is under the mouse pointer when the user made his or her last scrolling action.

Some applications do not work well with momentum scroll events because of the quantity and magnitude of these events. These applications can opt out of this feature by turning off the `AppleMomentumScrollSupported` default in the user defaults system. The application should disable this feature immediately after it launches.

In a Cocoa application, for example, you could add the following code to an [initialize](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/initialize) class method in the class that handles scroll events:

```objc
+ (void)initialize {
    NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
    NSDictionary *appDefaults = [NSDictionary dictionaryWithObject:@"NO"
       forKey:@"AppleMomentumScrollSupported"];
    [defaults registerDefaults:appDefaults];
}
```

Carbon applications can include the same user-defaults code but should put it in early initialization routines such as the `main` function, as in this example:

```objc
#import <Foundation/Foundation.h>

int main(int argc, char *argv[])
{
    NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
    NSDictionary *appDefaults = [NSDictionary dictionaryWithObject:@"NO"
       forKey:@"AppleMomentumScrollSupported"];
    [defaults registerDefaults:appDefaults];

    // other code goes here
}
```
