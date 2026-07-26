---
title: rangeOfFragment
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 9.0+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcomponents/rangeoffragment
source_url: 'https://developer.apple.com/documentation/foundation/urlcomponents/rangeoffragment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcomponents/rangeoffragment.json'
content_hash: 'sha256:e8ccc3c7861782c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLComponents](../urlcomponents.md)

# rangeOfFragment

<sub>Instance Property</sub>

Returns the character range of the fragment in the string returned by the string property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var rangeOfFragment: Range<String.Index>? { get }
```

## Discussion

If the component does not exist, nil is returned.

> [!note] Note
> Zero length components are legal. For example, the URL string “scheme://:@/?#” has a zero length user, password, host, query and fragment; the URL strings “scheme:” and “” both have a zero length path.

## See Also

### Locating components in the URL string representation

- [rangeOfHost](rangeofhost.md) — Returns the character range of the host in the string returned by the string property.
- [rangeOfPassword](rangeofpassword.md) — Returns the character range of the password in the string returned by the string property.
- [rangeOfPath](rangeofpath.md) — Returns the character range of the path in the string returned by the string property.
- [rangeOfPort](rangeofport.md) — Returns the character range of the port in the string returned by the string property.
- [rangeOfQuery](rangeofquery.md) — Returns the character range of the query in the string returned by the string property.
- [rangeOfScheme](rangeofscheme.md) — Returns the character range of the scheme in the string returned by the string property.
- [rangeOfUser](rangeofuser.md) — Returns the character range of the user in the string returned by the string property.
