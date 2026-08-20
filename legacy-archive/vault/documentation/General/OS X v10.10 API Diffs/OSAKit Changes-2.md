---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/OSAKit.html
archived_at: '2026-07-15T07:34:56.160907Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# OSAKit Changes

## OSAKit (Added)

Added OSALanguageAdded OSALanguage.availableLanguages() -> [AnyObject]! [class]Added OSALanguage.init(component: Component)Added OSALanguage.componentInstanceAdded OSALanguage.defaultLanguage() -> OSALanguage! [class]Added OSALanguage.featuresAdded OSALanguage.init(forName: String!)Added OSALanguage.init(forScriptDataDescriptor: NSAppleEventDescriptor!)Added OSALanguage.infoAdded OSALanguage.manufacturerAdded OSALanguage.nameAdded OSALanguage.setDefaultLanguage(OSALanguage!) [class]Added OSALanguage.sharedLanguageInstance() -> OSALanguageInstance!Added OSALanguage.subTypeAdded OSALanguage.threadSafeAdded OSALanguage.typeAdded OSALanguage.versionAdded OSALanguageFeatures [struct]Added OSALanguageFeatures.SupportsAECoercionAdded OSALanguageFeatures.SupportsAESendingAdded OSALanguageFeatures.SupportsCompilingAdded OSALanguageFeatures.SupportsConvenienceAdded OSALanguageFeatures.SupportsDialectsAdded OSALanguageFeatures.SupportsEventHandlingAdded OSALanguageFeatures.SupportsGetSourceAdded OSALanguageFeatures.SupportsRecordingAdded OSALanguageFeatures.init(_: UInt)Added OSALanguageFeatures.init(rawValue: UInt)Added OSALanguageInstanceAdded OSALanguageInstance.componentInstanceAdded OSALanguageInstance.defaultTargetAdded OSALanguageInstance.languageAdded OSALanguageInstance.init(language: OSALanguage!)Added OSALanguageInstance.richTextFromDescriptor(NSAppleEventDescriptor!) -> NSAttributedString!Added OSAScriptAdded OSAScript.compileAndReturnError(AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> BoolAdded OSAScript.compiledAdded OSAScript.init(compiledData: NSData!, fromURL: NSURL!, usingStorageOptions: OSAStorageOptions, error: NSErrorPointer)Added OSAScript.compiledDataForType(String!, usingStorageOptions: OSAStorageOptions, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSData!Added OSAScript.init(contentsOfURL: NSURL!, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>)Added OSAScript.init(contentsOfURL: NSURL!, languageInstance: OSALanguageInstance!, usingStorageOptions: OSAStorageOptions, error: NSErrorPointer)Added OSAScript.executeAndReturnDisplayValue(AutoreleasingUnsafeMutablePointer<NSAttributedString?>, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor!Added OSAScript.executeAndReturnError(AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor!Added OSAScript.executeAppleEvent(NSAppleEventDescriptor!, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor!Added OSAScript.executeHandlerWithName(String!, arguments:[AnyObject]!, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor!Added OSAScript.languageAdded OSAScript.languageInstanceAdded OSAScript.richTextFromDescriptor(NSAppleEventDescriptor!) -> NSAttributedString!Added OSAScript.richTextSourceAdded OSAScript.init(scriptDataDescriptor: NSAppleEventDescriptor!, fromURL: NSURL!, languageInstance: OSALanguageInstance!, usingStorageOptions: OSAStorageOptions, error: NSErrorPointer)Added OSAScript.scriptDataDescriptorWithContentsOfURL(NSURL!) -> NSAppleEventDescriptor! [class]Added OSAScript.sourceAdded OSAScript.init(source: String!)Added OSAScript.init(source: String!, fromURL: NSURL!, languageInstance: OSALanguageInstance!, usingStorageOptions: OSAStorageOptions)Added OSAScript.init(source: String!, language: OSALanguage!)Added OSAScript.urlAdded OSAScript.writeToURL(NSURL!, ofType: String!, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> BoolAdded OSAScript.writeToURL(NSURL!, ofType: String!, usingStorageOptions: OSAStorageOptions, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> BoolAdded OSAScriptControllerAdded OSAScriptController.compileScript(AnyObject!)Added OSAScriptController.compilingAdded OSAScriptController.languageAdded OSAScriptController.recordScript(AnyObject!)Added OSAScriptController.resultViewAdded OSAScriptController.runScript(AnyObject!)Added OSAScriptController.scriptAdded OSAScriptController.scriptStateAdded OSAScriptController.scriptViewAdded OSAScriptController.stopScript(AnyObject!)Added OSAScriptState [enum]Added OSAScriptState.RecordingAdded OSAScriptState.RunningAdded OSAScriptState.StoppedAdded OSAScriptViewAdded OSAScriptView.indentWidthAdded OSAScriptView.indentsWrappedLinesAdded OSAScriptView.sourceAdded OSAScriptView.tabWidthAdded OSAScriptView.usesScriptAssistantAdded OSAScriptView.usesTabsAdded OSAScriptView.wrapsLinesAdded OSAStorageOptions [struct]Added OSAStorageOptions.CompileIntoContextAdded OSAStorageOptions.DontSetScriptLocationAdded OSAStorageOptions.NullAdded OSAStorageOptions.PreventGetSourceAdded OSAStorageOptions.ShowStartupScreenAdded OSAStorageOptions.StayOpenAppletAdded OSAStorageOptions.init(_: UInt)Added OSAStorageOptions.init(rawValue: UInt)Added OSAScriptErrorAppAddressKeyAdded OSAScriptErrorAppNameAdded OSAScriptErrorAppNameKeyAdded OSAScriptErrorBriefMessageAdded OSAScriptErrorBriefMessageKeyAdded OSAScriptErrorExpectedTypeKeyAdded OSAScriptErrorMessageAdded OSAScriptErrorMessageKeyAdded OSAScriptErrorNumberAdded OSAScriptErrorNumberKeyAdded OSAScriptErrorOffendingObjectKeyAdded OSAScriptErrorPartialResultKeyAdded OSAScriptErrorRangeAdded OSAScriptErrorRangeKeyAdded OSAStorageApplicationBundleTypeAdded OSAStorageApplicationTypeAdded OSAStorageScriptBundleTypeAdded OSAStorageScriptTypeAdded OSAStorageTextType

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
