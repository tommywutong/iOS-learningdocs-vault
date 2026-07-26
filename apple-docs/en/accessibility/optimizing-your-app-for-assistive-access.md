---
title: Optimizing your app for Assistive Access
framework: Accessibility
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/accessibility/optimizing-your-app-for-assistive-access
source_url: 'https://developer.apple.com/documentation/accessibility/optimizing-your-app-for-assistive-access'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/accessibility/optimizing-your-app-for-assistive-access.json'
content_hash: 'sha256:5b8a665ecc1a0ab8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Accessibility](../accessibility.md) · [Assistive technologies](assistive-technologies.md) · [Assistive Access](assistive-access.md)

# Optimizing your app for Assistive Access

<sub>Article</sub>

Adjust your app’s UI to make sure it works well for people who use Assistive Access.

## Overview

In general, make sure your standard app UI works well for Assistive Access. However, you can make adjustments to your UI to make sure it looks and works as you expect in Assistive Access. You can optimize your UI for Assistive Access in one of these ways:

- Create a streamlined UI by adopting the Assistive Access scene type.
- Get more screen space for your existing UI by opting in to full-screen mode.

Additionally, you can remove workflows or UI elements that aren’t appropriate in the context of Assistive Access.

### Create a streamlined UI for Assistive Access

Adding the [UISupportsAssistiveAccess](../bundleresources/information-property-list/uisupportsassistiveaccess.md) key to your project’s Info pane with a value of `YES` indicates your app supports a streamlined experience designed for Assistive Access. It allows your app’s UI to match the prominent style of Assistive Access controls. It also lists your app as Optimized for Assistive Access in Settings, so that a trusted supporter configuring Assistive Access on someone’s behalf knows that your app is optimized for this feature.

If you add this key to your project’s Info pane, adopt the [AssistiveAccess](../swiftui/assistiveaccess.md) scene type to provide a streamlined UI for your app when Assistive Access is on. For example, you can define a custom view hierarchy with fewer onscreen elements.

```swift
import SwiftUI

@main
struct ExampleApp: App {
    var body: some Scene {
        // Defines the default app UI. 
        WindowGroup {
            StandardContentView()
        }
        
        // Defines the app UI when Assistive Access is on.
        AssistiveAccess {
            AssistiveAccessContentView()
        }
    }
}
```

### Opt in to full-screen mode for your existing UI

Adding the [UISupportsFullScreenInAssistiveAccess](../bundleresources/information-property-list/uisupportsfullscreeninassistiveaccess.md) key to your project’s Info pane with a value of `YES` allows your app’s standard UI to expand into all the available space above the Back button in Assistive Access. It also lists your app as Optimized for Assistive Access in Settings, so that a trusted supporter configuring Assistive Access on someone’s behalf knows that your app’s UI is optimized for this feature.

If you add this key to your project’s Info pane, ensure your UI is adaptive so that it works with flexible screen dimensions. Don’t rely on fixed screen sizes in your app design or logic. Use safe areas and layout guides to avoid overlapping your app’s UI with system UI or hardware elements. For more information, see [safeAreaInsets](../uikit/uiview/safeareainsets.md) and [safeAreaLayoutGuide](../uikit/uiview/safearealayoutguide.md).

If you don’t add this key to your project’s Info pane, a trusted supporter can still choose to make your app available in Assistive Access. By default, the system draws apps in a reduced frame to fit them onscreen with the prominent Back button in Assistive Access. This frame matches the dimensions of a smaller iPhone or iPad screen, so you don’t need to make changes to your existing UI for your app to work in Assistive Access.

### Remove unnecessary UI elements

It may not be possible for a person who’s using your app while Assistive Access is running to complete certain tasks or workflows, due to the differences described in [Understand certain differences in Assistive Access on iPhone](https://support.apple.com/guide/assistive-access-iphone/understand-differences-assistive-access-dev473e94873/ios). In situations like this, you can make note of these differences when you test your app in Assistive Access, and remove workflows or UI elements that aren’t appropriate in the context of Assistive Access.

To make small adjustments to your UI in Assistive Access, you check whether Assistive Access is running on the device using SwiftUI or the Accessibility framework.

**SwiftUI**

```swift
import SwiftUI

@Environment(\.accessibilityAssistiveAccessEnabled) private var isAssistiveAccessEnabled

if isAssistiveAccessEnabled {
  // Assistive Access is on. Make small adjustments specific to Assistive Access.
}
```

**Accessibility framework**

```swift
import Accessibility

if AccessibilitySettings.isAssistiveAccessEnabled {
  // Assistive Access is on. Make small adjustments specific to Assistive Access.
} 
```

For Assistive Access design guidance, read Human Interface Guidelines \> [Accessibility](../design/human-interface-guidelines/accessibility.md).

## See Also

#### Related reference

- [AXAssistiveAccessEnabled](accessibilitysettings/isassistiveaccessenabled.md)
- [accessibilityAssistiveAccessEnabled](../swiftui/environmentvalues/accessibilityassistiveaccessenabled.md)
- [UISupportsFullScreenInAssistiveAccess](../bundleresources/information-property-list/uisupportsfullscreeninassistiveaccess.md)
- [AssistiveAccess](../swiftui/assistiveaccess.md)
- [UISupportsAssistiveAccess](../bundleresources/information-property-list/uisupportsassistiveaccess.md)

#### Related articles

- [Performing accessibility testing for your app](performing-accessibility-testing-for-your-app.md)

#### Related design guidance

- [Accessibility](../design/human-interface-guidelines/accessibility.md)

#### Related videos

- [Customize your app for Assistive Access](../https_/developer.apple.com/videos/play/wwdc2025/238.md)
- [Meet Assistive Access](../https_/developer.apple.com/videos/play/wwdc2023/10032.md)
