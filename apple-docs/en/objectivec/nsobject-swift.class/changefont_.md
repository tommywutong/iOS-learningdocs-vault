---
title: 'changeFont:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/changefont:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/changefont:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/changefont%3A.json'
content_hash: 'sha256:ba92094c82cb3a14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# changeFont:

<sub>Instance Method</sub>

Informs responders of a font change.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) changeFont:(id) sender;
```

## Parameters

- `sender` — The object that sent the message.

## Discussion

Generally this change is because the user changed the font either in the selection of a rich text field or in a whole plain text field. Any object that contains a font the user can change must respond to the [changeFont:](changefont_.md) message by sending a [convert(_:)](<../../appkit/nsfontmanager/convert(__).md>) message back to `sender` (an NSFontManager object) for each font in the selection. For more information, see Responding to Font Changes.

Be aware that [selectedFont](../../appkit/nsfontmanager/selectedfont.md) at this point may return unpredictable results. The font in this property may not be the last font selected, or there may be multiple fonts selected at the time [changeFont:](changefont_.md) is called. The use of [selectedFont](../../appkit/nsfontmanager/selectedfont.md) from within [changeFont:](changefont_.md) is strongly discouraged.

## See Also

### Related Documentation

- [convert(_:toFamily:)](<../../appkit/nsfontmanager/convert(__tofamily_).md>) — Returns a font whose traits are as similar as possible to those of the given font except for the font family, which is changed to the given family.
- [addFontTrait(_:)](<../../appkit/nsfontmanager/addfonttrait(__).md>) — Adds a trait to the font.
- [convert(_:toSize:)](<../../appkit/nsfontmanager/convert(__tosize_).md>) — Returns a font object whose traits are the same as those of the given font, except for the size, which is changed to the given size.
- [convert(_:toHaveTrait:)](<../../appkit/nsfontmanager/convert(__tohavetrait_).md>) — Returns a new version of the font object containing a single additional trait.
- [modifyFont(_:)](<../../appkit/nsfontmanager/modifyfont(__).md>) — Modifies a trait of the font.
- [convert(_:toNotHaveTrait:)](<../../appkit/nsfontmanager/convert(__tonothavetrait_).md>) — Returns a new version of a font object without the specified traits.
- [modifyFontViaPanel(_:)](<../../appkit/nsfontmanager/modifyfontviapanel(__).md>) — Modifies a font trait using input from the Font panel.
- [convertWeight(_:of:)](<../../appkit/nsfontmanager/convertweight(__of_).md>) — Returns a font object whose weight is greater or lesser than that of the given font.
- [convert(_:toFace:)](<../../appkit/nsfontmanager/convert(__toface_).md>) — Returns a font whose traits are as similar as possible to those of the given font except for the typeface, which is changed to the given typeface.
- [removeFontTrait(_:)](<../../appkit/nsfontmanager/removefonttrait(__).md>) — Removes a trait from the font.
