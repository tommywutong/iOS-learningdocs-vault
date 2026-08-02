---
title: Adding Bluetooth LE MIDI Support
apple_id: DTS40015045
resource_type: QA
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: CoreMIDI
published: '2014-11-11'
source_url: https://developer.apple.com/library/archive/qa/qa1831/_index.html
archived_at: '2026-07-18T02:35:06.171616Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1831

# Adding Bluetooth LE MIDI Support

## Q:  How can I add Bluetooth LE MIDI support to my application?

A: With the release of iOS 8 and OS X Yosemite, sending and receiving MIDI data is supported using Bluetooth Low Energy connections on any iOS device or Mac that has native Bluetooth Low Energy support. All established connections are secure which means that pairing is enforced and connections cannot be made to your devices without your explicit consent.

After a connection is established, it simply appears as an ordinary MIDI device that any MIDI application can communicate with.

There are two key roles involved in a Bluetooth connection; the __Central__ and the __Peripheral__. In order to have a Bluetooth connection one Central and a minimum of one Peripheral device is required.

The Peripheral's job is to become discoverable and advertise that it has some functionality you can connect to. For Bluetooth MIDI, the peripheral side will advertise its MIDI capabilities. The Central may scan for a Peripheral device that is advertising MIDI capability and then establish a connection.

After a Bluetooth connection has been established, MIDI data can be transferred bi-directionally between the Central and the Peripheral. Both iOS devices and Macs can play either role allowing Mac to Mac, iOS to iOS, Mac to iOS or iOS to Mac connections.

The Audio MIDI Setup applications provides a Bluetooth configuration icon in the MIDI Studio Panel (see Figure 1) that allows a Mac to play the role of either Central or Peripheral.

Double clicking the Bluetooth configuration icon will open a new window (see Figure 2). This window will allow you to play either the Central or the Peripheral role. In the top part of this window (this is the Peripheral view) click the __Advertise__ button to become discoverable. This will allow the Mac to take on the role of Peripheral. When advertising, the buttons name will change to __Stop Advertising__ which can be pressed to stop discoverability.

In the bottom part of the window (this is the Central view) you can connect to a device advertising MIDI functionality allowing the Mac to take on the role of Central. Once the pairing happens, a new MIDI device will appear in the setup and any application making use of MIDI devices will be able to see the device and communicate with it.

__Figure 1__  Audio MIDI Setup MIDI Studio panel showing Bluetooth Configuration Icon.

!!

__Figure 2__  Audio MIDI Setup Bluetooth Configuration Window.

!

There are two view controller objects which are part of the CoreAudioKit framework that can be used to manage Bluetooth MIDI connections on iOS. Both of these Bluetooth MIDI view controllers inherit from `UIViewController`.

`CABTMIDICentralViewController` allows an application to play the role of the Central, which means the application can scan and connect to a Peripheral device.

`CABTMIDILocalPeripheralViewController` allows an application to play the role of Peripheral, which allows the application to advertise its services and wait for a connection.

The code in Listings 1 and 2 demonstrate how these view controllers can be displayed. The techniques shown may be used interchangeably with both view controllers. Please see the [View Controller Programming Guide for iOS](https://developer.apple.com/library/ios/featuredarticles/ViewControllerPGforiPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007457-CH1-SW1) for more information.

__Listing 1__  Presenting a CABTMIDICentralViewController

```objc
- (void)doneAction:(id)sender
{
    [self dismissViewControllerAnimated:YES completion:nil];
}

- (IBAction)configureCentral:(id)sender
{
    CABTMIDICentralViewController *viewController = [CABTMIDICentralViewController new];

    UINavigationController *navController = [[UINavigationController alloc] initWithRootViewController:viewController];

    // this will present a view controller as a popover in iPad and modal VC on iPhone
    viewController.navigationItem.rightBarButtonItem =
        [[UIBarButtonItem alloc] initWithBarButtonSystemItem:UIBarButtonSystemItemDone
                                                      target:self
                                                      action:@selector(doneAction:)];

    navController.modalPresentationStyle = UIModalPresentationPopover;

    UIPopoverPresentationController *popC = navController.popoverPresentationController;
    popC.permittedArrowDirections = UIPopoverArrowDirectionAny;
    popC.sourceRect = [sender frame];

    UIButton *button = (UIButton *)sender;
    popC.sourceView = button.superview;

    [self presentViewController:navController animated:YES completion:nil];
}
```


__Listing 2__  Pushing a CABTMIDILocalPeripheralViewController

```objc
- (IBAction)configureLocalPeripheral:(UIButton *)sender {
    CABTMIDILocalPeripheralViewController *viewController = [[CABTMIDILocalPeripheralViewController alloc] init];
    [self.navigationController pushViewController: viewController animated:YES];
}
```


[What's New In Core Audio - WWDC 2014 Session 501](https://developer.apple.com/videos/wwdc/2014/#501)

[View Controller Programming Guide for iOS](https://developer.apple.com/library/ios/featuredarticles/ViewControllerPGforiPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007457-CH1-SW1)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-11-11 | New document that summarizes how to use Bluetooth LE MIDI starting with iOS 8 and OS X 10.10 |

