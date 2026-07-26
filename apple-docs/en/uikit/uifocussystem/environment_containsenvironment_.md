---
title: 'environment:containsEnvironment:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifocussystem/environment:containsenvironment:'
source_url: 'https://developer.apple.com/documentation/uikit/uifocussystem/environment:containsenvironment:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocussystem/environment%3Acontainsenvironment%3A.json'
content_hash: 'sha256:f1f7ab7bc1af5733'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusSystem](../uifocussystem.md)

# environment:containsEnvironment:

<sub>Type Method</sub>

Returns a Boolean value that indicates whether one focus environment is contained by another.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (BOOL) environment:(id<UIFocusEnvironment>) environment containsEnvironment:(id<UIFocusEnvironment>) otherEnvironment;
```

## Parameters

- `environment` — The object whose children you want to check.

- `otherEnvironment` — The target object.

## Return Value

[true](../../swift/true.md) if `environment` is an ancestor of `otherEnvironment`, or [false](../../swift/false.md) if it is not.

## Discussion

Use this method to determine if the two environments are related. For example, you might specify a [UIWindow](../uiwindow.md) object for `environment` and a [UIView](../uiview.md) object for `otherEnvironment` to determine if the view is displayed by that window.
