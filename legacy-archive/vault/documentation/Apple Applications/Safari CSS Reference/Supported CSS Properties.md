---
title: Safari CSS Reference
apple_id: TP40002050
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: User Experience
technology: WebKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariCSSRef/Articles/StandardCSSProperties.html
archived_at: '2026-07-15T05:19:03.072209Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari CSS Reference](Introduction%20to%20Safari%20CSS%20Reference.md)


[Next](Supported%20CSS%20Rules.md)[Previous](Explanation%20of%20Terms.md)

# Supported CSS Properties

Safari and WebKit implement a large subset of the CSS 2.1 Specification defined by the World Wide Web Consortium (W3C), along with portions of the CSS 3 Specification. This reference describes the supported properties and provides Safari availability information. If a property is not listed here, it is not implemented by Safari and WebKit.

The CSS attributes in this article are divided according to the groups defined by the W3C CSS Specification:

- [Box Model](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvbg66cnn5sgk3a) describes properties specific to the bounding boxes of block elements, including borders, padding, and margins. Additional box-related properties specific to tables are described separately in [Tables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvkgcytmmvzq).
- [Visual Formatting Model](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvlgs43vmfwem33snvqxi5djnztu233emvwa) describes properties that set the position and size of block elements.
- [Visual Effects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvlgs43vmfwekztgmvrxi4y) describes properties that adjust the visual presentation of block elements, including overflow behavior, resizing behavior, visibility, animation, transforms, and transitions.
- [Generated Content, Automatic Numbering, and Lists](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvdwk3tfojqxizleinxw45dfnz2ec5lun5wwc5djmnhhk3lcmvzgs3thmfxgitdjon2hg) describes properties that allow you to change the contents of an element, create automatically numbered sections and headings, and manipulate the style of list elements.
- [Paged Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvigcz3fmrgwkzdjme) describes properties associated with controlling appearance attributes specific to printed versions of a webpage, such as page break behavior.
- [Colors and Backgrounds](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvbw63dpojzwc3teijqwg23hojxxk3teom) describes properties that control the background of block-level elements and the color of text content within elements.
- [Fonts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvdg63tuom) describes properties specific to font selection for text within an element. It also describes properties used in downloadable font definitions.
- [Text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvjvomru) describes properties specific to text styles, spacing, and automatic scrolling (marquee).
- [Tables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvkgcytmmvzq) describes layout and styling properties specific to table elements.
- [User Interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvkxgzlsjfxhizlsmzqwgzi) describes properties that relate to user interface elements in the browser, such as scrolling text areas, scroll bars, and so on. It also describes properties that are outside the scope of the page content, such as cursor style and the callout shown when you touch and hold a touch target such as a link in iOS.

Defines a variety of border properties for an element within one declaration.

____Syntax____: |  |
```
border: border_width  border_style  border_color;
```

____Parameters____: ___border_width___: The width of the border on all sides.

___border_style___: The style of the border.

___border_color___: The color of the border.

____Subproperties____: - `[border-color](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzc2y3pnrxxe)`
- `[border-style](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzc243upfwgk)`
- `[border-width](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzc253jmr2gq)`

____Support Level____: CSS 2.1.

Defines a variety of properties for an element’s bottom border within one declaration.

____Syntax____: |  |
```
border-bottom: border_width  border_style  border_color;
```

____Parameters____: ___border_width___: The width of the bottom border.

___border_style___: The style of the border.

___border_color___: The color of the border.

____Subproperties____: - `[border-bottom-color](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf6ytpor2g63k7mnxwy33s)`
- `[border-bottom-style](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf6ytpor2g63k7on2hs3df)`
- `[border-bottom-width](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf6ytpor2g63k7o5uwi5di)`

____Support Level____: CSS 2.1.

Defines the color of the bottom border of an element.

____Syntax____: |  |
```
border-bottom-color: color
```

____Parameters____: ___color___: The color of the bottom border.

____Constants____: __`currentcolor`__: The value of the element’s `color` property.

__`-webkit-activelink`__: The default color of a hyperlink that is being clicked.

__`-webkit-focus-ring-color`__: The color that surrounds a UI element, such as a text field, that has focus.

__`-webkit-link`__: The default color of a hyperlink that has been visited.

__`-webkit-text`__: The default text color.

`activeborder`, `activecaption`, `appworkspace`, `aqua`, `background`, `black`, `blue`, `buttonface`, `buttonhighlight`, `buttonshadow`, `buttontext`, `captiontext`, `fuchsia`, `gray`, `graytext`, `green`, `grey`, `highlight`, `highlighttext`, `inactiveborder`, `inactivecaption`, `inactivecaptiontext`, `infobackground`, `infotext`, `lime`, `maroon`, `match`, `menu`, `menutext`, `navy`, `olive`, `orange`, `purple`, `red`, `scrollbar`, `silver`, `teal`, `threeddarkshadow`, `threedface`, `threedhighlight`, `threedlightshadow`, `threedshadow`, `transparent`, `white`, `window`, `windowframe`, `windowtext`, `yellow`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the style of the bottom border of an element.

____Syntax____: |  |
```
border-bottom-style: style;
```

____Parameters____: ___style___: The style of the bottom border.

____Constants____: `dashed`, `dotted`, `double`, `groove`, `hidden`, `inset`, `none`, `outset`, `ridge`, `solid`

____Support Level____: CSS 2.1.

Defines the width of the bottom border of an element.

____Syntax____: |  |
```
border-bottom-width: width;
```

____Parameters____: ___width___: The width of the bottom border.

____Types Allowed____: Length units

____Constants____: `medium`, `thick`, `thin`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the color of an element’s border.

____Syntax____: |  |
```
border-color: color;
```

____Parameters____: ___color___: The color of the border.

____Subproperties____: - `[border-bottom-color](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf6ytpor2g63k7mnxwy33s)`
- `[border-left-color](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf63dfmz2f6y3pnrxxe)`
- `[border-right-color](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf64tjm5uhix3dn5wg64q)`
- `[border-top-color](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf65dpobpwg33mn5za)`

____Support Level____: CSS 2.1.

Defines a variety of properties for an element’s left border within one declaration.

____Syntax____: |  |
```
border-left: border_width  border_style  border_color
```

____Parameters____: ___border_width___: The width of the left border.

___border_style___: The style of the left border.

___border_color___: The color of the left border.

____Subproperties____: - `[border-left-color](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf63dfmz2f6y3pnrxxe)`
- `[border-left-style](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf63dfmz2f643upfwgk)`
- `[border-left-width](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf63dfmz2f653jmr2gq)`

____Support Level____: CSS 2.1.

Defines the color of the left border of an element.

____Syntax____: |  |
```
border-left-color: color;
```

____Parameters____: ___color___: The color of the left border.

____Constants____: __`currentcolor`__: The value of the element’s `color` property.

__`-webkit-activelink`__: The default color of a hyperlink that is being clicked.

__`-webkit-focus-ring-color`__: The color that surrounds a UI element, such as a text field, that has focus.

__`-webkit-link`__: The default color of a hyperlink that has been visited.

__`-webkit-text`__: The default text color.

`activeborder`, `activecaption`, `appworkspace`, `aqua`, `background`, `black`, `blue`, `buttonface`, `buttonhighlight`, `buttonshadow`, `buttontext`, `captiontext`, `fuchsia`, `gray`, `graytext`, `green`, `grey`, `highlight`, `highlighttext`, `inactiveborder`, `inactivecaption`, `inactivecaptiontext`, `infobackground`, `infotext`, `lime`, `maroon`, `match`, `menu`, `menutext`, `navy`, `olive`, `orange`, `purple`, `red`, `scrollbar`, `silver`, `teal`, `threeddarkshadow`, `threedface`, `threedhighlight`, `threedlightshadow`, `threedshadow`, `transparent`, `white`, `window`, `windowframe`, `windowtext`, `yellow`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the style of the left border of an element.

____Syntax____: |  |
```
border-left-style: style;
```

____Parameters____: ___style___: The style of the left border.

____Constants____: `dashed`, `dotted`, `double`, `groove`, `hidden`, `inset`, `none`, `outset`, `ridge`, `solid`

____Support Level____: CSS 2.1.

Defines the width of the left border of an element.

____Syntax____: |  |
```
border-left-width: width;
```

____Parameters____: ___width___: The width of the left border.

____Types Allowed____: Length units

____Constants____: `medium`, `thick`, `thin`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines a variety of properties for an element’s right border within one declaration.

____Syntax____: |  |
```
border-right: border_width border_style border_color;
```

____Parameters____: ___border_width___: The width of the right border.

___border_style___: The style of the right border.

___border_color___: The color of the right border.

____Subproperties____: - `[border-right-color](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf64tjm5uhix3dn5wg64q)`
- `[border-right-style](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf64tjm5uhix3tor4wyzi)`
- `[border-right-width](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf64tjm5uhix3xnfshi2a)`

____Support Level____: CSS 2.1.

Defines the color of the right border of an element.

____Syntax____: |  |
```
border-right-color: color;
```

____Parameters____: ___color___: The color of the right border.

____Constants____: __`currentcolor`__: The value of the element’s `color` property.

__`-webkit-activelink`__: The default color of a hyperlink that is being clicked.

__`-webkit-focus-ring-color`__: The color that surrounds a UI element, such as a text field, that has focus.

__`-webkit-link`__: The default color of a hyperlink that has been visited.

__`-webkit-text`__: The default text color.

`activeborder`, `activecaption`, `appworkspace`, `aqua`, `background`, `black`, `blue`, `buttonface`, `buttonhighlight`, `buttonshadow`, `buttontext`, `captiontext`, `fuchsia`, `gray`, `graytext`, `green`, `grey`, `highlight`, `highlighttext`, `inactiveborder`, `inactivecaption`, `inactivecaptiontext`, `infobackground`, `infotext`, `lime`, `maroon`, `match`, `menu`, `menutext`, `navy`, `olive`, `orange`, `purple`, `red`, `scrollbar`, `silver`, `teal`, `threeddarkshadow`, `threedface`, `threedhighlight`, `threedlightshadow`, `threedshadow`, `transparent`, `white`, `window`, `windowframe`, `windowtext`, `yellow`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the style of the right border of an element.

____Syntax____: |  |
```
border-right-style: style;
```

____Parameters____: ___style___: The style of the right border.

____Constants____: `dashed`, `dotted`, `double`, `groove`, `hidden`, `inset`, `none`, `outset`, `ridge`, `solid`

____Support Level____: CSS 2.1.

Defines the width of the right border of an element.

____Syntax____: |  |
```
border-right-width: width;
```

____Parameters____: ___width___: The width of the right border.

____Types Allowed____: Length units

____Constants____: `medium`, `thick`, `thin`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the style for an element’s border.

____Syntax____: |  |
```
border-style: style;
```

____Parameters____: ___style___: The style of the border.

____Subproperties____: - `[border-bottom-style](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf6ytpor2g63k7on2hs3df)`
- `[border-left-style](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf63dfmz2f643upfwgk)`
- `[border-right-style](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf64tjm5uhix3tor4wyzi)`
- `[border-top-style](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf65dpobpxg5dznrsq)`

____Support Level____: CSS 2.1.

Defines a variety of properties for an element’s top border within one declaration.

____Syntax____: |  |
```
border-top: border_width border_style border_color;
```

____Parameters____: ___border_width___: The width of the top border.

___border_style___: The style of the top border.

___border_color___: The color of the top border.

____Subproperties____: - `[border-top-color](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf65dpobpwg33mn5za)`
- `[border-top-style](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf65dpobpxg5dznrsq)`
- `[border-top-width](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf65dpobpxo2leorua)`

____Support Level____: CSS 2.1.

Defines the color of the top border of an element.

____Syntax____: |  |
```
border-top-color: color;
```

____Parameters____: ___color___: The color of the top border.

____Constants____: __`currentcolor`__: The value of the element’s `color` property.

__`-webkit-activelink`__: The default color of a hyperlink that is being clicked.

__`-webkit-focus-ring-color`__: The color that surrounds a UI element, such as a text field, that has focus.

__`-webkit-link`__: The default color of a hyperlink that has been visited.

__`-webkit-text`__: The default text color.

`activeborder`, `activecaption`, `appworkspace`, `aqua`, `background`, `black`, `blue`, `buttonface`, `buttonhighlight`, `buttonshadow`, `buttontext`, `captiontext`, `fuchsia`, `gray`, `graytext`, `green`, `grey`, `highlight`, `highlighttext`, `inactiveborder`, `inactivecaption`, `inactivecaptiontext`, `infobackground`, `infotext`, `lime`, `maroon`, `match`, `menu`, `menutext`, `navy`, `olive`, `orange`, `purple`, `red`, `scrollbar`, `silver`, `teal`, `threeddarkshadow`, `threedface`, `threedhighlight`, `threedlightshadow`, `threedshadow`, `transparent`, `white`, `window`, `windowframe`, `windowtext`, `yellow`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the style of the top border of an element.

____Syntax____: |  |
```
border-top-style: style;
```

____Parameters____: ___style___: The style of the top border.

____Constants____: `dashed`, `dotted`, `double`, `groove`, `hidden`, `inset`, `none`, `outset`, `ridge`, `solid`

____Support Level____: CSS 2.1.

Defines the width of the top border of an element.

____Syntax____: |  |
```
border-top-width: width;
```

____Parameters____: ___width___: The width of the top border.

____Types Allowed____: Length units

____Constants____: `medium`, `thick`, `thin`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the width of the border of an element.

____Syntax____: |  |
```
border-width: width;
```

____Parameters____: ___width___: The width of the border.

____Subproperties____: - `[border-bottom-width](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf6ytpor2g63k7o5uwi5di)`
- `[border-left-width](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf63dfmz2f653jmr2gq)`
- `[border-right-width](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf64tjm5uhix3xnfshi2a)`
- `[border-top-width](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrg64temvzf65dpobpxo2leorua)`

____Support Level____: CSS 2.1.

Defines the width of an element’s outer-element margin.

____Syntax____: |  |
```
margin: value;
margin: margin_top margin_right margin_bottom margin_left
```

____Parameters____: ___value___: The width of the margin.

___margin_top___: The width of the top margin.

___margin_right___: The width of the right margin.

___margin_bottom___: The width of the bottom margin.

___margin_left___: The width of the left margin.

____Subproperties____: - `[margin-bottom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvwwc4thnfxc2ytpor2g63i)`
- `[margin-left](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvwwc4thnfxc23dfmz2a)`
- `[margin-right](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvwwc4thnfxc24tjm5uhi)`
- `[margin-top](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvwwc4thnfxc25dpoa)`

____Support Level____: CSS 2.1.

Defines the width of the bottom margin of an element.

____Syntax____: |  |
```
margin-bottom: value;
```

____Parameters____: ___value___: The width of the bottom margin.

____Types Allowed____: Numbers as a percentage, length units

____Constants____: `auto`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the width of the left margin of an element.

____Syntax____: |  |
```
margin-left: value;
```

____Parameters____: ___value___: The width of the left margin.

____Types Allowed____: Numbers as a percentage, length units

____Constants____: `auto`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the width of the right margin of an element.

____Syntax____: |  |
```
margin-right: value;
```

____Parameters____: ___value___: The width of the right margin.

____Types Allowed____: Numbers as a percentage, length units

____Constants____: `auto`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the width of the top margin of an element.

____Syntax____: |  |
```
margin-top: value;
```

____Parameters____: ___value___: The width of the top margin.

____Types Allowed____: Numbers as a percentage, length units

____Constants____: `auto`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the width of an element’s inner-element padding.

____Syntax____: |  |
```
padding: value;
padding: padding_top padding_right padding_bottom padding_left
```

____Parameters____: ___value___: The width of the padding on all sides.

___padding_top___: The width of the top padding.

___padding_right___: The width of the right padding.

___padding_bottom___: The width of the bottom padding.

___padding_left___: The width of the left padding.

____Subproperties____: - `[padding-bottom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvygczdenfxgollcn52hi33n)`
- `[padding-left](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvygczdenfxgollmmvthi)`
- `[padding-right](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvygczdenfxgollsnftwq5a)`
- `[padding-top](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvygczdenfxgollun5ya)`

____Support Level____: CSS 2.1.

Defines the width of the bottom padding of an element.

____Syntax____: |  |
```
padding-bottom: value;
```

____Parameters____: ___value___: The width of the bottom padding.

____Types Allowed____: Numbers as a percentage, length units

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the width of the left padding of an element.

____Syntax____: |  |
```
padding-left: value;
```

____Parameters____: ___value___: The width of the left padding.

____Types Allowed____: Numbers as a percentage, length units

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the width of the right padding of an element.

____Syntax____: |  |
```
padding-right: value;
```

____Parameters____: ___value___: The width of the right padding.

____Types Allowed____: Numbers as a percentage, length units

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the width of the top padding of an element.

____Syntax____: |  |
```
padding-top: value;
```

____Parameters____: ___value___: The width of the top padding.

____Types Allowed____: Numbers as a percentage, length units

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Specifies that the bottom-left corner of a box be rounded with the specified radius.

____Syntax____: |  |
```
-webkit-border-bottom-left-radius: radius;
-webkit-border-bottom-left-radius: horizontal_radius vertical_radius;
```

____Parameters____: ___radius___: The radius of the rounded corner.

___horizontal_radius___: The horizontal radius of the rounded corner.

___vertical_radius___: The vertical radius of the rounded corner.

____Types Allowed____: Length units

____Subproperties____: - `[-webkit-border-bottom-right-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfvrg65dun5ws24tjm5uhillsmfsgs5lt)`
- `[-webkit-border-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfvzgczdjovzq)`
- `[-webkit-border-top-left-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfv2g64bnnrswm5bnojqwi2lvom)`
- `[-webkit-border-top-right-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfv2g64bnojuwo2dufvzgczdjovzq)`

____Discussion____: This property takes either one or two parameters. If one parameter is specified, it controls both the horizontal and vertical radii of a quarter ellipse. If two parameters are specified, the first parameter normally represents the horizontal radius and the second parameter represents the remaining radius. (Compatibility note: In Internet Explorer, if writing-mode is specified as `tb-rl`, these parameters are reversed.)

Changes to this property can be animated.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 1.0 and later.

____Support Level____: Experimental CSS 3.

Specifies that the bottom-right corner of a box be rounded with the specified radius.

____Syntax____: |  |
```
-webkit-border-bottom-right-radius: radius;
-webkit-border-bottom-right-radius: horizontal_radius vertical_radius;
```

____Parameters____: ___radius___: The radius of the rounded corner.

___horizontal_radius___: The horizontal radius of the rounded corner.

___vertical_radius___: The vertical radius of the rounded corner.

____Types Allowed____: Length units

____Subproperties____: - `[-webkit-border-bottom-left-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfvrg65dun5ws23dfmz2c24tbmruxk4y)`
- `[-webkit-border-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfvzgczdjovzq)`
- `[-webkit-border-top-left-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfv2g64bnnrswm5bnojqwi2lvom)`
- `[-webkit-border-top-right-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfv2g64bnojuwo2dufvzgczdjovzq)`

____Discussion____: This property takes either one or two parameters. If one parameter is specified, it controls both the horizontal and vertical radii of a quarter ellipse. If two parameters are specified, the first parameter normally represents the horizontal radius and the second parameter represents the remaining radius. (Compatibility note: In Internet Explorer, if writing-mode is specified as `tb-rl`, these parameters are reversed.)

Changes to this property can be animated.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 1.0 and later.

____Support Level____: Experimental CSS 3.

Specifies an image as the border for a box.

____Syntax____: |  |
```
-webkit-border-image: method top right bottom left x_repeat y_repeat
-webkit-border-image: method top right bottom left / border x_repeat y_repeat
-webkit-border-image: method top right bottom left / top_border right_border bottom_border left_border x_repeat y_repeat
```

____Parameters____: ___method___: The method of which to produce the image. This could be expressed by the `url()` syntax, which contains the URI of the image (in the same fashion as the `background-image` property), or by a procedural function such as `gradient()`.

___top___: The distance from the top edge of the image.

___right___: The distance from the right edge of the image.

___bottom___: The distance from the bottom edge of the image.

___left___: The distance from the left edge of the image.

___x_repeat___: The horizontal repeat style.

___y_repeat___: The vertical repeat style.

___border___: The width of the border on all sides.

___top_border___: The width of the top border.

___right_border___: The width of the right border.

___bottom_border___: The width of the bottom border.

___left_border___: The width of the left border.

____Constants____: __`repeat`__: The image is tiled.

__`round`__: The image is stretched before it is tiled to prevent partial tiles

__`stretch`__: The image is stretched to the size of the border.

____Discussion____: The specified image is cut into nine pieces according to the length values given. This property applies to any box, including inline elements, but does not apply to table cells if the `border-collapse` property is set to `collapse`.

The first five fields are required. The four inset values that follow `method` represent distances from the top, right, bottom, and left edges of the image. If no unit is specified, they represent actual pixels in the original image (assuming a raster image). If a unit (such as `px`) is specified, they represent CSS units (which may or may not be the same thing). The values may also be specified as a percentage of the size of the image as well as vector coordinates.

After the required fields, you can optionally include a border width field or fields, preceded by a slash (`/`). You can specify all four border widths individually or specify a single value that applies to all four fields. If these values are not the same size as the inset values, the slices of the original image are scaled to fit. Note that `border-width` constants like `thick` are not valid.

Finally, you can specify a repeat style in each direction. These values affect how the top, bottom, left, right, and center portions are altered to fit the required dimensions, and can be any of the following: `repeat` (tiled), `stretch`, or `round` (the `round` style is like tiling, except that it stretches all nine pieces slightly so that there is no partial tile at the end).

____Availability____: Available in Safari 3.0 and later.

Available in iOS 1.0 and later.

____Support Level____: Experimental CSS 3.

Specifies that the corners of a box be rounded with the specified radius.

____Syntax____: |  |
```
-webkit-border-radius: radius;
-webkit-border-radius: horizontal_radius vertical_radius;
```

____Parameters____: ___radius___: The radius of the rounded corners.

___horizontal_radius___: The horizontal radius of the rounded corners.

___vertical_radius___: The vertical radius of the rounded corners.

____Types Allowed____: Length units

____Subproperties____: - `[-webkit-border-bottom-left-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfvrg65dun5ws23dfmz2c24tbmruxk4y)`
- `[-webkit-border-bottom-right-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfvrg65dun5ws24tjm5uhillsmfsgs5lt)`
- `[-webkit-border-top-left-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfv2g64bnnrswm5bnojqwi2lvom)`
- `[-webkit-border-top-right-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfv2g64bnojuwo2dufvzgczdjovzq)`

____Discussion____: This property takes either one or two parameters. If one parameter is specified, it controls both the horizontal and vertical radii of a quarter ellipse. If two parameters are specified, the first parameter normally represents the horizontal radius and the second parameter represents the remaining radius. (Compatibility note: In Internet Explorer, if writing-mode is specified as `tb-rl`, these parameters are reversed.)

____Availability____: Available in Safari 3.0 and later.

Available in iOS 1.0 and later.

____Support Level____: Experimental CSS 3.

Specifies that the top-left corner of a box be rounded with the specified radius.

____Syntax____: |  |
```
-webkit-border-top-left-radius: radius;
-webkit-border-top-left-radius: horizontal_radius vertical_radius;
```

____Parameters____: ___radius___: The radius of the rounded corner.

___horizontal_radius___: The horizontal radius of the rounded corner.

___vertical_radius___: The vertical radius of the rounded corner.

____Types Allowed____: Length units

____Subproperties____: - `[-webkit-border-bottom-left-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfvrg65dun5ws23dfmz2c24tbmruxk4y)`
- `[-webkit-border-bottom-right-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfvrg65dun5ws24tjm5uhillsmfsgs5lt)`
- `[-webkit-border-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfvzgczdjovzq)`
- `[-webkit-border-top-right-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfv2g64bnojuwo2dufvzgczdjovzq)`

____Discussion____: This property takes either one or two parameters. If one parameter is specified, it controls both the horizontal and vertical radii of a quarter ellipse. If two parameters are specified, the first parameter normally represents the horizontal radius and the second parameter represents the remaining radius. (Compatibility note: In Internet Explorer, if writing-mode is specified as `tb-rl`, these parameters are reversed.)

Changes to this property can be animated.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 1.0 and later.

____Support Level____: Experimental CSS 3.

Specifies that the top-right corner of a box be rounded with the specified radius.

____Syntax____: |  |
```
-webkit-border-top-right-radius: radius;
-webkit-border-top-right-radius: horizontal_radius vertical_radius;
```

____Parameters____: ___radius___: The radius of the rounded corner.

___horizontal_radius___: The horizontal radius of the rounded corner.

___vertical_radius___: The vertical radius of the rounded corner.

____Types Allowed____: Length units

____Subproperties____: - `[-webkit-border-bottom-left-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfvrg65dun5ws23dfmz2c24tbmruxk4y)`
- `[-webkit-border-bottom-right-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfvrg65dun5ws24tjm5uhillsmfsgs5lt)`
- `[-webkit-border-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfvzgczdjovzq)`
- `[-webkit-border-top-right-radius](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfv2g64bnojuwo2dufvzgczdjovzq)`

____Discussion____: This property takes either one or two parameters. If one parameter is specified, it controls both the horizontal and vertical radii of a quarter ellipse. If two parameters are specified, the first parameter normally represents the horizontal radius and the second parameter represents the remaining radius. (Compatibility note: In Internet Explorer, if writing-mode is specified as `tb-rl`, these parameters are reversed.)

Changes to this property can be animated.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 1.0 and later.

____Support Level____: Experimental CSS 3.

Specifies that the size of a box be measured according to either its content (default) or its total size including borders.

____Syntax____: |  |
```
-webkit-box-sizing: sizing_model;
```

____Parameters____: ___sizing_model___: The model by which the size of the box is measured.

____Constants____: __`border-box`__: The box size includes borders in addition to content.

__`content-box`__: The box size only includes content.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 1.1 and later. (Called `box-sizing` in iOS 1.0.)

____Support Level____: Experimental CSS 3.

Applies a drop shadow effect to the border box of an object.

____Syntax____: |  |
```
-webkit-box-shadow: hoff voff blur color;
```

____Parameters____: ___hoff___: The horizontal offset of the shadow.

___voff___: The vertical offset of the shadow.

___blur___: The blur radius of the shadow.

___color___: The color of the shadow.

____Constants____: __`none`__: The box has no shadow.

____Discussion____: This property takes four parameters. The first two are horizontal and vertical offsets—down for horizontal, and to the right for vertical. The third value is a blur radius. The fourth value is the color of the shadow. Changes to this property can be animated.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Experimental CSS 3.

Specifies the behavior of an element’s bottom margin if it is adjacent to an element with a margin. Elements can maintain their respective margins or share a single margin between them.

____Syntax____: |  |
```
-webkit-margin-bottom-collapse: collapse_behavior;
```

____Parameters____: ___collapse_behavior___: The behavior of the bottom margin.

____Constants____: __`collapse`__: Two adjacent margins are collapsed into a single margin.

__`discard`__: The element’s margin is discarded if it is adjacent to another element with a margin.

__`separate`__: Two adjacent margins remain separate.

____Discussion____: This property allows you to emulate the behavior of some browsers in quirks mode where table cell margins are collapsed into the borders of vertically adjacent cells.

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-margin-bottom-collapse` in Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Apple extension.

Specifies the behavior of an element’s vertical margins if it is adjacent to an element with a margin. Elements can maintain their respective margins or share a single margin between them.

____Syntax____: |  |
```
-webkit-margin-collapse: collapse_behavior;
```

____Parameters____: ___collapse_behavior___: The behavior of the vertical margins.

____Subproperties____: - `[-webkit-margin-bottom-collapse](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillnmfzgo2lofvrg65dun5ws2y3pnrwgc4dtmu)`
- `[-webkit-margin-top-collapse](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillnmfzgo2lofv2g64bnmnxwy3dbobzwk)`

____Discussion____: This property allows you to emulate the behavior of some browsers in quirks mode where table cell margins are collapsed into the borders of vertically adjacent cells.

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-magin-collapse` in Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Apple extension.

Provides the width of the starting margin.

____Syntax____: |  |
```
-webkit-margin-start: width;
```

____Parameters____: ___width___: The width of the starting margin.

____Types Allowed____: Numbers as a percentage, length units

____Constants____: __`auto`__: The margin is automatically determined.

____Discussion____: If the writing direction is left-to-right, this value overrides `margin-left`. If the writing direction is right-to-left, this value overrides `margin-right`.

____Availability____: Available in Safari 3.0 and later. (Called it is `-khtml-margin-start` in Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Apple extension.

Specifies the behavior of an element’s top margin if it is adjacent to an element with a margin. Elements can maintain their respective margins or share a single margin between them.

____Syntax____: |  |
```
-webkit-margin-top-collapse: collapse_behavior;
```

____Parameters____: ___collapse_behavior___: The behavior of the top margin.

____Constants____: __`collapse`__: Two adjacent margins are collapsed into a single margin.

__`discard`__: The element’s margin is discarded if it is adjacent to another element with a margin.

__`separate`__: Two adjacent margins remain separate.

____Discussion____: This property allows you to emulate the behavior of some browsers in quirks mode where table cell margins are collapsed into the borders of vertically adjacent cells.

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-magin-top-collapse` in Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Apple extension.

Provides the width of the starting padding.

____Syntax____: |  |
```
-webkit-padding-start: width;
```

____Parameters____: ___width___: The width of the starting padding.

____Types Allowed____: Numbers as a percentage, length units

____Discussion____: If the writing direction is left-to-right, this value overrides `padding-left`. If the writing direction is right-to-left, this value overrides `padding-right`.

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-padding-start` in Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Apple extension.

Defines the location of the bottom edge of the element for both absolute and relative positioning.

____Syntax____: |  |
```
bottom: position;
```

____Parameters____: ___position___: The location of the bottom edge of the element.

____Types Allowed____: Numbers as a percentage, length units

____Constants____: `auto`

____Discussion____: Changes to this property can be animated.

____Availability____: Available in Safari 1.0 and later.

Available in iOS 1.0 and later

____Support Level____: CSS 2.1.

Defines the sides of an element on which no floating elements are permitted to be displayed.

____Syntax____: |  |
```
clear: value;
```

____Parameters____: ___value___: The sides of the element on which no floating elements can be displayed.

____Constants____: `both`, `left`, `none`, `right`

____Availability____: Available in Safari 1.0 and later.

Available in iOS 1.0 and later

____Support Level____: CSS 2.1.

Sets the direction in which text is rendered.

____Syntax____: |  |
```
direction: value;
```

____Parameters____: ___value___: The direction of the text.

____Constants____: `ltr`, `rtl`

____Availability____: Available in Safari 1.0 and later.

Available in iOS 1.0 and later

____Support Level____: CSS 2.1.

Defines how an element is displayed onscreen.

____Syntax____: |  |
```
display: mode;
```

____Parameters____: ___mode___: The display mode.

____Constants____: ___-webkit-box___: The element is displayed in its own flex box.

___-webkit-inline-box___: The element is displayed inline in its own flex box.

`block`, `compact`, `inline`, `inline-block`, `inline-table`, `list-item`, `none`, `run-in`, `table`, `table-caption`, `table-cell`, `table-column`, `table-column-group`, `table-footer-group`, `table-header-group`, `table-row`, `table-row-group`

____Availability____: Available in Safari 1.0 and later.

Available in iOS 1.0 and later

____Support Level____: CSS 2.1.

Indicates whether an element (often a graphic) should be pulled out of the normal text flow and floated toward a particular horizontal position within its enclosing element.

____Syntax____: |  |
```
float: position;
```

____Parameters____: ___position___: The position for the element to be floated toward.

____Constants____: `center`, `left`, `none`, `right`

____Discussion____: If `float` is set to `none`, the element is displayed inline wherever it appears within the text flow.

If `float` is set to a positional value, the element is laid out as it normally would be within the flow, then is moved as far as possible towards the specified position. If an element is vertically positioned such that it would run into another element that is part of the same float, it stops at the point of contact. Thus, in effect, this causes these floating elements to stack up at the specified horizontal position.

If the width of a series of stacked floating elements exceeds the width of the enclosing box, further elements wrap to a new row. You can force an element to always wrap to a new row by setting the `clear` property on that element. (See `[clear](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrwyzlboi)` for more information.)

__Note:__ With the exception of elements with intrinsic width (an `img` tag, for example), you should always set the width property on floating elements to ensure consistent behavior across browsers.

____Availability____: Available in Safari 1.0 and later.

Available in iOS 1.0 and later

____Support Level____: CSS 2.1.

Defines the height of a structural element.

____Syntax____: |  |
```
height: value;
```

____Parameters____: ___value___: The height of the element.

____Types Allowed____: Numbers as a percentage, length units, nonnegative values

____Constants____: `auto`, `intrinsic`, `min-intrinsic`

____Discussion____: This property has no effect on inline elements. Changes to this property can be animated.

____Availability____: Available in Safari 1.0 and later.

Available in iOS 1.0 and later

____Support Level____: CSS 2.1.

Defines the location of the left edge of the element for both absolute and relative positioning.

____Syntax____: |  |
```
left: position;
```

____Parameters____: ___position___: The location of the left edge of the element.

____Types Allowed____: Numbers as a percentage, length units

____Constants____: `auto`

____Discussion____: Changes to this property can be animated.

____Availability____: Available in Safari 1.0 and later.

Available in iOS 1.0 and later

____Support Level____: CSS 2.1.

Defines the vertical interline spacing of lines within the text of an element.

____Syntax____: |  |
```
line-height: height;
```

____Parameters____: ___height___: The interline spacing value.

____Types Allowed____: Floating-point numbers, Numbers as a percentage, length units

____Constants____: `normal`

____Discussion____: Changes to this property can be animated.

____Availability____: Available in Safari 1.0 and later.

Available in iOS 1.0 and later

____Support Level____: CSS 2.1.

Defines the maximum height of a structural element.

____Syntax____: |  |
```
max-height: height;
```

____Parameters____: ___height___: The maximum height.

____Constants____: `intrinsic`, `min-intrinsic`, `none`

____Availability____: Available in Safari 1.3 and later. (Positioned elements require Safari 2.0.2 and later.)

Available in iOS 1.0 and later.

____Support Level____: CSS 2.1.

Defines the maximum width of a structural element.

____Syntax____: |  |
```
max-width: width;
```

____Parameters____: ___width___: The maximum width.

____Constants____: `intrinsic`, `min-intrinsic`, `none`

____Availability____: Available in Safari 1.0 and later. (Positioned elements require Safari 2.0.2 and later.)

Available in iOS 1.0 and later.

____Support Level____: CSS 2.1.

Defines the minimum height of a structural element.

____Syntax____: |  |
```
min-height: height;
```

____Parameters____: ___height___: The minimum height.

____Types Allowed____: Numbers as a percentage, length units, nonnegative values

____Constants____: `intrinsic`, `min-intrinsic`

____Availability____: Available in Safari 1.3 and later. (Positioned elements require Safari 2.0.2 and later.)

Available in iOS 1.0 and later.

____Support Level____: CSS 2.1.

Defines the minimum width of a structural element.

____Syntax____: |  |
```
min-width: width;
```

____Parameters____: ___width___: The minimum width.

____Types Allowed____: Numbers as a percentage, length units, nonnegative values

____Constants____: `intrinsic`, `min-intrinsic`

____Availability____: Available in Safari 1.0 and later. (Positioned elements require Safari 2.0.2 and later.)

Available in iOS 1.0 and later.

____Support Level____: CSS 2.1.

Specifies how to blend the offscreen rendering into the current composite rendering.

____Syntax____: |  |
```
opacity: value;
```

____Parameters____: ___value___: The opacity.

____Types Allowed____: Floating-point numbers

____Discussion____: Changes to this property can be animated.

____Availability____: Available in Safari 2.0 and later. (Called `-khtml-opacity` in Safari 1.1.)

Available in iOS 1.0 and later.

____Support Level____: CSS 2.1.

Specifies how an element is positioned.

____Syntax____: |  |
```
position: positioning_model;
```

____Parameters____: ___positioning_model___: The positioning model for the element.

____Constants____: `absolute`, `fixed`, `relative`, `static`

____Discussion____: This property affects the behavior of positional properties such as `float` and `left`/`right`/`top`/`bottom`.

____Support Level____: CSS 2.1.

Defines the location of the right edge of the element for both absolute and relative positioning.

____Syntax____: |  |
```
right: position;
```

____Parameters____: ___position___: The location of the right edge of the element.

____Types Allowed____: Numbers as a percentage, length units

____Constants____: `auto`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the location of the top edge of the element for both absolute and relative positioning.

____Syntax____: |  |
```
top: position;
```

____Parameters____: ___position___: The opacity.

____Types Allowed____: The location of the top edge of the element.

____Constants____: `auto`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the Unicode bidirectional text algorithm used to display text.

____Syntax____: |  |
```
unicode-bidi: algorithm;
```

____Parameters____: ___algorithm___: The bidirectional text algorithm.

____Constants____: `bidi-override`, `embed`, `normal`

____Discussion____: This property _must_ be set if you intend to change the direction of inline text.

____Support Level____: CSS 2.1.

Defines the vertical alignment of elements inline with text.

____Syntax____: |  |
```
vertical-align: position;
```

____Parameters____: ___position___: The vertical alignment of the text.

____Types Allowed____: Numbers as a percentage, length units

____Constants____: ___-webkit-baseline-middle___: The center of the element is aligned with the baseline of the text.

`baseline`, `bottom`, `middle`, `sub`, `super`, `text-bottom`, `text-top`, `top`

____Support Level____: CSS 2.1.

Defines the width of a structural element.

____Syntax____: |  |
```
width: value;
```

____Parameters____: ___value___: The width of the element.

____Types Allowed____: Numbers as a percentage, length units, nonnegative values

____Constants____: `auto`, `intrinsic`, `min-intrinsic`

____Discussion____: This property has no effect on inline elements. Changes to this property can be animated.

____Support Level____: CSS 2.1.

Overrides the default stacking order of elements.

____Syntax____: |  |
```
z-index: distance;
```

____Parameters____: ___distance___: The z-index of the element.

____Constants____: `auto`

____Discussion____: Formally, the `z-index` property sets the height of an element above the drawing plane (in pixels). Its primary use is to override the default stacking order of elements.

By default, elements are stacked in the order in which they appear within the DOM tree; later elements appear on top of earlier elements. If you set a `z-index` value for an element, that element is displayed on top of all elements with a lower `z-index` value, underneath all elements with a higher `z-index` value, and stacked according to its position in the DOM tree relative to all elements with the same `z-index` value.

By default, elements are assigned a `z-index` value of `auto`, which is equivalent to zero (`0`).

Changes to this property can be animated.

____Support Level____: CSS 2.1.

Specifies the magnification of an element.

____Syntax____: |  |
```
zoom: vMagnification;
```

____Parameters____: ___vMagnification___: The magnification of the element.

____Types Allowed____: Numbers as a percentage, floating-point numbers, nonnegative values

____Constants____: __`normal`__: A zoom level of `100%`.

__`reset`__: Specifies that an element not scale at all when a zoom is applied.

____Discussion____: Children of elements with the `zoom` property do not inherit the property, but they are affected by it. The default value of the `zoom` property is `normal`, which is equivalent to a percentage value of `100%` or a floating-point value of `1.0`.

Changes to this property can be animated.

____Availability____: Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Defines the clipping region.

____Syntax____: |  |
```
clip: shape;
```

____Parameters____: ___shape___: The clipping region.

____Constants____: `auto`

____Discussion____: A clipping region is the portion of an element in which its content will be rendered. The default is to render content within the entire element size.

If you do not use the constant `auto`, the value should be in the form of a supported shape (currently limited to `rect`).

For example, `clip: rect(3px 20px 5px 8px);` defines a rectangular clip region with a top edge 3 pixels from the top of the element, a right edge 20 pixels from the left edge of the element, a bottom border 5 pixels from the top of the element, and a left border 8 pixels from the left edge of the element.

____Support Level____: CSS 2.1.

Defines the treatment of content that overflows the element’s bounds.

____Syntax____: |  |
```
overflow: behavior;
```

____Parameters____: ___behavior___: The overflow behavior.

____Subproperties____: - `[overflow-x](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvxxmzlsmzwg65znpa)`
- `[overflow-y](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvxxmzlsmzwg65znpe)`

____Discussion____: This property allows you to choose the behavior for content that overflows the element bounds, such as providing scroll bars or hiding the overflowed content.

____Support Level____: CSS 2.1.

Defines the treatment of content that overflows the element’s horizontal bounds.

____Syntax____: |  |
```
overflow-x: behavior;
```

____Parameters____: ___behavior___: The overflow behavior.

____Constants____: __`-webkit-marquee`__: The content behaves like a marquee.

`auto`, `hidden`, `overlay`, `scroll`, `visible`

____Availability____: Available in Safari 3.0 and later.

Available in iOS 1.0 and later.

____Support Level____: Stable CSS 3.

Defines the treatment of content that overflows the element’s vertical bounds.

____Syntax____: |  |
```
overflow-y: behavior;
```

____Parameters____: ___behavior___: The overflow behavior.

____Constants____: __`-webkit-marquee`__: The content behaves like a marquee.

`auto`, `hidden`, `overlay`, `scroll`, `visible`

____Availability____: Available in Safari 3.0 and later.

Available in iOS 1.0 and later.

____Support Level____: Stable CSS 3.

Specifies the directions in which resizing is allowed.

____Syntax____: |  |
```
resize: direction;
```

____Parameters____: ___direction___: The directions in which resizing is allowed.

____Constants____: `auto`, `both`, `horizontal`, `none`, `vertical`

____Availability____: Available in Safari 3.0 and later.

Available in iOS 1.0 and later.

____Support Level____: Stable CSS 3.

Defines whether or not an element is visible onscreen.

____Syntax____: |  |
```
visibility: value;
```

____Constants____: `collapse`, `hidden`, `visible`

____Discussion____: Note that elements made invisible using this property still take up space onscreen. Changes to this property can be animated.

____Availability____: Available in Safari 1.0 and later. (All supported except for `collapse`.)

Available in iOS 1.0 and later.

____Support Level____: CSS 2.1.

Combines common animation properties into a single property.

____Syntax____: |  |
```
-webkit-animation: name duration timing_function delay iteration_count direction [, ... ];
```

____Parameters____: ___name___: See `[-webkit-animation-name](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvpxozlcnnuxix3bnzuw2ylunfxw4x3omfwwk)` for details.

___duration___: See `-webkit-animation-duration` for details.

___timing_function___: See `[-webkit-animation-timing-function](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvpxozlcnnuxix3bnzuw2ylunfxw4x3unfwws3thl5thk3tdoruw63q)` for details.

___delay___: See `[-webkit-animation-delay](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvpxozlcnnuxix3bnzuw2ylunfxw4x3emvwgc6i)` for details.

___iteration-count___: See `[-webkit-animation-iteration-count](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvpxozlcnnuxix3bnzuw2ylunfxw4x3jorsxeylunfxw4x3dn52w45a)` for details.

___direction___: See `[-webkit-animation-direction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvpxozlcnnuxix3bnzuw2ylunfxw4x3enfzgky3unfxw4)` for details.

____Discussion____: Refer to the respective property for details of each property and default values.

____Availability____: Available in iOS 2.0 and later.

Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Defines when an animation starts.

____Syntax____: |  |
```
-webkit-animation-delay: time [, ...];
```

____Parameters____: ___time___: The time to begin executing an animation after it is applied. If `0`, the animation executes as soon as it is applied. If positive, it specifies an offset from the moment the animation is applied, and the animation delays execution by that offset. If negative, the animation executes the moment the property changes but appears to begin at the specified negative offset—that is, begins part-way through the animation. Nonzero values must specify a unit: `s` for seconds, `ms` for milliseconds. The default value is `0`.

____Constants____: __`now`__: The animation begins immediately.

Available in iOS 2.0 and later.

____Discussion____: This property allows an animation to begin execution some time after it is applied.

____Availability____: Available in iOS 2.0 and later.

Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Determines whether the animation should play in reverse on alternate iterations.

____Syntax____: |  |
```
-webkit-animation-direction: direction [, ...]
```

____Parameters____: ___direction___: The direction to play. The default value is `normal`.

____Constants____: __`normal`__: Play each iteration of the animation in the forward direction.

__`alternate`__: Play even-numbered iterations of the animation in the forward direction and odd-numbered iterations in the reverse direction.

When an animation is played in reverse, the timing functions are also reversed. For example, when played in reverse, an ease-in animation appears as an ease-out animation.

____Availability____: Available in iOS 2.0 and later.

Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Specifies the length of time that an animation takes to complete one iteration.

____Syntax____: |  |
```
-webkit-animation-duration: time [, ...]
```

____Parameters____: __time__: The duration of an animation. If `0`, the animation iteration is immediate (there is no animation). A negative value is treated as `0`. The default value is `0`.

____Availability____: Available in iOS 2.0 and later.

Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Specifies whether the effects of an animation are apparent before the animation starts and after it ends.

____Syntax____: |  |
```
-webkit-animation-fill-mode: mode [, ...]
```

____Parameters____: ___mode___: The animation’s fill mode. Can be `none`, `forwards`, `backwards`, or `both`.

____Constants____: __`none`__: The effects of the animation are apparent only during the defined duration of the animation.

__`forwards`__: The animation’s final keyframe continues to apply after the final iteration of the animation completes.

__`backwards`__: The animation’s initial keyframe is applied as soon as the animation style is applied to an element. This only affects animations that have a nonzero value for `-webkit-animation-delay`.

__`both`__: The animation’s initial keyframe is applied as soon as the animation style is applied to an element, and the animation’s final keyframe continues to apply after the final iteration of the animation completes. The initial keyframe only affects animations that have a nonzero value for `-webkit-animation-delay`.

____Discussion____: By default, an animation starts as soon as the style that describes the animation is applied to an element; however, the `-webkit-animation-delay` property can delay the start of an animation. Specifying a value of `backwards` or `both` for this property overrides the `-webkit-animation-delay` property and tells the animation to start as soon as the style is applied.

____Availability____: Available in Safari 5.0 and later.

Available in iOS 4.0 and later.

____Support Level____: Apple extension.

Specifies the number of times an animation iterates.

____Syntax____: |  |
```
-webkit-animation-iteration-count: number [, ...]
```

____Parameters____: ___number___: The number of iterations. If `1`, the animation plays from beginning to end once. A value of `infinite` causes the animation to repeat forever. Noninteger values cause the animation to end partway through an iteration. Negative values are invalid. The default value is `1`.

____Constants____: __`infinite`__: Repeats the animation forever.

____Discussion____: This property is often used with a `-webkit-animation-direction` property set to `alternate`, which causes the animation to play in reverse on alternate iterations.

____Availability____: Available in iOS 2.0 and later.

Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Specifies the name of an animation.

____Syntax____: |  |
```
-webkit-animation-name: name [, ...]
```

____Parameters____: ___name___: The name of the animation.

The name is used to select the `-webkit-keyframe` at-rule that provides the keyframes and property values for the animation. If the name does not match any `-webkit-keyframe` at-rule, there are no properties to be animated and the animation is not executed. See [@-webkit-keyframes](Supported%20CSS%20Rules.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tmmbrfvjvona) for a description of this rule.

If `"none"`, no animation is executed even if there is a `-webkit-keyframe` at-rule with that name. Setting this property to `"none"` explicitly disables animations.

The default value is `""`.

____Availability____: Available in iOS 2.0 and later.

Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Determines whether the animation is running or paused.

____Syntax____: |  |
```
-webkit-animation-play-state: play_state [, ...]
```

____Parameters____: ___play_state___: The state of an animation.

____Constants____: __`running`__: Plays the animation.

__`paused`__: Pauses the animation.

____Discussion____: A running animation can be paused by setting this property to `paused`. Set this property to `running` to continue running a paused animation. A paused animation continues to display the current value of the animation in a static state. When a paused animation is resumed, it restarts from the current value, not from the beginning of the animation.

The default value is `running`.

____Availability____: Available in iOS 2.0 and later.

Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Defines how an animation progresses between keyframes.

____Syntax____: |  |
```
-webkit-animation-timing-function: function [, ...]
```

____Parameters____: ___function___: The function to apply between keyframes. The default value is `ease`.

____Constants____: __`ease`__: Equivalent to `cubic-bezier(0.25, 0.1, 0.25, 1.0)`.

____Availability____: Available in iOS 2.0 and later.

Available in Safari 4.0 and later.

__`linear`__: Equivalent to `cubic-bezier(0.0, 0.0, 1.0, 1.0)`.

____Availability____: Available in iOS 2.0 and later.

Available in Safari 4.0 and later.

__`ease-in`__: Equivalent to `cubic-bezier(0.42, 0, 1.0, 1.0)`.

____Availability____: Available in iOS 2.0 and later.

Available in Safari 4.0 and later.

__`ease-out`__: Equivalent to `cubic-bezier(0, 0, 0.58, 1.0)`.

____Availability____: Available in iOS 2.0 and later.

Available in Safari 4.0 and later.

__`ease-in-out`__: Equivalent to `cubic-bezier(0.42, 0, 0.58, 1.0)`.

____Availability____: Available in iOS 2.0 and later.

Available in Safari 4.0 and later.

__`step-end`__: Equivalent to `steps(1, end)`.

____Availability____: Available in iOS 5.0 and later.

Available in Safari 5.1 and later.

__`step-start`__: Equivalent to `steps(1, start)`.

____Availability____: Available in iOS 5.0 and later.

Available in Safari 5.1 and later.

____Discussion____: The timing function is specified using a cubic Bezier curve. Use the constants to specify preset points of the curve or the `cubic-bezier` function to specify your own points. See `cubic-bezier` for a description of the parameters for this function. See [Timing Functions](CSS%20Property%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tsnjvfvjvomru) for additional information about timing functions.

This property applies between keyframes, not over the entire animation. For example, for an `ease-in-out` timing function, an animation eases in at the start of the keyframe and eases out at the end of the keyframe. A `-webkit-animation-timing-function` defined within a keyframe block applies to that keyframe; otherwise, the timing function specified for the animation is used.

____Availability____: Available in iOS 2.0 and later.

Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Determines whether or not a transformed element is visible when it is not facing the screen.

____Syntax____: |  |
```
-webkit-backface-visibility: visibility;
```

____Parameters____: ___visibility___: Determines whether or not the back face of a transformed element is visible. The default value is `visible`.

____Constants____: __`visible`__: The element is always visible even when it is not facing the screen.

__`hidden`__: The element is invisible if it is not facing the screen.

____Discussion____: Use this property to specify whether or not an element is visible when it is not facing the screen. For example, if the identity transform is set, an element faces the screen; otherwise, it may face away from the screen. For example, applying a rotation about y of 180 degrees in the absence of any other transforms causes an element to face away from the screen.

This property is useful when you place two elements back to back, as you would do to create a playing card. Without this property, the front and back elements could at times switch places during an animation to flip the card. Another example is creating a box out of six elements whose outside and inside faces can be viewed. This is useful when creating the backdrop for a three-dimensional stage.

____Availability____: Available in iOS 2.0 and later.

____Support Level____: Apple extension.

Defines a reflection of a border box.

____Syntax____: |  |
```
-webkit-box-reflect: direction  offset  mask-box-image;
```

____Parameters____: ___direction___: The position of the reflection relative to the border box. Can be `above`, `below`, `left`, or `right`.

___offset___: The distance of the reflection from the edge of the border box, in length units or as a percentage. The default value is `0`.

___mask-box-image___: Used to overlay the reflection. If omitted, the reflection has no mask.

____Constants____: __`above`__: The reflection appears above the border box.

__`below`__: The reflection appears below the border box.

__`left`__: The reflection appears to the left of the border box.

__`right`__: The reflection appears to the right of the border box.

____Discussion____: Reflections will update automatically as the source changes. Specifying a reflection has the effect of creating a stacking context (like opacity, masks, and transforms). The reflection is non-interactive, and as such, it has no effect on hit testing. The reflection has no effect on layout, other than being part of a container’s overflow; it is similar to `-webkit-box-shadow` in this respect.

____Availability____: Available in iOS 2.0 and later.

____Support Level____: Apple extension.

Defines a variety of mask properties within one declaration.

____Syntax____: |  |
```
-webkit-mask: attachment, clip, origin, image, repeat, composite, box-image;
```

____Parameters____: ___attachment___: See `[-webkit-mask-attachment](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvjvomy)` for details.

___clip___: See `[-webkit-mask-clip](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvjvona)` for details.

___origin___: See `[-webkit-mask-origin](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvjvonq)` for details.

___image___: See `[-webkit-mask-image](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvjvony)` for details.

___repeat___: See `[-webkit-mask-repeat](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvjvooa)` for details.

___composite___: See `[-webkit-mask-composite](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvjvomjt)` for details.

____Discussion____: As with most composite properties, all arguments are optional.

____Availability____: Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Defines the scrolling or fixed nature of the image mask.

____Syntax____: |  |
```
-webkit-mask-attachment: mask-attachment;
```

____Parameters____: ___mask-attachment___: If `fixed`, the mask does not move when the page scrolls; if `scroll`, the image moves when the page scrolls.

____Availability____: Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Defines an image to be used as a mask for a border box.

____Syntax____: |  |
```
-webkit-mask-box-image: uri top right bottom left x_repeat y_repeat
```

____Parameters____: ___uri___: The file path of the image.

___top___: The distance from the top edge of the image.

___right___: The distance from the right edge of the image.

___bottom___: The distance from the bottom edge of the image.

___left___: The distance from the left edge of the image.

___x_repeat___: The horizontal repeat style.

___y_repeat___: The vertical repeat style.

____Discussion____: The `uri` field contains the URI for the image. The four inset values that follow represent distances from the top, right, bottom, and left edges of the image. If no unit is specified, they represent actual pixels in the original image (assuming a raster image). If a unit (such as `px`) is specified, they represent CSS units (which may or may not be the same thing). The values may also be specified as a percentage of the size of the image.

You can specify a repeat style in each direction. These values affect how the top, bottom, left, right, and center portions are altered to fit the required dimensions, and can be any of the following: `repeat` (tiled), `stretch`, or `round` (the round style is like tiling, except that it stretches all nine pieces slightly so that there is no partial tile at the end).

____Availability____: Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Specifies whether the mask should extend into the border of a box.

____Syntax____: |  |
```
-webkit-mask-clip: behavior;
```

____Parameters____: ___behavior___: The clipping behavior of the mask.

____Availability____: Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Sets a compositing style for a mask.

____Syntax____: |  |
```
-webkit-mask-composite: compositing_style;
```

____Parameters____: ___compositing_style___: The compositing style of the mask.

____Discussion____: The default value is `border`, which means that the background extends into the border area. Specifying a value of `padding` limits the background so that it extends only into the padding area enclosed by the border.

____Availability____: Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Defines an image to be used as a mask for an element.

____Syntax____: |  |
```
-webkit-mask-image: value;
```

____Parameters____: ___value___: The file path of the image.

____Availability____: Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Determines where the `-webkit-mask-position` property is anchored.

____Syntax____: |  |
```
-webkit-mask-origin: origin;
```

____Parameters____: ___origin___: The origin of the mask position.

____Constants____: __`border`__: The mask’s position is anchored at the upper-left corner of the element’s border.

__`content`__: The mask’s position is anchored at the upper-left corner of the element’s content.

__`padding`__: The mask’s position is anchored at the upper-left corner of the element’s padding.

____Availability____: Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Defines the position of a mask.

____Syntax____: |  |
```
-webkit-mask-position: xpos;
-webkit-mask-position: xpos ypos;
```

____Parameters____: ___xpos___: The x-coordinate of the position of the mask.

___ypos___: The y-coordinate of the position of the mask.

____Discussion____: Position can be specified in terms of pixels or percentages of the viewport width or using the keywords `top`, `left`, `center`, `right`, or `bottom`.

Changes to this property can be animated in Safari 4.0 and later.

____Availability____: Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Defines the x-coordinate of the position of a mask.

____Syntax____: |  |
```
-webkit-mask-position-x: value;
```

____Parameters____: ___value___: The x-coordinate of the position of the mask.

____Availability____: Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Defines the y-coordinate of the position of a mask.

____Syntax____: |  |
```
-webkit-mask-position-y: value;
```

____Parameters____: ___value___: The y-coordinate of the position of the mask.

____Availability____: Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Defines the repeating qualities of a mask.

____Syntax____: |  |
```
-webkit-mask-repeat: value;
```

____Parameters____: ___value___: The repeating behavior of the mask.

____Discussion____: This property controls whether tiling of an element’s mask should occur in the x direction, the y direction, both, or neither.

____Availability____: Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Overrides the size of a mask.

____Syntax____: |  |
```
-webkit-mask-size: length;
-webkit-mask-size: length_x length_y;
```

____Parameters____: ___length___: The width and height of the mask.

___length_x___: The width of the mask.

___length_y___: The height of the mask.

____Discussion____: Changes to this property can be animated in Safari 4.0 and later.

____Availability____: Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Gives depth to a scene, causing elements farther away from the viewer to appear smaller.

____Syntax____: |  |
```
-webkit-perspective: value;
```

____Parameters____: ___value___: The distance in pixels from the viewer’s position to the z=`0` plane. The default value is `none`.

____Constants____: __`none`__: No perspective transform is applied.

____Discussion____: The `-webkit-perspective` property applies the same transform as the `perspective(<number>)` transform function, except that it applies only to the children of the element, not to the transform on the element itself.

The use of this property with any value other than `none` establishes a stacking context. It also establishes a containing block (somewhat similar to `position:relative`), just as the `-webkit-transform` property does.

This transform alters the effect of other transforms. In the absence of additional transforms, this transform has no effect.

____Availability____: Available in Safari 4.0.3 and later running on Mac OS X v10.6 and later.

Available in iOS 2.0 and later.

____Support Level____: Apple extension.

Sets the origin of the `-webkit-perspective` property described in [-webkit-perspective](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvpxozlcnnuxix3qmvzhg4dfmn2gs5tf).

____Syntax____: |  |
```
-webkit-perspective-origin: posx posy;
```

____Parameters____: ___posx___: The x-origin as a percentage or value.

___posy___: The y-origin as a percentage or value.

____Constants____: __`top`__: Sets the y-origin to the top of the element’s border box.

__`center`__: Sets the x or y origin to the center of the element’s border box. If this constant appears before `left` or `right`, specifies the y-origin. If it appears after `top` or `bottom`, specifies the x-origin. If appears alone, centers both the x and y origin.

__`bottom`__: Sets the y-origin to the bottom of the element’s border box.

__`left`__: Sets the x-origin to the left side of the border box.

__`right`__: Sets the x-origin to the right side of the border box.

____Discussion____: This property effectively sets the x and y position at which the viewer appears to be looking at the children of the element. The default value is `50%` for both x and y coordinates.

____Availability____: Available in Safari 4.0.3 and later running on Mac OS X v10.6 and later.

Available in iOS 2.0 and later.

____Support Level____: Apple extension.

Specifies transformations to be applied to an element.

____Syntax____: |  |
```
-webkit-transform: function ... ;
```

____Parameters____: ___function___: A transform function. Possible values are described in [Transform Functions](CSS%20Property%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tsnjvfvjvomq)

____Constants____: __`none`__: No transforms are applied.

____Discussion____: The `-webkit-transform` property specifies a list of transformations, separated by whitespace, to be applied to an element, such as rotation, scaling, and so on.

The set of transform functions is similar to those allowed by SVG, although there are additional functions to support 3D transformations. If multiple transforms are applied, the transform is generated by performing a matrix concatenation of each transform in the list.

For example, the following `div` element is rotated 45 degrees clockwise:

```
<div style="width: 12em; margin-top: 5em;
            -webkit-transform: rotate(45deg)">...</div>
```

If a list of transforms is provided, the net effect is as if each transform is specified separately in the order provided.

The default value is `none` (no transforms applied).

Changes to this property can be animated.

____Availability____: Available in Safari 3.1 and later.

Available in iOS 2.0 and later.

____Support Level____: Apple extension.

Sets the origin for the [-webkit-transform](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvpxozlcnnuxix3uojqw443gn5zg2) property.

____Syntax____: |  |
```
-webkit-transform-origin: posx
-webkit-transform-origin: posx posy
```

____Parameters____: ___posx___: The x origin as a percentage or value.

___posy___: The y origin as a percentage or value.

____Constants____: __`top`__: Sets the y origin to the top of the element’s border box.

__`center`__: Sets the x or y origin to the center of the element’s border box. If this constant appears before `left` or `right`, specifies the y origin. If this constant appears after `top` or `bottom`, specifies the x origin. If it appears alone, centers both the x and y origin.

__`bottom`__: Sets the y origin to the bottom of the element’s border box.

__`left`__: Sets the x origin to the left side of the border box.

__`right`__: Sets the x origin to the right side of the border box.

____Discussion____: The `-webkit-transform-origin` property establishes the origin for transforms applied to an element with respect to its border box.

The values may be expressed either as a CSS length unit or as a percentage of the element’s size. For example, a value of `50% 50%` causes transformations to occur around the element’s center. Changing the origin to `100% 0%` causes transformation to occur around the top-right corner of the element. The default value is `50% 50%`.

If only one argument is provided, it is interpreted as the horizontal position.

____Availability____: Available in Safari 3.1 and Later.

Available in iOS 2.0 and later.

____Support Level____: Apple extension.

The x coordinate of the origin for transforms applied to an element with respect to its border box.

____Syntax____: |  |
```
-webkit-transform-origin-x: posx
```

____Parameters____: ___posx___: The x origin as a percentage or value.

____Discussion____: The values may be expressed either as a CSS length unit or as a percentage of the element’s size. For example, a value of `50% 50%` causes transformations to occur around the element’s center. Changing the origin to `100% 0%` causes transformation to occur around the top-right corner of the element. The default value is `50% 50%`.

Changes to this property can be animated.

____Availability____: Available in Safari 3.1 and Later.

Available in iOS 2.0 and later.

____Support Level____: Apple extension.

The y coordinate of the origin for transforms applied to an element with respect to its border box.

____Syntax____: |  |
```
-webkit-transform-origin-y: posy
```

____Parameters____: ___posy___: The y origin as a percentage or value.

____Discussion____: The values may be expressed either as a CSS length unit or as a percentage of the element’s size. For example, a value of `50% 50%` causes transformations to occur around the element’s center. Changing the origin to `100% 0%` causes transformation to occur around the top-right corner of the element. The default value is `50% 50%`.

Changes to this property can be animated.

____Availability____: Available in Safari 3.1 and Later.

Available in iOS 2.0 and later.

____Support Level____: Apple extension.

The z coordinate of the origin for transforms applied to an element with respect to its border box.

____Syntax____: |  |
```
-webkit-transform-origin-z: posz
```

____Parameters____: ___posz___: The z origin as a percentage or value.

____Discussion____: The values may be expressed either as a CSS length unit or as a percentage of the element’s size. For example, a value of `50% 50%` causes transformations to occur around the element’s center. Changing the origin to `100% 0%` causes transformation to occur around the top-right corner of the element. The default value is `50% 50%`.

Changes to this property can be animated.

____Availability____: Available in Safari 4.0.3 and later running on Mac OS X v10.6 and later.

Available in iOS 2.0 and later.

____Support Level____: Apple extension.

Defines how nested, transformed elements are rendered in 3D space.

____Syntax____: |  |
```
-webkit-transform-style: style;
```

____Parameters____: ___style___: The transform style.

____Constants____: __`flat`__: Flatten all children of this element into the 2D plane.

__`preserve-3d`__: Preserve the 3D perspective.

____Discussion____: If `-webkit-transform-style` is `flat`, all children of this element are rendered flattened into the 2D plane of the element. Therefore, rotating the element about the x or y axes causes children positioned at positive or negative z positions to appear on the element’s plane, rather than in front of or behind it. If `-webkit-transform-style` is `preserve-3d`, this flattening is not performed, so children maintain their position in 3D space.

This flattening takes place at each element, so preserving a hierarchy of elements in 3D space requires that each ancestor in the hierarchy have the value `preserve-3d` for `-webkit-transform-style`. But `-webkit-transform-style` affects only an element’s children; the leaf nodes in a hierarchy do not require the `preserve-3d` style.

The default value is `flat`.

____Availability____: Available in Safari 4.0.3 and later running on Mac OS X v10.6 and later.

Available in iOS 2.0 and later.

____Support Level____: Apple extension.

Combines `-webkit-transition-delay`,`-webkit-transition-duration`,`-webkit-transition-property`, and `-webkit-transition-timing-function` into a single property.

____Syntax____: |  |
```
-webkit-transition: property duration timing_function delay [, ...]
```

____Parameters____: ___property___: See `[-webkit-transition-property](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvjvooi)` for details.

___duration___: See `[-webkit-transition-duration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvjvomjq)` for details.

___timing_function___: See `[-webkit-transition-timing-function](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvjvoni)` for details.

___delay___: See `[-webkit-transition-delay](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvjvomjr)` for details.

____Availability____: Available in Safari 3.1 and Later.

Available in iOS 2.0 and later.

____Support Level____: Apple extension.

Defines when the transition starts.

____Syntax____: |  |
```
-webkit-transition-delay: time [, ...]
```

____Parameters____: ___time___: The time to begin executing a transition after it is applied. If `0`, the transition executes as soon as the property changes. Otherwise, the value specifies an offset from the moment the property changes, and the transition delays execution by that offset. If the value is negative, the transition executes the moment the property changes but appears to begin at the specified negative offset—that is, begins part-way through the transition. Nonzero values must specify a unit: `s` for seconds, `ms` for milliseconds. Negative values are invalid. The default value is `0`.

____Constants____: __`now`__: The transition begins immediately.

Available in iOS 2.0 and later.

____Availability____: Available in iOS 2.0 and later.

Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Defines how long the transition from the old value to the new value should take.

____Syntax____: |  |
```
-webkit-transition-duration: time [, ...]
```

____Parameters____: ___time___: If `0`, the transition is immediate (there is no animation). A negative value is treated as `0`. Nonzero values must specify a unit: `s` for seconds, `ms` for milliseconds. Negative values are invalid. The default value is `0`.

____Availability____: Available in Safari 3.1 and Later.

Available in iOS 2.0 and later.

____Support Level____: Apple extension.

Specifies the name of the CSS property to which the transition is applied.

____Syntax____: |  |
```
-webkit-transition-property: name;
```

____Parameters____: ___name___: The name of the transition. You can list multiple properties. Property names should be bare, unquoted names. The default value is `all`.

____Constants____: __`none`__: No transition specified.

__`all`__: The default transition name.

____Availability____: Available in Safari 3.1 and Later.

Available in iOS 2.0 and later.

____Support Level____: Apple extension.

Specifies how the intermediate values used during a transition are calculated.

____Syntax____: |  |
```
-webkit-transition-timing-function: timing_function [, ...]
```

____Parameters____: ___timing_function___: The timing function.

____Constants____: __`ease`__: Equivalent to `cubic-bezier(0.25, 0.1, 0.25, 1.0)`.

__`linear`__: Equivalent to `cubic-bezier(0.0, 0.0, 1.0, 1.0)`.

__`ease-in`__: Equivalent to `cubic-bezier(0.42, 0, 1.0, 1.0)`.

__`ease-out`__: Equivalent to `cubic-bezier(0, 0, 0.58, 1.0)`.

__`ease-in-out`__: Equivalent to `cubic-bezier(0.42, 0, 0.58, 1.0)`.

____Discussion____: This property allows for a transition to change speed over its duration. These effects, commonly called easing functions, are mathematical functions that produce a smooth curve.

The timing function is specified using a cubic Bezier curve. Use the constants to specify preset points of the curve or the `cubic-bezier` function to specify your own points. See `cubic-bezier` for a description of the parameters for this function.

The timing function takes as its input the current elapsed percentage of the transition duration and outputs a percentage that determines how close the transition is to its goal state.

The default value is `ease`.

____Availability____: Available in Safari 3.1 and Later.

Available in iOS 2.0 and later.

____Support Level____: Apple extension.

Embeds an arbitrary batch of content (such as a movie or a specially formatted string) to be embedded alongside a CSS property.

____Syntax____: |  |
```
content: value;
content: function;
```

____Parameters____: ___value___: The file path of the content.

___function___: A function that procedurally generates an image, such as `gradient`.

____Support Level____: CSS 2.1.

Increments a numerical counter for auto-numbering.

____Syntax____: |  |
```
counter-increment: counter_name increment_by;
```

____Parameters____: ___counter_name___: The name of the counter.

___increment_by___: The amount by which the counter increments.

____Constants____: `none`

____Discussion____: This property is commonly used in conjunction with the [content](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrw63tumvxhi) property to create section numbers or other auto-numbered containers. For example:

```
<style>
    p#top {
        counter-reset: section;
    }

    h1:before
    {
        content: "Section " counter(section) " ";
        counter-increment: section 1;
    }
</style>

<p id="top">This resets the counter.</p>

<H1>First section</H1>
<H1>Next section</H1>
```

This snippet inserts “Section 1:” at the beginning of the first heading, “Section 2:” at the beginning of the second, and so on.

__Important:__ You _must_ use the `[counter-reset](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrw65loorsxellsmvzwk5a)` property to reset the counter on some element that appears in the DOM tree prior to the first element where you use counter-increment on that counter. Otherwise, this call increments a nonexistent counter and all of your sections will be numbered "Section 1”.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 1.0 and later.

____Support Level____: CSS 2.1.

Resets a counter used by the `[counter-increment](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrw65loorsxelljnzrxezlnmvxhi)` property and the `counter` function.

____Syntax____: |  |
```
counter-reset: counter_name
```

____Parameters____: ___counter_name___: The name of the counter.

____Constants____: `none`

____Discussion____: For an example of this property, see the documentation for `[counter-increment](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvrw65loorsxelljnzrxezlnmvxhi)`.

____Availability____: Available in Safari 3.0 and later.

____Support Level____: CSS 2.1.

Defines the display style for a list and list elements.

____Syntax____: |  |
```
list-style: type position image;
```

____Parameters____: ___type___: The type of list.

___position___: The position of the list marker.

___image___: The file path of an image to be used as the list marker.

____Subproperties____: - `[list-style-image](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvwgs43ul5zxi6lmmvpws3lbm5sq)`
- `[list-style-position](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvwgs43ul5zxi6lmmvpxa33tnf2gs33o)`
- `[list-style-type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvwgs43ul5zxi6lmmvpxi6lqmu)`

____Discussion____: As with most composite properties, all arguments are optional.

____Support Level____: CSS 2.1.

Defines an image to use as the opening symbol of a list element.

____Syntax____: |  |
```
list-style-image: value
list-style-image: function
```

____Parameters____: ___value___: The file path of the image.

___function___: A function that procedurally generates an image, such as `gradient`.

____Support Level____: CSS 2.1.

Defines the position of the marker of a list element.

____Syntax____: |  |
```
list-style-position: value
```

____Parameters____: ___value___: The position of the marker.

____Constants____: __`inside`__: The marker is placed inside the text. Wrapping text appears directly below the marker.

__`outside`__: The text of the list item is indented from the marker.

____Support Level____: CSS 2.1.

Defines the type of marker of a list element.

____Syntax____: |  |
```
list-style-type: value
```

____Parameters____: ___value___: The type of marker.

____Constants____: `armenian`, `circle`, `cjk-ideographic`, `decimal`, `decimal-leading-zero`, `disc`, `georgian`, `hebrew`, `hiragana`, `hiragana-iroha`, `katakana`, `katakana-iroha`, `lower-alpha`, `lower-greek`, `lower-latin`, `lower-roman`, `none`, `square`, `upper-alpha`, `upper-latin`, `upper-roman`

____Support Level____: CSS 2.1.

Defines the minimum number of lines in a paragraph that must be left at the bottom of a page (before a page break).

____Syntax____: |  |
```
orphans: number_of_lines
```

____Parameters____: ___number_of_lines___: The number of lines.

____Types Allowed____: Integers

____Availability____: Available in Safari 1.3 and later.

____Support Level____: CSS 2.1.

Defines the page break behavior following an element's definition.

____Syntax____: |  |
```
page-break-after: behavior
```

____Parameters____: ___behavior___: The page break behavior.

____Constants____: `always`, `auto`, `avoid`, `left`, `right`

____Availability____: Safari 1.2 and later.

____Support Level____: CSS 2.1.

Defines the page break behavior before an element's definition.

____Syntax____: |  |
```
page-break-before: behavior
```

____Parameters____: ___behavior___: The page break behavior.

____Constants____: `always`, `auto`, `avoid`, `left`, `right`

____Availability____: Safari 1.2 and later.

____Support Level____: CSS 2.1.

Defines the page break behavior within an element.

____Syntax____: |  |
```
page-break-inside: behavior
```

____Parameters____: ___behavior___: The page break behavior.

____Constants____: `auto`, `avoid`

____Availability____: Safari 1.3 and later.

____Support Level____: CSS 2.1.

Defines the minimum number of lines in a paragraph that must be left at the top of a page (after a page break).

____Syntax____: |  |
```
widows: number_of_lines
```

____Parameters____: ___number_of_lines___: The number of lines.

____Types Allowed____: Integers

____Availability____: Safari 1.3 and later.

____Support Level____: CSS 2.1.

Defines a variety of background properties within one declaration.

____Syntax____: |  |
```
background: background_color background_image background_repeat background_attachment background_position;
```

____Parameters____: ___background_color___: The background color.

___background_image___: The file path of the background image.

___background_repeat___: The repeating behavior of the background image.

___background_attachment___: If `fixed`, the background image does not move when the page scrolls; if `scroll`, the image moves when the page scrolls.

___background_position___: The position of the background image.

____Discussion____: As with most composite properties, all arguments are optional.

____Support Level____: CSS 2.1.

Defines the scrolling or fixed nature of the page background.

____Syntax____: |  |
```
background-attachment: behavior
```

____Parameters____: ___background_attachment___: If `fixed`, the background image does not move when the page scrolls; if `scroll`, the image moves when the page scrolls.

____Constants____: `scroll`, `fixed`

____Support Level____: CSS 2.1.

Defines an element’s background color.

____Syntax____: |  |
```
background-color: color
```

____Parameters____: ___color___: The background color.

____Constants____: __`currentcolor`__: The value of the element’s `color` property.

__`-webkit-activelink`__: The default color of a hyperlink that is being clicked.

__`-webkit-focus-ring-color`__: The color that surrounds a UI element, such as a text field, that has focus.

__`-webkit-link`__: The default color of a hyperlink that has been visited.

__`-webkit-text`__: The default text color.

`activeborder`, `activecaption`, `appworkspace`, `aqua`, `background`, `black`, `blue`, `buttonface`, `buttonhighlight`, `buttonshadow`, `buttontext`, `captiontext`, `fuchsia`, `gray`, `graytext`, `green`, `grey`, `highlight`, `highlighttext`, `inactiveborder`, `inactivecaption`, `inactivecaptiontext`, `infobackground`, `infotext`, `lime`, `maroon`, `match`, `menu`, `menutext`, `navy`, `olive`, `orange`, `purple`, `red`, `scrollbar`, `silver`, `teal`, `threeddarkshadow`, `threedface`, `threedhighlight`, `threedlightshadow`, `threedshadow`, `transparent`, `white`, `window`, `windowframe`, `windowtext`, `yellow`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines an element’s background image.

____Syntax____: |  |
```
background-image: value
background-image: function
```

____Parameters____: ___value___: The file path of the image.

__`function`__: A function that procedurally generates an image, such as `gradient`.

____Support Level____: CSS 2.1.

Defines the origin of a background image.

____Syntax____: |  |
```
background-position: xpos
background-position: xpos ypos
```

____Parameters____: ___xpos___: The x-coordinate of the origin of the background image.

___ypos___: The y-coordinate of the origin of the background image.

____Discussion____: Position can be specified in terms of pixels or percentages of the viewport width or using the keywords `top`, `left`, `center`, `right`, or `bottom`.

Changes to this property can be animated in Safari 4.0 and later.

____Support Level____: CSS 2.1.

Defines the x-coordinate of the origin of a background image.

____Syntax____: |  |
```
background-position-x: value
```

____Parameters____: ___value___: The x-coordinate of the origin of the background image.

____Support Level____: Apple extension.

Defines the y-coordinate of the origin of a background image.

____Syntax____: |  |
```
background-position-y: value
```

____Parameters____: ___value___: The y-coordinate of the origin of the background image.

____Support Level____: Apple extension.

Defines the repeating qualities of the background image.

____Syntax____: |  |
```
background-repeat: value
```

____Parameters____: ___value___: The repeating behavior of the background image.

____Discussion____: This property controls whether tiling of an element’s background image should occur in the x direction, the y direction, both, or neither.

____Support Level____: CSS 2.1.

Defines the color of the text of an element.

____Syntax____: |  |
```
color: value
```

____Parameters____: ___value___: The color. Colors can be specified with a constants, an RGB value, or a hexadecimal value.

____Constants____: __`-webkit-activelink`__: The default color of a hyperlink that is being clicked.

__`-webkit-focus-ring-color`__: The color that surrounds a UI element, such as a text field, that has focus.

__`-webkit-link`__: The default color of a hyperlink that has been visited.

__`-webkit-text`__: The default text color.

`activeborder`, `activecaption`, `appworkspace`, `aqua`, `background`, `black`, `blue`, `buttonface`, `buttonhighlight`, `buttonshadow`, `buttontext`, `captiontext`, `fuchsia`, `gray`, `graytext`, `green`, `grey`, `highlight`, `highlighttext`, `inactiveborder`, `inactivecaption`, `inactivecaptiontext`, `infobackground`, `infotext`, `lime`, `maroon`, `match`, `menu`, `menutext`, `navy`, `olive`, `orange`, `purple`, `red`, `scrollbar`, `silver`, `teal`, `threeddarkshadow`, `threedface`, `threedhighlight`, `threedlightshadow`, `threedshadow`, `transparent`, `white`, `window`, `windowframe`, `windowtext`, `yellow`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Specifies the clipping behavior of the background of a box.

____Syntax____: |  |
```
-webkit-background-clip: behavior
```

____Parameters____: ___behavior___: The clipping behavior of the background.

____Constants____: ___border___: The background clips to the border of the box.

___content___: The background clips to the content of the box.

___padding___: The background clips to the padding of the box.

___text___: The background clips to the text of the box.

Available in Safari 4.0 and later.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 1.0 and later.

____Support Level____: Experimental CSS 3.

Sets a compositing style for background images and colors.

____Syntax____: |  |
```
-webkit-background-composite: compositing_style
```

____Parameters____: ___compositing_style___: The compositing style of the background.

____Discussion____: The default value is `border`, which means that the background extends into the border area. Specifying a value of `padding` limits the background so that it extends only into the padding area enclosed by the border.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 1.0 and later.

____Support Level____: Under development.

Determines where the background-position property is anchored.

____Syntax____: |  |
```
-webkit-background-origin: origin
```

____Parameters____: ___origin___: The origin of the background position.

____Discussion____: The background position can be anchored at the upper-left corner of the border, the upper-left corner of the padding area inside the border, or the upper-left corner of the content inside the padding area.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 1.0 and later.

____Support Level____: Experimental CSS 3.

Overrides the size of a background image.

____Syntax____: |  |
```
-webkit-background-size: length
-webkit-background-size: length_x length_y
```

____Parameters____: ___length___: The width and height of the background image.

___length_x___: The width of the background image.

___length_y___: The height of the background image.

____Discussion____: Changes to this property can be animated in Safari 4.0 and later.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 1.0 and later.

____Support Level____: Experimental CSS 3.

Defines a variety of properties for an element’s text font within one declaration.

____Syntax____: |  |
```
font: font_style font_variant font_weight font_size / line_height
        font_family
font: ui_style
```

____Parameters____: ___font_style___: The style of the font.

___font_variant___: The variant of the font.

___font_weight___: The weight, or boldness, of the font.

___font_size___: The size of the font.

___line_height___: The distance between lines.

___font_family___: The family of the font.

___ui_style___: The user interface style to replicate.

____Constants____: __`-webkit-control`__: The style of the text of a standard size UI element, such as a button.

__`-webkit-mini-control`__: The style of the text of a miniature size UI element, such as a button.

__`-webkit-small-control`__: The style of the text of a small size UI element, such as a button.

`caption`, `icon`, `menu`, `message-box`, `small-caption`, `status-bar`

____Discussion____: In addition to declaring a font style explicitly by characteristics, you can also specify a user interface style using constants such as `caption`. These constants represent the default font style for the specified user interface element, and as such, their specific values are dependent on the browser, the operating system, and user configuration options.

Using the `font` property resets all related font properties that are not explicitly specified.

____Support Level____: CSS 2.1.

Defines a list of fonts for element styling or downloadable font definitions.

____Syntax____: |  |
```
font-family: family [, ...]
```

____Parameters____: ___family___: The family of the font.

____Discussion____: The font-family property has two different meanings, depending on context.

In the context of an element style, it defines a font to use for text within an element. Because not all computers have the same fonts available, this property to specify multiple acceptable fonts in descending order of preference. In addition, constants such as `serif` or `sans-serif` provide generic fallback fonts in case a browser does not have any of the listed fonts available.

In the context of a downloadable font definition, this property provides the name of the font that the font definition describes. In this form, you may specify multiple family names for the font, but generally only a single family name (optionally, specify that it should match against generic font names like `serif`).

For more information about downloadable font definitions, see [@font-face](Supported%20CSS%20Rules.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tmmbrfvjvomq).

____Availability____: Available in Safari 1.0 and later. Downloadable fonts supported in Safari 3.1 and later.

Available in iOS 1.0 and later.

____Support Level____: CSS 2.1.

Defines the font size for the text in an element or in a downloadable font definition.

____Syntax____: |  |
```
font-size: value
```

____Parameters____: ___value___: The size of the font.

____Types Allowed____: Numbers as a percentage, length units

____Constants____: `large`, `larger`, `medium`, `small`, `smaller`, `-webkit-xxx-large`, `x-large`, `x-small`, `xx-large`, `xx-small`

____Discussion____: Changes to this property can be animated in Safari 4.0 and later. For more information about downloadable font definitions, see [@font-face](Supported%20CSS%20Rules.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tmmbrfvjvomq).

____Availability____: Available in Safari 1.0 and later. Downloadable fonts supported in Safari 3.1 and later.

Available in iOS 1.0 and later.

____Support Level____: CSS 2.1.

Defines the font style for the text in an element or a downloadable font definition.

____Syntax____: |  |
```
font-style: value
```

____Parameters____: ___value___: The style of the font.

____Constants____: `italic`, `normal`, `oblique`

____Availability____: Available in Safari 1.0 and later. Downloadable fonts supported in Safari 3.1 and later.

Available in iOS 1.0 and later.

____Support Level____: CSS 2.1.

Defines special font properties for the text in an element or for a downloadable font definition.

____Syntax____: |  |
```
font-variant: value
```

____Parameters____: ___value___: The variant of the font.

____Constants____: `normal`, `small-caps`

____Discussion____: For more information about downloadable font definitions, see [@font-face](Supported%20CSS%20Rules.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tmmbrfvjvomq).

____Availability____: Available in Safari 1.0 and later. (The value `small-caps` is not supported.) Downloadable fonts supported in Safari 3.1 and later.

Available in iOS 1.0 and later.

____Support Level____: CSS 2.1.

Defines the font weight of the text in an element or for a downloadable font definition.

____Syntax____: |  |
```
font-weight: value
```

____Parameters____: ___value___: The weight, or boldness, of the font.

____Types Allowed____: Integers, nonnegative values

____Constants____: `100`, `200`, `300`, `400`, `500`, `600`, `700`, `800`, `900`, `bold`, `bolder`, `lighter`, `normal`

____Discussion____: For more information about downloadable font definitions, see [@font-face](Supported%20CSS%20Rules.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tmmbrfvjvomq).

____Availability____: Available in Safari 1.0 and later. Downloadable fonts supported in Safari 3.1 and later.

Available in iOS 1.0 and later.

____Support Level____: CSS 2.1.

Provides a list of locations for a downloadable font definition.

____Syntax____: |  |
```
src: local("Times New Roman"),
    URL(http://...) format("truetype"),
    URL(http://...), ...
```

____Discussion____: This property takes a comma-delimited list of font locations which may be locally installed font family names or HTTP URLs.

For more information about downloadable font definitions, see [@font-face](Supported%20CSS%20Rules.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tmmbrfvjvomq).

____Availability____: Available in Safari 3.1 and later.

____Support Level____: CSS 3.

Describes the unicode characters supported by a downloadable font definition.

____Syntax____: |  |
```
unicode-range: range [, ...];
unicode-range: start_character-end_character [, ...];
```

____Parameters____: ___range___: The range of supported characters.

___start_character___: The first character in a range of supported characters.

___end_character___: The last character in a range of supported characters.

____Discussion____: This property takes a comma-delimited list of Unicode character ranges. There are two supported formats: singleton ranges and pair ranges.

A singleton range is in the form `U+xxxx` where `xxxx` is a hexadecimal number. For example, the range `U+2150` indicates that Unicode character `0x2150` is supported. Leading zeroes may be omitted, so `U+300` is the same as `U+0300`. The following snippet shows a singleton range: `unicode-range: U+2150;`

A singleton range may also contain wildcards in the form of a question-mark character. For example, `U+36??` contains two wildcard characters. This range matches any value in which the first two digits are `36`, without regard to the value for the last two digits. The following snippet shows a wildcard range that represents the Unicode characters 0x2160 through 0x216f, inclusive: `unicode-range: U+216?;`

A pair range is in the form of a hyphen-separated pair of hexadecimal values in the form `U+xxxx-yyyy` where `xxxx` and `yyyy` are hexadecimal numbers. For example, the following pair range represents the Unicode characters from `0x2164` through `0x2156`, inclusive: `unicode-range: U+2154-2156;`

For more information about downloadable font definitions, see [@font-face](Supported%20CSS%20Rules.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tmmbrfvjvomq).

____Availability____: Available in Safari 3.1 and later.

____Support Level____: CSS 3.

Defines the horizontal interletter spacing of characters within the text of an element.

____Syntax____: |  |
```
letter-spacing: length
```

____Parameters____: ___length___: The size of the character spacing.

____Types Allowed____: Length units

____Constants____: `normal`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the alignment for inline content within an element.

____Syntax____: |  |
```
text-align: position
```

____Parameters____: ___position___: The inline content alignment.

____Constants____: __`-webkit-auto`__: Text is aligned to the default alignment.

__`-webkit-center`__: Text is aligned to the center.

__`-webkit-left`__: Text is aligned to the left.

__`-webkit-right`__: Text is aligned to the right.

`center`, `end`, `justify`, `left`, `right`, `start`

____Support Level____: CSS 2.1.

Defines special styling for text, such as underlines.

____Syntax____: |  |
```
text-decoration: style
```

____Parameters____: ___style___: The type of decoration.

____Constants____: `line-through`, `none`, `overline`, `underline`

____Support Level____: CSS 2.1.

Defines the amount to indent the first line of text within an element.

____Syntax____: |  |
```
text-indent: length;
```

____Parameters____: ___length___: The amount to indent.

____Types Allowed____: Numbers as a percentage, length units

____Support Level____: CSS 2.1.

Controls overflow of non-wrapped text.

____Syntax____: |  |
```
text-overflow: behavior;
```

____Parameters____: ___behavior___: The overflow behavior.

____Constants____: `clip`, `ellipsis`

____Discussion____: This property controls how Safari displays text that exceeds the specified width of the enclosing paragraph if the `[overflow](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvxxmzlsmzwg65y)` property is set to `hidden` and style rules or `nowrap` tags prevent the text from wrapping (or if a single word is too long to fit by itself).

____Support Level____: CSS 3.

Defines a variety of properties for an element’s text shadow within one declaration.

____Syntax____: |  |
```
text-shadow: color x_offset y_offset blur_radius
```

____Parameters____: ___color___: The color of the shadow.

___x_offset___: The horizontal offset of the shadow.

___y_offset___: The vertical offset of the shadow.

___blur_radius___: The blur radius of the shadow.

____Constants____: `none`

____Discussion____: Although the CSS specification allows it, multiple shadows are not supported in Safari. Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines a capitalization transformation for the text in an element.

____Syntax____: |  |
```
text-transform: transformation
```

____Parameters____: ___transformation___: The capitalization transformation.

____Constants____: `capitalize`, `lowercase`, `none`, `uppercase`

____Support Level____: CSS 2.1.

Defines how whitespace characters in an element are handled onscreen.

____Syntax____: |  |
```
white-space: policy
```

____Parameters____: ___policy___: The policy for displaying whitespace in the element.

____Constants____: `normal`, `nowrap`, `pre`, `pre-line`, `pre-wrap`

____Support Level____: CSS 2.1.

Specifies the level of strictness when breaking lines of text in ideographic languages such as Chinese, Japanese, and Korean.

____Syntax____: |  |
```
word-break: strictness
```

____Parameters____: ___strictness___: The level of strictness.

____Constants____: `break-all`, `break-word`, `normal`

____Availability____: Available in Safari 3.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Stable CSS 3.

Defines the amount of space between words.

____Syntax____: |  |
```
word-spacing: length
```

____Parameters____: ___length___: The amount of spacing.

____Types Allowed____: Length units

____Constants____: `normal`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Specifies word-splitting behavior for wrapping lines that are too long for the enclosing box and contain no spaces.

____Syntax____: |  |
```
word-wrap: behavior
```

____Parameters____: ___behavior___: The wrapping behavior.

____Constants____: `break-word`, `normal`

____Availability____: Available in Safari 2.0 and later.

Available in iOS 1.0 and later.

____Support Level____: Stable CSS 3.

Defines properties for showing content as though displayed on an electronic marquee sign.

____Syntax____: |  |
```
-webkit-marquee: direction increment repetition style speed
```

____Parameters____: __`direction`__: The direction of the marquee.

__`increment`__: The distance the marquee moves in each increment

__`repetition`__: The number of times the marquee repeats.

__`style`__: The style of the marquee’s motion.

__`speed`__: The scroll or slide speed of the marquee.

____Subproperties____: - `[-webkit-marquee-direction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillnmfzhc5lfmuwwi2lsmvrxi2lpny)`
- `[-webkit-marquee-increment](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillnmfzhc5lfmuwws3tdojsw2zlooq)`
- `[-webkit-marquee-repetition](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillnmfzhc5lfmuwxezlqmv2gs5djn5xa)`
- `[-webkit-marquee-speed](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillnmfzhc5lfmuwxg4dfmvsa)`
- `[-webkit-marquee-style](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillnmfzhc5lfmuwxg5dznrsq)`

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-marquee` in Safari 2.0.)

Available in iOS 1.0.

____Support Level____: Under development.

Specifies the direction of motion for a marquee box.

____Syntax____: |  |
```
-webkit-marquee-direction: direction
```

____Parameters____: ___direction___: The direction of the marquee.

____Constants____: __`ahead`__: The marquee moves from bottom to top.

__`auto`__: The marquee moves in the default direction.

__`backwards`__: The marquee moves from right to left.

__`down`__: The marquee moves from bottom to top.

__`forwards`__: The marquee moves from left to right.

__`left`__: The marquee moves from right to left.

__`reverse`__: The marquee moves from top to bottom.

__`right`__: The marquee moves from left to right.

__`up`__: The marquee moves from bottom to top.

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-marquee-direction` in Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Under development.

Defines the distance the marquee moves in each increment.

____Syntax____: |  |
```
-webkit-marquee-increment: distance
```

____Parameters____: ___distance___: The distance the marquee moves in each increment

____Types Allowed____: Numbers as a percentage, length units

____Constants____: ___large___: The marquee moves a large amount in each increment.

___medium___: The marquee moves a medium amount in each increment.

___small___: The marquee moves a small amount in each increment.

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-marquee-increment` in Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Under development.

Specifies the number of times a marquee box repeats (or `infinite`).

____Syntax____: |  |
```
-webkit-marquee-repetition: iterations
```

____Parameters____: ___iterations___: The number of times the marquee repeats.

____Types Allowed____: Integers, nonnegative values

____Constants____: __`infinite`__: The marquee repeats infinitely.

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-marquee-repetition` in Safari 2.0.)

Available in iOS 1.0.

____Support Level____: Under development.

Defines the scroll or slide speed of a marquee box.

____Syntax____: |  |
```
-webkit-marquee-speed: speed
-webkit-marquee-speed: distance / time
```

____Parameters____: ___speed___: The scroll or slide speed of the marquee.

___distance___: The distance term in the speed equation.

___time___: The time term in the speed equation.

____Types Allowed____: Integers, time units, nonnegative values

____Constants____: ___fast___: The marquee moves at a fast speed.

___normal___: The marquee moves at a normal speed.

___slow___: The marquee moves at a slow speed.

____Discussion____: This property can either take one speed parameter (`slow`, for example) or a measure of distance and a measure of time separated by a slash (`/`).

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-marquee-speed` in Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Under development.

Specifies the style of marquee motion.

____Syntax____: |  |
```
-webkit-marquee-style: style
```

____Parameters____: ___style___: The style of the marquee’s motion.

____Constants____: ___alternate___: The marquee shifts back and forth.

___none___: The marquee does not move.

___scroll___: The marquee loops in its specified direction.

___slide___: The marquee moves in its specified direction, but stops either when the entirety of its content has been displayed or the content reaches the opposite border of its box, whichever comes second.

____Discussion____: The values `scroll` and `slide` both cause the content to start outside the box and move into the box, but if the value `scroll` is specified, the content stops moving once the last content is visible. The value `alternate` causes the content to shift back and forth within the box in the specified direction.

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-marquee-style` in Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Under development.

Specifies a fill color for text.

____Syntax____: |  |
```
-webkit-text-fill-color: color
```

____Parameters____: ___color___: The fill color. Colors can be specified with a constant, an RGB value, or a hexadecimal value.

____Constants____: __`currentcolor`__: The value of the element’s `color` property.

__`-webkit-activelink`__: The default color of a hyperlink that is being clicked.

__`-webkit-focus-ring-color`__: The color that surrounds a UI element, such as a text field, that has focus.

__`-webkit-link`__: The default color of a hyperlink that has been visited.

__`-webkit-text`__: The default text color.

`activeborder`, `activecaption`, `appworkspace`, `aqua`, `background`, `black`, `blue`, `buttonface`, `buttonhighlight`, `buttonshadow`, `buttontext`, `captiontext`, `fuchsia`, `gray`, `graytext`, `green`, `grey`, `highlight`, `highlighttext`, `inactiveborder`, `inactivecaption`, `inactivecaptiontext`, `infobackground`, `infotext`, `lime`, `maroon`, `match`, `menu`, `menutext`, `navy`, `olive`, `orange`, `purple`, `red`, `scrollbar`, `silver`, `teal`, `threeddarkshadow`, `threedface`, `threedhighlight`, `threedlightshadow`, `threedshadow`, `transparent`, `white`, `window`, `windowframe`, `windowtext`, `yellow`

____Discussion____: If not specified, the color specified by the `color` property is used. `-webkit-fill-color` is commonly used in combination with `-webkit-text-stroke`. Changes to this property can be animated.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Apple extension.

Specifies the shape to use in place of letters in a password input field.

____Syntax____: |  |
```
-webkit-text-security: shape
```

____Parameters____: ___shape___: The shape to use in place of letters.

____Constants____: ___circle___: A circle shape.

___disc___: A disc shape.

___none___: No shape is used.

___square___: A square shape.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 1.0 and later.

____Support Level____: Apple extension.

Specifies a size adjustment for displaying text content in Safari on iOS.

____Syntax____: |  |
```
-webkit-text-size-adjust: percentage
```

____Parameters____: ___percentage___: The size at which to display text in Safari on iOS.

____Constants____: ___auto___: The text size is automatically adjusted for Safari on iOS.

___none___: The text size is not adjusted.

____Availability____: Available in iOS 1.0 and later.

____Support Level____: Apple extension—Safari on iOS only.

Specifies the width and color of the outline (stroke) of text.

____Syntax____: |  |
```
-webkit-text-stroke: width color
```

____Parameters____: ___width___: The width of the stroke.

___color___: The color of the stroke.

____Subproperties____: - `[-webkit-text-stroke-color](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillumv4hilltorzg623ffvrw63dpoi)`
- `[-webkit-text-stroke-width](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillumv4hilltorzg623ffv3wszduna)`

____Discussion____: This property is commonly used in combination with `-webkit-text-fill-color`.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Apple extension.

Specifies the color of the outline (stroke) of text.

____Syntax____: |  |
```
-webkit-text-stroke-color: color
```

____Parameters____: ___color___: The color of the stroke.

____Constants____: __`currentcolor`__: The value of the element’s `color` property.

__`-webkit-activelink`__: The default color of a hyperlink that is being clicked.

__`-webkit-focus-ring-color`__: The color that surrounds a UI element, such as a text field, that has focus.

__`-webkit-link`__: The default color of a hyperlink that has been visited.

__`-webkit-text`__: The default text color.

`activeborder`, `activecaption`, `appworkspace`, `aqua`, `background`, `black`, `blue`, `buttonface`, `buttonhighlight`, `buttonshadow`, `buttontext`, `captiontext`, `fuchsia`, `gray`, `graytext`, `green`, `grey`, `highlight`, `highlighttext`, `inactiveborder`, `inactivecaption`, `inactivecaptiontext`, `infobackground`, `infotext`, `lime`, `maroon`, `match`, `menu`, `menutext`, `navy`, `olive`, `orange`, `purple`, `red`, `scrollbar`, `silver`, `teal`, `threeddarkshadow`, `threedface`, `threedhighlight`, `threedlightshadow`, `threedshadow`, `transparent`, `white`, `window`, `windowframe`, `windowtext`, `yellow`

____Discussion____: If not specified, the color specified by the `color` property is used. `-webkit-text-stroke-color` is commonly used in combination with `-webkit-text-fill-color`. Changes to this property can be animated.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Apple extension.

Specifies the width for the text outline.

____Syntax____: |  |
```
-webkit-text-stroke-width: width
```

____Parameters____: ___width___: The width of the stroke.

____Types Allowed____: Length units

____Constants____: ___medium___: A medium stroke.

___thick___: A thick stroke.

___thin___: A thin stroke.

____Discussion____: This property is significant only in combination with `-webkit-text-stroke-color`.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Apple extension.

Specifies line-breaking rules for CJK (Chinese, Japanese, and Korean) text.

____Syntax____: |  |
```
-webkit-line-break: setting
```

____Parameters____: ___setting___: The line-breaking setting.

____Constants____: ___after-white-space___: The line breaks after white space.

___normal___: A standard line-breaking rule.

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-line-break` in Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Apple extension.

Changes the appearance of buttons and other controls to resemble native controls.

____Syntax____: |  |
```
-webkit-appearance: appearance
```

____Parameters____: ___appearance___: The appearance of the control.

____Constants____: __`caps-lock-indicator`__: The indicator that appears in a password field when Caps Lock is active.

Available in Safari 4.0 and later.

Available in iOS 2.0 and later

`button`, `button-bevel`, `caret`, `checkbox`, `default-button`, `listbox`, `listitem`, `media-fullscreen-button`, `media-mute-button`, `media-play-button`, `media-seek-back-button`, `media-seek-forward-button`, `media-slider`, `media-sliderthumb`, `menulist`, `menulist-button`, `menulist-text`, `menulist-textfield`, `none`, `push-button`, `radio`, `searchfield`, `searchfield-cancel-button`, `searchfield-decoration`, `searchfield-results-button`, `searchfield-results-decoration`, `slider-horizontal`, `slider-vertical`, `sliderthumb-horizontal`, `sliderthumb-vertical`, `square-button`, `textarea`, `textfield`

The following constants are unsupported in Safari 4.0:

`scrollbarbutton-down`, `scrollbarbutton-left`, `scrollbarbutton-right`, `scrollbarbutton-up`, `scrollbargripper-horizontal`, `scrollbargripper-vertical`, `scrollbarthumb-horizontal`, `scrollbarthumb-vertical`, `scrollbartrack-horizontal`, `scrollbartrack-vertical`

____Availability____: Available in Safari 3.0 and later.

Available in iOS 1.0 and later.

____Support Level____: Experimental CSS 3.

Defines the behavior of nonbreaking spaces within text.

____Syntax____: |  |
```
-webkit-nbsp-mode: behavior;
```

____Parameters____: ___behavior___: The behavior of nonbreaking spaces.

____Constants____: ___normal___: Nonbreaking spaces are treated as usual.

___space___: Nonbreaking spaces are treated like standard spaces.

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-nbsp-mode` in Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Apple extension.

Overrides ordering defaults for right-to-left content.

____Syntax____: |  |
```
-webkit-rtl-ordering: order;
```

____Parameters____: ___order___: The order of the content.

____Constants____: ___logical___: Raw content is in mixed order (requiring a bidirectional renderer).

___visual___: Right-to-left content is encoded in reverse order so an entire line of text can be rendered from left to right in a unidirectional fashion.

____Discussion____: The distinction between these two character orders is normally handled automatically as a side effect of character set. This property allows you to override whether the browser should treat the content as being in logical or visual order.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Apple extension.

Specifies that an entire element should be draggable instead of its contents.

____Syntax____: |  |
```
-webkit-user-drag: behavior;
```

____Parameters____: ___behavior___: The dragging behavior of the element.

____Constants____: ___auto___: The default dragging behavior is used.

___element___: The entire element is draggable instead of its contents.

___none___: The element cannot be dragged at all.

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-user-drag` in Safari 2.0.)

____Support Level____: Apple extension.

Determines whether a user can edit the content of an element.

____Syntax____: |  |
```
-webkit-user-modify: policy;
```

____Parameters____: ___policy___: The user modification policy.

____Constants____: ___read-only___: The content is read-only.

___read-write___: The content can be read and written.

___read-write-plaintext-only___: The content can be read and written, but any rich formatting of pasted text is lost.

____Discussion____: This is closely related to the `contentEditable` attribute.

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-user-modify` in Safari 2.0.)

Available in iOS 5.0 and later.

____Support Level____: Apple extension.

Determines whether a user can select the content of an element.

____Syntax____: |  |
```
-webkit-user-select: policy;
```

____Parameters____: ___policy___: The user selection policy.

____Constants____: ___auto___: The user can select content in the element.

___none___: The user cannot select any content.

___text___: The user can select text in the element.

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-user-select` in Safari 2.0.)

Available in iOS 3.0 and later.

____Support Level____: Apple extension.

Defines the model of an element’s border.

____Syntax____: |  |
```
border-collapse: behavior;
```

____Constants____: `collapse`, `separate`

____Support Level____: CSS 2.1.

Defines the spacing between an element’s border and the content within.

____Syntax____: |  |
```
border-spacing: length;
```

____Parameters____: ___length___: The size of the spacing.

____Subproperties____: - `[-webkit-border-horizontal-spacing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfvug64tjpjxw45dbnqwxg4dbmnuw4zy)`
- `[-webkit-border-vertical-spacing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn5zgizlsfv3gk4tunfrwc3bnonygcy3jnztq)`

____Support Level____: CSS 2.1.

Defines the side of a table on which its caption appears.

____Syntax____: |  |
```
caption-side: side;
```

____Parameters____: ___side___: The side of the table that will have a caption.

____Constants____: `bottom`, `left`, `right`, `top`

____Support Level____: CSS 2.1.

Sets the border behavior for cells with no content.

____Syntax____: |  |
```
empty-cells: behavior;
```

____Parameters____: ___behavior___: The behavior for cells with no content.

____Constants____: `hide`, `show`

____Support Level____: CSS 2.1.

Specifies whether to use automatic or fixed table layout.

____Syntax____: |  |
```
table-layout: behavior;
```

____Parameters____: ___behavior___: If `auto`, layout is determined by all cells in the table; if `fixed`, layout is determined by the first row of content only.

____Constants____: `auto`, `fixed`

____Discussion____: Automatic table layout, specified by the value `auto`, is the default table layout behavior. In this mode, the table layout is calculated based on the contents of every cell in every row of the table.

Fixed table layout, specified by the value `fixed`, is a faster (but more restrictive) layout behavior. In this layout mode, the layout of the table is calculated based only on the first row of tabular content (not including any heading rows). This mode allows the layout to be calculated much earlier in the page load process and greatly simplifies the calculations, but can cause content in later rows to overflow the table’s boundaries.

____Support Level____: CSS 2.1.

Defines the spacing between the horizontal portion of an element’s border and the content within.

____Syntax____: |  |
```
-webkit-border-horizontal-spacing: value;
```

____Parameters____: ___value___: The amount of horizontal spacing.

____Types Allowed____: Length units, nonnegative values

____Discussion____: Equivalent to the horizontal portion of the border-spacing property. Changes to this property can be animated.

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-border-horizontal-spacing` in Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Apple extension.

Defines the spacing between the vertical portion of an element’s border and the content within.

____Syntax____: |  |
```
-webkit-border-vertical-spacing: value;
```

____Parameters____: ___value___: The amount of vertical spacing.

____Types Allowed____: Length units, nonnegative values

____Discussion____: Equivalent to the vertical portion of the border-spacing property. Changes to this property can be animated.

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-border-vertical-spacing` in Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Apple extension.

Determines whether a column break can and should occur after an element in a multicolumn flow layout.

____Syntax____: |  |
```
-webkit-column-break-after: policy;
```

____Parameters____: ___policy___: The column break policy.

____Constants____: ___always___: A column break is always inserted after the element.

___auto___: A right column break is inserted after the element where appropriate.

___avoid___: Column breaks are avoided after the element.

___left___: A left column break is inserted after the element.

___right___: A right column break is inserted after the element.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Under development.

Determines whether a column break can and should occur before an element in a multicolumn flow layout.

____Syntax____: |  |
```
-webkit-column-break-before: policy;
```

____Parameters____: ___policy___: The column break policy.

____Constants____: ___always___: A column break is always inserted before the element.

___auto___: A right column break is inserted before the element where appropriate.

___avoid___: Column breaks are avoided before the element.

___left___: A left column break is inserted before the element.

___right___: A right column break is inserted before the element.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Under development.

Determines whether a column break should be avoided within the bounds of an element in a multicolumn flow layout.

____Syntax____: |  |
```
-webkit-column-break-inside: policy;
```

____Parameters____: ___policy___: The column break policy.

____Constants____: ___auto___: A right column break is inserted within the element where appropriate.

___avoid___: Column breaks are avoided within the element.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Under development.

Specifies the number of columns desired in a multicolumn flow.

____Syntax____: |  |
```
-webkit-column-count: number_of_columns;
```

____Parameters____: ___number_of_columns___: The number of columns in the multicolumn flow.

____Types Allowed____: Integers, nonnegative values

____Constants____: ___auto___: The element has one column.

____Discussion____: Changes to this property can be animated.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Under development.

Specifies the space between columns in a multicolumn flow.

____Syntax____: |  |
```
-webkit-column-gap: width;
```

____Parameters____: ___width___: The width of the gap.

____Types Allowed____: Length units

____Constants____: ___normal___: Columns in the element have the normal gap width between them.

____Discussion____: Changes to this property can be animated.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Under development.

Specifies the color, style, and width of the column rule.

____Syntax____: |  |
```
-webkit-column-rule: width style color;
```

____Parameters____: ___width___: The width of the column rule.

___style___: The style of the column rule.

___color___: The color of the column rule.

____Subproperties____: - `[-webkit-column-rule-color](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxilldn5whk3lofvzhk3dffvrw63dpoi)`
- `[-webkit-column-rule-style](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxilldn5whk3lofvzhk3dffvzxi6lmmu)`
- `[-webkit-column-rule-width](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxilldn5whk3lofvzhk3dffv3wszduna)`

____Discussion____: The column rule appears in the middle of the column gap in a multicolumn flow layout.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Under development.

Specifies the color of the column rule.

____Syntax____: |  |
```
-webkit-column-rule-color: color;
```

____Parameters____: ___color___: The color of the column rule.

____Constants____: __`currentcolor`__: The value of the element’s `color` property.

__`-webkit-activelink`__: The default color of a hyperlink that is being clicked.

__`-webkit-focus-ring-color`__: The color that surrounds a UI element, such as a text field, that has focus.

__`-webkit-link`__: The default color of a hyperlink that has been visited.

__`-webkit-text`__: The default text color.

`activeborder`, `activecaption`, `appworkspace`, `aqua`, `background`, `black`, `blue`, `buttonface`, `buttonhighlight`, `buttonshadow`, `buttontext`, `captiontext`, `fuchsia`, `gray`, `graytext`, `green`, `grey`, `highlight`, `highlighttext`, `inactiveborder`, `inactivecaption`, `inactivecaptiontext`, `infobackground`, `infotext`, `lime`, `maroon`, `match`, `menu`, `menutext`, `navy`, `olive`, `orange`, `purple`, `red`, `scrollbar`, `silver`, `teal`, `threeddarkshadow`, `threedface`, `threedhighlight`, `threedlightshadow`, `threedshadow`, `transparent`, `white`, `window`, `windowframe`, `windowtext`, `yellow`

____Discussion____: Changes to this property can be animated.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Under development.

Specifies the style of the column rule.

____Syntax____: |  |
```
-webkit-column-rule-style: style;
```

____Parameters____: ___style___: The style of the column rule.

____Constants____: ___dashed___: The column rule has a dashed line style.

___dotted___: The column rule has a dotted line style.

___double___: The column rule has a double solid line style.

___groove___: The column rule has a grooved style.

___hidden___: The column rule is hidden.

___inset___: The column rule has an inset style.

___none___: The column rule has no style.

___outset___: The column rule has an outset style.

___ridge___: The column rule has a ridged style.

___solid___: The column rule has a solid line style.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Under development.

Specifies the width of the column rule.

____Syntax____: |  |
```
-webkit-column-rule-width: width;
```

____Parameters____: ___width___: The width of the column rule.

____Types Allowed____: Length units

____Constants____: ___medium___: The column rule has a medium width.

___thick___: The column rule has a thick width.

___thin___: The column rule has a thin width.

____Discussion____: Changes to this property can be animated.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Under development.

Specifies the width of the column in a multicolumn flow.

____Syntax____: |  |
```
-webkit-column-width: width;
```

____Parameters____: ___width___: The width of the column.

____Types Allowed____: Length units

____Constants____: ___auto___: Columns in the element are of normal width.

____Discussion____: Changes to this property can be animated.

____Availability____: Available in Safari 3.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Under development.

A composite property that specifies the width and number of columns in a multicolumn flow layout.

____Syntax____: |  |
```
-webkit-columns: width count
```

____Parameters____: ___width___: The width of each column.

___count___: The number of columns.

____Subproperties____: - `[-webkit-column-count](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxilldn5whk3lofvrw65looq)`
- `[-webkit-column-width](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxilldn5whk3lofv3wszduna)`

____Availability____: Available in Safari 3.0 and later.

Available in iOS 2.0 and later.

____Support Level____: Under development.

Defines the cursor to display onscreen when the pointer is over an element.

____Syntax____: |  |
```
cursor: style;
```

____Parameters____: ___style___: The type of cursor.

____Constants____: ___-webkit-grab___: An open hand cursor indicating the element can be grabbed.

___-webkit-grabbing___: A closed hand cursor indicating the element has been grabbed.

___-webkit-zoom-in___: A zoom-in cursor.

___-webkit-zoom-out___: A zoom-out cursor.

`alias`, `all-scroll`, `auto`, `cell`, `col-resize`, `context-menu`, `copy`, `crosshair`, `default`, `e-resize`, `ew-resize`, `hand`, `help`, `move`, `n-resize`, `ne-resize`, `nesw-resize`, `no-drop`, `none`, `not-allowed`, `ns-resize`, `nw-resize`, `nwse-resize`, `pointer`, `progress`, `row-resize`, `s-resize`, `se-resize`, `sw-resize`, `text`, `vertical-text`, `w-resize`, `wait`

____Discussion____: Although the CSS specification allows it, Safari does not support custom cursors.

____Availability____: Available in Safari 1.2 and later.

____Support Level____: CSS 2.1.

Defines a variety of properties for an element’s outline (drawn outside the element’s border) within one declaration.

____Syntax____: |  |
```
outline: color style width;
```

____Parameters____: ___color___: The color of the outline.

___style___: The style of the outline.

___width___: The width of the outline.

____Subproperties____: - `[outline-color](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvxxk5dmnfxgklldn5wg64q)`
- `[outline-style](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvxxk5dmnfxgklltor4wyzi)`
- `[outline-width](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfvxxk5dmnfxgkllxnfshi2a)`

____Support Level____: CSS 2.1.

Defines the color of an element’s outline.

____Syntax____: |  |
```
outline-color: color;
```

____Parameters____: ___color___: The color of the outline.

____Constants____: ___-webkit-focus-ring-color___: The color that surrounds a UI element, such as a text field, that has focus.

`invert`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the offset of an element’s outline from its border.

____Syntax____: |  |
```
outline-offset: length;
```

____Parameters____: ___length___: The size of the offset.

____Types Allowed____: Length units

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the style of an element’s outline.

____Syntax____: |  |
```
outline-style: value;
```

____Parameters____: ___value___: The style of the outline.

____Constants____: `auto`

____Support Level____: CSS 2.1.

Defines the width of an element's outline.

____Syntax____: |  |
```
outline-width: value;
```

____Parameters____: ___value___: The width of the outline.

____Types Allowed____: Length units

____Constants____: `medium`, `thick`, `thin`

____Discussion____: Changes to this property can be animated.

____Support Level____: CSS 2.1.

Defines the parts of an element that responds to pointer events, such as a click, mouse over, or hover.

____Syntax____: |  |
```
pointer-events: value;
```

____Parameters____: ___value___: The parts of the element that respond to pointer events.

____Constants____: __`auto`__: The entire element responds to pointer events.

__`none`__: The element does not respond to pointer events.

____Discussion____: Providing a value of `none` does not disable the Inspect Element option that appears when the element is Control-clicked, however the option may return the wrong element.

____Availability____: Available in Safari 4.0 and later.

____Support Level____: Apple extension.

Specifies the alignment of nested elements within an outer flexible box element.

____Syntax____: |  |
```
-webkit-box-align: alignment;
```

____Parameters____: ___alignment___: The alignment of nested elements.

____Constants____: ___baseline___: Elements are aligned with the baseline of the box.

___center___: Elements are aligned with the center of the box.

___end___: Elements are aligned with the end of the box.

___start___: Elements are aligned with the start of the box.

___stretch___: Elements are stretched to fill the box.

____Discussion____: This property specifies the horizontal alignment if the box direction is vertical, and vice versa. This property applies only to flexible box layouts. For more information about flexible boxes, see [http://www.w3.org/TR/css3-layout/](http://www.w3.org/TR/css3-layout/).

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-box-align` in Safari 1.1 through Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Under development.

Specifies the direction in which child elements of a flexible box element are laid out.

____Syntax____: |  |
```
-webkit-box-direction: layout_direction;
```

____Parameters____: ___layout_direction___: The layout direction.

____Constants____: ___normal___: Elements are laid out in the default direction.

___reverse___: Elements are laid out in the reverse direction.

____Discussion____: This applies only to flexible box layouts. For more information about flexible boxes, see [http://www.w3.org/TR/css3-layout/](http://www.w3.org/TR/css3-layout/).

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-box-direction` in Safari 1.1 through Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Under development.

Specifies an element’s flexibility.

____Syntax____: |  |
```
-webkit-box-flex: flex_value;
```

____Parameters____: ___flex_value___: The flexibility of the element.

____Types Allowed____: Floating-point numbers

____Discussion____: Flexible elements can stretch or shrink to fit the size of the bounding box of their parent element. The amount of stretching or shrinkage of an element is determined by its flex value relative to the flex values of other elements within the same parent element.

This property applies only to flexible box layouts. For more information about flexible boxes, see [http://www.w3.org/TR/css3-layout/](http://www.w3.org/TR/css3-layout/).

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-box-flex` in Safari 1.1 through Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Under development.

Specifies groups of dynamically resizing elements that are adjusted to be the same size.

____Syntax____: |  |
```
-webkit-box-flex-group: group_number;
```

____Parameters____: ___group_number___: The group number of the flexible element.

____Types Allowed____: Integers, nonnegative values

____Discussion____: During size adjustment of flex boxes, any boxes with the same group number are adjusted to be the same size.

This property applies only to flexible box layouts. For more information about flexible boxes, see [http://www.w3.org/TR/css3-layout/](http://www.w3.org/TR/css3-layout/).

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-box-flex-group` in Safari 1.1 through Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Under development.

Specifies whether a flexible box should contain multiple lines of content.

____Syntax____: |  |
```
-webkit-box-lines: behavior;
```

____Parameters____: ___behavior___: If `multiple`, the flexible box can contain multiple lines of content; if `single`, only one line is allowed.

____Constants____: ___multiple___: The box can contain multiple lines of content.

___single___: The box can contain only one line of content.

____Discussion____: This property applies only to flexible box layouts. For more information about flexible boxes, see [http://www.w3.org/TR/css3-layout/](http://www.w3.org/TR/css3-layout/).

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-box-lines` in Safari 1.1 through Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Under development.

Specifies a rough ordering of elements in a flexible box.

____Syntax____: |  |
```
-webkit-box-ordinal-group: group_number;
```

____Parameters____: ___group_number___: The ordinal group number of the element.

____Types Allowed____: Integers, nonnegative values

____Discussion____: Elements with lower ordinal group values are displayed first.

This property applies only to flexible box layouts. For more information about flexible boxes, see [http://www.w3.org/TR/css3-layout/](http://www.w3.org/TR/css3-layout/).

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-box-ordinal-group` in Safari 1.1 through Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Under development.

Specifies the layout of elements nested within a flexible box element.

____Syntax____: |  |
```
-webkit-box-orient: orientation;
```

____Parameters____: ___orientation___: The orientation of elements nested in the flexible box.

____Constants____: ___block-axis___: Elements are oriented along the box’s axis.

___horizontal___: Elements are oriented horizontally.

___inline-axis___: Elements are oriented along the inline axis.

___vertical___: Elements are oriented vertically.

____Discussion____: This property applies only to flexible box layouts. For more information about flexible boxes, see [http://www.w3.org/TR/css3-layout/](http://www.w3.org/TR/css3-layout/).

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-box-orient` in Safari 1.1 through Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Under development.

Specifies alignment of child elements within the current element in the direction of orientation.

____Syntax____: |  |
```
-webkit-box-pack: alignment;
```

____Parameters____: ___alignment___: The alignment of child elements.

____Constants____: ___center___: Child elements are aligned to the center of the element.

___end___: Child elements are aligned to the end of the element.

___justify___: Child elements are justified with both the start and end of the element.

___start___: Child elements are aligned to the start of the element.

____Discussion____: For elements whose children are aligned horizontally, a packing value of `start` indicates left alignment with extra space towards the right side, a value of `end` indicates right alignment with extra space to the left, a value of `center` indicates center alignment with extra space split evenly on either side, and a value of `justify` indicates that the outer elements should be aligned on the left and right, with space added evenly between the elements.

Similarly, for elements whose children are aligned vertically, a value of `start` indicates that the elements should be aligned to the top, a value of `end` indicates that the elements should be aligned to the bottom, and so on.

This property is similar to `[-webkit-box-align](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytenrwfuwxozlcnnuxillcn54c2ylmnftw4)`, which specifies alignment in the opposite direction from the direction of orientation.

This property applies only to flexible box layouts. For more information about flexible boxes, see [http://www.w3.org/TR/css3-layout/](http://www.w3.org/TR/css3-layout/).

____Availability____: Available in Safari 3.0 and later. (Called `-khtml-box-pack` in Safari 1.1 through Safari 2.0.)

Available in iOS 1.0 and later.

____Support Level____: Under development.

Specifies the behavior of regions in a Dashboard widget.

____Syntax____: |  |
```
-webkit-dashboard-region:
            dashboard-region( ... )
            [...]
```

____Constants____: ___none___: No behavior is specified.

____Discussion____: This property is described in more detail in [Declaring Control Regions](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/Articles/ControlRegions.html#//apple_ref/doc/uid/TP40003045) in _[Dashboard Programming Topics](../Dashboard%20Programming%20Topics/Introduction%20to%20Dashboard%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqmzx)_.

____Availability____: Available in Safari 3.0 and later. (Called `-apple-dashboard-region` in Safari 2.0.)

____Support Level____: Apple extension—Dashboard only.

Specifies whether to use native-style scrolling in an overflow:scroll element.

____Syntax____: |  |
```
-webkit-overflow-scrolling: value
```

____Parameters____: ___value___: The style of scrolling.

____Constants____: ___auto___: One finger scrolling without momentum.

___touch___: Native-style scrolling. Specifying this style has the effect of creating a stacking context (like opacity, masks, and transforms).

____Discussion____: The default value is `auto`.

____Availability____: Available in iOS 5.0 and later.

____Support Level____: Under development.

Overrides the highlight color shown when the user taps a link or a JavaScript clickable element in Safari on iOS.

____Syntax____: |  |
```
-webkit-tap-highlight-color: color;
```

____Parameters____: ___color___: The tapped link color.

____Discussion____: This property obeys the alpha value, if specified. If you don’t specify an alpha value, Safari on iOS applies a default alpha value to the color. To disable tap highlighting, set the alpha value to `0` (invisible). If you set the alpha value to `1.0` (opaque), the element is not visible when tapped.

____Availability____: Available in iOS 1.1.1 and later.

____Support Level____: Apple extension—Safari on iOS only.

Disables the default callout shown when you touch and hold a touch target.

____Syntax____: |  |
```
-webkit-touch-callout: behavior;
```

____Parameters____: ___behavior___: The touch callout behavior.

____Discussion____: On iOS, when you touch and hold a touch target such as a link, Safari displays a callout containing information about the link. This property allows you to disable that callout.

The current allowable values are _none_ and `inherit`.

____Availability____: Available in iOS 2.0 and later.

____Support Level____: Apple extension—Safari on iOS only.

WebKit provides partial support for a number of properties that are not supported for developer use. This list may include:

- Properties designed for Apple internal use, such as properties specific to the way Mail and other applications use WebKit.
- Properties that are in a very early stage of development and are not really usable yet.
- Properties that are used within WebKit itself and cannot be parsed in a CSS file.
- Properties that are parsed for historical reasons, but that are not actually used.

Because these properties are unsupported, they are not documented in detail. However, they are listed here so that if you find them in the source code, in test cases, and so on, you will be able to determine their status.

- `-webkit-border-fit`
- `-webkit-font-size-delta`
- `-webkit-highlight`
- `-webkit-line-clamp`
- `-webkit-match-nearest-mail-blockquote-color`
- `-webkit-text-decorations-in-effect`
- `-webkit-transition-repeat-count`

- `font-size-adjust`—Describes the font aspect ratio to preserve proportionality in the event of font substitution. Unsupported CSS 2 property; removed in CSS 2.1; reintroduced in CSS 3.
- `font-stretch`—Selects a normal, condensed, or extended variant of a font in an element or describes availability of these variants in a font definition. Declared in CSS 2.1/CSS 3.
- `marker-offset`—Sets the offset of a marker (a bullet in a bulleted list, for example). Unsupported CSS 2 property; removed in CSS 2.1.
- `marks`—Sets what type of crop marks to use on paged media. Unsupported CSS 2 property; removed in CSS 2.1.
- `page`—Used for named page support. Unsupported CSS 2 property; removed in CSS 2.1.
- `quotes`—Sets the quotation mark characters used for nested <q> tags.
- `size`—Sets page dimensions for paged media. Unsupported CSS 2 property; removed in CSS 2.1.
- `speak-header`—Sets whether a browser should speak the contents of the corresponding table heading cell before speaking the contents of each cell. Unsupported CSS 2 aural media property. Aural media deprecated in CSS 2.1. Property reintroduced in CSS 3
- `text-line-through`—Composite property describing overstrike color, style, and mode. Declared in CSS 3.
- `text-line-through-color`—Describes color for overstrike. Declared in CSS 3.
- `text-line-through-mode`—Describes the mode for overstrike. Declared in CSS 3.
- `text-line-through-style`—Describes the style for overstrike. Declared in CSS 3.
- `text-line-through-width`—Describes the width for overstrike. Declared in CSS 3.
- `text-overline`—Composite property describing overline color, style, mode, and width(like underline, but above the text). Declared in CSS 3.
- `text-overline-color`—Describes the color of overline (like underline, but above the text). Declared in CSS 3.
- `text-overline-mode`—Describes the mode of overline (like underline, but above the text). Declared in CSS 3.
- `text-overline-style`—Describes the style of overline (like underline, but above the text). Declared in CSS 3.
- `text-overline-width`—Describes the width of overline (like underline, but above the text). Declared in CSS 3.
- `text-underline`—Composite property describing underline color, style, mode, and width. Declared in CSS 3.
- `text-underline-color`—Describes the color of underline. Declared in CSS 3.
- `text-underline-mode`—Describes the mode of underline. Declared in CSS 3.
- `text-underline-style`—Describes the style of underline. Declared in CSS 3.
- `text-underline-width`—Describes the width of underline. Declared in CSS 3.

- `scrollbar-3dlight-color`—Microsoft Internet Explorer property.
- `scrollbar-arrow-color`—Microsoft Internet Explorer property.
- `scrollbar-darkshadow-color`—Microsoft Internet Explorer property.
- `scrollbar-face-color`—Microsoft Internet Explorer property.
- `scrollbar-highlight-color`—Microsoft Internet Explorer property.
- `scrollbar-shadow-color`—Microsoft Internet Explorer property.
- `scrollbar-track-color`—Microsoft Internet Explorer property.

[Next](Supported%20CSS%20Rules.md)[Previous](Explanation%20of%20Terms.md)

