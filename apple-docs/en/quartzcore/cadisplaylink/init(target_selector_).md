---
title: 'init(target:selector:)'
framework: Core Animation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/cadisplaylink/init(target:selector:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/cadisplaylink/init(target:selector:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cadisplaylink/init%28target%3Aselector%3A%29.json'
content_hash: 'sha256:0e3e3803ed00a881'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CADisplayLink](../cadisplaylink.md)

# init(target:selector:)

<sub>Initializer</sub>

Creates a display link for a target that calls its selector.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(target: Any, selector sel: Selector)
```

## Parameters

- `target` — An object in your app that you want the system to notify each time it updates a display.

- `sel` — A selector instance that represents a method for `target`.

## Return Value

A new [CADisplayLink](../cadisplaylink.md) object.

## Discussion

The selector on the target must be a method with the following signature, where sender is the display link returned by this method.

**Swift**

```swift
@objc func selector(sender: CADisplayLink)
```

**Objective-C**

```objc
- (void) selector:(CADisplayLink *)sender;
```

The newly constructed display link retains the target.
