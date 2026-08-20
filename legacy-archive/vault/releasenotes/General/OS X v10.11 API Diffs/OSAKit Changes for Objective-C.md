---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/OSAKit.html
archived_at: '2026-07-18T02:53:11.017342Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# OSAKit Changes for Objective-C

### OSAKit

#### OSALanguage.h

Modified +[OSALanguage availableLanguages]

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)availableLanguages ``` |
| To | ``` + (NSArray<OSALanguage *> * _Nonnull)availableLanguages ``` |

Modified OSALanguage.componentInstance

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) ComponentInstance componentInstance ``` |
| To | ``` @property(readonly, nonnull) ComponentInstance componentInstance ``` |

Modified +[OSALanguage defaultLanguage]

|  | Declaration |
| --- | --- |
| From | ``` + (OSALanguage *)defaultLanguage ``` |
| To | ``` + (OSALanguage * _Nullable)defaultLanguage ``` |

Modified OSALanguage.info

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *info ``` |
| To | ``` @property(readonly, copy, nullable) NSString *info ``` |

Modified -[OSALanguage initWithComponent:]

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithComponent:(Component)component ``` |
| To | ``` - (instancetype _Nonnull)initWithComponent:(Component _Nonnull)component ``` |

Modified +[OSALanguage languageForName:]

|  | Declaration |
| --- | --- |
| From | ``` + (OSALanguage *)languageForName:(NSString *)name ``` |
| To | ``` + (OSALanguage * _Nullable)languageForName:(NSString * _Nonnull)name ``` |

Modified +[OSALanguage languageForScriptDataDescriptor:]

|  | Declaration |
| --- | --- |
| From | ``` + (OSALanguage *)languageForScriptDataDescriptor:(NSAppleEventDescriptor *)descriptor ``` |
| To | ``` + (OSALanguage * _Nullable)languageForScriptDataDescriptor:(NSAppleEventDescriptor * _Nonnull)descriptor ``` |

Modified OSALanguage.name

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *name ``` |
| To | ``` @property(readonly, copy, nullable) NSString *name ``` |

Modified +[OSALanguage setDefaultLanguage:]

|  | Declaration |
| --- | --- |
| From | ``` + (void)setDefaultLanguage:(OSALanguage *)defaultLanguage ``` |
| To | ``` + (void)setDefaultLanguage:(OSALanguage * _Nonnull)defaultLanguage ``` |

Modified -[OSALanguage sharedLanguageInstance]

|  | Declaration |
| --- | --- |
| From | ``` - (OSALanguageInstance *)sharedLanguageInstance ``` |
| To | ``` - (OSALanguageInstance * _Nonnull)sharedLanguageInstance ``` |

Modified OSALanguage.version

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *version ``` |
| To | ``` @property(readonly, copy, nullable) NSString *version ``` |

#### OSALanguageInstance.h

Modified OSALanguageInstance.componentInstance

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) ComponentInstance componentInstance ``` |
| To | ``` @property(readonly, nonnull) ComponentInstance componentInstance ``` |

Modified OSALanguageInstance.defaultTarget

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSAppleEventDescriptor *defaultTarget ``` |
| To | ``` @property(strong, nullable) NSAppleEventDescriptor *defaultTarget ``` |

Modified -[OSALanguageInstance initWithLanguage:]

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithLanguage:(OSALanguage *)language ``` |
| To | ``` - (instancetype _Nonnull)initWithLanguage:(OSALanguage * _Nonnull)language ``` |

Modified OSALanguageInstance.language

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) OSALanguage *language ``` |
| To | ``` @property(readonly, strong, nonnull) OSALanguage *language ``` |

Modified +[OSALanguageInstance languageInstanceWithLanguage:]

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)languageInstanceWithLanguage:(OSALanguage *)language ``` |
| To | ``` + (instancetype _Nonnull)languageInstanceWithLanguage:(OSALanguage * _Nonnull)language ``` |

Modified -[OSALanguageInstance richTextFromDescriptor:]

|  | Declaration |
| --- | --- |
| From | ``` - (NSAttributedString *)richTextFromDescriptor:(NSAppleEventDescriptor *)descriptor ``` |
| To | ``` - (NSAttributedString * _Nullable)richTextFromDescriptor:(NSAppleEventDescriptor * _Nonnull)descriptor ``` |

#### OSAScript.h

Modified -[OSAScript compileAndReturnError:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)compileAndReturnError:(NSDictionary **)errorInfo ``` |
| To | ``` - (BOOL)compileAndReturnError:(NSDictionary<NSString *,id> * _Nullable * _Nullable)errorInfo ``` |

Modified -[OSAScript compiledDataForType:usingStorageOptions:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (NSData *)compiledDataForType:(NSString *)type usingStorageOptions:(OSAStorageOptions)storageOptions error:(NSDictionary **)errorInfo ``` |
| To | ``` - (NSData * _Nullable)compiledDataForType:(NSString * _Nonnull)type usingStorageOptions:(OSAStorageOptions)storageOptions error:(NSDictionary<NSString *,id> * _Nullable * _Nullable)errorInfo ``` |

Modified -[OSAScript executeAndReturnDisplayValue:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (NSAppleEventDescriptor *)executeAndReturnDisplayValue:(NSAttributedString **)displayValue error:(NSDictionary **)errorInfo ``` |
| To | ``` - (NSAppleEventDescriptor * _Nullable)executeAndReturnDisplayValue:(NSAttributedString * _Nullable * _Nonnull)displayValue error:(NSDictionary<NSString *,id> * _Nullable * _Nullable)errorInfo ``` |

Modified -[OSAScript executeAndReturnError:]

|  | Declaration |
| --- | --- |
| From | ``` - (NSAppleEventDescriptor *)executeAndReturnError:(NSDictionary **)errorInfo ``` |
| To | ``` - (NSAppleEventDescriptor * _Nullable)executeAndReturnError:(NSDictionary<NSString *,id> * _Nullable * _Nullable)errorInfo ``` |

Modified -[OSAScript executeAppleEvent:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (NSAppleEventDescriptor *)executeAppleEvent:(NSAppleEventDescriptor *)event error:(NSDictionary **)errorInfo ``` |
| To | ``` - (NSAppleEventDescriptor * _Nullable)executeAppleEvent:(NSAppleEventDescriptor * _Nonnull)event error:(NSDictionary<NSString *,id> * _Nullable * _Nullable)errorInfo ``` |

Modified -[OSAScript executeHandlerWithName:arguments:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (NSAppleEventDescriptor *)executeHandlerWithName:(NSString *)name arguments:(NSArray *)arguments error:(NSDictionary **)errorInfo ``` |
| To | ``` - (NSAppleEventDescriptor * _Nullable)executeHandlerWithName:(NSString * _Nonnull)name arguments:(NSArray * _Nonnull)arguments error:(NSDictionary<NSString *,id> * _Nullable * _Nullable)errorInfo ``` |

Modified -[OSAScript initWithCompiledData:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCompiledData:(NSData *)data error:(NSDictionary **)errorInfo ``` |
| To | ``` - (id _Nonnull)initWithCompiledData:(NSData * _Nonnull)data error:(NSDictionary<NSString *,id> * _Nullable * _Nullable)errorInfo ``` |

Modified -[OSAScript initWithCompiledData:fromURL:usingStorageOptions:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCompiledData:(NSData *)data fromURL:(NSURL *)url usingStorageOptions:(OSAStorageOptions)storageOptions error:(NSError **)errorInfo ``` |
| To | ``` - (instancetype _Nullable)initWithCompiledData:(NSData * _Nonnull)data fromURL:(NSURL * _Nullable)url usingStorageOptions:(OSAStorageOptions)storageOptions error:(NSError * _Nullable * _Nullable)errorInfo ``` |

Modified -[OSAScript initWithContentsOfURL:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url error:(NSDictionary **)errorInfo ``` |
| To | ``` - (instancetype _Nullable)initWithContentsOfURL:(NSURL * _Nonnull)url error:(NSDictionary<NSString *,id> * _Nullable * _Nullable)errorInfo ``` |

Modified -[OSAScript initWithContentsOfURL:language:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url language:(OSALanguage *)language error:(NSDictionary **)errorInfo ``` |
| To | ``` - (id _Nonnull)initWithContentsOfURL:(NSURL * _Nonnull)url language:(OSALanguage * _Nonnull)language error:(NSDictionary<NSString *,id> * _Nullable * _Nullable)errorInfo ``` |

Modified -[OSAScript initWithContentsOfURL:languageInstance:usingStorageOptions:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url languageInstance:(OSALanguageInstance *)instance usingStorageOptions:(OSAStorageOptions)storageOptions error:(NSError **)errorInfo ``` |
| To | ``` - (instancetype _Nullable)initWithContentsOfURL:(NSURL * _Nonnull)url languageInstance:(OSALanguageInstance * _Nullable)instance usingStorageOptions:(OSAStorageOptions)storageOptions error:(NSError * _Nullable * _Nullable)errorInfo ``` |

Modified -[OSAScript initWithScriptDataDescriptor:fromURL:languageInstance:usingStorageOptions:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithScriptDataDescriptor:(NSAppleEventDescriptor *)data fromURL:(NSURL *)url languageInstance:(OSALanguageInstance *)instance usingStorageOptions:(OSAStorageOptions)storageOptions error:(NSError **)errorInfo ``` |
| To | ``` - (instancetype _Nullable)initWithScriptDataDescriptor:(NSAppleEventDescriptor * _Nonnull)data fromURL:(NSURL * _Nullable)url languageInstance:(OSALanguageInstance * _Nullable)instance usingStorageOptions:(OSAStorageOptions)storageOptions error:(NSError * _Nullable * _Nullable)errorInfo ``` |

Modified -[OSAScript initWithSource:]

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSource:(NSString *)source ``` |
| To | ``` - (instancetype _Nonnull)initWithSource:(NSString * _Nonnull)source ``` |

Modified -[OSAScript initWithSource:fromURL:languageInstance:usingStorageOptions:]

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSource:(NSString *)source fromURL:(NSURL *)url languageInstance:(OSALanguageInstance *)instance usingStorageOptions:(OSAStorageOptions)storageOptions ``` |
| To | ``` - (instancetype _Nonnull)initWithSource:(NSString * _Nonnull)source fromURL:(NSURL * _Nullable)url languageInstance:(OSALanguageInstance * _Nullable)instance usingStorageOptions:(OSAStorageOptions)storageOptions ``` |

Modified -[OSAScript initWithSource:language:]

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSource:(NSString *)source language:(OSALanguage *)language ``` |
| To | ``` - (instancetype _Nonnull)initWithSource:(NSString * _Nonnull)source language:(OSALanguage * _Nullable)language ``` |

Modified OSAScript.language

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) OSALanguage *language ``` |
| To | ``` @property(strong, nonnull) OSALanguage *language ``` |

Modified OSAScript.languageInstance

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) OSALanguageInstance *languageInstance ``` |
| To | ``` @property(strong, nonnull) OSALanguageInstance *languageInstance ``` |

Modified -[OSAScript richTextFromDescriptor:]

|  | Declaration |
| --- | --- |
| From | ``` - (NSAttributedString *)richTextFromDescriptor:(NSAppleEventDescriptor *)descriptor ``` |
| To | ``` - (NSAttributedString * _Nullable)richTextFromDescriptor:(NSAppleEventDescriptor * _Nonnull)descriptor ``` |

Modified OSAScript.richTextSource

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSAttributedString *richTextSource ``` |
| To | ``` @property(readonly, copy, nullable) NSAttributedString *richTextSource ``` |

Modified +[OSAScript scriptDataDescriptorWithContentsOfURL:]

|  | Declaration |
| --- | --- |
| From | ``` + (NSAppleEventDescriptor *)scriptDataDescriptorWithContentsOfURL:(NSURL *)url ``` |
| To | ``` + (NSAppleEventDescriptor * _Nullable)scriptDataDescriptorWithContentsOfURL:(NSURL * _Nonnull)url ``` |

Modified OSAScript.source

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *source ``` |
| To | ``` @property(readonly, copy, nonnull) NSString *source ``` |

Modified OSAScript.url

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSURL *url ``` |
| To | ``` @property(readonly, copy, nullable) NSURL *url ``` |

Modified -[OSAScript writeToURL:ofType:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)writeToURL:(NSURL *)url ofType:(NSString *)type error:(NSDictionary **)errorInfo ``` |
| To | ``` - (BOOL)writeToURL:(NSURL * _Nonnull)url ofType:(NSString * _Nonnull)type error:(NSDictionary<NSString *,id> * _Nullable * _Nullable)errorInfo ``` |

Modified -[OSAScript writeToURL:ofType:usingStorageOptions:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)writeToURL:(NSURL *)url ofType:(NSString *)type usingStorageOptions:(OSAStorageOptions)storageOptions error:(NSDictionary **)errorInfo ``` |
| To | ``` - (BOOL)writeToURL:(NSURL * _Nonnull)url ofType:(NSString * _Nonnull)type usingStorageOptions:(OSAStorageOptions)storageOptions error:(NSDictionary<NSString *,id> * _Nullable * _Nullable)errorInfo ``` |

#### OSAScriptController.h

Modified -[OSAScriptController compileScript:]

|  | Declaration |
| --- | --- |
| From | ``` - (IBAction)compileScript:(id)sender ``` |
| To | ``` - (IBAction)compileScript:(id _Nullable)sender ``` |

Modified OSAScriptController.language

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) OSALanguage *language ``` |
| To | ``` @property(strong, nullable) OSALanguage *language ``` |

Modified -[OSAScriptController recordScript:]

|  | Declaration |
| --- | --- |
| From | ``` - (IBAction)recordScript:(id)sender ``` |
| To | ``` - (IBAction)recordScript:(id _Nullable)sender ``` |

Modified OSAScriptController.resultView

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSTextView *resultView ``` |
| To | ``` @property(strong, nullable) NSTextView *resultView ``` |

Modified -[OSAScriptController runScript:]

|  | Declaration |
| --- | --- |
| From | ``` - (IBAction)runScript:(id)sender ``` |
| To | ``` - (IBAction)runScript:(id _Nullable)sender ``` |

Modified OSAScriptController.script

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) OSAScript *script ``` |
| To | ``` @property(copy, nullable) OSAScript *script ``` |

Modified OSAScriptController.scriptView

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) OSAScriptView *scriptView ``` |
| To | ``` @property(strong, nullable) OSAScriptView *scriptView ``` |

Modified -[OSAScriptController stopScript:]

|  | Declaration |
| --- | --- |
| From | ``` - (IBAction)stopScript:(id)sender ``` |
| To | ``` - (IBAction)stopScript:(id _Nullable)sender ``` |

#### OSAScriptView.h

Modified OSAScriptView.source

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *source ``` |
| To | ``` @property(copy, nullable) NSString *source ``` |

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
