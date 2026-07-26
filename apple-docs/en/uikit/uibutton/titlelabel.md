---
title: titleLabel
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/titlelabel
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/titlelabel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/titlelabel.json'
content_hash: 'sha256:c04aeb9b46c3e691'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# titleLabel

<sub>Instance Property</sub>

A view that displays the value of the `currentTitle` property for a button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var titleLabel: UILabel? { get }
```

## Discussion

Although this property is read-only, its own properties are read/write. Use these properties primarily to configure the text of the button. For example:

```objc
UIButton *button                  = [UIButton buttonWithType: UIButtonTypeSystem];
button.titleLabel.font            = [UIFont systemFontOfSize: 12];
button.titleLabel.lineBreakMode   = NSLineBreakByTruncatingTail;
```

Do not use the label object to set the text color or the shadow color. Instead, use the [- setTitleColor:forState:](<settitlecolor(__for_).md>) and [- setTitleShadowColor:forState:](<settitleshadowcolor(__for_).md>) methods of this class to make those changes. To set the actual text of the label, use [- setTitle:forState:](<settitle(__for_).md>) (`button.titleLabel.text` does not let you set the text).

The `titleLabel` property returns a value even if the button has not been displayed yet. The value of the property is  `nil` for system buttons.

## See Also

### Related Documentation

- [currentTitle](currenttitle.md) — The current title that is displayed on the button.

### Managing the title

- [- titleForState:](<title(for_).md>) — Returns the title associated with the specified state.
- [- setTitle:forState:](<settitle(__for_).md>) — Sets the title to use for the specified state.
- [- attributedTitleForState:](<attributedtitle(for_).md>) — Returns the styled title associated with the specified state.
- [- setAttributedTitle:forState:](<setattributedtitle(__for_).md>) — Sets the styled title to use for the specified state.
- [- titleColorForState:](<titlecolor(for_).md>) — Returns the title color used for a state.
- [- setTitleColor:forState:](<settitlecolor(__for_).md>) — Sets the color of the title to use for the specified state.
- [- titleShadowColorForState:](<titleshadowcolor(for_).md>) — Returns the shadow color of the title used for a state.
- [- setTitleShadowColor:forState:](<settitleshadowcolor(__for_).md>) — Sets the color of the title shadow to use for the specified state.
