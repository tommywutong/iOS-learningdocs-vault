---
title: AttributeScopes
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes.json'
content_hash: 'sha256:3dd526bb554ca034'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# AttributeScopes

<sub>Enumeration</sub>

Collections of attributes that system frameworks define.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum AttributeScopes
```

## Overview

Attribute scopes define groups of attributes appropriate for use with attributed strings in a certain domain. Attribute definitions contain a name, value type, and encode/decode methods to support serialization.

For example, the [FoundationAttributes](attributescopes/foundationattributes.md) scope provides an attribute type for a link to a URL, [LinkAttribute](attributescopes/foundationattributes/linkattribute.md), along with a property to access this type, [link](attributescopes/foundationattributes/link.md). Because [FoundationAttributes](attributescopes/foundationattributes.md) implements [AttributeDynamicLookup](attributedynamiclookup.md), you can access the link attribute by name, as this example shows:

```swift
var attrStr = AttributedString("Example site")
attrStr.link = URL(string: "http://example.com")
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md)

## Topics

### Foundation-Defined Attributes

- [foundation](attributescopes/foundation.md) — A property for accessing the attribute scopes that Foundation defines.
- [FoundationAttributes](attributescopes/foundationattributes.md) — Attribute scopes that Foundation defines.

### SwiftUI-Defined Attributes

- [swiftUI](attributescopes/swiftui.md) — A property for accessing the attribute scopes that SwiftUI defines.
- [SwiftUIAttributes](attributescopes/swiftuiattributes.md) — Attribute scopes that SwiftUI defines.

### UIKit-Defined Attributes

- [uiKit](attributescopes/uikit.md) — A property for accessing the attribute scopes that UIKit defines.
- [UIKitAttributes](attributescopes/uikitattributes.md) — Attribute scopes that UIKit defines.

### AppKit-Defined Attributes

- [appKit](attributescopes/appkit.md) — A property for accessing the attribute scopes that AppKit defines.
- [AppKitAttributes](attributescopes/appkitattributes.md) — Attribute scopes that AppKit defines.

### Translation-Defined Attributes

- [translation](attributescopes/translation.md) — Provides access to translation-related attributes.
- [TranslationAttributes](attributescopes/translationattributes.md) — A scope that defines translation-specific properties on attributed strings.

### Structures

- [AccessibilityAttributes](attributescopes/accessibilityattributes.md)
- [CoreTextAttributes](attributescopes/coretextattributes.md) — A namespace for attributes defined by CoreText.
- [SpeechAttributes](attributescopes/speechattributes.md)

### Instance Properties

- [accessibility](attributescopes/accessibility.md)

## See Also

### Using Defined Attributes

- [AttributeDynamicLookup](attributedynamiclookup.md) — A type to support dynamic member lookup of attributes and containers.
- [ScopedAttributeContainer](scopedattributecontainer.md) — An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.
