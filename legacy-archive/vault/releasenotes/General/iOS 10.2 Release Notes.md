---
title: iOS 10.2 Release Notes
apple_id: TP40017585
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-10.2/index.html
archived_at: '2026-07-18T02:54:41.620033Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 10.2

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tkobvfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tkobvfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tkobvfvbuqmjnknltc)

### Introduction

iOS 10.2 SDK provides support for developing iOS apps. It’s packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for iOS and macOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for iPhone, iPad, or iPod touch running iOS 10.2. You can also test your apps using the included iOS Simulator, which supports iOS 10.2. iOS 10.2 SDK requires a Mac computer running macOS 10.10.3 (Yosemite) or later.

This version of iOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/).

### Bug Reporting

For issues not mentioned in [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tkobvfvbuqmjnknltc), please file bugs through the Apple Developer website [https://developer.apple.com/bug-reporting/](https://developer.apple.com/bug-reporting/). Additionally, you may discuss these issues and iOS 10.2 SDK in the Apple Developer Forums: [http://devforums.apple.com](http://devforums.apple.com/). To get more information about iCloud for Developers, go to [http://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Notes and Known Issues

The following items relate to using iOS 10.2 SDK to develop code.

### AAC

Automatic Assessment Configuration (AAC) now prevents using the Universal Clipboard during an assessment.

### SOS

SOS is only supported in India.

### SpriteKit

The following [SKNode](https://developer.apple.com/documentation/spritekit/sknode) methods and attributes are deprecated, but missing the deprecation notice from the public header (`SKNode.h`):

- DEPRECATED: Attributes are only supported for node classes supporting [SKShader](https://developer.apple.com/documentation/spritekit/skshader) (see [SKSpriteNode](https://developer.apple.com/documentation/spritekit/skspritenode)).
- `@property (nonatomic, nonnull, copy) NSDictionary<NSString *, SKAttributeValue *> *attributeValues;`
- `- (nullable SKAttributeValue*)valueForAttributeNamed:(nonnull NSString *)key;`
- `- (void)setValue:(SKAttributeValue*)value forAttributeNamed:(nonnull NSString *)key NS_SWIFT_NAME(setValue(_:forAttribute:));`
