---
title: 'rect(cornerRadius:style:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/rect(cornerradius:style:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/rect(cornerradius:style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/rect%28cornerradius%3Astyle%3A%29.json'
content_hash: 'sha256:aba26c16f925a5a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# rect(cornerRadius:style:)

<sub>Type Method</sub>

A rectangular shape with rounded corners, aligned inside the frame of the view containing it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func rect(cornerRadius: CGFloat, style: RoundedCornerStyle = .continuous) -> Self
```

## See Also

### Getting rectangles

- [rect](rect.md) — A rectangular shape aligned inside the frame of the view containing it.
- [rect(cornerRadii:style:)](<rect(cornerradii_style_).md>) — A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [rect(corners:isUniform:)](<rect(corners_isuniform_).md>) — Creates a rectangle with the same corner style set on four corners.
- [rect(cornerSize:style:)](<rect(cornersize_style_).md>) — A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [rect(topLeadingCorner:topTrailingCorner:bottomLeadingCorner:bottomTrailingCorner:)](<rect(topleadingcorner_toptrailingcorner_bottomleadingcorner_bottomtrailingcorner_).md>) — Creates a rectangle with individual styles for each corner.
- [rect(topLeadingRadius:bottomLeadingRadius:bottomTrailingRadius:topTrailingRadius:style:)](<rect(topleadingradius_bottomleadingradius_bottomtrailingradius_toptrailingradius_style_).md>) — A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [rect(uniformBottomCorners:topLeadingCorner:topTrailingCorner:)](<rect(uniformbottomcorners_topleadingcorner_toptrailingcorner_).md>) — Creates a rectangle with a corner style set on the two bottom corners uniformly, and two other styles for the two top corners respectively.
- [rect(uniformLeadingCorners:topTrailingCorner:bottomTrailingCorner:)](<rect(uniformleadingcorners_toptrailingcorner_bottomtrailingcorner_).md>) — Creates a rectangle with a corner style uniformly set on the two leading corners, and two other styles for the two trailing corners respectively.
- [rect(uniformLeadingCorners:uniformTrailingCorners:)](<rect(uniformleadingcorners_uniformtrailingcorners_).md>) — Creates a rectangle with a corner style uniformly set on the two leading corners, and another style uniformly set on the two trailing corners.
- [rect(uniformTopCorners:bottomLeadingCorner:bottomTrailingCorner:)](<rect(uniformtopcorners_bottomleadingcorner_bottomtrailingcorner_).md>) — Creates a rectangle with a corner style uniformly set on the two top corners, and two other styles for the bottom two corners respectively.
- [rect(uniformTopCorners:uniformBottomCorners:)](<rect(uniformtopcorners_uniformbottomcorners_).md>) — Creates a rectangle with a corner style uniformly set on the two top corners, and another style uniformly set on the two bottom corners.
- [rect(uniformTrailingCorners:topLeadingCorner:bottomLeadingCorner:)](<rect(uniformtrailingcorners_topleadingcorner_bottomleadingcorner_).md>) — Creates a rectangle with a corner style uniformly set on the two trailing corners, and two other styles for the two leading corners respectively.
