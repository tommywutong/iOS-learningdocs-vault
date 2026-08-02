---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/IOBluetoothUI.html
archived_at: '2026-07-18T02:54:28.984519Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# IOBluetoothUI Changes

## IOBluetoothUI

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

IOBluetoothDeviceSelectorController.hRemoved -[IOBluetoothDeviceSelectorController runPanelWithAttributes:]Modified [-[IOBluetoothDeviceSelectorController getDeviceSelectorControllerRef]](https://developer.apple.com/documentation/iobluetoothui/iobluetoothdeviceselectorcontroller/1574309-getdeviceselectorcontrollerref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [+[IOBluetoothDeviceSelectorController withDeviceSelectorControllerRef:]](https://developer.apple.com/documentation/iobluetoothui/iobluetoothdeviceselectorcontroller/1574310-withdeviceselectorcontrollerref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

IOBluetoothPairingController.hRemoved -[IOBluetoothPairingController runPanelWithAttributes:]Modified [+[IOBluetoothPairingController withPairingControllerRef:]](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpairingcontroller/1468733-withpairingcontrollerref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[IOBluetoothPairingController getPairingControllerRef]](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpairingcontroller/1468766-getpairingcontrollerref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

IOBluetoothPasskeyDisplay.hAdded [IOBluetoothAccessibilityIgnoredImageCell](https://developer.apple.com/documentation/iobluetoothui/iobluetoothaccessibilityignoredimagecell)Added [IOBluetoothAccessibilityIgnoredTextFieldCell](https://developer.apple.com/documentation/iobluetoothui/iobluetoothaccessibilityignoredtextfieldcell)Added [IOBluetoothPasskeyDisplay](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpasskeydisplay)Added [-[IOBluetoothPasskeyDisplay advancePasskeyIndicator]](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpasskeydisplay/1516412-advancepasskeyindicator)Added [-[IOBluetoothPasskeyDisplay resetAll]](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpasskeydisplay/1539786-resetall)Added [-[IOBluetoothPasskeyDisplay resetPasskeyIndicator]](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpasskeydisplay/1516528-resetpasskeyindicator)Added [-[IOBluetoothPasskeyDisplay retreatPasskeyIndicator]](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpasskeydisplay/1516384-retreatpasskeyindicator)Added [IOBluetoothPasskeyDisplay.returnHighlightImage](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpasskeydisplay/1516533-returnhighlightimage)Added [IOBluetoothPasskeyDisplay.returnImage](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpasskeydisplay/1516380-returnimage)Added [-[IOBluetoothPasskeyDisplay setPasskeyIndicatorEnabled:]](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpasskeydisplay/1539774-setpasskeyindicatorenabled)Added [-[IOBluetoothPasskeyDisplay setPasskeyString:]](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpasskeydisplay/1539781-setpasskeystring)Added -[IOBluetoothPasskeyDisplay setReturnType:]Added [-[IOBluetoothPasskeyDisplay setupUIForDevice:]](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpasskeydisplay/1539771-setupuifordevice)Added [+[IOBluetoothPasskeyDisplay sharedDisplayView]](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpasskeydisplay/1516546-shareddisplayview)Added [BluetoothKeyboardReturnType](https://developer.apple.com/documentation/iobluetoothui/bluetoothkeyboardreturntype)Added [kBluetoothKeyboardANSIReturn](https://developer.apple.com/documentation/iobluetoothui/bluetoothkeyboardreturntype/kbluetoothkeyboardansireturn)Added [kBluetoothKeyboardISOReturn](https://developer.apple.com/documentation/iobluetoothui/bluetoothkeyboardreturntype/kbluetoothkeyboardisoreturn)Added [kBluetoothKeyboardJISReturn](https://developer.apple.com/documentation/iobluetoothui/bluetoothkeyboardreturntype/kbluetoothkeyboardjisreturn)IOBluetoothUIUserLib.hAdded [IOBluetoothValidateHardwareWithDescription()](https://developer.apple.com/documentation/iobluetoothui/1411859-iobluetoothvalidatehardwarewithd) (no architecture available)Modified [IOBluetoothPairingControllerRunPanelWithAttributes()](https://developer.apple.com/documentation/iobluetoothui/1411860-iobluetoothpairingcontrollerrunp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [IOBluetoothDeviceSelectorRunPanelWithAttributes()](https://developer.apple.com/documentation/iobluetoothui/1411872-iobluetoothdeviceselectorrunpane)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [IOBluetoothServiceBrowserControllerBrowseDevices()](https://developer.apple.com/documentation/iobluetoothui/1411887-iobluetoothservicebrowsercontrol)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [IOBluetoothServiceBrowserControllerSetOptions()](https://developer.apple.com/documentation/iobluetoothui/1411863-iobluetoothservicebrowsercontrol)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [IOBluetoothServiceBrowserControllerCreate()](https://developer.apple.com/documentation/iobluetoothui/1411881-iobluetoothservicebrowsercontrol)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [IOBluetoothServiceBrowserControllerDiscoverWithDeviceAttributes()](https://developer.apple.com/documentation/iobluetoothui/1411877-iobluetoothservicebrowsercontrol)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [IOBluetoothValidateHardware()](https://developer.apple.com/documentation/iobluetoothui/1411871-iobluetoothvalidatehardware)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [IOBluetoothServiceBrowserControllerDiscover()](https://developer.apple.com/documentation/iobluetoothui/1411875-iobluetoothservicebrowsercontrol)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
