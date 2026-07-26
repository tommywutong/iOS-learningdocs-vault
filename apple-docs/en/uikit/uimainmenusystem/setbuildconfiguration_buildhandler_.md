---
title: 'setBuildConfiguration:buildHandler:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimainmenusystem/setbuildconfiguration:buildhandler:'
source_url: 'https://developer.apple.com/documentation/uikit/uimainmenusystem/setbuildconfiguration:buildhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimainmenusystem/setbuildconfiguration%3Abuildhandler%3A.json'
content_hash: 'sha256:6ee13be30b3eb9d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMainMenuSystem](../uimainmenusystem.md)

# setBuildConfiguration:buildHandler:

<sub>Instance Method</sub>

Specifies that the main menu system should be built using the specified configuration. A build handler can be optionally provided, which the main menu system will use instead of calling `-buildMenuWithBuilder:`. Setting this will invalidate and rebuild the main menu system. Ideally it should be set once, and as early as possible, preferably in `-application:didFinishLaunchingWithOptions:`. Subsequent rebuilds of the main menu system will continue to use this `configuration` and `buildHandler`. It is a developer error to set the `configuration` while the main menu system is building. Doing so will assert.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) setBuildConfiguration:(UIMainMenuSystemConfiguration *) configuration buildHandler:(void (^)(id<UIMenuBuilder>builder)) buildHandler;
```

## See Also

### Configuring a main menu system

- [Configuration](configuration.md) — A configuration for the main menu system. You can specify whether or not certain elements are present in the initial main menu, as well as a block to build the menu using a UIMenuBuilder.
