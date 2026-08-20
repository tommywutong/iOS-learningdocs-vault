---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/WatchKit.html
archived_at: '2026-07-18T02:56:28.789808Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# WatchKit Changes

## WatchKit

Modified WKAccessibilityImageRegion.label

|  | Declaration |
| --- | --- |
| From | ``` var label: String! ``` |
| To | ``` var label: String ``` |

Modified WKInterfaceButton.setBackgroundColor(UIColor?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setBackgroundColor(_ color: UIColor!) ``` | iOS 8.2 |
| To | ``` func setBackgroundColor(_ color: UIColor?) ``` | iOS 8.3 |

Modified WKInterfaceController.init()

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init() ``` |

Modified WKInterfaceController.handleUserActivity([NSObject: AnyObject]?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func handleUserActivity(_ userInfo: [NSObject : AnyObject]!) ``` | iOS 8.2 |
| To | ``` func handleUserActivity(_ userInfo: [NSObject : AnyObject]?) ``` | iOS 8.3 |

Modified WKInterfaceController.openParentApplication([NSObject: AnyObject], reply:(([NSObject: AnyObject]!, NSError!) -> Void)?) -> Bool [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func openParentApplication(_ userInfo: [NSObject : AnyObject]!, reply reply: (([NSObject : AnyObject]!, NSError!) -> Void)!) -> Bool ``` | iOS 8.2 |
| To | ``` class func openParentApplication(_ userInfo: [NSObject : AnyObject], reply reply: (([NSObject : AnyObject]!, NSError!) -> Void)?) -> Bool ``` | iOS 8.3 |

Modified WKInterfaceController.presentTextInputControllerWithSuggestions([AnyObject]?, allowedInputMode: WKTextInputMode, completion:([AnyObject]!) -> Void)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func presentTextInputControllerWithSuggestions(_ suggestions: [AnyObject]!, allowedInputMode inputMode: WKTextInputMode, completion completion: (([AnyObject]!) -> Void)!) ``` | iOS 8.2 |
| To | ``` func presentTextInputControllerWithSuggestions(_ suggestions: [AnyObject]?, allowedInputMode inputMode: WKTextInputMode, completion completion: ([AnyObject]!) -> Void) ``` | iOS 8.3 |

Modified WKInterfaceController.reloadRootControllersWithNames([AnyObject], contexts:[AnyObject]?) [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func reloadRootControllersWithNames(_ names: [AnyObject]!, contexts contexts: [AnyObject]!) ``` | iOS 8.2 |
| To | ``` class func reloadRootControllersWithNames(_ names: [AnyObject], contexts contexts: [AnyObject]?) ``` | iOS 8.3 |

Modified WKInterfaceController.updateUserActivity(String, userInfo:[NSObject: AnyObject]?, webpageURL: NSURL?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func updateUserActivity(_ type: String!, userInfo userInfo: [NSObject : AnyObject]!, webpageURL webpageURL: NSURL!) ``` | iOS 8.2 |
| To | ``` func updateUserActivity(_ type: String, userInfo userInfo: [NSObject : AnyObject]?, webpageURL webpageURL: NSURL?) ``` | iOS 8.3 |

Modified WKInterfaceDevice.cachedImages

|  | Declaration |
| --- | --- |
| From | ``` var cachedImages: [NSObject : AnyObject]! { get } ``` |
| To | ``` var cachedImages: [NSObject : AnyObject] { get } ``` |

Modified WKInterfaceImage.setTintColor(UIColor?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setTintColor(_ tintColor: UIColor!) ``` | iOS 8.2 |
| To | ``` func setTintColor(_ tintColor: UIColor?) ``` | iOS 8.3 |

Modified WKInterfaceMap.addAnnotation(CLLocationCoordinate2D, withImage: UIImage?, centerOffset: CGPoint)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func addAnnotation(_ location: CLLocationCoordinate2D, withImage image: UIImage!, centerOffset offset: CGPoint) ``` | iOS 8.2 |
| To | ``` func addAnnotation(_ location: CLLocationCoordinate2D, withImage image: UIImage?, centerOffset offset: CGPoint) ``` | iOS 8.3 |

Modified WKInterfaceMap.addAnnotation(CLLocationCoordinate2D, withImageNamed: String?, centerOffset: CGPoint)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func addAnnotation(_ location: CLLocationCoordinate2D, withImageNamed name: String!, centerOffset offset: CGPoint) ``` | iOS 8.2 |
| To | ``` func addAnnotation(_ location: CLLocationCoordinate2D, withImageNamed name: String?, centerOffset offset: CGPoint) ``` | iOS 8.3 |

Modified WKInterfaceObject.setAccessibilityImageRegions([AnyObject])

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setAccessibilityImageRegions(_ accessibilityImageRegions: [AnyObject]!) ``` | iOS 8.2 |
| To | ``` func setAccessibilityImageRegions(_ accessibilityImageRegions: [AnyObject]) ``` | iOS 8.3 |

Modified WKInterfaceSwitch.setAttributedTitle(NSAttributedString?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setAttributedTitle(_ attributedTitle: NSAttributedString!) ``` | iOS 8.2 |
| To | ``` func setAttributedTitle(_ attributedTitle: NSAttributedString?) ``` | iOS 8.3 |

Modified WKInterfaceSwitch.setColor(UIColor?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setColor(_ color: UIColor!) ``` | iOS 8.2 |
| To | ``` func setColor(_ color: UIColor?) ``` | iOS 8.3 |

Modified WKInterfaceSwitch.setTitle(String?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setTitle(_ title: String!) ``` | iOS 8.2 |
| To | ``` func setTitle(_ title: String?) ``` | iOS 8.3 |

Modified WatchKitErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let WatchKitErrorDomain: NSString! ``` |
| To | ``` let WatchKitErrorDomain: String ``` |

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
