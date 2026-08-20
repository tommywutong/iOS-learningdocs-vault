---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/OSAKit.html
archived_at: '2026-07-18T02:52:34.216206Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# OSAKit Changes

## OSAKit

Removed OSALanguageFeatures.valueRemoved OSAStorageOptions.valueAdded OSALanguageFeatures.init(rawValue: UInt)Added OSAStorageOptions.init(rawValue: UInt)Modified OSALanguage.init(component: Component)

|  | Declaration |
| --- | --- |
| From | ``` init(component component: Component) ``` |
| To | ``` init!(component component: Component) ``` |

Modified OSALanguage.init(forName: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(forName name: String!) -> OSALanguage ``` |
| To | ``` init!(forName name: String!) -> OSALanguage ``` |

Modified OSALanguage.init(forScriptDataDescriptor: NSAppleEventDescriptor!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(forScriptDataDescriptor descriptor: NSAppleEventDescriptor!) -> OSALanguage ``` | OS X 10.10 |
| To | ``` init!(forScriptDataDescriptor descriptor: NSAppleEventDescriptor!) -> OSALanguage ``` | OS X 10.6 |

Modified OSALanguage.sharedLanguageInstance() -> OSALanguageInstance!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified OSALanguage.threadSafe

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified OSALanguageFeatures [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OSALanguageFeatures : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var SupportsCompiling: OSALanguageFeatures { get }     static var SupportsGetSource: OSALanguageFeatures { get }     static var SupportsAECoercion: OSALanguageFeatures { get }     static var SupportsAESending: OSALanguageFeatures { get }     static var SupportsRecording: OSALanguageFeatures { get }     static var SupportsConvenience: OSALanguageFeatures { get }     static var SupportsDialects: OSALanguageFeatures { get }     static var SupportsEventHandling: OSALanguageFeatures { get } } ``` | RawOptionSet |
| To | ``` struct OSALanguageFeatures : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var SupportsCompiling: OSALanguageFeatures { get }     static var SupportsGetSource: OSALanguageFeatures { get }     static var SupportsAECoercion: OSALanguageFeatures { get }     static var SupportsAESending: OSALanguageFeatures { get }     static var SupportsRecording: OSALanguageFeatures { get }     static var SupportsConvenience: OSALanguageFeatures { get }     static var SupportsDialects: OSALanguageFeatures { get }     static var SupportsEventHandling: OSALanguageFeatures { get } } ``` | RawOptionSetType |

Modified OSALanguageFeatures.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified OSALanguageInstance.init(language: OSALanguage!)

|  | Declaration |
| --- | --- |
| From | ``` init(language language: OSALanguage!) ``` |
| To | ``` init!(language language: OSALanguage!) ``` |

Modified OSAScript.compileAndReturnError(AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func compileAndReturnError(_ errorInfo: AutoreleasingUnsafePointer<NSDictionary?>) -> Bool ``` |
| To | ``` func compileAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool ``` |

Modified OSAScript.init(compiledData: NSData!, fromURL: NSURL!, usingStorageOptions: OSAStorageOptions, error: NSErrorPointer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(compiledData data: NSData!, fromURL url: NSURL!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: NSErrorPointer) ``` | OS X 10.10 |
| To | ``` init!(compiledData data: NSData!, fromURL url: NSURL!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: NSErrorPointer) ``` | OS X 10.6 |

Modified OSAScript.compiledDataForType(String!, usingStorageOptions: OSAStorageOptions, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSData!

|  | Declaration |
| --- | --- |
| From | ``` func compiledDataForType(_ type: String!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: AutoreleasingUnsafePointer<NSDictionary?>) -> NSData! ``` |
| To | ``` func compiledDataForType(_ type: String!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSData! ``` |

Modified OSAScript.init(contentsOfURL: NSURL!, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfURL url: NSURL!, error errorInfo: AutoreleasingUnsafePointer<NSDictionary?>) ``` |
| To | ``` init!(contentsOfURL url: NSURL!, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) ``` |

Modified OSAScript.init(contentsOfURL: NSURL!, languageInstance: OSALanguageInstance!, usingStorageOptions: OSAStorageOptions, error: NSErrorPointer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(contentsOfURL url: NSURL!, languageInstance instance: OSALanguageInstance!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: NSErrorPointer) ``` | OS X 10.10 |
| To | ``` init!(contentsOfURL url: NSURL!, languageInstance instance: OSALanguageInstance!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: NSErrorPointer) ``` | OS X 10.6 |

Modified OSAScript.executeAndReturnDisplayValue(AutoreleasingUnsafeMutablePointer<NSAttributedString?>, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor!

|  | Declaration |
| --- | --- |
| From | ``` func executeAndReturnDisplayValue(_ displayValue: AutoreleasingUnsafePointer<NSAttributedString?>, error errorInfo: AutoreleasingUnsafePointer<NSDictionary?>) -> NSAppleEventDescriptor! ``` |
| To | ``` func executeAndReturnDisplayValue(_ displayValue: AutoreleasingUnsafeMutablePointer<NSAttributedString?>, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor! ``` |

Modified OSAScript.executeAndReturnError(AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor!

|  | Declaration |
| --- | --- |
| From | ``` func executeAndReturnError(_ errorInfo: AutoreleasingUnsafePointer<NSDictionary?>) -> NSAppleEventDescriptor! ``` |
| To | ``` func executeAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor! ``` |

Modified OSAScript.executeAppleEvent(NSAppleEventDescriptor!, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor!

|  | Declaration |
| --- | --- |
| From | ``` func executeAppleEvent(_ event: NSAppleEventDescriptor!, error errorInfo: AutoreleasingUnsafePointer<NSDictionary?>) -> NSAppleEventDescriptor! ``` |
| To | ``` func executeAppleEvent(_ event: NSAppleEventDescriptor!, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor! ``` |

Modified OSAScript.executeHandlerWithName(String!, arguments:[AnyObject]!, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor!

|  | Declaration |
| --- | --- |
| From | ``` func executeHandlerWithName(_ name: String!, arguments arguments: [AnyObject]!, error errorInfo: AutoreleasingUnsafePointer<NSDictionary?>) -> NSAppleEventDescriptor! ``` |
| To | ``` func executeHandlerWithName(_ name: String!, arguments arguments: [AnyObject]!, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor! ``` |

Modified OSAScript.languageInstance

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified OSAScript.richTextSource

|  | Declaration |
| --- | --- |
| From | ``` var richTextSource: NSAttributedString! { get } ``` |
| To | ``` @NSCopying var richTextSource: NSAttributedString! { get } ``` |

Modified OSAScript.init(scriptDataDescriptor: NSAppleEventDescriptor!, fromURL: NSURL!, languageInstance: OSALanguageInstance!, usingStorageOptions: OSAStorageOptions, error: NSErrorPointer)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(scriptDataDescriptor data: NSAppleEventDescriptor!, fromURL url: NSURL!, languageInstance instance: OSALanguageInstance!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: NSErrorPointer) ``` | OS X 10.10 |
| To | ``` init!(scriptDataDescriptor data: NSAppleEventDescriptor!, fromURL url: NSURL!, languageInstance instance: OSALanguageInstance!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: NSErrorPointer) ``` | OS X 10.6 |

Modified OSAScript.scriptDataDescriptorWithContentsOfURL(NSURL!) -> NSAppleEventDescriptor! [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified OSAScript.init(source: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(source source: String!) ``` |
| To | ``` init!(source source: String!) ``` |

Modified OSAScript.init(source: String!, fromURL: NSURL!, languageInstance: OSALanguageInstance!, usingStorageOptions: OSAStorageOptions)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(source source: String!, fromURL url: NSURL!, languageInstance instance: OSALanguageInstance!, usingStorageOptions storageOptions: OSAStorageOptions) ``` | OS X 10.10 |
| To | ``` init!(source source: String!, fromURL url: NSURL!, languageInstance instance: OSALanguageInstance!, usingStorageOptions storageOptions: OSAStorageOptions) ``` | OS X 10.6 |

Modified OSAScript.init(source: String!, language: OSALanguage!)

|  | Declaration |
| --- | --- |
| From | ``` init(source source: String!, language language: OSALanguage!) ``` |
| To | ``` init!(source source: String!, language language: OSALanguage!) ``` |

Modified OSAScript.url

|  | Declaration |
| --- | --- |
| From | ``` var url: NSURL! { get } ``` |
| To | ``` @NSCopying var url: NSURL! { get } ``` |

Modified OSAScript.writeToURL(NSURL!, ofType: String!, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ url: NSURL!, ofType type: String!, error errorInfo: AutoreleasingUnsafePointer<NSDictionary?>) -> Bool ``` |
| To | ``` func writeToURL(_ url: NSURL!, ofType type: String!, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool ``` |

Modified OSAScript.writeToURL(NSURL!, ofType: String!, usingStorageOptions: OSAStorageOptions, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ url: NSURL!, ofType type: String!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: AutoreleasingUnsafePointer<NSDictionary?>) -> Bool ``` |
| To | ``` func writeToURL(_ url: NSURL!, ofType type: String!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool ``` |

Modified OSAScriptController.script

|  | Declaration |
| --- | --- |
| From | ``` var script: OSAScript! ``` |
| To | ``` @NSCopying var script: OSAScript! ``` |

Modified OSAStorageOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OSAStorageOptions : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var Null: OSAStorageOptions { get }     static var PreventGetSource: OSAStorageOptions { get }     static var CompileIntoContext: OSAStorageOptions { get }     static var DontSetScriptLocation: OSAStorageOptions { get }     static var StayOpenApplet: OSAStorageOptions { get }     static var ShowStartupScreen: OSAStorageOptions { get } } ``` | RawOptionSet |
| To | ``` struct OSAStorageOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Null: OSAStorageOptions { get }     static var PreventGetSource: OSAStorageOptions { get }     static var CompileIntoContext: OSAStorageOptions { get }     static var DontSetScriptLocation: OSAStorageOptions { get }     static var StayOpenApplet: OSAStorageOptions { get }     static var ShowStartupScreen: OSAStorageOptions { get } } ``` | RawOptionSetType |

Modified OSAStorageOptions.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified OSAScriptErrorAppAddressKey

|  | Declaration |
| --- | --- |
| From | ``` let OSAScriptErrorAppAddressKey: NSString! ``` |
| To | ``` let OSAScriptErrorAppAddressKey: String ``` |

Modified OSAScriptErrorAppName

|  | Declaration |
| --- | --- |
| From | ``` let OSAScriptErrorAppName: NSString! ``` |
| To | ``` let OSAScriptErrorAppName: String ``` |

Modified OSAScriptErrorAppNameKey

|  | Declaration |
| --- | --- |
| From | ``` let OSAScriptErrorAppNameKey: NSString! ``` |
| To | ``` let OSAScriptErrorAppNameKey: String ``` |

Modified OSAScriptErrorBriefMessage

|  | Declaration |
| --- | --- |
| From | ``` let OSAScriptErrorBriefMessage: NSString! ``` |
| To | ``` let OSAScriptErrorBriefMessage: String ``` |

Modified OSAScriptErrorBriefMessageKey

|  | Declaration |
| --- | --- |
| From | ``` let OSAScriptErrorBriefMessageKey: NSString! ``` |
| To | ``` let OSAScriptErrorBriefMessageKey: String ``` |

Modified OSAScriptErrorExpectedTypeKey

|  | Declaration |
| --- | --- |
| From | ``` let OSAScriptErrorExpectedTypeKey: NSString! ``` |
| To | ``` let OSAScriptErrorExpectedTypeKey: String ``` |

Modified OSAScriptErrorMessage

|  | Declaration |
| --- | --- |
| From | ``` let OSAScriptErrorMessage: NSString! ``` |
| To | ``` let OSAScriptErrorMessage: String ``` |

Modified OSAScriptErrorMessageKey

|  | Declaration |
| --- | --- |
| From | ``` let OSAScriptErrorMessageKey: NSString! ``` |
| To | ``` let OSAScriptErrorMessageKey: String ``` |

Modified OSAScriptErrorNumber

|  | Declaration |
| --- | --- |
| From | ``` let OSAScriptErrorNumber: NSString! ``` |
| To | ``` let OSAScriptErrorNumber: String ``` |

Modified OSAScriptErrorNumberKey

|  | Declaration |
| --- | --- |
| From | ``` let OSAScriptErrorNumberKey: NSString! ``` |
| To | ``` let OSAScriptErrorNumberKey: String ``` |

Modified OSAScriptErrorOffendingObjectKey

|  | Declaration |
| --- | --- |
| From | ``` let OSAScriptErrorOffendingObjectKey: NSString! ``` |
| To | ``` let OSAScriptErrorOffendingObjectKey: String ``` |

Modified OSAScriptErrorPartialResultKey

|  | Declaration |
| --- | --- |
| From | ``` let OSAScriptErrorPartialResultKey: NSString! ``` |
| To | ``` let OSAScriptErrorPartialResultKey: String ``` |

Modified OSAScriptErrorRange

|  | Declaration |
| --- | --- |
| From | ``` let OSAScriptErrorRange: NSString! ``` |
| To | ``` let OSAScriptErrorRange: String ``` |

Modified OSAScriptErrorRangeKey

|  | Declaration |
| --- | --- |
| From | ``` let OSAScriptErrorRangeKey: NSString! ``` |
| To | ``` let OSAScriptErrorRangeKey: String ``` |

Modified OSAStorageApplicationBundleType

|  | Declaration |
| --- | --- |
| From | ``` let OSAStorageApplicationBundleType: NSString! ``` |
| To | ``` let OSAStorageApplicationBundleType: String ``` |

Modified OSAStorageApplicationType

|  | Declaration |
| --- | --- |
| From | ``` let OSAStorageApplicationType: NSString! ``` |
| To | ``` let OSAStorageApplicationType: String ``` |

Modified OSAStorageScriptBundleType

|  | Declaration |
| --- | --- |
| From | ``` let OSAStorageScriptBundleType: NSString! ``` |
| To | ``` let OSAStorageScriptBundleType: String ``` |

Modified OSAStorageScriptType

|  | Declaration |
| --- | --- |
| From | ``` let OSAStorageScriptType: NSString! ``` |
| To | ``` let OSAStorageScriptType: String ``` |

Modified OSAStorageTextType

|  | Declaration |
| --- | --- |
| From | ``` let OSAStorageTextType: NSString! ``` |
| To | ``` let OSAStorageTextType: String ``` |

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
