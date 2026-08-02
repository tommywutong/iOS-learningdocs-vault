---
title: Code Loading Programming Topics
apple_id: 10000052i
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingCode/Concepts/CocoaBundles.html
archived_at: '2026-07-15T07:16:27.096475Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Loading Programming Topics](Introduction%20to%20Dynamically%20Loading%20Code.md)


[Next](CFBundle%20and%20NSBundle.md)[Previous](About%20Loadable%20Bundles.md)

# Loadable Bundles in Cocoa

Loadable bundles written for the Cocoa runtime environment include a few features specific to Cocoa. Because they are written for Cocoa, they contain code for Objective-C classes. In particular, every Cocoa loadable bundle contains a _principal class_. The code loading mechanism provided by the NSBundle class uses a bundle’s principal class as an entry point. Applications loading bundles can ask NSBundle to find the principal class and use the returned `Class` object to create an instance of that class.

NSBundle finds the principal class in one of two ways. First, it looks for the `NSPrincipalClass` key in the bundle’s information property list. If the key is present, it uses the class named by the key’s value as the bundle’s principal class. If the key is not present or the key specifies a class that does not exist, NSBundle uses the first class loaded as the principal class. If the bundle is built with Xcode, the order of classes as viewed in the project determines the order in which they are loaded.

[Next](CFBundle%20and%20NSBundle.md)[Previous](About%20Loadable%20Bundles.md)

