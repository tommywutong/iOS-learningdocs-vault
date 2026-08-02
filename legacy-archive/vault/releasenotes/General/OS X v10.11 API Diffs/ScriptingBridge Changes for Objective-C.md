---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/ScriptingBridge.html
archived_at: '2026-07-18T02:53:13.043863Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# ScriptingBridge Changes for Objective-C

### ScriptingBridge

#### SBApplication.h

Modified [+[SBApplication applicationWithBundleIdentifier:]](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1588086-applicationwithbundleidentifier)

|  | Declaration |
| --- | --- |
| From | ``` + (id)applicationWithBundleIdentifier:(NSString *)ident ``` |
| To | ``` + (__kindof SBApplication * _Nullable)applicationWithBundleIdentifier:(NSString * _Nonnull)ident ``` |

Modified [+[SBApplication applicationWithProcessIdentifier:]](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1588085-applicationwithprocessidentifier)

|  | Declaration |
| --- | --- |
| From | ``` + (id)applicationWithProcessIdentifier:(pid_t)pid ``` |
| To | ``` + (__kindof SBApplication * _Nullable)applicationWithProcessIdentifier:(pid_t)pid ``` |

Modified [+[SBApplication applicationWithURL:]](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1588084-applicationwithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (id)applicationWithURL:(NSURL *)url ``` |
| To | ``` + (__kindof SBApplication * _Nullable)applicationWithURL:(NSURL * _Nonnull)url ``` |

Modified [-[SBApplication classForScriptingClass:]](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1423987-class)

|  | Declaration |
| --- | --- |
| From | ``` - (Class)classForScriptingClass:(NSString *)className ``` |
| To | ``` - (Class _Nullable)classForScriptingClass:(NSString * _Nonnull)className ``` |

Modified [SBApplication.delegate](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1423983-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) id<SBApplicationDelegate> delegate ``` |
| To | ``` @property(strong, nullable) id<SBApplicationDelegate> delegate ``` |

Modified [-[SBApplication initWithBundleIdentifier:]](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1424009-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithBundleIdentifier:(NSString *)ident ``` |
| To | ``` - (__kindof SBApplication * _Nullable)initWithBundleIdentifier:(NSString * _Nonnull)ident ``` |

Modified [-[SBApplication initWithProcessIdentifier:]](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1424001-initwithprocessidentifier)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithProcessIdentifier:(pid_t)pid ``` |
| To | ``` - (__kindof SBApplication * _Nullable)initWithProcessIdentifier:(pid_t)pid ``` |

Modified [-[SBApplication initWithURL:]](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1423947-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithURL:(NSURL *)url ``` |
| To | ``` - (__kindof SBApplication * _Nullable)initWithURL:(NSURL * _Nonnull)url ``` |

Modified [-[SBApplicationDelegate eventDidFail:withError:]](https://developer.apple.com/documentation/scriptingbridge/sbapplicationdelegate/1424011-eventdidfail)

|  | Declaration |
| --- | --- |
| From | ``` - (id)eventDidFail:(const AppleEvent *)event withError:(NSError *)error ``` |
| To | ``` - (id _Nonnull)eventDidFail:(const AppleEvent * _Nonnull)event withError:(NSError * _Nonnull)error ``` |

#### SBElementArray.h

Modified [-[SBElementArray arrayByApplyingSelector:]](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423951-arraybyapplyingselector)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)arrayByApplyingSelector:(SEL)selector ``` |
| To | ``` - (NSArray<id> * _Nonnull)arrayByApplyingSelector:(SEL _Nonnull)selector ``` |

Modified [-[SBElementArray arrayByApplyingSelector:withObject:]](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1424007-array)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)arrayByApplyingSelector:(SEL)aSelector withObject:(id)argument ``` |
| To | ``` - (NSArray<id> * _Nonnull)arrayByApplyingSelector:(SEL _Nonnull)aSelector withObject:(id _Nonnull)argument ``` |

Modified [-[SBElementArray get]](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423997-get)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)get ``` |
| To | ``` - (NSArray<ObjectType> * _Nullable)get ``` |

Modified [-[SBElementArray objectAtLocation:]](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423963-objectatlocation)

|  | Declaration |
| --- | --- |
| From | ``` - (id)objectAtLocation:(id)location ``` |
| To | ``` - (ObjectType _Nonnull)objectAtLocation:(id _Nonnull)location ``` |

Modified [-[SBElementArray objectWithID:]](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423985-objectwithid)

|  | Declaration |
| --- | --- |
| From | ``` - (id)objectWithID:(id)identifier ``` |
| To | ``` - (ObjectType _Nonnull)objectWithID:(id _Nonnull)identifier ``` |

Modified [-[SBElementArray objectWithName:]](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423971-objectwithname)

|  | Declaration |
| --- | --- |
| From | ``` - (id)objectWithName:(NSString *)name ``` |
| To | ``` - (ObjectType _Nonnull)objectWithName:(NSString * _Nonnull)name ``` |

#### SBObject.h

Modified [-[SBObject elementArrayWithCode:]](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423995-elementarray)

|  | Declaration |
| --- | --- |
| From | ``` - (SBElementArray *)elementArrayWithCode:(DescType)code ``` |
| To | ``` - (SBElementArray * _Nonnull)elementArrayWithCode:(DescType)code ``` |

Modified [-[SBObject get]](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423965-get)

|  | Declaration |
| --- | --- |
| From | ``` - (id)get ``` |
| To | ``` - (id _Nullable)get ``` |

Modified [-[SBObject init]](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423993-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

Modified [-[SBObject initWithData:]](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423961-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(id)data ``` |
| To | ``` - (instancetype _Nonnull)initWithData:(id _Nonnull)data ``` |

Modified [-[SBObject initWithElementCode:properties:data:]](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423999-initwithelementcode)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithElementCode:(DescType)code properties:(NSDictionary *)properties data:(id)data ``` |
| To | ``` - (instancetype _Nonnull)initWithElementCode:(DescType)code properties:(NSDictionary<NSString *,id> * _Nullable)properties data:(id _Nullable)data ``` |

Modified [-[SBObject initWithProperties:]](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423973-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithProperties:(NSDictionary *)properties ``` |
| To | ``` - (instancetype _Nonnull)initWithProperties:(NSDictionary * _Nonnull)properties ``` |

Modified [-[SBObject lastError]](https://developer.apple.com/documentation/scriptingbridge/sbobject/1424005-lasterror)

|  | Declaration |
| --- | --- |
| From | ``` - (NSError *)lastError ``` |
| To | ``` - (NSError * _Nullable)lastError ``` |

Modified [-[SBObject propertyWithClass:code:]](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423977-propertywithclass)

|  | Declaration |
| --- | --- |
| From | ``` - (SBObject *)propertyWithClass:(Class)cls code:(AEKeyword)code ``` |
| To | ``` - (SBObject * _Nonnull)propertyWithClass:(Class _Nonnull)cls code:(AEKeyword)code ``` |

Modified [-[SBObject propertyWithCode:]](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423975-propertywithcode)

|  | Declaration |
| --- | --- |
| From | ``` - (SBObject *)propertyWithCode:(AEKeyword)code ``` |
| To | ``` - (SBObject * _Nonnull)propertyWithCode:(AEKeyword)code ``` |

Modified [-[SBObject sendEvent:id:parameters:]](https://developer.apple.com/documentation/scriptingbridge/sbobject/1579905-sendevent)

|  | Declaration |
| --- | --- |
| From | ``` - (id)sendEvent:(AEEventClass)eventClass id:(AEEventID)eventID parameters:(DescType)firstParamCode, ... ``` |
| To | ``` - (id _Nonnull)sendEvent:(AEEventClass)eventClass id:(AEEventID)eventID parameters:(DescType)firstParamCode, ... ``` |

Modified [-[SBObject setTo:]](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423967-setto)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setTo:(id)value ``` |
| To | ``` - (void)setTo:(id _Nullable)value ``` |

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
