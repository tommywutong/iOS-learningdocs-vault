---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/OSAKit.html
archived_at: '2026-07-15T07:34:46.958907Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# OSAKit Changes

## OSAKit

OSALanguage.hRemoved -[OSALanguage componentInstance]Removed -[OSALanguage features]Removed -[OSALanguage info]Removed -[OSALanguage isThreadSafe]Removed -[OSALanguage manufacturer]Removed -[OSALanguage name]Removed -[OSALanguage subType]Removed -[OSALanguage type]Removed -[OSALanguage version]Added OSALanguage.componentInstanceAdded OSALanguage.featuresAdded OSALanguage.infoAdded OSALanguage.manufacturerAdded OSALanguage.nameAdded OSALanguage.subTypeAdded OSALanguage.threadSafeAdded OSALanguage.typeAdded OSALanguage.versionModified -[OSALanguage initWithComponent:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithComponent:(Component)component ``` |
| To | ``` - (instancetype)initWithComponent:(Component)component ``` |

OSALanguageInstance.hRemoved -[OSALanguageInstance componentInstance]Removed -[OSALanguageInstance language]Added OSALanguageInstance.componentInstanceAdded OSALanguageInstance.defaultTargetAdded OSALanguageInstance.languageAdded -[OSALanguageInstance richTextFromDescriptor:]Modified -[OSALanguageInstance initWithLanguage:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithLanguage:(OSALanguage *)language ``` |
| To | ``` - (instancetype)initWithLanguage:(OSALanguage *)language ``` |

Modified +[OSALanguageInstance languageInstanceWithLanguage:]

|  | Declaration |
| --- | --- |
| From | ``` + (id)languageInstanceWithLanguage:(OSALanguage *)language ``` |
| To | ``` + (instancetype)languageInstanceWithLanguage:(OSALanguage *)language ``` |

OSAScript.hRemoved -[OSAScript isCompiled]Removed -[OSAScript language]Removed -[OSAScript languageInstance]Removed -[OSAScript richTextSource]Removed -[OSAScript setLanguage:]Removed -[OSAScript setLanguageInstance:]Removed -[OSAScript source]Removed -[OSAScript url]Added OSAScript.compiledAdded OSAScript.languageAdded OSAScript.languageInstanceAdded OSAScript.richTextSourceAdded OSAScript.sourceAdded OSAScript.urlModified -[OSAScript initWithCompiledData:fromURL:usingStorageOptions:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCompiledData:(NSData *)data fromURL:(NSURL *)url usingStorageOptions:(OSAStorageOptions)storageOptions error:(NSError **)errorInfo ``` |
| To | ``` - (instancetype)initWithCompiledData:(NSData *)data fromURL:(NSURL *)url usingStorageOptions:(OSAStorageOptions)storageOptions error:(NSError **)errorInfo ``` |

Modified -[OSAScript initWithContentsOfURL:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url error:(NSDictionary **)errorInfo ``` |
| To | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url error:(NSDictionary **)errorInfo ``` |

Modified -[OSAScript initWithContentsOfURL:languageInstance:usingStorageOptions:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url languageInstance:(OSALanguageInstance *)instance usingStorageOptions:(OSAStorageOptions)storageOptions error:(NSError **)errorInfo ``` |
| To | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url languageInstance:(OSALanguageInstance *)instance usingStorageOptions:(OSAStorageOptions)storageOptions error:(NSError **)errorInfo ``` |

Modified -[OSAScript initWithScriptDataDescriptor:fromURL:languageInstance:usingStorageOptions:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithScriptDataDescriptor:(NSAppleEventDescriptor *)data fromURL:(NSURL *)url languageInstance:(OSALanguageInstance *)instance usingStorageOptions:(OSAStorageOptions)storageOptions error:(NSError **)errorInfo ``` |
| To | ``` - (instancetype)initWithScriptDataDescriptor:(NSAppleEventDescriptor *)data fromURL:(NSURL *)url languageInstance:(OSALanguageInstance *)instance usingStorageOptions:(OSAStorageOptions)storageOptions error:(NSError **)errorInfo ``` |

Modified -[OSAScript initWithSource:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithSource:(NSString *)source ``` |
| To | ``` - (instancetype)initWithSource:(NSString *)source ``` |

Modified -[OSAScript initWithSource:fromURL:languageInstance:usingStorageOptions:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithSource:(NSString *)source fromURL:(NSURL *)url languageInstance:(OSALanguageInstance *)instance usingStorageOptions:(OSAStorageOptions)storageOptions ``` |
| To | ``` - (instancetype)initWithSource:(NSString *)source fromURL:(NSURL *)url languageInstance:(OSALanguageInstance *)instance usingStorageOptions:(OSAStorageOptions)storageOptions ``` |

Modified -[OSAScript initWithSource:language:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithSource:(NSString *)source language:(OSALanguage *)language ``` |
| To | ``` - (instancetype)initWithSource:(NSString *)source language:(OSALanguage *)language ``` |

OSAScriptController.hRemoved -[OSAScriptController isCompiling]Removed -[OSAScriptController language]Removed -[OSAScriptController resultView]Removed -[OSAScriptController script]Removed -[OSAScriptController scriptState]Removed -[OSAScriptController scriptView]Removed -[OSAScriptController setLanguage:]Removed -[OSAScriptController setResultView:]Removed -[OSAScriptController setScript:]Removed -[OSAScriptController setScriptView:]Added OSAScriptController.compilingAdded OSAScriptController.languageAdded OSAScriptController.resultViewAdded OSAScriptController.scriptAdded OSAScriptController.scriptStateAdded OSAScriptController.scriptViewModified -[OSAScriptController compileScript:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)compileScript:(id)sender ``` |
| To | ``` - (IBAction)compileScript:(id)sender ``` |

Modified -[OSAScriptController recordScript:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)recordScript:(id)sender ``` |
| To | ``` - (IBAction)recordScript:(id)sender ``` |

Modified -[OSAScriptController runScript:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)runScript:(id)sender ``` |
| To | ``` - (IBAction)runScript:(id)sender ``` |

Modified -[OSAScriptController stopScript:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)stopScript:(id)sender ``` |
| To | ``` - (IBAction)stopScript:(id)sender ``` |

OSAScriptView.hRemoved -[OSAScriptView indentWidth]Removed -[OSAScriptView indentsWrappedLines]Removed -[OSAScriptView setIndentWidth:]Removed -[OSAScriptView setIndentsWrappedLines:]Removed -[OSAScriptView setSource:]Removed -[OSAScriptView setTabWidth:]Removed -[OSAScriptView setUsesScriptAssistant:]Removed -[OSAScriptView setUsesTabs:]Removed -[OSAScriptView setWrapsLines:]Removed -[OSAScriptView source]Removed -[OSAScriptView tabWidth]Removed -[OSAScriptView usesScriptAssistant]Removed -[OSAScriptView usesTabs]Removed -[OSAScriptView wrapsLines]Added OSAScriptView.indentWidthAdded OSAScriptView.indentsWrappedLinesAdded OSAScriptView.sourceAdded OSAScriptView.tabWidthAdded OSAScriptView.usesScriptAssistantAdded OSAScriptView.usesTabsAdded OSAScriptView.wrapsLines

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
