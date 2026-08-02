---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/ScriptingBridge.html
archived_at: '2026-07-18T02:53:42.116444Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# ScriptingBridge Changes for Swift

### ScriptingBridge

Removed SBApplication.applicationWithBundleIdentifier(_: String!) -> AnyObject! [class]Removed SBApplication.applicationWithProcessIdentifier(_: pid_t) -> AnyObject! [class]Removed SBApplication.applicationWithURL(_: NSURL!) -> AnyObject! [class]Modified [SBApplication](https://developer.apple.com/documentation/scriptingbridge/sbapplication)

|  | Declaration |
| --- | --- |
| From | ``` class SBApplication : SBObject, NSCoding {     init!(bundleIdentifier ident: String!)     init!(URL url: NSURL!)     init!(processIdentifier pid: pid_t)     class func applicationWithBundleIdentifier(_ ident: String!) -> AnyObject!     class func applicationWithURL(_ url: NSURL!) -> AnyObject!     class func applicationWithProcessIdentifier(_ pid: pid_t) -> AnyObject!     func classForScriptingClass(_ className: String!) -> AnyClass!     var running: Bool { get }     func activate()     var delegate: SBApplicationDelegate!     var launchFlags: LSLaunchFlags     var sendMode: AESendMode     var timeout: Int } ``` |
| To | ``` class SBApplication : SBObject {     init?(bundleIdentifier ident: String)     init?(URL url: NSURL)     init?(processIdentifier pid: pid_t)     class func applicationWithBundleIdentifier(_ ident: String) -> SBApplication?     class func applicationWithURL(_ url: NSURL) -> SBApplication?     class func applicationWithProcessIdentifier(_ pid: pid_t) -> SBApplication?     func classForScriptingClass(_ className: String) -> AnyClass?     var running: Bool { get }     func activate()     var delegate: SBApplicationDelegate?     var launchFlags: LSLaunchFlags     var sendMode: AESendMode     var timeout: Int } ``` |

Modified [SBApplication.classForScriptingClass(_: String) -> AnyClass?](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1423987-classforscriptingclass)

|  | Declaration |
| --- | --- |
| From | ``` func classForScriptingClass(_ className: String!) -> AnyClass! ``` |
| To | ``` func classForScriptingClass(_ className: String) -> AnyClass? ``` |

Modified [SBApplication.delegate](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1423983-delegate)

|  | Declaration |
| --- | --- |
| From | ``` var delegate: SBApplicationDelegate! ``` |
| To | ``` var delegate: SBApplicationDelegate? ``` |

Modified [SBApplication.init(bundleIdentifier: String)](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1424009-initwithbundleidentifier)

|  | Declaration |
| --- | --- |
| From | ``` init!(bundleIdentifier ident: String!) ``` |
| To | ``` init?(bundleIdentifier ident: String) ``` |

Modified [SBApplication.init(processIdentifier: pid_t)](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1424001-initwithprocessidentifier)

|  | Declaration |
| --- | --- |
| From | ``` init!(processIdentifier pid: pid_t) ``` |
| To | ``` init?(processIdentifier pid: pid_t) ``` |

Modified [SBApplication.init(URL: NSURL)](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1423947-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` init!(URL url: NSURL!) ``` |
| To | ``` init?(URL url: NSURL) ``` |

Modified [SBApplicationDelegate](https://developer.apple.com/documentation/scriptingbridge/sbapplicationdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol SBApplicationDelegate {     func eventDidFail(_ event: UnsafePointer<AppleEvent>, withError error: NSError!) -> AnyObject! } ``` |
| To | ``` protocol SBApplicationDelegate {     func eventDidFail(_ event: UnsafePointer<AppleEvent>, withError error: NSError) -> AnyObject } ``` |

Modified [SBApplicationDelegate.eventDidFail(_: UnsafePointer<AppleEvent>, withError: NSError) -> AnyObject](https://developer.apple.com/documentation/scriptingbridge/sbapplicationdelegate/1424011-eventdidfail)

|  | Declaration |
| --- | --- |
| From | ``` func eventDidFail(_ event: UnsafePointer<AppleEvent>, withError error: NSError!) -> AnyObject! ``` |
| To | ``` func eventDidFail(_ event: UnsafePointer<AppleEvent>, withError error: NSError) -> AnyObject ``` |

Modified [SBElementArray](https://developer.apple.com/documentation/scriptingbridge/sbelementarray)

|  | Declaration |
| --- | --- |
| From | ``` class SBElementArray : NSMutableArray {     func objectWithName(_ name: String!) -> AnyObject!     func objectWithID(_ identifier: AnyObject!) -> AnyObject!     func objectAtLocation(_ location: AnyObject!) -> AnyObject!     func arrayByApplyingSelector(_ selector: Selector) -> [AnyObject]!     func arrayByApplyingSelector(_ aSelector: Selector, withObject argument: AnyObject!) -> [AnyObject]!     func get() -> [AnyObject]! } ``` |
| To | ``` class SBElementArray : NSMutableArray {     func objectWithName(_ name: String) -> AnyObject     func objectWithID(_ identifier: AnyObject) -> AnyObject     func objectAtLocation(_ location: AnyObject) -> AnyObject     func arrayByApplyingSelector(_ selector: Selector) -> [AnyObject]     func arrayByApplyingSelector(_ aSelector: Selector, withObject argument: AnyObject) -> [AnyObject]     func get() -> [AnyObject]? } ``` |

Modified [SBElementArray.arrayByApplyingSelector(_: Selector) -> [AnyObject]](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423951-arraybyapplyingselector)

|  | Declaration |
| --- | --- |
| From | ``` func arrayByApplyingSelector(_ selector: Selector) -> [AnyObject]! ``` |
| To | ``` func arrayByApplyingSelector(_ selector: Selector) -> [AnyObject] ``` |

Modified [SBElementArray.arrayByApplyingSelector(_: Selector, withObject: AnyObject) -> [AnyObject]](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1424007-arraybyapplyingselector)

|  | Declaration |
| --- | --- |
| From | ``` func arrayByApplyingSelector(_ aSelector: Selector, withObject argument: AnyObject!) -> [AnyObject]! ``` |
| To | ``` func arrayByApplyingSelector(_ aSelector: Selector, withObject argument: AnyObject) -> [AnyObject] ``` |

Modified [SBElementArray.get() -> [AnyObject]?](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423997-get)

|  | Declaration |
| --- | --- |
| From | ``` func get() -> [AnyObject]! ``` |
| To | ``` func get() -> [AnyObject]? ``` |

Modified [SBElementArray.objectAtLocation(_: AnyObject) -> AnyObject](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423963-object)

|  | Declaration |
| --- | --- |
| From | ``` func objectAtLocation(_ location: AnyObject!) -> AnyObject! ``` |
| To | ``` func objectAtLocation(_ location: AnyObject) -> AnyObject ``` |

Modified [SBElementArray.objectWithID(_: AnyObject) -> AnyObject](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423985-objectwithid)

|  | Declaration |
| --- | --- |
| From | ``` func objectWithID(_ identifier: AnyObject!) -> AnyObject! ``` |
| To | ``` func objectWithID(_ identifier: AnyObject) -> AnyObject ``` |

Modified [SBElementArray.objectWithName(_: String) -> AnyObject](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423971-objectwithname)

|  | Declaration |
| --- | --- |
| From | ``` func objectWithName(_ name: String!) -> AnyObject! ``` |
| To | ``` func objectWithName(_ name: String) -> AnyObject ``` |

Modified [SBObject](https://developer.apple.com/documentation/scriptingbridge/sbobject)

|  | Declaration |
| --- | --- |
| From | ``` class SBObject : NSObject, NSCoding {     init!()     init!(properties properties: [NSObject : AnyObject]!)     init!(data data: AnyObject!)     func get() -> AnyObject!     func lastError() -> NSError! } extension SBObject {     init!(elementCode code: DescType, properties properties: [NSObject : AnyObject]!, data data: AnyObject!)     func propertyWithCode(_ code: AEKeyword) -> SBObject!     func propertyWithClass(_ cls: AnyClass!, code code: AEKeyword) -> SBObject!     func elementArrayWithCode(_ code: DescType) -> SBElementArray!     func setTo(_ value: AnyObject!) } ``` |
| To | ``` class SBObject : NSObject, NSCoding {     init()     init(properties properties: [NSObject : AnyObject])     init(data data: AnyObject)     func get() -> AnyObject?     func lastError() -> NSError? } extension SBObject {     init(elementCode code: DescType, properties properties: [String : AnyObject]?, data data: AnyObject?)     func propertyWithCode(_ code: AEKeyword) -> SBObject     func propertyWithClass(_ cls: AnyClass, code code: AEKeyword) -> SBObject     func elementArrayWithCode(_ code: DescType) -> SBElementArray     func setTo(_ value: AnyObject?) } ``` |

Modified [SBObject.elementArrayWithCode(_: DescType) -> SBElementArray](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423995-elementarray)

|  | Declaration |
| --- | --- |
| From | ``` func elementArrayWithCode(_ code: DescType) -> SBElementArray! ``` |
| To | ``` func elementArrayWithCode(_ code: DescType) -> SBElementArray ``` |

Modified [SBObject.get() -> AnyObject?](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423965-get)

|  | Declaration |
| --- | --- |
| From | ``` func get() -> AnyObject! ``` |
| To | ``` func get() -> AnyObject? ``` |

Modified [SBObject.init()](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423993-init)

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init() ``` |

Modified [SBObject.init(data: AnyObject)](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423961-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` init!(data data: AnyObject!) ``` |
| To | ``` init(data data: AnyObject) ``` |

Modified [SBObject.init(elementCode: DescType, properties: [String : AnyObject]?, data: AnyObject?)](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423999-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(elementCode code: DescType, properties properties: [NSObject : AnyObject]!, data data: AnyObject!) ``` |
| To | ``` init(elementCode code: DescType, properties properties: [String : AnyObject]?, data data: AnyObject?) ``` |

Modified [SBObject.init(properties: [NSObject : AnyObject])](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423973-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(properties properties: [NSObject : AnyObject]!) ``` |
| To | ``` init(properties properties: [NSObject : AnyObject]) ``` |

Modified [SBObject.lastError() -> NSError?](https://developer.apple.com/documentation/scriptingbridge/sbobject/1424005-lasterror)

|  | Declaration |
| --- | --- |
| From | ``` func lastError() -> NSError! ``` |
| To | ``` func lastError() -> NSError? ``` |

Modified [SBObject.propertyWithClass(_: AnyClass, code: AEKeyword) -> SBObject](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423977-propertywithclass)

|  | Declaration |
| --- | --- |
| From | ``` func propertyWithClass(_ cls: AnyClass!, code code: AEKeyword) -> SBObject! ``` |
| To | ``` func propertyWithClass(_ cls: AnyClass, code code: AEKeyword) -> SBObject ``` |

Modified [SBObject.propertyWithCode(_: AEKeyword) -> SBObject](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423975-propertywithcode)

|  | Declaration |
| --- | --- |
| From | ``` func propertyWithCode(_ code: AEKeyword) -> SBObject! ``` |
| To | ``` func propertyWithCode(_ code: AEKeyword) -> SBObject ``` |

Modified [SBObject.setTo(_: AnyObject?)](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423967-setto)

|  | Declaration |
| --- | --- |
| From | ``` func setTo(_ value: AnyObject!) ``` |
| To | ``` func setTo(_ value: AnyObject?) ``` |

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
