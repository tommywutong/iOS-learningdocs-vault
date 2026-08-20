---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/OSAKit.html
archived_at: '2026-07-18T02:53:40.090423Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# OSAKit Changes for Swift

### OSAKit

Removed OSALanguageFeatures.init(_: UInt)Removed OSAStorageOptions.init(_: UInt)Modified OSALanguage

|  | Declaration |
| --- | --- |
| From | ``` class OSALanguage : NSObject {     class func availableLanguages() -> [AnyObject]!     init!(forName name: String!) -> OSALanguage     class func languageForName(_ name: String!) -> OSALanguage!     init!(forScriptDataDescriptor descriptor: NSAppleEventDescriptor!) -> OSALanguage     class func languageForScriptDataDescriptor(_ descriptor: NSAppleEventDescriptor!) -> OSALanguage!     class func defaultLanguage() -> OSALanguage!     class func setDefaultLanguage(_ defaultLanguage: OSALanguage!)     init!(component component: Component)     func sharedLanguageInstance() -> OSALanguageInstance!     var componentInstance: ComponentInstance { get }     var name: String! { get }     var info: String! { get }     var version: String! { get }     var type: OSType { get }     var subType: OSType { get }     var manufacturer: OSType { get }     var features: OSALanguageFeatures { get }     var threadSafe: Bool { get } } ``` |
| To | ``` class OSALanguage : NSObject {     class func availableLanguages() -> [OSALanguage]      init?(forName name: String)     class func languageForName(_ name: String) -> OSALanguage?      init?(forScriptDataDescriptor descriptor: NSAppleEventDescriptor)     class func languageForScriptDataDescriptor(_ descriptor: NSAppleEventDescriptor) -> OSALanguage?     class func defaultLanguage() -> OSALanguage?     class func setDefaultLanguage(_ defaultLanguage: OSALanguage)     init(component component: Component)     func sharedLanguageInstance() -> OSALanguageInstance     var componentInstance: ComponentInstance { get }     var name: String? { get }     var info: String? { get }     var version: String? { get }     var type: OSType { get }     var subType: OSType { get }     var manufacturer: OSType { get }     var features: OSALanguageFeatures { get }     var threadSafe: Bool { get } } ``` |

Modified OSALanguage.availableLanguages() -> [OSALanguage] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func availableLanguages() -> [AnyObject]! ``` |
| To | ``` class func availableLanguages() -> [OSALanguage] ``` |

Modified OSALanguage.defaultLanguage() -> OSALanguage? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func defaultLanguage() -> OSALanguage! ``` |
| To | ``` class func defaultLanguage() -> OSALanguage? ``` |

Modified OSALanguage.info

|  | Declaration |
| --- | --- |
| From | ``` var info: String! { get } ``` |
| To | ``` var info: String? { get } ``` |

Modified OSALanguage.init(component: Component)

|  | Declaration |
| --- | --- |
| From | ``` init!(component component: Component) ``` |
| To | ``` init(component component: Component) ``` |

Modified OSALanguage.init(forName: String)

|  | Declaration |
| --- | --- |
| From | ``` init!(forName name: String!) -> OSALanguage ``` |
| To | ``` init?(forName name: String) ``` |

Modified OSALanguage.init(forScriptDataDescriptor: NSAppleEventDescriptor)

|  | Declaration |
| --- | --- |
| From | ``` init!(forScriptDataDescriptor descriptor: NSAppleEventDescriptor!) -> OSALanguage ``` |
| To | ``` init?(forScriptDataDescriptor descriptor: NSAppleEventDescriptor) ``` |

Modified OSALanguage.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String? { get } ``` |

Modified OSALanguage.setDefaultLanguage(_: OSALanguage) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func setDefaultLanguage(_ defaultLanguage: OSALanguage!) ``` |
| To | ``` class func setDefaultLanguage(_ defaultLanguage: OSALanguage) ``` |

Modified OSALanguage.sharedLanguageInstance() -> OSALanguageInstance

|  | Declaration |
| --- | --- |
| From | ``` func sharedLanguageInstance() -> OSALanguageInstance! ``` |
| To | ``` func sharedLanguageInstance() -> OSALanguageInstance ``` |

Modified OSALanguage.version

|  | Declaration |
| --- | --- |
| From | ``` var version: String! { get } ``` |
| To | ``` var version: String? { get } ``` |

Modified OSALanguageFeatures [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OSALanguageFeatures : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var SupportsCompiling: OSALanguageFeatures { get }     static var SupportsGetSource: OSALanguageFeatures { get }     static var SupportsAECoercion: OSALanguageFeatures { get }     static var SupportsAESending: OSALanguageFeatures { get }     static var SupportsRecording: OSALanguageFeatures { get }     static var SupportsConvenience: OSALanguageFeatures { get }     static var SupportsDialects: OSALanguageFeatures { get }     static var SupportsEventHandling: OSALanguageFeatures { get } } ``` | RawOptionSetType |
| To | ``` struct OSALanguageFeatures : OptionSetType {     init(rawValue rawValue: UInt)     static var SupportsCompiling: OSALanguageFeatures { get }     static var SupportsGetSource: OSALanguageFeatures { get }     static var SupportsAECoercion: OSALanguageFeatures { get }     static var SupportsAESending: OSALanguageFeatures { get }     static var SupportsRecording: OSALanguageFeatures { get }     static var SupportsConvenience: OSALanguageFeatures { get }     static var SupportsDialects: OSALanguageFeatures { get }     static var SupportsEventHandling: OSALanguageFeatures { get } } ``` | OptionSetType |

Modified OSALanguageInstance

|  | Declaration |
| --- | --- |
| From | ``` class OSALanguageInstance : NSObject {     convenience init!(language language: OSALanguage!)     class func languageInstanceWithLanguage(_ language: OSALanguage!) -> Self!     init!(language language: OSALanguage!)     var language: OSALanguage! { get }     var componentInstance: ComponentInstance { get }     var defaultTarget: NSAppleEventDescriptor!     func richTextFromDescriptor(_ descriptor: NSAppleEventDescriptor!) -> NSAttributedString! } ``` |
| To | ``` class OSALanguageInstance : NSObject {     convenience init(language language: OSALanguage)     class func languageInstanceWithLanguage(_ language: OSALanguage) -> Self     init(language language: OSALanguage)     var language: OSALanguage { get }     var componentInstance: ComponentInstance { get }     var defaultTarget: NSAppleEventDescriptor?     func richTextFromDescriptor(_ descriptor: NSAppleEventDescriptor) -> NSAttributedString? } ``` |

Modified OSALanguageInstance.defaultTarget

|  | Declaration |
| --- | --- |
| From | ``` var defaultTarget: NSAppleEventDescriptor! ``` |
| To | ``` var defaultTarget: NSAppleEventDescriptor? ``` |

Modified OSALanguageInstance.init(language: OSALanguage)

|  | Declaration |
| --- | --- |
| From | ``` init!(language language: OSALanguage!) ``` |
| To | ``` init(language language: OSALanguage) ``` |

Modified OSALanguageInstance.language

|  | Declaration |
| --- | --- |
| From | ``` var language: OSALanguage! { get } ``` |
| To | ``` var language: OSALanguage { get } ``` |

Modified OSALanguageInstance.richTextFromDescriptor(_: NSAppleEventDescriptor) -> NSAttributedString?

|  | Declaration |
| --- | --- |
| From | ``` func richTextFromDescriptor(_ descriptor: NSAppleEventDescriptor!) -> NSAttributedString! ``` |
| To | ``` func richTextFromDescriptor(_ descriptor: NSAppleEventDescriptor) -> NSAttributedString? ``` |

Modified OSAScript

|  | Declaration |
| --- | --- |
| From | ``` class OSAScript : NSObject, NSCopying {     class func scriptDataDescriptorWithContentsOfURL(_ url: NSURL!) -> NSAppleEventDescriptor!     init!(source source: String!)     init!(source source: String!, language language: OSALanguage!)     init!(source source: String!, fromURL url: NSURL!, languageInstance instance: OSALanguageInstance!, usingStorageOptions storageOptions: OSAStorageOptions)     init!(contentsOfURL url: NSURL!, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>)     init!(contentsOfURL url: NSURL!, language language: OSALanguage!, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>)     init!(contentsOfURL url: NSURL!, languageInstance instance: OSALanguageInstance!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: NSErrorPointer)     init!(compiledData data: NSData!, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>)     init!(compiledData data: NSData!, fromURL url: NSURL!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: NSErrorPointer)     init!(scriptDataDescriptor data: NSAppleEventDescriptor!, fromURL url: NSURL!, languageInstance instance: OSALanguageInstance!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: NSErrorPointer)     var source: String! { get }     @NSCopying var url: NSURL! { get }     var language: OSALanguage!     var languageInstance: OSALanguageInstance!     var compiled: Bool { get }     func compileAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool     func executeAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor!     func executeAppleEvent(_ event: NSAppleEventDescriptor!, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor!     func executeAndReturnDisplayValue(_ displayValue: AutoreleasingUnsafeMutablePointer<NSAttributedString?>, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor!     func executeHandlerWithName(_ name: String!, arguments arguments: [AnyObject]!, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor!     @NSCopying var richTextSource: NSAttributedString! { get }     func richTextFromDescriptor(_ descriptor: NSAppleEventDescriptor!) -> NSAttributedString!     func writeToURL(_ url: NSURL!, ofType type: String!, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool     func writeToURL(_ url: NSURL!, ofType type: String!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool     func compiledDataForType(_ type: String!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSData! } ``` |
| To | ``` class OSAScript : NSObject, NSCopying {     class func scriptDataDescriptorWithContentsOfURL(_ url: NSURL) -> NSAppleEventDescriptor?     init(source source: String)     init(source source: String, language language: OSALanguage?)     init(source source: String, fromURL url: NSURL?, languageInstance instance: OSALanguageInstance?, usingStorageOptions storageOptions: OSAStorageOptions)     init?(contentsOfURL url: NSURL, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>)     init(contentsOfURL url: NSURL, language language: OSALanguage, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>)     init(contentsOfURL url: NSURL, languageInstance instance: OSALanguageInstance?, usingStorageOptions storageOptions: OSAStorageOptions) throws     init(compiledData data: NSData, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>)     init(compiledData data: NSData, fromURL url: NSURL?, usingStorageOptions storageOptions: OSAStorageOptions) throws     init(scriptDataDescriptor data: NSAppleEventDescriptor, fromURL url: NSURL?, languageInstance instance: OSALanguageInstance?, usingStorageOptions storageOptions: OSAStorageOptions) throws     var source: String { get }     @NSCopying var url: NSURL? { get }     var language: OSALanguage     var languageInstance: OSALanguageInstance     var compiled: Bool { get }     func compileAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool     func executeAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor?     func executeAppleEvent(_ event: NSAppleEventDescriptor, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor?     func executeAndReturnDisplayValue(_ displayValue: AutoreleasingUnsafeMutablePointer<NSAttributedString?>, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor?     func executeHandlerWithName(_ name: String, arguments arguments: [AnyObject], error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor?     @NSCopying var richTextSource: NSAttributedString? { get }     func richTextFromDescriptor(_ descriptor: NSAppleEventDescriptor) -> NSAttributedString?     func writeToURL(_ url: NSURL, ofType type: String, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool     func writeToURL(_ url: NSURL, ofType type: String, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool     func compiledDataForType(_ type: String, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSData? } ``` |

Modified OSAScript.compiledDataForType(_: String, usingStorageOptions: OSAStorageOptions, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSData?

|  | Declaration |
| --- | --- |
| From | ``` func compiledDataForType(_ type: String!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSData! ``` |
| To | ``` func compiledDataForType(_ type: String, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSData? ``` |

Modified OSAScript.executeAndReturnDisplayValue(_: AutoreleasingUnsafeMutablePointer<NSAttributedString?>, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor?

|  | Declaration |
| --- | --- |
| From | ``` func executeAndReturnDisplayValue(_ displayValue: AutoreleasingUnsafeMutablePointer<NSAttributedString?>, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor! ``` |
| To | ``` func executeAndReturnDisplayValue(_ displayValue: AutoreleasingUnsafeMutablePointer<NSAttributedString?>, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor? ``` |

Modified OSAScript.executeAndReturnError(_: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor?

|  | Declaration |
| --- | --- |
| From | ``` func executeAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor! ``` |
| To | ``` func executeAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor? ``` |

Modified OSAScript.executeAppleEvent(_: NSAppleEventDescriptor, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor?

|  | Declaration |
| --- | --- |
| From | ``` func executeAppleEvent(_ event: NSAppleEventDescriptor!, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor! ``` |
| To | ``` func executeAppleEvent(_ event: NSAppleEventDescriptor, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor? ``` |

Modified OSAScript.executeHandlerWithName(_: String, arguments: [AnyObject], error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor?

|  | Declaration |
| --- | --- |
| From | ``` func executeHandlerWithName(_ name: String!, arguments arguments: [AnyObject]!, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor! ``` |
| To | ``` func executeHandlerWithName(_ name: String, arguments arguments: [AnyObject], error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor? ``` |

Modified OSAScript.init(compiledData: NSData, fromURL: NSURL?, usingStorageOptions: OSAStorageOptions) throws

|  | Declaration |
| --- | --- |
| From | ``` init!(compiledData data: NSData!, fromURL url: NSURL!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: NSErrorPointer) ``` |
| To | ``` init(compiledData data: NSData, fromURL url: NSURL?, usingStorageOptions storageOptions: OSAStorageOptions) throws ``` |

Modified OSAScript.init(contentsOfURL: NSURL, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>)

|  | Declaration |
| --- | --- |
| From | ``` init!(contentsOfURL url: NSURL!, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) ``` |
| To | ``` init?(contentsOfURL url: NSURL, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) ``` |

Modified OSAScript.init(contentsOfURL: NSURL, languageInstance: OSALanguageInstance?, usingStorageOptions: OSAStorageOptions) throws

|  | Declaration |
| --- | --- |
| From | ``` init!(contentsOfURL url: NSURL!, languageInstance instance: OSALanguageInstance!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: NSErrorPointer) ``` |
| To | ``` init(contentsOfURL url: NSURL, languageInstance instance: OSALanguageInstance?, usingStorageOptions storageOptions: OSAStorageOptions) throws ``` |

Modified OSAScript.init(scriptDataDescriptor: NSAppleEventDescriptor, fromURL: NSURL?, languageInstance: OSALanguageInstance?, usingStorageOptions: OSAStorageOptions) throws

|  | Declaration |
| --- | --- |
| From | ``` init!(scriptDataDescriptor data: NSAppleEventDescriptor!, fromURL url: NSURL!, languageInstance instance: OSALanguageInstance!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: NSErrorPointer) ``` |
| To | ``` init(scriptDataDescriptor data: NSAppleEventDescriptor, fromURL url: NSURL?, languageInstance instance: OSALanguageInstance?, usingStorageOptions storageOptions: OSAStorageOptions) throws ``` |

Modified OSAScript.init(source: String)

|  | Declaration |
| --- | --- |
| From | ``` init!(source source: String!) ``` |
| To | ``` init(source source: String) ``` |

Modified OSAScript.init(source: String, fromURL: NSURL?, languageInstance: OSALanguageInstance?, usingStorageOptions: OSAStorageOptions)

|  | Declaration |
| --- | --- |
| From | ``` init!(source source: String!, fromURL url: NSURL!, languageInstance instance: OSALanguageInstance!, usingStorageOptions storageOptions: OSAStorageOptions) ``` |
| To | ``` init(source source: String, fromURL url: NSURL?, languageInstance instance: OSALanguageInstance?, usingStorageOptions storageOptions: OSAStorageOptions) ``` |

Modified OSAScript.init(source: String, language: OSALanguage?)

|  | Declaration |
| --- | --- |
| From | ``` init!(source source: String!, language language: OSALanguage!) ``` |
| To | ``` init(source source: String, language language: OSALanguage?) ``` |

Modified OSAScript.language

|  | Declaration |
| --- | --- |
| From | ``` var language: OSALanguage! ``` |
| To | ``` var language: OSALanguage ``` |

Modified OSAScript.languageInstance

|  | Declaration |
| --- | --- |
| From | ``` var languageInstance: OSALanguageInstance! ``` |
| To | ``` var languageInstance: OSALanguageInstance ``` |

Modified OSAScript.richTextFromDescriptor(_: NSAppleEventDescriptor) -> NSAttributedString?

|  | Declaration |
| --- | --- |
| From | ``` func richTextFromDescriptor(_ descriptor: NSAppleEventDescriptor!) -> NSAttributedString! ``` |
| To | ``` func richTextFromDescriptor(_ descriptor: NSAppleEventDescriptor) -> NSAttributedString? ``` |

Modified OSAScript.richTextSource

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var richTextSource: NSAttributedString! { get } ``` |
| To | ``` @NSCopying var richTextSource: NSAttributedString? { get } ``` |

Modified OSAScript.scriptDataDescriptorWithContentsOfURL(_: NSURL) -> NSAppleEventDescriptor? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func scriptDataDescriptorWithContentsOfURL(_ url: NSURL!) -> NSAppleEventDescriptor! ``` |
| To | ``` class func scriptDataDescriptorWithContentsOfURL(_ url: NSURL) -> NSAppleEventDescriptor? ``` |

Modified OSAScript.source

|  | Declaration |
| --- | --- |
| From | ``` var source: String! { get } ``` |
| To | ``` var source: String { get } ``` |

Modified OSAScript.url

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var url: NSURL! { get } ``` |
| To | ``` @NSCopying var url: NSURL? { get } ``` |

Modified OSAScript.writeToURL(_: NSURL, ofType: String, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ url: NSURL!, ofType type: String!, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool ``` |
| To | ``` func writeToURL(_ url: NSURL, ofType type: String, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool ``` |

Modified OSAScript.writeToURL(_: NSURL, ofType: String, usingStorageOptions: OSAStorageOptions, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ url: NSURL!, ofType type: String!, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool ``` |
| To | ``` func writeToURL(_ url: NSURL, ofType type: String, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool ``` |

Modified OSAScriptController

|  | Declaration |
| --- | --- |
| From | ``` class OSAScriptController : NSController {     var scriptView: OSAScriptView!     var resultView: NSTextView!     @NSCopying var script: OSAScript!     var language: OSALanguage!     var scriptState: OSAScriptState { get }     var compiling: Bool { get }     @IBAction func compileScript(_ sender: AnyObject!)     @IBAction func recordScript(_ sender: AnyObject!)     @IBAction func runScript(_ sender: AnyObject!)     @IBAction func stopScript(_ sender: AnyObject!) } ``` |
| To | ``` class OSAScriptController : NSController {     var scriptView: OSAScriptView?     var resultView: NSTextView?     @NSCopying var script: OSAScript?     var language: OSALanguage?     var scriptState: OSAScriptState { get }     var compiling: Bool { get }     @IBAction func compileScript(_ sender: AnyObject?)     @IBAction func recordScript(_ sender: AnyObject?)     @IBAction func runScript(_ sender: AnyObject?)     @IBAction func stopScript(_ sender: AnyObject?) } ``` |

Modified OSAScriptController.compileScript(_: AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func compileScript(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func compileScript(_ sender: AnyObject?) ``` |

Modified OSAScriptController.language

|  | Declaration |
| --- | --- |
| From | ``` var language: OSALanguage! ``` |
| To | ``` var language: OSALanguage? ``` |

Modified OSAScriptController.recordScript(_: AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func recordScript(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func recordScript(_ sender: AnyObject?) ``` |

Modified OSAScriptController.resultView

|  | Declaration |
| --- | --- |
| From | ``` var resultView: NSTextView! ``` |
| To | ``` var resultView: NSTextView? ``` |

Modified OSAScriptController.runScript(_: AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func runScript(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func runScript(_ sender: AnyObject?) ``` |

Modified OSAScriptController.script

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var script: OSAScript! ``` |
| To | ``` @NSCopying var script: OSAScript? ``` |

Modified OSAScriptController.scriptView

|  | Declaration |
| --- | --- |
| From | ``` var scriptView: OSAScriptView! ``` |
| To | ``` var scriptView: OSAScriptView? ``` |

Modified OSAScriptController.stopScript(_: AnyObject?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func stopScript(_ sender: AnyObject!) ``` |
| To | ``` @IBAction func stopScript(_ sender: AnyObject?) ``` |

Modified OSAScriptState [enum]

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified OSAScriptView

|  | Declaration |
| --- | --- |
| From | ``` class OSAScriptView : NSTextView {     var source: String!     var usesScriptAssistant: Bool     var usesTabs: Bool     var tabWidth: Int     var wrapsLines: Bool     var indentsWrappedLines: Bool     var indentWidth: Int } ``` |
| To | ``` class OSAScriptView : NSTextView {     var source: String?     var usesScriptAssistant: Bool     var usesTabs: Bool     var tabWidth: Int     var wrapsLines: Bool     var indentsWrappedLines: Bool     var indentWidth: Int } ``` |

Modified OSAScriptView.source

|  | Declaration |
| --- | --- |
| From | ``` var source: String! ``` |
| To | ``` var source: String? ``` |

Modified OSAStorageOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OSAStorageOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Null: OSAStorageOptions { get }     static var PreventGetSource: OSAStorageOptions { get }     static var CompileIntoContext: OSAStorageOptions { get }     static var DontSetScriptLocation: OSAStorageOptions { get }     static var StayOpenApplet: OSAStorageOptions { get }     static var ShowStartupScreen: OSAStorageOptions { get } } ``` | RawOptionSetType |
| To | ``` struct OSAStorageOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var Null: OSAStorageOptions { get }     static var PreventGetSource: OSAStorageOptions { get }     static var CompileIntoContext: OSAStorageOptions { get }     static var DontSetScriptLocation: OSAStorageOptions { get }     static var StayOpenApplet: OSAStorageOptions { get }     static var ShowStartupScreen: OSAStorageOptions { get } } ``` | OptionSetType |

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
