---
title: 'actionWithIdentifier:alternateAction:configurationProvider:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwindowsceneactivationaction/actionwithidentifier:alternateaction:configurationprovider:'
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowsceneactivationaction/actionwithidentifier:alternateaction:configurationprovider:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowsceneactivationaction/actionwithidentifier%3Aalternateaction%3Aconfigurationprovider%3A.json'
content_hash: 'sha256:523d00d2ddb1c872'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [ActivationAction](../uiwindowscene/activationaction.md)

# actionWithIdentifier:alternateAction:configurationProvider:

<sub>Type Method</sub>

Creates an activation action with the specified parameters.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) actionWithIdentifier:(UIActionIdentifier) identifier alternateAction:(UIAction *) alternateAction configurationProvider:(UIWindowSceneActivationActionConfigurationProvider) configurationProvider;
```

## Parameters

- `identifier` — The unique identifier for the action. Specify `nil` to let this method create a unique identifier for you.

- `alternateAction` — An alternate action to perform if the platform doesn’t support multiple scenes or if requesting a scene fails.

- `configurationProvider` — The closure the system calls when the user selects the action. The closure should return a [ActivationConfiguration](../uiwindowscene/activationconfiguration.md) object.

## Return Value

A newly initialized activation action object.

## See Also

### Creating an activation action

- [ConfigurationProvider](../uiwindowscene/activationaction/configurationprovider.md) — A type alias defining a closure that provides an activation configuration for the activation action.
